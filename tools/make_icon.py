"""Make the 1024x1024 August Works / Monstah Uploads app icon (icon.png)."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

S = 1024
img = Image.new("RGB", (S, S), "#1d1d1b")
d = ImageDraw.Draw(img)
d.ellipse((112, 112, S - 112, S - 112), fill="#e8a33d")
font = None
for name in ("georgiab.ttf", "georgia.ttf", "arialbd.ttf"):
    try:
        font = ImageFont.truetype(name, 320)
        break
    except OSError:
        continue
text = "AW"
box = d.textbbox((0, 0), text, font=font)
w, h = box[2] - box[0], box[3] - box[1]
d.text(((S - w) / 2 - box[0], (S - h) / 2 - box[1]), text, fill="#1d1d1b", font=font)
out = Path(__file__).resolve().parent.parent / "icon.png"
img.save(out)
print(out)
