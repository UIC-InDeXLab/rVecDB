"""3-seed mean ± half-range for the 2026-11-25 extra experiments -> results/<ds>/x_summary.md
Usage: python -m sse.x_summary"""
import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
SPECS = [("awa2", "x_seed{s}/groupk.json", ["part", "method", "level", "k"]),
         ("awa2", "x_seed{s}/agg.json", ["method"]),
         ("awa2", "x_seed{s}/textq.json", ["method", "slice"]),
         ("inat", "seed{s}/groupk.json", ["class", "part", "method", "level"])]


def table(files, keys):
    d = pd.concat([pd.DataFrame(json.loads(f.read_text())) for f in files])
    num = [c for c in d.columns if c not in keys and pd.api.types.is_numeric_dtype(d[c])]
    g = d.groupby(keys, sort=False)[num]
    m, h = g.mean(), (g.max() - g.min()) / 2
    t = m.astype(object)
    for c in num:
        t[c] = [f"{a:.3f} ±{b:.3f}" for a, b in zip(m[c], h[c])]
    return t.reset_index().to_markdown(index=False)


def main():
    out = {}
    for ds, pat, keys in SPECS:
        files = [ROOT / "results" / ds / pat.format(s=s) for s in range(3)]
        files = [f for f in files if f.exists()]
        if files:
            out.setdefault(ds, []).append(f"### {pat.split('/')[-1]} ({len(files)} seeds)\n\n{table(files, keys)}\n")
    for ds, parts in out.items():
        (ROOT / "results" / ds / "x_summary.md").write_text("\n".join(parts))
        print(ds, "->", ROOT / "results" / ds / "x_summary.md")


if __name__ == "__main__":
    main()
