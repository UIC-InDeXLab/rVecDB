"""Baselines that need little or no training: B6 plain CLIP, B2 CLIP+text, B1 labels (+B1-soft).

Every method is a dict of "views". A view is (matrix, kind):
  kind "cos"    : cosine similarity between rows
  kind "jacc"   : Jaccard between binary rows (predicted yes/no labels)
  kind "taxlab" : matrix of [order_code, family_code, tiebreak_vec...] -> label agreement (B1)
Views used: habitat, diet, family (ranking at Family level), full (general search).
"""
import numpy as np
import torch
import torch.nn.functional as F

from .awa2 import load_meta, CACHE
from .taxonomy_awa2 import LEVELS


def _center_cos(m):
    return m - m.mean(0, keepdims=True)


def b6_clip(X):
    return {"habitat": (X, "cos"), "diet": (X, "cos"), "family": (X, "cos"), "full": (X, "cos")}


def b2_text(X):
    T = np.load(CACHE / "clip_text.npz")
    return {
        "habitat": (_center_cos(X @ T["habitat"].T), "cos"),
        "diet": (_center_cos(X @ T["diet"].T), "cos"),
        "family": (_center_cos(X @ T["family"].T), "cos"),
        "full": (X, "cos"),
    }


def _train_probe(Xtr, Ytr, multilabel, epochs=60, dev="cuda"):
    Xtr = torch.tensor(Xtr, device=dev)
    Ytr = torch.tensor(Ytr, device=dev)
    n_out = Ytr.shape[1] if multilabel else int(Ytr.max()) + 1
    lin = torch.nn.Linear(Xtr.shape[1], n_out).to(dev)
    opt = torch.optim.AdamW(lin.parameters(), lr=1e-3, weight_decay=1e-4)
    for _ in range(epochs):
        perm = torch.randperm(len(Xtr), device=dev)
        for i in range(0, len(Xtr), 1024):
            b = perm[i:i + 1024]
            out = lin(Xtr[b])
            loss = (F.binary_cross_entropy_with_logits(out, Ytr[b].float()) if multilabel
                    else F.cross_entropy(out, Ytr[b].long()))
            opt.zero_grad(); loss.backward(); opt.step()
    return lin


@torch.no_grad()
def _predict(lin, X, multilabel, dev="cuda"):
    out = lin(torch.tensor(X, device=dev))
    return (torch.sigmoid(out) if multilabel else torch.softmax(out, -1)).cpu().numpy()


def b1_labels(X, img_df, cls_df, return_order=False):
    """Train classifiers on the train split (same labels SSE sees), then build label views.

    Returns (B1 hard-label method, B1-soft method, label accuracy info).
    """
    tr = img_df.split.values == "train"
    ci = img_df.cls.map({c: i for i, c in enumerate(cls_df.cls)}).values
    hab = np.stack(cls_df.habitat.values)[ci] >= 0.5
    diet = np.stack(cls_df.diet.values)[ci] >= 0.5

    p_hab = _predict(_train_probe(X[tr], hab[tr], True), X, True)
    p_diet = _predict(_train_probe(X[tr], diet[tr], True), X, True)

    # Taxonomy classifiers: vocabulary = labels present in the training classes only.
    codes, probs = {}, {}
    for lvl in LEVELS:
        vocab = sorted(cls_df.loc[~cls_df.unseen, lvl].unique())
        y = img_df.cls.map(dict(zip(cls_df.cls, cls_df[lvl]))).values
        y_tr = np.array([vocab.index(v) for v in y[tr]])
        probs[lvl] = _predict(_train_probe(X[tr], y_tr, False), X, False)
        codes[lvl] = probs[lvl].argmax(1)

    taxlab = np.concatenate([codes["order"][:, None], codes["family"][:, None], X], 1)
    hard = {"habitat": ((p_hab >= 0.5).astype(np.float32), "jacc"),
            "diet": ((p_diet >= 0.5).astype(np.float32), "jacc"),
            "family": (taxlab, "taxlab"), "full": (X, "cos")}
    soft = {"habitat": (p_hab, "cos"), "diet": (p_diet, "cos"),
            "family": (probs["family"], "cos"), "full": (X, "cos")}
    if return_order:
        return hard, soft, codes["order"], probs["order"]
    return hard, soft


def sse_views(E, L, prefix="family"):
    plen = L["prefix"][prefix]
    return {"habitat": (E[:, slice(*L["habitat"])], "cos"),
            "diet": (E[:, slice(*L["diet"])], "cos"),
            "family": (E[:, :plen], "cos"),
            "tax": (E[:, slice(*L["tax"])], "cos"),
            "rest": (E[:, slice(*L["rest"])], "cos"),
            "full": (E, "cos")}
