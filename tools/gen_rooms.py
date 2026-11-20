#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compose 5 square-room backgrounds (390x296) from the original icons.
The page overlays invisible tap hotspots at the same coordinates."""
import os
from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, 'src', 'assets', 'images')
W, H = 390, 296
S = 4

FLOOR = 240
ROOMS = {
    1: dict(wall=(252, 239, 215), floor=(228, 202, 166), base=(208, 178, 138),
            objects=[('bed', 4, 150, 120), ('wardrobe', 262, 128, 110), ('desk', 138, 158, 100),
                     ('chair', 244, 196, 62), ('rug', 20, 244, 80)]),
    2: dict(wall=(246, 236, 218), floor=(214, 196, 172), base=(196, 176, 150),
            objects=[('fridge', 6, 110, 96), ('cabinet', 270, 104, 104), ('microwave', 282, 42, 64),
                     ('pot', 150, 112, 96), ('basket', 250, 224, 64), ('trash', 30, 226, 56)]),
    3: dict(wall=(228, 240, 240), floor=(204, 220, 220), base=(186, 202, 202),
            objects=[('washer', 8, 150, 108), ('sink', 128, 196, 68), ('bathtub', 202, 180, 116),
                     ('mirror', 36, 30, 64), ('towel', 146, 26, 64), ('outlet', 330, 144, 44)]),
    4: dict(wall=(206, 226, 238), floor=(208, 200, 186), base=(190, 182, 168),
            objects=[('shoerack', 4, 160, 80), ('carton', 306, 212, 66), ('flowerpot', 222, 206, 64),
                     ('wateringcan', 146, 214, 64), ('toolbox', 36, 200, 92)]),
    5: dict(wall=(244, 230, 226), floor=(216, 190, 176), base=(198, 172, 158),
            objects=[('suitcase', 4, 190, 84), ('mom', 140, 120, 100), ('radio', 296, 120, 62),
                     ('vanity', 250, 180, 100), ('handbag', 36, 212, 78), ('pillow', 140, 226, 72)]),
}


def sc(v):
    return int(v * S)


def icon(name, size):
    im = Image.open(os.path.join(A, name + '.png')).convert('RGBA')
    return im.resize((sc(size), sc(size)), Image.LANCZOS)


def bg(wall, floor, base):
    im = Image.new('RGBA', (W * S, H * S), wall)
    d = ImageDraw.Draw(im)
    d.rectangle((0, sc(FLOOR), W * S, H * S), fill=floor)
    d.line((0, sc(FLOOR), W * S, sc(FLOOR)), fill=base, width=sc(2))
    for x in range(0, W, 44):
        d.line((sc(x), sc(FLOOR), sc(x) - sc(14), H * S), fill=base, width=sc(1))
    for y in range(FLOOR + 18, H, 22):
        d.line((0, sc(y), W * S, sc(y)), fill=base, width=sc(1))
    for x in range(18, W, 36):
        d.line((sc(x), 0, sc(x), sc(FLOOR)), fill=tuple(max(0, c - 5) for c in wall), width=sc(2))
    d.line((0, sc(FLOOR - 3), W * S, sc(FLOOR - 3)), fill=base, width=sc(3))
    return im, d


def window(d, x, y, w, h):
    d.rectangle((sc(x - 5), sc(y - 5), sc(x + w + 5), sc(y + h + 5)), fill=(246, 239, 226))
    d.rectangle((sc(x), sc(y), sc(x + w), sc(y + h)), fill=(176, 214, 232))
    d.rectangle((sc(x), sc(y), sc(x + w), sc(y + h)), outline=(150, 140, 124), width=sc(3))
    d.line((sc(x + w / 2), sc(y), sc(x + w / 2), sc(y + h)), fill=(150, 140, 124), width=sc(3))
    d.line((sc(x), sc(y + h / 2), sc(x + w), sc(y + h / 2)), fill=(150, 140, 124), width=sc(3))
    d.rectangle((sc(x - 16), sc(y - 12), sc(x - 5), sc(y + h + 8)), fill=(238, 176, 160))
    d.rectangle((sc(x + w + 5), sc(y - 12), sc(x + w + 16), sc(y + h + 8)), fill=(238, 176, 160))


def picture(d, x, y, w, h):
    d.rectangle((sc(x), sc(y), sc(x + w), sc(y + h)), fill=(250, 246, 234), outline=(150, 140, 124), width=sc(3))
    d.rectangle((sc(x + 6), sc(y + 6), sc(x + w - 6), sc(y + h - 6)), fill=(206, 224, 208))


def shadow(im, x, y, s):
    if y + s < 245:
        return
    lay = Image.new('RGBA', im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    d.ellipse((sc(x + 14), sc(y + s - 10), sc(x + s - 10), sc(y + s + 2)), fill=(60, 46, 42, 50))
    im.alpha_composite(lay)


def make(n):
    cfg = ROOMS[n]
    im, d = bg(cfg['wall'], cfg['floor'], cfg['base'])

    if n == 1:
        window(d, 52, 28, 100, 78)
        picture(d, 200, 24, 60, 46)
    elif n == 2:
        # stove: cabinet + counter top + burner + knobs
        d.rectangle((sc(130), sc(198), sc(260), sc(242)), fill=(196, 158, 120))
        d.rectangle((sc(126), sc(190), sc(264), sc(202)), fill=(232, 224, 210))
        d.ellipse((sc(172), sc(188), sc(220), sc(206)), fill=(120, 112, 104))
        d.ellipse((sc(178), sc(191), sc(214), sc(203)), fill=(86, 84, 82))
        for kx in (140, 236):
            d.ellipse((sc(kx), sc(214), sc(kx + 14), sc(228)), fill=(120, 100, 80))
        for y in (16, 52, 88, 124, 160):
            d.line((0, sc(y), W * S, sc(y)), fill=(232, 222, 204), width=sc(2))
    elif n == 3:
        for x in range(0, W, 48):
            d.line((sc(x), 0, sc(x), sc(FLOOR)), fill=(212, 228, 228), width=sc(2))
        for y in range(0, FLOOR, 44):
            d.line((0, sc(y), W * S, sc(y)), fill=(212, 228, 228), width=sc(2))
        d.rectangle((sc(144), sc(274), sc(236), sc(292)), fill=(240, 234, 220))
    elif n == 4:
        d.rectangle((0, 0, W * S, sc(150)), fill=(198, 224, 238))
        for y in (26, 62, 98, 134):
            d.line((0, sc(y), W * S, sc(y)), fill=(236, 240, 244), width=sc(4))
        d.line((0, sc(150), W * S, sc(150)), fill=(160, 168, 176), width=sc(6))
        for x in range(20, W, 56):
            d.line((sc(x), sc(150), sc(x), sc(FLOOR)), fill=(170, 178, 186), width=sc(3))
        d.rectangle((0, sc(150), W * S, sc(FLOOR)), fill=(206, 216, 222))
    elif n == 5:
        for x in range(0, W, 30):
            d.rectangle((sc(x), 0, sc(x + 12), sc(FLOOR)), fill=(238, 222, 218))
        d.rounded_rectangle((sc(126), sc(196), sc(262), sc(268)), radius=sc(12), fill=(196, 170, 190))
        d.rounded_rectangle((sc(126), sc(208), sc(262), sc(242)), radius=sc(10), fill=(214, 188, 206))
        d.rectangle((sc(292), sc(182), sc(366), sc(FLOOR)), fill=(180, 142, 116))
        d.rectangle((sc(288), sc(178), sc(370), sc(186)), fill=(206, 168, 140))

    for name, x, y, s in cfg['objects']:
        shadow(im, x, y, s)
        im.alpha_composite(icon(name, s), (sc(x), sc(y)))

    im.resize((W, H), Image.LANCZOS).convert('RGB').save(os.path.join(A, 'room%d.png' % n))


for i in range(1, 6):
    make(i)
print('rooms done')
