import re
import os; D = os.path.dirname(os.path.abspath(__file__)) + "/"
src = open(D+"ai-baithak-palettes.html", encoding="utf-8").read()
css = open(D+"cut/ph.css", encoding="utf-8").read()
assert "/*__PH_CSS__*/" in src
built = src.replace("/*__PH_CSS__*/", css)
open(D+"ai-baithak-built.html", "w", encoding="utf-8").write(built)
i = built.index('<svg width="0"')
pre = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
open(D+"ai-baithak-preview.html", "w", encoding="utf-8").write(pre + built[:i] + "</head><body>" + built[i:] + "</body></html>")
print("built", len(built))
