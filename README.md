# news-image-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/danzz-ai/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/danzz-ai/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

One image that sums up the world's news of Saturday 21 November 2026: Iran's missile-and-drone strikes on US positions in Bahrain, COP31 climate talks in Antalya closing in on a final deal, Mexico capturing 'El Chapo Isidro' with 11 dead, Russian missiles hitting Kryvyi Rih with debris landing in Poland, the Nasdaq AI sell-off's worst week since March 2020, and a dengue breakthrough in Brazil — plus the day's other big stories in the ticker below.

## The image

A newspaper front page, dated **SATURDAY, 21 NOVEMBER 2026 — THE WORLD TODAY**. The hero panel shows the night sky over Bahrain under Iran's missile-and-drone attack on the US bases at Al-Riffa and Awali. Below it, five panels: COP31 in Antalya, the 'El Chapo Isidro' capture in Mexico, the Kryvyi Rih strike and debris in Poland, the Nasdaq AI sell-off, and Brazil's dengue breakthrough. The "ALSO TODAY" strip covers the Sparta II cargo ship fire in the Gulf of Finland, the Nigeria boat capsizes, the Rohingya genocide verdict, the Shenzhen summit aftermath, and the death of Paolo Bulgari. Every story was reported on 21 November 2026.

The image was drawn with `render_front_page.py` (Python + Pillow) so every headline and the date are crisp and legible — no garbled text.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) copies `entry.png` to `/output/entry.png`. The output is a JPEG (1024×1024, ~209 KB), inside the gate limits (≤ 1 MiB, ≤ 1024×1024). Running it twice produces byte-identical output: it is a plain file copy with a size check.

---

<sub>Entered on [make.fun](https://make.fun/?ref=magsnez0&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
