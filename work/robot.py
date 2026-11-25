import numpy as np
from collections import deque
from PIL import Image, ImageFilter
from scipy import ndimage as ndi
BASE = r"C:/Users/myma/AppData/Local/Temp/claude/97f6e422c1775293/bc9452eb-aa13-4f93-8276-f0deca776c69/"
OUT = BASE + "scratchpad/cut/"
im = Image.open(BASE+"images/4.png").convert("RGB")
X0,Y0,X1,Y1 = 78,188,262,376
c = im.crop((X0,Y0,X1,Y1)); arr = np.array(c).astype(int); H,W = arr.shape[:2]
bgc = np.array([9,6,1])
def paint(x0,y0,x1,y1): arr[y0-Y0:y1-Y0, x0-X0:x1-X0] = bgc
paint(78,188,124,214)     # stray text + curve, top-left
paint(205,188,262,223)    # stray text, top-right
paint(214,254,262,288)    # dashed arrow
paint(236,288,262,300)    # keep laptop but clear glow bits? (small)
c = Image.fromarray(arr.astype('uint8'))
mx = arr.max(axis=2)
passable = (mx < 60)
def flood(passable, seeds):
    h,w = passable.shape; seen = np.zeros((h,w),bool); dq = deque()
    for x,y in seeds:
        if 0<=x<w and 0<=y<h and passable[y,x] and not seen[y,x]: seen[y,x]=True; dq.append((x,y))
    while dq:
        x,y = dq.popleft()
        for nx,ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if 0<=nx<w and 0<=ny<h and passable[ny,nx] and not seen[ny,nx]:
                seen[ny,nx]=True; dq.append((nx,ny))
    return seen
seeds=[(2,2),(70,2),(140,2),(180,2),(2,60),(2,120),(180,60),(180,100),(2,170),(60,H-3),(140,H-3),(180,H-3),(105,5),(180,150)]
bg = flood(passable, seeds)
fg = ~bg
lab,n = ndi.label(fg); sizes = ndi.sum(fg,lab,range(1,n+1))
keep = np.zeros_like(fg)
for i,s in enumerate(sizes,1):
    if s>=300: keep |= (lab==i)
keep = ndi.binary_fill_holes(keep)
a = Image.fromarray((keep*255).astype('uint8')).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.7))
out = c.convert('RGBA'); out.putalpha(a); out.save(OUT+'robot.png',optimize=True)
prev = Image.new('RGBA',out.size,(255,143,31,255)); prev.alpha_composite(out)
prev.resize((out.width*3,out.height*3),Image.LANCZOS).convert('RGB').save(OUT+'robot_prev.png'); print(out.size)
