# PENDING_UPDATES.md — Items awaiting the PI

Priority: 🔴 blocks a correct public site · 🟠 should be resolved soon · 🟢 optional

| # | Item | Default currently shipped | Action needed |
|---|---|---|---|
| 1 ✅ | **CV.pdf** — resolved: the current file is a 9-page, text-searchable LaTeX export updated October 25, 2026 (verified 2026-11-06). | — | Re-export after the JIFS acceptance so the CV lists it. |
| 2 🟢 | **Current students** — resolved 2026-09-03 (Jing Li, Uchenna J. Okorie, Fiona A. Ochieng). | Cards show name + degree level only. | Optional: supply research topics, start terms, and photos to enrich the cards. Add the Ph.D. students to the CV. |
| 3 🔴 | **Google Scholar URL** `citations?user=abdallah-alsammani` is not a valid Scholar ID format (Scholar blocks automated lookup). | Since 2026-11-06 the link opens a Scholar author search for “Abdallah Alsammani”. | Send the 12-character `user=` ID; set it in `PROFILES` in `_build/build.py` and rebuild. |
| 4 ✅ | **ORCID** — resolved 2026-09-03: 0000-0003-4340-4550 (from the medRxiv record). | Added to header links, footer, JSON-LD. | Confirm it is yours (it is the submitter ORCID on the ICU preprint). |
| 5 🟠 | **Sudan lecturer dates** — CV p.1 says Aug 2012–Aug 2013; CV p.6 says 2010–2013. | 2012–2013 shown on cv.html; teaching.html shows no dates. | Confirm; fix the CV too. |
| 6 🟠 | **Assessment Coordinator** end date — CV says "2022–Present" but JU appointment ended July 2025. | 2022–2025 shown. | Confirm. |
| 7 🟠 | **Unfunded grants** (NIH R21 2024; IHER Pilot 2026; INBRE Pilot 2026) — CV lists them under "Unfunded". | Omitted. | Confirm omission, or say if you want a "Submitted" list. |
| 8 🟢 | **Group name** — old site branded "AMDS Lab"; not in CV. | "Applied Mathematics & Data Science group". | Confirm preferred name/acronym. |
| 9 🟢 | **Collaborators section** — old site listed collaborators with affiliations not in the CV. | Omitted. | Provide a verified list (name, affiliation, link) if you want it back. |
| 10 🟢 | **Member photos** — none available. | Initials avatars. | Provide square headshots (≥400×400) to replace avatars. |
| 11 🟢 | **Real scientific figures** — Featured Research uses schematic SVGs drawn for the site. | Schematics. | Provide publication figures (with rights) to swap in. |
| 12 🟢 | **Site URL** assumed `https://aalsammani.github.io`. | Used in canonical/OG/sitemap. | Confirm or provide custom domain. |
| 13 🟢 | **Office address** 1200 N. DuPont Highway carried over from old contact page; room/building not known. | Main campus address. | Add building/room if desired. |
| 16 ✅ | **(Resolved 2026-11-06: linked to https://aalsammani.github.io/calculus-4-DS/ and the GitHub repo.)** Calculus and Matrix Methods for Data Science — requested as a featured open educational project, but no URL or description exists in the source files, on the live site, or via web search. | Not shown. | Send the URL (repository or site) and a one sentence description; add it to `_data/resources.json`. |
| 17 🟢 | **Research figures** — no publication figures exist in the repository; Featured Research uses schematic SVGs drawn for the site. | Schematics. | Provide figures (with rights) as PNG/SVG in `assets/img/` and point `_data/featured.json` at them. |
| 18 ✅ | **(Resolved 2026-11-06: identifiability package, ML Selection Framework, SIRA linked.)** Code repositories — no repository is linked from the site; GitHub's API was rate limited during the audit. | Resources section links to the GitHub profile only. | Add specific repositories (identifiability tutorial code, ICU model) to `_data/resources.json`. |
| 19 ✅ | **(Resolved 2026-11-06: doi:10.35542/osf.io/vsjhe_v2.)** EdArXiv companion paper — cited on Teaching without a link; no URL was supplied. | Text only. | Provide the EdArXiv URL/DOI. |
| 15 🟢 | **ASCE link** for the Ubaka CRC 2026 paper could not be machine-verified (ascelibrary.org blocks bots). | Used as supplied. | Click it once on the live site. |
| 14 🟢 | Google Fonts could not be loaded in the review sandbox; Playfair/Source Sans rendering verified only by fallback. | — | Glance at the live site once deployed. |

## Added 2026-11-06 (v7.1 audit)
| # | Item | Default currently shipped | Action needed |
|---|---|---|---|
| 20 🟠 | **JIFS article** — accepted Nov 5, 2026; no DOI, volume, or pages exist yet. | "Accepted (in press)", journal name only. | When it appears online: remove `"status": "accepted"`, add the DOI and citation in `_data/publications.json`, add a news item, rebuild. |
| 21 🟠 | **Low-rank compression preprint** (SSRN 7293357; with J. Li, L. Liu, C. Ndeke, U. Okorie) is on ORCID but not on the CV. | Listed as a preprint. | Confirm it should be public; add it to the CV. Note: C. Ndeke appears only as a co-author (not on the Group page, per item from v4.1). |
| 22 🟢 | **CV** does not yet list the JIFS acceptance, the low-rank preprint, the EdArXiv preprint, or Ph.D. students J. Li and U. J. Okorie; it still gives the old arXiv titles for 2505.08873 and 2308.05819. | Site follows the verified external records. | Update the CV and re-upload CV.pdf. |
| 23 🟢 | **AES 2025 and AI in Epilepsy 2026 abstracts** — taken from the CV; no public abstract URL found. | Listed without links. | Send links if available. |
| 24 🟢 | **ICU mortality paper** — medRxiv shows no published version (checked 2026-11-06). | Preprint. | Update only when a journal acceptance or publication is public. |
| 25 🟢 | **`.nojekyll`** — earlier docs said it exists; it does not. GitHub Pages runs Jekyll, which (usefully) does not publish `_data/` and `_build/`. All `*.md` files at the root, including this one, ARE publicly served. | Unchanged. | Keep as is unless you prefer to hide the maintenance notes. |
