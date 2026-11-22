#!/usr/bin/env python3
"""Draw the news-image-20261121 front page: 'The World Today — 21 November 2026'.

A newspaper front page rendered with PIL so every headline and the date are
crisp and legible. Output: entry.png (a JPEG, 1024x1024, under 1 MiB).
All stories were reported on Saturday 21 November 2026.
"""
import os
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

PAPER = (247, 243, 233)
INK = (17, 17, 17)
RED = (179, 32, 44)
GREY = (90, 86, 78)
PANEL = (255, 253, 246)
HERO_BG = (14, 26, 46)
HERO_BG2 = (28, 48, 84)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_center(draw, cx, y, text, fnt, fill):
    draw.text((cx - draw.textlength(text, font=fnt) / 2, y), text, font=fnt, fill=fill)


def hero_art(base):
    """Night sky over Bahrain: missile arcs, explosion glow, base silhouette."""
    art = Image.new("RGB", (968, 112), HERO_BG2)
    d = ImageDraw.Draw(art)
    # sky gradient bands
    for i in range(112):
        t = i / 111
        d.line([(0, i), (968, i)],
               fill=(int(14 + 22 * t), int(26 + 30 * t), int(46 + 46 * t)))
    rng = random.Random(21112026)
    for _ in range(70):
        x, y = rng.randint(0, 967), rng.randint(0, 60)
        r = rng.choice([1, 1, 2])
        d.ellipse([x - r, y - r, x + r, y + r], fill=(220, 225, 240))
    # explosion glow, left third
    glow = Image.new("RGB", (968, 112), (0, 0, 0))
    gd = ImageDraw.Draw(glow)
    for r, col in ((64, (255, 120, 20)), (44, (255, 170, 40)), (26, (255, 220, 120))):
        gd.ellipse([150 - r, 96 - r, 150 + r, 96 + r], fill=col)
    glow = glow.filter(ImageFilter.GaussianBlur(14))
    art = Image.blend(art, Image.composite(glow, Image.new("RGB", (968, 112), (0, 0, 0)),
                                            glow.convert("L").point(lambda v: v)), 0.85)
    d = ImageDraw.Draw(art)
    # missile arcs with bright heads
    for x0, y0, x1, y1, col in ((700, 8, 880, 78, (255, 200, 90)),
                                (620, 4, 760, 66, (235, 240, 255)),
                                (820, 12, 940, 60, (255, 160, 60))):
        d.arc([x0, y0 - 70, x1 + 60, y1 + 40], start=200, end=330, fill=col, width=3)
        d.ellipse([x1 - 4, y1 - 4, x1 + 4, y1 + 4], fill=(255, 240, 200))
    # base silhouette along the bottom
    for x, w, h in ((0, 90, 26), (110, 60, 38), (200, 130, 22), (360, 70, 34),
                    (470, 110, 24), (620, 80, 40), (730, 120, 26), (880, 88, 36)):
        d.rectangle([x, 112 - h, x + w, 112], fill=(6, 10, 20))
    d.rectangle([700, 112 - 52, 706, 112], fill=(6, 10, 20))  # tower
    d.rectangle([690, 112 - 56, 716, 112 - 52], fill=(6, 10, 20))
    return art


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([6, 6, W - 7, H - 7], outline=INK, width=3)

    # ---- masthead ----
    draw_center(d, W // 2, 14, "THE WORLD TODAY", font(SERIF_B, 74), INK)
    d.line([(28, 112), (996, 112)], fill=INK, width=3)
    d.line([(28, 118), (996, 118)], fill=INK, width=1)
    draw_center(d, W // 2, 128, "SATURDAY, 21 NOVEMBER 2026",
                font(SANS_B, 30), RED)
    d.line([(28, 168), (996, 168)], fill=INK, width=2)

    # ---- hero ----
    hx0, hy0, hx1, hy1 = 28, 180, 996, 520
    d.rectangle([hx0, hy0, hx1, hy1], fill=HERO_BG)
    d.text((hx0 + 20, hy0 + 12), "MIDDLE EAST  •  LEAD STORY",
           font=font(SANS_B, 19), fill=(255, 190, 90))
    d.text((hx0 + 20, hy0 + 42), "IRAN STRIKES U.S. BASES",
           font=font(SERIF_B, 56), fill=(255, 255, 255))
    d.text((hx0 + 20, hy0 + 102), "IN BAHRAIN",
           font=font(SERIF_B, 56), fill=(255, 255, 255))
    deck = ("IRGC missiles and drones hit Al-Riffa and Awali; a civilian plant "
            "burns, no one hurt — Gulf defences intercept the rest.")
    y = hy0 + 168
    for line in wrap(d, deck, font(SANS, 21), hx1 - hx0 - 40):
        d.text((hx0 + 20, y), line, font=font(SANS, 21), fill=(215, 222, 235))
        y += 27
    img.paste(hero_art(img), (hx0, hy1 - 112))

    # ---- panels ----
    def panel(x0, y0, x1, y1, kicker, headline, deck_text, head_size=26):
        d.rectangle([x0, y0, x1, y1], fill=PANEL, outline=(150, 146, 136), width=1)
        d.text((x0 + 14, y0 + 10), kicker, font=font(SANS_B, 16), fill=RED)
        y = y0 + 34
        for line in wrap(d, headline, font(SERIF_B, head_size), x1 - x0 - 28):
            d.text((x0 + 14, y), line, font=font(SERIF_B, head_size), fill=INK)
            y += head_size + 6
        y += 4
        for line in wrap(d, deck_text, font(SANS, 18), x1 - x0 - 28):
            d.text((x0 + 14, y), line, font=font(SANS, 18), fill=(52, 50, 46))
            y += 22

    d.line([(28, 536), (996, 536)], fill=INK, width=2)
    panel(28, 548, 340, 732, "COP31  •  ANTALYA",
          "Climate talks close in on a final deal",
          "Negotiators in Antalya push through the night as COP31 nears agreement.")
    panel(356, 548, 668, 732, "MEXICO",
          "‘El Chapo Isidro’ captured; 11 dead",
          "Troops seize the cartel boss in a raid that leaves eleven dead.")
    panel(684, 548, 996, 732, "UKRAINE  •  POLAND",
          "Russian missiles hit Kryvyi Rih; debris lands in Poland",
          "Strike hits Kryvyi Rih as missile parts fall in Poland.", head_size=24)
    d.line([(28, 748), (996, 748)], fill=INK, width=2)
    panel(28, 760, 502, 904, "MARKETS",
          "Nasdaq AI sell-off: worst week since March 2020",
          "AI shares lead a global rout as investors flee richly valued tech.")
    panel(522, 760, 996, 904, "BRAZIL",
          "Dengue breakthrough",
          "Brazil reports a dengue breakthrough in the fight against the mosquito-borne disease.")

    # ---- ticker ----
    tick1 = "Sparta II ship fire, Gulf of Finland  •  Nigeria boat capsizes  •  Rohingya genocide verdict"
    tick2 = "Shenzhen summit aftermath  •  Paolo Bulgari dies"
    d.rectangle([28, 920, 996, 984], fill=INK)
    d.text((44, 928), "ALSO TODAY", font=font(SANS_B, 17), fill=(255, 190, 90))
    d.text((188, 928), tick1, font=font(SANS, 17), fill=(255, 255, 255))
    d.text((44, 954), tick2, font=font(SANS, 17), fill=(255, 255, 255))

    draw_center(d, W // 2, 994, "All stories reported Saturday 21 November 2026  •  The World Today",
                font(SANS, 15), GREY)

    img.save(OUT, format="JPEG", quality=88, optimize=True)
    print(f"wrote {OUT} {os.path.getsize(OUT)} bytes")


if __name__ == "__main__":
    main()
