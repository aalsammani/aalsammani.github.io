# -*- coding: utf-8 -*-
"""Generate the seven static pages. Usage: python3 _build/build.py (from site root)."""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from partials import *
from publications import PUBS, TYPE_LABEL

OUT = os.path.join(os.path.dirname(__file__), "..")

def write(name, html):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", name)

def authors_html(a):
    return re.sub(r"\*\*(.+?)\*\*", r'<span class="me">\1</span>', a)

def page(current, title, desc, body, ld=""):
    return head(title, desc, current, ld) + header(current) + body + footer()


# =============================================================================
# HOME
# =============================================================================
home = f"""
<section class="hero">
  <div class="container hero__grid">
    <div class="hero__portrait"><img src="assets/img/profile.jpg" alt="Portrait of Abdallah Alsammani" width="200" height="200" fetchpriority="high"></div>
    <div>
      <h1 class="hero__name">Abdallah Alsammani, Ph.D.</h1>
      <p class="hero__role">Assistant Professor of Mathematics and Data Science</p>
      <p class="hero__inst">Department of Mathematical Sciences, Delaware State University</p>
      <p class="hero__lede">I am an applied mathematician and data scientist. My research develops <strong>mathematically rigorous computational methods for biological, clinical, and public-health systems</strong>, combining dynamical-systems models of infectious disease, scientific machine learning that couples mechanistic models with data, interpretable clinical prediction, and statistical methods for intracranial EEG.</p>
      <div class="hero__links">{social_links()}</div>
      <div class="btn-row">
        <a class="btn btn--primary" href="research.html">Explore research {icon('i-arrow')}</a>
        <a class="btn btn--outline" href="publications.html">Publications</a>
        <a class="btn btn--outline" href="CV.pdf">{icon('i-download')} Download CV</a>
      </div>
    </div>
    <div class="hero__visual">{hero_svg()}</div>
  </div>
</section>

<section class="tagline-band" aria-label="Research program">
  <div class="container">
    <p class="tagline-band__title">Mathematical &amp; Scientific Machine Learning <span>for Biomedical Systems</span></p>
    <p class="tagline-band__text">A research program that treats differential equations, statistical inference, and machine learning as one toolkit for understanding disease dynamics, clinical outcomes, and neural signals.</p>
  </div>
</section>

<section class="section" id="pillars">
  <div class="container">
    <div class="section-head section-head--row reveal">
      <div>
        <h2>Four research pillars</h2>
        <p>Each pillar builds on the previous one: rigorous models, methods that learn from data, applications to biomedical data, and a long-standing focus on the brain.</p>
      </div>
      <a class="more link-arrow" href="research.html">Full research overview {icon('i-arrow')}</a>
    </div>
    <div class="pillars reveal">
      <article class="pillar">
        <div class="pillar__num">01</div>
        <div class="pillar__icon">{PILLAR_ICONS['modeling']}</div>
        <h3>Mathematical Modeling</h3>
        <p>Deterministic and stochastic dynamical systems for infectious diseases and biological processes, with stability, identifiability, and optimal-control analysis.</p>
        <ul class="pillar__topics"><li>ODE, SDE &amp; delay systems</li><li>Stability &amp; bifurcation</li><li>Optimal control</li><li>Multiscale host–pathogen models</li></ul>
        <a class="link-arrow" href="research.html#modeling">Read more {icon('i-arrow')}</a>
      </article>
      <article class="pillar">
        <div class="pillar__num">02</div>
        <div class="pillar__icon">{PILLAR_ICONS['sciml']}</div>
        <h3>Scientific Machine Learning</h3>
        <p>Physics-informed and hybrid methods that integrate mechanistic models with data for inference, prediction, and control of dynamical systems.</p>
        <ul class="pillar__topics"><li>Neural differential equations</li><li>Hybrid mechanistic–statistical models</li><li>Structural identifiability</li><li>Uncertainty quantification</li></ul>
        <a class="link-arrow" href="research.html#sciml">Read more {icon('i-arrow')}</a>
      </article>
      <article class="pillar">
        <div class="pillar__num">03</div>
        <div class="pillar__icon">{PILLAR_ICONS['biomed']}</div>
        <h3>Biomedical Data Science</h3>
        <p>Interpretable, calibrated predictive models for clinical outcomes and disease risk, and robust statistical methodology for complex biomedical data.</p>
        <ul class="pillar__topics"><li>Clinical prediction &amp; EHR data</li><li>Calibration &amp; interpretability</li><li>Circular statistics &amp; bias correction</li><li>High-dimensional data</li></ul>
        <a class="link-arrow" href="research.html#biomed">Read more {icon('i-arrow')}</a>
      </article>
      <article class="pillar">
        <div class="pillar__num">04</div>
        <div class="pillar__icon">{PILLAR_ICONS['neuro']}</div>
        <h3>Computational Neuroscience</h3>
        <p>Statistical and computational analysis of electrophysiological data, centered on high-frequency oscillations in epilepsy and their clinical use.</p>
        <ul class="pillar__topics"><li>Intracranial EEG</li><li>High-frequency oscillations</li><li>Sleep &amp; vigilance state</li><li>Long-term recordings</li></ul>
        <a class="link-arrow" href="research.html#neuro">Read more {icon('i-arrow')}</a>
      </article>
    </div>
  </div>
</section>

<section class="section section--alt" id="featured">
  <div class="container">
    <div class="section-head section-head--row reveal">
      <div>
        <h2>Featured research</h2>
        <p>Three representative projects, one from each side of the program: methods, disease dynamics, and neural data.</p>
      </div>
      <a class="more link-arrow" href="publications.html">All publications {icon('i-arrow')}</a>
    </div>
    <div class="featured reveal">
      <article class="project">
        <div class="project__figure">{FIG_HYBRID}</div>
        <div class="project__body">
          <h3>Structural identifiability for mechanistic and hybrid models</h3>
          <p>Before fitting a differential-equation model to data, can its parameters be recovered at all? A symbolic, reproducible workflow in Julia for answering that question, as a foundation for hybrid mechanistic–learned models.</p>
          <p class="project__methods"><span>Methods</span> · Symbolic computation · ODE models · Scientific ML</p>
          <div class="project__links"><a href="https://arxiv.org/abs/2605.18910" target="_blank" rel="noopener">Paper {icon('i-ext')}</a></div>
        </div>
      </article>
      <article class="project">
        <div class="project__figure">{FIG_EPI}</div>
        <div class="project__body">
          <h3>Vaccination behavior, COVID-19 dynamics, and economic outcomes</h3>
          <p>A coupled epidemiological–economic model linking vaccination decisions and economic conditions to long-term pandemic trajectories, with analysis of the resulting equilibria and intervention trade-offs.</p>
          <p class="project__methods"><span>Methods</span> · Dynamical systems · Behavioral epidemiology · Stability analysis</p>
          <div class="project__links"><a href="https://doi.org/10.3934/mbe.2025084" target="_blank" rel="noopener">Paper {icon('i-ext')}</a></div>
        </div>
      </article>
      <article class="project">
        <div class="project__figure">{FIG_IEEG}</div>
        <div class="project__body">
          <h3>High-frequency oscillations in long-term intracranial EEG</h3>
          <p>How recording duration and vigilance state shape the characterization of high-frequency oscillations, a candidate biomarker of the epileptogenic zone, in a multi-center clinical collaboration.</p>
          <p class="project__methods"><span>Methods</span> · Signal analysis · Circular statistics · Clinical neurophysiology</p>
          <div class="project__links"><a href="https://doi.org/10.1212/WNL.0000000000218225" target="_blank" rel="noopener">Paper {icon('i-ext')}</a></div>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="section" id="journey">
  <div class="container">
    <div class="section-head reveal">
      <h2>Academic journey</h2>
      <p>From doctoral training in applied mathematics through two biomedical postdoctoral appointments to a tenure-track position in mathematical sciences.</p>
    </div>
    <ol class="timeline reveal">
      <li>
        <div class="timeline__years">2014 – 2020</div>
        <div class="timeline__inst">Auburn University</div>
        <div class="timeline__role">Ph.D., Applied Mathematics</div>
        <div class="timeline__note">Nonautonomous &amp; stochastic HBV infection models</div>
      </li>
      <li>
        <div class="timeline__years">2021 – 2022</div>
        <div class="timeline__inst">University of Nebraska Medical Center</div>
        <div class="timeline__role">Postdoctoral Research Associate, Neurosurgery</div>
        <div class="timeline__note">Intracranial EEG &amp; high-frequency oscillations</div>
      </li>
      <li>
        <div class="timeline__years">2022</div>
        <div class="timeline__inst">University of Georgia</div>
        <div class="timeline__role">Postdoctoral Research Associate, Infectious Diseases</div>
        <div class="timeline__note">Epidemiological modeling for CDC-contracted research</div>
      </li>
      <li>
        <div class="timeline__years">2022 – 2025</div>
        <div class="timeline__inst">Jacksonville University</div>
        <div class="timeline__role">Assistant Professor of Data Science</div>
        <div class="timeline__note">Built the undergraduate data-science research program</div>
      </li>
      <li class="is-current">
        <div class="timeline__years">2025 – present</div>
        <div class="timeline__inst">Delaware State University</div>
        <div class="timeline__role">Assistant Professor of Mathematics and Data Science</div>
        <div class="timeline__note">Tenure-track, Department of Mathematical Sciences</div>
      </li>
    </ol>
    <div class="timeline-foot"><a class="link-arrow" href="cv.html">Full curriculum vitae {icon('i-arrow')}</a></div>
  </div>
</section>

<section class="section section--alt" id="news">
  <div class="container">
    <div class="section-head reveal">
      <h2>Recent news</h2>
    </div>
    <ul class="news reveal">
      <li><span class="news__date">2026</span><div><div class="news__title">Study on recording duration and vigilance state in HFO characterization published in <em>Neurology</em></div><p class="news__text">Collaborative work with the epilepsy research group at the University of Nebraska Medical Center. <a href="https://doi.org/10.1212/WNL.0000000000218225" target="_blank" rel="noopener">Read the paper</a>.</p></div></li>
      <li><span class="news__date">2026</span><div><div class="news__title">Faculty Summer Research Grant awarded (PI)</div><p class="news__text">Delaware State University support for interdisciplinary research in mathematical modeling, infectious-disease dynamics, and data science.</p></div></li>
      <li><span class="news__date">2026</span><div><div class="news__title">Faculty mentor, Delaware INBRE Summer Undergraduate Research Program</div><p class="news__text">Supervising undergraduate biomedical and data-science research projects.</p></div></li>
      <li><span class="news__date">2026</span><div><div class="news__title">Interpretable machine-learning prognosis of mycetoma published</div><p class="news__text"><em>Transactions of The Royal Society of Tropical Medicine and Hygiene</em>. <a href="https://doi.org/10.1093/trstmh/trag061" target="_blank" rel="noopener">Read the paper</a>.</p></div></li>
      <li><span class="news__date">2026</span><div><div class="news__title">Preprint on calibrated, interpretable ICU mortality prediction posted to medRxiv</div><p class="news__text">Co-authored with undergraduate researcher Merasia M. Johnson. <a href="https://www.medrxiv.org/content/10.64898/2026.05.30.26354524v1" target="_blank" rel="noopener">Read the preprint</a>.</p></div></li>
      <li><span class="news__date">2026</span><div><div class="news__title">Work-zone safety paper published in the Construction Research Congress 2026 proceedings</div><p class="news__text">Co-authored with former mentee Ann Ubaka; a second CRC 2026 paper on sustainable equipment-fleet management is accepted. <a href="https://ascelibrary.org/doi/10.1061/9780784486993.087" target="_blank" rel="noopener">Read the paper</a>.</p></div></li>
      <li><span class="news__date">2026</span><div><div class="news__title">New preprints on fractional adaptive control and structural identifiability</div><p class="news__text">See <a href="publications.html">Publications</a> for links.</p></div></li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta-panel reveal">
      <div>
        <h2>Interested in joining or collaborating?</h2>
        <p>I welcome prospective graduate and undergraduate students, and collaborators in public health, medicine, and neuroscience who want to work at the interface of mathematics, machine learning, and biomedical science.</p>
      </div>
      <div class="btn-row">
        <a class="btn btn--on-dark" href="group.html#join">Join the group</a>
        <a class="btn btn--on-dark-outline" href="contact.html">Contact</a>
      </div>
    </div>
  </div>
</section>
"""

write("index.html", page("index.html",
    "Abdallah Alsammani, Ph.D. — Mathematical & Scientific Machine Learning for Biomedical Systems",
    "Abdallah Alsammani is Assistant Professor of Mathematics and Data Science at Delaware State University. He develops mathematical models, scientific machine learning, and biomedical data-science methods for infectious disease, clinical prediction, and computational neuroscience.",
    home, ld="person"))


# =============================================================================
# RESEARCH
# =============================================================================
def area(aid, num, title, lead, questions, methods, works):
    q = "".join(f"<li>{x}</li>" for x in questions)
    m = "".join(f'<span class="tag">{x}</span>' for x in methods)
    w = "".join(f'<li><a href="{href}" {"target=_blank rel=noopener" if href.startswith("http") else ""}>{t}</a><span class="muted">{meta}</span></li>' for t, meta, href in works)
    return f"""
<article class="area reveal" id="{aid}">
  <div class="area__num">{num}</div>
  <div>
    <h3>{title}</h3>
    <p class="area__lead">{lead}</p>
    <ul class="area__questions">{q}</ul>
  </div>
  <aside class="area__side">
    <h4>Methods</h4>
    <div class="tags">{m}</div>
    <h4>Representative work</h4>
    <ul>{w}</ul>
  </aside>
</article>"""

research = f"""
<section class="page-header">
  <div class="container">
    <div>
      <h1>Research</h1>
      <p class="page-header__lede">My research is interdisciplinary, integrating applied mathematics, biostatistics, data science, and machine learning to study complex biological, clinical, and public-health systems. The aim is mathematically rigorous, computationally efficient approaches that bridge theory, data, and real-world applications in healthcare and the biomedical sciences.</p>
      <nav class="page-header__nav" aria-label="On this page">
        <a href="#modeling">01 Modeling</a><a href="#sciml">02 Scientific ML</a><a href="#biomed">03 Biomedical Data</a><a href="#neuro">04 Neuroscience</a><a href="#toolkit">Toolkit</a><a href="#funding">Funding</a><a href="#directions">Directions</a>
      </nav>
    </div>
    <div class="page-header__visual">{hero_svg()}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    {area("modeling", "01", "Mathematical Modeling",
      "Deterministic and stochastic models of infectious diseases and biological processes, analyzed with the tools of dynamical systems and control theory.",
      ["How do seasonality, stochastic fluctuations, and delays change the long-term behavior of infection models such as hepatitis B, COVID-19, and cholera?",
       "Which vaccination, treatment, and sanitation strategies are optimal, and how sensitive are they to behavior and economic conditions?",
       "How do within-host and population-level processes couple across scales?"],
      ["ODE / SDE / delay systems", "Stability &amp; bifurcation", "Basic reproduction number", "Optimal control", "Fractional calculus", "Host–pathogen models"],
      [("Impact of vaccination behavior on COVID-19 dynamics and economic outcomes", "Math. Biosci. Eng., 2025", "https://doi.org/10.3934/mbe.2025084"),
       ("Cholera transmission dynamics with sanitation control measures", "arXiv, 2025", "https://arxiv.org/abs/2505.08873"),
       ("Adaptive control and Mittag-Leffler stability of Caputo fractional systems", "arXiv, 2026", "https://arxiv.org/abs/2602.07105"),
       ("Stability analysis of a chemotherapy model with delays", "DCDS-B, 2019", "https://doi.org/10.3934/dcdsb.2019002")])}

    {area("sciml", "02", "Scientific Machine Learning",
      "Physics-informed and data-driven methods for dynamical systems, so that mechanistic structure and observational data inform each other for inference, prediction, and control.",
      ["When a model is combined with a learned component, which parameters remain structurally identifiable from the data that are actually available?",
       "How can neural differential equations and hybrid mechanistic–statistical models encode biological constraints while learning from surveillance and clinical data?",
       "How should uncertainty be quantified and propagated through hybrid models used for forecasting and decision support?"],
      ["Neural differential equations", "Physics-informed learning", "Hybrid modeling", "Structural identifiability", "Symbolic computation", "Uncertainty quantification"],
      [("A tutorial on symbolic structural identifiability analysis of ODE models in Julia", "arXiv, 2026", "https://arxiv.org/abs/2605.18910"),
       ("Stochastic modeling and computational simulations of HBV infection dynamics", "arXiv, 2023", "https://arxiv.org/abs/2308.05819")])}

    {area("biomed", "03", "Biomedical Data Science",
      "Predictive models for clinical outcomes and disease risk that clinicians can trust, and robust statistical methodology for complex, high-dimensional biomedical data.",
      ["Can interpretable, well-calibrated models built from routine clinical data support prognosis where specialist resources are scarce?",
       "How should measurement bias be corrected when estimating circular quantities such as phase?",
       "How do explainable machine-learning models complement classical statistics in public-safety and health datasets?"],
      ["Interpretable ML", "Calibration", "Electronic health records", "Circular statistics", "Bias correction", "Survival &amp; time series", "Bayesian inference"],
      [("Interpretable machine-learning prognosis of mycetoma from routine clinical data", "Trans. R. Soc. Trop. Med. Hyg., 2026", "https://doi.org/10.1093/trstmh/trag061"),
       ("Calibrated and interpretable ML for ICU mortality prediction", "medRxiv preprint, 2026", "https://www.medrxiv.org/content/10.64898/2026.05.30.26354524v1"),
       ("Estimation of circular statistics in the presence of measurement bias", "IEEE J. Biomed. Health Inform., 2024", "https://doi.org/10.1109/JBHI.2023.3334684"),
       ("Predicting sleep disorders using machine learning", "ICCSA, 2025", "https://doi.org/10.1007/978-3-031-97000-9_7")])}

    {area("neuro", "04", "Computational Neuroscience",
      "Statistical and computational analysis of electrophysiological data, centered on high-frequency oscillations in epilepsy and their role in clinical diagnosis and monitoring.",
      ["How do recording duration, sleep stage, and circadian rhythm affect the detection and interpretation of high-frequency oscillations?",
       "How does intracranial monitoring itself alter sleep, and what does that mean for biomarker reliability?",
       "Can automated detection of pathological oscillations be made robust enough for long-term clinical use?"],
      ["Intracranial EEG", "HFO detection", "Sleep &amp; vigilance state", "Phase analysis", "Signal processing"],
      [("Influence of recording duration and vigilance state on HFO characterization in epilepsy", "Neurology, 2026", "https://doi.org/10.1212/WNL.0000000000218225"),
       ("Circadian rhythms in high-frequency oscillations from long-term intracranial EEG", "AI in Epilepsy Conference, 2026", "publications.html"),
       ("Effect of sleep stage on high-frequency oscillations and artifacts", "AES Annual Meeting, 2021", "publications.html")])}
  </div>
</section>

<section class="section section--alt" id="toolkit">
  <div class="container">
    <div class="section-head reveal">
      <h2>Mathematical &amp; computational toolkit</h2>
      <p>A shared set of methods and software used across all four pillars.</p>
    </div>
    <div class="toolkit reveal">
      <div><h3>Mathematical modeling</h3><ul><li>Ordinary &amp; partial differential equations</li><li>Stochastic differential equations</li><li>Dynamical systems &amp; bifurcation theory</li><li>Optimal control theory</li></ul></div>
      <div><h3>Statistics &amp; machine learning</h3><ul><li>Hypothesis testing, regression, survival &amp; time-series analysis</li><li>Bayesian inference, circular statistics</li><li>Supervised &amp; unsupervised learning, deep learning</li><li>Model validation &amp; calibration</li></ul></div>
      <div><h3>Software</h3><ul><li>Python (NumPy, SciPy, pandas, scikit-learn, TensorFlow, Keras)</li><li>R (caret, randomForest, ggplot2), SAS</li><li>MATLAB, Mathematica, Julia, Scilab</li><li>C++, SQL, Tableau, BEAST</li></ul></div>
    </div>
  </div>
</section>

<section class="section" id="funding">
  <div class="container">
    <div class="section-head reveal">
      <h2>Grants &amp; funding</h2>
      <p>Internal and external support for research and education spanning mathematical modeling, biomedical data science, and broadening participation in computational STEM.</p>
    </div>
    <div class="grants reveal">
      <div class="grant-group">
        <h3>Funded</h3>
        <div class="grant"><div class="grant__title">Faculty Summer Research Grant</div><div class="grant__org">Delaware State University · Interdisciplinary research in mathematical modeling, infectious-disease dynamics, and data science</div><div class="grant__meta">Principal Investigator · 2026</div></div>
        <div class="grant"><div class="grant__title">Delaware INBRE Undergraduate Research Program</div><div class="grant__org">Delaware INBRE / Delaware State University · Undergraduate biomedical and data-science research projects</div><div class="grant__meta">Faculty Mentor · 2026</div></div>
        <div class="grant"><div class="grant__title">Grant for Scholarship of Teaching and Learning (SoTL)</div><div class="grant__org">Jacksonville University · Interactive learning modules for undergraduate mathematics and data-science education</div><div class="grant__meta">Principal Investigator · 2023–2024</div></div>
      </div>
      <div class="grant-group grant-group--pending">
        <h3>Under review</h3>
        <div class="grant"><div class="grant__title">Computational STEM Pathways (CSP)</div><div class="grant__org">Alfred P. Sloan Foundation · Lead institution: Delaware State University; partner: Florida A&amp;M University</div><div class="grant__meta">Principal Investigator · 2026</div></div>
        <div class="grant"><div class="grant__title">Computational STEM Pathways (CSP)</div><div class="grant__org">Alfred P. Sloan Foundation · Partner institutions: Hampton University and University of Nevada, Las Vegas</div><div class="grant__meta">Co-Principal Investigator · 2026</div></div>
        <div class="grant"><div class="grant__title">Causal Machine Learning for Equitable STEM Achievement: Evidence from PISA 2022 and NAEP Mathematics</div><div class="grant__org">AERA–NSF Research Grants Program</div><div class="grant__meta">Principal Investigator · 2026</div></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt" id="directions">
  <div class="container">
    <div class="section-head reveal">
      <h2>Where the program is heading</h2>
      <p>Ongoing and planned work that extends each pillar.</p>
    </div>
    <div class="directions reveal">
      <div class="direction"><h3>Hybrid epidemic forecasting</h3><p>Mechanistic compartmental models combined with machine learning to build forecasting systems that encode biological structure while learning from real-time surveillance data.</p></div>
      <div class="direction"><h3>Trustworthy clinical prediction</h3><p>Calibration, uncertainty quantification, and interpretability for clinical models, from ICU outcomes to multimodal electronic-health-record data, with attention to fairness and health disparities.</p></div>
      <div class="direction"><h3>Identifiability and control for hybrid models</h3><p>Neural differential equations, physics-informed learning, and symbolic identifiability analysis as a unified basis for inference and control of biological systems.</p></div>
      <div class="direction"><h3>Automated HFO detection</h3><p>Deep-learning architectures for detecting and classifying pathological high-frequency oscillations in long-term intracranial EEG, building on ongoing clinical collaborations.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta-panel reveal">
      <div>
        <h2>Interested in collaboration?</h2>
        <p>I welcome inquiries from prospective students, postdoctoral researchers, and faculty in public health, medicine, neuroscience, and the mathematical sciences.</p>
      </div>
      <div class="btn-row"><a class="btn btn--on-dark" href="contact.html">Get in touch</a><a class="btn btn--on-dark-outline" href="publications.html">Publications</a></div>
    </div>
  </div>
</section>
"""
write("research.html", page("research.html",
    "Research — Abdallah Alsammani, Ph.D.",
    "Research program in mathematical modeling, scientific machine learning, biomedical data science, and computational neuroscience: questions, methods, representative papers, and funding.",
    research))


# =============================================================================
# PUBLICATIONS
# =============================================================================
years = sorted({p["year"] for p in PUBS}, reverse=True)
counts = {t: sum(1 for p in PUBS if p["type"] == t) for t in TYPE_LABEL}
pub_blocks = []
for y in years:
    items = []
    for p in [p for p in PUBS if p["year"] == y]:
        links = "".join(f'<a href="{u}" target="_blank" rel="noopener">{l} {icon("i-ext")}</a>' for l, u in p["links"])
        links_html = f'<div class="pub__links">{links}</div>' if links else ""
        items.append(f"""
      <article class="pub" data-type="{p['type']}">
        <div>
          <h3 class="pub__title">{p['title']}</h3>
          <p class="pub__authors">{authors_html(p['authors'])}</p>
          <p class="pub__venue">{p['venue']}</p>
        </div>
        <div class="pub__side"><span class="pub__type">{TYPE_LABEL[p['type']]}</span>{links_html}</div>
      </article>""")
    pub_blocks.append(f'<div class="pub-year reveal"><h2 class="pub-year__label">{y}</h2>{"".join(items)}</div>')

FILTER_LABEL = {"journal": "Journal articles", "accepted": "Accepted / in press", "proceedings": "Conference proceedings", "preprint": "Preprints", "abstract": "Conference abstracts", "other": "Other"}
filters = "".join(
    f'<button class="filter-btn" type="button" data-filter="{t}" aria-pressed="false">{FILTER_LABEL[t]} ({counts[t]})</button>'
    for t in ["journal", "accepted", "proceedings", "preprint", "abstract", "other"])

publications = f"""
<section class="page-header page-header--simple">
  <div class="container">
    <div>
      <h1>Publications</h1>
      <p class="page-header__lede">Peer-reviewed journal articles, conference proceedings, preprints, and presentations across mathematical biology, machine learning for health, biostatistics, and computational neuroscience. Grouped by year; use the filters to narrow by type.</p>
      <div class="pub-summary">
        <div><strong>{counts['journal']}</strong><span>journal articles</span></div>
        <div><strong>{counts['accepted']}</strong><span>accepted / in press</span></div>
        <div><strong>{counts['proceedings']}</strong><span>conference proceedings</span></div>
        <div><strong>{counts['preprint']}</strong><span>preprints &amp; working papers</span></div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container container--narrow">
    <div class="pub-toolbar" role="group" aria-label="Filter publications by type">
      <span class="lbl">Show</span>
      <button class="filter-btn" type="button" data-filter="all" aria-pressed="true">All ({len(PUBS)})</button>
      {filters}
    </div>
    {"".join(pub_blocks)}
    <p class="pub-empty" hidden>No publications of this type.</p>
    <div class="btn-row" style="margin-top: var(--s-6)">
      <a class="btn btn--outline" href="{SCHOLAR}" target="_blank" rel="noopener">{icon('i-scholar')} Google Scholar profile</a>
      <a class="btn btn--outline" href="CV.pdf">{icon('i-download')} Download CV</a>
    </div>
  </div>
</section>
"""
write("publications.html", page("publications.html",
    "Publications — Abdallah Alsammani, Ph.D.",
    "Journal articles, conference proceedings, preprints, and presentations by Abdallah Alsammani in mathematical biology, machine learning for health, biostatistics, and computational neuroscience.",
    publications))


# =============================================================================
# RESEARCH GROUP
# =============================================================================
group = f"""
<section class="page-header page-header--simple">
  <div class="container">
    <div>
      <h1>Research Group</h1>
      <p class="page-header__lede">The Applied Mathematics &amp; Data Science group at Delaware State University develops mathematical models and data-driven methods for problems in public health, biomedical science, and computational neuroscience. We are a small, collaborative group committed to rigorous work and to training the next generation of applied mathematicians and data scientists.</p>
      <nav class="page-header__nav" aria-label="On this page"><a href="#pi">Principal Investigator</a><a href="#members">Current students</a><a href="#alumni">Former mentees</a><a href="#join">Join the group</a></nav>
    </div>
  </div>
</section>

<section class="section" id="pi">
  <div class="container">
    <div class="pi-card reveal">
      <div class="pi-card__photo"><img src="assets/img/profile.jpg" alt="Portrait of Abdallah Alsammani" width="160" height="160"></div>
      <div>
        <h3>Abdallah Alsammani, Ph.D.</h3>
        <div class="pi-card__role">Principal Investigator · Assistant Professor of Mathematics and Data Science</div>
        <div class="pi-card__dept">Department of Mathematical Sciences, Delaware State University</div>
        <p>Dr. Alsammani earned his Ph.D. in Applied Mathematics from Auburn University (2020), held postdoctoral appointments in Neurosurgery at the University of Nebraska Medical Center and in Infectious Diseases at the University of Georgia, and was Assistant Professor of Data Science at Jacksonville University before joining Delaware State University in 2025. He is a member of the American Epilepsy Society and the American Mathematical Society.</p>
        <div class="tags"><span class="tag">Mathematical modeling</span><span class="tag">Scientific machine learning</span><span class="tag">Biomedical data science</span><span class="tag">Computational neuroscience</span></div>
        <div class="btn-row"><a class="btn btn--outline" href="cv.html">Curriculum vitae</a><a class="btn btn--ghost" href="mailto:{EMAIL}">{icon('i-mail')} {EMAIL}</a></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt" id="members">
  <div class="container">
    <div class="section-head reveal">
      <h2>Current students</h2>
      <p>Graduate researchers working with the group in the Department of Mathematical Sciences at Delaware State University.</p>
    </div>
    <div class="members reveal">
      <article class="member">
        <div class="member__avatar" aria-hidden="true">JL</div>
        <div><h3>Jing Li</h3><div class="member__role">Ph.D. Student</div></div>
      </article>
      <article class="member">
        <div class="member__avatar" aria-hidden="true">UO</div>
        <div><h3>Uchenna J. Okorie</h3><div class="member__role">Ph.D. Student</div></div>
      </article>
      <article class="member">
        <div class="member__avatar" aria-hidden="true">FO</div>
        <div><h3>Fiona A. Ochieng</h3><div class="member__role">M.S. Student</div></div>
      </article>
    </div>
  </div>
</section>

<section class="section" id="alumni">
  <div class="container container--narrow">
    <div class="section-head reveal">
      <h2>Former Research Mentees</h2>
      <p>Selected undergraduate and graduate research mentorship at Delaware State University and Jacksonville University, spanning biomedical data science, statistical learning, transportation safety, and applied data analytics. Several projects have resulted in peer-reviewed publications and research preprints.</p>
    </div>
    <h3 class="mentees__inst reveal">Delaware State University</h3>
    <table class="mentee-table reveal">
      <thead><tr><th scope="col">Student</th><th scope="col">Research project / scholarly outcome</th><th scope="col">Term</th></tr></thead>
      <tbody>
        <tr><td>Merasia M. Johnson</td><td>Biomedical machine learning for ICU mortality prediction; co-author, <a class="pub-ref" href="https://www.medrxiv.org/content/10.64898/2026.05.30.26354524v1" target="_blank" rel="noopener">Calibrated and Interpretable Machine Learning for ICU Mortality Prediction Using First 24-Hour Clinical Data</a> (medRxiv preprint, 2026).</td><td>Spring 2026</td></tr>
      </tbody>
    </table>
    <h3 class="mentees__inst reveal">Jacksonville University</h3>
    <table class="mentee-table reveal">
      <thead><tr><th scope="col">Student</th><th scope="col">Research project / scholarly outcome</th><th scope="col">Term</th></tr></thead>
      <tbody>
        <tr><td>Sarah Goodyear</td><td>Independent research on statistical learning methods and an industry data-analytics internship; co-author, <a class="pub-ref" href="https://doi.org/10.1007/978-3-031-97000-9_7" target="_blank" rel="noopener">Predicting Sleep Disorders Using Machine Learning: A Comparative Analysis</a> (ICCSA 2025).</td><td>Fall 2024 – Spring 2025</td></tr>
        <tr><td>Holly Gallup</td><td>Data analysis and visualization for animal-shelter outcomes.</td><td>Spring 2025</td></tr>
        <tr><td>Ann Ubaka</td><td>Construction work-zone crash analysis and safety modeling; co-author, <a class="pub-ref" href="https://ascelibrary.org/doi/10.1061/9780784486993.087" target="_blank" rel="noopener">Construction Work Zone Safety: Identifying Critical Crash Factors and Patterns in Florida</a> (Construction Research Congress 2026).</td><td>Fall 2024 – Spring 2025</td></tr>
        <tr><td>Sarah Wehrung</td><td>Road-accident data analytics and visualization.</td><td>Fall 2023</td></tr>
        <tr><td>Rhea White</td><td>Introduction to data science and prediction algorithms in R.</td><td>Fall 2023</td></tr>
        <tr><td>Cody Thomas</td><td>NFL game-prediction modeling using singular value decomposition.</td><td>Spring 2023</td></tr>
      </tbody>
    </table>
  </div>
</section>

<section class="section section--alt" id="join">
  <div class="container">
    <div class="section-head reveal">
      <h2>Interested in joining the research group?</h2>
      <p>I welcome motivated students with backgrounds in mathematics, statistics, computer science, or related quantitative fields. Students drawn to mathematical modeling, machine learning, epidemiology, or computational neuroscience are especially encouraged to reach out.</p>
    </div>
    <div class="join reveal">
      <ol class="join__steps">
        <li><strong>Read a paper or two.</strong><span>Skim the <a href="research.html">research overview</a> and pick one publication close to your interests. Knowing what we do makes the first conversation much more useful.</span></li>
        <li><strong>Email a short introduction.</strong><span>Include your background, the problems you find interesting, your programming experience, and a CV or transcript. A specific question about a paper is always welcome.</span></li>
        <li><strong>Apply to the program.</strong><span>Prospective Ph.D. and M.S. students apply through the Delaware State University graduate program in Mathematical Sciences. Current DSU undergraduates can start with a semester research project or a summer program such as Delaware INBRE.</span></li>
      </ol>
      <aside class="join__aside">
        <h3>What students work on</h3>
        <ul><li>Differential-equation models of disease</li><li>Machine learning on clinical and public-health data</li><li>Scientific computing in Python, R, Julia, or MATLAB</li><li>Analysis of neural and physiological signals</li></ul>
        <div class="btn-row"><a class="btn btn--primary" href="mailto:{EMAIL}?subject=Research%20group%20inquiry">{icon('i-mail')} Email Dr. Alsammani</a></div>
      </aside>
    </div>
  </div>
</section>
"""
write("group.html", page("group.html",
    "Research Group — Abdallah Alsammani, Ph.D.",
    "The Applied Mathematics & Data Science research group at Delaware State University: principal investigator, current members, past mentees, and how to join.",
    group))


# =============================================================================
# TEACHING
# =============================================================================
teaching = f"""
<section class="page-header page-header--simple">
  <div class="container">
    <div>
      <h1>Teaching</h1>
      <p class="page-header__lede">Mathematics gives us the language to describe complex systems precisely and to reason about them with confidence. In every course I teach, the goal is habits of thought that are rigorous, portable, and grounded in first principles: not only how a method works, but why, where its assumptions break, and how it connects to questions beyond the classroom.</p>
      <nav class="page-header__nav" aria-label="On this page"><a href="#approach">Approach</a><a href="#courses">Courses</a><a href="#curriculum">Curriculum</a><a href="#mentoring">Mentoring</a></nav>
    </div>
  </div>
</section>

<section class="section" id="approach">
  <div class="container">
    <div class="section-head reveal">
      <h2>How I teach</h2>
      <p>Three principles organize my classroom practice, whether the course is proof-based analysis or applied machine learning.</p>
    </div>
    <div class="principles reveal">
      <div class="principle"><h3>Theory before application</h3><p>Definitions and central theorems first, worked examples and applications as consequences. In applied courses, every computational technique is preceded by the result that justifies it, so students see computation as an outgrowth of theory rather than a substitute for it.</p></div>
      <div class="principle"><h3>Purposeful computation</h3><p>Laboratory work in Python, R, or MATLAB is tightly coupled to each unit's mathematics. A representative assignment: derive the gradient update for a regularized model, implement it, apply it to real data, and interpret the results in light of both statistical theory and the subject matter.</p></div>
      <div class="principle"><h3>Research-informed examples</h3><p>Optimization illustrated by parameter estimation in epidemic models; conditional probability grounded in diagnostic-screening problems; questions of fairness and bias treated as part of doing applied mathematics responsibly.</p></div>
    </div>
  </div>
</section>

<section class="section section--alt" id="courses">
  <div class="container">
    <div class="section-head reveal">
      <h2>Courses taught</h2>
      <p>Undergraduate and graduate courses across four institutions, spanning pure mathematics, probability and statistics, differential equations, data science, and machine learning.</p>
    </div>
    <div class="courses reveal">
      <div class="course-block">
        <h3>Delaware State University</h3>
        <p class="course-block__meta">Department of Mathematical Sciences · 2025–present</p>
        <ul class="course-list">
          <li><span class="code">MTSC 821</span><span>Scientific Computations I</span><span class="lvl">Graduate</span></li>
          <li><span class="code">MTSC 571</span><span>Complex Analysis</span><span class="lvl">Graduate</span></li>
          <li><span class="code">MTSC 452</span><span>Advanced Calculus II</span><span class="lvl"></span></li>
          <li><span class="code">MTSC 341</span><span>Probability</span><span class="lvl">Online</span></li>
        </ul>
      </div>
      <div class="course-block">
        <h3>Jacksonville University</h3>
        <p class="course-block__meta">School of Science and Mathematics · 2022–2025 · courses developed and taught</p>
        <ul class="course-list">
          <li><span class="code">MATH 470</span><span>Machine Learning Algorithms</span><span class="lvl"></span></li>
          <li><span class="code">MATH 270</span><span>Introduction to Data Science</span><span class="lvl"></span></li>
          <li><span class="code">MATH 170</span><span>Data Science Foundations</span><span class="lvl"></span></li>
          <li><span class="code">MATH 481WS</span><span>Capstone Research Project</span><span class="lvl">Capstone</span></li>
          <li><span class="code">MATH 420</span><span>Linear Algebra II</span><span class="lvl"></span></li>
          <li><span class="code">MATH 331</span><span>Differential Equations</span><span class="lvl"></span></li>
          <li><span class="code">MATH 315</span><span>Probability</span><span class="lvl"></span></li>
          <li><span class="code">MATH 240</span><span>Calculus III</span><span class="lvl"></span></li>
          <li><span class="code">MATH 205</span><span>Elementary Statistics</span><span class="lvl"></span></li>
        </ul>
      </div>
      <div class="course-block course-block--wide">
        <div>
          <h3>Auburn University</h3>
          <p class="course-block__meta">Department of Mathematics and Statistics · Graduate Teaching Assistant &amp; Instructor of Record · 2014–2020</p>
        </div>
        <div>
          <h4>Primary instructor</h4>
          <p class="course-block__note">Calculus I, II, and III; Pre-Calculus; College Algebra.</p>
          <h4 style="margin-top:var(--s-4)">Teaching assistant</h4>
          <p class="course-block__note">Introduction to Statistics, Linear Algebra, Differential Equations.</p>
        </div>
        <div>
          <p class="course-block__note">Supervised the Auburn University Mathematics Tutoring Center for two semesters, coordinating academic support for hundreds of undergraduates. Six years of teaching students with widely varying preparation sharpened the ability to diagnose conceptual gaps and calibrate explanations while keeping standards rigorous.</p>
          <span class="award">{icon('i-award')} Excellence in Teaching Award, 2019–2020</span>
        </div>
      </div>
      <div class="course-block course-block--wide">
        <div>
          <h3>Al Neelain University &amp; Academy of Engineering and Medical Sciences</h3>
          <p class="course-block__meta">Lecturer · Khartoum, Sudan</p>
        </div>
        <div><p class="course-block__note">Real Analysis, Abstract Algebra, Number Theory, Topology, Mathematical Methods, Introduction to Statistics, and MATLAB Programming.</p></div>
        <div><p class="course-block__note">Early teaching in a resource-constrained environment reinforced clarity, precision, and engagement as the foundations of effective instruction.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="curriculum">
  <div class="container">
    <div class="section-head reveal">
      <h2>Curriculum &amp; program development</h2>
      <p>Beyond individual courses, I have helped build programs, assessments, and pedagogical initiatives that strengthen data-science education.</p>
    </div>
    <div class="initiatives reveal">
      <div class="initiative"><h3>Data Science Certificate Program</h3><p>Designed and launched a structured credential pathway in data analysis, machine learning, and statistical computing.</p><span class="muted">Jacksonville University · 2023</span></div>
      <div class="initiative"><h3>Program assessment</h3><p>Assessment Coordinator for the Data Science major and minor: outcomes assessment, alignment of course objectives with program goals, and formal reporting.</p><span class="muted">Jacksonville University · 2022–2025</span></div>
      <div class="initiative"><h3>Scholarship of Teaching &amp; Learning grant</h3><p>Principal investigator for a funded project on interactive learning modules and active-learning strategies in mathematics and data-science courses.</p><span class="muted">Jacksonville University · 2023–2024</span></div>
    </div>
  </div>
</section>

<section class="section section--alt" id="mentoring">
  <div class="container">
    <div class="section-head reveal">
      <h2>Research mentoring &amp; advising</h2>
      <p>Mentorship is a natural extension of classroom teaching: guiding students from their first exposure to research methods through formal presentation of independent work.</p>
    </div>
    <div class="grid grid--2 reveal">
      <div class="prose">
        <h3>Research supervision</h3>
        <p>I currently mentor graduate and undergraduate researchers at Delaware State University, including through the Delaware INBRE Summer Undergraduate Research Program, and previously supervised eight independent undergraduate research projects and student internships at Jacksonville University (MATH 487RI, MATH 490). Students learn to read technical literature critically, formulate precise mathematical and statistical problems, implement and validate computational solutions, and communicate results to varied audiences.</p>
        <p><a class="link-arrow" href="group.html">Meet the research group {icon('i-arrow')}</a></p>
      </div>
      <div class="prose">
        <h3>Academic advising</h3>
        <p>At Jacksonville University I served as academic advisor for eight undergraduate students in the Mathematics and Data Science programs, providing individualized guidance on degree planning, course selection, internships, career exploration, and graduate-school preparation. Supporting students from groups historically underrepresented in the mathematical sciences is a responsibility I hold with conviction: accessible office hours, assignments that build skill in a graduated sequence, and a classroom where rigorous questions are expected and welcomed.</p>
      </div>
    </div>
  </div>
</section>
"""
write("teaching.html", page("teaching.html",
    "Teaching — Abdallah Alsammani, Ph.D.",
    "Teaching philosophy, courses taught at Delaware State University, Jacksonville University, and Auburn University, curriculum development, and research mentoring by Abdallah Alsammani.",
    teaching))


# =============================================================================
# CV
# =============================================================================
def entry(when, what, where, note=""):
    n = f'<div class="cv-entry__note">{note}</div>' if note else ""
    return f'<div class="cv-entry"><div class="cv-entry__when">{when}</div><div><div class="cv-entry__what">{what}</div><div class="cv-entry__where">{where}</div>{n}</div></div>'

cv = f"""
<section class="page-header page-header--simple">
  <div class="container">
    <div>
      <h1>Curriculum Vitae</h1>
      <p class="page-header__lede">Academic appointments, education, honors, service, and skills. Publications and grants are detailed on their own pages. The complete CV is available as a PDF.</p>
      <div class="btn-row" style="margin-top:var(--s-5)">
        <a class="btn btn--primary" href="CV.pdf">{icon('i-download')} Download full CV (PDF)</a>
        <a class="btn btn--outline" href="publications.html">Publications</a>
        <a class="btn btn--outline" href="research.html#funding">Grants</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container cv-layout">
    <nav class="cv-toc" aria-label="CV sections">
      <ul>
        <li><a href="#appointments">Appointments</a></li>
        <li><a href="#education">Education</a></li>
        <li><a href="#honors">Honors &amp; fellowships</a></li>
        <li><a href="#service">Academic service</a></li>
        <li><a href="#development">Professional development</a></li>
        <li><a href="#skills">Technical skills</a></li>
        <li><a href="#memberships">Memberships</a></li>
      </ul>
      <a class="btn btn--outline" href="CV.pdf">{icon('i-download')} PDF</a>
    </nav>
    <div>
      <div class="cv-section" id="appointments">
        <h2>Academic appointments</h2>
        {entry("Aug 2025 – present", "Assistant Professor of Mathematics and Data Science (Tenure-Track)", "Department of Mathematical Sciences, Delaware State University, Dover, DE", "Teaches undergraduate and graduate courses in data science and applied mathematics; establishing a research program in mathematical biology, machine learning, and biomedical data science; mentors graduate and undergraduate researchers.")}
        {entry("Aug 2022 – Jul 2025", "Assistant Professor of Data Science", "School of Science and Mathematics, Jacksonville University, Jacksonville, FL", "Designed and delivered the data-science curriculum; established an undergraduate research program supervising eight independent projects; led assessment for the Data Science major and minor; developed the Data Science Certificate Program; served on the AI Taskforce and Planning &amp; Budget Committee.")}
        {entry("Jan 2022 – Jul 2022", "Postdoctoral Research Associate", "Department of Infectious Diseases, University of Georgia, Athens, GA", "Epidemiological modeling and statistical analysis for CDC-contracted research on infectious-disease dynamics; supervised a research group of seven Ph.D. students.")}
        {entry("Jan 2021 – Jan 2022", "Postdoctoral Research Associate", "Department of Neurosurgery, University of Nebraska Medical Center, Omaha, NE", "Computational methods for intracranial EEG from epilepsy patients; statistical frameworks for detecting and characterizing high-frequency oscillations; circular-statistics methodology published in <em>IEEE JBHI</em>.")}
        {entry("Aug 2014 – Dec 2020", "Graduate Teaching Assistant &amp; Instructor of Record", "Department of Mathematics and Statistics, Auburn University, Auburn, AL", "Primary instructor for the calculus sequence and pre-calculus; supervised the Mathematics Tutoring Center; Excellence in Teaching Award (2019–2020).")}
        {entry("Aug 2012 – Aug 2013", "Lecturer of Mathematics and Statistics", "Al Neelain University, Khartoum, Sudan")}
        {entry("Aug 2012 – Aug 2013", "Lecturer of Applied Mathematics", "Academy of Engineering and Medical Sciences, Khartoum, Sudan")}
      </div>

      <div class="cv-section" id="education">
        <h2>Education</h2>
        {entry("2020", "Ph.D. in Applied Mathematics", "Auburn University, Auburn, AL", "Dissertation: <em>Dynamical Behavior of Nonautonomous and Stochastic HBV Infection Model</em>. Focus: mathematical modeling of infectious diseases, stochastic differential equations, dynamical systems.")}
        {entry("2014", "Postgraduate Diploma in Mathematics", "International Centre for Theoretical Physics (ICTP), Trieste, Italy", "Pre-doctoral program in advanced mathematical methods. Thesis: <em>Alexander Polynomials for Knots</em>.")}
        {entry("2012", "M.Sc. in Applied Mathematics", "African Institute for Mathematical Sciences (AIMS), Mbour, Senegal", "Thesis: <em>Elliptic Curve Cryptography Under Finite Field</em>.")}
        {entry("2009", "B.Sc. in Mathematics (Honors)", "Al Neelain University, Khartoum, Sudan", "Outstanding Student Award. Thesis: <em>Linear and Nonlinear Optimization Problems</em>.")}
      </div>

      <div class="cv-section" id="honors">
        <h2>Honors, awards &amp; fellowships</h2>
        {entry("2019 – 2020", "Excellence in Teaching Award", "Department of Mathematics and Statistics, Auburn University")}
        {entry("2014 – 2020", "Graduate Teaching Assistantship", "Auburn University — six years of full funding")}
        {entry("2013 – 2014", "Pre-Ph.D. Fellowship in Mathematics", "International Centre for Theoretical Physics (ICTP), Trieste, Italy")}
        {entry("2011 – 2012", "Master's Scholarship in Applied Mathematics", "African Institute for Mathematical Sciences (AIMS), Senegal")}
        {entry("2004 – 2009", "Outstanding Undergraduate Student Award", "Al Neelain University, Khartoum, Sudan")}
      </div>

      <div class="cv-section" id="service">
        <h2>Academic service</h2>
        <h3 style="font-family:var(--font-sans);font-size:var(--fs-base);margin-bottom:var(--s-3)">University-level · Jacksonville University</h3>
        {entry("2024 – 2025", "Member, Planning and Budget Committee", "Jacksonville University")}
        {entry("2023 – 2024", "Member, Artificial Intelligence Taskforce Committee", "Jacksonville University")}
        {entry("2023 – 2024", "Faculty search committees", "Assistant Professor in Computing Science (Davis College of Business); Assistant Professor in Mathematical Physics; Assistant Professor in Oceanography (Marine Science Department)")}
        {entry("2022 – 2023", "Faculty search committees", "Assistant Dean, Davis College of Business; Visiting Assistant Professor in Mathematics")}
        <h3 style="font-family:var(--font-sans);font-size:var(--fs-base);margin:var(--s-5) 0 var(--s-3)">Departmental &amp; college · Jacksonville University</h3>
        {entry("2022 – 2025", "Assessment Coordinator, Data Science Programs", "Jacksonville University")}
        {entry("2023", "Developed the Data Science Certificate Program", "Jacksonville University")}
        {entry("2022 – 2023", "Member, Applied Science Committee", "College of Arts and Sciences, Jacksonville University")}
        <h3 style="font-family:var(--font-sans);font-size:var(--fs-base);margin:var(--s-5) 0 var(--s-3)">Professional service &amp; outreach</h3>
        {entry("2026", "Faculty Mentor, Delaware INBRE Undergraduate Research Program", "Delaware INBRE / Delaware State University")}
        {entry("Mar 2018", "Organizing Committee, 52nd Spring Topology and Dynamical Systems Conference", "Auburn University")}
        {entry("Mar 2017", "Event Coordinator, Regional Science Olympiad", "Auburn University")}
      </div>

      <div class="cv-section" id="development">
        <h2>Professional development</h2>
        {entry("Completed", "Biostatistics Professional Certificate", "Johns Hopkins University (Coursera)", "Summary Statistics, Hypothesis Testing, Simple Regression, and Multiple Regression Analysis in Public Health.")}
        {entry("Completed", "FlexStack: Python Fundamentals Certificate", "Georgia Institute of Technology", "Foundations and Syntax; Data Structures and Modules; Web Technologies and Data Processing.")}
        {entry("In progress", "Google Data Analytics Professional Certificate", "Google / Coursera", "5 of 8 courses completed.")}
      </div>

      <div class="cv-section" id="skills">
        <h2>Technical skills</h2>
        <ul class="cv-list">
          <li><strong>Statistical computing:</strong> R, SAS, Python (NumPy, SciPy, pandas, statsmodels)</li>
          <li><strong>Mathematical modeling:</strong> MATLAB, Mathematica, Scilab, Julia</li>
          <li><strong>Machine learning:</strong> Python (scikit-learn, TensorFlow, Keras), R (caret, randomForest)</li>
          <li><strong>Visualization:</strong> Matplotlib, Seaborn, ggplot2, Tableau</li>
          <li><strong>Other languages:</strong> C++, SQL</li>
          <li><strong>Specialized software:</strong> BEAST (Bayesian evolutionary analysis)</li>
          <li><strong>Statistical methods:</strong> hypothesis testing, regression, survival and time-series analysis, Bayesian inference, circular statistics</li>
          <li><strong>Machine learning:</strong> supervised and unsupervised learning, deep learning, model validation</li>
          <li><strong>Mathematical modeling:</strong> ODEs, PDEs, SDEs, dynamical systems, optimal control</li>
          <li><strong>Data science:</strong> data wrangling, exploratory analysis, feature engineering, predictive modeling, big-data analytics</li>
          <li><strong>Operating systems:</strong> Windows, Linux (Ubuntu, Mint), macOS</li>
        </ul>
      </div>

      <div class="cv-section" id="memberships">
        <h2>Professional memberships</h2>
        <ul class="cv-list"><li>American Epilepsy Society (AES)</li><li>American Mathematical Society (AMS)</li></ul>
      </div>
    </div>
  </div>
</section>
"""
write("cv.html", page("cv.html",
    "Curriculum Vitae — Abdallah Alsammani, Ph.D.",
    "Academic appointments, education, honors, service, professional development, and technical skills of Abdallah Alsammani, with the full CV available as a PDF.",
    cv))


# =============================================================================
# CONTACT
# =============================================================================
contact = f"""
<section class="page-header page-header--simple">
  <div class="container">
    <div>
      <h1>Contact</h1>
      <p class="page-header__lede">I welcome inquiries about research collaboration, graduate and undergraduate advising, seminar and conference invitations, and consulting on mathematical modeling and biomedical data analysis.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="contact reveal">
      <div>
        <ul class="contact-list">
          <li><span class="ic">{icon('i-mail')}</span><div><h3>Email</h3><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
          <li><span class="ic">{icon('i-phone')}</span><div><h3>Office phone</h3><p>{PHONE}</p></div></li>
          <li><span class="ic">{icon('i-building')}</span><div><h3>Office</h3><p>Department of Mathematical Sciences<br>Delaware State University<br>1200 N. DuPont Highway<br>Dover, DE 19901, USA</p></div></li>
          <li><span class="ic">{icon('i-users')}</span><div><h3>Profiles</h3><p><a href="{SCHOLAR}" target="_blank" rel="noopener">Google Scholar</a> · <a href="{GITHUB}" target="_blank" rel="noopener">GitHub</a> · <a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></p></div></li>
        </ul>
      </div>
      <div class="contact-map">
        <iframe src="https://www.google.com/maps?q=Delaware%20State%20University%2C%201200%20N%20DuPont%20Hwy%2C%20Dover%2C%20DE%2019901&output=embed" title="Map showing Delaware State University, Dover, Delaware" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section-head reveal">
      <h2>Ways to work together</h2>
    </div>
    <ul class="reasons reveal">
      <li><strong>Research collaboration</strong>Modeling, machine learning, or statistical analysis for projects in public health, medicine, or neuroscience. Clinical and epidemiological collaborators with data and a question are especially welcome.</li>
      <li><strong>Prospective students</strong>Graduate and undergraduate students interested in mathematical modeling, scientific machine learning, or biomedical data science. See <a href="group.html#join">how to join the group</a>.</li>
      <li><strong>Talks and seminars</strong>Invitations for departmental seminars, conference sessions, and outreach on mathematics, data science, and their biomedical applications.</li>
      <li><strong>Consulting</strong>Quantitative advice on model design, identifiability, prediction, and interpretation for health-related datasets.</li>
    </ul>
  </div>
</section>
"""
write("contact.html", page("contact.html",
    "Contact — Abdallah Alsammani, Ph.D.",
    "Contact Abdallah Alsammani, Assistant Professor of Mathematics and Data Science at Delaware State University, for research collaboration, advising, talks, and consulting.",
    contact))
