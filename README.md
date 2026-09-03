# Abdallah Alsammani — Academic Website

Static site (plain HTML/CSS/JS, no build step required to deploy). Version 4.0, September 2026.

## Deploy
Copy everything in this folder to the root of the GitHub Pages repository (`aalsammani.github.io`) and push.
**Replace `CV.pdf` with your real vector PDF export** — the included file is a temporary raster fallback (see PENDING_UPDATES.md).

## Previewing
Open the site through a local server (`python3 -m http.server` in this folder, then http://localhost:8000) or use the
self-contained copies in `preview/` — those render correctly even when opened as a single file. The regular pages
require the `assets/` folder beside them.

## Structure
```
index.html            Home
research.html         Research program (4 pillars, toolkit, funding, directions)
publications.html     Year-grouped, filterable publication list
group.html            Research group (PI, members, past mentees, join)
teaching.html         Teaching philosophy, courses, curriculum, mentoring
cv.html               Structured CV + PDF download
contact.html          Contact + collaboration
assets/css/style.css  Single shared stylesheet (design tokens in section 1)
assets/js/main.js     Nav toggle, current-page marking, reveal, publication filter
assets/img/           profile.jpg, favicon.svg
_build/               Optional generator: edit partials/publications, run `python3 _build/build.py`
```

## Editing
- **Add a publication:** edit `_build/publications.py`, run the build; or hand-edit `publications.html` following an existing `<article class="pub">`.
- **Change nav/footer:** edit `_build/partials.py`, rebuild (they are shared by all pages).
- **Colors/spacing/type:** `assets/css/style.css` section 1.

## Documentation
PROJECT_CONTEXT.md · WEBSITE_STYLE_GUIDE.md · CONTENT_VERIFICATION.md · CHANGELOG.md · PENDING_UPDATES.md
