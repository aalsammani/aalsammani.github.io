# PENDING_UPDATES.md — Items awaiting the PI

Priority: 🔴 blocks a correct public site · 🟠 should be resolved soon · 🟢 optional

| # | Item | Default currently shipped | Action needed |
|---|---|---|---|
| 1 🔴 | **CV.pdf** — the project file named CV.pdf is a zip bundle, not a PDF. | A temporary raster PDF rebuilt from the 8 page images (works, but not text-searchable and ~1.2 MB). | Replace `CV.pdf` with the real vector export. |
| 2 🟢 | **Current students** — resolved 2026-09-03 (Jing Li, Uchenna J. Okorie, Fiona A. Ochieng). | Cards show name + degree level only. | Optional: supply research topics, start terms, and photos to enrich the cards. Add the Ph.D. students to the CV. |
| 3 🔴 | **Google Scholar URL** `citations?user=abdallah-alsammani` is not a valid Scholar ID format. | Kept (in header links, footer, Publications, Contact). | Send the 12-character `user=` ID; replace `SCHOLAR` in `_build/partials.py` and rebuild (or find-and-replace in HTML). |
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
| 15 🟢 | **ASCE link** for the Ubaka CRC 2026 paper could not be machine-verified (ascelibrary.org blocks bots). | Used as supplied. | Click it once on the live site. |
| 14 🟢 | Google Fonts could not be loaded in the review sandbox; Playfair/Source Sans rendering verified only by fallback. | — | Glance at the live site once deployed. |
