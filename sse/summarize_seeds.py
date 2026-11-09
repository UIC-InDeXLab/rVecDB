"""Average the key numbers over seeds: results/awa2/seed*/results.json -> results/awa2/round2_summary.md"""
import json
from collections import defaultdict

import numpy as np

from .awa2 import ROOT

RES = ROOT / "results/awa2"


def collect(pattern):
    runs = sorted(RES.glob(pattern))
    vals = defaultdict(list)          # (table, method, metric) -> [values per seed]
    for f in runs:
        r = json.loads(f.read_text())
        for row in r["E1"]:
            own = {"habitat": "habitat", "diet": "diet", "family": "taxonomy"}.get(row["view"])
            if own:
                vals[("E1 own facet", row["method"], row["view"])].append(row[own])
        e3 = r["E3"] if all(isinstance(v, dict) for v in r["E3"].values()) else {"SSE": r["E3"]}
        for lab, d in e3.items():
            for k, v in d.items():
                vals[("E3 general search", lab, k)].append(v)
        for row in r["E4"]:
            if row["slice"] in ("all", "x unseen"):
                for k in ("predicate_F1", "P@10_feasible", "NDCG@10"):
                    vals[("E4 queries", row["method"], f"{k} [{row['slice']}]")].append(row[k])
        for row in r["leakage"]:
            vals[("E4 no-mixing error (lower=better)", row["method"], row["pair_type"])].append(row["abs_error"])
        for row in r.get("E2b", []):
            for k in ("same-order AUC", "same-family AUC", "same-genus AUC"):
                vals[("E2b prefix keeps levels (pair AUC)", f"{row['method']} {row['prefix']}", k)].append(row[k])
        for row in r["E5b"]:
            vals[("E5b in-between", row["method"], "spearman")].append(row["spearman_on_label-different_pairs"])
        for row in r["E5c"]:
            vals[("E5c threshold dial", row["method"], "monotonic")].append(row["monotonic_spearman"])
        for row in r["E2"]:
            if (row["level"], row["prefix_len"]) in {("order", 8), ("family", 32), ("genus", 64)}:
                vals[(f"E2 zoom levels [{row['split']}]", row["method"],
                      f"{row['level']}@{row['prefix_len']}")].append(row["mAP"])
    return runs, vals


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--pattern", default="seed*/results.json")
    ap.add_argument("--out", default="round2_summary.md")
    args = ap.parse_args()
    runs, vals = collect(args.pattern)
    out = [f"# AwA2 {args.out} — mean ± spread over {len(runs)} seeds\n",
           "Spread = standard deviation across seeds. Same test queries in every seed.\n"]
    tables = defaultdict(lambda: defaultdict(dict))
    for (tab, meth, metric), v in vals.items():
        tables[tab][meth][metric] = f"{np.mean(v):.3f} ± {np.std(v):.3f}"
    for tab, rows in tables.items():
        metrics = sorted({m for r in rows.values() for m in r})
        out += [f"\n### {tab}\n", "| method | " + " | ".join(metrics) + " |", "|---" * (len(metrics) + 1) + "|"]
        for meth, r in rows.items():
            out.append(f"| {meth} | " + " | ".join(r.get(m, "–") for m in metrics) + " |")
    (RES / args.out).write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
