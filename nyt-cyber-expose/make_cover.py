import os
from PIL import Image, ImageDraw, ImageFont

bg_path = '/home/user0/files/SSRN_Strategic_Intelligence_Stack/publishing/nyt-cyber-expose/kdp/handoff/cover_background.png'
out_jpg = '/home/user0/files/SSRN_Strategic_Intelligence_Stack/publishing/nyt-cyber-expose/kdp/handoff/cover_final.jpg'
out_pdf = '/home/user0/files/SSRN_Strategic_Intelligence_Stack/publishing/nyt-cyber-expose/kdp/handoff/cover_final.pdf'

# Target KDP Print Proportions: 5.5 x 8.5 inches at 300 DPI -> 1650 x 2550 pixels
TARGET_W, TARGET_H = 1650, 2550

img = Image.open(bg_path).convert('RGB')

img_w, img_h = img.size
aspect_target = TARGET_W / TARGET_H
aspect_img = img_w / img_h

if aspect_img > aspect_target:
    new_w = int(img_h * aspect_target)
    left = (img_w - new_w) / 2
    img = img.crop((left, 0, left + new_w, img_h))
else:
    new_h = int(img_w / aspect_target)
    top = (img_h - new_h) / 2
    img = img.crop((0, top, img_w, top + new_h))

img = img.resize((TARGET_W, TARGET_H), Image.LANCZOS)
draw = ImageDraw.Draw(img)

try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 150)
    font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 60)
    font_author = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 100)
except:
    font_title = ImageFont.load_default()
    font_sub = ImageFont.load_default()
    font_author = ImageFont.load_default()

title = "MINUTES TO ZERO"
subtitle = "Vol 1: The Architecture of Blindness"
author = "NIMMIT X"

def draw_text(draw, text, font, y_pos, color="white"):
    box = draw.textbbox((0,0), text, font=font)
    w = box[2] - box[0]
    x = (TARGET_W - w) / 2
    draw.text((x, y_pos), text, font=font, fill=color)

draw_text(draw, title, font_title, 350)
draw_text(draw, subtitle, font_sub, 550)
draw_text(draw, author, font_author, 2200)

img.save(out_jpg, quality=95)
img.save(out_pdf, resolution=300.0)
print("Cover generated and exported to JPG and PDF.")
