import numpy as np
from collections import deque
from PIL import Image, ImageFilter
from scipy import ndimage as ndi

BASE = r"C:/Users/myma/AppData/Local/Temp/claude/97f6e422c1775293/bc9452eb-aa13-4f93-8276-f0deca776c69/"
OUT = BASE + "scratchpad/cut/"

def load(n): return Image.open(BASE + "images/" + n).convert("RGB")

def flood(passable, seeds):
    h, w = passable.shape
    seen = np.zeros((h, w), bool)
    dq = deque()
    for (x, y) in seeds:
        if 0 <= x < w and 0 <= y < h and passable[y, x] and not seen[y, x]:
            seen[y, x] = True; dq.append((x, y))
    while dq:
        x, y = dq.popleft()
        for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if 0 <= nx < w and 0 <= ny < h and passable[ny, nx] and not seen[ny, nx]:
                seen[ny, nx] = True; dq.append((nx, ny))
    return seen

def finish(rgb, fg, name, keep_min=60, erode=1, blur=0.7, comp="all"):
    # drop tiny islands, fill holes, soften edge
    lab, n = ndi.label(fg)
    sizes = ndi.sum(fg, lab, range(1, n+1))
    keep = np.zeros_like(fg)
    for i, s in enumerate(sizes, 1):
        if s >= keep_min: keep |= (lab == i)
    keep = ndi.binary_fill_holes(keep)
    a = Image.fromarray((keep*255).astype("uint8"))
    for _ in range(erode): a = a.filter(ImageFilter.MinFilter(3))
    a = a.filter(ImageFilter.GaussianBlur(blur))
    out = rgb.convert("RGBA"); out.putalpha(a)
    out.save(OUT + name + ".png", optimize=True)
    # preview on a flat color
    prev = Image.new("RGBA", out.size, (255, 143, 31, 255)); prev.alpha_composite(out)
    prev = prev.resize((out.width*3, out.height*3), Image.LANCZOS); prev.convert("RGB").save(OUT + name + "_prev.png")
    return out

# ---- Maryam (image 2) ----
im = load("2.png")
box = (528, 130, 711, 471)
c = im.crop(box)
arr = np.array(c).astype(int)
# remove footer line residue near bottom-left (abs y 446-452, x<548)
ya, yb = 446-130, 453-130
arr[ya:yb, 0:20] = arr[ya-6:ya-5, 0:20]
c = Image.fromarray(arr.astype("uint8"))
mx = arr.max(axis=2); mn = arr.min(axis=2)
orange = (arr[..., 0] > 140) & (arr[..., 2] < 90)
passable = ((mx < 100) | orange)
# wall off the left shoulder fade so the flood cannot leak into the sleeve
h, w = mx.shape
passable[int(690/3)-4:, 0:9] = False
seeds = [(20, 40), (60, 10), (120, 3), (170, 3), (5, 60), (5, 110), (180, 140), (181, 150), (178, 135)]
bg = flood(passable, seeds)
fg = ~bg
fg[:, :0] = fg[:, :0]
res = finish(c, fg, "maryam", keep_min=400)
# fade the far-left sliver
a = np.array(res.split()[3]).astype(float)
ramp = np.clip((np.arange(a.shape[1]) - 4) / 26.0, 0, 1)
a *= ramp[None, :]
res.putalpha(Image.fromarray(a.astype("uint8")))
res.save(OUT + "maryam.png", optimize=True)
prev = Image.new("RGBA", res.size, (255, 143, 31, 255)); prev.alpha_composite(res)
prev.resize((res.width*3, res.height*3), Image.LANCZOS).convert("RGB").save(OUT + "maryam_prev.png")
print("maryam", res.size)

# ---- woman (image 3) ----
im = load("3.png")
c = im.crop((358, 172, 505, 470)); arr = np.array(c).astype(int)
yellow = (arr[..., 0] > 150) & (arr[..., 1] > 100) & (arr[..., 2] < 120)
yellow = ndi.binary_dilation(yellow, iterations=1)
passable = (arr.max(axis=2) < 70) & ~yellow
bg = flood(passable, [(140, 150), (100, 10), (140, 290), (120, 80), (130, 250)])
res = finish(c, ~bg, "woman", keep_min=20)
print("woman", res.size)

# ---- man (image 3) ----
c = im.crop((600, 285, 707, 470)); arr = np.array(c).astype(int)
yellow = (arr[..., 0] > 150) & (arr[..., 1] > 100) & (arr[..., 2] < 120)
yellow = ndi.binary_dilation(yellow, iterations=1)
passable = (arr.max(axis=2) < 70) & ~yellow
bg = flood(passable, [(5, 5), (5, 100), (40, 150), (30, 30), (50, 170)])
res = finish(c, ~bg, "man", keep_min=20)
print("man", res.size)
