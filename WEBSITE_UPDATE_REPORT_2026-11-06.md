# Website update report — November 6, 2026 (v7.1)

Scope: content verification and maintenance of https://aalsammani.github.io. No redesign: layout, navigation, palette,
typography, page set, photographs, filters, and interactive features are unchanged. Every page was rebuilt from
`_data/` and `_build/` with the existing generator.

## 1. Summary
- Publication database audited record by record against Crossref, the DOI registry, arXiv, medRxiv, ORCID, OpenAlex,
  Zenodo, and the October 25, 2026 CV: 22 → 27 records, no duplicates, all existing IDs kept.
- Accepted, published, and preprint statuses are now distinguished. The *Journal of Intelligent & Fuzzy Systems*
  article is shown as **Accepted (in press)**, with no invented DOI, volume, or pages.
- Two former preprints are now listed as journal articles (*Bulletin of Mathematical Biology*, *BIOMATH*).
- Four verified research software / open-education resources added.
- Seven figure and illustration defects corrected, most of them mathematical inconsistencies.
- One broken HTML tag (visible on the homepage as "< h3>") and several smaller technical issues fixed.
- The owner's direct edits to `index.html` on GitHub (Sept 27) were ported into the generator so rebuilds keep them.

## 2. Publications corrected

| Record | Former status / data | New status / data | Evidence |
|---|---|---|---|
| Alsammani — *Machine learning algorithm selection: A unified framework from classical methods to foundation models* | not listed | **Accepted (in press)**, *J. Intelligent & Fuzzy Systems*, accepted Nov 5, 2026; not yet published | PI-supplied acceptance date; companion README ("accepted for publication"); no Crossref record exists (consistent with unpublished) |
| Alsammani — *A tutorial on symbolic structural identifiability analysis of ODE models in Julia* | Preprint, arXiv:2605.18910 | **Journal article**, *Bull. Math. Biol.* 88(11), Article 212 (online Oct 25, 2026); arXiv kept | https://doi.org/10.1007/s11538-026-01779-0 (Crossref); arXiv journal-ref |
| Mohammed & Alsammani — *Long-term coexistence of epidemics and risk awareness…* | Preprint, arXiv:2607.18301 | **Journal article**, *BIOMATH* 15(2), Article 2610234 (online Oct 23, 2026); arXiv kept | https://doi.org/10.55630/j.biomath.2026.10.234 (Crossref); arXiv journal-ref |
| Alsammani, Johnson, Elrefaei — ICU mortality | medRxiv preprint | **Unchanged: preprint** | medRxiv API: one version, "no articles found for published version" |
| Chen et al., *Neurology* 107(2) e218225 | 7 authors + "et al." | full 11-author list | Crossref |
| Yousif et al., *TRSTMH* | article number only | 120(9), 929–947; full 7-author list | Crossref |
| Alsammani, Stacey, Gliske, *IEEE JBHI* 28(2) | year 2023 | year 2024 (issue Feb 2024; online 2023); arXiv:2209.10468 linked | Crossref; CV |
| Rueda-Benavides et al., CRC 2026 | no link | DOI 10.1061/9780784487006.049 | Crossref |
| Ubaka et al., CRC 2026 | ASCE URL | DOI link (same article; ASCE blocks link checkers) | Crossref |
| ICCSA 2023 / 2024 / 2025 | ICCSA 2023/2024 without DOI | DOIs 10.1007/978-3-031-37108-0_21, 10.1007/978-3-031-65223-3_13; LNCS venue wording; arXiv 2305.08210 / 2308.13921 | Crossref, arXiv |
| Alflahi et al., *Information Systems* 140 | DOI only | + arXiv:2601.16490 | arXiv |
| arXiv:2505.08873 (cholera) | v1 title | v2 title *Threshold dynamics and integrated control of cholera transmission with sanitation and vaccination* (v1 title noted) | arXiv API (v2, 2026-08-22) |
| arXiv:2308.05819 (stochastic HBV) | older title | v3 title *…: Extinction, persistence, and ergodicity* | arXiv API (v3, 2026-08-18) |
| arXiv:2408.04862 (trophic cascade) | "et al." | full author list incl. P. Landi | arXiv |
| SSRN 6512551 (crash severity), SSRN 6388938 (fractional, SSRN version of arXiv:2602.07105) | no link / arXiv only | SSRN DOI links | Crossref |
| SSRN 7293357 — *Compositional error analysis and spectral budget allocation for low-rank compression of feedforward neural networks* (Alsammani, Li, Liu, Ndeke, Okorie) | not listed | **Preprint** | Crossref; on PI's ORCID; *not yet on CV — please confirm* |
| EdArXiv — *A student-centered framework for responsible use of generative AI in higher education* | cited on Teaching without link | Preprint record + DOI 10.35542/osf.io/vsjhe_v2 | Crossref, ORCID |
| Tyner et al., *SLEEP* 2022 abstract | "45, 1" | 45(Suppl. 1), A255, Abstract 0579; DOI | Crossref |
| Alsammani et al., AES 2021 abstract | no link | AES abstract page | ORCID |
| Das et al. 2026 (AI in Epilepsy conf.); Shindhelm et al. 2025 (AES) | missing from site (on CV; listed in earlier site versions) | Conference abstracts, no links | CV p.3 |

All other records (MBE 2025, DCDS-B 2019, dissertation, ICCSA 2025, fractional arXiv) verified unchanged.
Area tags (`dynsys`, `sciml`, …) and the "Selected" list are editorial, not bibliographic.

## 3. Accepted manuscripts
- *Journal of Intelligent & Fuzzy Systems*: Accepted (in press), accepted November 5, 2026. Label "Accepted (in press)",
  venue text says "not yet published". No DOI, volume, issue, or pages are shown because none exist.
- Schema change (backward compatible): optional `"status": "accepted"` on a journal record; `pub_item()` renders
  the label, `.label--accepted` styles it (primary blue, distinct from the teal preprint label).

## 4. Newly verified journal publications
- *Bulletin of Mathematical Biology* 88(11), Article 212 (2026). The status given in the request ("accepted") is
  superseded: the article was published online on October 25, 2026.
- *BIOMATH* 15(2), Article 2610234 (2026).

## 5. Research software and resources added (`_data/resources.json`)
| Resource | Links | Verified via |
|---|---|---|
| ML Selection Framework (companion to the JIFS article; described as educational notebooks, not experimental results) | GitHub; Zenodo concept DOI 10.5281/zenodo.19599147 (all versions; latest v1.1.0, Oct 28, 2026); v1.0.0 DOI 10.5281/zenodo.19599148 cited in text | GitHub API (public, MIT), Zenodo API |
| Structural identifiability tutorial reproducibility package | GitHub; Zenodo 10.5281/zenodo.18684343 | Zenodo API (v2.1.0) |
| SIRA, code for the BIOMATH article | GitHub; Zenodo 10.5281/zenodo.22164947 | Zenodo API |
| *Calculus and Matrix Methods for Data Science* open textbook (resolves PENDING #16) | live site + GitHub | GitHub API, HTTP 200 |
| AI student guide | + Zenodo 10.5281/zenodo.22153920 | Zenodo API |

Public repositories for unpublished work (e.g., HCV multiscale model, SciML book) were intentionally not added.

## 6. Figures modified (`_build/figures.py`, `assets/js/explorers.js`)
| Figure | Problem | Change | Basis |
|---|---|---|---|
| Hero phase portrait | Vector field from dx/dt = −0.35x − y, dy/dt = x − 0.35y, but trajectories decayed at rate 0.16: ≈10° median misalignment | One constant k = 0.16 for both; trajectories are exact solutions r = r₀e^(−kt) | Linear spiral sink; measured alignment 9.6° → 1.8° (discretization) |
| Pillar 02 animation (SciML) | Precomputed field and particle paths inconsistent (8° median, 19° p90) | Regenerated: f = linear spiral sink, g = −c‖x‖²x correction; RK4; field, paths, particles from the same ODE | Alignment 2.0° |
| Pillar 01 animation (modeling) | Unlabeled dashed S(t) on a 0–1 scale beside I(t) curves scaled ×3 (the fit recovers exact SIR, R₀ = 3, 2, 1.4) | Removed the S(t) curve; the label "I(t), three values of β" is now exact | SIR fit to the drawn curves |
| Pillar 04 animation (synthetic iEEG) | Event markers did not coincide with any visible high-frequency burst | Regenerated: seamless periodic background, 3.2 px-period Gaussian bursts centred on each marker | Documented in `_anim_neuro()` |
| Featured: vaccination/COVID-19 | Hand-drawn Bézier curves and an unlabeled dashed "economic" curve presented like model output | Computed from SIR with vaccination (β = 0.3, γ = 0.1, ν = 0.002 vs 0.01/day, RK4); labeled synthetic | Documented in `_fig_epi()`; not the MBE paper's model or results |
| Featured: identifiability | Caption text ran outside the figure and was clipped | Rewrapped within the 300 × 200 view box | — |
| Pillar 03 reliability diagram | Accessible label said "overconfident"; all points lie below the diagonal, i.e. systematic overestimation | Label corrected | Calibration terminology |
| Explorers | x-tick labels rounded 2.5/7.5 to "3"/"8"; identifiability demo's "second pair" equalled the first when a = b | Exact tick labels; distinct pair (30/70 split) when a = b | — |

Unchanged (checked, sound): FIG_UQ (SIR ensemble envelope), FIG_NODE, FIG_IEEG (labeled schematic), the SIR and hybrid
explorers (RK4), photographs. All figures remain labeled as synthetic illustrations; none depicts publication data.

## 7. Technical issues corrected
- `index.html`: malformed `< h3>` tag (rendered as literal text on the third featured card).
- Generator out of sync with the live homepage: hero statement, identity line, 400 × 400 portrait, hyphenation, and
  the corrected heading are now produced by `_build/build.py` (a rebuild previously would have reverted them).
- Heading outline: Group and Contact jumped from h1 to h3; visually hidden h2 added (no visual change).
- Home canonical and og:url now the site root (matches sitemap); sitemap `lastmod` updated.
- Google Scholar link: the `user=abdallah-alsammani` ID is not a valid Scholar ID; the link now opens a Scholar
  author search until the real ID is supplied.
- JSON-LD `knowsAbout` aligned with the stated research areas; method tags extended (numerical simulation; inverse
  problems and parameter estimation; algorithm selection and evaluation; low-rank approximation).
- `preview/*.preview.html` were v4.1 copies (Sept 3) with outdated content and fonts; regenerated by the new
  `_build/make_previews.py`.
- Documentation corrected: there is no `.nojekyll`; `_build/partials.py` does not exist; CV.pdf is now a proper PDF.

## 8. Validation results (executed 2026-11-06)
- `python _build/validate.py`: 0 errors, 0 warnings. The same script on the original site reports 2 errors (the
  `< h3>` tag) and 2 warnings (heading jumps).
- `python _build/validate.py --external`: 22/22 DOIs registered; every arXiv, GitHub, Zenodo, ORCID, medRxiv, AES,
  and site link returned HTTP 200. ASCE (403) and LinkedIn (999) block automated clients; ASCE is now reached via DOI.
- Headless Chrome 7 pages: no console errors before or after (capture verified with a deliberate test message).
- Functional test (injected script): area filter counts all = 27, dynsys 9, sciml 3, biomed 4, neuro 6, other 6;
  `aria-pressed` toggles; one "Accepted (in press)" label; pillar toggle opens; mobile menu opens; all four explorers render.
- Responsive check: each page in a 390/768/1024 px frame: no horizontal overflow (before or after).
- Screenshots of all 7 pages captured at 390/768/1440 px before and after; Home, Publications, and Research reviewed
  side by side at desktop width: layout, spacing, colours, and typography unchanged.
- Generator reproducibility: building the untouched source reproduced the committed pages except `index.html`,
  which explained the hand-edit port above.

## 9. Items requiring your confirmation (see also PENDING_UPDATES.md #20–25)
1. When the JIFS article appears online: DOI, volume/issue/pages (then remove `status`).
2. Whether the SSRN low-rank compression preprint should be public (it is on ORCID, not on the CV).
3. The real Google Scholar profile ID.
4. Update CV.pdf: JIFS acceptance, new preprints, Ph.D. students J. Li and U. J. Okorie, current arXiv titles.
5. Links for the AES 2025 and AI-in-Epilepsy 2026 abstracts, if any.
6. The area tag (`sciml`) chosen for the JIFS and low-rank papers.

## 10. Sources used
Crossref REST API (api.crossref.org/works/{doi}; author query "Alsammani"); DOI registry handle API
(doi.org/api/handles); arXiv API (export.arxiv.org/api/query); medRxiv/bioRxiv API (api.biorxiv.org/details,
/pubs); ORCID public API (pub.orcid.org/v3.0/0000-0003-4340-4550/works); OpenAlex (api.openalex.org, authors
A5090223147, A5133026759); Zenodo API (records 19599148, 23734444, 23093726, 22164948, 22153921); GitHub API
(users/aalsammani/repos); CV.pdf (updated October 25, 2026). Google Scholar could not be queried (automated access blocked).
