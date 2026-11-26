import json, re, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
# Base: the A-F board, so C, D and F render exactly as published. L is taken from the calm board.
src = open(D + "ai-baithak-palettes.html", encoding="utf-8").read()
calm = open(D + "ai-baithak-calm.html", encoding="utf-8").read()
out = src


def must_sub(pattern, repl, text, flags=re.S):
    new, n = re.subn(pattern, lambda m: repl, text, count=1, flags=flags)
    assert n == 1, pattern
    return new


# ---- L styles from the calm board (palette tokens, dark and accent variants, tile colors)
l_css = [ln for ln in calm.split("\n") if ln.startswith(".pal-l")]
assert len(l_css) == 3, len(l_css)
extra_css = "\n".join(l_css) + """
/* L only: softened photos, dark-filled story covers, calm feed tiles */
.pal-l .ph,.pal-l .tph{filter:saturate(.6)}
.cv .ring.dk{background:var(--dk)}
.q0{background:var(--k0b);color:var(--k0f)} .q0 .k{color:var(--k0k)}
.q1{background:var(--k1b);color:var(--k1f)} .q1 .k{color:var(--k1k)}
.q2{background:var(--k2b);color:var(--k2f)} .q2 .k{color:var(--k2k)}
.q3{background:var(--k3b);color:var(--k3f)} .q3 .k{color:var(--k3k)}
.q4{background:var(--k4b);color:var(--k4f)} .q4 .k{color:var(--k4k)}
"""
marker = "/* ===== sample posts (sizes in cqw"
out = out.replace(marker, extra_css + "\n" + marker, 1)

# L uses --url for the link color on its posts; other palettes fall back to --o0
old = ".url{font:700 4.4cqw/1 var(--font-d);color:var(--o0);"
assert old in out
out = out.replace(old, ".url{font:700 4.4cqw/1 var(--font-d);color:var(--url,var(--o0));")

# ---- L entry from the calm board
m = re.search(r'    (\{"id": "l".*?\}),?\n', calm)
assert m
l_entry = m.group(1)

# ---- keep C, D, F in the original order, then L
out = must_sub(r"  var TILES = \[", """  PAL = PAL.filter(function(p){ return ['c','d','f'].indexOf(p.id) > -1; });
  PAL.push(%s);
  var LTILES = [
    ['Team','Meet the Leadership Council','q0'],
    ['Event','21 Nov Mega Project Day','q2'],
    ['Workshop','Build your first AI agent','q3','robot'],
    ['Join us','We are extending our core teams','q1'],
    ['Spotlight','Meet our team lead','q4','maryam'],
    ['Quote','Learning grows when people come together','q0'],
    ['Teamwork','Different skills, same goal','q3','duo'],
    ['Partners','Our outreach partner','q1'],
    ['Register','Join the next session','q2']
  ];
  var TILES = [""" % l_entry, out)

out = out.replace("  function feed(){ return TILES.map(tile).join(''); }",
                  "  function feed(p){ return (p && p.id === 'l' ? LTILES : TILES).map(tile).join(''); }")
old_cov = """  function covers(){
    return COVERS.map(function(c,i){
      return '<div class="cv"><div class="ring" style="--rc:var(--c'+(i%3)+')">'+icon(c[0])+'</div><span>'+c[1]+'</span></div>';
    }).join('');
  }"""
new_cov = """  function covers(p){
    return COVERS.map(function(c,i){
      var dark = p && p.id === 'l' && i % 2 === 1;
      var rc = 'var(--' + (dark ? 'dc' : 'c') + (i%3) + ')';
      return '<div class="cv"><div class="ring'+(dark?' dk':'')+'" style="--rc:'+rc+'">'+icon(c[0])+'</div><span>'+c[1]+'</span></div>';
    }).join('');
  }"""
assert old_cov in out
out = out.replace(old_cov, new_cov)
assert "'+feed()+'" in out and "'+covers()+'" in out
out = out.replace("'+feed()+'", "'+feed(p)+'").replace("'+covers()+'", "'+covers(p)+'")

old_note = "Ring color follows the topic: orange for events, accent 1 for team, accent 2 for learning. Keep the same rule on every cover.</p>"
assert old_note in out
out = out.replace(old_note, "'+(p.id === 'l' ? 'Covers alternate between light and dark fills. Ring color follows the topic, and the same topic always keeps the same ring color.' : 'Ring color follows the topic: orange for events, accent 1 for team, accent 2 for learning. Keep the same rule on every cover.')+'</p>")
assert "var letters = 'ABCDEF';" in out
out = out.replace("var L = letters[i];", "var L = p.id.toUpperCase();")

# ---- header, guide, title
out = out.replace("<title>AI Baithak Palettes</title>", "<title>AI Baithak Shortlist C D F L</title>")
header = """<header>
    <p class="eyebrow">AI Baithak · Instagram color options · shortlist</p>
    <h1>Four color options: C, D, F and L</h1>
    <p class="lede">The four picks from the earlier boards, together in one place and unchanged. <b>C · Sunset Burn</b>, <b>D · Cream Studio</b> and <b>F · Mustard &amp; Cream</b> come from <a href="https://claude.ai/artifact/BmNWnGyrjbfA25xWZbKZJw" target="_blank" rel="noopener">the first board</a> (A to F). <b>L · Warm Neutral</b> comes from <a href="https://claude.ai/artifact/TCf88i1k3Hf24eXUPfYTpE" target="_blank" rel="noopener">the calm board</a> (L to P). The letters stay the same so they match what you already know.</p>
    <p class="lede">Each option shows six sample posts (three of them with people and the robot from your workshop post), story highlight covers and a nine-post feed. Click any color to copy its hex code.</p>
  </header>"""
out = must_sub(r"<header>.*?</header>", header, out)

guide = """<section class="opt" id="guide-sec">
    <h2 class="sec" style="margin-top:0">How the four compare</h2>
    <div class="guide">
      <div><h3>C · Sunset Burn</h3><p>Dark base, orange kept as the signature, with coral and gold. The warmest and most energetic of the four, and the closest to today's dark feed.</p></div>
      <div><h3>D · Cream Studio</h3><p>The only fully light option with full-strength color. Ink text, orange for big shapes, green and indigo for detail. Good for breaking up a dark grid.</p></div>
      <div><h3>F · Mustard &amp; Cream</h3><p>Four flat colors only, with no orange. The strictest system and the easiest to keep consistent. Photos are turned black and cream to stay inside the palette.</p></div>
      <div><h3>L · Warm Neutral</h3><p>The calmest of the four. Paper and charcoal with a soft apricot, used once per post. Photos are slightly softened to match.</p></div>
    </div>

    <p class="foot-note">The logo and partner names in these mockups are redrawn placeholders for layout only. Real artwork replaces them in the final templates. Post text is taken from your existing posts. The people and the robot are cut out of screenshots of your own posts, so they look soft here. Original photos will look sharper, and each needs its own cut-out with a transparent background.</p>
  </section>"""
out = must_sub(r'<section class="opt" id="guide-sec">.*?</section>', guide, out)

open(D + "ai-baithak-mix.html", "w", encoding="utf-8").write(out)
css_ph = open(D + "cut/ph.css", encoding="utf-8").read()
assert "/*__PH_CSS__*/" in out
built = out.replace("/*__PH_CSS__*/", css_ph)
open(D + "ai-baithak-mix-built.html", "w", encoding="utf-8").write(built)
print("ok", len(built))
