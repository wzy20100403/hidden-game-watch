#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extra original icons for the puzzle redesign (chair, outlet, radio,
flashlight, key, ice tray, note). Same hand-drawn flat style as gen_assets."""
import os
from PIL import Image, ImageDraw

OUT = os.path.join(os.path.dirname(__file__), '..', 'src', 'assets', 'images')
os.makedirs(OUT, exist_ok=True)
S, U = 3, 200
INK = (60, 46, 42)
W = 5
CREAM = (255, 246, 228)
WOOD = (203, 152, 100)
WOOD_D = (170, 120, 74)
GRAY = (176, 182, 190)
GRAY_D = (140, 148, 158)
WHITE = (252, 252, 250)
YELLOW = (248, 200, 90)
RED = (232, 106, 96)
BLUE = (120, 186, 228)
TEAL = (92, 176, 168)
PAPER = (250, 242, 218)


class P:
    def __init__(self):
        self.img = Image.new('RGBA', (U * S, U * S), (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.img)

    def b(self, x0, y0, x1, y1):
        return [x0 * S, y0 * S, x1 * S, y1 * S]

    def rr(self, x0, y0, x1, y1, r=10, fill=WHITE, outline=INK, w=W):
        self.d.rounded_rectangle(self.b(x0, y0, x1, y1), radius=r * S, fill=fill,
                                 outline=outline, width=w * S)

    def ell(self, x0, y0, x1, y1, fill=WHITE, outline=INK, w=W):
        self.d.ellipse(self.b(x0, y0, x1, y1), fill=fill, outline=outline, width=w * S)

    def line(self, pts, fill=INK, w=W):
        self.d.line([(x * S, y * S) for x, y in pts], fill=fill, width=w * S, joint='curve')

    def poly(self, pts, fill=WHITE, outline=INK, w=W):
        self.d.polygon([(x * S, y * S) for x, y in pts], fill=fill, outline=outline, width=w * S)

    def save(self, name):
        self.img.resize((U * 2, U * 2), Image.LANCZOS).save(os.path.join(OUT, name))


def chair():
    p = P()
    p.rr(52, 34, 78, 104, 8, WOOD)
    p.rr(52, 40, 148, 60, 8, WOOD)
    p.rr(50, 96, 150, 118, 8, WOOD_D)
    p.line([(62, 118), (56, 168)], w=7)
    p.line([(138, 118), (144, 168)], w=7)
    p.line([(70, 140), (146, 140)], w=5)
    p.save('chair.png')


def outlet():
    p = P()
    p.rr(58, 48, 142, 152, 12)
    p.ell(84, 82, 100, 98, fill=GRAY_D)
    p.ell(100, 82, 116, 98, fill=GRAY_D)
    p.rr(88, 120, 112, 132, 4, GRAY)
    p.line([(100, 152), (100, 176)], w=6)
    p.save('outlet.png')


def radio():
    p = P()
    p.rr(40, 78, 152, 158, 8, RED)
    for i in range(3):
        p.line([(52, 92 + i * 14), (96, 92 + i * 14)], fill=INK, w=4)
    p.ell(112, 92, 138, 118, fill=CREAM)
    p.ell(118, 140, 132, 154, fill=WHITE)
    p.line([(120, 78), (150, 34)], w=5)
    p.line([(88, 158), (80, 176)], w=6)
    p.line([(112, 158), (120, 176)], w=6)
    p.save('radio.png')


def flashlight():
    p = P()
    p.poly([(54, 84), (54, 116), (112, 132), (112, 68)], fill=GRAY)
    p.rr(112, 66, 132, 134, 6, GRAY_D)
    p.rr(132, 72, 146, 128, 4, YELLOW)
    p.line([(146, 78), (176, 58)], fill=YELLOW, w=6)
    p.line([(146, 100), (180, 100)], fill=YELLOW, w=6)
    p.line([(146, 122), (176, 142)], fill=YELLOW, w=6)
    p.save('flashlight.png')


def key():
    p = P()
    p.ell(36, 76, 92, 132, fill=YELLOW)
    p.ell(52, 92, 76, 116, fill=CREAM)
    p.rr(86, 98, 168, 110, 4, YELLOW)
    p.rr(150, 104, 158, 124, 3, YELLOW)
    p.rr(132, 104, 140, 120, 3, YELLOW)
    p.save('key.png')


def ice():
    p = P()
    p.rr(34, 74, 166, 150, 8, BLUE)
    for x in (44, 84, 124):
        p.rr(x, 84, x + 32, 116, 4, WHITE)
        p.rr(x, 120, x + 32, 142, 4, WHITE)
    p.save('ice.png')


def note():
    p = P()
    p.rr(48, 38, 152, 164, 3, PAPER)
    p.line([(64, 66), (136, 66)], w=4)
    p.line([(64, 90), (136, 90)], w=4)
    p.line([(64, 114), (122, 114)], w=4)
    p.line([(64, 138), (110, 138)], w=4)
    p.save('note.png')


def console_small():
    p = P()
    p.rr(34, 62, 166, 146, 12, RED)
    p.rr(48, 74, 108, 116, 6, TEAL)
    p.ell(124, 80, 136, 92, fill=WHITE)
    p.ell(140, 80, 152, 92, fill=WHITE)
    p.line([(60, 128), (70, 138)], w=5)
    p.line([(70, 128), (60, 138)], w=5)
    p.ell(132, 124, 150, 142, fill=YELLOW)
    p.save('console_small.png')


for fn in (chair, outlet, radio, flashlight, key, ice, note, console_small):
    fn()
print('extra assets done')
