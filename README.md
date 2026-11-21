# news-image-20261121 — THE WORLD TODAY, Saturday 21 November 2026

[![news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/queenxaz/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/queenxaz/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121)

A program that draws one newspaper front page summing up the world's news of
Saturday 21 November 2026 — 48 stories, 6 regions, 7 fields — and writes it
to `/output/entry.png` (1024×1024 JPEG, deterministic, no network).

## What the page shows

- **3 big leads:** Russia's 100-missile barrage, one landing in Poland;
  Wall Street slides into correction as AI sells off; COP31 misses its deadline.
- **12 more illustrated stories** with flat drawings, each tagged how sure
  (CONFIRMED / REPORTED / CLAIM / OFFICIAL) and its source.
- **33 more in the also-on list** — 48 stories in all.
- **THE DAY IN UTC** timeline, a dotted world map with 16 numbered pins,
  a HOW SURE legend, BY REGION and BY FIELD counts, a day-in-numbers strip,
  and a **DATE CHECK** box listing what was deliberately left out (20 Nov and
  earlier: the Asian plunge, the Shenzhen trilateral, the ICJ Rohingya ruling,
  Kerch Bridge) and what has not happened yet (22 Nov).

## Run it

```bash
python3 main.py        # writes /output/entry.png
```

Pure Python 3.13 standard library + Pillow. Two runs write identical bytes.

## Entry

Built for the [make.fun](https://make.fun/bounty/news-image-20261121)
news-image-20261121 bounty by [@sakit](https://make.fun/@sakit).
