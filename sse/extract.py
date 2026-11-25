"""Compute frozen CLIP ViT-L/14 image features for AwA2, plus text features for B2.

Usage: .venv/bin/python -m sse.extract
Writes cache/awa2/clip_img.npy (N x 768, float16, L2-normalised) and cache/awa2/clip_text.npz
"""
import os

import numpy as np
import torch
from torch.utils.data import DataLoader
from tqdm import tqdm
import open_clip

from .awa2 import load_meta, ZipImages, CACHE
from .taxonomy_awa2 import HABITAT_PREDICATES, DIET_PREDICATES

HABITAT_PROMPT = {
    "arctic": "in the arctic snow and ice", "coastal": "on a coast", "desert": "in a desert",
    "bush": "in the bush", "plains": "on open plains", "forest": "in a forest",
    "fields": "in fields", "jungle": "in a jungle", "mountains": "in the mountains",
    "ocean": "in the ocean", "ground": "on the ground", "water": "in water",
    "tree": "in a tree", "cave": "in a cave",
}
DIET_PROMPT = {
    "fish": "eats fish", "meat": "eats meat", "plankton": "eats plankton",
    "vegetation": "eats plants", "insects": "eats insects",
}


@torch.no_grad()
def main():
    img_df, cls_df = load_meta()
    print(img_df.split.value_counts().to_dict())
    dev = "cuda"
    # default = the paper's encoder; CLIP_MODEL=EVA02-L-14 CLIP_PRETRAINED=merged2b_s4b_b131k SSE_CACHE=cache/awa2_eva
    # gives the EVA-CLIP features (same 768-d output) for the encoder study
    name, pre = os.environ.get("CLIP_MODEL", "ViT-L-14"), os.environ.get("CLIP_PRETRAINED", "openai")
    model, _, preprocess = open_clip.create_model_and_transforms(name, pretrained=pre)
    model = model.to(dev).eval().half()
    tok = open_clip.get_tokenizer(name)
    print("encoder", name, pre, flush=True)

    out = CACHE / "clip_img.npy"
    if not out.exists():
        dl = DataLoader(ZipImages(img_df.path, preprocess), batch_size=256, num_workers=24)
        feats = []
        for x in tqdm(dl, desc="clip images"):
            f = model.encode_image(x.to(dev).half())
            feats.append(torch.nn.functional.normalize(f.float(), dim=-1).cpu().half())
        np.save(out, torch.cat(feats).numpy())

    def enc(texts):
        f = model.encode_text(tok(texts).to(dev))
        return torch.nn.functional.normalize(f.float(), dim=-1).cpu().numpy()

    text = {
        "habitat": enc([f"a photo of an animal that lives {HABITAT_PROMPT[p]}." for p in HABITAT_PREDICATES]),
        "diet": enc([f"a photo of an animal that {DIET_PROMPT[p]}." for p in DIET_PREDICATES]),
    }
    for lvl in ("order", "family", "genus"):
        names = sorted(cls_df[lvl].unique())
        text[lvl] = enc([f"a photo of an animal of the {lvl} {n}." for n in names])
        text[lvl + "_names"] = np.array(names)
    names = list(cls_df.cls.str.replace("+", " "))
    text["species"] = enc([f"a photo of a {n}." for n in names])          # text references (sse.awa2_extra textq)
    np.savez(CACHE / "clip_text.npz", **text)
    print("saved", out)


if __name__ == "__main__":
    main()
