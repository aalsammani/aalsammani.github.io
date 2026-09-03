# WEBSITE_STYLE_GUIDE.md — Visual system (v4.0)

Design intent: **calm, precise, mathematically serious.** Attractiveness comes from typography, composition,
whitespace, and a small number of scientific visuals — not decoration. One memorable element (the phase-portrait
hero visual + the numbered pillar system); everything else is quiet.

## 1. Colour tokens (`assets/css/style.css` §1)
| Token | Value | Use |
|---|---|---|
| `--navy-primary` | #1B3A4B | Header, tagline band, CTA panels, primary buttons, pub-year rules |
| `--navy-dark` | #12293A | Footer, mobile nav, primary-button hover |
| `--blue-accent` | #2980B0 | Timeline dots, pillar hover rule, focus ring, hero visual strokes |
| `--blue-accent-dark` | #1F6A93 | Links, roles, dates, small numerals (AA-safe on light backgrounds) |
| `--blue-light` | #5CB8E6 | Accent on dark backgrounds only (brand name, tagline second line, nav underline) |
| `--blue-wash` | #E3EEF6 | Figure backgrounds, icon tiles, avatars |
| `--background-primary` | #F4F6FA | Page ground |
| `--background-secondary` | #FFFFFF | Alternating sections, cards |
| `--background-tint` | #EAF0F6 | Tags |
| `--text-primary` | #1A2B3C | Headings, body |
| `--text-secondary` | #4A5F72 | Supporting text (6.1:1 on page ground) |
| `--text-muted` | #5E7082 | Metadata, captions (4.7:1) |
| `--border-subtle` / `--border` | #E1E7EE / #CBD5DF | Rules, card edges |

The five-colour accent set from v3 (teal, warm, gold, purple) was retired. One accent family only.

## 2. Typography
- **Playfair Display** (serif): name, h1, h2, h3 (pillars/projects/areas), publication titles, timeline institutions,
  pub-year labels, numerals in `.pub-summary`. Weights 500–700.
- **Source Sans 3** (sans): body, navigation, buttons, tags, metadata, table text, member/course names.
- Scale: 13 / 14.4 / 17 (base) / 18 / 21 / 26 / 34 / 44 px. Body 17px desktop, 16px ≤768px.
- Line length: `--measure: 66ch` on paragraphs; hero lede 60ch; page ledes 62ch.
- No all-caps tracked eyebrows; no monospace labels; no single-word colour accents inside headings.

## 3. Spacing & layout
- 8px scale: `--s-1`…`--s-9` (4 → 88px). Sections use `--s-9` (88px) desktop, `--s-8` (64px) mobile.
- Container 1120px (hero 1220px), 24px side padding (16px ≤480px).
- Alternating section grounds (page / white) with hairline borders separate major blocks.

## 4. Components (each has one job)
| Component | Class | Purpose |
|---|---|---|
| Hero | `.hero` | Portrait · identity · 90-word research statement · links · 3 CTAs · phase-portrait visual |
| Tagline band | `.tagline-band` | Navy band stating the program in one line |
| Research pillar | `.pillar` | 01–04 numbered, icon, 1–2 sentence summary, topics list, link |
| Project card | `.project` | Figure + title + summary + methods line + real links only |
| Timeline | `.timeline` | Horizontal 5-step academic journey; vertical ≤1024px |
| News list | `.news` | Date + title + one line; not cards |
| CTA panel | `.cta-panel` | Navy panel with two buttons, ends Home and Research |
| Page header | `.page-header` | h1 + lede + optional on-page pill nav (+ visual on Research) |
| Research area | `.area` | Number · title · lead · open questions · methods tags · representative work |
| Publication | `.pub` | Serif title, authors (PI marked), subdued venue, type label, DOI/arXiv chips |
| Member card | `.member` | Initials/photo avatar, name, role, topic |
| Course block | `.course-block` | Institution + tabular course list |
| CV entry | `.cv-entry` | When · what · where · note |

Border radius: 4 (chips) / 8 (buttons, tiles) / 12 (cards, panels). Shadows: sm/md/lg, navy-tinted, used only on
hover elevation and the hero portrait.

## 5. Interaction
- Cards lift 3px + `--shadow-md` on hover; pillars grow a 3px top rule; buttons lift 1px.
- Links: colour change + underline on hover; arrow links slide the arrow 3px.
- Reveal: `.reveal` fades/slides 14px once when 8% visible. Disabled under `prefers-reduced-motion`.
- Focus: 2px `--blue-accent` outline, 3px offset, everywhere.

## 6. Scientific visuals
All inline SVG, generated or hand-drawn, using only the palette above:
- Hero / Research header: phase portrait (spiral sink, vector field, one uncertainty band, sampled points).
- Featured figures: SIR-with-learned-rate diagram; two-scenario epidemic curves; iEEG trace with HFO events.
- Pillar icons: 40px line icons (curve, graph+curve, EHR grid+ECG, EEG trace).
Avoid: brains, robots, circuit boards, stock medical photos, DNA helices.

## 7. Breakpoints
1180 (hero tightens) · 1024 (visual hidden, pillars 2-col, timeline vertical, CV TOC inline) · 768 (mobile nav,
single columns, hero centred) · 480 (tighter padding, full-width buttons).
