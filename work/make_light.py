import json, re

D = r"C:/Users/myma/AppData/Local/Temp/claude/97f6e422c1775293/bc9452eb-aa13-4f93-8276-f0deca776c69/scratchpad/"
src = open(D + "ai-baithak-palettes.html", encoding="utf-8").read()

# ---------------------------------------------------------------- palette data
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

# G  Sky & Sun
P.append(dict(
    id="g", name="Sky &amp; Sun", short="Sky blue + navy + orange",
    mood="A fresh sky-blue base with navy where you need dark. Orange and blue are opposites, so the signature orange stands out without being loud.",
    best="AI workshops, announcements and event posters. Anything that should feel clear and trustworthy.",
    watch="Keep blue to labels, icons and small shapes. Orange text on the sky base is weak, so orange goes on highlight blocks with navy text on top.",
    sw=[["Sky","#EAF3FF","Light base"],["Cloud White","#FFFFFF","Cards"],["Navy","#0B2545","Dark base and text"],["Sun Orange","#FF8F1F","Signature"],
        ["Sky Blue","#4DA3FF","Accent 1"],["Butter","#FFD35C","Accent 2"],["Link Blue","#2F7FE0","Labels on light"],["Slate Blue","#4A5F7A","Secondary text"]],
    light=variant(bg="#EAF3FF",bg2="#FFFFFF",line="#C5DAF3",fg="#0B2545",muted="#4A5F7A",hl_fg="#0B2545",hl_bg="#FF8F1F",o0="#FF8F1F",o1="#2F7FE0",url="#D96A00",
                  c0="#FF8F1F",c1="#2F7FE0",c2="#0B2545",btn_bg="#FF8F1F",btn_fg="#0B2545",wave="#CFE1F7",stroke="#0B2545",tag_fg="#2F7FE0",disc="#FFD35C",panel="#FFFFFF",
                  bar=bar("#FF8F1F","#4DA3FF","#FFD35C")),
    dark=variant(bg="#0B2545",bg2="#13335F",line="#24508A",fg="#FFFFFF",muted="#A9BEDA",hl_fg="#FF8F1F",o0="#FF8F1F",c0="#FF8F1F",c1="#4DA3FF",c2="#FFD35C",
                 btn_bg="#FF8F1F",btn_fg="#0B2545",wave="#17406F",tag_fg="#4DA3FF",disc="#4DA3FF",bar=bar("#FF8F1F","#4DA3FF","#FFD35C")),
    accent=variant(bg="#FF8F1F",bg2="#0B2545",line="#0B2545",fg="#0B2545",muted="#4A2A00",card_fg="#FFFFFF",card_muted="#A9BEDA",hl_fg="#FF8F1F",hl_bg="#0B2545",
                   o0="#0B2545",o1="#0B2545",c0="#FF8F1F",c1="#FFD35C",c2="#4DA3FF",btn_bg="#0B2545",btn_fg="#FF8F1F",logo="#0B2545",mark="#0B2545",wave="#FFA84D",
                   stroke="#0B2545",tag_bg="#0B2545",tag_fg="#FFD35C",disc="#EAF3FF",panel="#0B2545",bar=bar("#0B2545","#EAF3FF","#FFD35C")),
    dk="#0B2545",
    tiles=[("#EAF3FF","#0B2545","#D96A00"),("#FFFFFF","#0B2545","#2F7FE0"),("#FF8F1F","#0B2545","#0B2545"),("#0B2545","#FFFFFF","#FF8F1F"),("#4DA3FF","#0B2545","#0B2545")],
))

# H  Blush & Berry
P.append(dict(
    id="h", name="Blush &amp; Berry", short="Blush pink + plum + orange",
    mood="A soft blush base with plum for the dark posts. Warm and friendly, which suits volunteers, team spotlights and community moments.",
    best="Team spotlights, volunteer posts, community recaps and quotes.",
    watch="Berry and orange are both warm and can compete. Use berry for labels and one accent shape per post, and keep orange to the highlight block.",
    sw=[["Blush","#FFEEEA","Light base"],["Cloud White","#FFFFFF","Cards"],["Plum","#2A1026","Dark base and text"],["Signal Orange","#FF8F1F","Signature"],
        ["Berry","#D6336C","Accent 1"],["Peach","#FFC9B3","Accent 2"],["Berry Light","#FF6FA5","Berry on dark"],["Mauve","#7A5568","Secondary text"]],
    light=variant(bg="#FFEEEA",bg2="#FFFFFF",line="#F5D2CB",fg="#2A1026",muted="#7A5568",hl_fg="#2A1026",hl_bg="#FF8F1F",o0="#FF8F1F",o1="#D6336C",url="#D6336C",
                  c0="#FF8F1F",c1="#D6336C",c2="#2A1026",btn_bg="#FF8F1F",btn_fg="#2A1026",wave="#F8DAD4",stroke="#2A1026",tag_fg="#D6336C",disc="#FFC9B3",panel="#FFFFFF",
                  bar=bar("#FF8F1F","#D6336C","#FFC9B3")),
    dark=variant(bg="#2A1026",bg2="#3D1A38",line="#5E2C57",fg="#FFFFFF",muted="#D8B7CF",hl_fg="#FF8F1F",o0="#FF8F1F",c0="#FF8F1F",c1="#FF6FA5",c2="#FFC9B3",
                 btn_bg="#FF8F1F",btn_fg="#2A1026",wave="#3B1D36",tag_fg="#FF6FA5",disc="#D6336C",bar=bar("#FF8F1F","#FF6FA5","#FFC9B3")),
    accent=variant(bg="#D6336C",bg2="#FFFFFF",line="#FFFFFF",fg="#FFFFFF",muted="#FFE3EC",card_fg="#2A1026",card_muted="#7A5568",hl_fg="#2A1026",hl_bg="#FF8F1F",
                   o0="#FFC9B3",o1="#FFC9B3",url="#FFFFFF",c0="#FF8F1F",c1="#D6336C",c2="#2A1026",btn_bg="#FF8F1F",btn_fg="#2A1026",logo="#FFFFFF",mark="#FFC9B3",
                   wave="#E2527F",stroke="#FFFFFF",tag_bg="#2A1026",tag_fg="#FFC9B3",disc="#FFC9B3",panel="#FFFFFF",bar=bar("#2A1026","#FFC9B3","#FF8F1F")),
    dk="#2A1026",
    tiles=[("#FFEEEA","#2A1026","#D6336C"),("#FFFFFF","#2A1026","#D6336C"),("#FF8F1F","#2A1026","#2A1026"),("#2A1026","#FFFFFF","#FF8F1F"),("#D6336C","#FFFFFF","#FFC9B3")],
))

# I  Mint & Lime
P.append(dict(
    id="i", name="Mint &amp; Lime", short="Mint + forest + orange + lime",
    mood="A cool mint base with deep forest green for the dark posts and a lime pop. Orange stays the signature and green adds a fresh, growing feeling.",
    best="Learning posts, workshops, recaps and anything about growth.",
    watch="Lime is very bright, so use it for one block per post and never as text. Emerald on the mint base is for small labels only.",
    sw=[["Mint","#E6F6EE","Light base"],["Cloud White","#FFFFFF","Cards"],["Forest","#0E2A22","Dark base and text"],["Signal Orange","#FF8F1F","Signature"],
        ["Emerald","#0B7A50","Accent 1 on light"],["Mint Bright","#3DDC97","Accent 1 on dark"],["Lime","#C9F27A","Accent 2"],["Sage","#4B6B5F","Secondary text"]],
    light=variant(bg="#E6F6EE",bg2="#FFFFFF",line="#BFE3D0",fg="#0E2A22",muted="#4B6B5F",hl_fg="#0E2A22",hl_bg="#FF8F1F",o0="#FF8F1F",o1="#0B7A50",url="#0B7A50",
                  c0="#FF8F1F",c1="#0B7A50",c2="#0E2A22",btn_bg="#FF8F1F",btn_fg="#0E2A22",wave="#CDEBDD",stroke="#0E2A22",tag_fg="#0B7A50",disc="#C9F27A",panel="#FFFFFF",
                  bar=bar("#FF8F1F","#0B7A50","#C9F27A")),
    dark=variant(bg="#0E2A22",bg2="#153A30",line="#24584A",fg="#FFFFFF",muted="#A9CDBE",hl_fg="#FF8F1F",o0="#FF8F1F",c0="#FF8F1F",c1="#3DDC97",c2="#C9F27A",
                 btn_bg="#FF8F1F",btn_fg="#0E2A22",wave="#14362D",tag_fg="#3DDC97",disc="#3DDC97",bar=bar("#FF8F1F","#3DDC97","#C9F27A")),
    accent=variant(bg="#C9F27A",bg2="#0E2A22",line="#0E2A22",fg="#0E2A22",muted="#2F4F42",card_fg="#FFFFFF",card_muted="#A9CDBE",hl_fg="#C9F27A",hl_bg="#0E2A22",
                   o0="#0E2A22",o1="#0E2A22",c0="#FF8F1F",c1="#3DDC97",c2="#C9F27A",btn_bg="#0E2A22",btn_fg="#C9F27A",logo="#0E2A22",mark="#0E2A22",wave="#B4E05F",
                   stroke="#0E2A22",tag_bg="#0E2A22",tag_fg="#C9F27A",disc="#FF8F1F",panel="#0E2A22",bar=bar("#0E2A22","#FF8F1F","#FFFFFF")),
    dk="#0E2A22",
    tiles=[("#E6F6EE","#0E2A22","#0B7A50"),("#FFFFFF","#0E2A22","#0B7A50"),("#FF8F1F","#0E2A22","#0E2A22"),("#0E2A22","#FFFFFF","#3DDC97"),("#C9F27A","#0E2A22","#0E2A22")],
))

# J  Lavender & Marigold
P.append(dict(
    id="j", name="Lavender &amp; Marigold", short="Lavender + indigo + orange",
    mood="A soft lavender base with deep indigo for the dark posts. Violet and marigold sit beside the orange for a playful, creative feel.",
    best="Creative and design posts, workshop sign-ups and team intros.",
    watch="Violet and orange are both strong. Keep violet for labels and the accent post, and let orange be the highlight.",
    sw=[["Lavender","#EFEAFF","Light base"],["Cloud White","#FFFFFF","Cards"],["Indigo","#1F1747","Dark base and text"],["Signal Orange","#FF8F1F","Signature"],
        ["Violet","#6B4EE6","Accent 1"],["Marigold","#FFC857","Accent 2"],["Lilac","#A794FF","Violet on dark"],["Dusk","#5E5688","Secondary text"]],
    light=variant(bg="#EFEAFF",bg2="#FFFFFF",line="#D6CCF7",fg="#1F1747",muted="#5E5688",hl_fg="#1F1747",hl_bg="#FF8F1F",o0="#FF8F1F",o1="#6B4EE6",url="#6B4EE6",
                  c0="#FF8F1F",c1="#6B4EE6",c2="#1F1747",btn_bg="#FF8F1F",btn_fg="#1F1747",wave="#DDD4FA",stroke="#1F1747",tag_fg="#6B4EE6",disc="#FFC857",panel="#FFFFFF",
                  bar=bar("#FF8F1F","#6B4EE6","#FFC857")),
    dark=variant(bg="#1F1747",bg2="#2C2260",line="#453A8A",fg="#FFFFFF",muted="#C7BFEF",hl_fg="#FF8F1F",o0="#FF8F1F",c0="#FF8F1F",c1="#A794FF",c2="#FFC857",
                 btn_bg="#FF8F1F",btn_fg="#1F1747",wave="#2A2160",tag_fg="#A794FF",disc="#7B61FF",bar=bar("#FF8F1F","#A794FF","#FFC857")),
    accent=variant(bg="#6B4EE6",bg2="#FFFFFF",line="#FFFFFF",fg="#FFFFFF",muted="#E3DDFF",card_fg="#1F1747",card_muted="#5E5688",hl_fg="#1F1747",hl_bg="#FFC857",
                   o0="#FFC857",o1="#FFC857",url="#FFFFFF",c0="#FF8F1F",c1="#6B4EE6",c2="#1F1747",btn_bg="#FF8F1F",btn_fg="#1F1747",logo="#FFFFFF",mark="#FFC857",
                   wave="#7C62F0",stroke="#FFFFFF",tag_bg="#1F1747",tag_fg="#FFC857",disc="#FFC857",panel="#FFFFFF",bar=bar("#1F1747","#FFC857","#FF8F1F")),
    dk="#1F1747",
    tiles=[("#EFEAFF","#1F1747","#6B4EE6"),("#FFFFFF","#1F1747","#6B4EE6"),("#FF8F1F","#1F1747","#1F1747"),("#1F1747","#FFFFFF","#FFC857"),("#6B4EE6","#FFFFFF","#FFC857")],
))

# K  Clay & Olive
P.append(dict(
    id="k", name="Clay &amp; Olive", short="Stone + espresso + terracotta",
    mood="Earthy and calm: a warm stone base, espresso for the dark posts, terracotta as the signature and olive for detail. It looks premium and different from most tech pages.",
    best="Interviews, quotes, partner posts and longer posts.",
    watch="Terracotta is a deeper orange and moves the brand slightly toward red, so check it next to your current logo before committing. White text on terracotta works for big words only.",
    sw=[["Stone","#F3ECE2","Light base"],["Linen","#FFFBF5","Cards"],["Espresso","#2B211C","Dark base and text"],["Terracotta","#E2602C","Signature"],
        ["Olive","#5F6B2F","Accent 1"],["Sand","#E9C79F","Accent 2"],["Light Terracotta","#F2763F","Terracotta on dark"],["Clay Grey","#7B6A5F","Secondary text"]],
    light=variant(bg="#F3ECE2",bg2="#FFFBF5",line="#E3D7C6",fg="#2B211C",muted="#7B6A5F",hl_fg="#FFFFFF",hl_bg="#E2602C",o0="#E2602C",o1="#5F6B2F",url="#B8431A",
                  c0="#E2602C",c1="#5F6B2F",c2="#2B211C",btn_bg="#E2602C",btn_fg="#FFFFFF",wave="#E8DCCB",stroke="#2B211C",tag_fg="#5F6B2F",disc="#E9C79F",panel="#FFFBF5",
                  bar=bar("#E2602C","#5F6B2F","#E9C79F")),
    dark=variant(bg="#2B211C",bg2="#3A2E27",line="#5A483D",fg="#FFF6EA",muted="#CDBBA9",hl_fg="#F2763F",o0="#F2763F",c0="#F2763F",c1="#A9B66B",c2="#E9C79F",
                 btn_bg="#E2602C",btn_fg="#FFFFFF",wave="#3A2E27",tag_fg="#A9B66B",disc="#5F6B2F",bar=bar("#F2763F","#A9B66B","#E9C79F")),
    accent=variant(bg="#5F6B2F",bg2="#FFFBF5",line="#FFF6EA",fg="#FFF6EA",muted="#E4E0C4",card_fg="#2B211C",card_muted="#7B6A5F",hl_fg="#2B211C",hl_bg="#E9C79F",
                   o0="#E9C79F",o1="#E9C79F",url="#FFF6EA",c0="#E2602C",c1="#5F6B2F",c2="#2B211C",btn_bg="#E2602C",btn_fg="#FFFFFF",logo="#FFF6EA",mark="#E9C79F",
                   wave="#6E7A3C",stroke="#FFF6EA",tag_bg="#2B211C",tag_fg="#E9C79F",disc="#E9C79F",panel="#FFFBF5",bar=bar("#2B211C","#E9C79F","#E2602C")),
    dk="#2B211C",
    tiles=[("#F3ECE2","#2B211C","#B8431A"),("#FFFBF5","#2B211C","#5F6B2F"),("#E2602C","#FFFFFF","#FFFFFF"),("#2B211C","#FFF6EA","#F2763F"),("#5F6B2F","#FFF6EA","#E9C79F")],
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
palette_css = "\n".join(css) + "\n\n"

out = src
def must_sub(pattern, repl, text, flags=re.S, count=1):
    new, n = re.subn(pattern, lambda m: repl, text, count=count, flags=flags)
    assert n == count, (pattern, n)
    return new

# palette CSS region
a = out.index(".pal-a{--bg:#0E0B14")
b = out.index("/* ===== sample posts (sizes in cqw")
out = out[:a] + palette_css + out[b:]

# url color token
assert ".url{font:700 4.4cqw/1 var(--font-d);color:var(--o0);" in out
out = out.replace(".url{font:700 4.4cqw/1 var(--font-d);color:var(--o0);", ".url{font:700 4.4cqw/1 var(--font-d);color:var(--url,var(--o0));")

# tile kinds from tokens
tile_css = "\n".join(
    ".k%d{background:var(--k%db);color:var(--k%df)} .k%d .k{color:var(--k%dk)}" % (i, i, i, i, i) for i in range(5))
out = must_sub(r"\.k0\{background:var\(--bg\);color:var\(--fg\)\}.*?\.k4\{background:var\(--c2\);color:var\(--on2\)\}", tile_css, out)

# drop option-E rule, add dark covers
assert ".pal-e .ps .cta2{background:#FF8F1F;color:#0D0D0D}\n" in out
out = out.replace(".pal-e .ps .cta2{background:#FF8F1F;color:#0D0D0D}\n", "")
assert ".cv-note{font-size:12.5px;" in out
out = out.replace(".cv-note{font-size:12.5px;", ".cv .ring.dk{background:var(--dk)}\n.cv-note{font-size:12.5px;")

# filter no longer needed
out = must_sub(r"\n\s*<filter id=\"gm-duo\".*?</filter>", "", out)

# JS: compare block, palettes, tiles, letters, covers
out = must_sub(r"  var CMP = .*?</p></div>';\n", "", out)
pal_js = []
variants = ["v-l", "v-l", "v-d", "v-l", "v-a", "v-d"]
for p in P:
    pal_js.append(json.dumps(dict(id=p["id"], cls="pal-" + p["id"], name=p["name"], mode="Light first", short=p["short"],
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
out = out.replace("var letters = 'ABCDEF';", "var letters = 'GHIJK';")
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

# page text
out = out.replace("<title>AI Baithak Palettes</title>", "<title>AI Baithak Light Palettes</title>")
header = """<header>
    <p class="eyebrow">AI Baithak · Instagram color options · second board</p>
    <h1>Five lighter color options</h1>
    <p class="lede">Each option is <b>light first</b>. Most posts sit on a light base, with a dark variation for emphasis and one bold accent post. Orange stays the signature, except in K, where terracotta takes its place. The lettering continues from <a href="https://claude.ai/artifact/BmNWnGyrjbfA25xWZbKZJw" target="_blank" rel="noopener">the first board</a> (A to F), so these are G to K.</p>
    <p class="lede">Each option shows six sample posts (three of them with people and the robot from your workshop post), story highlight covers and a nine-post feed. Click any color to copy its hex code.</p>
  </header>"""
out = must_sub(r"<header>.*?</header>", header, out)
guide = """<section class="opt" id="guide-sec">
    <h2 class="sec" style="margin-top:0">How the light and dark variations work</h2>
    <div class="guide">
      <div><h3>Light is the home base</h3><p>Most posts use the light base, so the profile feels bright. The dark variation is for strong moments like events, quotes and announcements.</p></div>
      <div><h3>Accent base now and then</h3><p>Use the bold accent base for about one post in six, for spotlights and big calls to action.</p></div>
      <div><h3>The signature color is a highlight block</h3><p>On light backgrounds, orange text is hard to read. The signature color goes on highlight blocks, buttons and shapes, with dark text on top.</p></div>
      <div><h3>Mix the grid</h3><p>Aim for light, dark and accent in every row of three. The feed preview in each option shows the pattern.</p></div>
    </div>

    <div class="pick">
      <h3>My pick</h3>
      <p>Use <b>G · Sky &amp; Sun</b> as the main look. Orange and blue are opposites, so your signature stands out. Navy replaces black for the dark posts, and the blue reads as clear and trustworthy, which suits an AI community.</p>
      <p>For a warmer, community feel choose <b>H · Blush &amp; Berry</b>. For something different from most tech pages choose <b>K · Clay &amp; Olive</b>, but check the terracotta next to your logo first.</p>
      <p>This is a recommendation. The final choice is the team's.</p>
    </div>

    <p class="foot-note">The logo and partner names in these mockups are redrawn placeholders for layout only. Real artwork replaces them in the final templates. Post text is taken from your existing posts. The people and the robot are cut out of screenshots of your own posts, so they look soft here. Original photos will look sharper, and each needs its own cut-out with a transparent background.</p>
  </section>"""
out = must_sub(r'<section class="opt" id="guide-sec">.*?</section>', guide, out)

open(D + "ai-baithak-light.html", "w", encoding="utf-8").write(out)

# ---------------------------------------------------------------- build with images
css_ph = open(D + "cut/ph.css", encoding="utf-8").read()
assert "/*__PH_CSS__*/" in out
built = out.replace("/*__PH_CSS__*/", css_ph)
open(D + "ai-baithak-light-built.html", "w", encoding="utf-8").write(built)
i = built.index('<svg width="0"')
pre = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
open(D + "ai-baithak-light-preview.html", "w", encoding="utf-8").write(pre + built[:i] + "</head><body>" + built[i:] + "</body></html>")
print("ok", len(built))
