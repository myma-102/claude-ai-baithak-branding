D = r"C:/Users/myma/AppData/Local/Temp/claude/97f6e422c1775293/bc9452eb-aa13-4f93-8276-f0deca776c69/scratchpad/"
src = open(D + "ai-baithak-grid.html", encoding="utf-8").read()
css = open(D + "cut/ph.css", encoding="utf-8").read() + "\n" + open(D + "cut/leaders.css", encoding="utf-8").read()
assert "/*__PH_CSS__*/" in src and "/*__NOW_JS__*/" in src
built = src.replace("/*__PH_CSS__*/", css).replace("/*__NOW_JS__*/", open(D + "cut/now.js", encoding="utf-8").read())
open(D + "ai-baithak-grid-built.html", "w", encoding="utf-8").write(built)
i = built.index('<svg width="0"')
pre = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
open(D + "ai-baithak-grid-preview.html", "w", encoding="utf-8").write(pre + built[:i] + "</head><body>" + built[i:] + "</body></html>")
print("ok", len(built))
