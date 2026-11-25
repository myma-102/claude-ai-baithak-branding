import json, re

D = r"C:/Users/myma/AppData/Local/Temp/claude/97f6e422c1775293/bc9452eb-aa13-4f93-8276-f0deca776c69/scratchpad/"
src = open(D + "ai-baithak-palettes.html", encoding="utf-8").read()

def bar(a, b, c):
    return "linear-gradient(90deg,%s 0 55%%,%s 55%% 78%%,%s 78%% 100%%)" % (a, b, c)

def variant(**kw):
    d = dict(kw)
    d.setdefault("card_fg", d["fg"]); d.setdefault("card_muted", d["muted"])
    d.setdefault("o1", d["c1"]); d.setdefault("url", d["o0"])
    d.setdefault("hl_bg", "transparent"); d.setdefault("logo", d["fg"]); d.setdefault("mark", d["o0"])
    d.setdefault("stroke", d["o0"]); d.setdefault("tag_bg", "transparent"); d.setdefault("panel", d["bg2"])
    return d

KEYS = ["bg","bg2","line","fg","muted","card_fg","card_muted","hl_fg","hl_bg","o0","o1","url","c0","c1","c2",
        "btn_bg","btn_fg","logo","mark","wave","stroke","tag_bg","tag_fg","disc","panel","bar"]

def css_vars(d):
    return ";".join("--%s:%s" % (k.replace("_", "-"), d[k]) for k in KEYS)

P = []

# L  Warm Neutral
P.append(dict(
    id="l", name="Warm Neutral", short="Paper + charcoal + soft apricot",
    mood="Warm greige and paper tones with charcoal for the dark posts. The orange is softened to apricot and used in one place per post, so the feed stays quiet.",
    best="Everyday posts, team intros, quotes and announcements. The closest calm option to your current orange, black and white.",
    watch="Apricot is soft, so it works as a highlight block with charcoal text on top, not as text on paper.",
    sw=[["Paper","#F6F2EC","Light base"],["Warm White","#FBF9F5","Cards"],["Charcoal","#2B2927","Dark base and text"],["Soft Apricot","#E09A62","Signature"],
        ["Sand","#E6D9C8","Accent 1"],["Taupe","#B9AEA0","Accent 2"],["Taupe Brown","#7D6A57","Labels on light"],["Warm Grey","#6F6A63","Secondary text"]],
    light=variant(bg="#F6F2EC",bg2="#FBF9F5",line="#E2DACE",fg="#2B2927",muted="#6F6A63",hl_fg="#2B2927",hl_bg="#E09A62",o0="#E09A62",o1="#7D6A57",url="#7D6A57",
                  c0="#E09A62",c1="#7D6A57",c2="#2B2927",btn_bg="#E09A62",btn_fg="#2B2927",wave="#E9E1D5",stroke="#2B2927",tag_fg="#7D6A57",disc="#E6D9C8",panel="#FBF9F5",
                  bar=bar("#E09A62","#B9AEA0","#E6D9C8")),
    dark=variant(bg="#2B2927",bg2="#373431",line="#4C4843",fg="#F6F2EC",muted="#B9B1A6",hl_fg="#E8A874",o0="#E09A62",c0="#E09A62",c1="#B9AEA0",c2="#E6D9C8",
                 btn_bg="#E09A62",btn_fg="#2B2927",wave="#34312E",tag_fg="#B9AEA0",disc="#5A544D",bar=bar("#E09A62","#B9AEA0","#E6D9C8")),
    accent=variant(bg="#E6D9C8",bg2="#FBF9F5",line="#D2C4B0",fg="#2B2927",muted="#5E5951",hl_fg="#2B2927",hl_bg="#E09A62",o0="#2B2927",o1="#7D6A57",url="#2B2927",
                   c0="#E09A62",c1="#7D6A57",c2="#2B2927",btn_bg="#2B2927",btn_fg="#F6F2EC",logo="#2B2927",mark="#E09A62",wave="#DDCFBC",stroke="#2B2927",
                   tag_bg="#2B2927",tag_fg="#E6D9C8",disc="#F6F2EC",panel="#FBF9F5",bar=bar("#2B2927","#B9AEA0","#E09A62")),
    dk="#2B2927",
    tiles=[("#F6F2EC","#2B2927","#7D6A57"),("#E6D9C8","#2B2927","#7D6A57"),("#E09A62","#2B2927","#2B2927"),("#2B2927","#F6F2EC","#E09A62"),("#B9AEA0","#2B2927","#2B2927")],
))

# M  Soft Sage
P.append(dict(
    id="m", name="Soft Sage", short="Mist sage + moss + soft clay",
    mood="A gentle sage-green base with deep moss for the dark posts. Soft clay stands in for orange, and the whole feed feels natural and unhurried.",
    best="Learning posts, workshops, recaps and community posts.",
    watch="Sage and clay are both quiet, so contrast comes from the dark moss. Keep body text on the base in moss, never in sage.",
    sw=[["Mist Sage","#EDF1EA","Light base"],["Cream","#FAFBF8","Cards"],["Deep Moss","#26302A","Dark base and text"],["Soft Clay","#D99B72","Signature"],
        ["Sage","#A9B8A2","Accent 1"],["Pale Sage","#D5DFD0","Accent 2"],["Deep Sage","#5F7A5B","Labels on light"],["Olive Grey","#5E6A5C","Secondary text"]],
    light=variant(bg="#EDF1EA",bg2="#FAFBF8",line="#D3DCCD",fg="#26302A",muted="#5E6A5C",hl_fg="#26302A",hl_bg="#D99B72",o0="#D99B72",o1="#5F7A5B",url="#5F7A5B",
                  c0="#D99B72",c1="#5F7A5B",c2="#26302A",btn_bg="#D99B72",btn_fg="#26302A",wave="#E0E7DB",stroke="#26302A",tag_fg="#5F7A5B",disc="#D5DFD0",panel="#FAFBF8",
                  bar=bar("#D99B72","#A9B8A2","#D5DFD0")),
    dark=variant(bg="#26302A",bg2="#313C35",line="#46544B",fg="#EDF1EA",muted="#AEBBA9",hl_fg="#E3A97F",o0="#D99B72",c0="#D99B72",c1="#A9B8A2",c2="#D5DFD0",
                 btn_bg="#D99B72",btn_fg="#26302A",wave="#2C3730",tag_fg="#A9B8A2",disc="#46544B",bar=bar("#D99B72","#A9B8A2","#D5DFD0")),
    accent=variant(bg="#A9B8A2",bg2="#FAFBF8",line="#8FA08A",fg="#1F2822",muted="#34443A",card_fg="#26302A",card_muted="#5E6A5C",hl_fg="#26302A",hl_bg="#EDF1EA",
                   o0="#26302A",o1="#26302A",url="#26302A",c0="#D99B72",c1="#5F7A5B",c2="#26302A",btn_bg="#26302A",btn_fg="#EDF1EA",logo="#26302A",mark="#26302A",
                   wave="#B8C5B1",stroke="#26302A",tag_bg="#26302A",tag_fg="#D5DFD0",disc="#EDF1EA",panel="#FAFBF8",bar=bar("#26302A","#EDF1EA","#D99B72")),
    dk="#26302A",
    tiles=[("#EDF1EA","#26302A","#5F7A5B"),("#D5DFD0","#26302A","#46544B"),("#D99B72","#26302A","#26302A"),("#26302A","#EDF1EA","#D99B72"),("#A9B8A2","#26302A","#26302A")],
))

# N  Dusty Blue
P.append(dict(
    id="n", name="Dusty Blue", short="Mist + slate + dusty blue",
    mood="A cool, misty base with slate for the dark posts and dusty blue for detail. A touch of soft apricot keeps the link to your orange.",
    best="Event posts, partner posts and anything that should feel clean and professional.",
    watch="Dusty blue is low contrast on the mist base, so use it for shapes and fills. Text stays slate.",
    sw=[["Mist","#EEF1F4","Light base"],["Cloud","#FAFBFC","Cards"],["Slate","#2A3441","Dark base and text"],["Soft Apricot","#DE9C6C","Signature"],
        ["Dusty Blue","#8FA4BA","Accent 1"],["Fog Blue","#D4DEE8","Accent 2"],["Steel Blue","#4F6A86","Labels on light"],["Blue Grey","#62707F","Secondary text"]],
    light=variant(bg="#EEF1F4",bg2="#FAFBFC",line="#D7DEE6",fg="#2A3441",muted="#62707F",hl_fg="#2A3441",hl_bg="#DE9C6C",o0="#DE9C6C",o1="#4F6A86",url="#4F6A86",
                  c0="#DE9C6C",c1="#4F6A86",c2="#2A3441",btn_bg="#DE9C6C",btn_fg="#2A3441",wave="#E2E8EE",stroke="#2A3441",tag_fg="#4F6A86",disc="#D4DEE8",panel="#FAFBFC",
                  bar=bar("#DE9C6C","#8FA4BA","#D4DEE8")),
    dark=variant(bg="#2A3441",bg2="#354253",line="#4A5A6E",fg="#EEF1F4",muted="#B2BECB",hl_fg="#E7AE84",o0="#DE9C6C",c0="#DE9C6C",c1="#8FA4BA",c2="#D4DEE8",
                 btn_bg="#DE9C6C",btn_fg="#2A3441",wave="#313D4C",tag_fg="#8FA4BA",disc="#4A5A6E",bar=bar("#DE9C6C","#8FA4BA","#D4DEE8")),
    accent=variant(bg="#8FA4BA",bg2="#FAFBFC",line="#7A90A7",fg="#1F2935",muted="#2A3A4D",card_fg="#2A3441",card_muted="#62707F",hl_fg="#2A3441",hl_bg="#DE9C6C",
                   o0="#2A3441",o1="#2A3441",url="#1F2935",c0="#DE9C6C",c1="#4F6A86",c2="#2A3441",btn_bg="#2A3441",btn_fg="#EEF1F4",logo="#1F2935",mark="#1F2935",
                   wave="#A1B3C6",stroke="#1F2935",tag_bg="#2A3441",tag_fg="#D4DEE8",disc="#D4DEE8",panel="#FAFBFC",bar=bar("#2A3441","#D4DEE8","#DE9C6C")),
    dk="#2A3441",
    tiles=[("#EEF1F4","#2A3441","#4F6A86"),("#D4DEE8","#2A3441","#4F6A86"),("#DE9C6C","#2A3441","#2A3441"),("#2A3441","#EEF1F4","#DE9C6C"),("#8FA4BA","#1F2935","#1F2935")],
))

# O  Blush Stone
P.append(dict(
    id="o", name="Blush Stone", short="Blush + cocoa + dusty rose",
    mood="A soft blush-stone base with cocoa for the dark posts and dusty rose for detail. Warm and gentle without being bright pink.",
    best="Team spotlights, volunteer posts and quotes.",
    watch="Dusty rose and apricot sit close together, so use one per post. Labels on the light base use the deeper rose.",
    sw=[["Blush Stone","#F5EAE6","Light base"],["Porcelain","#FCF8F6","Cards"],["Cocoa","#3A2D2B","Dark base and text"],["Soft Apricot","#DA976F","Signature"],
        ["Dusty Rose","#D4A5A5","Accent 1"],["Shell","#E8D3CC","Accent 2"],["Deep Rose","#96605F","Labels on light"],["Mauve Grey","#7B6865","Secondary text"]],
    light=variant(bg="#F5EAE6",bg2="#FCF8F6",line="#E6D6D0",fg="#3A2D2B",muted="#7B6865",hl_fg="#3A2D2B",hl_bg="#DA976F",o0="#DA976F",o1="#96605F",url="#96605F",
                  c0="#DA976F",c1="#96605F",c2="#3A2D2B",btn_bg="#DA976F",btn_fg="#3A2D2B",wave="#EBDCD6",stroke="#3A2D2B",tag_fg="#96605F",disc="#E8D3CC",panel="#FCF8F6",
                  bar=bar("#DA976F","#D4A5A5","#E8D3CC")),
    dark=variant(bg="#3A2D2B",bg2="#483A37",line="#5E4D49",fg="#F5EAE6",muted="#C9B6B1",hl_fg="#E8A985",o0="#DA976F",c0="#DA976F",c1="#D4A5A5",c2="#E8D3CC",
                 btn_bg="#DA976F",btn_fg="#3A2D2B",wave="#43342F",tag_fg="#D4A5A5",disc="#5E4D49",bar=bar("#DA976F","#D4A5A5","#E8D3CC")),
    accent=variant(bg="#D4A5A5",bg2="#FCF8F6",line="#C48F8F",fg="#3A2D2B",muted="#5C3F3E",card_fg="#3A2D2B",card_muted="#7B6865",hl_fg="#3A2D2B",hl_bg="#F5EAE6",
                   o0="#3A2D2B",o1="#3A2D2B",url="#3A2D2B",c0="#DA976F",c1="#96605F",c2="#3A2D2B",btn_bg="#3A2D2B",btn_fg="#F5EAE6",logo="#3A2D2B",mark="#3A2D2B",
                   wave="#DDB5B5",stroke="#3A2D2B",tag_bg="#3A2D2B",tag_fg="#E8D3CC",disc="#F5EAE6",panel="#FCF8F6",bar=bar("#3A2D2B","#E8D3CC","#DA976F")),
    dk="#3A2D2B",
    tiles=[("#F5EAE6","#3A2D2B","#96605F"),("#E8D3CC","#3A2D2B","#96605F"),("#DA976F","#3A2D2B","#3A2D2B"),("#3A2D2B","#F5EAE6","#DA976F"),("#D4A5A5","#3A2D2B","#3A2D2B")],
))

# P  Mono Ink
P.append(dict(
    id="p", name="Mono Ink", short="Greys + ink + one soft apricot",
    mood="The most minimal option: fog, white and ink with greys in between, and a single soft apricot accent. Almost no color, so the photos and words do the work.",
    best="A clean, editorial feed. Works for every post type.",
    watch="With so little color, posts can feel plain. Keep strong photos and headlines, and use the apricot only as the highlight.",
    sw=[["Fog","#F4F4F2","Light base"],["White","#FFFFFF","Cards"],["Ink","#161616","Dark base and text"],["Soft Apricot","#E8A06A","Signature"],
        ["Stone","#9C9C98","Accent 1"],["Light Grey","#DCDCD8","Accent 2"],["Graphite","#5F5F5B","Secondary text"]],
    light=variant(bg="#F4F4F2",bg2="#FFFFFF",line="#E0E0DC",fg="#161616",muted="#5F5F5B",hl_fg="#161616",hl_bg="#E8A06A",o0="#E8A06A",o1="#5F5F5B",url="#161616",
                  c0="#E8A06A",c1="#5F5F5B",c2="#161616",btn_bg="#E8A06A",btn_fg="#161616",wave="#E8E8E4",stroke="#161616",tag_fg="#5F5F5B",disc="#DCDCD8",panel="#FFFFFF",
                  bar=bar("#E8A06A","#9C9C98","#DCDCD8")),
    dark=variant(bg="#161616",bg2="#222222",line="#3A3A38",fg="#F4F4F2",muted="#A8A8A4",hl_fg="#E8A06A",o0="#E8A06A",c0="#E8A06A",c1="#9C9C98",c2="#DCDCD8",
                 btn_bg="#E8A06A",btn_fg="#161616",wave="#232322",tag_fg="#A8A8A4",disc="#3A3A38",bar=bar("#E8A06A","#9C9C98","#DCDCD8")),
    accent=variant(bg="#DCDCD8",bg2="#FFFFFF",line="#C4C4C0",fg="#161616",muted="#4A4A47",hl_fg="#161616",hl_bg="#E8A06A",o0="#161616",o1="#161616",url="#161616",
                   c0="#E8A06A",c1="#5F5F5B",c2="#161616",btn_bg="#161616",btn_fg="#F4F4F2",logo="#161616",mark="#161616",wave="#CFCFCB",stroke="#161616",
                   tag_bg="#161616",tag_fg="#DCDCD8",disc="#F4F4F2",panel="#FFFFFF",bar=bar("#161616","#9C9C98","#E8A06A")),
    dk="#161616",
    tiles=[("#F4F4F2","#161616","#5F5F5B"),("#DCDCD8","#161616","#5F5F5B"),("#E8A06A","#161616","#161616"),("#161616","#F4F4F2","#E8A06A"),("#9C9C98","#161616","#161616")],
))

# ---------------------------------------------------------------- generated CSS
css = []
for p in P:
    cls = "pal-" + p["id"]
    tiles = ";".join("--k%db:%s;--k%df:%s;--k%dk:%s" % (i, t[0], i, t[1], i, t[2]) for i, t in enumerate(p["tiles"]))
    dc = ";".join("--dc%d:%s" % (i, p["dark"]["c%d" % i]) for i in range(3))
    css.append(".%s{%s;--dk:%s;%s;%s}" % (cls, css_vars(p["light"]), p["dk"], dc, tiles))
    css.append(".%s .v-d{%s}" % (cls, css_vars(p["dark"])))
    css.append(".%s .v-a{%s}" % (cls, css_vars(p["accent"])))
css.append("/* calm board: photos are softened so they match the muted palettes */")
css.append(".ph,.tph{filter:saturate(.6)}")
palette_css = "\n".join(css) + "\n\n"

out = src
def must_sub(pattern, repl, text, flags=re.S, count=1):
    new, n = re.subn(pattern, lambda m: repl, text, count=count, flags=flags)
    assert n == count, (pattern, n)
    return new

a = out.index(".pal-a{--bg:#0E0B14")
b = out.index("/* ===== sample posts (sizes in cqw")
out = out[:a] + palette_css + out[b:]

assert ".url{font:700 4.4cqw/1 var(--font-d);color:var(--o0);" in out
out = out.replace(".url{font:700 4.4cqw/1 var(--font-d);color:var(--o0);", ".url{font:700 4.4cqw/1 var(--font-d);color:var(--url,var(--o0));")

tile_css = "\n".join(
    ".k%d{background:var(--k%db);color:var(--k%df)} .k%d .k{color:var(--k%dk)}" % (i, i, i, i, i) for i in range(5))
out = must_sub(r"\.k0\{background:var\(--bg\);color:var\(--fg\)\}.*?\.k4\{background:var\(--c2\);color:var\(--on2\)\}", tile_css, out)

assert ".pal-e .ps .cta2{background:#FF8F1F;color:#0D0D0D}\n" in out
out = out.replace(".pal-e .ps .cta2{background:#FF8F1F;color:#0D0D0D}\n", "")
assert ".cv-note{font-size:12.5px;" in out
out = out.replace(".cv-note{font-size:12.5px;", ".cv .ring.dk{background:var(--dk)}\n.cv-note{font-size:12.5px;")

out = must_sub(r"\n\s*<filter id=\"gm-duo\".*?</filter>", "", out)
out = must_sub(r"  var CMP = .*?</p></div>';\n", "", out)

pal_js = []
variants = ["v-l", "v-l", "v-d", "v-l", "v-a", "v-d"]
for p in P:
    pal_js.append(json.dumps(dict(id=p["id"], cls="pal-" + p["id"], name=p["name"], mode="Calm", short=p["short"],
                                  mood=p["mood"], best=p["best"], watch=p["watch"], sw=p["sw"], v=variants), ensure_ascii=False))
out = must_sub(r"  var PAL = \[.*?\n  \];\n", "  var PAL = [\n    " + ",\n    ".join(pal_js) + "\n  ];\n", out)
tiles_js = """  var TILES = [
    ['Team','Meet the Leadership Council','k0'],
    ['Event','21 Nov Mega Project Day','k2'],
    ['Workshop','Build your first AI agent','k3','robot'],
    ['Join us','We are extending our core teams','k1'],
    ['Spotlight','Meet our team lead','k4','maryam'],
    ['Quote','Learning grows when people come together','k0'],
    ['Teamwork','Different skills, same goal','k3','duo'],
    ['Partners','Our outreach partner','k1'],
    ['Register','Join the next session','k2']
  ];
"""
out = must_sub(r"  var TILES = \[.*?\n  \];\n", tiles_js, out)
assert "var letters = 'ABCDEF';" in out
out = out.replace("var letters = 'ABCDEF';", "var letters = 'LMNOP';")
old_cov = """  function covers(){
    return COVERS.map(function(c,i){
      return '<div class="cv"><div class="ring" style="--rc:var(--c'+(i%3)+')">'+icon(c[0])+'</div><span>'+c[1]+'</span></div>';
    }).join('');
  }"""
new_cov = """  function covers(){
    return COVERS.map(function(c,i){
      var dark = i % 2 === 1;
      var rc = 'var(--' + (dark ? 'dc' : 'c') + (i%3) + ')';
      return '<div class="cv"><div class="ring'+(dark?' dk':'')+'" style="--rc:'+rc+'">'+icon(c[0])+'</div><span>'+c[1]+'</span></div>';
    }).join('');
  }"""
assert old_cov in out
out = out.replace(old_cov, new_cov)
old_note = "Ring color follows the topic: orange for events, accent 1 for team, accent 2 for learning. Keep the same rule on every cover."
assert old_note in out
out = out.replace(old_note, "Covers alternate between light and dark fills. Ring color follows the topic, and the same topic always keeps the same ring color.")

out = out.replace("<title>AI Baithak Palettes</title>", "<title>AI Baithak Calm Palettes</title>")
header = """<header>
    <p class="eyebrow">AI Baithak · Instagram color options · calm and minimal</p>
    <h1>Five calm, minimal color options</h1>
    <p class="lede">These replace the earlier G to K, which were too vibrant. Every option here is <b>low in saturation</b>: soft neutrals, one muted accent, and a darker variation for emphasis. Your orange is softened to apricot or clay and used once per post. The lettering continues from <a href="https://claude.ai/artifact/BmNWnGyrjbfA25xWZbKZJw" target="_blank" rel="noopener">the first board</a> (A to F), so these are L to P.</p>
    <p class="lede">Each option shows six sample posts (three of them with people and the robot from your workshop post), story highlight covers and a nine-post feed. The photos are softened a little to match. Click any color to copy its hex code.</p>
  </header>"""
out = must_sub(r"<header>.*?</header>", header, out)
guide = """<section class="opt" id="guide-sec">
    <h2 class="sec" style="margin-top:0">How to keep it calm</h2>
    <div class="guide">
      <div><h3>Mostly neutral</h3><p>Aim for about 80% neutral colors: the base, the card color and the text. The accent colors fill the rest.</p></div>
      <div><h3>One accent per post</h3><p>Pick a single accent for each post. The signature color goes on one highlight block, button or shape, with dark text on top.</p></div>
      <div><h3>Dark for emphasis</h3><p>Use the dark variation for events, quotes and announcements, roughly one post in three. The rest stay on the light base.</p></div>
      <div><h3>Let the photos lead</h3><p>With quiet colors, the people and headlines carry the post. Keep photos large and give text room around it.</p></div>
    </div>

    <div class="pick">
      <h3>My pick</h3>
      <p>Use <b>L · Warm Neutral</b> as the main look. It is the calmest option that still feels like AI Baithak, because the apricot is a softer version of your orange and the charcoal stands in for your black.</p>
      <p>If the team wants the most minimal feed, choose <b>P · Mono Ink</b>. For a cooler, more professional tone choose <b>N · Dusty Blue</b>.</p>
      <p>This is a recommendation. The final choice is the team's.</p>
    </div>

    <p class="foot-note">The logo and partner names in these mockups are redrawn placeholders for layout only. Real artwork replaces them in the final templates. Post text is taken from your existing posts. The people and the robot are cut out of screenshots of your own posts, so they look soft here. Original photos will look sharper, and each needs its own cut-out with a transparent background.</p>
  </section>"""
out = must_sub(r'<section class="opt" id="guide-sec">.*?</section>', guide, out)

open(D + "ai-baithak-calm.html", "w", encoding="utf-8").write(out)

css_ph = open(D + "cut/ph.css", encoding="utf-8").read()
assert "/*__PH_CSS__*/" in out
built = out.replace("/*__PH_CSS__*/", css_ph)
open(D + "ai-baithak-calm-built.html", "w", encoding="utf-8").write(built)
i = built.index('<svg width="0"')
pre = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
open(D + "ai-baithak-calm-preview.html", "w", encoding="utf-8").write(pre + built[:i] + "</head><body>" + built[i:] + "</body></html>")
print("ok", len(built))
