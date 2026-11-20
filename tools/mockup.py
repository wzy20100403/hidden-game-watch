"""生成 466x466 手表圆屏设计预览（仅设计稿，不是真机截图）。

用与 index.ux 相同的配色、字号比例和素材，拼出「标题 / 游戏 / 找到」三屏，
再用圆形裁切模拟 round watch 可视区域。
"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, 'src', 'assets', 'images')
OUT = os.path.join(ROOT, 'preview')
os.makedirs(OUT, exist_ok=True)

W = H = 466
BG = (253, 243, 227)
INK = (74, 52, 40)
MUTED = (169, 140, 112)
ACCENT = (224, 106, 90)
CREAM = (255, 248, 239)
CARD_BG = (255, 231, 194)
CARD_BD = (240, 223, 203)

FONT = '/system/fonts/NotoSansCJK-Regular.ttc'
f_title = ImageFont.truetype(FONT, 31)
f_big = ImageFont.truetype(FONT, 30)
f_name = ImageFont.truetype(FONT, 17)
f_body = ImageFont.truetype(FONT, 16)
f_small = ImageFont.truetype(FONT, 14)
f_tiny = ImageFont.truetype(FONT, 12)
f_btn = ImageFont.truetype(FONT, 22)


def center(d, y, text, font, fill):
    w = d.textlength(text, font=font)
    d.text(((W - w) / 2, y), text, font=font, fill=fill)


def icon(name, size):
    im = Image.open(os.path.join(A, name + '.png')).convert('RGBA')
    return im.resize((size, size), Image.LANCZOS)


def paste_center(canvas, im, cx, cy):
    canvas.alpha_composite(im, (int(cx - im.width / 2), int(cy - im.height / 2)))


def circle_clip(im):
    mask = Image.new('L', (W, H), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, W - 1, H - 1), fill=255)
    out = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    out.paste(im, (0, 0), mask)
    return out


def screen_title():
    im = Image.new('RGBA', (W, H), BG)
    d = ImageDraw.Draw(im)
    paste_center(im, icon('logo', 120), W / 2, 92)
    center(d, 158, '妈妈把我的游戏机', f_title, INK)
    center(d, 196, '藏起来了', f_title, INK)
    center(d, 250, '原创致敬版 · 在房间里把它找出来', f_small, MUTED)
    # button
    x0, y0, x1, y1 = (W - 150) / 2, 292, (W + 150) / 2, 344
    d.rounded_rectangle((x0, y0, x1, y1), 14, fill=ACCENT)
    tw = d.textlength('开始找', font=f_btn)
    d.text(((W - tw) / 2, 300), '开始找', font=f_btn, fill=CREAM)
    center(d, 374, '原创美术 · 不含任何商业游戏素材', f_tiny, (195, 176, 156))
    return circle_clip(im)


def screen_play():
    im = Image.new('RGBA', (W, H), BG)
    d = ImageDraw.Draw(im)
    center(d, 34, '第 1 关 · 卧室', f_small, MUTED)
    center(d, 56, '轻点物件仔细找', f_big, INK)

    # hint box
    d.rounded_rectangle((63, 96, 403, 136), 10, fill=(255, 247, 232), outline=(240, 217, 188))
    center(d, 106, '妈妈：被子都收进衣柜了。', f_small, (138, 90, 46))

    cards = [
        ('bed', '床'), ('wardrobe', '衣柜'), ('desk', '书桌'),
        ('rug', '地毯'), ('plant', '盆栽'), ('tvstand', '电视柜'),
    ]
    tones = [(255, 231, 194), (217, 237, 255), (233, 224, 255),
             (216, 242, 225), (255, 224, 228), (255, 246, 201)]
    cw = ch = 108
    gap = 6
    start_x = (W - (3 * cw + 2 * gap)) / 2
    y0 = 150
    for i, (ic, label) in enumerate(cards):
        r, c = divmod(i, 3)
        x = start_x + c * (cw + gap)
        y = y0 + r * (ch + gap)
        d.rounded_rectangle((x, y, x + cw, y + ch), 16, fill=tones[i], outline=CARD_BD, width=2)
        paste_center(im, icon(ic, 56), x + cw / 2, y + 39)
        tw = d.textlength(label, font=f_name)
        d.text((x + (cw - tw) / 2, y + 74), label, font=f_name, fill=(90, 68, 51))

    center(d, 392, '妈妈：藏在这间屋里。', f_small, (122, 92, 69))
    return circle_clip(im)


def screen_found():
    im = Image.new('RGBA', (W, H), BG)
    d = ImageDraw.Draw(im)
    paste_center(im, icon('console', 132), W / 2, 120)
    center(d, 196, '找到啦！', f_big, ACCENT)
    center(d, 244, '衣柜最里面，游戏机被羽绒服裹着！', f_body, (90, 68, 51))
    center(d, 274, '妈妈：「你怎么找到的？！」', f_small, MUTED)
    x0, y0, x1, y1 = (W - 150) / 2, 316, (W + 150) / 2, 368
    d.rounded_rectangle((x0, y0, x1, y1), 14, fill=ACCENT)
    tw = d.textlength('下一关', font=f_btn)
    d.text(((W - tw) / 2, 324), '下一关', font=f_btn, fill=CREAM)
    return circle_clip(im)


def main():
    shots = [('标题页', screen_title()), ('游戏中', screen_play()), ('找到了', screen_found())]
    for i, (name, im) in enumerate(shots):
        im.save(os.path.join(OUT, 'screen-%d.png' % (i + 1)))

    pad = 26
    sheet = Image.new('RGB', (W * 3 + pad * 4, H + pad * 2 + 30), (32, 32, 36))
    d = ImageDraw.Draw(sheet)
    for i, (name, im) in enumerate(shots):
        x = pad + i * (W + pad)
        # 表圈
        d.ellipse((x - 8, pad - 8 + 12, x + W + 7, pad + H + 7 + 12), fill=(58, 58, 64))
        sheet.paste(im, (x, pad + 12), im)
        tw = d.textlength(name, font=f_small)
        d.text((x + (W - tw) / 2, pad + H + 26), name, font=f_small, fill=(200, 200, 205))
    sheet.save(os.path.join(OUT, 'contact.png'))
    print('saved', OUT)


if __name__ == '__main__':
    main()
