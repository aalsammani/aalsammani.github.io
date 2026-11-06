# PROJECT_CONTEXT.md — Long-term memory for the Alsammani website

Last updated: 2026-11-06 (v7.1 publication audit; earlier: 2026-09-13 v5.0 redesign)

## Owner
Abdallah Alsammani, Ph.D. — Assistant Professor of Mathematics and Data Science (tenure-track),
Department of Mathematical Sciences, Delaware State University, Dover, DE. aalsammani@desu.edu · 302.857.6642.
Site URL: https://aalsammani.github.io (from the CV header). Update `SITE` in `_build/build.py`,
`sitemap.xml`, and `robots.txt` if a custom domain is adopted. (`_build/partials.py` no longer exists.)

## Purpose of the site
Communicate a coherent research identity — **Mathematical & Scientific Machine Learning for Biomedical Systems** —
to prospective students, collaborators, funders, and hiring/tenure committees. It must look like an established
academic research program, not an online CV and not a technology start-up.

## Source of truth
The CV (current file: October 25, 2026) is the source of truth for appointments, teaching, service, and mentoring.
For **publication status and bibliographic data**, the publisher/registry record (Crossref DOI metadata, arXiv,
medRxiv, ORCID) is authoritative, because the CV lags behind acceptances and revisions; a status is changed only on
verifiable evidence (accepted ≠ published; submitted ≠ accepted). Nothing is invented; unverifiable content is omitted and logged in
PENDING_UPDATES.md rather than guessed.

## Site architecture (v4.0)
| Page | Question it answers |
|---|---|
| index.html | Who is the PI and what is the research program? |
| research.html | What questions and methods define the program? (4 pillars, toolkit, funding, directions) |
| publications.html | What scholarship has resulted? (year-grouped, filterable) |
| group.html | Who is conducting the work, and how to join? |
| teaching.html | How does the PI teach and mentor? |
| cv.html | What is the complete academic record? (+ CV.pdf) |
| contact.html | How can someone reach or collaborate with the PI? |

Academic service, professional development, and technical skills live on the CV page, not Teaching.

## Research framing decisions
The CV's six research interests map onto four public pillars:
1. Mathematical Modeling ← Mathematical & Computational Epidemiology + Systems & Multiscale Modeling
2. Scientific Machine Learning ← Scientific Machine Learning
3. Biomedical Data Science ← Machine Learning for Healthcare + Statistical Methodology
4. Computational Neuroscience ← Computational Neuroscience
Featured projects (Home): identifiability tutorial (SciML), COVID vaccination–economics model (modeling), HFO in
long-term iEEG (neuroscience). The NoSQL database and construction-safety papers are listed in Publications but not
foregrounded, because they sit outside the biomedical identity.

## Technical decisions
- One shared stylesheet (`assets/css/style.css`) with tokens; one shared script. No CSS frameworks, no icon fonts.
  Icons are an inline SVG sprite (`ICONS` in `_build/partials.py`).
- Fonts: Playfair Display (serif: name, h1/h2/h3, pub titles) + Source Sans 3 (everything else) from Google Fonts.
- No canvas animations. The hero/research visual is a static, mathematically generated SVG phase portrait.
- Motion: one gentle reveal on section blocks, hover elevation on cards; `prefers-reduced-motion` disables all.
- Optional generator in `_build/` (Python, no dependencies). The generated HTML is what is deployed; hand-editing
  the HTML is fine if the generator is abandoned.
- Legacy files (about.html, index_old.html, index_revised_6_910_26.html, old style.css, Main.js, old_md_cv.txt)
  are NOT part of v4.0 and should be deleted from the deployed repository.

## Conventions
- Author string in publications: PI marked with `<span class="me">`; use the exact name form from the CV
  (Alsammani, A. / Alsammani, A. A. / Alsammani, A. A. M.).
- Dates: "2022 – 2025" with spaced en dash in timelines; "Aug 2022 – Jul 2025" on the CV page.
- Never display metrics (years, counts, students) that cannot be computed directly from the CV.
- Don't add collaborator affiliations unless they appear in the CV or the PI confirms them.

## How to update (typical cycles)
1. New paper → add to `_build/publications.py` (or hand-edit publications.html); add a Home news item if notable;
   consider swapping a Featured Research card. Update CONTENT_VERIFICATION.md and CHANGELOG.md.
2. New CV → diff against CONTENT_VERIFICATION.md; regenerate CV.pdf; update cv.html appointments/service.
3. New student → add a member card in group.html (photo optional; initials avatar fallback).

## v5.0 notes
- Content is data driven: `_data/*.json` is the source of truth for publications, news, people, featured projects, resources.
- Palette moved to a lighter academic blue (#294766 / #315574) with a burgundy accent (#7A2E3B); see WEBSITE_STYLE_GUIDE.md.
- Research is framed as a progression (Dynamical Systems → Structural Identifiability → Scientific ML → Biomedical Applications)
  with three methodological themes and three application domains; optimization for learning is an emerging, unpublished direction.

## v7.1 notes (2026-11-06)
- Publication records may carry `"status": "accepted"` (journal type) for formally accepted, unpublished articles; they
  render as "Accepted (in press)" and must not carry a journal DOI. Remove the field when the article is published.
- The owner sometimes edits `index.html` directly on GitHub; before rebuilding, compare the live HTML with a fresh build
  (`git diff` after `python _build/build.py`) and port any such edits into `_build/build.py` first.
- Figures and animations in `_build/figures.py` are generated from documented equations where they depict dynamics
  (hero, FIG_EPI, ANIM_SCIML, ANIM_NEURO); ANIM_MODELING, ANIM_BIOMED, FIG_UQ, FIG_IEEG, FIG_NODE remain precomputed/static.
- Checks: `python _build/validate.py` (add `--external` to resolve all DOIs/links). Previews: `python _build/make_previews.py`.
- GitHub Pages builds with Jekyll (no `.nojekyll`); `_data/` and `_build/` are therefore not published, root `*.md` files are.
