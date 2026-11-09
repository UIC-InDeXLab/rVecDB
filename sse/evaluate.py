"""Run E1-E5 on AwA2 and write results/awa2/*.md + results.json.

Database = all test images (seen_test + unseen). Ground truth is per class (species):
  habitat / diet similarity = cosine of the people-rated score vectors (graded answer key)
  family-level ranking gain = 1 same family, 0.5 same order, 0 otherwise

Usage: .venv/bin/python -m sse.evaluate
"""
import json
from pathlib import Path

import numpy as np
from scipy.stats import spearmanr
from tqdm import tqdm

from .awa2 import load_meta, CACHE, ROOT
from .baselines import b6_clip, b2_text, b1_labels, sse_views
from .taxonomy_awa2 import LEVELS

import os
OUT = Path(os.environ.get("SSE_OUT", ROOT / "results/awa2"))
OUT.mkdir(parents=True, exist_ok=True)
RNG = np.random.default_rng(0)
PROG = ROOT / "logs/PROGRESS.md"
RUN_TAG = ""


def note(step, status):
    import time
    line = f"| {time.strftime('%m-%d %H:%M:%S')} | evaluate{('[' + RUN_TAG + ']') if RUN_TAG else ''}/{step} | {status} |"
    print(line, flush=True)
    if PROG.exists():
        with open(PROG, "a") as f:
            f.write(line + "\n")


def run(name, fn, *a, **k):
    import time
    note(name, "started"); t0 = time.time()
    out = fn(*a, **k)
    note(name, f"done ({time.time() - t0:.0f} s)")
    return out


# ---------------------------------------------------------------- scoring
class Scorer:
    def __init__(self, view):
        M, self.kind = view
        M = np.asarray(M, dtype=np.float32)
        if self.kind == "cos":
            M = M / (np.linalg.norm(M, axis=1, keepdims=True) + 1e-8)
        elif self.kind == "taxlab":
            v = M[:, 2:]
            M = np.concatenate([M[:, :2], v / (np.linalg.norm(v, axis=1, keepdims=True) + 1e-8)], 1)
        self.M = M

    def __call__(self, q, db):
        M = self.M
        if self.kind == "cos":
            return M[db] @ M[q]
        if self.kind == "jacc":
            inter = M[db] @ M[q]
            union = M[db].sum(1) + M[q].sum() - inter
            return np.where(union > 0, inter / np.maximum(union, 1e-8), 1.0)
        if self.kind == "taxlab":
            same_f = M[db, 1] == M[q, 1]
            same_o = M[db, 0] == M[q, 0]
            return same_f * 1.0 + (same_o & ~same_f) * 0.5 + 0.01 * (M[db, 2:] @ M[q, 2:])
        raise ValueError(self.kind)

    def pairs(self, a, b):
        M = self.M
        if self.kind == "cos":
            return (M[a] * M[b]).sum(1)
        if self.kind == "jacc":
            inter = (M[a] * M[b]).sum(1)
            union = M[a].sum(1) + M[b].sum(1) - inter
            return np.where(union > 0, inter / np.maximum(union, 1e-8), 1.0)
        if self.kind == "taxlab":
            same_f = M[a, 1] == M[b, 1]
            same_o = M[a, 0] == M[b, 0]
            return same_f * 1.0 + (same_o & ~same_f) * 0.5 + 0.01 * (M[a, 2:] * M[b, 2:]).sum(1)
        raise ValueError(self.kind)


# ---------------------------------------------------------------- ground truth
def truth(cls_df):
    def cosm(col):
        v = np.stack(cls_df[col].values)
        v = v / (np.linalg.norm(v, axis=1, keepdims=True) + 1e-8)
        return v @ v.T
    codes = {l: cls_df[l].astype("category").cat.codes.values for l in LEVELS}
    same = {l: codes[l][:, None] == codes[l][None, :] for l in LEVELS}
    tax_sim = same["order"] * 1.0 + same["family"] + same["genus"]          # 0..3
    fam_gain = np.where(same["family"], 1.0, np.where(same["order"], 0.5, 0.0))
    hab_bin = np.stack(cls_df.habitat.values) >= 0.5
    hab_pattern_same = (hab_bin[:, None] == hab_bin[None]).all(-1)
    return {"habitat": cosm("habitat"), "diet": cosm("diet"), "tax": tax_sim,
            "fam_gain": fam_gain, "hab_pattern_same": hab_pattern_same, "codes": codes}


def ap(scores, rel):
    order = np.argsort(-scores, kind="stable")
    r = rel[order]
    if r.sum() == 0:
        return np.nan
    hits = np.cumsum(r)
    return float((hits[r] / (np.flatnonzero(r) + 1)).mean())


def ndcg(gains, ideal_gains, k=10):
    disc = 1 / np.log2(np.arange(2, k + 2))
    g = np.asarray(gains[:k]); ig = np.sort(ideal_gains)[::-1][:k]
    dcg = (g * disc[:len(g)]).sum(); idcg = (ig * disc[:len(ig)]).sum()
    return dcg / idcg if idcg > 0 else np.nan


def md_table(rows, cols, title):
    s = [f"### {title}", "", "| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for r in rows:
        s.append("| " + " | ".join(f"{r[c]:.3f}" if isinstance(r[c], float) else str(r[c]) for c in cols) + " |")
    return "\n".join(s) + "\n"


# ---------------------------------------------------------------- experiments
def e1(methods, c, db, T, n_pairs=200_000):
    """G1: does each block/view track its own facet (Spearman vs. ground truth)?"""
    a, b = RNG.choice(db, n_pairs), RNG.choice(db, n_pairs)
    keep = a != b; a, b = a[keep], b[keep]
    gt = {"habitat": T["habitat"][c[a], c[b]], "diet": T["diet"][c[a], c[b]], "taxonomy": T["tax"][c[a], c[b]]}
    rows = []
    for mname, views in methods.items():
        for vname in ("habitat", "diet", "family", "tax", "rest", "full"):
            if vname not in views or (vname == "full" and mname != "SSE"):
                continue
            s = Scorer(views[vname]).pairs(a, b)
            row = {"method": mname, "view": vname}
            for g, v in gt.items():
                row[g] = float(spearmanr(s, v).statistic)
            rows.append(row)
    return rows


def e3(views_sse, X, c, db, nq=500, k=10):
    """G3: general search. Overlap@10 with CLIP neighbours; same-species AP."""
    clip, full = Scorer((X, "cos")), Scorer(views_sse["full"])
    qs = RNG.choice(db, nq, replace=False)
    ov, ap_clip, ap_sse = [], [], []
    for q in qs:
        d = db[db != q]
        s1, s2 = clip(q, d), full(q, d)
        ov.append(len(set(d[np.argsort(-s1)[:k]]) & set(d[np.argsort(-s2)[:k]])) / k)
        rel = c[d] == c[q]
        ap_clip.append(ap(s1, rel)); ap_sse.append(ap(s2, rel))
    return {"overlap@10_with_CLIP": float(np.mean(ov)),
            "species_mAP_CLIP": float(np.nanmean(ap_clip)), "species_mAP_SSE": float(np.nanmean(ap_sse))}


def make_workload(db, c, T, n=1000):
    qs = []
    for _ in range(n):
        x, q = RNG.choice(db, 2, replace=False)
        frac = RNG.choice([0.1, 0.25, 0.5])
        qs.append((int(x), int(q), float(frac)))
    return qs


def e4(methods, workload, db, c, T, unseen_img):
    """G4/G5a: filter on habitat (reference x), rank by Family (reference q)."""
    per = {m: [] for m in methods}
    for x, q, frac in tqdm(workload, desc="E4 queries", mininterval=10):
        true_s = T["habitat"][c[x], c[db]]
        tau = np.quantile(true_s, 1 - frac)
        F_true = true_s >= tau
        n_feas = int(F_true.sum())
        gain_all = F_true * T["fam_gain"][c[q], c[db]]
        for m, views in methods.items():
            hs = Scorer(views["habitat"])(x, db)
            M = np.zeros(len(db), bool); M[np.argsort(-hs, kind="stable")[:n_feas]] = True
            fs = Scorer(views["family"])(q, db)
            fs_m = np.where(M, fs, -np.inf)
            top = np.argsort(-fs_m, kind="stable")[:10]
            per[m].append({
                "predicate_F1": float((M & F_true).sum() / n_feas),
                "predicate_AP": ap(hs, F_true),
                "P@10_feasible": float(F_true[top].mean()),
                "NDCG@10": float(ndcg(gain_all[top], gain_all[F_true])),
                "x_unseen": bool(unseen_img[x]), "q_unseen": bool(unseen_img[q]),
            })
    return per


def summarize_e4(per):
    rows, slices = [], {"all": lambda r: True,
                        "x unseen": lambda r: r["x_unseen"], "x seen": lambda r: not r["x_unseen"],
                        "q unseen": lambda r: r["q_unseen"]}
    for m, rs in per.items():
        for sname, f in slices.items():
            sub = [r for r in rs if f(r)]
            row = {"method": m, "slice": sname, "n": len(sub)}
            for k in ("predicate_F1", "predicate_AP", "P@10_feasible", "NDCG@10"):
                row[k] = float(np.nanmean([r[k] for r in sub]))
            rows.append(row)
    return rows


def leakage(methods, db, c, T, cls_df, n=300, frac=0.25):
    """No-mixing test. Pairs of habitat references:
      A: very similar habitat, different Order  (filters should agree)
      B: same Family, clearly different habitat  (filters should differ)
    Error = |Jaccard(method feasible sets) - Jaccard(true feasible sets)|.
    """
    order = T["codes"]["order"]; fam = T["codes"]["family"]
    ca, cb = c[db][:, None], c[db][None, :]
    out = []
    for name, cond in {
        "A same-habitat/diff-order": lambda i, j: T["habitat"][i, j] >= 0.9 and order[i] != order[j],
        "B same-family/diff-habitat": lambda i, j: fam[i] == fam[j] and T["habitat"][i, j] <= 0.7 and i != j,
    }.items():
        cls_pairs = [(i, j) for i in range(len(cls_df)) for j in range(len(cls_df)) if cond(i, j)]
        if not cls_pairs:
            continue
        err = {m: [] for m in methods}; jt = []
        n_feas = int(frac * len(db))
        for _ in tqdm(range(n), desc=name, mininterval=10):
            i, j = cls_pairs[RNG.integers(len(cls_pairs))]
            xi = RNG.choice(db[c[db] == i]) if (c[db] == i).any() else None
            xj = RNG.choice(db[c[db] == j]) if (c[db] == j).any() else None
            if xi is None or xj is None:
                continue
            t1 = set(np.argsort(-T["habitat"][c[xi], c[db]], kind="stable")[:n_feas])
            t2 = set(np.argsort(-T["habitat"][c[xj], c[db]], kind="stable")[:n_feas])
            jtrue = len(t1 & t2) / len(t1 | t2); jt.append(jtrue)
            for m, views in methods.items():
                s = Scorer(views["habitat"])
                m1 = set(np.argsort(-s(xi, db), kind="stable")[:n_feas])
                m2 = set(np.argsort(-s(xj, db), kind="stable")[:n_feas])
                err[m].append(abs(len(m1 & m2) / len(m1 | m2) - jtrue))
        for m in methods:
            out.append({"pair_type": name, "method": m, "n_class_pairs": len(cls_pairs),
                        "true_jaccard": float(np.mean(jt)), "abs_error": float(np.mean(err[m]))})
    return out


def e5b(methods, db, c, T, n_pairs=200_000):
    """In-between similarity: among pairs whose yes/no habitat labels DIFFER,
    does the method still order them by true graded habitat similarity?"""
    a, b = RNG.choice(db, n_pairs), RNG.choice(db, n_pairs)
    keep = (a != b) & ~T["hab_pattern_same"][c[a], c[b]]
    a, b = a[keep], b[keep]
    gt = T["habitat"][c[a], c[b]]
    return [{"method": m, "spearman_on_label-different_pairs":
             float(spearmanr(Scorer(v["habitat"]).pairs(a, b), gt).statistic)} for m, v in methods.items()]


def e5c(methods, db, c, T, nq=300, bins=10):
    """Threshold behaviour: as the method's habitat score rises, does true similarity rise step by step?"""
    rows = []
    for m, views in tqdm(methods.items(), desc="E5c", mininterval=10):
        s_fn = Scorer(views["habitat"]); curves = []
        for x in RNG.choice(db, nq, replace=False):
            s = s_fn(x, db); t = T["habitat"][c[x], c[db]]
            order = np.argsort(s, kind="stable")
            curves.append([t[ch].mean() for ch in np.array_split(order, bins)])
        curve = np.nanmean(np.array(curves), 0)
        rows.append({"method": m, "monotonic_spearman": float(spearmanr(np.arange(bins), curve).statistic),
                     "low_bin_true_sim": float(curve[0]), "high_bin_true_sim": float(curve[-1]),
                     "curve": [round(float(v), 3) for v in curve]})
    return rows


def e2(embs, X_pca, img_df, c, cls_df, nq=400, lengths=(4, 8, 16, 32, 64)):
    """G2: taxonomy prefix of length L -> AP for finding same Order / Family / Genus."""
    codes = {l: cls_df[l].astype("category").cat.codes.values[c] for l in LEVELS}
    rows = []
    for split in ("seen_test", "unseen"):
        db = np.flatnonzero(img_df.split.values == split)
        qs = RNG.choice(db, min(nq, len(db)), replace=False)
        for mname, E in tqdm({**embs, "CLIP-PCA": X_pca}.items(), desc=f"E2 {split}", mininterval=10):
            for L in lengths:
                sc = Scorer((E[:, :L], "cos"))
                for lvl in LEVELS:
                    aps = []
                    for q in qs:
                        d = db[db != q]
                        aps.append(ap(sc(q, d), codes[lvl][d] == codes[lvl][q]))
                    rows.append({"split": split, "method": mname, "prefix_len": L, "level": lvl,
                                 "mAP": float(np.nanmean(aps))})
    return rows


def save(res, md):
    (OUT / "results.json").write_text(json.dumps(res, indent=1))
    (OUT / "results.md").write_text("\n".join(md))


def e2b(methods, db, c, T, n_pairs=300_000):
    """Does each taxonomy prefix keep ALL coarser levels?  Pair AUC for 'same <level> or not'
    using the Order (8), Family (32) and Genus (64) prefix of each SSE, and the labels for B1."""
    from sklearn.metrics import roc_auc_score
    a, b = RNG.choice(db, n_pairs), RNG.choice(db, n_pairs)
    keep = a != b; a, b = a[keep], b[keep]
    tax = T["tax"][c[a], c[b]]               # 0 diff order, 1 same order, 2 same family, 3 same genus
    rows = []
    for m, views in methods.items():
        prefixes = views["levels"] if "levels" in views else ({"order@8": (views["tax"][0][:, :8], "cos"), "family@32": views["family"],
                     "genus@64": views["tax"]} if "tax" in views else {"family view": views["family"]})
        for pname, view in prefixes.items():
            s = Scorer(view).pairs(a, b)
            row = {"method": m, "prefix": pname}
            for lvl, thr in (("order", 1), ("family", 2), ("genus", 3)):
                row[f"same-{lvl} AUC"] = float(roc_auc_score(tax >= thr, s))
            rows.append(row)
    return rows


def main():
    import argparse
    global OUT, RUN_TAG
    ap = argparse.ArgumentParser()
    ap.add_argument("--sse", default="SSE=main_768,SSE-hard=hard_768",
                    help="comma list of label=embedding_tag; the first one is used for E2/E3")
    ap.add_argument("--mrl", default="mrl_768", help="embedding tag of the MRL ablation ('' to skip)")
    ap.add_argument("--out", default="", help="sub-folder of results/awa2")
    ap.add_argument("--no-baselines", action="store_true")
    ap.add_argument("--extra", default="", help="trained baselines: comma list label=npz_tag, e.g. 'B3 separate=b3_s0'")
    ap.add_argument("--seed", type=int, default=0, help="seed for baseline training (B1)")
    args = ap.parse_args()
    if args.out:
        OUT = OUT / args.out
        OUT.mkdir(parents=True, exist_ok=True)
        RUN_TAG = args.out
    import torch
    torch.manual_seed(args.seed)

    img_df, cls_df = load_meta()
    X = np.load(CACHE / "clip_img.npy").astype(np.float32)
    c = img_df.cls.map({k: i for i, k in enumerate(cls_df.cls)}).values
    db = np.flatnonzero(np.isin(img_df.split.values, ["seen_test", "unseen"]))
    unseen_img = img_df.split.values == "unseen"
    T = truth(cls_df)
    print("database size", len(db), "| unseen classes:", list(cls_df.cls[cls_df.unseen]))

    sse = dict(kv.split("=") for kv in args.sse.split(","))
    first = next(iter(sse))
    L = json.loads((CACHE / f"emb_{sse[first]}.json").read_text())["layout"]
    E = {lab: np.load(CACHE / f"emb_{tag}.npy") for lab, tag in sse.items()}
    methods = {lab: sse_views(E[lab], L) for lab in sse}
    if not args.no_baselines:
        b1, b1s = run("train-B1-classifiers", b1_labels, X, img_df, cls_df)
        methods.update({"B1 labels": b1, "B1-soft": b1s, "B2 CLIP+text": b2_text(X), "B6 plain CLIP": b6_clip(X)})

    for kv in filter(None, args.extra.split(",")):
        lab, tag = kv.split("=")
        Z = np.load(CACHE / f"{tag}.npz")
        methods[lab] = {"habitat": (Z["habitat"], "cos"), "diet": (Z["diet"], "cos"),
                        "family": (Z["family"], "cos"), "full": (Z["full"], "cos"),
                        "levels": {"order@8": (Z["order"], "cos"), "family@32": (Z["family"], "cos"),
                                   "genus@64": (Z["genus"], "cos")}}

    res, md = {"args": vars(args)}, [f"# AwA2 results {args.out}\n", f"args: `{vars(args)}`\n"]
    res["E1"] = run("E1", e1, methods, c, db, T)
    md.append(md_table(res["E1"], ["method", "view", "habitat", "diet", "taxonomy"],
                       "E1 — Spearman of each view vs. each true facet (higher on own facet = good)"))
    save(res, md)
    res["E3"] = {lab: run(f"E3-{lab}", e3, methods[lab], X, c, db) for lab in sse}
    e3rows = [{"method": lab, **v} for lab, v in res["E3"].items()]
    md.append(md_table(e3rows, list(e3rows[0].keys()), "E3 — general search preserved"))
    save(res, md)
    wl = make_workload(db, c, T)
    per = run("E4", e4, methods, wl, db, c, T, unseen_img); res["E4"] = summarize_e4(per)
    md.append(md_table(res["E4"], ["method", "slice", "n", "predicate_F1", "predicate_AP", "P@10_feasible", "NDCG@10"],
                       "E4/E5a — Q1 queries: habitat filter (ref x) + Family ranking (ref q)"))
    save(res, md)
    res["leakage"] = run("E4-leakage", leakage, methods, db, c, T, cls_df)
    md.append(md_table(res["leakage"], ["pair_type", "method", "n_class_pairs", "true_jaccard", "abs_error"],
                       "E4 — no-mixing test (lower error = better)"))
    save(res, md)
    res["E2b"] = run("E2b", e2b, methods, db, c, T)
    md.append(md_table(res["E2b"], ["method", "prefix", "same-order AUC", "same-family AUC", "same-genus AUC"],
                       "E2b — does each prefix keep its own AND coarser levels? (pair AUC)"))
    save(res, md)
    res["E5b"] = run("E5b", e5b, methods, db, c, T)
    md.append(md_table(res["E5b"], ["method", "spearman_on_label-different_pairs"],
                       "E5b — in-between similarity among pairs labels call 'different'"))
    save(res, md)
    res["E5c"] = run("E5c", e5c, methods, db, c, T)
    md.append(md_table(res["E5c"], ["method", "monotonic_spearman", "low_bin_true_sim", "high_bin_true_sim"],
                       "E5c — stricter threshold -> closer matches?"))
    save(res, md)

    embs = dict(E)
    if args.mrl and (CACHE / f"emb_{args.mrl}.npy").exists():
        embs["SSE-MRL (genus everywhere)"] = np.load(CACHE / f"emb_{args.mrl}.npy")
    tr = img_df.split.values == "train"
    mu = X[tr].mean(0); _, _, Vt = np.linalg.svd(X[tr] - mu, full_matrices=False)
    res["E2"] = run("E2", e2, embs, (X - mu) @ Vt[:64].T, img_df, c, cls_df)
    md.append(md_table(res["E2"], ["split", "method", "prefix_len", "level", "mAP"],
                       "E2 — taxonomy prefix length vs. level"))
    save(res, md)
    print("\n".join(md))


if __name__ == "__main__":
    main()
