"""B5 — ask an open vision-language model (Qwen2.5-VL-7B) about every candidate, LOTUS-style.

For Q1-type queries (E4): habitat filter with reference image x, Family ranking with reference image q.
The model sees TWO images, names both animals, then answers; the score is P(Yes) at its final answer token:
  habitat: "Do these two animals typically live in similar natural habitats?"     (x vs candidate)
  family : "Do these two animals belong to the same biological family?"         (q vs candidate)

Sample: 50 queries x 200 candidate images each (same pools for every method, so the comparison is fair).
Scores are cached and the run can resume. Progress lines go to logs/PROGRESS.md every 10%.

Usage: .venv/bin/python -m sse.b5_vlm score      # run the model (slow part)
       .venv/bin/python -m sse.b5_vlm evaluate   # compare all methods on the same pools
"""
import io
import json
import sys
import time
import zipfile
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import torch

from .awa2 import load_meta, CACHE, ROOT, ZIP_PATH
from .evaluate import Scorer, truth, ndcg, ap, note

N_QUERIES, POOL, BATCH, MAX_NEW = 50, 200, 64, 90
MODEL = "Qwen/Qwen2.5-VL-7B-Instruct"
# "Name first, then answer": with a one-word answer the 7B model says "No" even to brown bear vs polar bear
# (it names both correctly but does not reason about taxonomy). Naming first fixes that (checked by hand).
PROMPTS = {
    "habitat": "Image 1 and Image 2 each show an animal. First name both animals. Then decide: do these two "
               "animals typically live in similar natural habitats? End your reply with exactly 'Answer: Yes' "
               "or 'Answer: No'.",
    "family": "Image 1 and Image 2 each show an animal. First name both animals. Then decide: do they belong "
              "to the same biological family (taxonomic rank 'family', e.g. Felidae, Canidae, Ursidae)? End your "
              "reply with exactly 'Answer: Yes' or 'Answer: No'.",
}
# Fairer graded version: a 0-10 rating instead of Yes/No (the answer key is graded too).
PROMPTS_RATING = {
    "habitat": "Image 1 and Image 2 each show an animal. First name both animals. Then rate how similar their "
               "typical natural habitats are, from 0 (completely different) to 10 (the same). End your reply with "
               "exactly 'Score: N' where N is an integer from 0 to 10.",
    "family": "Image 1 and Image 2 each show an animal. First name both animals. Then rate how closely related "
              "they are in the biological taxonomy, from 0 (different orders) to 5 (same order, different family) "
              "to 10 (same family). End your reply with exactly 'Score: N' where N is an integer from 0 to 10.",
}
MODE = "yesno"
SCORES = CACHE / "b5_scores.npz"
SCORES_RATING = CACHE / "b5_scores_rating.npz"
OUT = ROOT / "results/awa2/b5"


def workload():
    img_df, cls_df = load_meta()
    db = np.flatnonzero(np.isin(img_df.split.values, ["seen_test", "unseen"]))
    rng = np.random.default_rng(7)
    qs = []
    for _ in range(N_QUERIES):
        x, q = rng.choice(db, 2, replace=False)
        pool = rng.choice(db[(db != x) & (db != q)], POOL, replace=False)
        qs.append({"x": int(x), "q": int(q), "frac": float(rng.choice([0.1, 0.25, 0.5])), "pool": pool.tolist()})
    return img_df, cls_df, db, qs


def load_images(paths):
    from PIL import Image
    zf_local = {}

    def one(p):
        import threading
        tid = threading.get_ident()
        if tid not in zf_local:                      # open the zip ONCE per thread
            zf_local[tid] = zipfile.ZipFile(ZIP_PATH)
        zf = zf_local[tid]
        im = Image.open(io.BytesIO(zf.read(p))).convert("RGB")
        im.thumbnail((224, 224))
        return im
    with ThreadPoolExecutor(16) as ex:
        return list(ex.map(one, paths))


def parse_rating(text):
    import re
    m = re.findall(r"Score:\s*(\d+)", text)
    return min(10, int(m[-1])) / 10 if m else None


def score(mode="yesno"):
    from transformers import Qwen2_5_VLForConditionalGeneration, AutoProcessor
    rating = mode == "rating"
    SC = SCORES_RATING if rating else SCORES
    prompts = PROMPTS_RATING if rating else PROMPTS
    img_df, cls_df, db, qs = workload()
    pairs = []  # (query_idx, pool_pos, facet, ref_img, cand_img)
    for qi, w in enumerate(qs):
        for pi, cand in enumerate(w["pool"]):
            pairs.append((qi, pi, 0, w["x"], cand))
            pairs.append((qi, pi, 1, w["q"], cand))
    S = np.full((N_QUERIES, POOL, 2), np.nan, np.float32)
    if SC.exists():
        S = np.load(SC)["S"]
    todo = [p for p in pairs if np.isnan(S[p[0], p[1], p[2]])]
    print(f"pairs total {len(pairs)}, still to score {len(todo)}", flush=True)
    if not todo:
        return
    need = sorted({p[3] for p in todo} | {p[4] for p in todo})
    t0 = time.time()
    ims = dict(zip(need, load_images(img_df.path.values[need])))
    print(f"loaded {len(ims)} images in {time.time() - t0:.0f} s", flush=True)

    model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
        MODEL, torch_dtype=torch.bfloat16, attn_implementation="sdpa", device_map="cuda").eval()
    proc = AutoProcessor.from_pretrained(MODEL, min_pixels=128 * 28 * 28 // 4, max_pixels=224 * 224)
    proc.tokenizer.padding_side = "left"
    tok = proc.tokenizer
    yes_ids = [tok.encode(w, add_special_tokens=False)[0] for w in ("Yes", " Yes")]
    no_ids = [tok.encode(w, add_special_tokens=False)[0] for w in ("No", " No")]
    yn = torch.tensor(yes_ids + no_ids, device="cuda")
    n_missing = 0
    texts = {f: proc.apply_chat_template(
        [{"role": "user", "content": [{"type": "image"}, {"type": "image"}, {"type": "text", "text": prompts[f]}]}],
        tokenize=False, add_generation_prompt=True) for f in prompts}
    facet_names = list(prompts)

    t0, done, next_pct = time.time(), 0, 10
    with torch.no_grad():
        bs = 32 if rating else BATCH
        for b in range(0, len(todo), bs):
            chunk = todo[b:b + bs]
            inp = proc(text=[texts[facet_names[p[2]]] for p in chunk],
                       images=[im for p in chunk for im in (ims[p[3]], ims[p[4]])],
                       padding=True, return_tensors="pt").to("cuda")
            out = model.generate(**inp, max_new_tokens=160 if rating else MAX_NEW, do_sample=False,
                                 output_scores=not rating, return_dict_in_generate=True)
            gen = out.sequences[:, inp["input_ids"].shape[1]:]              # (B, steps)
            if not rating:
                steps = torch.stack([sc[:, yn] for sc in out.scores], 1).float()  # (B, steps, 4) yes/no logits only
            if rating:
                for p, txt in zip(chunk, proc.batch_decode(gen, skip_special_tokens=True)):
                    v = parse_rating(txt)
                    if v is None:
                        v = 0.5; n_missing += 1
                    S[p[0], p[1], p[2]] = v
                chunk_done = True
            else:
                chunk_done = False
            for j, p in enumerate(chunk if not chunk_done else []):
                pos = torch.nonzero(torch.isin(gen[j], yn)).flatten()
                if len(pos) == 0:                                           # no final answer found
                    S[p[0], p[1], p[2]] = 0.5; n_missing += 1; continue
                lg = steps[j, pos[-1]]                                      # last Yes/No token = the answer
                pr = torch.softmax(lg, -1)
                S[p[0], p[1], p[2]] = float(pr[:2].sum())
            done += len(chunk)
            pct = 100 * done / len(todo)
            if pct >= next_pct or b + bs >= len(todo):
                np.savez(SC, S=S)
                rate = done / (time.time() - t0)
                note(f"B5-VLM-{mode}", f"{pct:.0f}% of {len(todo)} pairs, {rate:.1f} pairs/s, "
                               f"~{(len(todo) - done) / rate / 60:.0f} min left")
                next_pct += 10
    elapsed = time.time() - t0
    np.savez(SC, S=S)
    (CACHE / f"b5_timing{'_rating' if rating else ''}.json").write_text(json.dumps({"pairs": len(todo), "seconds": elapsed,
                                                       "pairs_per_s": len(todo) / elapsed,
                                                       "no_answer_found": n_missing}))


def evaluate():
    from .baselines import b1_labels, b2_text, b6_clip, sse_views
    img_df, cls_df, db, qs = workload()
    S = np.load(SCORES)["S"]
    assert not np.isnan(S).any(), "VLM scores incomplete — run `score` first"
    X = np.load(CACHE / "clip_img.npy").astype(np.float32)
    c = img_df.cls.map({k: i for i, k in enumerate(cls_df.cls)}).values
    T = truth(cls_df)
    unseen_img = img_df.split.values == "unseen"
    E = np.load(CACHE / "emb_tree_s0.npy")
    L = json.loads((CACHE / "emb_tree_s0.json").read_text())["layout"]
    torch.manual_seed(0)
    b1, b1s = b1_labels(X, img_df, cls_df)
    methods = {"SSE": sse_views(E, L), "B1 labels": b1, "B1-soft": b1s, "B2 CLIP+text": b2_text(X),
               "B6 plain CLIP": b6_clip(X)}
    for lab, tag in (("B3 separate", "b3tree_s0"), ("B4 CSN", "csntree_s0")):
        Z = np.load(CACHE / f"{tag}.npz")
        methods[lab] = {"habitat": (Z["habitat"], "cos"), "family": (Z["family"], "cos")}
    scorers = {m: (Scorer(v["habitat"]), Scorer(v["family"])) for m, v in methods.items()}

    SR = np.load(SCORES_RATING)["S"] if SCORES_RATING.exists() else None
    if SR is not None and np.isnan(SR).any():
        SR = None
    per = {m: [] for m in [*methods, "B5 VLM (Qwen2.5-VL-7B)", *(["B5 VLM rating 0-10"] if SR is not None else [])]}
    for qi, w in enumerate(qs):
        pool = np.array(w["pool"])
        true_s = T["habitat"][c[w["x"]], c[pool]]
        F_true = true_s >= np.quantile(true_s, 1 - w["frac"])
        n_feas = int(F_true.sum())
        gain = F_true * T["fam_gain"][c[w["q"]], c[pool]]
        cand = {m: (hs(w["x"], pool), fs(w["q"], pool)) for m, (hs, fs) in scorers.items()}
        cand["B5 VLM (Qwen2.5-VL-7B)"] = (S[qi, :, 0], S[qi, :, 1])
        if SR is not None:
            cand["B5 VLM rating 0-10"] = (SR[qi, :, 0] + 1e-3 * S[qi, :, 0], SR[qi, :, 1] + 1e-3 * S[qi, :, 1])
        for m, (h, f) in cand.items():
            M = np.zeros(POOL, bool); M[np.argsort(-h, kind="stable")[:n_feas]] = True
            top = np.argsort(-np.where(M, f, -np.inf), kind="stable")[:10]
            per[m].append({"predicate_F1": float((M & F_true).sum() / n_feas), "predicate_AP": ap(h, F_true),
                           "P@10_feasible": float(F_true[top].mean()),
                           "NDCG@10": float(ndcg(gain[top], gain[F_true])), "x_unseen": bool(unseen_img[w["x"]])})
    rows = []
    for m, rs in per.items():
        for sl, f in (("all", lambda r: True), ("x unseen", lambda r: r["x_unseen"])):
            sub = [r for r in rs if f(r)]
            rows.append({"method": m, "slice": sl, "n": len(sub),
                         **{k: float(np.nanmean([r[k] for r in sub]))
                            for k in ("predicate_F1", "predicate_AP", "P@10_feasible", "NDCG@10")}})
    timing = json.loads((CACHE / "b5_timing.json").read_text()) if (CACHE / "b5_timing.json").exists() else {}
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "results.json").write_text(json.dumps({"rows": rows, "timing": timing}, indent=1))
    md = [f"### B5 — {N_QUERIES} Q1 queries, each over the same {POOL} candidates for every method", "",
          f"VLM speed: {timing.get('pairs_per_s', float('nan')):.1f} image pairs/s on the RTX 5090 "
          f"(one query = {POOL} habitat + {POOL} family pairs).", "",
          "| method | slice | n | predicate_F1 | predicate_AP | P@10_feasible | NDCG@10 |", "|---|---|---|---|---|---|---|"]
    md += [f"| {r['method']} | {r['slice']} | {r['n']} | {r['predicate_F1']:.3f} | {r['predicate_AP']:.3f} | "
           f"{r['P@10_feasible']:.3f} | {r['NDCG@10']:.3f} |" for r in rows]
    (OUT / "results.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    {"score": score, "score_rating": lambda: score("rating"), "evaluate": evaluate}[sys.argv[1]]()
