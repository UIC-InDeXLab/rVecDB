# MovieLens results (seed 1)

### E1 — Spearman of each view vs each true facet

| method | view | genre | tone | theme | style |
|---|---|---|---|---|---|
| SSE | genre | 0.347 | 0.213 | 0.310 | 0.194 |
| SSE | tone | 0.271 | 0.274 | 0.285 | 0.213 |
| SSE | theme | 0.277 | 0.194 | 0.313 | 0.177 |
| SSE | style | 0.250 | 0.229 | 0.274 | 0.253 |
| SSE-hard | genre | 0.226 | 0.141 | 0.220 | 0.125 |
| SSE-hard | tone | 0.204 | 0.146 | 0.206 | 0.119 |
| SSE-hard | theme | 0.198 | 0.123 | 0.210 | 0.106 |
| SSE-hard | style | 0.190 | 0.143 | 0.201 | 0.143 |
| B3 separate | genre | 0.346 | 0.214 | 0.311 | 0.193 |
| B3 separate | tone | 0.271 | 0.275 | 0.287 | 0.214 |
| B3 separate | theme | 0.281 | 0.195 | 0.315 | 0.174 |
| B3 separate | style | 0.256 | 0.229 | 0.279 | 0.252 |
| B4 CSN | genre | 0.392 | 0.235 | 0.335 | 0.215 |
| B4 CSN | tone | 0.294 | 0.308 | 0.299 | 0.236 |
| B4 CSN | theme | 0.312 | 0.222 | 0.349 | 0.206 |
| B4 CSN | style | 0.267 | 0.249 | 0.287 | 0.286 |
| B1 labels | genre | 0.007 | 0.008 | 0.011 | 0.007 |
| B1 labels | tone | -0.004 | 0.034 | 0.010 | 0.021 |
| B1 labels | theme | 0.042 | 0.040 | 0.051 | 0.033 |
| B1 labels | style | 0.074 | 0.015 | 0.055 | 0.041 |
| B1-soft | genre | 0.334 | 0.167 | 0.269 | 0.143 |
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
| SSE | 0.750 |
| B4 CSN | 0.633 |

### E4 — filter on one facet (ref x), rank on another (ref q); graded truth

| method | predicate_F1 | predicate_AP | P@10_feasible | NDCG@10 |
|---|---|---|---|---|
| SSE | 0.352 | 0.345 | 0.316 | 0.124 |
| SSE-hard | 0.304 | 0.293 | 0.282 | 0.097 |
| B3 separate | 0.354 | 0.347 | 0.317 | 0.119 |
| B4 CSN | 0.364 | 0.361 | 0.320 | 0.129 |
| B1 labels | 0.184 | 0.185 | 0.170 | 0.036 |
| B1-soft | 0.331 | 0.324 | 0.278 | 0.091 |
| B2 text prompts | 0.251 | 0.248 | 0.296 | 0.086 |
| B6 plain bge | 0.293 | 0.280 | 0.249 | 0.092 |

### E5b — in-between similarity among pairs whose yes/no tags differ

| method | genre | tone | theme | style |
|---|---|---|---|---|
| B1 labels | 0.007 | 0.033 | 0.051 | 0.039 |
| B1-soft | 0.333 | 0.215 | 0.280 | 0.199 |
| B2 text prompts | 0.105 | 0.067 | 0.099 | 0.035 |
| B3 separate | 0.344 | 0.275 | 0.315 | 0.250 |
| B4 CSN | 0.391 | 0.308 | 0.350 | 0.284 |
| B6 plain bge | 0.173 | 0.106 | 0.190 | 0.099 |
| SSE | 0.346 | 0.274 | 0.313 | 0.251 |
| SSE-hard | 0.226 | 0.147 | 0.210 | 0.142 |

### E5c — tone threshold as a dial

| method | monotonic | low | high |
|---|---|---|---|
| SSE | 1.000 | -0.121 | 0.173 |
| SSE-hard | 1.000 | -0.058 | 0.106 |
| B3 separate | 1.000 | -0.108 | 0.157 |
| B4 CSN | 1.000 | -0.130 | 0.168 |
| B1 labels | 0.042 | -0.001 | 0.007 |
| B1-soft | 1.000 | -0.083 | 0.144 |
| B2 text prompts | 0.964 | -0.048 | 0.088 |
| B6 plain bge | 1.000 | -0.035 | 0.093 |
