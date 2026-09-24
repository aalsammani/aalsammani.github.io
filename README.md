# Abdallah Alsammani — Academic Website (v7.0, September 2026)

Static site for GitHub Pages: plain HTML, one stylesheet, one small script, no frameworks or build dependencies.
Deploy by copying this folder's contents to the root of the `aalsammani.github.io` repository.

## Files that must already exist in the repository (not included here)
- `AI-Guide-4-students.pdf` — linked from teaching.html and research.html (keep it at the repository root).

## Structure
```
index.html research.html publications.html group.html teaching.html cv.html contact.html
CV.pdf                      full CV (replace with your current vector export)
assets/css/style.css        design system; palette and type scale in §1 tokens
assets/js/main.js           mobile menu, current-page marking, publication area filter
assets/js/explorers.js      interactive research illustrations (research.html)
assets/img/                 profile.jpg, favicon.svg
_data/                      CONTENT SOURCE OF TRUTH (JSON): publications, news, people, featured, resources
_build/                     generator: python3 _build/build.py regenerates the seven pages from _data + prose
robots.txt sitemap.xml .nojekyll
```

## Updating content (no HTML editing needed)
1. **Publications** — add an object to `_data/publications.json` (fields: id, year, type = journal|conference|preprint|abstract|other,
   areas = any of dynsys|sciml|biomed|neuro|other, selected = true to feature it in Selected Publications, title, authors with
   your name as `**Alsammani, A.**`, venue HTML, links {label: url}). Run the build.
2. **News** — add to `_data/news.json`; set `"home": true` on the three items you want on the homepage.
3. **People** — edit `_data/people.json` (current students; former mentees grouped by institution, with optional outcome links).
4. **Featured projects** — edit `_data/featured.json`; to use a real figure, put the image in `assets/img/` and change the
   `figure` field handling in `_build/build.py` (FIGS dict) or replace the SVG string with an `<img>` tag.
5. **Software & resources** — edit `_data/resources.json`.
6. Run `python3 _build/build.py` from this folder and commit the regenerated HTML.

Prose that is not data (research narrative, teaching text, CV entries) lives in `_build/build.py`.

See WEBSITE_MAINTENANCE.md for step by step update, preview, publish, and rollback instructions.
