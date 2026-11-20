#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""390x450 方屏设计预览（设计稿，不是真机截图）。"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, 'src', 'assets', 'images')
OUT = os.path.join(ROOT, 'preview-square')
os.makedirs(OUT, exist_ok=True)
W, H = 390, 450
BG = (251, 244, 228)
INK = (74, 52, 40)
MUTED = (167, 141, 114)
ACCENT = (232, 115, 95)
FONT = '/system/fonts/NotoSansCJK-Regular.ttc'
f_title = ImageFont.truetype(FONT, 30)
f_h1 = ImageFont.truetype(FONT, 22)
f_lv = ImageFont.truetype(FONT, 13)
f_body = ImageFont.truetype(FONT, 13)
f_btn = ImageFont.truetype(FONT, 17)
f_small = ImageFont.truetype(FONT, 11)


def center(d, y, text, font, fill, width=W):
    w = d.textlength(text, font=font)
    d.text(((width - w) / 2, y), text, font=font, fill=fill)


def center_box(d, x0, x1, y, text, font, fill):
    w = d.textlength(text, font=font)
    d.text(((x0 + x1 - w) / 2, y), text, font=font, fill=fill)


def icon(name, size):
    return Image.open(os.path.join(A, name + '.png')).convert('RGBA').resize((size, size), Image.LANCZOS)


def wrap(d, text, font, maxw):
    lines, cur = [], ''
    for ch in text:
        if d.textlength(cur + ch, font=font) > maxw:
            lines.append(cur); cur = ch
        else:
            cur += ch
    lines.append(cur)
    return lines


def title_screen():
    im = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(im)
    logo = icon('logo', 62)
    im.paste(logo, ((W - 62) // 2, 2), logo)
    center(d, 70, '妈妈把我的游戏机藏起来了', f_h1, INK)
    center(d, 100, '房间解谜 · 原创致敬', f_small, MUTED)
    mom = icon('mom', 52)
    con = icon('console', 40)
    im.paste(mom, (96, 118), mom)
    im.paste(con, (250, 124), con)
    center_box(d, 180, 210, 126, '?', ImageFont.truetype(FONT, 24), ACCENT)
    center(d, 186, '左右箭头换房间，点物件找线索。', f_body, (107, 81, 56))
    center(d, 204, '找道具、用道具，别让妈妈起疑心。', f_body, (107, 81, 56))
    # start / random / hell / settings
    d.rounded_rectangle((120, 224, 270, 264), 20, fill=ACCENT)
    center(d, 232, '开始游戏', f_btn, (255, 255, 255))
    d.rounded_rectangle((120, 270, 270, 310), 20, fill=(255, 247, 232), outline=(232, 115, 95))
    center(d, 278, '随机模式', f_btn, (201, 85, 61))
    d.rounded_rectangle((120, 316, 270, 356), 20, fill=(179, 58, 43))
    center(d, 324, '地狱模式', f_btn, (255, 255, 255))
    d.rounded_rectangle((135, 362, 255, 390), 14, fill=(255, 247, 232), outline=(232, 115, 95))
    center(d, 367, '设置', f_small, (201, 85, 61))
    center(d, 404, '原创美术 · 不含商业游戏素材', f_small, MUTED)
    im.save(os.path.join(OUT, 'title.png'))

def play_screen(n, label, msg, bag=(), susp=0):
    im = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(im)
    d.text((22, 20), label, font=f_lv, fill=(91, 67, 49))
    right = '疑心 ' + '●' * susp + '○' * (3 - susp)
    d.text((W - 22 - d.textlength(right, font=f_lv), 20), right, font=f_lv, fill=(176, 85, 63))
    room = Image.open(os.path.join(A, 'room%d.png' % n)).convert('RGB').resize((390, 270), Image.LANCZOS)
    im.paste(room, (0, 44))
    for cx, ch in ((6, '‹'), (338, '›')):
        d.ellipse((cx, 141, cx + 46, 187), fill=(60, 46, 42))
        d.text((cx + 12, 143), ch, font=ImageFont.truetype(FONT, 30), fill=(255, 247, 232))
    d.rounded_rectangle((12, 316, 378, 366), 10, fill=(255, 255, 255), outline=(235, 217, 192))
    lines = wrap(d, msg, f_body, 340)[:2]
    for i, ln in enumerate(lines):
        center(d, 323 + i * 17, ln, f_body, (91, 67, 49))
    if not bag:
        d.text((12, 377), '手上没有东西', font=f_small, fill=MUTED)
    x = 20
    for name, cname in bag:
        w = 30 + int(d.textlength(cname, font=f_small)) + 18
        d.rounded_rectangle((x, 371, x + w, 403), 8, fill=(255, 233, 226), outline=ACCENT)
        im.paste(icon(name, 18), (x + 5, 376), icon(name, 18))
        d.text((x + 30, 378), cname, font=f_small, fill=(107, 81, 56))
        x += w + 8
    d.rounded_rectangle((318, 373, 378, 403), 15, fill=(244, 193, 93))
    center_box(d, 318, 378, 379, '提示', f_body, (91, 67, 49))
    im.save(os.path.join(OUT, 'play%d.png' % n))


def result_screen(kind, text, btn):
    im = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(im)
    ico = {'found': 'console', 'caught': 'mom', 'win': 'console'}[kind]
    im.paste(icon(ico, 126), ((W - 126) // 2, 66), icon(ico, 126))
    head = {'found': '找到啦！', 'caught': '被妈妈发现了！', 'win': '全部找到！'}[kind]
    color = {'found': (217, 87, 63), 'caught': (176, 69, 47), 'win': INK}[kind]
    center(d, 216, head, f_h1, color)
    lines = wrap(d, text, f_body, 300)[:3]
    for i, ln in enumerate(lines):
        center(d, 258 + i * 22, ln, f_body, (91, 67, 49))
    d.rounded_rectangle((105, 330, 285, 382), 26, fill=ACCENT)
    center(d, 344, btn, f_btn, (255, 255, 255))
    im.save(os.path.join(OUT, kind + '.png'))


title_screen()
play_screen(1, '第 1 天 · 卧室', '掀开被子，枕头下有一把手电筒。', [('flashlight', '手电筒')], 1)
play_screen(2, '第 2 天 · 厨房', '冰块丢进锅里，汤不烫了。', [('ice', '冰块')], 1)
play_screen(3, '第 3 天 · 浴室', '滚筒转得飞快，得先让它停。', [], 1)
play_screen(4, '第 4 天 · 阳台', '浇水壶底下粘着一把小钥匙。', [('key', '小钥匙')], 1)
play_screen(5, '第 5 天 · 妈妈房间', '妈妈在打盹，得先让她分心。', [('key', '小钥匙')], 2)
result_screen('found', '踩上椅子，从衣柜顶摸到了游戏机！', '下一天')
result_screen('caught', '妈妈推门进来：你在房间里翻什么呢？', '再来一次')
result_screen('win', '妈妈叹了口气：「只准玩十分钟哦。」', '再玩一次')

names = ['title', 'play1', 'play2', 'play3', 'play4', 'play5', 'found', 'caught', 'win']
ims = [Image.open(os.path.join(OUT, n + '.png')) for n in names]
cols, rows = 3, 3
sheet = Image.new('RGB', (W * cols + 20 * (cols + 1), H * rows + 20 * (rows + 1)), (40, 40, 40))
for i, im in enumerate(ims):
    sheet.paste(im, (20 + (i % cols) * (W + 20), 20 + (i // cols) * (H + 20)))
sheet.save(os.path.join(OUT, 'contact.png'))
print('saved', OUT, sheet.size)
