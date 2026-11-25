import json, re, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
# Base: the calm board source, which already carries the full page (posts, people posts, story covers, feed, overview).
src = open(D + "ai-baithak-calm.html", encoding="utf-8").read()


def bar(a, b, c):
    return "linear-gradient(90deg,%s 0 55%%,%s 55%% 78%%,%s 78%% 100%%)" % (a, b, c)


def variant(**kw):
    d = dict(kw)
    d.setdefault("card_fg", d["fg"]); d.setdefault("card_muted", d["muted"])
    d.setdefault("o1", d["c1"]); d.setdefault("url", d["o0"])
    d.setdefault("hl_bg", "transparent"); d.setdefault("logo", d["fg"]); d.setdefault("mark", d["o0"])
    d.setdefault("stroke", d["o0"]); d.setdefault("tag_bg", "transparent"); d.setdefault("panel", d["bg2"])
    return d


KEYS = ["bg", "bg2", "line", "fg", "muted", "card_fg", "card_muted", "hl_fg", "hl_bg", "o0", "o1", "url", "c0", "c1", "c2",
        "btn_bg", "btn_fg", "logo", "mark", "wave", "stroke", "tag_bg", "tag_fg", "disc", "panel", "bar"]


def css_vars(d):
    return ";".join("--%s:%s" % (k.replace("_", "-"), d[k]) for k in KEYS)


def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [v / 12.92 if v <= .03928 else ((v + .055) / 1.055) ** 2.4 for v in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]


def cr(a, b):
    x, y = lum(a), lum(b)
    return (max(x, y) + .05) / (min(x, y) + .05)


SKIN = ["#F6D9C4", "#E5B48F", "#C98B5B", "#9A5E37", "#5E3B25"]


def extra(name, deep, paper, hero, ink, sup):
    def strip(bg, label, fg):
        dots = "".join('<span style="width:22px;height:22px;border-radius:50%%;background:%s;display:block"></span>' % s for s in SKIN)
        return ('<div style="background:%s;color:%s;padding:12px 10px;display:flex;flex-direction:column;align-items:center;gap:8px;min-width:0">'
                '<span style="display:flex;gap:5px">%s</span><span style="font:600 11px var(--font-d);letter-spacing:.06em">%s</span></div>') % (bg, fg, dots, label)
    pairs = [("Paper on Deep", paper, deep), ("Hero on Deep", hero, deep), ("Ink on Hero", ink, hero), ("Ink on Paper", ink, paper)]
    rows = ""
    for lab, f, b in pairs:
        r = cr(f, b)
        lvl = "AAA" if r >= 7 else "AA" if r >= 4.5 else "large text only" if r >= 3 else "decorative only"
        rows += ('<span style="display:inline-flex;align-items:center;gap:8px;margin:0 16px 6px 0"><span style="display:inline-block;width:34px;height:22px;border-radius:5px;background:%s;color:%s;font:700 12px/22px var(--font-d);text-align:center">Aa</span>'
                 '<span style="font-size:12.5px;color:var(--muted)">%s %.1f : 1 · %s</span></span>') % (b, f, lab, r, lvl)
    return ('<div style="margin:6px 0 22px"><h3 class="sub">Skin-tone and contrast check</h3>'
            '<div style="display:grid;grid-template-columns:repeat(3,1fr);border:1px solid var(--line);border-radius:10px;overflow:hidden;max-width:560px">%s%s%s</div>'
            '<p style="margin:10px 0 0">%s</p></div>') % (strip(deep, "ON DEEP", paper), strip(paper, "ON PAPER", ink), strip(hero, "ON ACCENT", ink), rows)


P = []

# Q  Petrol & Coral
P.append(dict(
    id="q", name="Petrol & Coral", short="Deep teal + coral + sand",
    mood="A deep petrol teal for the dark posts with a warm coral accent. Teal and coral sit opposite each other on the wheel, so faces in warm skin tones stand out against the dark panel. Sand keeps the light posts from going stark white.",
    best="Team posts, speakers and portraits. The coral keeps some warmth from your orange, and the teal gives photos a strong ground.",
    watch="Coral text on sand is weak. Use coral for blocks and shapes with dark text on top, and use petrol for text on the light base.",
    sw=[["Sand", "#F4EADB", "Light base"], ["Cream", "#FBF5EA", "Cards"], ["Petrol", "#0A3D44", "Dark base and labels"], ["Coral", "#FF6B5E", "Signature"],
        ["Seafoam", "#8ED6CB", "Accent 1"], ["Warm Sand", "#E2D2B8", "Accent 2"], ["Night", "#101C1E", "Text"], ["Teal Grey", "#5E6B69", "Secondary text"]],
    light=variant(bg="#F4EADB", bg2="#FBF5EA", line="#E3D5BF", fg="#101C1E", muted="#5E6B69", hl_fg="#101C1E", hl_bg="#FF6B5E", o0="#FF6B5E", o1="#0A3D44", url="#0A3D44",
                  c0="#FF6B5E", c1="#0A3D44", c2="#101C1E", btn_bg="#FF6B5E", btn_fg="#101C1E", wave="#EBDFCB", stroke="#101C1E", tag_fg="#0A3D44", disc="#8ED6CB", panel="#FBF5EA",
                  bar=bar("#FF6B5E", "#8ED6CB", "#0A3D44")),
    dark=variant(bg="#0A3D44", bg2="#11505A", line="#1E5E68", fg="#F4EADB", muted="#A9CBC8", hl_fg="#FF8579", o0="#FF6B5E", c0="#FF6B5E", c1="#8ED6CB", c2="#F4EADB",
                 btn_bg="#FF6B5E", btn_fg="#101C1E", wave="#0F4850", tag_fg="#8ED6CB", disc="#1E5E68", bar=bar("#FF6B5E", "#8ED6CB", "#F4EADB")),
    accent=variant(bg="#FF6B5E", bg2="#FBF5EA", line="#E85A4E", fg="#101C1E", muted="#3A1E1B", card_fg="#101C1E", card_muted="#5E6B69", hl_fg="#101C1E", hl_bg="#F4EADB",
                   o0="#101C1E", o1="#101C1E", url="#101C1E", c0="#F4EADB", c1="#0A3D44", c2="#101C1E", btn_bg="#0A3D44", btn_fg="#F4EADB", logo="#101C1E", mark="#101C1E",
                   wave="#FF8176", stroke="#101C1E", tag_bg="#0A3D44", tag_fg="#F4EADB", disc="#F4EADB", panel="#FBF5EA", bar=bar("#101C1E", "#F4EADB", "#0A3D44")),
    dk="#0A3D44", v=["v-l", "v-d", "v-a", "v-l", "v-d", "v-a"],
    tiles=[("#F4EADB", "#101C1E", "#0A3D44"), ("#8ED6CB", "#101C1E", "#0A3D44"), ("#FF6B5E", "#101C1E", "#101C1E"), ("#0A3D44", "#F4EADB", "#FF6B5E"), ("#E2D2B8", "#101C1E", "#0A3D44")],
    chk=("#0A3D44", "#F4EADB", "#FF6B5E", "#101C1E", "#8ED6CB"),
))

# R  Oxblood & Rose
P.append(dict(
    id="r", name="Oxblood & Rose", short="Wine red + hot rose + blush",
    mood="A dark wine base with a bright rose accent. Red-brown depth flatters medium and deep skin and feels more human than the usual tech blues. Raspberry gives a second step for shapes and charts.",
    best="Community, volunteer and people-led posts. Quotes and team spotlights look strong on the wine base.",
    watch="Rose and raspberry are close, so use one per post. Labels on the light base use the dark wine, not rose.",
    sw=[["Blush", "#FFECE6", "Light base"], ["Porcelain", "#FFF8F5", "Cards"], ["Oxblood", "#4A0F22", "Dark base and labels"], ["Rose", "#FF7FA8", "Signature"],
        ["Raspberry", "#C23A5B", "Accent 1"], ["Petal", "#F8CFD2", "Accent 2"], ["Wine Ink", "#220A12", "Text"], ["Mauve Grey", "#7A4A52", "Secondary text"]],
    light=variant(bg="#FFECE6", bg2="#FFF8F5", line="#F0D3CB", fg="#220A12", muted="#7A4A52", hl_fg="#220A12", hl_bg="#FF7FA8", o0="#FF7FA8", o1="#4A0F22", url="#4A0F22",
                  c0="#FF7FA8", c1="#C23A5B", c2="#4A0F22", btn_bg="#FF7FA8", btn_fg="#220A12", wave="#F8DDD6", stroke="#220A12", tag_fg="#4A0F22", disc="#F8CFD2", panel="#FFF8F5",
                  bar=bar("#FF7FA8", "#C23A5B", "#F8CFD2")),
    dark=variant(bg="#4A0F22", bg2="#5D1A31", line="#74293F", fg="#FFECE6", muted="#E3B5C0", hl_fg="#FF9BBB", o0="#FF7FA8", c0="#FF7FA8", c1="#F8CFD2", c2="#FFECE6",
                 btn_bg="#FF7FA8", btn_fg="#220A12", wave="#55162A", tag_fg="#F8CFD2", disc="#74293F", bar=bar("#FF7FA8", "#C23A5B", "#FFECE6")),
    accent=variant(bg="#FF7FA8", bg2="#FFF8F5", line="#EE6E97", fg="#220A12", muted="#4A0F22", card_fg="#220A12", card_muted="#7A4A52", hl_fg="#220A12", hl_bg="#FFECE6",
                   o0="#220A12", o1="#220A12", url="#220A12", c0="#FFECE6", c1="#C23A5B", c2="#4A0F22", btn_bg="#4A0F22", btn_fg="#FFECE6", logo="#220A12", mark="#220A12",
                   wave="#FF93B6", stroke="#220A12", tag_bg="#4A0F22", tag_fg="#FFECE6", disc="#FFECE6", panel="#FFF8F5", bar=bar("#220A12", "#FFECE6", "#C23A5B")),
    dk="#4A0F22", v=["v-l", "v-l", "v-d", "v-a", "v-d", "v-l"],
    tiles=[("#FFECE6", "#220A12", "#4A0F22"), ("#F8CFD2", "#220A12", "#4A0F22"), ("#FF7FA8", "#220A12", "#220A12"), ("#4A0F22", "#FFECE6", "#FF7FA8"), ("#C23A5B", "#FFECE6", "#FFECE6")],
    chk=("#4A0F22", "#FFECE6", "#FF7FA8", "#220A12", "#C23A5B"),
))

# S  Ultramarine & Lime
P.append(dict(
    id="s", name="Ultramarine & Lime", short="Electric blue + acid lime + off-white",
    mood="The loudest option. A strong ultramarine ground with an acid lime accent, the kind of pairing that stops the scroll and reads as software. Warm skin glows against this blue.",
    best="Event announcements, workshops and registration posts, anything that needs to be noticed in the feed.",
    watch="Keep lime for pills, numbers and one highlight per post, never as a large area behind faces. On the light base the blue carries the text.",
    sw=[["Off-white", "#F3F2EC", "Light base"], ["White", "#FFFFFF", "Cards"], ["Ultramarine", "#2230D8", "Dark base and labels"], ["Lime", "#CFF53E", "Signature"],
        ["Periwinkle", "#8C96FF", "Accent 1"], ["Lavender Mist", "#DDE0FF", "Accent 2"], ["Midnight", "#0C0C2E", "Text"], ["Indigo Grey", "#55556E", "Secondary text"]],
    light=variant(bg="#F3F2EC", bg2="#FFFFFF", line="#DEDCD2", fg="#0C0C2E", muted="#55556E", hl_fg="#0C0C2E", hl_bg="#CFF53E", o0="#CFF53E", o1="#2230D8", url="#2230D8",
                  c0="#CFF53E", c1="#2230D8", c2="#0C0C2E", btn_bg="#CFF53E", btn_fg="#0C0C2E", wave="#E8E7DE", stroke="#0C0C2E", tag_fg="#2230D8", disc="#DDE0FF", panel="#FFFFFF",
                  bar=bar("#CFF53E", "#8C96FF", "#2230D8")),
    dark=variant(bg="#2230D8", bg2="#3341E6", line="#4A58EE", fg="#F3F2EC", muted="#C9CEFF", hl_fg="#CFF53E", o0="#CFF53E", c0="#CFF53E", c1="#8C96FF", c2="#F3F2EC",
                 btn_bg="#CFF53E", btn_fg="#0C0C2E", wave="#2B39E0", tag_fg="#CFF53E", disc="#4A58EE", bar=bar("#CFF53E", "#8C96FF", "#F3F2EC")),
    accent=variant(bg="#CFF53E", bg2="#FFFFFF", line="#BDE22F", fg="#0C0C2E", muted="#1E2146", card_fg="#0C0C2E", card_muted="#55556E", hl_fg="#CFF53E", hl_bg="#2230D8",
                   o0="#0C0C2E", o1="#0C0C2E", url="#2230D8", c0="#2230D8", c1="#8C96FF", c2="#0C0C2E", btn_bg="#2230D8", btn_fg="#F3F2EC", logo="#0C0C2E", mark="#0C0C2E",
                   wave="#D9FA6A", stroke="#0C0C2E", tag_bg="#2230D8", tag_fg="#F3F2EC", disc="#F3F2EC", panel="#FFFFFF", bar=bar("#0C0C2E", "#2230D8", "#8C96FF")),
    dk="#2230D8", v=["v-l", "v-d", "v-a", "v-d", "v-l", "v-d"],
    tiles=[("#F3F2EC", "#0C0C2E", "#2230D8"), ("#DDE0FF", "#0C0C2E", "#2230D8"), ("#CFF53E", "#0C0C2E", "#0C0C2E"), ("#2230D8", "#F3F2EC", "#CFF53E"), ("#8C96FF", "#0C0C2E", "#0C0C2E")],
    chk=("#2230D8", "#F3F2EC", "#CFF53E", "#0C0C2E", "#8C96FF"),
))

# T  Bottle & Peach
P.append(dict(
    id="t", name="Bottle & Peach", short="Deep green + peach + jade",
    mood="A dark bottle green with a soft, warm peach accent that echoes skin, so portraits and graphics feel related. The green is kept deep so it does not tint faces. Jade supports charts and icons.",
    best="Learning posts, workshops, recaps and anything about growth. Peach on green looks warm and approachable.",
    watch="Green is a risk behind faces if it is bright or grey. Keep photos on the deep bottle green, the peach, or the cream, never on jade.",
    sw=[["Ivory", "#FBF1E3", "Light base"], ["Cream", "#FFF9F0", "Cards"], ["Bottle", "#0F3A2D", "Dark base and labels"], ["Peach", "#FFAE94", "Signature"],
        ["Jade", "#3FAE86", "Accent 1"], ["Sand", "#EBDCC6", "Accent 2"], ["Forest Ink", "#0B1D16", "Text"], ["Moss Grey", "#5A6A60", "Secondary text"]],
    light=variant(bg="#FBF1E3", bg2="#FFF9F0", line="#EBDCC6", fg="#0B1D16", muted="#5A6A60", hl_fg="#0B1D16", hl_bg="#FFAE94", o0="#FFAE94", o1="#0F3A2D", url="#0F3A2D",
                  c0="#FFAE94", c1="#0F3A2D", c2="#3FAE86", btn_bg="#FFAE94", btn_fg="#0B1D16", wave="#F1E4CE", stroke="#0B1D16", tag_fg="#0F3A2D", disc="#EBDCC6", panel="#FFF9F0",
                  bar=bar("#FFAE94", "#3FAE86", "#0F3A2D")),
    dark=variant(bg="#0F3A2D", bg2="#184A3A", line="#27604C", fg="#FBF1E3", muted="#B5D1C4", hl_fg="#FFAE94", o0="#FFAE94", c0="#FFAE94", c1="#3FAE86", c2="#FBF1E3",
                 btn_bg="#FFAE94", btn_fg="#0B1D16", wave="#144233", tag_fg="#7FD0AE", disc="#27604C", bar=bar("#FFAE94", "#3FAE86", "#FBF1E3")),
    accent=variant(bg="#FFAE94", bg2="#FFF9F0", line="#F09A80", fg="#0B1D16", muted="#3B2218", card_fg="#0B1D16", card_muted="#5A6A60", hl_fg="#0B1D16", hl_bg="#FBF1E3",
                   o0="#0B1D16", o1="#0B1D16", url="#0F3A2D", c0="#FBF1E3", c1="#0F3A2D", c2="#0B1D16", btn_bg="#0F3A2D", btn_fg="#FBF1E3", logo="#0B1D16", mark="#0B1D16",
                   wave="#FFBEA8", stroke="#0B1D16", tag_bg="#0F3A2D", tag_fg="#FBF1E3", disc="#FBF1E3", panel="#FFF9F0", bar=bar("#0B1D16", "#FBF1E3", "#3FAE86")),
    dk="#0F3A2D", v=["v-l", "v-d", "v-l", "v-d", "v-a", "v-l"],
    tiles=[("#FBF1E3", "#0B1D16", "#0F3A2D"), ("#EBDCC6", "#0B1D16", "#0F3A2D"), ("#FFAE94", "#0B1D16", "#0B1D16"), ("#0F3A2D", "#FBF1E3", "#FFAE94"), ("#3FAE86", "#0B1D16", "#0B1D16")],
    chk=("#0F3A2D", "#FBF1E3", "#FFAE94", "#0B1D16", "#3FAE86"),
))

# U  Graphite & Neon
P.append(dict(
    id="u", name="Graphite & Neon", short="Charcoal blue + cyan + hot pink",
    mood="The most technical look. A cool graphite base, a bright cyan accent and a hot pink spark, like light on a dark screen. A neutral dark ground is the safest for every skin tone.",
    best="AI and tech content: tool demos, workshops, announcements and speaker posts.",
    watch="Pink is a spark, not a base. Use it once per post. Cyan on the light base is too weak for text, so labels use graphite.",
    sw=[["Ice", "#EEF5F8", "Light base"], ["White", "#FFFFFF", "Cards"], ["Graphite", "#1B2027", "Dark base and labels"], ["Cyan", "#3CC6F2", "Signature"],
        ["Hot Pink", "#F2488E", "Accent 1"], ["Frost", "#C9D8E0", "Accent 2"], ["Carbon", "#0F1318", "Text"], ["Steel", "#566570", "Secondary text"]],
    light=variant(bg="#EEF5F8", bg2="#FFFFFF", line="#D5E1E7", fg="#0F1318", muted="#566570", hl_fg="#0F1318", hl_bg="#3CC6F2", o0="#3CC6F2", o1="#1B2027", url="#1B2027",
                  c0="#3CC6F2", c1="#F2488E", c2="#1B2027", btn_bg="#3CC6F2", btn_fg="#0F1318", wave="#E1EBF0", stroke="#0F1318", tag_fg="#1B2027", disc="#C9D8E0", panel="#FFFFFF",
                  bar=bar("#3CC6F2", "#F2488E", "#1B2027")),
    dark=variant(bg="#1B2027", bg2="#262D36", line="#38424D", fg="#EEF5F8", muted="#A9B6C0", hl_fg="#3CC6F2", o0="#3CC6F2", c0="#3CC6F2", c1="#F2488E", c2="#EEF5F8",
                 btn_bg="#3CC6F2", btn_fg="#0F1318", wave="#222830", tag_fg="#3CC6F2", disc="#38424D", bar=bar("#3CC6F2", "#F2488E", "#EEF5F8")),
    accent=variant(bg="#3CC6F2", bg2="#FFFFFF", line="#2BB3E0", fg="#0F1318", muted="#12303C", card_fg="#0F1318", card_muted="#566570", hl_fg="#0F1318", hl_bg="#EEF5F8",
                   o0="#0F1318", o1="#0F1318", url="#0F1318", c0="#F2488E", c1="#1B2027", c2="#0F1318", btn_bg="#1B2027", btn_fg="#EEF5F8", logo="#0F1318", mark="#0F1318",
                   wave="#5CD0F5", stroke="#0F1318", tag_bg="#1B2027", tag_fg="#EEF5F8", disc="#EEF5F8", panel="#FFFFFF", bar=bar("#0F1318", "#EEF5F8", "#F2488E")),
    dk="#1B2027", v=["v-d", "v-l", "v-a", "v-l", "v-d", "v-l"],
    tiles=[("#EEF5F8", "#0F1318", "#1B2027"), ("#F2488E", "#0F1318", "#0F1318"), ("#3CC6F2", "#0F1318", "#0F1318"), ("#1B2027", "#EEF5F8", "#3CC6F2"), ("#C9D8E0", "#0F1318", "#1B2027")],
    chk=("#1B2027", "#EEF5F8", "#3CC6F2", "#0F1318", "#F2488E"),
))

# V  Poppy & Cobalt
P.append(dict(
    id="v", name="Poppy & Cobalt", short="Cobalt + poppy red + warm paper",
    mood="A primary-color print look: cobalt, poppy red and warm paper with black ink. Flat shapes and heavy type, closer to a poster than a gradient. It feels like a community, not a startup.",
    best="Community posts, campaigns, partner posts and posters. Works well with big, cut-out photos.",
    watch="Red on cobalt vibrates, so keep them apart. Put poppy on paper or black, and cobalt on paper. Text on poppy stays black.",
    sw=[["Paper", "#F1ECE0", "Light base"], ["Warm White", "#FAF7F0", "Cards"], ["Cobalt", "#1A3FC4", "Dark base and labels"], ["Poppy", "#E8402D", "Signature"],
        ["Sky", "#9DB8FF", "Accent 1"], ["Sand", "#DDD5C3", "Accent 2"], ["Black", "#15151B", "Text"], ["Stone", "#5C5A55", "Secondary text"]],
    light=variant(bg="#F1ECE0", bg2="#FAF7F0", line="#DDD5C3", fg="#15151B", muted="#5C5A55", hl_fg="#15151B", hl_bg="#E8402D", o0="#E8402D", o1="#1A3FC4", url="#1A3FC4",
                  c0="#E8402D", c1="#1A3FC4", c2="#15151B", btn_bg="#E8402D", btn_fg="#15151B", wave="#E7E0D1", stroke="#15151B", tag_fg="#1A3FC4", disc="#9DB8FF", panel="#FAF7F0",
                  bar=bar("#E8402D", "#1A3FC4", "#9DB8FF")),
    dark=variant(bg="#1A3FC4", bg2="#2A4FD6", line="#4766E0", fg="#F1ECE0", muted="#C6D3FF", hl_fg="#15151B", hl_bg="#E8402D", o0="#9DB8FF", c0="#E8402D", c1="#9DB8FF", c2="#F1ECE0",
                 btn_bg="#E8402D", btn_fg="#15151B", wave="#2447CF", tag_fg="#9DB8FF", disc="#4766E0", bar=bar("#E8402D", "#9DB8FF", "#F1ECE0")),
    accent=variant(bg="#E8402D", bg2="#FAF7F0", line="#D4331F", fg="#15151B", muted="#3A0F0A", card_fg="#15151B", card_muted="#5C5A55", hl_fg="#15151B", hl_bg="#F1ECE0",
                   o0="#15151B", o1="#15151B", url="#15151B", c0="#F1ECE0", c1="#1A3FC4", c2="#15151B", btn_bg="#15151B", btn_fg="#F1ECE0", logo="#15151B", mark="#15151B",
                   wave="#EE5A48", stroke="#15151B", tag_bg="#15151B", tag_fg="#F1ECE0", disc="#F1ECE0", panel="#FAF7F0", bar=bar("#15151B", "#F1ECE0", "#1A3FC4")),
    dk="#1A3FC4", v=["v-l", "v-d", "v-a", "v-d", "v-l", "v-a"],
    tiles=[("#F1ECE0", "#15151B", "#1A3FC4"), ("#9DB8FF", "#15151B", "#1A3FC4"), ("#E8402D", "#15151B", "#15151B"), ("#1A3FC4", "#F1ECE0", "#9DB8FF"), ("#15151B", "#F1ECE0", "#E8402D")],
    chk=("#1A3FC4", "#F1ECE0", "#E8402D", "#15151B", "#9DB8FF"),
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
css.append("/* bold board: photos keep their full color */")
palette_css = "\n".join(css) + "\n\n"

out = src
a = out.index(".pal-l{--bg:")
b = out.index("/* ===== sample posts (sizes in cqw")
out = out[:a] + palette_css + out[b:]


def must_sub(pattern, repl, text, flags=re.S):
    new, n = re.subn(pattern, lambda m: repl, text, count=1, flags=flags)
    assert n == 1, pattern
    return new


pal_js = []
for p in P:
    pal_js.append(json.dumps(dict(id=p["id"], cls="pal-" + p["id"], name=p["name"], mode="Bold", short=p["short"], mood=p["mood"], best=p["best"], watch=p["watch"],
                                  sw=p["sw"], v=p["v"], extra=extra(p["name"], *p["chk"][:4], p["chk"][4])), ensure_ascii=False))
out = must_sub(r"  var PAL = \[.*?\n  \];\n", "  var PAL = [\n    " + ",\n    ".join(pal_js) + "\n  ];\n", out)
assert "var letters = 'LMNOP';" in out
out = out.replace("var letters = 'LMNOP';", "var letters = 'QRSTUV';")
out = out.replace("<title>AI Baithak Calm Palettes</title>", "<title>AI Baithak Bold Palettes</title>")

header = """<header>
    <p class="eyebrow">AI Baithak · Instagram color options · bold and saturated</p>
    <h1>Six bold color options</h1>
    <p class="lede">A third direction, built to look nothing like the first two: <a href="https://claude.ai/artifact/BmNWnGyrjbfA25xWZbKZJw" target="_blank" rel="noopener">A to F</a> were black and orange with mustard, and <a href="https://claude.ai/artifact/TCf88i1k3Hf24eXUPfYTpE" target="_blank" rel="noopener">L to P</a> were soft pastels and greys. These are <b>deep, saturated colors with one loud accent</b>, picked so real photos of people look good on them. The lettering continues, so these are Q to V.</p>
    <p class="lede">Each option shows six sample posts (three with people and the robot from your workshop post), story highlight covers and a nine-post feed, plus a skin-tone and contrast check. Photos keep their full color. Click any color to copy its hex code.</p>
  </header>"""
out = must_sub(r"<header>.*?</header>", header, out)

guide = """<section class="opt" id="guide-sec">
    <h2 class="sec" style="margin-top:0">How the research shaped these</h2>
    <div class="guide">
      <div><h3>Deep, not pale</h3><p>Each option has one rich dark base (petrol, oxblood, ultramarine, bottle green, graphite, cobalt). Photos sit on a strong ground, and the colors are not lightened versions of the earlier sets.</p></div>
      <div><h3>Built around skin</h3><p>Neutral and deep backgrounds, and navy and earth tones, are the ones photographers name as the safest across skin tones. Greens are kept deep so they do not tint faces. The strips under each palette show five skin tones on its grounds.</p></div>
      <div><h3>One loud accent</h3><p>2026 trend writing favors saturated color with a single strong accent on a stable core. Each option keeps that accent for pills, numbers and one highlight per post.</p></div>
      <div><h3>Contrast is checked</h3><p>Every option lists the contrast ratios for its main text pairs. Where a pair is weak, the notes say which color to use for text instead.</p></div>
    </div>

    <div class="pick">
      <h3>My pick</h3>
      <p>Use <b>Q · Petrol &amp; Coral</b> as the main look. Coral keeps some warmth from your orange, petrol is a skin-friendly deep ground, and it works for people, events and graphics.</p>
      <p>For event hype and registration posts, add <b>S · Ultramarine &amp; Lime</b>. For AI and tool content, <b>U · Graphite &amp; Neon</b> has the most technical feel.</p>
      <p>This is a recommendation. The final choice is the team's.</p>
    </div>

    <p class="foot-note">Sources: <a href="https://learn.zoner.com/how-background-color-affects-complexion-our-10-shade-test/" target="_blank" rel="noopener">Zoner</a>, <a href="https://kellytareskiphotography.com/how-to-choose-background-colors-to-complement-skin-tones/" target="_blank" rel="noopener">Kelly Tareski Photography</a>, <a href="https://savageuniversal.com/us-en/blog/how-to-choose-right-gray-background/" target="_blank" rel="noopener">Savage Universal</a>, <a href="https://learn.g2.com/graphic-design-trends" target="_blank" rel="noopener">G2</a>, <a href="https://www.adobe.com/express/learn/blog/what-trending-color-palettes-mean" target="_blank" rel="noopener">Adobe Express</a>. Most skin-tone guidance was tested on lighter skin, so the checks here include deeper tones. The logo and partner names in these mockups are redrawn placeholders for layout only. Post text is taken from your existing posts. The people and the robot are cut out of screenshots of your own posts, so they look soft here. Original photos will look sharper.</p>
  </section>"""
out = must_sub(r'<section class="opt" id="guide-sec">.*?</section>', guide, out)

open(D + "ai-baithak-bold.html", "w", encoding="utf-8").write(out)
css_ph = open(D + "cut/ph.css", encoding="utf-8").read()
assert "/*__PH_CSS__*/" in out
built = out.replace("/*__PH_CSS__*/", css_ph)
open(D + "ai-baithak-bold-built.html", "w", encoding="utf-8").write(built)
print("ok", len(built))
