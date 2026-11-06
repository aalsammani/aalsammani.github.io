# CHANGELOG.md

## v4.0 — 2026-09-02 · Comprehensive redesign and reorganization
### Architecture
- Split Research into `research.html` (program) and `publications.html` (output).
- Renamed `team.html` → `group.html` (Research Group); added `cv.html`.
- Moved Academic Service, Professional Development, and Technical Skills from Teaching to CV page.
- Removed legacy files from the deploy set: `about.html` (stale JU page), `index_old.html`,
  `index_revised_6_910_26.html`, old `style.css`/`Main.js` (sidebar system), `old_md_cv.txt`.
### Design system
- One shared stylesheet with named tokens (`--navy-primary`, `--blue-accent`, `--text-secondary`, …) and an 8px
  spacing scale; one shared script. Removed Font Awesome (inline SVG sprite instead) and IBM Plex Mono.
- Retired the five-colour accent set; single navy/blue family.
- Replaced neural-network canvas animations with a static generated phase-portrait SVG.
- Reduced motion to one reveal + hover elevation; `prefers-reduced-motion` respected; removed scroll-progress bar
  and count-up counters.
### Homepage
- Hero rebuilt: portrait | name · title · institution · 90-word research statement · 4 profile links · 3 CTAs
  (Explore research / Publications / Download CV) | scientific visual. Biography moved off the hero.
- Added tagline band "Mathematical & Scientific Machine Learning for Biomedical Systems".
- Added four numbered research pillars, Featured Research (3 projects), horizontal academic timeline, news list,
  join/collaborate panel. Removed unverifiable statistics strip and the education detail block.
### Content corrections (see CONTENT_VERIFICATION.md)
- Neurology paper marked published (was "in press"); ORCID placeholder removed; unsupported metrics removed;
  Ph.D. student roster and collaborator affiliations omitted pending confirmation; Sloan CSP (PI) restored;
  unfunded grants omitted; contact footer year and dead Scholar `#` link fixed; missing `alt` fixed.
### Accessibility / SEO / quality
- Skip link, visible focus styles, `aria-current`, `aria-expanded` on menu toggle, Escape closes menu,
  labelled SVG figures, single `<h1>` per page, AA contrast on all text tokens.
- Canonical/OG/theme-color tags, JSON-LD Person schema, `sitemap.xml`, `robots.txt`, favicon, `.nojekyll`.
- Automated audit: 0 broken internal links/anchors/images; no horizontal overflow at 390/768/1024/1920.

## v4.0.1 — 2026-09-03 · Rendering-failure diagnosis and hardening
- **Cause of the reported unstyled page:** `index.html` was opened on its own (single-file preview), detached from
  the `assets/` folder, so `assets/css/style.css`, `assets/js/main.js`, and `assets/img/profile.jpg` returned
  file-not-found. Served as a directory, every page loads all assets (verified over HTTP, 14 renders, 0 404s,
  0 console errors, 0 HTML errors, 340/340 CSS rules parsed). No paths were wrong; none were changed.
- Hardened the markup so a page degrades sanely even without CSS: sprite icons carry intrinsic
  `width="16" height="16"`; the mobile navigation uses the native `hidden` attribute (toggled by `main.js`) instead
  of relying on CSS to hide it, which removes the "duplicate navigation" when styles are absent.
- Fixed `.cv-toc a` over-riding `.btn` on the CV page's sidebar PDF button (scoped to `.cv-toc ul a`).
- Added `preview/*.preview.html`: self-contained copies (CSS, JS, portrait inlined) that render correctly when opened
  as a lone file. These are for previewing only; deploy the parent folder.

## v4.1 — 2026-09-03 · Hero refinement and research-group roster update
### Hero / navigation
- Portrait moved inside the content grid (208px column, centred, thin offset ring) in a Portrait | Identity | Visual
  composition; hero container 1200px; top padding reduced (nav-to-name gap 48px, was ~90px).
- Research statement shortened to 45 words so it no longer duplicates the tagline band.
- Navbar portrait removed; identity mark is the name plus a quiet "Ph.D." suffix (hidden ≤480px).
- ORCID (0000-0003-4340-4550) added to profile links and JSON-LD.
### Research Group
- Current students: Jing Li (Ph.D.), Uchenna J. Okorie (Ph.D.), Fiona A. Ochieng (M.S.). Merasia M. Johnson moved
  to Former Research Mentees.
- "Past mentees" → "Former Research Mentees", split into Delaware State University and Jacksonville University
  tables (Student | Research project / scholarly outcome | Term); new broader introduction; publication titles
  italicised and linked; Sarah Goodyear consolidated into one entry.
### Publications / cross-site
- Ubaka et al., CRC 2026: status accepted → published (Conference proceedings), ASCE link added.
  Counts now: 6 journal · 1 accepted · 4 proceedings · 7 preprints · 4 abstracts · 2 other.
- ICU-mortality preprint: medRxiv link and DOI added; described as a preprint everywhere.
- Home news rewritten for the two items above; Research page representative-work link for the ICU preprint now
  points to medRxiv.
- Verified: each student name occurs exactly once on group.html; no student is listed as both current and former.

## v5.0 — 2026-09-13 · Comprehensive redesign: information architecture, narrative, visual system
### Architecture and content
- Homepage cut from eight sections to five: hero → research overview (progression Dynamical Systems → Structural
  Identifiability → Scientific ML → Biomedical Applications, three methodological themes, three domains) → three featured
  projects → three highlights → call to action. Removed pillars grid, academic timeline, full news list, stats.
- Research page reorganized into three methodological themes (Dynamical Systems & Stochastic Modeling; Scientific ML &
  Structural Identifiability; Statistical Learning, UQ & Optimization) and three application domains; optimization for
  learning added as an explicitly unpublished emerging direction; Software & resources section added (verified items only).
- Publications: Selected Publications (6) before the complete list; area filters (Dynamical Systems / Scientific ML /
  Biomedical Data Science / Neuroscience / Other Applications); year → peer reviewed / preprints / other grouping;
  no counters; no "in press".
- Group page restructured: People (PI + 3 current students) / Current projects (4) / Opportunities + former mentees /
  Group news (full news list now lives here).
- Teaching shortened to philosophy, four principles, generative AI framework + guide panel, current and selected courses,
  mentoring; Auburn and Sudan teaching reduced to one line; certificates removed.
- CV page trimmed to appointments, education, honors, service, skills; professional development certificates removed
  (remain in the PDF). Contact simplified; phone number removed from the public site.
- All structured content moved to `_data/*.json`; generator rewritten to read it.
### Visual system
- Palette: primary #294766, light #315574, burgundy accent #7A2E3B, charcoal text, white/off white surfaces.
- White sticky header with burgundy active underline; navy footer reduced to three lines.
- Fonts: Source Serif 4 (headings, publication titles) + Source Sans 3 (text). Hero name 52px, h2 34px, titles 22px, body 17px.
- Cards, shadows, reveal animation, canvas visuals, and the multi tone accent set removed; hairline rules and top rules
  carry hierarchy. Phase portrait and three schematic figures recoloured to the new palette.
- Person schema, canonical, OG, favicon, sitemap, robots retained; nav label "Research Group" → "Group".

## v6.0 — 2026-09-23 · Final revision: interactivity, figures, teaching statement, maintenance guide
- Palette: navy #294766 with muted teal accent #2E7D86 and soft gray surfaces (replaces the burgundy accent).
- Interactive explorers on Research (vanilla JS, inline SVG/canvas, ~14 KB): SIR model with R0 readout and
  parameter uncertainty envelope; structural identifiability of dx/dt = −(a+b)x; mechanistic (constant β) versus
  hybrid (time varying β) fit to synthetic seasonal data with RMSE readout; animated synthetic iEEG with HFO events
  (play/pause, auto paused under reduced motion). All labeled synthetic.
- Hero phase portrait trajectories now draw in over 4.5 s (CSS only; off under prefers-reduced-motion).
- New static figures: neural ODE architecture; uncertainty propagation band computed numerically from an SIR ensemble.
  Hybrid model figure relabeled so it poses the identifiability question rather than stating a result.
- Equations set in native MathML (no library dependency).
- Teaching philosophy expanded to five themes: mathematical understanding; theory → computation → interpretation;
  an inclusive and demanding classroom; active learning and independent thinking; mentoring and responsible tools.
- Group projects link to the related publications. WEBSITE_MAINTENANCE.md added.

## v7.0 — 2026-09-24 · Final refinement: hero, four pillars restored with animations, interactive research diagram
- Hero: name reduced to 39 px (clamp 1.85–2.45 rem) and kept on one line on desktop; title moved to a teal kicker above the
  name; portrait enlarged to 200 px with a soft ring; faint grid background; introduction rewritten in first person.
- Research program section: interactive progression diagram (four selectable stages with animated dashed connectors;
  selecting a stage opens and scrolls to the matching pillar) plus the four research pillars from v4, each with a CSS
  animated concept figure (epidemic curves for three β; particles flowing along a mechanistic plus learned vector field;
  reliability diagram with points appearing and a recalibration curve; scrolling synthetic iEEG with HFO events) and an
  expandable panel with questions, methods, and selected publications. Animations are pure CSS and switch off under
  prefers-reduced-motion; the diagram stacks vertically below 1024 px.
- Group page PI biography rewritten in first person. No em dashes in prose anywhere on the site.

## v7.1 — 2026-11-06 · Publication audit, research software, figure corrections (no redesign)
Full details and evidence: `WEBSITE_UPDATE_REPORT_2026-11-06.md`.
### Publications (`_data/publications.json`, 22 → 27 records; all IDs preserved)
- New: Alsammani, *Machine learning algorithm selection* — **accepted** in *Journal of Intelligent & Fuzzy Systems*
  (Nov 5, 2026), shown as "Accepted (in press)"; no DOI/volume/pages (none exist yet). Companion code + Zenodo DOI linked.
- Preprint → journal: identifiability tutorial (*Bull. Math. Biol.* 88(11), Art. 212, doi:10.1007/s11538-026-01779-0);
  epidemic–awareness paper (*BIOMATH* 15(2), Art. 2610234, doi:10.55630/j.biomath.2026.10.234). arXiv kept as extra links.
- Corrected: full author lists (Neurology, TRSTMH, arXiv 2408.04862); TRSTMH 120(9) 929–947; JBHI year 2023 → 2024 (issue
  date); current arXiv titles for 2505.08873 (v2) and 2308.05819 (v3); DOIs added for CRC fleet paper, ICCSA 2023/2024,
  SLEEP 2022, SSRN preprints; open arXiv versions linked for JBHI, ICCSA 2023/2024, Information Systems.
- Added from CV/ORCID: low-rank compression preprint (SSRN 7293357), EdArXiv AI framework preprint, AES 2025 and
  AI-in-Epilepsy 2026 abstracts. ICU paper unchanged (medRxiv preprint; no published version).
- Schema: optional `"status": "accepted"` on a journal record → label "Accepted (in press)" (`.label--accepted`).
### Content
- News: three new homepage items (JIFS acceptance, BMB, BIOMATH); arXiv-posting item superseded by the BMB item.
- Software & resources: identifiability reproducibility package, ML Selection Framework, SIRA code, *Calculus and Matrix
  Methods for Data Science* open textbook (PENDING #16), Zenodo DOI for the AI guide; EdArXiv DOI on Teaching (PENDING #19).
- Research/Home/Group links updated from arXiv to journal DOIs; method tags and JSON-LD `knowsAbout` aligned with the
  stated research areas. Google Scholar link → author search (profile ID still unverified, PENDING #3).
- Generator now reproduces the owner's direct GitHub edits to index.html (hero statement, identity line, 400 px portrait,
  hyphenation); a rebuild no longer reverts them.
### Figures (`_build/figures.py`, `assets/js/explorers.js`)
- Hero phase portrait: vector field used decay 0.35 but trajectories 0.16 (≈10° misalignment) → one shared constant.
- Pillar 02 animation regenerated from a single ODE (linear spiral sink + cubic correction, RK4), field and particles consistent.
- Pillar 01: removed unlabeled S(t) curve drawn on a different scale from the three (×3-scaled) I(t) curves.
- Pillar 04: synthetic iEEG regenerated so each event marker sits on an actual high-frequency burst.
- Featured vaccination figure: hand-drawn Bézier curves and an unlabeled dashed curve → curves computed from an SIR model
  with vaccination, labeled synthetic. Identifiability figure: clipped caption text rewrapped.
- Reliability-diagram label corrected ("overestimates risk", not "overconfident"); explorers: x tick labels no longer
  rounded (2.5 shown as "3"), identifiability demo shows a genuinely different (a, b) pair when a = b.
### Technical
- Fixed broken `< h3>` tag on the homepage; visually hidden `<h2>` on Group and Contact (heading outline);
  home canonical/og:url → site root (matches sitemap); sitemap lastmod updated; ASCE link → DOI link.
- `preview/*.preview.html` regenerated from current pages (were v4.1, Sept 3) by new `_build/make_previews.py`.
- New `_build/validate.py` (structure, links, anchors, data consistency; `--external` resolves DOIs and links).
