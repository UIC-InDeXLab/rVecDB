"""AwA2 loading: metadata, facet scores, splits. Reads straight from the zip."""
import io
import os
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd

from .taxonomy_awa2 import TAXONOMY, LEVELS, HABITAT_PREDICATES, DIET_PREDICATES

ROOT = Path(__file__).resolve().parent.parent
ZIP_PATH = ROOT / "data/awa2/AwA2-data.zip"
CACHE = Path(os.environ.get("SSE_CACHE", ROOT / "cache/awa2"))
CACHE.mkdir(parents=True, exist_ok=True)


def _find(names, suffix):
    hits = [n for n in names if n.endswith(suffix)]
    assert len(hits) == 1, (suffix, hits[:5])
    return hits[0]


def _read_list(zf, name):
    rows = zf.read(name).decode().strip().splitlines()
    return [r.split()[-1].strip() for r in rows if r.strip()]


def _load_meta_raw(seed=0, seen_test_frac=0.2):
    """Return (images DataFrame, classes DataFrame).

    images: path, cls, split in {train, seen_test, unseen}
    classes: cls, order, family, genus, unseen(bool), habitat scores, diet scores
    """
    out_img, out_cls = CACHE / "images.parquet", CACHE / "classes.pkl"
    if out_img.exists() and out_cls.exists():
        return pd.read_parquet(out_img), pd.read_pickle(out_cls)

    zf = zipfile.ZipFile(ZIP_PATH)
    names = zf.namelist()
    classes = _read_list(zf, _find(names, "/classes.txt"))
    predicates = _read_list(zf, _find(names, "/predicates.txt"))
    cont = np.loadtxt(io.BytesIO(zf.read(_find(names, "/predicate-matrix-continuous.txt"))))
    test_classes = set(_read_list(zf, _find(names, "/testclasses.txt")))
    assert cont.shape == (len(classes), len(predicates))

    p_idx = {p: i for i, p in enumerate(predicates)}
    cls_df = pd.DataFrame({"cls": classes})
    for lvl_i, lvl in enumerate(LEVELS):
        cls_df[lvl] = [TAXONOMY[c][lvl_i] for c in classes]
    cls_df["unseen"] = [c in test_classes for c in classes]
    cls_df["habitat"] = list(cont[:, [p_idx[p] for p in HABITAT_PREDICATES]] / 100.0)
    cls_df["diet"] = list(cont[:, [p_idx[p] for p in DIET_PREDICATES]] / 100.0)

    imgs = sorted(n for n in names if "/JPEGImages/" in n and n.lower().endswith(".jpg"))
    img_df = pd.DataFrame({"path": imgs, "cls": [n.split("/")[-2] for n in imgs]})
    rng = np.random.default_rng(seed)
    split = np.where(img_df.cls.isin(test_classes), "unseen", "train").astype(object)
    seen = np.flatnonzero(split == "train")
    held = rng.choice(seen, size=int(len(seen) * seen_test_frac), replace=False)
    split[held] = "seen_test"
    img_df["split"] = split

    img_df.to_parquet(out_img)
    cls_df.to_pickle(out_cls)
    return img_df, cls_df


VAL_UNSEEN_CLASSES = 5
VAL_SEEN_FRAC = 0.15


def load_meta():
    """Normal mode: splits train / seen_test / unseen (the real test data).

    Validation mode (environment SSE_VAL=1), for choosing settings WITHOUT looking at test:
      - 5 of the 40 training species become 'unseen'  (validation-unseen)
      - 15% of the remaining training images become 'seen_test'  (validation-seen)
      - the real test images become 'heldout' and are never touched
    """
    img_df, cls_df = _load_meta_raw()
    if os.environ.get("SSE_VAL") != "1":
        return img_df, cls_df
    img_df, cls_df = img_df.copy(), cls_df.copy()
    rng = np.random.default_rng(123)
    train_classes = sorted(cls_df.cls[~cls_df.unseen])
    val_unseen = set(rng.choice(train_classes, VAL_UNSEEN_CLASSES, replace=False))
    split = np.where(img_df.split.values == "train", "train", "heldout").astype(object)
    split[img_df.cls.isin(val_unseen).values & (split == "train")] = "unseen"
    tr = np.flatnonzero(split == "train")
    split[rng.choice(tr, int(len(tr) * VAL_SEEN_FRAC), replace=False)] = "seen_test"
    img_df["split"] = split
    cls_df["unseen"] = cls_df.cls.isin(val_unseen) | cls_df.unseen   # never in any training vocabulary
    print("VALIDATION MODE — val-unseen classes:", sorted(val_unseen), flush=True)
    return img_df, cls_df


class ZipImages:
    """torch Dataset over images inside the zip (one ZipFile handle per worker)."""

    def __init__(self, paths, transform):
        self.paths, self.transform, self._zf = list(paths), transform, None

    def __len__(self):
        return len(self.paths)

    def __getitem__(self, i):
        from PIL import Image
        if self._zf is None:
            self._zf = zipfile.ZipFile(ZIP_PATH)
        img = Image.open(io.BytesIO(self._zf.read(self.paths[i]))).convert("RGB")
        return self.transform(img)
