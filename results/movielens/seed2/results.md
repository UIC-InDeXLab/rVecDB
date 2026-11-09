# MovieLens results (seed 2)

### E1 — Spearman of each view vs each true facet

| method | view | genre | tone | theme | style |
|---|---|---|---|---|---|
| SSE | genre | 0.347 | 0.209 | 0.309 | 0.190 |
| SSE | tone | 0.292 | 0.269 | 0.290 | 0.210 |
| SSE | theme | 0.276 | 0.189 | 0.312 | 0.174 |
| SSE | style | 0.271 | 0.224 | 0.277 | 0.247 |
| SSE-hard | genre | 0.223 | 0.139 | 0.217 | 0.122 |
| SSE-hard | tone | 0.200 | 0.145 | 0.204 | 0.118 |
| SSE-hard | theme | 0.192 | 0.118 | 0.212 | 0.105 |
| SSE-hard | style | 0.191 | 0.140 | 0.199 | 0.140 |
| B3 separate | genre | 0.346 | 0.210 | 0.307 | 0.189 |
| B3 separate | tone | 0.276 | 0.275 | 0.290 | 0.211 |
| B3 separate | theme | 0.272 | 0.196 | 0.312 | 0.178 |
| B3 separate | style | 0.259 | 0.224 | 0.279 | 0.249 |
| B4 CSN | genre | 0.393 | 0.242 | 0.341 | 0.219 |
| B4 CSN | tone | 0.300 | 0.311 | 0.304 | 0.239 |
| B4 CSN | theme | 0.311 | 0.222 | 0.350 | 0.203 |
| B4 CSN | style | 0.286 | 0.250 | 0.294 | 0.284 |
| B1 labels | genre | 0.007 | 0.008 | 0.011 | 0.009 |
| B1 labels | tone | -0.003 | 0.035 | 0.012 | 0.023 |
| B1 labels | theme | 0.042 | 0.041 | 0.052 | 0.035 |
| B1 labels | style | 0.071 | 0.013 | 0.055 | 0.039 |
| B1-soft | genre | 0.334 | 0.167 | 0.268 | 0.143 |
| B1-soft | tone | 0.282 | 0.215 | 0.258 | 0.161 |
| B1-soft | theme | 0.274 | 0.154 | 0.280 | 0.139 |
| B1-soft | style | 0.258 | 0.163 | 0.250 | 0.200 |
| B2 text prompts | genre | 0.105 | 0.059 | 0.103 | 0.054 |
| B2 text prompts | tone | 0.082 | 0.067 | 0.082 | 0.043 |
| B2 text prompts | theme | 0.089 | 0.054 | 0.099 | 0.049 |
| B2 text prompts | style | 0.049 | 0.036 | 0.053 | 0.035 |
| B6 plain bge | genre | 0.174 | 0.106 | 0.190 | 0.098 |
| B6 plain bge | tone | 0.174 | 0.106 | 0.190 | 0.098 |
| B6 plain bge | theme | 0.174 | 0.106 | 0.190 | 0.098 |
| B6 plain bge | style | 0.174 | 0.106 | 0.190 | 0.098 |

### E3 — general search preserved

| method | overlap@10_with_bge |
|---|---|
| SSE | 0.740 |
| B4 CSN | 0.642 |

### E4 — filter on one facet (ref x), rank on another (ref q); graded truth

| method | predicate_F1 | predicate_AP | P@10_feasible | NDCG@10 |
|---|---|---|---|---|
| SSE | 0.351 | 0.343 | 0.307 | 0.122 |
| SSE-hard | 0.301 | 0.289 | 0.272 | 0.093 |
| B3 separate | 0.353 | 0.346 | 0.315 | 0.122 |
| B4 CSN | 0.364 | 0.361 | 0.321 | 0.128 |
| B1 labels | 0.184 | 0.185 | 0.172 | 0.036 |
| B1-soft | 0.331 | 0.324 | 0.280 | 0.092 |
| B2 text prompts | 0.251 | 0.248 | 0.296 | 0.086 |
| B6 plain bge | 0.293 | 0.280 | 0.249 | 0.092 |

### E5b — in-between similarity among pairs whose yes/no tags differ

| method | genre | tone | theme | style |
|---|---|---|---|---|
| B1 labels | 0.007 | 0.034 | 0.052 | 0.037 |
| B1-soft | 0.333 | 0.214 | 0.280 | 0.200 |
| B2 text prompts | 0.105 | 0.067 | 0.099 | 0.035 |
| B3 separate | 0.345 | 0.276 | 0.312 | 0.247 |
| B4 CSN | 0.392 | 0.311 | 0.350 | 0.282 |
| B6 plain bge | 0.173 | 0.106 | 0.190 | 0.099 |
| SSE | 0.346 | 0.269 | 0.312 | 0.245 |
| SSE-hard | 0.222 | 0.145 | 0.212 | 0.139 |

### E5c — tone threshold as a dial

| method | monotonic | low | high |
|---|---|---|---|
| SSE | 1.000 | -0.120 | 0.173 |
| SSE-hard | 1.000 | -0.058 | 0.107 |
| B3 separate | 1.000 | -0.107 | 0.156 |
| B4 CSN | 1.000 | -0.129 | 0.169 |
| B1 labels | 0.079 | -0.000 | 0.007 |
| B1-soft | 1.000 | -0.082 | 0.144 |
| B2 text prompts | 0.964 | -0.048 | 0.088 |
| B6 plain bge | 1.000 | -0.035 | 0.093 |
