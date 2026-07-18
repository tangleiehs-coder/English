# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG = (250, 247, 241)
INK = (43, 43, 43)
MUTED = (138, 129, 117)
ORANGE = (255, 119, 0)

font_path = "C:/Windows/Fonts/msyh.ttc"
f_title = ImageFont.truetype(font_path, 46)
f_sub = ImageFont.truetype(font_path, 24)
f_spine = ImageFont.truetype(font_path, 30)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# 标题
d.text((70, 60), "我的 EHS 英语书架", font=f_title, fill=INK)
d.text((72, 128), "用 5W 认识训练营，再翻几本样书", font=f_sub, fill=MUTED)
# 橙色小标
d.text((72, 170), "安全五点半 · EHS情景英语", font=f_sub, fill=ORANGE)

# 书脊数据： (文字, 颜色)
spines = [
    ("何事", (0, 102, 204)),
    ("何人", (14, 159, 154)),
    ("何时", (201, 151, 31)),
    ("何地", (255, 119, 0)),
    ("为何", (138, 109, 181)),
    ("点读卡", (47, 158, 107)),
    ("样课试听", (255, 119, 0)),
    ("日常生活", (14, 159, 154)),
    ("EHS场景", (0, 102, 204)),
]

n = len(spines)
board_y = 560
left = 70
right = W - 70
gap = 16
bw = (right - left - gap * (n - 1)) / n
top = 215
sp_h = board_y - top - 6

for i, (txt, col) in enumerate(spines):
    x = left + i * (bw + gap)
    # 书脊
    d.rectangle([x, top, x + bw, top + sp_h], fill=col)
    # 顶部高光带
    d.rectangle([x, top, x + bw, top + 10], fill=(255, 255, 255))
    # 竖排文字（逐字）
    chars = list(txt)
    cw = sp_h / len(chars)
    for j, ch in enumerate(chars):
        cy = top + 22 + j * cw + cw / 2
        d.text((x + bw / 2, cy), ch, font=f_spine, fill=(255, 255, 255), anchor="mm")

# 木质书架
d.rectangle([left - 20, board_y, right + 20, board_y + 26], fill=(179, 167, 141))
d.rectangle([left - 20, board_y, right + 20, board_y + 4], fill=(205, 193, 170))

img.save("og_shelf.png")
print("og_shelf.png saved", img.size)
