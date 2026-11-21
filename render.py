# THE WORLD TODAY — Saturday 21 November 2026
# Draws the day's newspaper front page with PIL. Deterministic: same bytes every run.
# SPDX-License-Identifier: MIT
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 243, 230)
INK = (17, 17, 17)
RED = (163, 22, 33)
BLUE = (30, 64, 175)
GOLD = (180, 83, 9)
TEAL = (15, 118, 110)
GREY = (90, 86, 76)
LIGHT = (238, 231, 214)
NAVY = (22, 35, 63)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_SERIF = lambda s: font("DejaVuSerif-Bold.ttf", s)
F_SERIF_I = lambda s: font("DejaVuSerif.ttf", s)
F_SANS = lambda s: font("DejaVuSans.ttf", s)
F_BOLD = lambda s: font("DejaVuSans-Bold.ttf", s)

# ---------------------------------------------------------------- data
# Every story below happened, or was first reported, on Sat 21 Nov 2026.
# Region tags drive the region bar; field tags drive the by-field strip.
LEADS = [
    {
        "region": "EUROPE", "field": "CONFLICT", "trust": "CONFIRMED",
        "source": "Reuters", "art": "missile",
        "headline": "RUSSIA'S 100-MISSILE BARRAGE — ONE LANDS IN POLAND",
        "summary": "A Kh-101 cruise missile crashes in south-east Poland as Moscow "
                   "pounds Ukraine. NATO jets scramble. Kyiv's three bridges hit; 9 dead.",
    },
    {
        "region": "AMERICAS", "field": "MARKETS", "trust": "CONFIRMED",
        "source": "CNBC", "art": "chart",
        "headline": "WALL STREET SLIDES INTO CORRECTION AS AI SELLS OFF",
        "summary": "S&P 500 -3.70%, Nasdaq -5.28%, Dow -1.93%. The SEC probes Nvidia "
                   "accounting; its shares fall 13.8%.",
    },
    {
        "region": "WORLD", "field": "CLIMATE", "trust": "REPORTED",
        "source": "Reuters", "art": "globe",
        "headline": "COP31 MISSES ITS DEADLINE — FOSSIL FUELS DROPPED",
        "summary": "The Antalya climate summit overruns as the political draft drops "
                   "any mention of fossil fuels.",
    },
]

# 12 more illustrated stories (pins 5-16 on the map).
CARDS = [
    {"pin": 5, "region": "MIDDLE EAST", "field": "CONFLICT", "trust": "REPORTED",
     "source": "Reuters", "icon": "tanker",
     "headline": "14 IRANIAN TANKERS MASS AT KHARG",
     "summary": "Convoy tests US blockade; strikes deferred."},
    {"pin": 6, "region": "MIDDLE EAST", "field": "CONFLICT", "trust": "CLAIM",
     "source": "Al Jazeera", "icon": "flame",
     "headline": "SAUDI-HOUTHI FIGHTING ESCALATES",
     "summary": "Strikes on 4 cities; 41 dead, 11 children."},
    {"pin": 7, "region": "EUROPE", "field": "DIPLOMACY", "trust": "CONFIRMED",
     "source": "BBC", "icon": "stars",
     "headline": "UK AND EU SEAL BRUSSELS DEALS",
     "summary": "Food checks end in 2028; mobility for 100,000."},
    {"pin": 9, "region": "AMERICAS", "field": "TECH", "trust": "REPORTED",
     "source": "AP", "icon": "chip",
     "headline": "TRUMP THREATENS AI DATACENTRE BAN",
     "summary": "US firms barred from AI centres abroad; huge tax."},
    {"pin": 10, "region": "ASIA", "field": "DIPLOMACY", "trust": "REPORTED",
     "source": "Reuters", "icon": "gear",
     "headline": "TRUMP-XI: HUMANS STAY IN THE LOOP",
     "summary": "Humans stay in loop on military AI decisions."},
    {"pin": 11, "region": "EUROPE", "field": "CONFLICT", "trust": "CLAIM",
     "source": "Kyiv", "icon": "target",
     "headline": "UKRAINE HITS BACK: 3 LAUNCHERS DOWN",
     "summary": "HIMARS wipes out 20 Russian commanders, a brigade HQ."},
    {"pin": 12, "region": "EUROPE", "field": "DIPLOMACY", "trust": "CONFIRMED",
     "source": "Reuters", "icon": "flag",
     "headline": "DENMARK SEALS US-GREENLAND PACT",
     "summary": "US-Greenland security pact ends months of strain."},
    {"pin": 13, "region": "ASIA", "field": "DIPLOMACY", "trust": "REPORTED",
     "source": "AP", "icon": "mega",
     "headline": "DHAKA BLAMES DELHI FOR VIOLENCE",
     "summary": "PM Tarique Rahman points at India and Awami League."},
    {"pin": 8, "region": "AMERICAS", "field": "TECH", "trust": "REPORTED",
     "source": "CNBC", "icon": "sigma",
     "headline": "ANTHROPIC 'SOLVES BIGGEST MATHS'",
     "summary": "In a year of AI maths wins, its latest proof tops them."},
    {"pin": 14, "region": "AMERICAS", "field": "SOCIETY", "trust": "OFFICIAL",
     "source": "Pentagon", "icon": "ufo",
     "headline": "US DECLASSIFIES MORE UFO FILM",
     "summary": "New Middle East footage released to the public."},
    {"pin": 15, "region": "EUROPE", "field": "CONFLICT", "trust": "CONFIRMED",
     "source": "Reuters", "icon": "shield",
     "headline": "EU GIVES €1BN FOR UKRAINE ARMS",
     "summary": "Peace Facility cash for Ukraine weapons."},
    {"pin": 16, "region": "MIDDLE EAST", "field": "CONFLICT", "trust": "REPORTED",
     "source": "AP", "icon": "fort",
     "headline": "IRAQ RETAKES JURF AL-SAKHAR",
     "summary": "Army retakes town after 12 years under Hezbollah."},
]

# Also-on items, numbered 16-48 in the paper.
ALSO = [
    ("AMERICAS", "LAW", "US judge blocks Trump's $4bn homeless-aid revamp"),
    ("EUROPE", "SOCIETY", "Estonia: 6,000 switch to Estonian citizenship"),
    ("EUROPE", "LAW", "French police sentenced for beating Michel Zecler"),
    ("EUROPE", "LAW", "Depardieu probed over sexual allegations"),
    ("EUROPE", "CONFLICT", "Denmark: Russia plotted to kill US-Ukrainian rapper"),
    ("AMERICAS", "LAW", "Indian man jailed 19 years in Sikh assassination plot"),
    ("AMERICAS", "LAW", "Mamdani: close New York's Rikers Island by 2032"),
    ("AFRICA", "DIPLOMACY", "ANC fights to hold South Africa's key cities"),
    ("AFRICA", "SOCIETY", "Ebola hits Congo children hardest; 100 schools hit"),
    ("AMERICAS", "DIPLOMACY", "Bukele set to formalise third-term bid"),
    ("ASIA", "TECH", "Taiwan: China-linked accounts target Meta votes"),
    ("AFRICA", "DIPLOMACY", "Morocco pledges €366m for home defence industry"),
    ("EUROPE", "DIPLOMACY", "Hungary lifts block on EU talks with Ukraine"),
    ("ASIA", "DIPLOMACY", "North Korea and Laos vow closer cooperation"),
    ("EUROPE", "LAW", "Tata faces criminal trial in the Netherlands"),
    ("MIDDLE EAST", "SOCIETY", "UN: Yemen's displaced reach 357,000 since August"),
    ("ASIA", "CONFLICT", "Four Afghan pupils killed by old munitions"),
    ("AMERICAS", "CONFLICT", "Two Salvadorans killed in Haiti blast"),
    ("AFRICA", "SOCIETY", "600 women killed in South Africa in three months"),
    ("AMERICAS", "CLIMATE", "US opens Pacific seabed to deep-sea mining"),
    ("EUROPE", "LAW", "Croatia charges three in daycare fraud probe"),
    ("MIDDLE EAST", "CONFLICT", "Palestinian shot dead by settler guard"),
    ("EUROPE", "CONFLICT", "Czechia weighs faster air-defence build-up"),
    ("ASIA", "CLIMATE", "Korea's coal use rises amid the Iran war"),
    ("ASIA", "DIPLOMACY", "Malaysia pulls Rohingya resettlement post"),
    ("EUROPE", "DIPLOMACY", "France probes ministry leaks on National Rally"),
    ("MIDDLE EAST", "CONFLICT", "Gaza Civil Defence struggles as cars fail"),
    ("AMERICAS", "SOCIETY", "Dead pets meant for cremation appear on livestream"),
    ("ASIA", "DIPLOMACY", "Nepal's Shah faces his India test"),
    ("AMERICAS", "LAW", "$811m migrant-scam fines fail to stop the scams"),
    ("AMERICAS", "DIPLOMACY", "Air Force One press told to hand over phones"),
    ("AMERICAS", "TECH", "California subpoenas Nvidia over China chip deals"),
    ("EUROPE", "SOCIETY", "Russia unveils first memorial at a kindergarten"),
]

TIMELINE = [
    ("01:10", "Poland airspace probe"),
    ("02:58", "100 missiles fired"),
    ("03:31", "Ebola in Congo"),
    ("04:22", "Judge blocks Trump plan"),
    ("04:59", "Iran war into 2027"),
    ("21:00", "Wall St in correction"),
]

NUMBERS = [
    ("100", "missiles fired at Ukraine"),
    ("-5.28%", "Nasdaq in one day"),
    ("-13.8%", "Nvidia shares"),
    ("14", "tankers at Kharg"),
    ("41", "claimed dead in Yemen"),
    ("100,000", "youth-mobility places"),
]

LEFT_OUT = [
    "Asian plunge (Nikkei -4.8%)",
    "Shenzhen trilateral",
    "ICJ Rohingya ruling",
    "Kerch Bridge 3rd strike",
    "Anthropic IPO debut",
    "GTA VI release",
    "Italy fines Meta €805m",
    "FAA ground stop",
    "Gaza Yellow Line",
    "Voyager 1 one light-day",
]

NOT_YET = [
    "COP31 final deal",
    "NATO chief's visit",
    "SpaceX splashdown",
    "Thanksgiving market closure",
    "Fed rate decision",
    "Trump-Putin follow-up",
]

SOURCES = ("Reuters · AP · BBC · CNBC · AFP · Bloomberg · Al Jazeera · Euronews · "
           "Axios · GOV.UK · UN News · NASA")

# Map pins: (grid col, grid row) on a 64 x 26 world grid.
PINS = {
    1: (34, 4), 2: (36, 5), 3: (10, 6), 4: (37, 7),
    5: (43, 9), 6: (41, 11), 7: (32, 5), 8: (5, 7),
    9: (9, 7), 10: (51, 9), 11: (36, 4), 12: (33, 4),
    13: (46, 9), 14: (9, 7), 15: (32, 5), 16: (42, 8),
}
PIN_DX = {14: 7, 15: -7}  # nudge the two doubled-up pins apart

# Landmass as (row, col_start, col_end) spans on the 64 x 26 grid.
LAND = [
    (0, 8, 12), (0, 18, 20), (0, 40, 58),
    (1, 6, 14), (1, 19, 21), (1, 38, 60),
    (2, 5, 15), (2, 20, 22), (2, 36, 60),
    (3, 4, 16), (3, 30, 33), (3, 36, 58),
    (4, 3, 16), (4, 29, 34), (4, 36, 56),
    (5, 3, 15), (5, 29, 35), (5, 37, 55),
    (6, 4, 14), (6, 29, 36), (6, 38, 54),
    (7, 5, 13), (7, 29, 37), (7, 39, 52),
    (8, 6, 12), (8, 30, 38), (8, 40, 50),
    (9, 7, 12), (9, 31, 37), (9, 41, 49),
    (10, 8, 12), (10, 32, 36), (10, 42, 48),
    (11, 9, 13), (11, 33, 36), (11, 43, 47),
    (12, 10, 13), (12, 33, 37), (12, 44, 47),
    (13, 12, 15), (13, 33, 38), (13, 44, 46),
    (14, 13, 16), (14, 34, 38), (14, 45, 47),
    (15, 13, 17), (15, 34, 38), (15, 46, 48),
    (16, 14, 17), (16, 34, 37), (16, 47, 50),
    (17, 14, 17), (17, 35, 37), (17, 50, 54),
    (18, 14, 17), (18, 35, 37), (18, 50, 55),
    (19, 15, 17), (19, 35, 36), (19, 51, 55),
    (20, 15, 17), (20, 35, 36), (20, 52, 54),
    (21, 15, 17), (21, 35, 36),
    (22, 16, 17),
    (23, 16, 16),
    (24, 16, 16),
    (25, 16, 16),
]

# ---------------------------------------------------------------- helpers

def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, color, max_w, leading, max_lines=None):
    """Draw wrapped text; returns y just below the last line.
    With max_lines, extra lines are dropped (last kept line gets ...)."""
    lines = wrap(draw, text, fnt, max_w)
    if max_lines is not None and len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1].rstrip(". ") + "..."
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def pill(draw, x, y, label, fnt, fg, bg):
    w = draw.textlength(label, font=fnt) + 12
    h = fnt.size + 7
    draw.rounded_rectangle([x, y, x + w, y + h], radius=3, fill=bg)
    draw.text((x + 6, y + 3), label, font=fnt, fill=fg)
    return w


def draw_missile_art(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=NAVY)
    for sx, sy in [(18, 14), (60, 30), (110, 10), (150, 34), (200, 12),
                   (250, 28), (290, 16), (40, 48), (170, 50)]:
        d.ellipse([x + sx, y + sy, x + sx + 2, y + sy + 2], fill=(220, 220, 200))
    # three missile trails streaking down-right
    for (x0, y0, x1, y1) in [(30, 6, 120, 66), (120, 0, 210, 58), (210, 10, 300, 70)]:
        d.line([x + x0, y + y0, x + x1, y + y1], fill=(255, 255, 255), width=3)
        d.ellipse([x + x1 - 4, y + y1 - 4, x + x1 + 4, y + y1 + 4],
                  fill=(255, 200, 60))
    # explosion burst over a bridge silhouette
    cx, cy = x + w - 52, y + h - 42
    for k in range(8):
        ang = k * 3.14159 / 4
        ex = cx + int(26 * (1 if k % 2 == 0 else 0.55) * (1 if ang < 3.2 else -1))
        ey = cy + int(26 * (1 if k % 2 == 0 else 0.55) * (1 if 0.8 < ang < 2.4 else -1))
        d.line([cx, cy, ex, ey], fill=(255, 140, 40), width=4)
    d.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], fill=(255, 190, 60))
    d.rectangle([x, y + h - 14, x + w, y + h], fill=(10, 14, 26))
    for bx in range(8, w - 8, 26):
        d.arc([x + bx, y + h - 30, x + bx + 22, y + h - 6], 180, 360,
              fill=(10, 14, 26), width=4)


def draw_chart_art(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(255, 255, 255))
    for gy in range(4):
        yy = y + 14 + gy * 22
        d.line([x + 10, yy, x + w - 10, yy], fill=(225, 225, 215), width=1)
    bars = [62, 52, 44, 34, 22, 12]
    bw = (w - 40) // len(bars)
    for i, bh in enumerate(bars):
        bx = x + 20 + i * bw
        d.rectangle([bx, y + h - 18 - bh, bx + bw - 8, y + h - 18], fill=RED)
    d.line([x + 20, y + 16, x + w - 24, y + h - 24], fill=(120, 20, 20), width=4)
    d.polygon([(x + w - 24, y + h - 24), (x + w - 40, y + h - 30),
               (x + w - 34, y + h - 12)], fill=(120, 20, 20))
    d.text((x + w - 74, y + 6), "-5.28%", font=F_BOLD(15), fill=RED)


def draw_globe_art(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=TEAL)
    cx, cy, r = x + w // 2 - 18, y + h // 2 + 4, 40
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(248, 243, 230))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(10, 90, 82), width=2)
    d.arc([cx - r, cy - r, cx + r, cy + r], 90, 270, fill=(10, 90, 82), width=2)
    d.ellipse([cx - 14, cy - r, cx + 14, cy + r], outline=(10, 90, 82), width=2)
    d.line([cx - r, cy, cx + r, cy], fill=(10, 90, 82), width=2)
    d.line([cx - r + 8, cy - 26, cx + r - 8, cy - 26], fill=(10, 90, 82), width=2)
    d.line([cx - r + 8, cy + 26, cx + r - 8, cy + 26], fill=(10, 90, 82), width=2)
    # a small sun, top right
    sx, sy = x + w - 34, y + 20
    d.ellipse([sx - 9, sy - 9, sx + 9, sy + 9], fill=(255, 200, 60))
    for k in range(8):
        ang = k * 3.14159 / 4
        d.line([sx + int(13 * (1 if ang < 3.2 else -1)) if k % 2 == 0 else sx,
                sy + int(13 * (1 if 0.8 < ang < 2.4 else -1)) if k % 2 else sy,
                sx + int(18 * (1 if ang < 3.2 else -1)) if k % 2 == 0 else sx,
                sy + int(18 * (1 if 0.8 < ang < 2.4 else -1)) if k % 2 else sy],
               fill=(255, 200, 60), width=2)
    # calendar page with a red X
    px, py = x + w - 66, y + h - 40
    d.rectangle([px, py, px + 44, py + 30], fill=(255, 255, 255),
                outline=(17, 17, 17), width=2)
    d.rectangle([px, py, px + 44, py + 9], fill=RED)
    d.line([px + 10, py + 15, px + 34, py + 26], fill=RED, width=3)
    d.line([px + 34, py + 15, px + 10, py + 26], fill=RED, width=3)


ART = {"missile": draw_missile_art, "chart": draw_chart_art, "globe": draw_globe_art}


def draw_icon(d, x, y, kind, s=26):
    """Tiny flat glyph in a 26x26 box."""
    d.rectangle([x, y, x + s, y + s], fill=LIGHT, outline=(200, 192, 172))
    c = INK
    if kind == "tanker":
        d.polygon([(x + 3, y + 17), (x + 23, y + 17), (x + 20, y + 22),
                   (x + 6, y + 22)], fill=c)
        d.rectangle([x + 6, y + 10, x + 12, y + 16], fill=RED)
        d.rectangle([x + 14, y + 12, x + 19, y + 16], fill=BLUE)
        d.line([x + 2, y + 24, x + 24, y + 24], fill=BLUE, width=2)
    elif kind == "flame":
        d.polygon([(x + 13, y + 3), (x + 19, y + 12), (x + 22, y + 18),
                   (x + 16, y + 23), (x + 9, y + 23), (x + 4, y + 17),
                   (x + 8, y + 11)], fill=(220, 90, 20))
        d.ellipse([x + 10, y + 14, x + 16, y + 21], fill=(255, 200, 60))
    elif kind == "stars":
        import math
        for k in range(8):
            a = k * math.pi / 4
            px = x + 13 + int(9 * math.cos(a))
            py = y + 13 + int(9 * math.sin(a))
            d.ellipse([px - 1, py - 1, px + 1, py + 1], fill=BLUE)
        d.ellipse([x + 11, y + 11, x + 15, y + 15], fill=GOLD)
    elif kind == "chip":
        d.rectangle([x + 7, y + 7, x + 19, y + 19], fill=c)
        d.rectangle([x + 11, y + 11, x + 15, y + 15], fill=LIGHT)
        for px in (10, 16):
            d.line([x + px, y + 3, x + px, y + 7], fill=c, width=2)
            d.line([x + px, y + 19, x + px, y + 23], fill=c, width=2)
        for py in (10, 16):
            d.line([x + 3, y + py, x + 7, y + py], fill=c, width=2)
            d.line([x + 19, y + py, x + 23, y + py], fill=c, width=2)
    elif kind == "gear":
        d.ellipse([x + 6, y + 6, x + 20, y + 20], outline=c, width=3)
        d.ellipse([x + 10, y + 10, x + 16, y + 16], fill=c)
        for px, py in [(13, 3), (13, 21), (3, 13), (21, 13)]:
            d.line([x + px, y + py, x + 13, y + 13], fill=c, width=3)
    elif kind == "target":
        for r, col in [(9, RED), (6, (255, 255, 255)), (3, RED)]:
            d.ellipse([x + 13 - r, y + 13 - r, x + 13 + r, y + 13 + r],
                      outline=col, width=2)
        d.ellipse([x + 12, y + 12, x + 14, y + 14], fill=RED)
    elif kind == "flag":
        d.line([x + 6, y + 4, x + 6, y + 23], fill=c, width=2)
        d.rectangle([x + 6, y + 5, x + 22, y + 14], fill=RED)
        d.line([x + 6, y + 9, x + 22, y + 9], fill=(255, 255, 255), width=2)
        d.line([x + 12, y + 5, x + 12, y + 14], fill=(255, 255, 255), width=2)
    elif kind == "mega":
        d.polygon([(x + 4, y + 10), (x + 18, y + 4), (x + 18, y + 16),
                   (x + 4, y + 16)], fill=RED)
        d.rectangle([x + 18, y + 8, x + 22, y + 16], fill=c)
        d.line([x + 8, y + 17, x + 8, y + 22], fill=c, width=2)
    elif kind == "sigma":
        d.text((x + 5, y + 2), "Σ", font=F_BOLD(19), fill=BLUE)
    elif kind == "ufo":
        d.ellipse([x + 3, y + 12, x + 23, y + 19], fill=c)
        d.pieslice([x + 8, y + 5, x + 18, y + 15], 180, 360, fill=(150, 190, 220))
        for lx in (8, 13, 18):
            d.ellipse([x + lx - 1, y + 14, x + lx + 1, y + 16], fill=(255, 200, 60))
    elif kind == "shield":
        d.polygon([(x + 13, y + 3), (x + 21, y + 7), (x + 21, y + 14),
                   (x + 13, y + 23), (x + 5, y + 14), (x + 5, y + 7)], fill=BLUE)
        d.line([x + 9, y + 13, x + 12, y + 16], fill=(255, 255, 255), width=2)
        d.line([x + 12, y + 16, x + 18, y + 9], fill=(255, 255, 255), width=2)
    elif kind == "fort":
        d.rectangle([x + 4, y + 10, x + 22, y + 23], fill=c)
        for bx in (4, 10, 16):
            d.rectangle([x + bx, y + 6, x + bx + 4, y + 10], fill=c)
        d.rectangle([x + 11, y + 16, x + 15, y + 23], fill=LIGHT)


def draw_map(d, x0, y0, w, h):
    """Dotted world map with numbered pins."""
    cw, ch = w / 64.0, h / 26.0
    for (r, c0, c1) in LAND:
        for c in range(c0, c1 + 1):
            cx = x0 + c * cw + cw / 2
            cy = y0 + r * ch + ch / 2
            d.ellipse([cx - 1.4, cy - 1.4, cx + 1.4, cy + 1.4], fill=(120, 110, 90))
    for num, (c, r) in PINS.items():
        cx = x0 + c * cw + cw / 2 + PIN_DX.get(num, 0)
        cy = y0 + r * ch + ch / 2
        d.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=RED,
                  outline=(255, 255, 255), width=1)
        t = str(num)
        tw = d.textlength(t, font=F_BOLD(9))
        d.text((cx - tw / 2, cy - 5), t, font=F_BOLD(9), fill=(255, 255, 255))

# ---------------------------------------------------------------- build

def counts():
    regions, fields = {}, {}
    all_stories = [(l["region"], l["field"]) for l in LEADS]
    all_stories += [(c["region"], c["field"]) for c in CARDS]
    all_stories += [(r, f) for (r, f, _t) in ALSO]
    for r, f in all_stories:
        regions[r] = regions.get(r, 0) + 1
        fields[f] = fields.get(f, 0) + 1
    return regions, fields


def build(path):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([6, 6, W - 7, H - 7], outline=INK, width=3)

    regions, fields = counts()
    total = len(LEADS) + len(CARDS) + len(ALSO)

    # ---- masthead
    d.text((W // 2, 12), "THE WORLD TODAY", font=F_SERIF(46), fill=INK,
           anchor="ma")
    d.line([16, 66, W - 16, 66], fill=INK, width=2)
    d.line([16, 70, W - 16, 70], fill=INK, width=1)
    d.text((16, 76), "SATURDAY 21 NOVEMBER 2026", font=F_BOLD(16), fill=INK)
    right = "%d STORIES · %d REGIONS · %d FIELDS" % (total, len(regions),
                                                     len(fields))
    d.text((W - 16, 76), right, font=F_BOLD(16), fill=RED, anchor="ra")
    sub = ("Russia's barrage reaches Poland, Wall Street slides into correction, "
           "COP31 misses its deadline — every story here happened on this day.")
    d.text((W // 2, 98), sub, font=F_SERIF_I(13), fill=INK, anchor="ma")

    # ---- UTC timeline strip
    d.rectangle([16, 122, W - 16, 150], fill=INK)
    d.text((26, 129), "THE DAY IN UTC", font=F_BOLD(10), fill=(255, 200, 60))
    tx = 146
    for t, label in TIMELINE:
        d.text((tx, 129), t, font=F_BOLD(10), fill=(255, 255, 255))
        tw = d.textlength(t, font=F_BOLD(10))
        d.text((tx + tw + 4, 129), label, font=F_SANS(10),
               fill=(235, 230, 215))
        tx += tw + 4 + d.textlength(label, font=F_SANS(10)) + 10

    # ---- three big leads
    ly, lh = 158, 214
    lw = (W - 32 - 2 * 12) // 3
    for i, lead in enumerate(LEADS):
        x = 16 + i * (lw + 12)
        d.rectangle([x, ly, x + lw, ly + lh], outline=INK, width=2)
        ART[lead["art"]](d, x + 1, ly + 1, lw - 2, 96)
        y = ly + 104
        pill(d, x + 8, y, lead["region"], F_BOLD(10), (255, 255, 255), RED)
        tag = "%s — %s" % (lead["trust"], lead["source"])
        d.text((x + lw - 8, y + 2), tag, font=F_BOLD(10), fill=BLUE,
               anchor="ra")
        y += 22
        y = text_block(d, x + 8, y, lead["headline"], F_BOLD(15), INK,
                       lw - 16, 18, max_lines=2)
        text_block(d, x + 8, y + 2, lead["summary"], F_SANS(11), INK,
                   lw - 16, 14, max_lines=3)

    # ---- map panel (left) + 12 illustrated cards (right)
    my = 380
    d.rectangle([16, my, 330, my + 220], outline=INK, width=2)
    d.text((22, my + 6), "THE WORLD — 16 STORIES PINNED", font=F_BOLD(12),
           fill=INK)
    d.text((22, my + 24), "HOW SURE: CONFIRMED = verified by two outlets",
           font=F_SANS(9), fill=GREY)
    d.text((22, my + 35), "REPORTED = one outlet · CLAIM = one side · "
           "OFFICIAL = govt", font=F_SANS(9), fill=GREY)
    draw_map(d, 22, my + 52, 302, 160)

    cx0, cy0 = 342, my
    cw = (W - 16 - cx0 - 2 * 8) // 3
    chh = 220 // 4
    for i, card in enumerate(CARDS):
        col, row = i % 3, i // 3
        x = cx0 + col * (cw + 8)
        y = cy0 + row * chh
        d.rectangle([x, y, x + cw, y + chh - 3], outline=(200, 192, 172),
                    width=1)
        draw_icon(d, x + 5, y + 5, card["icon"])
        hx = x + 36
        y = text_block(d, hx, y + 3, "%d. %s" % (card["pin"], card["headline"]),
                       F_BOLD(10), INK, cw - 41, 12, max_lines=2)
        full = "%s: %s — %s" % (card["trust"], card["summary"], card["source"])
        text_block(d, hx, y, full, F_SANS(9), GREY, cw - 41, 11,
                   max_lines=2)

    # ---- also-on list, numbered 16-48
    ay = 608
    d.text((16, ay), "ALSO ON 21 NOVEMBER", font=F_BOLD(13), fill=INK)
    d.line([16, ay + 20, W - 16, ay + 20], fill=INK, width=2)
    col_w = (W - 32) // 2
    f_item = F_SANS(11)
    for i, (_r, _f, text) in enumerate(ALSO):
        col, row = i % 2, i // 2
        x = 16 + col * col_w
        y = ay + 26 + row * 12
        d.text((x, y), "%d. %s" % (16 + i, text), font=f_item, fill=INK)

    # ---- day in numbers
    ny = 844
    d.rectangle([16, ny, W - 16, ny + 44], fill=INK)
    d.text((26, ny + 5), "THE DAY IN NUMBERS", font=F_BOLD(11),
           fill=(255, 200, 60))
    nx = 26
    for big, label in NUMBERS:
        d.text((nx, ny + 20), big, font=F_BOLD(13), fill=(255, 255, 255))
        bw = d.textlength(big, font=F_BOLD(13))
        d.text((nx + bw + 4, ny + 21), label, font=F_SANS(10),
               fill=(235, 230, 215))
        nx += bw + 4 + d.textlength(label, font=F_SANS(10)) + 14

    # ---- region / field bars
    by = 894
    reg = "  ·  ".join("%s %d" % (r, n) for r, n in
                       sorted(regions.items(), key=lambda kv: -kv[1]))
    d.text((16, by), "BY REGION:  " + reg, font=F_BOLD(11), fill=INK)
    fld = "  ·  ".join("%s %d" % (f, n) for f, n in
                       sorted(fields.items(), key=lambda kv: -kv[1]))
    d.text((16, by + 15), "BY FIELD:  " + fld, font=F_BOLD(11), fill=INK)

    # ---- DATE CHECK box
    dy = 926
    d.rectangle([16, dy, W - 16, dy + 68], outline=RED, width=2)
    d.rectangle([16, dy, W - 16, dy + 18], fill=RED)
    d.text((W // 2, dy + 2), "DATE CHECK — WHAT WE LEFT OUT, AND WHAT HAS NOT HAPPENED YET",
           font=F_BOLD(11), fill=(255, 255, 255), anchor="ma")
    d.text((24, dy + 22), "LEFT OUT (20 Nov and earlier):",
           font=F_BOLD(10), fill=RED)
    text_block(d, 24, dy + 35, "; ".join(LEFT_OUT), F_SANS(9), INK, 476,
               11, max_lines=3)
    d.text((524, dy + 22), "NOT YET (22 Nov):", font=F_BOLD(10), fill=RED)
    text_block(d, 524, dy + 35, "; ".join(NOT_YET), F_SANS(9), INK, 476,
               11, max_lines=3)

    # ---- sources footer
    d.text((16, 1000), "SOURCES: " + SOURCES, font=F_SANS(9), fill=GREY)
    d.text((W - 16, 1000), "Original drawings.", font=F_SANS(9), fill=GREY,
           anchor="ra")

    img.save(path, "JPEG", quality=88, optimize=True)
    return path


if __name__ == "__main__":
    import sys
    build(sys.argv[1] if len(sys.argv) > 1 else "entry.jpg")
