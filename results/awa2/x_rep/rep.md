### Q4: SELECT REP(g,5), COUNT(*) FROM Animals GROUP BY_4 E_habitat  (SSE, seed 0, 6000 test images)

| group | COUNT(*) | true habitat (avg, top 3) | REP(g,5): medoid species (count) | top species in group |
|---|---|---|---|---|
| 2 | 2647 | ground, fields, plains | pig (766); persian+cat (627); deer (622); zebra (338); collie (294) | pig (329), persian+cat (329), rat (153), horse (150) |
| 0 | 1336 | ground, jungle, bush | leopard (419); giant+panda (410); hippopotamus (328); elephant (94); leopard (85) | giant+panda (407), leopard (323), hippopotamus (254), elephant (94) |
| 3 | 1169 | water, ocean, arctic | humpback+whale (342); seal (305); seal (244); polar+bear (164); dolphin (114) | seal (461), humpback+whale (314), dolphin (95), polar+bear (85) |
| 1 | 848 | forest, tree, jungle | chimpanzee (246); raccoon (246); chimpanzee (191); squirrel (117); bobcat (48) | chimpanzee (334), raccoon (141), squirrel (113), gorilla (80) |
