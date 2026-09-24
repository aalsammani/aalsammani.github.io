# WEBSITE_STYLE_GUIDE.md — Visual system (v6.0, September 2026)

Intent: restrained, typographic, scholarly. Hierarchy comes from type, whitespace, and hairline rules; colour is used sparingly.

## Tokens (assets/css/style.css §1)
| Token | Value | Use |
|---|---|---|
| --primary-blue | #294766 | Headings accents, primary buttons, footer, brand, top rules |
| --primary-blue-light | #315574 | Large call to action panel |
| --accent (muted teal) | #2E7D86 | Active nav underline, kicker, preprint label, project numerals, hover links, explorer controls |
| --text-primary / --text-secondary / --text-muted | #1F2933 / #4B5866 / #5F6C7A | Body / supporting / metadata (all ≥ 4.5:1 on white) |
| --background / --background-off / --surface | #FFFFFF / #F8F9FB / #F1F4F8 | Page, alternating sections, figure grounds |
| --border / --border-subtle | #D9DFE7 / #E7EBF0 | Rules |

## Type
Source Serif 4 (600) for h1–h3, hero identity line, publication titles, footer name. Source Sans 3 for everything else.
Scale: hero 52px · h1 44px · h2 34px · h3 22px · body 17px (16px ≤768px) · small 15px · meta 13px. Measure 68ch.

## Components (one job each)
hero · progression line · theme (top rule block) · domain pills · project (figure + title + question + tags + links) ·
news list · cta panel · page-header with on page nav · area (narrative + methods/representative work sidebar) · grants ·
resources list · pub (title / authors / venue / label / link chips) with year and status groupings · people list ·
projects (numbered) · mentee table · steps · principle · framework · resource panel · cv entry · contact list · audience list.
No card grids, no box shadows except the 1px portrait ring, no animation beyond 160ms colour transitions.

## Breakpoints
1024 (hero visual hidden, 2 col grids), 768 (mobile nav, single column), 480 (tight padding, full width buttons).

## Figures and interactivity (v6)
Static figures: inline SVG in `_build/figures.py`, navy/teal/gray only, every figure captioned and labeled synthetic where applicable.
Explorers: `.explorer` panel (title, note, plot, controls, live readout). Plots use a 640×360 viewBox with 56/16/16/44 margins, 12–13 px axis text, teal for the quantity of interest, gray/light for context, teal band at 18% for uncertainty. No animation except the hero draw in and the iEEG canvas, both off under reduced motion.
