# WEBSITE_MAINTENANCE.md — How to update aalsammani.github.io

This site is plain HTML, CSS, and JavaScript hosted by GitHub Pages from the repository
`aalsammani/aalsammani.github.io` (branch `main`, root folder). There is no framework and no
required build step: GitHub serves the HTML files exactly as committed. A small Python generator
(`_build/build.py`) regenerates the HTML from data files so you never edit publication lists by hand.

Contents: 1 Repository · 2 Local setup · 3 Routine updates · 4 Figures and animations ·
5 Teaching and other prose · 6 Adding a page · 7 Preview and test · 8 Publish · 9 Verify deployment ·
10 Troubleshooting · 11 Roll back · 12 File map

---

## 1. Repository

- Repository: https://github.com/aalsammani/aalsammani.github.io
- Published site: https://aalsammani.github.io
- Settings → Pages must be set to *Deploy from a branch*, branch `main`, folder `/ (root)`.
- `.nojekyll` at the root tells GitHub not to run Jekyll; keep it.

## 2. Local setup (once)

```bash
git clone https://github.com/aalsammani/aalsammani.github.io.git
cd aalsammani.github.io
python3 --version          # any Python 3.8+ works; no packages are required
```

To rebuild pages after editing data or prose:
```bash
python3 _build/build.py     # rewrites index.html, research.html, ... in the root
```

## 3. Routine updates (edit a data file, rebuild, commit)

### 3a. Add a publication or preprint
Edit `_data/publications.json`. Add an object at the top of the list (newest first is only a
convention; the build sorts by year):
```json
{"id":"lastname2027venue","year":2027,"type":"journal","areas":["sciml"],"selected":true,
 "title":"Title exactly as published",
 "authors":"Coauthor, A., **Alsammani, A.**, & Other, B.",
 "venue":"<em>Journal Name</em>, 12(3), 100–120.",
 "links":{"DOI":"https://doi.org/10.xxxx/yyyy"}}
```
- `type`: `journal`, `conference`, `preprint`, `abstract`, or `other` (dissertation).
- `areas`: any of `dynsys`, `sciml`, `biomed`, `neuro`, `other` (drives the area filter).
- `selected: true` shows it in Selected Publications; keep that list to about six.
- Your name must be written `**Alsammani, A.**` (or `**Alsammani, A. A.**`) to be bolded.
- `links` labels that display well: `DOI`, `Publisher`, `arXiv`, `medRxiv`, `SSRN`, `Code`, `Data`.
- When a preprint is published: change `type` to `journal`, replace `venue`, add the DOI, and change
  the `medRxiv`/`arXiv` link to `DOI` (you may keep both).
Then `python3 _build/build.py`.

### 3b. Add a news item
Edit `_data/news.json`. Newest first. Set `"home": true` on exactly the three you want on the
homepage; all items appear under Group news.
```json
{"date":"2027","title":"Paper accepted in <em>Journal</em>","text":"One optional sentence.","url":"https://doi.org/...","home":true}
```

### 3c. Students and mentees
Edit `_data/people.json`. `current` is a list of `{name, role, topic, links}`; leave `topic` empty
rather than guessing. `former` is grouped by institution; each member has `name`, `term`, `project`,
and an optional `outcome` `{text, venue, url}` for a paper or preprint.

### 3d. Featured projects (homepage)
Edit `_data/featured.json` (three entries: title, question, tags, figure key, links). The `figure` key
maps to an SVG in `_build/figures.py` (see §4 for using a real image instead).

### 3e. Software and resources
Edit `_data/resources.json`: `{title, kind, text, links}`. Add code repositories here.

### 3f. Biography, appointment, contact
- Hero text and identity line: `_build/build.py`, section `HOME` (search for `hero__statement`).
- PI paragraph on the Group page: `_build/build.py`, section `GROUP`.
- Appointments, education, honors, service, skills: `_build/build.py`, section `CV` (`entry(...)` lines).
- Email and profile URLs: the `EMAIL` and `PROFILES` constants at the top of `_build/build.py`.
- Contact page address: `_build/build.py`, section `CONTACT`.
- Replace `CV.pdf` at the root with your new export (same filename) whenever the CV changes.

## 4. Figures and animations

- Static scientific figures are inline SVG strings in `_build/figures.py` (`hero_svg()`, `FIG_HYBRID`,
  `FIG_EPI`, `FIG_IEEG`, `FIG_UQ`, `FIG_NODE`). Edit the SVG text and rebuild.
- To use a real figure from a paper: save it as `assets/img/<name>.png` or `.svg` (≤ 300 KB, width ≥ 900 px),
  then in `_build/build.py` change the `FIGS` dictionary entry for that featured project to
  `'<img src="assets/img/<name>.png" alt="One sentence describing what the figure shows" loading="lazy">'`.
  Always write real alt text.
- Interactive explorers (SIR model, identifiability, mechanistic vs hybrid, animated iEEG) live in
  `assets/js/explorers.js`. Each is a function keyed by `data-explorer="..."`; the page markup that
  hosts them is produced by `explorer(...)` calls in `_build/build.py`, section `RESEARCH`.
  All explorer data are synthetic; keep the "synthetic illustration" notes if you edit them.
- Pillar animations on the homepage are inline SVG in `_build/figures.py` (`ANIM_MODELING`, `ANIM_SCIML`, `ANIM_BIOMED`, `ANIM_NEURO`) driven by CSS keyframes in `style.css` §18; the pillar text, questions, methods, and selected work are the `pillar(...)` calls in `_build/build.py`, section `HOME`, and the diagram stages are the `dnode(...)` calls just below them.
- The hero trajectory animation is CSS (`.hero__visual .traj` in `assets/css/style.css`); it is
  disabled automatically when a visitor prefers reduced motion.
- Colours for all figures are set in `explorers.js` (`C` object) and `figures.py`; keep them consistent
  with the CSS tokens in `assets/css/style.css` §1.

## 5. Teaching statement, philosophy, and courses
All Teaching prose is in `_build/build.py`, section `TEACHING`: the philosophy paragraphs, the four
"How I teach" principles (`principle(...)`), the AI framework (`framework(...)`), and the course lists.
The AI guide PDF is `AI-Guide-4-students.pdf` at the repository root; replace the file to update it.
The Research narrative is in section `RESEARCH` (`area(...)` calls) of the same file.

## 6. Adding a page
1. In `_build/build.py`, add `("newpage.html", "New Page")` to `NAV` (keep the nav to eight items or fewer).
2. Add a block at the end of the file:
   ```python
   newpage = page_header('New Page', 'One sentence lede.') + '''<section class="section"><div class="container container--narrow"> ... </div></section>'''
   page('newpage.html', 'New Page — Abdallah Alsammani, Ph.D.', 'Meta description.', newpage)
   ```
3. Add the URL to `sitemap.xml`. Rebuild. Reuse existing CSS classes (`section`, `container`,
   `section-head`, `prose`, `grid grid--2`) rather than adding new styles.

## 7. Preview and test before publishing
```bash
python3 _build/build.py
python3 -m http.server 8000          # then open http://localhost:8000 in a browser
```
Open the page directly from a server, not by double clicking the file, or the stylesheet may not load.
Check: the page you changed on desktop and on a narrow window (drag the browser to ~400 px wide);
every new link; the browser console (F12 → Console) shows no red errors.
Quick automated checks (optional): `tidy -q -e index.html` for HTML errors if `tidy` is installed.

## 8. Publish
```bash
git status                            # see what changed
git add -A
git commit -m "Add 2027 paper; update news"
git push origin main
```
GitHub Pages rebuilds automatically in about a minute.

## 9. Verify deployment
- Repository → *Actions* tab: the latest "pages build and deployment" run should show a green check.
- Open https://aalsammani.github.io in a private window (to avoid cache) and confirm the change.
- If the old version persists, hard refresh (Ctrl/Cmd+Shift+R).

## 10. Troubleshooting
| Symptom | Likely cause | Fix |
|---|---|---|
| Page shows unstyled text, huge icons | `assets/css/style.css` missing or moved, or file opened without a server | Restore the `assets/` folder; preview via `http.server` |
| A publication is missing or shows twice | JSON edited by hand with a syntax error or duplicated `id` | Run `python3 -c "import json;json.load(open('_data/publications.json'))"`; fix the reported line |
| Build prints a Python error | Unbalanced quotes in prose inside `build.py` | Read the line number in the traceback; use `&quot;` or a different quote style |
| A figure is blank | Bad SVG in `figures.py` or wrong `src` path (paths are case sensitive) | Open the SVG in a browser; check the filename matches exactly |
| Explorers do not react | JavaScript error | F12 → Console; the message names the line in `explorers.js` |
| Link 404 | Typo or file not committed | `git status` to see untracked files; check the exact filename |
| Actions run failed | Usually a file over 100 MB or a bad `.nojekyll` change | Open the run log; remove the large file; keep `.nojekyll` empty |

## 11. Roll back a bad update
```bash
git log --oneline -10                 # find the last good commit hash
git revert <bad-commit-hash>          # safest: creates a new commit undoing it
git push origin main
```
To restore a single file: `git checkout <good-commit-hash> -- publications.html` then commit.
Never force push to `main`; the history is your backup.

## 12. File map
```
index.html … contact.html   generated pages (edit via _data + _build, then rebuild)
_data/                      publications.json, news.json, people.json, featured.json, resources.json
_build/build.py             prose + page assembly;  _build/figures.py  SVG figures
assets/css/style.css        design tokens §1 (colours, type scale, spacing) and all components
assets/js/main.js           mobile menu, active nav, publication area filter
assets/js/explorers.js      interactive research illustrations (research.html only)
assets/img/                 profile.jpg, favicon.svg, any real figures you add
CV.pdf, AI-Guide-4-students.pdf, robots.txt, sitemap.xml, .nojekyll
*.md                        PROJECT_CONTEXT, WEBSITE_STYLE_GUIDE, CONTENT_VERIFICATION, CHANGELOG, PENDING_UPDATES, this guide
```
