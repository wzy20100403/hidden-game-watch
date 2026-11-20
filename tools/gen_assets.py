#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate original flat-style art for the BlueOS watch game.
All icons are drawn from scratch with PIL (no third-party assets).
"""
import os
from PIL import Image, ImageDraw

OUT = os.path.join(os.path.dirname(__file__), '..', 'src', 'assets', 'images')
os.makedirs(OUT, exist_ok=True)

S = 3            # supersampling factor
U = 200          # design units
INK = (60, 46, 42)
W = 5

# palette
CREAM = (255, 246, 228)
WOOD = (203, 152, 100)
WOOD_D = (170, 120, 74)
GREEN = (110, 190, 120)
GREEN_D = (78, 156, 95)
BLUE = (120, 186, 228)
BLUE_D = (86, 150, 196)
RED = (232, 106, 96)
YELLOW = (248, 200, 90)
PINK = (244, 158, 168)
PURPLE = (168, 148, 214)
GRAY = (176, 182, 190)
GRAY_D = (140, 148, 158)
WHITE = (252, 252, 250)
BROWN = (150, 112, 82)
TEAL = (92, 176, 168)
MINT = (168, 216, 186)
LAV = (214, 206, 240)
PEACH = (250, 196, 160)


class Pad:
    def __init__(self):
        self.img = Image.new('RGBA', (U * S, U * S), (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.img)

    def _s(self, v):
        return v * S

    def box(self, x0, y0, x1, y1):
        return [self._s(x0), self._s(y0), self._s(x1), self._s(y1)]

    def rr(self, x0, y0, x1, y1, r=10, fill=WHITE, outline=INK, w=W):
        self.d.rounded_rectangle(self.box(x0, y0, x1, y1), radius=self._s(r),
                                 fill=fill, outline=outline, width=self._s(w))

    def ell(self, x0, y0, x1, y1, fill=WHITE, outline=INK, w=W):
        self.d.ellipse(self.box(x0, y0, x1, y1), fill=fill, outline=outline,
                       width=self._s(w))

    def poly(self, pts, fill=WHITE, outline=INK, w=W):
        p = [(self._s(x), self._s(y)) for x, y in pts]
        self.d.polygon(p, fill=fill, outline=outline, width=self._s(w))

    def line(self, pts, fill=INK, w=W):
        p = [(self._s(x), self._s(y)) for x, y in pts]
        self.d.line(p, fill=fill, width=self._s(w), joint='curve')

    def arc(self, x0, y0, x1, y1, a0, a1, fill=INK, w=W):
        self.d.arc(self.box(x0, y0, x1, y1), a0, a1, fill=fill, width=self._s(w))

    def save(self, name):
        img = self.img.resize((U * 2, U * 2), Image.LANCZOS)
        img.save(os.path.join(OUT, name))


# ---------- bedroom ----------
def bed():
    p = Pad()
    p.rr(24, 54, 46, 152, 6, WOOD_D)
    p.rr(40, 96, 180, 152, 8, WOOD)
    p.rr(48, 86, 104, 116, 8, WHITE)
    p.rr(96, 96, 178, 150, 8, TEAL)
    p.line([(96, 118), (120, 118)])
    p.rr(44, 148, 60, 172, 4, WOOD_D)
    p.rr(164, 148, 180, 172, 4, WOOD_D)
    p.save('bed.png')


def wardrobe():
    p = Pad()
    p.rr(46, 18, 154, 182, 8, WOOD)
    p.line([(100, 26), (100, 174)])
    p.ell(88, 98, 96, 106, WOOD_D, INK, 3)
    p.ell(104, 98, 112, 106, WOOD_D, INK, 3)
    p.rr(38, 14, 162, 26, 4, WOOD_D)
    p.line([(58, 40), (92, 40)])
    p.line([(108, 40), (142, 40)])
    p.save('wardrobe.png')


def desk():
    p = Pad()
    p.rr(18, 66, 182, 84, 5, WOOD)
    p.rr(28, 84, 38, 174, 3, WOOD_D)
    p.rr(162, 84, 172, 174, 3, WOOD_D)
    p.rr(58, 88, 128, 130, 6, (226, 186, 138))
    p.ell(88, 104, 98, 114, WOOD_D, INK, 3)
    p.rr(136, 44, 172, 66, 3, MINT)
    p.line([(140, 52), (168, 52)])
    p.save('desk.png')


def rug():
    p = Pad()
    p.ell(14, 56, 186, 144, RED)
    p.ell(34, 70, 166, 130, (244, 170, 120), INK, 3)
    p.ell(66, 88, 134, 112, CREAM, INK, 3)
    p.line([(18, 128), (30, 136)])
    p.line([(182, 128), (170, 136)])
    p.save('rug.png')


def plant():
    p = Pad()
    p.poly([(62, 108), (138, 108), (128, 178), (72, 178)], (196, 120, 92))
    p.rr(66, 100, 134, 114, 4, (168, 96, 72))
    p.ell(70, 20, 112, 70, GREEN)
    p.ell(90, 18, 130, 66, GREEN_D)
    p.ell(56, 40, 98, 88, GREEN)
    p.ell(104, 36, 144, 86, GREEN_D)
    p.line([(100, 96), (100, 60)])
    p.save('plant.png')


def tv_stand():
    p = Pad()
    p.rr(30, 100, 170, 164, 6, WOOD)
    p.line([(100, 106), (100, 158)])
    p.ell(88, 126, 96, 134, WOOD_D, INK, 3)
    p.ell(104, 126, 112, 134, WOOD_D, INK, 3)
    p.rr(54, 26, 146, 100, 5, (86, 92, 110))
    p.rr(62, 34, 138, 86, 4, (120, 210, 210), INK, 3)
    p.line([(66, 40), (86, 62)])
    p.save('tvstand.png')


# ---------- kitchen ----------
def fridge():
    p = Pad()
    p.rr(56, 18, 144, 184, 10, (206, 228, 238))
    p.line([(56, 76), (144, 76)])
    p.rr(134, 86, 140, 128, 3, GRAY)
    p.rr(134, 36, 140, 66, 3, GRAY)
    p.rr(66, 30, 90, 42, 3, YELLOW, INK, 3)
    p.save('fridge.png')


def pot():
    p = Pad()
    p.rr(48, 96, 152, 166, 8, GRAY)
    p.ell(42, 78, 158, 106, (200, 206, 212))
    p.ell(92, 72, 108, 88, GRAY_D, INK, 3)
    p.line([(30, 116), (48, 112)])
    p.line([(170, 116), (152, 112)])
    p.arc(78, 34, 102, 62, 180, 300, (220, 220, 224), 4)
    p.arc(102, 30, 126, 58, 180, 300, (220, 220, 224), 4)
    p.save('pot.png')


def cabinet():
    p = Pad()
    p.rr(30, 38, 170, 172, 6, WOOD)
    p.line([(100, 46), (100, 164)])
    p.ell(88, 96, 96, 104, WOOD_D, INK, 3)
    p.ell(104, 96, 112, 104, WOOD_D, INK, 3)
    p.rr(22, 34, 178, 46, 3, WOOD_D)
    p.save('cabinet.png')


def basket():
    p = Pad()
    p.poly([(40, 100), (160, 100), (146, 174), (54, 174)], (222, 180, 120))
    for y in (120, 140, 160):
        p.line([(52, y), (148, y)])
    p.line([(70, 100), (80, 174)])
    p.line([(100, 100), (100, 174)])
    p.line([(130, 100), (120, 174)])
    p.ell(56, 76, 92, 112, RED)
    p.ell(92, 68, 128, 104, YELLOW)
    p.ell(120, 78, 152, 110, GREEN)
    p.save('basket.png')


def microwave():
    p = Pad()
    p.rr(28, 58, 172, 152, 8, (226, 226, 222))
    p.rr(38, 68, 130, 142, 5, (120, 130, 150))
    p.rr(44, 74, 124, 136, 4, (180, 220, 226), INK, 3)
    p.rr(138, 68, 164, 84, 3, GRAY_D, INK, 3)
    p.rr(138, 92, 164, 108, 3, GRAY_D, INK, 3)
    p.ell(146, 120, 158, 132, YELLOW, INK, 3)
    p.save('microwave.png')


def trash():
    p = Pad()
    p.poly([(52, 74), (148, 74), (138, 176), (62, 176)], GRAY)
    p.line([(76, 94), (78, 160)])
    p.line([(112, 94), (110, 160)])
    p.rr(44, 54, 156, 78, 6, GRAY_D)
    p.rr(92, 44, 108, 56, 3, GRAY_D, INK, 3)
    p.save('trash.png')


# ---------- bathroom ----------
def bathtub():
    p = Pad()
    p.rr(20, 66, 180, 148, 30, WHITE)
    p.rr(34, 78, 166, 136, 24, (150, 214, 226), INK, 3)
    p.ell(52, 84, 92, 108, WHITE, INK, 2)
    p.ell(96, 80, 128, 100, WHITE, INK, 2)
    p.ell(120, 90, 144, 108, WHITE, INK, 2)
    p.rr(34, 148, 50, 172, 4, GRAY_D)
    p.rr(150, 148, 166, 172, 4, GRAY_D)
    p.line([(176, 74), (176, 60)])
    p.arc(164, 52, 188, 76, 90, 270, GRAY_D, 4)
    p.save('bathtub.png')


def toilet():
    p = Pad()
    p.rr(58, 24, 142, 78, 8, WHITE)
    p.rr(48, 74, 152, 132, 20, WHITE)
    p.rr(58, 84, 142, 124, 16, (208, 228, 236), INK, 3)
    p.rr(72, 130, 128, 168, 6, WHITE)
    p.ell(84, 34, 96, 46, GRAY, INK, 3)
    p.save('toilet.png')


def washer():
    p = Pad()
    p.rr(36, 22, 164, 178, 10, WHITE)
    p.rr(44, 34, 156, 52, 4, (226, 230, 234), INK, 3)
    p.rr(132, 35, 150, 51, 3, GRAY_D, INK, 2)
    p.ell(58, 66, 142, 150, (170, 200, 220))
    p.ell(66, 74, 134, 142, (208, 230, 240), INK, 3)
    p.line([(74, 84), (96, 106)])
    p.save('washer.png')


def mirror():
    p = Pad()
    p.ell(52, 18, 148, 182, (238, 200, 120))
    p.ell(62, 28, 138, 172, (198, 226, 238), INK, 4)
    p.line([(78, 56), (78, 96)])
    p.line([(90, 48), (90, 76)])
    p.line([(120, 120), (132, 136)])
    p.save('mirror.png')


def sink():
    p = Pad()
    p.rr(38, 84, 162, 136, 16, WHITE)
    p.rr(48, 92, 152, 126, 12, (198, 224, 234), INK, 3)
    p.rr(94, 50, 106, 86, 4, GRAY_D)
    p.line([(100, 50), (128, 50), (128, 62)])
    p.rr(96, 136, 104, 176, 3, GRAY_D)
    p.rr(120, 136, 128, 172, 3, GRAY_D)
    p.save('sink.png')


def towel():
    p = Pad()
    p.line([(24, 44), (176, 44)], GRAY_D, 7)
    p.ell(18, 38, 32, 52, GRAY_D, INK, 3)
    p.ell(168, 38, 182, 52, GRAY_D, INK, 3)
    p.rr(58, 44, 142, 148, 6, PINK)
    p.line([(58, 122), (142, 122)])
    p.line([(78, 52), (78, 140)])
    p.line([(122, 52), (122, 140)])
    p.save('towel.png')


# ---------- balcony ----------
def flowerpot():
    p = Pad()
    p.poly([(60, 112), (140, 112), (128, 180), (72, 180)], (206, 122, 96))
    p.rr(64, 104, 136, 118, 4, (180, 100, 78))
    p.line([(100, 108), (100, 60)])
    p.line([(84, 108), (78, 74)])
    p.line([(116, 108), (122, 78)])
    p.ell(86, 48, 114, 76, YELLOW, INK, 4)
    p.ell(66, 62, 90, 86, PINK, INK, 4)
    p.ell(112, 64, 136, 88, PINK, INK, 4)
    p.ell(94, 56, 106, 68, (240, 150, 60), INK, 3)
    p.save('flowerpot.png')


def toolbox():
    p = Pad()
    p.rr(28, 78, 172, 164, 6, (236, 130, 86))
    p.rr(28, 78, 172, 100, 6, (210, 106, 66))
    p.line([(60, 84), (60, 158)])
    p.line([(140, 84), (140, 158)])
    p.arc(78, 46, 122, 90, 180, 360, GRAY_D, 6)
    p.rr(90, 112, 110, 130, 3, YELLOW, INK, 3)
    p.save('toolbox.png')


def shoerack():
    p = Pad()
    p.rr(30, 34, 170, 174, 6, (222, 186, 140))
    p.line([(30, 104), (170, 104)])
    p.rr(44, 66, 92, 96, 8, BLUE_D, INK, 4)
    p.rr(104, 62, 152, 92, 8, RED, INK, 4)
    p.rr(46, 126, 94, 156, 8, GREEN_D, INK, 4)
    p.rr(104, 130, 152, 160, 8, YELLOW, INK, 4)
    p.save('shoerack.png')


def bike():
    p = Pad()
    p.ell(18, 104, 88, 174, None, INK, 6)
    p.ell(112, 104, 182, 174, None, INK, 6)
    p.line([(53, 139), (90, 88), (132, 139), (100, 139), (100, 88)])
    p.line([(90, 88), (78, 70)])
    p.line([(70, 70), (92, 70)])
    p.line([(132, 139), (148, 74)])
    p.line([(138, 70), (158, 78)])
    p.ell(128, 62, 152, 86, None, INK, 5)
    p.ell(64, 126, 84, 152, GRAY, INK, 3)
    p.save('bike.png')


def wateringcan():
    p = Pad()
    p.rr(36, 84, 138, 170, 8, MINT)
    p.poly([(132, 92), (178, 68), (184, 84), (140, 112)], MINT)
    p.arc(54, 46, 118, 110, 180, 360, GREEN_D, 6)
    p.ell(42, 62, 54, 74, (150, 214, 226), INK, 3)
    p.ell(30, 80, 42, 92, (150, 214, 226), INK, 3)
    p.save('wateringcan.png')


def carton():
    p = Pad()
    p.rr(34, 54, 166, 170, 4, (216, 180, 132))
    p.poly([(34, 54), (100, 34), (166, 54), (100, 74)], (232, 200, 152))
    p.line([(100, 34), (100, 170)])
    p.rr(88, 34, 112, 170, 2, (236, 214, 176))
    p.line([(46, 86), (86, 86)])
    p.save('carton.png')


# ---------- mom's room ----------
def vanity():
    p = Pad()
    p.ell(58, 12, 142, 96, (238, 200, 120))
    p.ell(66, 20, 134, 88, (198, 226, 238), INK, 4)
    p.rr(30, 96, 170, 150, 6, (240, 228, 214))
    p.rr(44, 104, 156, 142, 4, (226, 206, 188))
    p.rr(48, 138, 62, 176, 3, WOOD_D)
    p.rr(138, 138, 152, 176, 3, WOOD_D)
    p.rr(52, 78, 64, 96, 3, PINK, INK, 3)
    p.rr(72, 82, 82, 96, 3, BLUE, INK, 3)
    p.save('vanity.png')


def pillow():
    p = Pad()
    p.rr(26, 56, 174, 144, 26, (250, 238, 244))
    p.line([(60, 76), (80, 96)])
    p.line([(140, 76), (120, 96)])
    p.line([(26, 120), (174, 120)], (238, 220, 232), 4)
    p.rr(158, 128, 170, 140, 3, PINK, INK, 3)
    p.save('pillow.png')


def handbag():
    p = Pad()
    p.arc(58, 34, 142, 118, 180, 360, (150, 96, 80), 8)
    p.rr(38, 84, 162, 176, 14, PINK)
    p.rr(38, 84, 162, 108, 14, (226, 130, 142))
    p.rr(92, 116, 108, 130, 4, (238, 200, 120), INK, 3)
    p.save('handbag.png')


def jewelry():
    p = Pad()
    p.rr(32, 74, 168, 164, 8, (196, 162, 214))
    p.rr(32, 64, 168, 92, 8, (170, 136, 192))
    p.poly([(100, 34), (128, 52), (100, 70), (72, 52)], (140, 220, 240))
    p.save('jewelry.png')


def suitcase():
    p = Pad()
    p.arc(78, 30, 122, 70, 180, 360, GRAY_D, 6)
    p.rr(26, 54, 174, 166, 10, (120, 156, 196))
    p.line([(26, 92), (174, 92)])
    p.rr(56, 130, 144, 138, 3, (90, 120, 160), INK, 2)
    p.ell(56, 166, 68, 178, INK, INK, 2)
    p.ell(132, 166, 144, 178, INK, INK, 2)
    p.save('suitcase.png')


def curtain():
    p = Pad()
    p.rr(16, 26, 184, 38, 4, WOOD)
    p.poly([(34, 34), (90, 34), (82, 170), (42, 170)], (244, 200, 170))
    p.poly([(110, 34), (166, 34), (158, 170), (118, 170)], (244, 200, 170))
    p.line([(52, 44), (48, 120)])
    p.line([(72, 44), (68, 120)])
    p.line([(128, 44), (124, 120)])
    p.line([(148, 44), (144, 120)])
    p.line([(82, 92), (118, 92)], (232, 168, 130), 6)
    p.save('curtain.png')


# ---------- characters and props ----------
def console():
    p = Pad()
    p.rr(36, 44, 164, 168, 18, (232, 106, 96))
    p.rr(36, 44, 164, 86, 18, (216, 84, 80))
    p.rr(48, 58, 152, 118, 8, (34, 44, 60))
    p.rr(56, 66, 144, 110, 5, (120, 200, 170), INK, 3)
    p.rr(88, 60, 112, 66, 2, (60, 74, 96), INK, 2)
    p.line([(62, 132), (86, 132)], INK, 10)
    p.line([(74, 120), (74, 144)], INK, 10)
    p.ell(118, 124, 136, 142, YELLOW)
    p.ell(142, 132, 158, 148, (120, 170, 230))
    p.save('console.png')


def mom():
    p = Pad()
    # hair behind
    p.ell(48, 22, 152, 126, (92, 66, 58))
    p.ell(70, 4, 130, 44, (92, 66, 58))
    # face
    p.ell(60, 30, 140, 108, (246, 204, 176))
    p.ell(82, 58, 92, 70, INK, INK, 3)
    p.ell(108, 58, 118, 70, INK, INK, 3)
    p.arc(88, 74, 112, 94, 20, 160, INK, 4)
    p.ell(66, 80, 78, 92, (244, 170, 156), None, 0)
    p.ell(122, 80, 134, 92, (244, 170, 156), None, 0)
    # body
    p.poly([(58, 104), (142, 104), (154, 180), (46, 180)], (236, 152, 140))
    p.poly([(78, 108), (122, 108), (130, 176), (70, 176)], CREAM)
    p.line([(100, 112), (100, 176)], (222, 206, 190), 3)
    p.save('mom.png')


def logo():
    img = Image.new('RGBA', (U * S, U * S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([10 * S, 10 * S, 190 * S, 190 * S], radius=44 * S,
                        fill=(255, 240, 214), outline=INK, width=6 * S)
    # console
    d.rounded_rectangle([44 * S, 54 * S, 156 * S, 166 * S], radius=18 * S,
                        fill=(232, 106, 96), outline=INK, width=5 * S)
    d.rounded_rectangle([58 * S, 70 * S, 142 * S, 118 * S], radius=8 * S,
                        fill=(120, 200, 170), outline=INK, width=4 * S)
    d.line([(66 * S, 140 * S), (94 * S, 140 * S)], fill=INK, width=9 * S)
    d.line([(80 * S, 126 * S), (80 * S, 154 * S)], fill=INK, width=9 * S)
    d.ellipse([116 * S, 130 * S, 132 * S, 146 * S], fill=YELLOW, outline=INK, width=3 * S)
    d.ellipse([138 * S, 140 * S, 152 * S, 154 * S], fill=(120, 170, 230), outline=INK, width=3 * S)
    img.resize((480, 480), Image.LANCZOS).save(os.path.join(OUT, 'logo.png'))


def make_all():
    for fn in [bed, wardrobe, desk, rug, plant, tv_stand,
               fridge, pot, cabinet, basket, microwave, trash,
               bathtub, toilet, washer, mirror, sink, towel,
               flowerpot, toolbox, shoerack, bike, wateringcan, carton,
               vanity, pillow, handbag, jewelry, suitcase, curtain,
               console, mom]:
        fn()
    logo()
    names = sorted(os.listdir(OUT))
    print('generated', len(names), 'files:', ', '.join(names))


if __name__ == '__main__':
    make_all()
