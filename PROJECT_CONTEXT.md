# PROJECT_CONTEXT.md — Long-term memory for the Alsammani website

Last updated: 2026-09-02 (v4.0 initial redesign)

## Owner
Abdallah Alsammani, Ph.D. — Assistant Professor of Mathematics and Data Science (tenure-track),
Department of Mathematical Sciences, Delaware State University, Dover, DE. aalsammani@desu.edu · 302.857.6642.
Site URL assumed: https://aalsammani.github.io (from the CV header). Update SITE_URL in `_build/partials.py`,
`sitemap.xml`, and `robots.txt` if a custom domain is adopted.

## Purpose of the site
Communicate a coherent research identity — **Mathematical & Scientific Machine Learning for Biomedical Systems** —
to prospective students, collaborators, funders, and hiring/tenure committees. It must look like an established
academic research program, not an online CV and not a technology start-up.

## Source of truth
The CV (updated June 26, 2026) is the single source of truth for every factual claim. If the site and CV disagree,
the CV wins and the site is corrected. Nothing is invented; unverifiable content is omitted and logged in
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
