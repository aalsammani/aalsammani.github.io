# -*- coding: utf-8 -*-
"""Shared partials for the Alsammani site generator.
Run build.py to regenerate the seven HTML pages from these partials + content.
The generated HTML is what gets deployed; this folder is optional tooling.
"""
import math

SITE_URL = "https://aalsammani.github.io"
NAME = "Abdallah Alsammani"
EMAIL = "aalsammani@desu.edu"
PHONE = "302.857.6642"
GITHUB = "https://github.com/aalsammani"
LINKEDIN = "https://www.linkedin.com/in/abdallah-alsammani/"
# Google Scholar ID is UNVERIFIED (see PENDING_UPDATES.md). Kept from previous site.
# ORCID verified from the medRxiv record 10.64898/2026.05.30.26354524 (submitter ORCID).
ORCID = "https://orcid.org/0000-0003-4340-4550"
SCHOLAR = "https://scholar.google.com/citations?user=abdallah-alsammani"

NAV = [
    ("index.html", "Home"),
    ("research.html", "Research"),
    ("publications.html", "Publications"),
    ("group.html", "Research Group"),
    ("teaching.html", "Teaching"),
    ("cv.html", "CV"),
    ("contact.html", "Contact"),
]

# ---------------------------------------------------------------- icon sprite
ICONS = """
<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">
  <symbol id="i-mail" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></symbol>
  <symbol id="i-scholar" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 9.5 12 4l10 5.5-10 5.5L2 9.5Z"/><path d="M6 12v4.5c0 1.5 3 3 6 3s6-1.5 6-3V12"/><path d="M22 9.5V15"/></symbol>
  <symbol id="i-orcid" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0a12 12 0 1 0 0 24 12 12 0 0 0 0-24ZM7.4 5.6a1 1 0 1 1 0 2 1 1 0 0 1 0-2Zm.8 3.2h1.5v8.6H8.2V8.8Zm3 0h3.7c3.5 0 5 2.5 5 4.3 0 2.2-1.7 4.3-5 4.3h-3.7V8.8Zm1.5 1.4v5.8h2.2c3 0 3.5-2.2 3.5-2.9 0-1.6-1-2.9-3.6-2.9h-2.1Z"/></symbol>
  <symbol id="i-github" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .5A11.5 11.5 0 0 0 8.36 22.9c.58.1.79-.25.79-.56v-2c-3.2.7-3.88-1.37-3.88-1.37-.52-1.33-1.28-1.68-1.28-1.68-1.05-.72.08-.7.08-.7 1.16.08 1.77 1.19 1.77 1.19 1.03 1.77 2.7 1.26 3.36.96.1-.75.4-1.26.73-1.55-2.56-.29-5.25-1.28-5.25-5.7 0-1.26.45-2.29 1.19-3.1-.12-.29-.52-1.46.11-3.05 0 0 .97-.31 3.17 1.18a11 11 0 0 1 5.77 0c2.2-1.49 3.17-1.18 3.17-1.18.63 1.59.23 2.76.11 3.05.74.81 1.19 1.84 1.19 3.1 0 4.43-2.7 5.4-5.27 5.69.41.36.78 1.06.78 2.14v3.17c0 .31.21.67.8.56A11.5 11.5 0 0 0 12 .5Z"/></symbol>
  <symbol id="i-linkedin" viewBox="0 0 24 24" fill="currentColor"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.13 1.45-2.13 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28ZM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13ZM7.12 20.45H3.56V9h3.56v11.45ZM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0Z"/></symbol>
  <symbol id="i-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></symbol>
  <symbol id="i-ext" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 4h6v6M20 4l-9 9M19 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h5"/></symbol>
  <symbol id="i-download" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v11M7 10l5 5 5-5M4 19h16"/></symbol>
  <symbol id="i-phone" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A17 17 0 0 1 3 5a2 2 0 0 1 2-2Z"/></symbol>
  <symbol id="i-pin" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s7-6.5 7-11.5a7 7 0 0 0-14 0C5 14.5 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.5"/></symbol>
  <symbol id="i-building" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 21V5a1 1 0 0 1 1-1h9a1 1 0 0 1 1 1v16M15 9h4a1 1 0 0 1 1 1v11M2 21h20M8 8h2M8 12h2M8 16h2"/></symbol>
  <symbol id="i-award" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="9" r="6"/><path d="m8.5 14-1.5 7 5-3 5 3-1.5-7"/></symbol>
  <symbol id="i-users" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><circle cx="17" cy="9" r="2.5"/><path d="M15.5 14.5a5 5 0 0 1 6 5"/></symbol>
</svg>
"""

def icon(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<svg{c} width="16" height="16" aria-hidden="true" focusable="false"><use href="#{name}"/></svg>'


# ------------------------------------------------------------ pillar icons
PILLAR_ICONS = {
    "modeling": """<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 33h30M7 35V6"/><path d="M8 30c4-1 6-18 10-18s6 12 10 12 6-6 8-8" /><circle cx="18" cy="12" r="1.6" fill="currentColor" stroke="none"/><circle cx="28" cy="24" r="1.6" fill="currentColor" stroke="none"/></svg>""",
    "sciml": """<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="8" cy="12" r="2.5"/><circle cx="8" cy="28" r="2.5"/><circle cx="20" cy="20" r="2.5"/><circle cx="32" cy="12" r="2.5"/><circle cx="32" cy="28" r="2.5"/><path d="M10.2 13.2 17.8 18.8M10.2 26.8l7.6-5.6M22.2 18.8l7.6-5.6M22.2 21.2l7.6 5.6"/><path d="M4 36c6-10 26-10 32 0" stroke-dasharray="2.5 2.5"/></svg>""",
    "biomed": """<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="6" width="30" height="28" rx="3"/><path d="M5 14h30M15 14v20M25 14v20"/><path d="M8 26h3l2-5 3 8 2-4h4" stroke-width="1.8"/></svg>""",
    "neuro": """<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 20h5l2-4 2 8 2-12 2 16 2-10 2 6 2-4h3"/><path d="M26 20h2l1-2 1 4 1-6 1 8 1-4h4" stroke-width="1.2" opacity=".7"/><path d="M3 32h34" opacity=".4"/></svg>""",
}


# ------------------------------------------------------------ hero visual
def hero_svg():
    """Phase portrait: spiral trajectories converging to a stable focus, with a
    faint vector field and a shaded uncertainty band on one trajectory."""
    W = H = 360
    cx, cy = 180, 182
    parts = []
    parts.append(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="hero-viz-t">')
    parts.append('<title id="hero-viz-t">Phase portrait of a dynamical system: trajectories spiral toward a stable equilibrium</title>')
    parts.append('<defs><radialGradient id="hg" cx="50%" cy="50%" r="55%"><stop offset="0" stop-color="#2980B0" stop-opacity=".10"/><stop offset="1" stop-color="#2980B0" stop-opacity="0"/></radialGradient></defs>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="172" fill="url(#hg)"/>')
    # faint grid
    g = ['<g stroke="#1B3A4B" stroke-opacity=".07" stroke-width="1">']
    for i in range(20, W, 40):
        g.append(f'<line x1="{i}" y1="18" x2="{i}" y2="{H-18}"/>')
        g.append(f'<line x1="18" y1="{i}" x2="{W-18}" y2="{i}"/>')
    g.append('</g>')
    parts.append("".join(g))
    # vector field ticks
    vf = ['<g stroke="#1B3A4B" stroke-opacity=".22" stroke-width="1.1" stroke-linecap="round">']
    for gx in range(40, W, 40):
        for gy in range(40, H, 40):
            x, y = (gx - cx) / 60.0, (gy - cy) / 60.0
            # spiral sink: dx = -0.35x - y ; dy = x - 0.35y
            dx, dy = -0.35 * x - y, x - 0.35 * y
            n = math.hypot(dx, dy) or 1
            dx, dy = dx / n * 7, dy / n * 7
            vf.append(f'<line x1="{gx-dx/2:.1f}" y1="{gy-dy/2:.1f}" x2="{gx+dx/2:.1f}" y2="{gy+dy/2:.1f}"/>')
    vf.append('</g>')
    parts.append("".join(vf))

    def spiral(r0, phase, decay=0.16, tmax=13.5, step=0.08):
        pts = []
        t = 0.0
        while t <= tmax:
            r = r0 * math.exp(-decay * t)
            pts.append((cx + r * math.cos(t + phase), cy + r * math.sin(t + phase)))
            t += step
        return pts

    def path(pts):
        return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)

    # uncertainty band around one trajectory
    band = spiral(150, 2.3)
    inner = spiral(138, 2.3)
    band_d = path(band) + " L" + " L".join(f"{x:.1f},{y:.1f}" for x, y in reversed(inner)) + " Z"
    parts.append(f'<path d="{band_d}" fill="#5CB8E6" fill-opacity=".16"/>')

    specs = [(160, 0.0, "#1B3A4B", .85, 1.7), (150, 2.3, "#2980B0", .9, 1.8), (165, 4.1, "#1B3A4B", .55, 1.3), (120, 1.2, "#2980B0", .5, 1.1)]
    for r0, ph, col, op, sw in specs:
        parts.append(f'<path d="{path(spiral(r0, ph))}" fill="none" stroke="{col}" stroke-opacity="{op}" stroke-width="{sw}" stroke-linecap="round"/>')
    # sample points on the second trajectory
    for k, (x, y) in enumerate(spiral(150, 2.3, step=0.5)):
        if k % 2 == 0 and k < 22:
            parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" fill="#fff" stroke="#2980B0" stroke-width="1.4"/>')
    # equilibrium
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="4.5" fill="#1B3A4B"/><circle cx="{cx}" cy="{cy}" r="9" fill="none" stroke="#1B3A4B" stroke-opacity=".35"/>')
    # equation label
    parts.append('<text x="30" y="40" font-family="Playfair Display, Georgia, serif" font-style="italic" font-size="15" fill="#1B3A4B" fill-opacity=".75">dx/dt = f(x, θ) + g(x; φ)</text>')
    parts.append('<text x="30" y="58" font-family="Source Sans 3, sans-serif" font-size="11" fill="#4A5F72" fill-opacity=".8">mechanistic model + learned component</text>')
    parts.append('</svg>')
    return "".join(parts)


# ---------------------------------------------------- featured project figures
FIG_HYBRID = """<svg viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Diagram: compartmental model with a learned rate term, and structural identifiability check">
<g font-family="Source Sans 3, sans-serif" font-size="11" fill="#1B3A4B">
<rect x="22" y="70" width="52" height="34" rx="6" fill="#fff" stroke="#1B3A4B" stroke-width="1.4"/><text x="48" y="92" text-anchor="middle" font-weight="600">S</text>
<rect x="124" y="70" width="52" height="34" rx="6" fill="#fff" stroke="#1B3A4B" stroke-width="1.4"/><text x="150" y="92" text-anchor="middle" font-weight="600">I</text>
<rect x="226" y="70" width="52" height="34" rx="6" fill="#fff" stroke="#1B3A4B" stroke-width="1.4"/><text x="252" y="92" text-anchor="middle" font-weight="600">R</text>
<path d="M74 87h44M176 87h44" stroke="#1B3A4B" stroke-width="1.4"/><path d="M114 83l6 4-6 4M216 83l6 4-6 4" fill="none" stroke="#1B3A4B" stroke-width="1.4"/>
<text x="96" y="80" text-anchor="middle" font-style="italic" font-size="11" fill="#2980B0">β(t)</text>
<text x="198" y="80" text-anchor="middle" font-style="italic" font-size="11">γ</text>
<g stroke="#2980B0" stroke-width="1.2" fill="#fff"><circle cx="82" cy="32" r="4"/><circle cx="82" cy="46" r="4"/><circle cx="96" cy="39" r="4"/><circle cx="110" cy="32" r="4"/><circle cx="110" cy="46" r="4"/></g>
<g stroke="#2980B0" stroke-width=".9" stroke-opacity=".6"><path d="M86 32l6 7M86 46l6-7M100 39l6-7M100 39l6 7"/></g>
<path d="M96 52v20" stroke="#2980B0" stroke-width="1.2" stroke-dasharray="3 2"/>
<text x="126" y="42" font-size="10" fill="#2980B0">learned rate</text>
<text x="22" y="150" font-size="11" fill="#4A5F72">Identifiability:</text>
<text x="110" y="150" font-size="11">β, γ</text><text x="140" y="150" font-size="11" fill="#1B3A4B">globally identifiable</text>
<text x="110" y="168" font-size="11">N</text><text x="140" y="168" font-size="11" fill="#4A5F72">fixed from data</text>
<path d="M26 156h268" stroke="#1B3A4B" stroke-opacity=".12"/>
</g></svg>"""

FIG_EPI = """<svg viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Chart: infection curves under high and low vaccination uptake, with an economic output curve">
<g font-family="Source Sans 3, sans-serif" font-size="10" fill="#4A5F72">
<path d="M34 24v144h240" stroke="#1B3A4B" stroke-opacity=".35" fill="none"/>
<path d="M34 168h240" stroke="#1B3A4B" stroke-opacity=".1"/><path d="M34 120h240M34 72h240" stroke="#1B3A4B" stroke-opacity=".07"/>
<path d="M36 164C70 160,90 100,120 78S170 60,200 110S240 156,272 164" fill="none" stroke="#1B3A4B" stroke-width="2"/>
<path d="M36 164C72 162,96 140,124 128S170 118,200 140S244 160,272 165" fill="none" stroke="#2980B0" stroke-width="2"/>
<path d="M36 60C80 62,120 92,150 96S220 84,272 74" fill="none" stroke="#5CB8E6" stroke-width="1.5" stroke-dasharray="4 3"/>
<text x="40" y="20">infections</text><text x="230" y="184">time</text>
<g transform="translate(150 24)"><rect width="122" height="40" rx="5" fill="#fff" stroke="#1B3A4B" stroke-opacity=".15"/>
<path d="M8 12h14" stroke="#1B3A4B" stroke-width="2"/><text x="27" y="15">low vaccination</text>
<path d="M8 25h14" stroke="#2980B0" stroke-width="2"/><text x="27" y="28">high vaccination</text>
<path d="M8 36h14" stroke="#5CB8E6" stroke-width="1.5" stroke-dasharray="4 3"/></g>
</g></svg>"""

FIG_IEEG = """<svg viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Diagram: intracranial EEG trace with detected high-frequency oscillations across wake and sleep states">
<g font-family="Source Sans 3, sans-serif" font-size="10" fill="#4A5F72">
<rect x="24" y="34" width="60" height="110" fill="#1B3A4B" fill-opacity=".04"/><rect x="84" y="34" width="86" height="110" fill="#2980B0" fill-opacity=".10"/><rect x="170" y="34" width="46" height="110" fill="#1B3A4B" fill-opacity=".04"/><rect x="216" y="34" width="62" height="110" fill="#2980B0" fill-opacity=".10"/>
<text x="54" y="48" text-anchor="middle">wake</text><text x="127" y="48" text-anchor="middle" fill="#1B3A4B" font-weight="600">NREM</text><text x="193" y="48" text-anchor="middle">wake</text><text x="247" y="48" text-anchor="middle" fill="#1B3A4B" font-weight="600">NREM</text>
<path d="M24 80q4-8 8 0t8 0 8-6 8 6 8 0 8-10 8 10 8 0 8-4 8 4 8 0 8-12 8 12 8 0 8-6 8 6 8 0 8-3 8 3 8 0 8-9 8 9 8 0 8-5 8 5 8 0 8-11 8 11 8 0 8-4 8 4" fill="none" stroke="#1B3A4B" stroke-width="1.1" stroke-opacity=".75"/>
<g stroke="#2980B0" stroke-width="1.8" stroke-linecap="round">
<path d="M40 114v14M62 114v14"/>
<path d="M90 108v20M98 108v20M108 108v20M116 108v20M126 108v20M134 108v20M146 108v20M156 108v20"/>
<path d="M182 114v14M204 114v14"/>
<path d="M222 108v20M232 108v20M240 108v20M250 108v20M260 108v20M270 108v20"/>
</g>
<text x="24" y="160">HFO events</text><text x="150" y="182" text-anchor="middle">recording duration →</text>
<path d="M24 144h254" stroke="#1B3A4B" stroke-opacity=".25"/>
</g></svg>"""

# ------------------------------------------------------------ page chrome
def head(title, desc, canonical, extra_ld=""):
    ld = f"""
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Abdallah Alsammani",
  "honorificSuffix": "Ph.D.",
  "jobTitle": "Assistant Professor of Mathematics and Data Science",
  "worksFor": {{"@type": "CollegeOrUniversity", "name": "Delaware State University", "department": "Department of Mathematical Sciences"}},
  "email": "mailto:{EMAIL}",
  "telephone": "+1-302-857-6642",
  "url": "{SITE_URL}/",
  "image": "{SITE_URL}/assets/img/profile.jpg",
  "sameAs": ["{ORCID}", "{GITHUB}", "{LINKEDIN}"],
  "alumniOf": [
    {{"@type": "CollegeOrUniversity", "name": "Auburn University"}},
    {{"@type": "CollegeOrUniversity", "name": "International Centre for Theoretical Physics"}},
    {{"@type": "CollegeOrUniversity", "name": "African Institute for Mathematical Sciences"}},
    {{"@type": "CollegeOrUniversity", "name": "Al Neelain University"}}
  ],
  "knowsAbout": ["Mathematical modeling", "Scientific machine learning", "Biomedical data science", "Computational neuroscience", "Mathematical epidemiology", "Dynamical systems", "Optimal control"]
}}
</script>""" if extra_ld == "person" else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="{NAME}">
<link rel="canonical" href="{SITE_URL}/{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE_URL}/{canonical}">
<meta property="og:image" content="{SITE_URL}/assets/img/profile.jpg">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#1B3A4B">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&family=Source+Sans+3:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">{ld}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
{ICONS}"""


def header(current):
    links = "".join(
        f'<li{" class=nav__cta" if href=="contact.html" else ""}><a href="{href}"{" aria-current=page" if href==current else ""}>{label}</a></li>'
        for href, label in NAV)
    mlinks = "".join(f'<a href="{href}"{" aria-current=page" if href==current else ""}>{label}</a>' for href, label in NAV)
    return f"""
<header class="site-header">
  <div class="container">
    <a class="brand" href="index.html" aria-label="Abdallah Alsammani — home">
      <span class="brand__name">Abdallah <span>Alsammani</span></span><span class="brand__sub">Ph.D.</span>
    </a>
    <nav aria-label="Primary">
      <ul class="nav">{links}</ul>
    </nav>
    <button class="nav-toggle" aria-expanded="false" aria-controls="mobile-nav" aria-label="Open menu"><span></span></button>
  </div>
</header>
<nav class="mobile-nav" id="mobile-nav" hidden aria-label="Mobile">{mlinks}</nav>
<main id="main">"""


def social_links(cls="icon-links"):
    return f"""<div class="{cls}">
  <a href="mailto:{EMAIL}" aria-label="Email">{icon('i-mail')}</a>
  <a href="{SCHOLAR}" target="_blank" rel="noopener" aria-label="Google Scholar">{icon('i-scholar')}</a>
  <a href="{ORCID}" target="_blank" rel="noopener" aria-label="ORCID">{icon('i-orcid')}</a>
  <a href="{GITHUB}" target="_blank" rel="noopener" aria-label="GitHub">{icon('i-github')}</a>
  <a href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="LinkedIn">{icon('i-linkedin')}</a>
</div>"""


def footer():
    return f"""</main>
<footer class="site-footer">
  <div class="container">
    <div>
      <h3>Abdallah Alsammani, Ph.D.</h3>
      <p>Assistant Professor of Mathematics and Data Science<br>Department of Mathematical Sciences<br>Delaware State University<br>1200 N. DuPont Highway, Dover, DE 19901</p>
    </div>
    <div>
      <h3>Site</h3>
      <ul>
        <li><a href="research.html">Research</a></li>
        <li><a href="publications.html">Publications</a></li>
        <li><a href="group.html">Research Group</a></li>
        <li><a href="teaching.html">Teaching</a></li>
        <li><a href="cv.html">Curriculum Vitae</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </div>
    <div>
      <h3>Connect</h3>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a><br>{PHONE}</p>
      <br>
      {social_links()}
    </div>
    <div class="site-footer__bottom">
      <span>© 2026 Abdallah Alsammani</span>
      <span>Mathematical &amp; Scientific Machine Learning for Biomedical Systems</span>
    </div>
  </div>
</footer>
<script src="assets/js/main.js" defer></script>
</body>
</html>
"""
