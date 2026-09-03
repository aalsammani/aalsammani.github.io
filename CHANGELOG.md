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
