# AI Baithak Instagram branding work

Palette options, a feed look and per-post grid covers for the AI Baithak Instagram profile (@ai_baithak), built as HTML pages that were published as claude.ai artifacts.

## Published pages

| Page | What it is | Source in `work/` |
|---|---|---|
| https://claude.ai/artifact/BmNWnGyrjbfA25xWZbKZJw | Palettes A to F (dark, light and bold options, a strict black, mustard, white and cream set) with sample posts, posts with people, story covers and a feed grid | `ai-baithak-palettes.html`, `build.py` |
| https://claude.ai/artifact/TCf88i1k3Hf24eXUPfYTpE | Calm, minimal palettes L to P (replaced an earlier vibrant G to K set) | `make_calm.py` (earlier set: `make_light.py`) |
| https://claude.ai/artifact/TGZCFa94Aw8gx1joBd39MX | Cover tiles for the 20 newest posts, built from each post's own design, with the profile shown now and with the covers | `ai-baithak-grid2.html`, `build_grid2.py` (first attempt: `ai-baithak-grid.html`) |

## Folder map

- `work/` page sources, build scripts and generated pages.
  - `*.html` without `-built` or `-preview` are the sources. They contain markers (`/*__PH_CSS__*/`, `/*__JS_DATA__*/`) where the build scripts inject images as base64.
  - `*-built.html` is what was published. `*-preview.html` is the same page wrapped in a document skeleton for local viewing.
  - `build.py`, `build_grid.py`, `build_grid2.py`, `make_light.py`, `make_calm.py` generate the built pages. They resolve `D` from their own location, so run them from anywhere with `python3 work/<script>.py`.
  - `matte.py`, `robot.py` cut the people and the robot out of screenshots with a flood fill from the background.
  - `cut/` cut-outs, logos and the base64 asset files the build scripts read.
  - `crops/`, `hires/`, `shots/` raw screenshots and crops from the Instagram profile and the posts.
- `source-images/` the design screenshots that were shared for the work.

## Notes

- Posts, captions, dates and like counts were read from the public profile on 24 Nov 2026.
- The folders `hires/`, `shots/` and `source-images/` contain screenshots of real people (team members and event attendees) and partner logos. Keep this repository private.
- Fonts (Poppins, Inter) load from Google Fonts. The published pages need no other external files.
