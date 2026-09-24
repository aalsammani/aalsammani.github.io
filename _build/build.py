# -*- coding: utf-8 -*-
"""Site generator, v7.0. Run from the site root:  python3 _build/build.py
Content lives in _data/*.json; page chrome and prose live here. Output: the seven
HTML files in the site root, which are what GitHub Pages serves."""
import os, sys, json, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..')
sys.path.insert(0, HERE)
from figures import ICONS, hero_svg, FIG_HYBRID, FIG_EPI, FIG_IEEG, FIG_UQ, FIG_NODE, ANIM_MODELING, ANIM_SCIML, ANIM_BIOMED, ANIM_NEURO

SITE = "https://aalsammani.github.io"
EMAIL = "aalsammani@desu.edu"
PROFILES = {  # verified URLs only (see CONTENT_VERIFICATION.md)
    "Google Scholar": ("i-scholar", "https://scholar.google.com/citations?user=abdallah-alsammani"),
    "ORCID": ("i-orcid", "https://orcid.org/0000-0003-4340-4550"),
    "GitHub": ("i-github", "https://github.com/aalsammani"),
    "LinkedIn": ("i-linkedin", "https://www.linkedin.com/in/abdallah-alsammani/"),
}
NAV = [("index.html", "Home"), ("research.html", "Research"), ("publications.html", "Publications"),
       ("group.html", "Group"), ("teaching.html", "Teaching"), ("cv.html", "CV"), ("contact.html", "Contact")]
AREA_LABEL = {"dynsys": "Dynamical Systems", "sciml": "Scientific ML", "biomed": "Biomedical Data Science", "neuro": "Neuroscience", "other": "Other Applications"}
TYPE_LABEL = {"journal": "Journal article", "conference": "Conference paper", "preprint": "Preprint", "abstract": "Conference abstract", "other": "Dissertation"}
FIGS = {"identifiability": FIG_HYBRID, "epidemic": FIG_EPI, "hfo": FIG_IEEG}

def load(n): return json.load(open(os.path.join(ROOT, '_data', n + '.json'), encoding='utf-8'))
PUBS, NEWS, PEOPLE, FEATURED, RESOURCES = load('publications'), load('news'), load('people'), load('featured'), load('resources')

def icon(n): return f'<svg width="16" height="16" aria-hidden="true" focusable="false"><use href="#{n}"/></svg>'
def me(a): return re.sub(r"\*\*(.+?)\*\*", r'<span class="me">\1</span>', a)
def ext(u): return ' target="_blank" rel="noopener"' if u.startswith('http') else ''

def profile_links():
    return '<div class="icon-links">' + ''.join(f'<a href="{u}"{ext(u)}>{icon(i)}{name}</a>' for name, (i, u) in PROFILES.items()) + '</div>'

def head(title, desc, canonical, person=False):
    ld = ""
    if person:
        same = ", ".join(f'"{u}"' for _, (_, u) in PROFILES.items() if 'scholar' not in u)
        ld = f'''
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Person","name":"Abdallah Alsammani","honorificSuffix":"Ph.D.",
 "jobTitle":"Assistant Professor of Mathematics and Data Science",
 "worksFor":{{"@type":"CollegeOrUniversity","name":"Delaware State University","department":"Department of Mathematical Sciences"}},
 "email":"mailto:{EMAIL}","url":"{SITE}/","image":"{SITE}/assets/img/profile.jpg","sameAs":[{same}],
 "alumniOf":[{{"@type":"CollegeOrUniversity","name":"Auburn University"}}],
 "knowsAbout":["Dynamical systems","Stochastic modeling","Structural identifiability","Scientific machine learning","Uncertainty quantification","Biomedical data science","Computational neuroscience","Mathematical epidemiology"]}}
</script>'''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="Abdallah Alsammani">
<link rel="canonical" href="{SITE}/{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}/{canonical}">
<meta property="og:image" content="{SITE}/assets/img/profile.jpg">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#294766">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,600;1,8..60,600&family=Source+Sans+3:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">{ld}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
{ICONS}
<header class="site-header">
  <div class="container">
    <a class="brand" href="index.html">Abdallah Alsammani</a>
    <nav aria-label="Primary"><ul class="nav">{''.join(f'<li><a href="{h}"{" aria-current=page" if h==canonical else ""}>{l}</a></li>' for h,l in NAV)}</ul></nav>
    <button class="nav-toggle" aria-expanded="false" aria-controls="mobile-nav" aria-label="Open menu"><span></span></button>
  </div>
</header>
<nav class="mobile-nav" id="mobile-nav" hidden aria-label="Mobile">{''.join(f'<a href="{h}"{" aria-current=page" if h==canonical else ""}>{l}</a>' for h,l in NAV)}</nav>
<main id="main">'''

FOOT = f'''</main>
<footer class="site-footer">
  <div class="container">
    <div><strong>Abdallah Alsammani, Ph.D.</strong>Department of Mathematical Sciences, Delaware State University<br><a href="mailto:{EMAIL}">{EMAIL}</a></div>
    <div class="links">{''.join(f'<a href="{u}"{ext(u)}>{name}</a>' for name,(i,u) in PROFILES.items())}<a href="CV.pdf">CV (PDF)</a></div>
    <div class="copy">© 2026 Abdallah Alsammani</div>
  </div>
</footer>
<script src="assets/js/main.js" defer></script>
</body>
</html>
'''

def page(canonical, title, desc, body, person=False, scripts=()):
    extra = ''.join(f'<script src="{x}" defer></script>\n' for x in scripts)
    open(os.path.join(ROOT, canonical), 'w', encoding='utf-8').write(head(title, desc, canonical, person) + body + FOOT.replace('<script src="assets/js/main.js" defer></script>\n', '<script src="assets/js/main.js" defer></script>\n' + extra)); print('wrote', canonical)

def page_header(h1, lede, nav=None):
    n = f'<nav class="on-page" aria-label="On this page">{"".join(f"<a href=#{a}>{t}</a>" for a,t in nav)}</nav>' if nav else ''
    return f'<section class="page-header"><div class="container"><h1>{h1}</h1><p class="page-header__lede">{lede}</p>{n}</div></section>'

def pub_item(p):
    links = ''.join(f'<a href="{u}"{ext(u)}>{l}</a>' for l, u in p['links'].items())
    lab = f'<span class="label label--preprint">Preprint</span>' if p['type'] == 'preprint' else f'<span class="label">{TYPE_LABEL[p["type"]]}</span>'
    return f'''
    <article class="pub" data-areas="{' '.join(p['areas'])}" data-type="{p['type']}">
      <div><h3 class="pub__title">{p['title']}</h3><p class="pub__authors">{me(p['authors'])} ({p['year']}).</p><p class="pub__venue">{p['venue']}</p></div>
      <div class="pub__side">{lab}{f'<div class="pub__links">{links}</div>' if links else ''}</div>
    </article>'''

# ============================================================ HOME
feat = ''.join(f'''
    <article class="project">
      <div class="project__figure">{FIGS[f['figure']]}</div>
      <h3>{f['title']}</h3><p>{f['question']}</p>
      <div class="tags">{''.join(f'<span class="tag">{t}</span>' for t in f['tags'])}</div>
      <div class="project__links">{''.join(f'<a href="{u}"{ext(u)}>{l} →</a>' for l,u in f['links'].items())}</div>
    </article>''' for f in FEATURED)
home_news = [n for n in NEWS if n.get('home')][:3]
news_html = ''.join(f'<li><span class="news__date">{n["date"]}</span><div><div class="news__title">{f"<a href={chr(34)}{n['url']}{chr(34)}{ext(n['url'])}>{n['title']}</a>" if n.get('url') else n['title']}</div>{f"<p class=news__text>{n['text']}</p>" if n.get('text') else ''}</div></li>' for n in home_news)
arrow = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

def pillar(pid, num, title, anim, summary, questions, tags, pubs, section):
    q=''.join(f'<li>{x}</li>' for x in questions); tg=''.join(f'<span class="tag">{x}</span>' for x in tags)
    pb=''.join(f'<li><a href="{u}"{ext(u)}>{t}</a> <span class="muted">· {m}</span></li>' for t,m,u in pubs)
    return f"""
    <article class="pillar" id="pillar-{pid}">
      <div class="pillar__anim">{anim}</div>
      <div class="pillar__num">{num}</div>
      <h3>{title}</h3>
      <p>{summary}</p>
      <button class="pillar__toggle" type="button" aria-expanded="false" aria-controls="pd-{pid}">Explore</button>
      <div class="pillar__detail" id="pd-{pid}" hidden>
        <h4>Questions</h4><ul>{q}</ul>
        <h4>Methods</h4><div class="tags">{tg}</div>
        <h4>Selected work</h4><ul>{pb}</ul>
        <a class="link-arrow" href="research.html#{section}">More on the Research page {arrow}</a>
      </div>
    </article>"""

pillars_html = (
  pillar("modeling","01","Mathematical Modeling",ANIM_MODELING,
    "Deterministic, stochastic, delayed, and fractional order models of infectious disease and biological processes, analyzed with stability, bifurcation, and optimal control theory.",
    ["How do seasonality, random fluctuation, and delay change the long term behavior of an infection model?","Which vaccination, treatment, or sanitation strategies are optimal, and how sensitive are they to human behavior?"],
    ["ODE, SDE, delay systems","Basic reproduction number","Lyapunov stability","Optimal control","Fractional calculus"],
    [("Vaccination behavior, COVID-19 dynamics, and economic outcomes","MBE, 2025","https://doi.org/10.3934/mbe.2025084"),("Mittag-Leffler stability of Caputo fractional systems with delays","arXiv, 2026","https://arxiv.org/abs/2602.07105"),("Cholera transmission with sanitation controls","arXiv, 2025","https://arxiv.org/abs/2505.08873")],"dynsys") +
  pillar("sciml","02","Scientific Machine Learning",ANIM_SCIML,
    "Hybrid models that keep mechanistic structure and let a learned component absorb what the mechanism omits, with structural identifiability analysis to decide what the data can determine before fitting.",
    ["When a learned term is added to a mechanistic model, which parameters remain identifiable from the observed outputs?","How should neural and universal differential equations be trained so that the learned part cannot silently compensate for a wrong mechanism?"],
    ["Neural and universal ODEs","Structural identifiability","Symbolic computation","Uncertainty quantification"],
    [("A tutorial on symbolic structural identifiability analysis of ODE models in Julia","arXiv, 2026","https://arxiv.org/abs/2605.18910"),("Stochastic dynamics of hepatitis B virus infection","arXiv, 2023","https://arxiv.org/abs/2308.05819")],"sciml") +
  pillar("biomed","03","Biomedical Data Science",ANIM_BIOMED,
    "Clinical prediction models that are calibrated and interpretable, statistical methods for data with unusual structure such as angles, and the optimization theory behind training learning models.",
    ["Can a model built from routine clinical data support prognosis where specialist resources are scarce?","How well calibrated are a model's probabilities, and how should they be corrected without losing discrimination?"],
    ["Calibration and interpretability","Circular statistics","Bayesian inference","Optimization for learning"],
    [("Calibrated and interpretable ML for ICU mortality prediction","medRxiv, 2026","https://www.medrxiv.org/content/10.64898/2026.05.30.26354524v1"),("Interpretable ML prognosis of mycetoma from routine clinical data","TRSTMH, 2026","https://doi.org/10.1093/trstmh/trag061"),("Circular statistics in the presence of measurement bias","IEEE JBHI","https://doi.org/10.1109/JBHI.2023.3334684")],"learning") +
  pillar("neuro","04","Computational Neuroscience",ANIM_NEURO,
    "Statistical analysis of intracranial EEG from patients with epilepsy, centered on high frequency oscillations as a candidate biomarker and on the recording conditions that confound them.",
    ["How do recording duration, sleep stage, and circadian time change the detection and interpretation of high frequency oscillations?","Can automated detection be made robust enough for long term clinical recordings?"],
    ["Signal processing","Event detection","Sleep and vigilance state","Phase and circadian analysis"],
    [("Recording duration and vigilance state in HFO characterization","Neurology, 2026","https://doi.org/10.1212/WNL.0000000000218225"),("Effect of sleep stage on high frequency oscillations and artifacts","AES, 2021","publications.html")],"domains"))

def dnode(pid, num, title, sub):
    return f'<a class="rdiag__node" href="#pillar-{pid}"><span class="rdiag__num">{num}</span><span class="rdiag__title">{title}</span><span class="rdiag__sub">{sub}</span></a>'
rdiag = ('<div class="rdiag" aria-label="Research program as a progression">'
  + dnode("modeling","01","Dynamical Systems","models with known structure") + '<span class="rdiag__arrow" aria-hidden="true"></span>'
  + dnode("sciml","02","Structural Identifiability","what the data can determine") + '<span class="rdiag__arrow" aria-hidden="true"></span>'
  + dnode("sciml","02","Scientific Machine Learning","structure plus learned terms") + '<span class="rdiag__arrow" aria-hidden="true"></span>'
  + dnode("biomed","03 · 04","Biomedical Applications","clinical, epidemic, neural data") + '</div>'
  + '<p class="rdiag__caption">Each stage constrains the next: a model with known structure is analyzed for what its outputs can determine; only then is a learned component added; and the result is judged by whether it can be trusted on clinical, epidemiological, or neural data. Select a stage to open the corresponding pillar.</p>')

home = f"""
<section class="hero"><div class="container hero__grid">
  <div class="hero__portrait"><img src="assets/img/profile.jpg" alt="Portrait of Abdallah Alsammani" width="200" height="200" fetchpriority="high"></div>
  <div>
    <p class="hero__kicker">Assistant Professor of Mathematics &amp; Data Science</p>
    <h1 class="hero__name">Abdallah Alsammani, Ph.D.</h1>
    <p class="hero__inst">Department of Mathematical Sciences, Delaware State University</p>
    <p class="hero__identity">Mathematical &amp; Scientific Machine Learning for Biomedical Systems</p>
    <p class="hero__statement">I am an applied mathematician. I build differential equation models of biological and clinical systems, ask which of their parameters can actually be learned from data, and combine them with machine learning when the mechanism is only partly known. The questions that drive the work are concrete: how an infection spreads and responds to intervention, which patients are at risk and how far a model's probability can be trusted, and what high frequency oscillations in intracranial EEG reveal about epilepsy.</p>
    <div class="btn-row"><a class="btn btn--primary" href="research.html">Research</a><a class="btn btn--outline" href="publications.html">Publications</a><a class="btn btn--outline" href="CV.pdf">CV</a></div>
    {profile_links()}
  </div>
  <div class="hero__visual">{hero_svg()}</div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head section-head--row"><div><h2>Research program</h2><p>One program in four connected pillars. I trained in dynamical systems at Auburn University, then worked with intracranial EEG data at the University of Nebraska Medical Center and with epidemiological models at the University of Georgia; the pillars below are where those threads meet.</p></div><a class="link-arrow" href="research.html">Full research overview {arrow}</a></div>
  {rdiag}
  <div class="pillars">{pillars_html}</div>
</div></section>

<section class="section section--off"><div class="container">
  <div class="section-head section-head--row"><div><h2>Featured research</h2><p>Three projects representing the methods, disease dynamics, and neural data sides of the program.</p></div><a class="link-arrow" href="publications.html">All publications {arrow}</a></div>
  <div class="featured">{feat}</div>
</div></section>

<section class="section"><div class="container container--narrow">
  <div class="section-head section-head--row"><div><h2>Latest highlights</h2></div><a class="link-arrow" href="group.html#news">All news {arrow}</a></div>
  <ul class="news">{news_html}</ul>
</div></section>

<section class="section" style="padding-top:0"><div class="container">
  <div class="cta"><div><h2>Students and collaborators</h2><p>I welcome prospective graduate students with backgrounds in mathematics, statistics, or computing, and collaborators in public health, medicine, and neuroscience whose questions call for mathematical modeling or scientific machine learning.</p></div>
  <div class="btn-row"><a class="btn btn--on-dark" href="group.html#opportunities">Join the group</a><a class="btn btn--on-dark-outline" href="contact.html">Contact</a></div></div>
</div></section>"""

page('index.html', 'Abdallah Alsammani, Ph.D. — Mathematical & Scientific Machine Learning for Biomedical Systems',
     'Abdallah Alsammani is Assistant Professor of Mathematics and Data Science at Delaware State University, working on dynamical systems, structural identifiability, scientific machine learning, uncertainty quantification, and biomedical modeling.', home, person=True)

# ============================================================ RESEARCH
def explorer(kind, title, note, controls, extra=''):
    body = '<canvas width="640" height="180" aria-label="Animated synthetic intracranial EEG trace with detected high frequency oscillation events"></canvas>' if kind=='ieeg' else '<svg role="img" aria-label="' + title + '"></svg>'
    return f'<div class="explorer" data-explorer="{kind}"><div class="explorer__title">{title}</div><p class="explorer__note">{note}</p>{body}<div class="explorer__controls">{controls}</div><div class="explorer__out" data-out aria-live="polite"></div>{extra}</div>'
def rng(p, label, lo, hi, step, val):
    return f'<label>{label} <input type="range" data-p="{p}" min="{lo}" max="{hi}" step="{step}" value="{val}"> <output data-v="{p}">{val}</output></label>'
def chk(p, label, on=False):
    return f'<label><input type="checkbox" data-p="{p}"{" checked" if on else ""}> {label}</label>'
def figure(svg, caption):
    return f'<figure class="figure">{svg}<figcaption>{caption}</figcaption></figure>'
MATH_HYBRID = '<math display="block"><mrow><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mi>f</mi><mo stretchy="false">(</mo><mi>x</mi><mo>,</mo><mi>θ</mi><mo stretchy="false">)</mo><mo>+</mo><mi>g</mi><mo stretchy="false">(</mo><mi>x</mi><mo>;</mo><mi>φ</mi><mo stretchy="false">)</mo></mrow></math>'
MATH_R0 = '<math><mrow><msub><mi mathvariant="script">R</mi><mn>0</mn></msub><mo>=</mo><mi>β</mi><mo>/</mo><mi>γ</mi></mrow></math>'
MATH_AB = '<math><mrow><mfrac><mrow><mi>d</mi><mi>x</mi></mrow><mrow><mi>d</mi><mi>t</mi></mrow></mfrac><mo>=</mo><mo>−</mo><mo stretchy="false">(</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo stretchy="false">)</mo><mi>x</mi></mrow></math>'

def area(aid, title, lead, paras, tags, works, extra=''):
    return f'''
<article class="area" id="{aid}">
  <div><h3>{title}</h3><p class="area__lead">{lead}</p><div class="prose">{''.join(f'<p>{x}</p>' for x in paras)}</div>{extra}</div>
  <aside class="area__side"><h4>Methods</h4><div class="tags">{''.join(f'<span class="tag">{t}</span>' for t in tags)}</div><h4>Representative work</h4><ul>{''.join(f'<li><a href="{u}"{ext(u)}>{t}</a><span class="muted">{m}</span></li>' for t,m,u in works)}</ul></aside>
</article>'''

works_dynsys = [("Impact of vaccination behavior on COVID-19 dynamics and economic outcomes","Math. Biosci. Eng., 2025","https://doi.org/10.3934/mbe.2025084"),
     ("Adaptive control and Mittag-Leffler stability of Caputo fractional systems with state-dependent delays","arXiv, 2026","https://arxiv.org/abs/2602.07105"),
     ("Long-term coexistence of epidemics and risk awareness","arXiv, 2026","https://arxiv.org/abs/2607.18301"),
     ("Stability analysis of a chemotherapy model with delays","DCDS-B, 2019","https://doi.org/10.3934/dcdsb.2019002")]
explorer_sir = explorer('sir', 'Explore: the SIR model and the basic reproduction number',
    'A closed population divided into susceptible, infectious, and recovered fractions with transmission rate β and recovery rate γ; ' + MATH_R0 + '. Synthetic illustration solved in the browser; not data from a publication.',
    rng('beta','β',0.05,1.0,0.01,0.30) + rng('gamma','γ',0.05,0.5,0.01,0.10) + chk('uq','show uncertainty envelope (β varied within ±20%)'))
explorer_ident = explorer('ident', 'Explore: structural identifiability',
    'For ' + MATH_AB + ' with observed output x(t), the data determine the sum a + b but not a and b separately. Move either slider, then switch on a second parameter pair with the same sum: the two curves coincide exactly.',
    rng('a','a',0.05,1.0,0.01,0.30) + rng('b','b',0.05,1.0,0.01,0.20) + chk('alt','show a second (a, b) with the same sum', True))
explorer_hybrid = explorer('hybrid', 'Explore: mechanistic model versus hybrid model on synthetic data',
    'Observations are generated from an SIR model whose transmission rate varies seasonally, with noise added. A purely mechanistic fit assumes a constant β; a hybrid fit keeps the SIR structure and lets a flexible time varying β(t) absorb what the mechanism omits. Here the flexible term is a small parametric family standing in for a learned component. Synthetic illustration only.',
    rng('amp','seasonal amplitude',0,0.8,0.1,0.4))
explorer_ieeg = explorer('ieeg', 'Animated illustration: high frequency oscillations in an intracranial recording',
    'A synthetic trace with brief high frequency bursts marked as detected events. The animation is paused automatically when reduced motion is requested. Illustration only, not patient data.',
    '<button class="btn btn--outline" type="button" data-p="play" aria-pressed="true">Pause</button>')
research = page_header('Research', 'Mathematically rigorous computational methods for biological, clinical, and public health systems. The program treats differential equations, statistical inference, and machine learning as a single toolkit, and it is organized as a progression: rigorous dynamical models, an analysis of what those models can learn from data, methods that combine models with data, and applications where the resulting predictions must be trusted.',
    [("methods","Methods"),("domains","Application domains"),("funding","Funding"),("resources","Software &amp; resources")]) + f'''
<section class="section"><div class="container">
  <div class="progression" style="margin-top:0"><span>Dynamical Systems</span>{arrow}<span>Structural Identifiability</span>{arrow}<span>Scientific Machine Learning</span>{arrow}<span>Biomedical Applications</span></div>
  <h2 id="methods" style="margin:var(--s6) 0 var(--s5)">Methodological themes</h2>
  {area("dynsys","Dynamical Systems &amp; Stochastic Modeling",
    "Deterministic and stochastic models of infectious diseases and biological processes, analyzed with the tools of dynamical systems and control theory.",
    ["My work in this area began with stability analysis of a chemotherapy model with delays and with hepatitis B virus infection models in autonomous, nonautonomous, and stochastic settings. More recent projects couple disease dynamics to human behavior: a model in which vaccination behavior, COVID-19 transmission, and economic outcomes influence one another, a cholera model with sanitation controls, and a study of how adaptive risk awareness and fatigue shape the long term coexistence of epidemics and awareness.",
     "A parallel line extends stability theory itself. With G. Farah I have established adaptive control and Mittag-Leffler stability results for Caputo fractional systems with state dependent delays, so that memory dependent dynamics can be analyzed with the same rigor as classical ones. Across these projects the tools are consistent: threshold quantities such as the basic reproduction number, Lyapunov based stability arguments, bifurcation analysis, and optimal control."],
    ["ODE, SDE and delay systems","Stability and bifurcation","Basic reproduction number","Optimal control","Fractional calculus"],
    works_dynsys, explorer_sir)
}
  {area("sciml","Scientific Machine Learning &amp; Structural Identifiability",
    "Methods that combine mechanistic models with learned components, and the identifiability analysis that determines what such a model can recover from data.",
    ["A hybrid model keeps the structure of a mechanistic model, " + MATH_HYBRID + " and lets a flexible component <em>g</em>, typically a neural network, absorb what the mechanism <em>f</em> cannot express. Neural and universal differential equations are the general form. The approach retains interpretability where mechanism is trusted and adds flexibility where it is not, but it raises a question that must be answered before any fitting: which parameters can be recovered from the observed outputs at all?",
     "Structural identifiability answers that question symbolically, from the model equations alone. I have written a tutorial on carrying out this analysis in Julia, and I treat identifiability as the first step of every modeling project. The ongoing goal is a theory of identifiable hybrid models: conditions under which a mechanistic model augmented with a learned component remains identifiable, and training procedures that enforce them."],
    ["Neural and universal differential equations","Hybrid mechanistic and learned models","Structural identifiability","Symbolic computation","Uncertainty quantification"],
    [("A tutorial on symbolic structural identifiability analysis of ODE models in Julia","arXiv, 2026","https://arxiv.org/abs/2605.18910"),
     ("Stochastic dynamics of hepatitis B virus infection","arXiv, 2023","https://arxiv.org/abs/2308.05819")],
    figure(FIG_NODE, "Architecture of a hybrid neural differential equation: the mechanistic vector field and a neural network are summed and integrated by an ODE solver; both parameter sets are trained by differentiating through the solver.") + explorer_ident + explorer_hybrid)}
  {area("learning","Statistical Learning, Uncertainty Quantification &amp; Optimization",
    "Predictive models whose probabilities mean what they say, statistical methodology for data with unusual structure, and the optimization theory that underlies training.",
    ["A clinical prediction model is useful only if it is calibrated, so that predicted probabilities match observed frequencies, and interpretable, so that its reasoning can be inspected. With undergraduate researcher M. Johnson and J. Elrefaei I developed a calibrated and interpretable model for ICU mortality from the first twenty four hours of clinical data, and with clinical collaborators an interpretable prognosis model for mycetoma from routine measurements. In statistical methodology, I developed a method for estimating circular statistics, such as the phase of an oscillation, when each measurement carries a systematic bias.",
     "An emerging direction treats the training of machine learning and deep learning models as a problem in dynamical systems and control. Gradient descent discretizes a gradient flow, momentum methods are second order dynamics, and stochastic gradients inject structured noise, so the stability, delay, and perturbation theory I use for biological systems applies to the algorithms that fit models as well. I am pursuing step size and adaptive schemes with stability guarantees, optimizers whose effect on robustness and calibration can be characterized, and training methods for hybrid and neural differential equation models that respect identifiability constraints. This direction is in progress and has not yet produced publications."],
    ["Calibration and interpretability","Circular statistics","Bayesian inference","Survival and time series analysis","Optimization for learning"],
    [("Calibrated and interpretable machine learning for ICU mortality prediction","medRxiv preprint, 2026","https://www.medrxiv.org/content/10.64898/2026.05.30.26354524v1"),
     ("Interpretable machine-learning prognosis of mycetoma from routine clinical data","Trans. R. Soc. Trop. Med. Hyg., 2026","https://doi.org/10.1093/trstmh/trag061"),
     ("Estimation of circular statistics in the presence of measurement bias","IEEE J. Biomed. Health Inform., 28(2)","https://doi.org/10.1109/JBHI.2023.3334684")],
    figure(FIG_UQ, "Uncertainty propagation: when the transmission rate of an SIR model is only known to within twenty percent, the possible epidemic curves form a band. Quantifying and reporting such bands is part of every forecasting project. Synthetic illustration."))}
</div></section>

<section class="section section--off" id="domains"><div class="container">
  <div class="section-head"><h2>Application domains</h2><p>The methods above are developed in response to questions from three domains, and each domain feeds back into the methods.</p></div>
  <div class="themes">
    <div class="theme"><h3>Infectious Disease Modeling</h3><p>Hepatitis B, COVID-19, and cholera models; behavior and economics coupled to transmission; hybrid forecasting that combines compartmental structure with learned transmission terms.</p></div>
    <div class="theme"><h3>Clinical and Biomedical Data Science</h3><p>ICU mortality and mycetoma prognosis from routine clinical data; calibration assessed across patient subgroups; extension to multimodal electronic health record data.</p></div>
    <div class="theme"><h3>Computational Neuroscience</h3><p>High frequency oscillations in intracranial EEG from patients with epilepsy: how recording duration, sleep stage, and circadian time shape a candidate biomarker, and automated detection for long term recordings.</p>
      <ul><li><a href="https://doi.org/10.1212/WNL.0000000000218225" target="_blank" rel="noopener">Recording duration and vigilance state in HFO characterization</a> · Neurology, 2026</li></ul></div>
  </div>
  {explorer_ieeg}
</div></section>

<section class="section" id="funding"><div class="container">
  <div class="section-head"><h2>Funding</h2></div>
  <div class="grants">
    <div><h3>Funded</h3>
      <div class="grant"><div class="grant__title">Faculty Summer Research Grant</div><div class="grant__org">Delaware State University · mathematical modeling, infectious disease dynamics, and data science</div><div class="grant__meta">Principal Investigator · 2026</div></div>
      <div class="grant"><div class="grant__title">Delaware INBRE Summer Undergraduate Research Program</div><div class="grant__org">Delaware INBRE / Delaware State University</div><div class="grant__meta">Faculty Mentor · 2026</div></div>
      <div class="grant"><div class="grant__title">Scholarship of Teaching and Learning Grant</div><div class="grant__org">Jacksonville University · interactive learning modules for mathematics and data science</div><div class="grant__meta">Principal Investigator · 2023–2024</div></div></div>
    <div><h3>Under review</h3>
      <div class="grant"><div class="grant__title">Computational STEM Pathways</div><div class="grant__org">Alfred P. Sloan Foundation · lead institution: Delaware State University</div><div class="grant__meta">Principal Investigator · 2026</div></div>
      <div class="grant"><div class="grant__title">Computational STEM Pathways</div><div class="grant__org">Alfred P. Sloan Foundation · partner institutions: Hampton University and University of Nevada, Las Vegas</div><div class="grant__meta">Co-Principal Investigator · 2026</div></div>
      <div class="grant"><div class="grant__title">Causal Machine Learning for Equitable STEM Achievement</div><div class="grant__org">AERA–NSF Research Grants Program</div><div class="grant__meta">Principal Investigator · 2026</div></div></div>
  </div>
</div></section>

<section class="section section--off" id="resources"><div class="container container--narrow">
  <div class="section-head"><h2>Software &amp; resources</h2><p>Tutorials, educational resources, and code released to support reproducible research and teaching.</p></div>
  <ul class="resources">{''.join(f'<li><span class="kind">{r["kind"]}</span><div><h3>{r["title"]}</h3><p>{r["text"]}</p></div><div class="links">{"".join(f"<a href={chr(34)}{u}{chr(34)}{ext(u)}>{l} →</a>" for l,u in r["links"].items())}</div></li>' for r in RESOURCES)}</ul>
</div></section>'''
page('research.html', 'Research — Abdallah Alsammani, Ph.D.', 'Research program in dynamical systems and stochastic modeling, scientific machine learning and structural identifiability, statistical learning, uncertainty quantification and optimization, applied to infectious disease, clinical data, and neuroscience.', research, scripts=('assets/js/explorers.js',))

# ============================================================ PUBLICATIONS
sel = ''.join(pub_item(p) for p in PUBS if p.get('selected'))
GROUPS = [("Peer reviewed", ("journal", "conference")), ("Preprints", ("preprint",)), ("Other scholarly work", ("abstract", "other"))]
years = ''
for y in sorted({p['year'] for p in PUBS}, reverse=True):
    yp = [p for p in PUBS if p['year'] == y]
    grp = [(n, [p for p in yp if p['type'] in t]) for n, t in GROUPS]; grp = [g for g in grp if g[1]]
    inner = ''
    for n, ps in grp:
        if len(grp) > 1: inner += f'<h3 class="pub-group">{n}</h3>'
        inner += ''.join(pub_item(p) for p in ps)
    years += f'<div class="pub-year"><h2 class="pub-year__label">{y}</h2>{inner}</div>'
filters = ''.join(f'<button class="filter-btn" type="button" data-filter="{k}" aria-pressed="false">{v}</button>' for k, v in AREA_LABEL.items())
pubs = page_header('Publications', 'Journal articles, conference papers, preprints, and other scholarly work in mathematical biology, scientific machine learning, biomedical data science, and computational neuroscience. Preprints are marked as such throughout.', [("selected","Selected"),("all","Complete list")]) + f'''
<section class="section" id="selected"><div class="container container--narrow">
  <div class="section-head"><h2>Selected publications</h2></div>
  <div class="selected">{sel}</div>
</div></section>
<section class="section section--off" id="all"><div class="container container--narrow">
  <div class="section-head"><h2>Complete list</h2><p>Grouped by year; within each year, peer reviewed work is listed before preprints. Filter by research area below.</p></div>
  <div class="pub-filters" role="group" aria-label="Filter by research area"><span class="lbl">Area</span><button class="filter-btn" type="button" data-filter="all" aria-pressed="true">All</button>{filters}</div>
  <div class="pub-list">{years}</div>
  <p class="pub-empty" hidden>No publications in this area.</p>
  <div class="btn-row" style="margin-top:var(--s6)"><a class="btn btn--outline" href="{PROFILES['Google Scholar'][1]}" target="_blank" rel="noopener">Google Scholar</a><a class="btn btn--outline" href="{PROFILES['ORCID'][1]}" target="_blank" rel="noopener">ORCID</a></div>
</div></section>'''
page('publications.html', 'Publications — Abdallah Alsammani, Ph.D.', 'Selected and complete publications of Abdallah Alsammani: journal articles, conference papers, and preprints in dynamical systems, scientific machine learning, biomedical data science, and neuroscience.', pubs)

# ============================================================ GROUP
cur = ''.join(f'<li><h3>{m["name"]}</h3><div class="role">{m["role"]}</div>{f"<div class=topic>{m['topic']}</div>" if m.get("topic") else ""}</li>' for m in PEOPLE['current'])
def mentee_rows(ms):
    r = ''
    for m in ms:
        proj = m['project']
        if m.get('outcome'):
            o = m['outcome']; proj += f'; co-author, <a class="pub-ref" href="{o["url"]}"{ext(o["url"])}>{o["text"]}</a> ({o["venue"]})'
        r += f'<tr><td>{m["name"]}</td><td>{proj}.</td><td>{m["term"]}</td></tr>'
    return r
former = ''.join(f'<h3>{g["institution"]}</h3><table class="mentee-table"><thead><tr><th scope="col">Student</th><th scope="col">Research project / scholarly outcome</th><th scope="col">Term</th></tr></thead><tbody>{mentee_rows(g["members"])}</tbody></table>' for g in PEOPLE['former'])
allnews = ''.join(f'<li><span class="news__date">{n["date"]}</span><div><div class="news__title">{f"<a href={chr(34)}{n['url']}{chr(34)}{ext(n['url'])}>{n['title']}</a>" if n.get('url') else n['title']}</div>{f"<p class=news__text>{n['text']}</p>" if n.get('text') else ''}</div></li>' for n in NEWS)
group = page_header('Research Group', 'A small group in the Department of Mathematical Sciences at Delaware State University developing mathematical models and data driven methods for problems in public health, biomedicine, and neuroscience, and training students to do the same.',
    [("people","People"),("projects","Current projects"),("opportunities","Opportunities"),("news","Group news")]) + f'''
<section class="section" id="people"><div class="container">
  <div class="pi"><div class="pi__photo"><img src="assets/img/profile.jpg" alt="Portrait of Abdallah Alsammani" width="140" height="140"></div>
    <div><h3>Abdallah Alsammani, Ph.D.</h3><div class="pi__role">Principal Investigator · Assistant Professor of Mathematics and Data Science</div>
    <p class="small muted">I completed my Ph.D. in Applied Mathematics at Auburn University in 2020, then held postdoctoral positions in Neurosurgery at the University of Nebraska Medical Center and in Infectious Diseases at the University of Georgia. I was Assistant Professor of Data Science at Jacksonville University from 2022 to 2025 before joining Delaware State University. I am a member of the American Epilepsy Society and the American Mathematical Society.</p>
    <p style="margin-top:var(--s3)"><a class="link-arrow" href="cv.html">Curriculum vitae {arrow}</a></p></div></div>
  <h2 style="margin:var(--s7) 0 var(--s5)">Current students</h2>
  <ul class="people">{cur}</ul>
</div></section>

<section class="section section--off" id="projects"><div class="container container--narrow">
  <div class="section-head"><h2>Current projects</h2><p>Directions the group is pursuing now. Each is a place where a new student can contribute.</p></div>
  <ol class="projects">
    <li><div><h3>Hybrid epidemic forecasting</h3><p>Compartmental models combined with learned transmission terms, with identifiability checked symbolically before fitting and forecasts evaluated on withheld data with calibration diagnostics.</p></div></li>
    <li><div><h3>Identifiability and optimization for hybrid models</h3><p>Conditions under which a mechanistic model augmented with a neural component remains structurally identifiable, and training procedures with stability guarantees that enforce them. Related: <a href="https://arxiv.org/abs/2605.18910" target="_blank" rel="noopener">identifiability tutorial</a>.</p></div></li>
    <li><div><h3>Trustworthy clinical prediction</h3><p>Calibration, uncertainty quantification, and interpretability for clinical models, from ICU outcomes to multimodal electronic health record data, with calibration assessed across patient subgroups.</p></div></li>
    <li><div><h3>Automated HFO detection in long term intracranial EEG</h3><p>Deep learning detectors for pathological high frequency oscillations that account for vigilance state and recording duration, building on the group's clinical collaborations. Related: <a href="https://doi.org/10.1212/WNL.0000000000218225" target="_blank" rel="noopener">Neurology, 2026</a>.</p></div></li>
  </ol>
</div></section>

<section class="section" id="opportunities"><div class="container">
  <div class="grid grid--2">
    <div><div class="section-head"><h2>Joining the group</h2><p>I welcome students with backgrounds in mathematics, statistics, computer science, or related quantitative fields. Prior training in biology or medicine is not required; comfort with calculus, linear algebra, and probability is expected, and programming experience in Python, R, Julia, or MATLAB is valuable.</p></div>
      <ol class="steps">
        <li><strong>Read one paper.</strong><span>Skim the <a href="research.html">research overview</a> and choose a publication close to your interests.</span></li>
        <li><strong>Send a short introduction.</strong><span>Your background, the problems you find interesting, your programming experience, and a CV or transcript. A specific question about a paper is welcome.</span></li>
        <li><strong>Apply.</strong><span>Graduate applicants apply through the Delaware State University graduate program in Mathematical Sciences. Current undergraduates can begin with a semester project or a summer program such as Delaware INBRE.</span></li>
      </ol>
      <div class="btn-row" style="margin-top:var(--s5)"><a class="btn btn--primary" href="mailto:{EMAIL}?subject=Research%20group%20inquiry">Email Dr. Alsammani</a></div></div>
    <div class="mentees"><div class="section-head"><h2>Former research mentees</h2><p>Selected undergraduate and graduate research mentorship at Delaware State University and Jacksonville University. Several projects have resulted in peer reviewed publications and research preprints.</p></div>{former}</div>
  </div>
</div></section>

<section class="section section--off" id="news"><div class="container container--narrow">
  <div class="section-head"><h2>Group news</h2></div>
  <ul class="news">{allnews}</ul>
</div></section>'''
page('group.html', 'Research Group — Abdallah Alsammani, Ph.D.', 'The research group of Abdallah Alsammani at Delaware State University: people, current projects, opportunities for students and collaborators, and news.', group)

# ============================================================ TEACHING
def principle(num, title, text):
    return f'<div class="principle"><h3><span>{num}</span>{title}</h3><p>{text}</p></div>'
def framework(t, q, pts):
    return f'<div><h3>{t}</h3><em>{q}</em><ul>{"".join(f"<li>{p}</li>" for p in pts)}</ul></div>'
teaching = page_header('Teaching', 'Mathematics provides a language for describing complex systems and reasoning about them with precision. My teaching is designed to help students develop habits of thought that are rigorous, transferable, and grounded in first principles, whether they are studying mathematical analysis, probability, data science, or machine learning.',
    [("philosophy","Philosophy"),("approach","How I teach"),("ai","Generative AI"),("courses","Courses"),("mentoring","Mentoring")]) + f'''
<section class="section" id="philosophy"><div class="container container--narrow">
  <div class="section-head"><h2>Teaching philosophy</h2><p>Students should understand not only how a method works, but why it works, when it applies, and where its limitations begin.</p></div>
  <div class="prose">
    <p><strong>Mathematical understanding.</strong> A regression, a numerical solver, or a neural network is a set of assumptions and a piece of mathematical structure before it is a line of code. I teach students to state those assumptions, follow the reasoning that justifies the method, and recognize the conditions under which it fails. In proof based courses this means walking through the reasoning that produces a finished argument rather than only the argument itself; in applied courses it means that every computational technique is preceded by the result that justifies it. A student who understands the mathematics can judge whether a familiar tool fits an unfamiliar problem.</p>
    <p><strong>From theory to computation to interpretation.</strong> My courses follow a consistent progression: a scientific question leads to a mathematical formulation, the formulation is carried out in computation, and the computation is interpreted in the language of the original question. Python, R, and MATLAB are integrated into mathematics courses for this reason, not as a separate skill. Students derive before they implement, validate before they trust, and interpret before they report, so that computation extends their mathematics rather than replacing it.</p>
    <p><strong>An inclusive and demanding classroom.</strong> I have taught students with widely varying preparation, from lecture halls in Khartoum to the calculus sequence and tutoring center at Auburn University to data science majors at Jacksonville University and graduate courses at Delaware State University. That experience shaped a simple practice: diagnose where a student actually is, adjust pacing and examples to meet them there, and keep the standard they are working toward fixed. Assignments build skill in a graduated sequence, office hours are structured so that asking a hard question is the expected behavior, and rigorous questions are welcomed from everyone. Supporting students from groups historically underrepresented in the mathematical sciences is a responsibility I hold with conviction; in my experience rigor and accessibility are complementary rather than competing goals.</p>
    <p><strong>Active learning and independent thinking.</strong> Class time is for thinking rather than transcription. Interactive modules, developed with the support of a Scholarship of Teaching and Learning grant, let students test ideas before they are formalized, and assessment rewards a correct formulation and a well argued interpretation over a memorized procedure. The long term goal is a student who can formulate a problem, reason from assumptions, use computation intelligently, evaluate results critically, and explain the conclusions to someone else. Support decreases as a course proceeds so that independence is practiced rather than merely expected.</p>
    <p><strong>Mentoring and responsible tools.</strong> Research mentoring extends the classroom: students move from a well posed question to a validated computational solution and a presentation of the result, and several undergraduate projects have led to conference papers and preprints. Generative AI is now part of how students learn and code, so I integrate its responsible and transparent use into my courses through a student guide built on three questions, described below, rather than leaving students to guess where the line lies.</p>
  </div>
</div></section>

<section class="section section--off" id="approach"><div class="container">
  <div class="section-head"><h2>How I teach</h2></div>
  <div class="principles">
    {principle("01","Foundations before black boxes","Students meet the assumptions and structure behind a method before relying on software to apply it: the least squares normal equations before regression software, the convexity assumptions behind gradient descent before tuning an optimizer.")}
    {principle("02","Computation with purpose","Python, R, MATLAB, numerical methods, and visualization extend the mathematics rather than replace it. Laboratory work asks students to implement a method from its description, validate it against known results, keep the analysis reproducible, and interpret the output.")}
    {principle("03","Research informed learning","Examples and projects come from infectious disease modeling, biomedical data science, computational neuroscience, and scientific machine learning. Student projects have contributed to a peer reviewed ICCSA paper on sleep disorder prediction and a medRxiv preprint on ICU mortality prediction.")}
    {principle("04","Assessment for understanding","Assessments reward reasoning over memorization and formulation before calculation; a well argued interpretation is part of every solution. Feedback is specific, and scaffolding decreases while the expectation of independent judgment increases through the term.")}
  </div>
</div></section>

<section class="section" id="ai"><div class="container">
  <div class="section-head"><h2>Responsible use of generative AI</h2><p>Use generative AI to support your learning, not to replace the thinking, skills, and responsibility your coursework is designed to develop. My student guide organizes that principle around three questions.</p></div>
  <div class="framework">
    {framework("Learning and growth","Does this use preserve the thinking the task exists to develop?",["Attempt the task first.","Preserve the skill the assignment is designed to develop.","Verify AI generated claims, calculations, code, and references.","Submit only work you can explain and defend."])}
    {framework("Ethics and integrity","Is my own contribution honestly and clearly represented?",["Disclose AI use when required.","Do not present AI generated work as your own.","Follow course specific expectations.","Agree on clear AI use norms in collaborative work."])}
    {framework("Awareness and safety","Is the output, and what I entered, safe to rely on?",["Protect personal, confidential, proprietary, and identifying information.","Confirm course and assignment expectations before using AI.","Recognize that AI outputs may be inaccurate or biased.","Recheck guidance as tools and policies evolve."])}
  </div>
  <div class="resource-panel"><div><h3>Student Guidelines for Responsible Use of Generative AI</h3><div class="sub">A practical guide for responsible AI use in higher education.</div><p>A one page framework for deciding when and how generative AI can support coursework while preserving learning, academic integrity, privacy, and individual responsibility. It is an educational resource, not an institutional policy; where a course policy differs, the course policy governs.</p><p class="small muted" style="margin-top:var(--s3)">Companion scholarship: Alsammani, A. (2026). <em>A Student-Centered Framework for Responsible Use of Generative AI in Higher Education.</em> EdArXiv preprint.</p></div>
    <div class="btn-row"><a class="btn btn--primary" href="AI-Guide-4-students.pdf" target="_blank" rel="noopener">View the guide (PDF)</a></div></div>
</div></section>

<section class="section section--off" id="courses"><div class="container">
  <div class="section-head"><h2>Courses</h2><p>Current teaching at Delaware State University and selected courses developed and taught previously. The complete teaching record is in the <a href="cv.html">CV</a>.</p></div>
  <div class="courses">
    <div class="course-block"><h3>Delaware State University</h3><p class="course-block__meta">Current · Department of Mathematical Sciences</p>
      <ul class="course-list"><li><span class="code">MTSC 821</span><span>Scientific Computations I</span><span class="lvl">Graduate</span></li><li><span class="code">MTSC 571</span><span>Complex Analysis</span><span class="lvl">Graduate</span></li><li><span class="code">MTSC 452</span><span>Advanced Calculus II</span><span class="lvl"></span></li><li><span class="code">MTSC 341</span><span>Probability</span><span class="lvl">Online</span></li></ul></div>
    <div class="course-block"><h3>Selected courses developed and taught</h3><p class="course-block__meta">Jacksonville University, 2022–2025</p>
      <ul class="course-list"><li><span class="code">MATH 470</span><span>Machine Learning Algorithms</span><span class="lvl"></span></li><li><span class="code">MATH 270</span><span>Introduction to Data Science</span><span class="lvl"></span></li><li><span class="code">MATH 170</span><span>Data Science Foundations</span><span class="lvl"></span></li><li><span class="code">MATH 481WS</span><span>Capstone Research Project</span><span class="lvl">Capstone</span></li><li><span class="code">MATH 331</span><span>Differential Equations</span><span class="lvl"></span></li><li><span class="code">MATH 420</span><span>Linear Algebra II</span><span class="lvl"></span></li></ul>
      <p class="course-block__note">Also developed the Data Science Certificate Program (2023) and served as Assessment Coordinator for the Data Science major and minor. Earlier teaching at Auburn University (calculus sequence; Excellence in Teaching Award, 2019–2020) and in Khartoum, Sudan.</p></div>
  </div>
</div></section>

<section class="section" id="mentoring"><div class="container container--narrow">
  <div class="section-head"><h2>Research mentoring</h2><p>I mentor graduate and undergraduate students in mathematical modeling, scientific machine learning, biomedical data science, and related computational research. Students begin with a well posed question, learn to formulate it mathematically, build and validate a computational solution, and present the result; several projects have led to conference papers and research preprints.</p></div>
  <a class="link-arrow" href="group.html">Research Group {arrow}</a>
</div></section>'''
page('teaching.html', 'Teaching — Abdallah Alsammani, Ph.D.', 'Teaching philosophy, classroom practice, responsible use of generative AI, current and selected courses, and research mentoring by Abdallah Alsammani.', teaching)

# ============================================================ CV
def entry(when, what, where, note=''):
    return f'<div class="cv-entry"><div class="cv-entry__when">{when}</div><div><div class="cv-entry__what">{what}</div><div class="cv-entry__where">{where}</div>{f"<div class=cv-entry__note>{note}</div>" if note else ""}</div></div>'
cv = page_header('Curriculum Vitae', 'Appointments, education, honors, service, and skills. Publications and funding are on their own pages; the complete record, including teaching history and professional development, is in the PDF.') + f'''
<section class="section"><div class="container cv-layout">
  <nav class="cv-toc" aria-label="CV sections"><ul><li><a href="#appointments">Appointments</a></li><li><a href="#education">Education</a></li><li><a href="#honors">Honors</a></li><li><a href="#service">Service</a></li><li><a href="#skills">Skills</a></li></ul><a class="btn btn--primary" href="CV.pdf">Download PDF</a></nav>
  <div>
    <div class="cv-section" id="appointments"><h2>Academic appointments</h2>
      {entry("Aug 2025 – present","Assistant Professor of Mathematics and Data Science (Tenure-Track)","Department of Mathematical Sciences, Delaware State University")}
      {entry("Aug 2022 – Jul 2025","Assistant Professor of Data Science","School of Science and Mathematics, Jacksonville University")}
      {entry("Jan 2022 – Jul 2022","Postdoctoral Research Associate","Department of Infectious Diseases, University of Georgia","Epidemiological modeling for CDC contracted research")}
      {entry("Jan 2021 – Jan 2022","Postdoctoral Research Associate","Department of Neurosurgery, University of Nebraska Medical Center","Intracranial EEG and high frequency oscillations")}
      {entry("Aug 2014 – Dec 2020","Graduate Teaching Assistant and Instructor of Record","Department of Mathematics and Statistics, Auburn University")}
      {entry("Aug 2012 – Aug 2013","Lecturer of Mathematics and Statistics","Al Neelain University and Academy of Engineering and Medical Sciences, Khartoum, Sudan")}</div>
    <div class="cv-section" id="education"><h2>Education</h2>
      {entry("2020","Ph.D., Applied Mathematics","Auburn University","Dissertation: <em>Dynamical Behavior of Nonautonomous and Stochastic HBV Infection Model</em>")}
      {entry("2014","Postgraduate Diploma in Mathematics","International Centre for Theoretical Physics (ICTP), Trieste, Italy")}
      {entry("2012","M.Sc., Applied Mathematics","African Institute for Mathematical Sciences (AIMS), Senegal")}
      {entry("2009","B.Sc., Mathematics (Honors)","Al Neelain University, Khartoum, Sudan")}</div>
    <div class="cv-section" id="honors"><h2>Honors and fellowships</h2>
      {entry("2019 – 2020","Excellence in Teaching Award","Department of Mathematics and Statistics, Auburn University")}
      {entry("2014 – 2020","Graduate Teaching Assistantship","Auburn University")}
      {entry("2013 – 2014","Pre-Ph.D. Fellowship in Mathematics","ICTP, Trieste, Italy")}
      {entry("2011 – 2012","Master's Scholarship in Applied Mathematics","AIMS, Senegal")}
      {entry("2004 – 2009","Outstanding Undergraduate Student Award","Al Neelain University")}</div>
    <div class="cv-section" id="service"><h2>Academic service</h2>
      {entry("2026","Faculty Mentor, Delaware INBRE Summer Undergraduate Research Program","Delaware State University")}
      {entry("2024 – 2025","Member, Planning and Budget Committee","Jacksonville University")}
      {entry("2023 – 2024","Member, Artificial Intelligence Taskforce Committee","Jacksonville University")}
      {entry("2022 – 2025","Assessment Coordinator, Data Science Programs","Jacksonville University")}
      {entry("2022 – 2024","Faculty search committees (five)","Jacksonville University")}
      {entry("2018","Organizing Committee, 52nd Spring Topology and Dynamical Systems Conference","Auburn University")}
      <p class="small muted" style="margin-top:var(--s4)">Memberships: American Epilepsy Society; American Mathematical Society.</p></div>
    <div class="cv-section" id="skills"><h2>Technical skills</h2>
      <ul class="cv-list"><li><strong>Modeling:</strong> ODE, PDE, SDE, dynamical systems, optimal control</li><li><strong>Statistics:</strong> regression, survival and time series analysis, Bayesian inference, circular statistics</li><li><strong>Machine learning:</strong> supervised and unsupervised learning, deep learning, model validation</li><li><strong>Languages and software:</strong> Python (NumPy, SciPy, pandas, scikit-learn, TensorFlow), R, Julia, MATLAB, Mathematica, SAS, C++, SQL</li></ul></div>
  </div>
</div></section>'''
page('cv.html', 'Curriculum Vitae — Abdallah Alsammani, Ph.D.', 'Academic appointments, education, honors, service, and skills of Abdallah Alsammani, with the complete CV available as a PDF.', cv)

# ============================================================ CONTACT
contact = page_header('Contact', 'For research collaboration, graduate and undergraduate advising, seminar and conference invitations, and consultation on mathematical modeling and biomedical data analysis.') + f'''
<section class="section"><div class="container contact">
  <ul class="contact-list">
    <li><h3>Email</h3><a href="mailto:{EMAIL}">{EMAIL}</a></li>
    <li><h3>Office</h3>Department of Mathematical Sciences<br>Delaware State University<br>1200 N. DuPont Highway, Dover, DE 19901</li>
    <li><h3>Profiles</h3>{profile_links()}</li>
  </ul>
  <ul class="audience">
    <li><strong>Prospective graduate students</strong><span>See <a href="group.html#opportunities">how to join the group</a>, then email a short introduction with your background and interests.</span></li>
    <li><strong>Research collaborators</strong><span>Clinical, epidemiological, and neuroscience collaborators with data and a question are especially welcome; so are mathematicians and computer scientists working on identifiability, hybrid modeling, or optimization.</span></li>
    <li><strong>Students interested in modeling or scientific machine learning</strong><span>Current Delaware State University undergraduates can begin with a semester research project or a summer program such as Delaware INBRE.</span></li>
  </ul>
</div></section>'''
page('contact.html', 'Contact — Abdallah Alsammani, Ph.D.', 'Contact Abdallah Alsammani, Assistant Professor of Mathematics and Data Science at Delaware State University.', contact)
