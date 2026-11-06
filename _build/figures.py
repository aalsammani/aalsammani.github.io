import math
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


# ------------------------------------------------------------ hero visual
def hero_svg():
    """Phase portrait: spiral trajectories converging to a stable focus, with a
    faint vector field and a shaded uncertainty band on one trajectory."""
    W = H = 360
    cx, cy = 180, 182
    DECAY = 0.16  # shared by the vector field and the trajectories
    parts = []
    parts.append(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="hero-viz-t">')
    parts.append('<title id="hero-viz-t">Phase portrait of a dynamical system: trajectories spiral toward a stable equilibrium</title>')
    parts.append('<defs><radialGradient id="hg" cx="50%" cy="50%" r="55%"><stop offset="0" stop-color="#2E7D86" stop-opacity=".10"/><stop offset="1" stop-color="#2E7D86" stop-opacity="0"/></radialGradient></defs>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="172" fill="url(#hg)"/>')
    # faint grid
    g = ['<g stroke="#294766" stroke-opacity=".07" stroke-width="1">']
    for i in range(20, W, 40):
        g.append(f'<line x1="{i}" y1="18" x2="{i}" y2="{H-18}"/>')
        g.append(f'<line x1="18" y1="{i}" x2="{W-18}" y2="{i}"/>')
    g.append('</g>')
    parts.append("".join(g))
    # vector field ticks
    vf = ['<g stroke="#294766" stroke-opacity=".22" stroke-width="1.1" stroke-linecap="round">']
    for gx in range(40, W, 40):
        for gy in range(40, H, 40):
            x, y = (gx - cx) / 60.0, (gy - cy) / 60.0
            # linear spiral sink dx/dt = -k x - y, dy/dt = x - k y with k = DECAY, whose
            # solutions are exactly r = r0 exp(-k t), angle = angle0 + t (the spirals below)
            dx, dy = -DECAY * x - y, x - DECAY * y
            n = math.hypot(dx, dy) or 1
            dx, dy = dx / n * 7, dy / n * 7
            vf.append(f'<line x1="{gx-dx/2:.1f}" y1="{gy-dy/2:.1f}" x2="{gx+dx/2:.1f}" y2="{gy+dy/2:.1f}"/>')
    vf.append('</g>')
    parts.append("".join(vf))

    def spiral(r0, phase, decay=DECAY, tmax=13.5, step=0.08):
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
    parts.append(f'<path d="{band_d}" fill="#8FB3D1" fill-opacity=".16"/>')

    specs = [(160, 0.0, "#294766", .85, 1.7), (150, 2.3, "#2E7D86", .9, 1.8), (165, 4.1, "#294766", .55, 1.3), (120, 1.2, "#2E7D86", .5, 1.1)]
    for r0, ph, col, op, sw in specs:
        parts.append(f'<path class="traj" pathLength="1" d="{path(spiral(r0, ph))}" fill="none" stroke="{col}" stroke-opacity="{op}" stroke-width="{sw}" stroke-linecap="round"/>')
    # sample points on the second trajectory
    for k, (x, y) in enumerate(spiral(150, 2.3, step=0.5)):
        if k % 2 == 0 and k < 22:
            parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" fill="#fff" stroke="#2E7D86" stroke-width="1.4"/>')
    # equilibrium
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="4.5" fill="#294766"/><circle cx="{cx}" cy="{cy}" r="9" fill="none" stroke="#294766" stroke-opacity=".35"/>')
    # equation label
    parts.append('<text x="30" y="40" font-family="Source Serif 4, Georgia, serif" font-style="italic" font-size="15" fill="#294766" fill-opacity=".75">dx/dt = f(x, θ) + g(x; φ)</text>')
    parts.append('<text x="30" y="58" font-family="Source Sans 3, sans-serif" font-size="11" fill="#4B5866" fill-opacity=".8">mechanistic model + learned component</text>')
    parts.append('</svg>')
    return "".join(parts)


# ---------------------------------------------------- featured project figures
FIG_HYBRID = """<svg viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Schematic: SIR compartmental model whose transmission rate is supplied by a learned component, and the structural identifiability question posed before fitting">
<g font-family="Source Sans 3, sans-serif" font-size="11" fill="#294766">
<rect x="22" y="70" width="52" height="34" rx="6" fill="#fff" stroke="#294766" stroke-width="1.4"/><text x="48" y="92" text-anchor="middle" font-weight="600">S</text>
<rect x="124" y="70" width="52" height="34" rx="6" fill="#fff" stroke="#294766" stroke-width="1.4"/><text x="150" y="92" text-anchor="middle" font-weight="600">I</text>
<rect x="226" y="70" width="52" height="34" rx="6" fill="#fff" stroke="#294766" stroke-width="1.4"/><text x="252" y="92" text-anchor="middle" font-weight="600">R</text>
<path d="M74 87h44M176 87h44" stroke="#294766" stroke-width="1.4"/><path d="M114 83l6 4-6 4M216 83l6 4-6 4" fill="none" stroke="#294766" stroke-width="1.4"/>
<text x="96" y="80" text-anchor="middle" font-style="italic" font-size="11" fill="#2E7D86">β(t)</text>
<text x="198" y="80" text-anchor="middle" font-style="italic" font-size="11">γ</text>
<g stroke="#2E7D86" stroke-width="1.2" fill="#fff"><circle cx="82" cy="32" r="4"/><circle cx="82" cy="46" r="4"/><circle cx="96" cy="39" r="4"/><circle cx="110" cy="32" r="4"/><circle cx="110" cy="46" r="4"/></g>
<g stroke="#2E7D86" stroke-width=".9" stroke-opacity=".6"><path d="M86 32l6 7M86 46l6-7M100 39l6-7M100 39l6 7"/></g>
<path d="M96 52v20" stroke="#2E7D86" stroke-width="1.2" stroke-dasharray="3 2"/>
<text x="126" y="42" font-size="10" fill="#2E7D86">learned rate</text>
<path d="M22 124h256" stroke="#294766" stroke-opacity=".12"/>
<text x="22" y="141" font-size="11" fill="#4B5866">Before fitting:</text>
<text x="22" y="157" font-size="10.5">which of β(t), γ, and the initial state does the</text>
<text x="22" y="171" font-size="10.5">observed output determine? Structural identifiability</text>
<text x="22" y="185" font-size="10.5" fill="#4B5866">analysis answers this from the model equations alone.</text>
</g></svg>"""

def _fig_epi():
    """SIR model with vaccination of susceptibles at a constant per capita rate nu,
        dS/dt = -beta S I - nu S,   dI/dt = beta S I - gamma I,
    with beta = 0.3/day, gamma = 0.1/day (R0 = 3), I(0) = 0.001, solved by RK4 over
    120 days for a low (nu = 0.002/day) and a high (nu = 0.01/day) vaccination rate.
    Synthetic illustration of the qualitative effect only; not output of the MBE paper."""
    beta, gamma, T, n = 0.3, 0.1, 120.0, 1200
    def run(nu):
        S, I, h, out = 0.999, 0.001, T / n, [(0.0, 0.001)]
        f = lambda S, I: (-beta * S * I - nu * S, beta * S * I - gamma * I)
        for k in range(n):
            a = f(S, I); b = f(S + h / 2 * a[0], I + h / 2 * a[1]); c = f(S + h / 2 * b[0], I + h / 2 * b[1]); d = f(S + h * c[0], I + h * c[1])
            S += h / 6 * (a[0] + 2 * b[0] + 2 * c[0] + d[0]); I += h / 6 * (a[1] + 2 * b[1] + 2 * c[1] + d[1])
            out.append(((k + 1) * h, I))
        return out
    low, high = run(0.002), run(0.01)
    ymax = max(i for _, i in low) * 1.12
    X = lambda t: 34 + t / T * 240
    Y = lambda i: 168 - i / ymax * 140
    path = lambda c: "M" + " L".join(f"{X(t):.1f},{Y(i):.1f}" for t, i in c[::8])
    return ('<svg viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Chart computed from an SIR model with vaccination: '
            'the infectious fraction over time for a low and a high vaccination rate; higher vaccination gives a later and much smaller epidemic peak. Synthetic illustration.">'
            '<g font-family="Source Sans 3, sans-serif" font-size="10" fill="#4B5866">'
            '<path d="M34 24v144h240" stroke="#294766" stroke-opacity=".35" fill="none"/>'
            '<path d="M34 120h240M34 72h240" stroke="#294766" stroke-opacity=".07"/>'
            f'<path d="{path(low)}" fill="none" stroke="#294766" stroke-width="2"/>'
            f'<path d="{path(high)}" fill="none" stroke="#2E7D86" stroke-width="2"/>'
            '<text x="40" y="20">infectious fraction I(t)</text><text x="274" y="184" text-anchor="end">time (days)</text>'
            '<text x="34" y="184">synthetic SIR model with vaccination</text>'
            '<g transform="translate(150 24)"><rect width="122" height="30" rx="5" fill="#fff" stroke="#294766" stroke-opacity=".15"/>'
            '<path d="M8 11h14" stroke="#294766" stroke-width="2"/><text x="27" y="14">low vaccination rate</text>'
            '<path d="M8 23h14" stroke="#2E7D86" stroke-width="2"/><text x="27" y="26">high vaccination rate</text></g>'
            '</g></svg>')
FIG_EPI = _fig_epi()

FIG_IEEG = """<svg viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Schematic, not patient data: intracranial EEG trace with detected high frequency oscillation events, more frequent during NREM sleep than wakefulness">
<g font-family="Source Sans 3, sans-serif" font-size="10" fill="#4B5866">
<rect x="24" y="34" width="60" height="110" fill="#294766" fill-opacity=".04"/><rect x="84" y="34" width="86" height="110" fill="#2E7D86" fill-opacity=".10"/><rect x="170" y="34" width="46" height="110" fill="#294766" fill-opacity=".04"/><rect x="216" y="34" width="62" height="110" fill="#2E7D86" fill-opacity=".10"/>
<text x="54" y="48" text-anchor="middle">wake</text><text x="127" y="48" text-anchor="middle" fill="#294766" font-weight="600">NREM</text><text x="193" y="48" text-anchor="middle">wake</text><text x="247" y="48" text-anchor="middle" fill="#294766" font-weight="600">NREM</text>
<path d="M24 80q4-8 8 0t8 0 8-6 8 6 8 0 8-10 8 10 8 0 8-4 8 4 8 0 8-12 8 12 8 0 8-6 8 6 8 0 8-3 8 3 8 0 8-9 8 9 8 0 8-5 8 5 8 0 8-11 8 11 8 0 8-4 8 4" fill="none" stroke="#294766" stroke-width="1.1" stroke-opacity=".75"/>
<g stroke="#2E7D86" stroke-width="1.8" stroke-linecap="round">
<path d="M40 114v14M62 114v14"/>
<path d="M90 108v20M98 108v20M108 108v20M116 108v20M126 108v20M134 108v20M146 108v20M156 108v20"/>
<path d="M182 114v14M204 114v14"/>
<path d="M222 108v20M232 108v20M240 108v20M250 108v20M260 108v20M270 108v20"/>
</g>
<text x="24" y="160">HFO events</text><text x="150" y="182" text-anchor="middle">recording duration →</text>
<path d="M24 144h254" stroke="#294766" stroke-opacity=".25"/>
</g></svg>"""


FIG_UQ = """<svg viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Uncertainty propagation: an ensemble of SIR trajectories with the transmission rate varied within twenty percent produces a band of possible epidemic curves around the nominal one">
<g font-family="Source Sans 3, sans-serif" font-size="10" fill="#4B5866">
<path d="M40 30v140h250" stroke="#294766" stroke-opacity=".4" fill="none"/>
<path d="M40.0,166.0 L43.1,163.6 L46.2,160.0 L49.4,154.4 L52.5,146.0 L55.6,134.2 L58.8,118.3 L61.9,98.8 L65.0,77.6 L68.1,57.6 L71.2,42.4 L74.4,33.9 L77.5,32.4 L80.6,36.8 L83.8,45.1 L86.9,53.4 L90.0,61.0 L93.1,68.1 L96.2,74.6 L99.4,80.6 L102.5,86.1 L105.6,91.2 L108.8,96.0 L111.9,100.4 L115.0,104.7 L118.1,109.3 L121.2,114.1 L124.4,118.9 L127.5,123.5 L130.6,127.9 L133.8,132.1 L136.9,136.1 L140.0,139.7 L143.1,143.0 L146.2,146.0 L149.4,148.7 L152.5,151.1 L155.6,153.3 L158.8,155.3 L161.9,157.0 L165.0,158.6 L168.1,160.0 L171.2,161.2 L174.4,162.2 L177.5,163.2 L180.6,164.0 L183.8,164.8 L186.9,165.4 L190.0,166.0 L193.1,166.5 L196.2,166.9 L199.4,167.3 L202.5,167.6 L205.6,167.9 L208.8,168.2 L211.9,168.4 L215.0,168.6 L218.1,168.8 L221.2,168.9 L224.4,169.1 L227.5,169.2 L230.6,169.3 L233.8,169.4 L236.9,169.5 L240.0,169.5 L243.1,169.6 L246.2,169.6 L249.4,169.7 L252.5,169.7 L255.6,169.8 L258.8,169.8 L261.9,169.8 L265.0,169.8 L268.1,169.9 L271.2,169.9 L274.4,169.9 L277.5,169.9 L280.6,169.9 L283.8,169.9 L286.9,169.9 L290.0,169.9 L290.0,170.0 L286.9,170.0 L283.8,170.0 L280.6,170.0 L277.5,170.0 L274.4,170.0 L271.2,170.0 L268.1,170.0 L265.0,170.0 L261.9,170.0 L258.8,170.0 L255.6,170.0 L252.5,170.0 L249.4,170.0 L246.2,170.0 L243.1,170.0 L240.0,170.0 L236.9,170.0 L233.8,170.0 L230.6,169.9 L227.5,169.9 L224.4,169.9 L221.2,169.9 L218.1,169.9 L215.0,169.9 L211.9,169.8 L208.8,169.8 L205.6,169.8 L202.5,169.7 L199.4,169.7 L196.2,169.6 L193.1,169.6 L190.0,169.5 L186.9,169.4 L183.8,169.3 L180.6,169.1 L177.5,169.0 L174.4,168.8 L171.2,168.6 L168.1,168.3 L165.0,168.0 L161.9,167.6 L158.8,167.1 L155.6,166.6 L152.5,166.0 L149.4,165.2 L146.2,164.3 L143.1,163.2 L140.0,161.9 L136.9,160.4 L133.8,158.7 L130.6,156.6 L127.5,154.1 L124.4,151.1 L121.2,147.7 L118.1,143.7 L115.0,138.9 L111.9,133.4 L108.8,127.0 L105.6,119.7 L102.5,111.3 L99.4,101.9 L96.2,91.4 L93.1,93.5 L90.0,97.0 L86.9,101.7 L83.8,107.6 L80.6,114.1 L77.5,120.9 L74.4,127.7 L71.2,134.1 L68.1,140.1 L65.0,145.3 L61.9,149.9 L58.8,153.8 L55.6,157.0 L52.5,159.6 L49.4,161.8 L46.2,163.5 L43.1,164.9 L40.0,166.0 Z" fill="#2E7D86" fill-opacity=".18"/>
<path d="M40.0,166.0 L43.1,164.3 L46.2,161.9 L49.4,158.7 L52.5,154.2 L55.6,148.2 L58.8,140.3 L61.9,130.5 L65.0,118.9 L68.1,105.8 L71.2,92.4 L74.4,79.8 L77.5,69.4 L80.6,62.2 L83.8,58.8 L86.9,59.1 L90.0,62.4 L93.1,68.1 L96.2,75.3 L99.4,83.4 L102.5,91.8 L105.6,100.1 L108.8,108.0 L111.9,115.4 L115.0,122.2 L118.1,128.3 L121.2,133.7 L124.4,138.6 L127.5,142.8 L130.6,146.6 L133.8,149.8 L136.9,152.7 L140.0,155.1 L143.1,157.2 L146.2,159.0 L149.4,160.6 L152.5,162.0 L155.6,163.1 L158.8,164.1 L161.9,165.0 L165.0,165.7 L168.1,166.3 L171.2,166.9 L174.4,167.3 L177.5,167.7 L180.6,168.0 L183.8,168.3 L186.9,168.6 L190.0,168.8 L193.1,169.0 L196.2,169.1 L199.4,169.2 L202.5,169.4 L205.6,169.4 L208.8,169.5 L211.9,169.6 L215.0,169.7 L218.1,169.7 L221.2,169.7 L224.4,169.8 L227.5,169.8 L230.6,169.8 L233.8,169.9 L236.9,169.9 L240.0,169.9 L243.1,169.9 L246.2,169.9 L249.4,169.9 L252.5,169.9 L255.6,170.0 L258.8,170.0 L261.9,170.0 L265.0,170.0 L268.1,170.0 L271.2,170.0 L274.4,170.0 L277.5,170.0 L280.6,170.0 L283.8,170.0 L286.9,170.0 L290.0,170.0" fill="none" stroke="#2E7D86" stroke-width="2"/>
<text x="44" y="28">infectious fraction</text><text x="230" y="184">time (days)</text>
<text x="165" y="60" text-anchor="middle">β ∈ [0.8β₀, 1.2β₀], γ fixed</text>
<text x="165" y="74" text-anchor="middle" fill="#2E7D86">envelope of 30 SIR trajectories; nominal β₀ in bold</text>
</g></svg>"""

FIG_NODE = """<svg viewBox="0 0 300 210" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Neural differential equation architecture: the state x at time t enters a mechanistic vector field and a neural network; their sum is integrated by an ODE solver to give the state at a later time, and gradients flow back through the solver to both parameter sets">
<g font-family="Source Sans 3, sans-serif" font-size="11" fill="#1F2933">
<text x="150" y="18" text-anchor="middle" font-size="11" fill="#4B5866">dx/dt = f(x, θ) + g(x; φ)</text>
<rect x="14" y="80" width="54" height="34" rx="5" fill="#fff" stroke="#294766" stroke-width="1.3"/><text x="41" y="101" text-anchor="middle" font-style="italic">x(t)</text>
<rect x="100" y="34" width="74" height="40" rx="5" fill="#fff" stroke="#294766" stroke-width="1.3"/><text x="137" y="51" text-anchor="middle">mechanism</text><text x="137" y="66" text-anchor="middle" font-style="italic">f(x, θ)</text>
<rect x="100" y="120" width="74" height="40" rx="5" fill="#fff" stroke="#2E7D86" stroke-width="1.3"/><text x="137" y="137" text-anchor="middle" fill="#2E7D86">neural network</text><text x="137" y="152" text-anchor="middle" font-style="italic" fill="#2E7D86">g(x; φ)</text>
<circle cx="205" cy="97" r="11" fill="#fff" stroke="#294766" stroke-width="1.3"/><text x="205" y="101" text-anchor="middle" font-size="14">+</text>
<rect x="232" y="80" width="56" height="34" rx="5" fill="#fff" stroke="#294766" stroke-width="1.3"/><text x="260" y="96" text-anchor="middle" font-size="10">ODE solver</text><text x="260" y="108" text-anchor="middle" font-size="10">x(t+Δt)</text>
<g stroke="#294766" stroke-width="1.2" fill="none"><path d="M68 97h16v-43h16M68 97h16v43h16M174 54h20v32M174 140h20v-32M216 97h16"/></g>
<path d="M260 114v60H41v-46" fill="none" stroke="#7A8794" stroke-width="1" stroke-dasharray="3 3"/>
<text x="150" y="196" text-anchor="middle" font-size="10" fill="#4B5866">gradients flow back through the solver to θ and φ</text>
</g></svg>"""

# ------------------------------------------------ generated pillar animations
def _anim_sciml():
    """Phase portrait of dx/dt = f(x) + g(x) in the plane, with the mechanism f a linear
    spiral sink, f(x, y) = (-a x + w y, -w x - a y), and the 'learned correction' g a cubic
    radial damping, g = -c (x^2 + y^2) (x, y); a = 0.15, w = 1, c = 0.05.  The field ticks,
    the three trajectories (RK4), and the moving particles all come from this one system, so
    the particles travel exactly along the drawn flow toward the stable equilibrium (origin)."""
    a, w, c = 0.15, 1.0, 0.05
    cx, cy, sx, sy = 150.0, 104.0, 60.0, 37.5            # model -> SVG: X = cx + sx x, Y = cy - sy y
    F = lambda x, y: (-a * x + w * y - c * (x * x + y * y) * x, -w * x - a * y - c * (x * x + y * y) * y)
    def traj(x, y, T=11.0, h=0.01):
        pts = [(x, y)]
        for k in range(int(round(T / h))):
            k1 = F(x, y); k2 = F(x + h / 2 * k1[0], y + h / 2 * k1[1]); k3 = F(x + h / 2 * k2[0], y + h / 2 * k2[1]); k4 = F(x + h * k3[0], y + h * k3[1])
            x += h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]); y += h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
            if k % 8 == 7: pts.append((x, y))
        return "M" + " L".join(f"{cx + sx * u:.1f},{cy - sy * v:.1f}" for u, v in pts)
    ticks = []
    for X in range(30, 271, 30):
        for Y in range(24, 190, 26):
            x, y = (X - cx) / sx, (cy - Y) / sy
            if x * x + y * y < 0.15: continue
            u, v = F(x, y); U, V = sx * u, -sy * v; n = (U * U + V * V) ** 0.5 or 1
            U, V = U / n * 2.6, V / n * 2.6
            ticks.append(f'<line x1="{X - U:.1f}" y1="{Y - V:.1f}" x2="{X + U:.1f}" y2="{Y + V:.1f}"/>')
    paths = [traj(2.0, 0.0), traj(-1.0, -2.0), traj(-1.0, 2.0)]
    out = ['<svg viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Animated phase portrait computed from one dynamical system: particles move along the flow toward a stable equilibrium; the vector field is a linear mechanistic term plus a nonlinear correction standing in for a learned component">',
           '<g stroke="#294766" stroke-opacity=".18" stroke-width="1" stroke-linecap="round">' + "".join(ticks) + '</g>']
    out += [f'<path d="{d}" fill="none" stroke="#294766" stroke-opacity=".28" stroke-width="1"/>' for d in paths]
    for k, d in enumerate(paths):
        for j, col in enumerate(("#294766", "#2E7D86")):
            out.append(f'<circle class="pa-flow" r="3.2" fill="{col}" style="offset-path:path(\'{d}\');animation-delay:-{1.3 * (2 * k + j):.1f}s"/>')
    out.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="4" fill="#294766"/>')
    out.append('<g font-family="Source Sans 3, sans-serif" font-size="10" fill="#4B5866"><text x="12" y="18" font-style="italic">dx/dt = f(x, θ) + g(x; φ)</text><text x="12" y="190">mechanism + learned correction</text></g></svg>')
    return "".join(out)


def _anim_neuro():
    """Synthetic intracranial EEG for the scrolling animation: a background built from
    sinusoids whose periods divide the 300 px scroll length (so the loop is seamless) plus
    smoothed periodic pseudo-random noise, with brief high frequency bursts (Gaussian envelope,
    3.2 px period, far faster than the background) centred exactly on the event markers.
    Illustration only, not patient data."""
    import random
    rng = random.Random(7)
    raw = [rng.gauss(0, 1) for _ in range(300)]
    noise = [sum(raw[(i + k) % 300] for k in range(-3, 4)) / 7 ** 0.5 for i in range(300)]  # smoothed, still periodic
    events = (55, 125, 235)
    def v(x):
        base = 17 * math.sin(2 * math.pi * x / 75) + 7 * math.sin(2 * math.pi * x / 30 + 1.0) + 1.6 * noise[int(x) % 300]
        burst = sum(15 * math.exp(-((x % 300 - e) / 6.0) ** 2) * math.sin(2 * math.pi * x / 3.2) for e in events)
        return 100 - base - burst
    xs = [i * 0.4 for i in range(int(600 / 0.4) + 1)]
    d = "M" + " L".join(f"{x:.1f},{v(x):.1f}" for x in xs)
    marks = "".join(f'<path d="M{e + o} 150v18" stroke="#2E7D86" stroke-width="2"/>' for o in (0, 300) for e in events)
    return ('<svg viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Animated synthetic intracranial EEG trace scrolling continuously, with brief high frequency bursts marked below as detected events; illustration only, not patient data">'
            '<defs><clipPath id="clip-eeg"><rect x="0" y="0" width="300" height="200"/></clipPath></defs><g clip-path="url(#clip-eeg)"><g class="pa-scroll">'
            f'<path d="{d}" fill="none" stroke="#294766" stroke-width="1.1"/>{marks}</g></g>'
            '<g font-family="Source Sans 3, sans-serif" font-size="10" fill="#4B5866"><text x="12" y="18">intracranial EEG (synthetic)</text><text x="12" y="190">high frequency oscillation events</text></g></svg>')


ANIM_MODELING = '''<svg viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Animated epidemic curves: the infectious fraction over time for three transmission rates, drawn repeatedly; a higher rate gives an earlier, higher peak"><g font-family="Source Sans 3, sans-serif" font-size="10" fill="#4B5866"><path d="M34 26v146h250" stroke="#294766" stroke-opacity=".35" fill="none"/><path class="pa-draw" pathLength="1" d="M34.0,167.6 L35.6,166.7 L37.1,165.5 L38.7,164.1 L40.2,162.5 L41.8,160.5 L43.4,158.1 L44.9,155.2 L46.5,151.9 L48.1,148.0 L49.6,143.4 L51.2,138.1 L52.8,132.2 L54.3,125.5 L55.9,118.1 L57.4,110.1 L59.0,101.6 L60.6,92.8 L62.1,84.0 L63.7,75.3 L65.2,67.1 L66.8,59.6 L68.4,53.0 L69.9,47.6 L71.5,43.5 L73.1,40.8 L74.6,39.3 L76.2,39.2 L77.8,40.2 L79.3,42.2 L80.9,45.1 L82.4,48.8 L84.0,53.0 L85.6,57.7 L87.1,62.6 L88.7,67.8 L90.2,73.1 L91.8,78.4 L93.4,83.7 L94.9,88.9 L96.5,93.9 L98.1,98.8 L99.6,103.5 L101.2,108.0 L102.8,112.3 L104.3,116.4 L105.9,120.2 L107.4,123.8 L109.0,127.2 L110.6,130.4 L112.1,133.5 L113.7,136.3 L115.2,138.9 L116.8,141.3 L118.4,143.6 L119.9,145.7 L121.5,147.7 L123.1,149.5 L124.6,151.2 L126.2,152.8 L127.8,154.3 L129.3,155.6 L130.9,156.9 L132.4,158.1 L134.0,159.1 L135.6,160.1 L137.1,161.0 L138.7,161.9 L140.2,162.7 L141.8,163.4 L143.4,164.1 L144.9,164.7 L146.5,165.3 L148.1,165.8 L149.6,166.3 L151.2,166.7 L152.8,167.1 L154.3,167.5 L155.9,167.9 L157.4,168.2 L159.0,168.5 L160.6,168.8 L162.1,169.0 L163.7,169.3 L165.2,169.5 L166.8,169.7 L168.4,169.9 L169.9,170.0 L171.5,170.2 L173.1,170.3 L174.6,170.5 L176.2,170.6 L177.8,170.7 L179.3,170.8 L180.9,170.9 L182.4,171.0 L184.0,171.1 L185.6,171.1 L187.1,171.2 L188.7,171.3 L190.2,171.3 L191.8,171.4 L193.4,171.4 L194.9,171.5 L196.5,171.5 L198.1,171.6 L199.6,171.6 L201.2,171.6 L202.8,171.6 L204.3,171.7 L205.9,171.7 L207.4,171.7 L209.0,171.7 L210.6,171.8 L212.1,171.8 L213.7,171.8 L215.2,171.8 L216.8,171.8 L218.4,171.8 L219.9,171.9 L221.5,171.9 L223.1,171.9 L224.6,171.9 L226.2,171.9 L227.8,171.9 L229.3,171.9 L230.9,171.9 L232.4,171.9 L234.0,171.9 L235.6,171.9 L237.1,171.9 L238.7,171.9 L240.2,172.0 L241.8,172.0 L243.4,172.0 L244.9,172.0 L246.5,172.0 L248.1,172.0 L249.6,172.0 L251.2,172.0 L252.8,172.0 L254.3,172.0 L255.9,172.0 L257.4,172.0 L259.0,172.0 L260.6,172.0 L262.1,172.0 L263.7,172.0 L265.2,172.0 L266.8,172.0 L268.4,172.0 L269.9,172.0 L271.5,172.0 L273.1,172.0 L274.6,172.0 L276.2,172.0 L277.8,172.0 L279.3,172.0 L280.9,172.0 L282.4,172.0 L284.0,172.0" fill="none" stroke="#294766" stroke-width="2" stroke-linecap="round"/><path class="pa-draw" pathLength="1" d="M34.0,167.6 L35.6,167.2 L37.1,166.7 L38.7,166.1 L40.2,165.5 L41.8,164.9 L43.4,164.2 L44.9,163.4 L46.5,162.6 L48.1,161.7 L49.6,160.7 L51.2,159.6 L52.8,158.4 L54.3,157.2 L55.9,155.8 L57.4,154.3 L59.0,152.8 L60.6,151.1 L62.1,149.4 L63.7,147.5 L65.2,145.5 L66.8,143.5 L68.4,141.3 L69.9,139.1 L71.5,136.7 L73.1,134.4 L74.6,131.9 L76.2,129.5 L77.8,127.0 L79.3,124.5 L80.9,122.1 L82.4,119.7 L84.0,117.4 L85.6,115.2 L87.1,113.2 L88.7,111.2 L90.2,109.4 L91.8,107.8 L93.4,106.4 L94.9,105.3 L96.5,104.3 L98.1,103.5 L99.6,103.0 L101.2,102.7 L102.8,102.7 L104.3,102.8 L105.9,103.2 L107.4,103.8 L109.0,104.5 L110.6,105.4 L112.1,106.5 L113.7,107.7 L115.2,109.1 L116.8,110.5 L118.4,112.1 L119.9,113.7 L121.5,115.4 L123.1,117.1 L124.6,118.9 L126.2,120.7 L127.8,122.5 L129.3,124.3 L130.9,126.2 L132.4,128.0 L134.0,129.7 L135.6,131.5 L137.1,133.2 L138.7,134.9 L140.2,136.5 L141.8,138.2 L143.4,139.7 L144.9,141.2 L146.5,142.7 L148.1,144.1 L149.6,145.4 L151.2,146.8 L152.8,148.0 L154.3,149.2 L155.9,150.4 L157.4,151.5 L159.0,152.5 L160.6,153.6 L162.1,154.5 L163.7,155.4 L165.2,156.3 L166.8,157.2 L168.4,158.0 L169.9,158.7 L171.5,159.4 L173.1,160.1 L174.6,160.8 L176.2,161.4 L177.8,162.0 L179.3,162.5 L180.9,163.1 L182.4,163.6 L184.0,164.0 L185.6,164.5 L187.1,164.9 L188.7,165.3 L190.2,165.7 L191.8,166.0 L193.4,166.4 L194.9,166.7 L196.5,167.0 L198.1,167.3 L199.6,167.5 L201.2,167.8 L202.8,168.0 L204.3,168.3 L205.9,168.5 L207.4,168.7 L209.0,168.9 L210.6,169.0 L212.1,169.2 L213.7,169.4 L215.2,169.5 L216.8,169.7 L218.4,169.8 L219.9,169.9 L221.5,170.0 L223.1,170.2 L224.6,170.3 L226.2,170.4 L227.8,170.5 L229.3,170.6 L230.9,170.6 L232.4,170.7 L234.0,170.8 L235.6,170.9 L237.1,170.9 L238.7,171.0 L240.2,171.0 L241.8,171.1 L243.4,171.2 L244.9,171.2 L246.5,171.2 L248.1,171.3 L249.6,171.3 L251.2,171.4 L252.8,171.4 L254.3,171.4 L255.9,171.5 L257.4,171.5 L259.0,171.5 L260.6,171.6 L262.1,171.6 L263.7,171.6 L265.2,171.6 L266.8,171.7 L268.4,171.7 L269.9,171.7 L271.5,171.7 L273.1,171.7 L274.6,171.7 L276.2,171.8 L277.8,171.8 L279.3,171.8 L280.9,171.8 L282.4,171.8 L284.0,171.8" fill="none" stroke="#2E7D86" stroke-width="2" stroke-linecap="round"/><path class="pa-draw" pathLength="1" d="M34.0,167.6 L35.6,167.5 L37.1,167.3 L38.7,167.1 L40.2,166.9 L41.8,166.7 L43.4,166.5 L44.9,166.3 L46.5,166.1 L48.1,165.9 L49.6,165.6 L51.2,165.4 L52.8,165.2 L54.3,164.9 L55.9,164.7 L57.4,164.4 L59.0,164.1 L60.6,163.9 L62.1,163.6 L63.7,163.3 L65.2,163.0 L66.8,162.7 L68.4,162.4 L69.9,162.1 L71.5,161.8 L73.1,161.4 L74.6,161.1 L76.2,160.8 L77.8,160.4 L79.3,160.1 L80.9,159.7 L82.4,159.4 L84.0,159.0 L85.6,158.7 L87.1,158.3 L88.7,157.9 L90.2,157.6 L91.8,157.2 L93.4,156.9 L94.9,156.5 L96.5,156.1 L98.1,155.8 L99.6,155.4 L101.2,155.0 L102.8,154.7 L104.3,154.3 L105.9,154.0 L107.4,153.7 L109.0,153.3 L110.6,153.0 L112.1,152.7 L113.7,152.4 L115.2,152.1 L116.8,151.8 L118.4,151.5 L119.9,151.3 L121.5,151.0 L123.1,150.8 L124.6,150.5 L126.2,150.3 L127.8,150.1 L129.3,149.9 L130.9,149.8 L132.4,149.6 L134.0,149.5 L135.6,149.4 L137.1,149.3 L138.7,149.2 L140.2,149.1 L141.8,149.1 L143.4,149.0 L144.9,149.0 L146.5,149.0 L148.1,149.0 L149.6,149.1 L151.2,149.1 L152.8,149.2 L154.3,149.3 L155.9,149.4 L157.4,149.5 L159.0,149.6 L160.6,149.7 L162.1,149.9 L163.7,150.1 L165.2,150.2 L166.8,150.4 L168.4,150.6 L169.9,150.9 L171.5,151.1 L173.1,151.3 L174.6,151.6 L176.2,151.8 L177.8,152.1 L179.3,152.3 L180.9,152.6 L182.4,152.9 L184.0,153.2 L185.6,153.5 L187.1,153.8 L188.7,154.1 L190.2,154.4 L191.8,154.7 L193.4,155.0 L194.9,155.3 L196.5,155.6 L198.1,156.0 L199.6,156.3 L201.2,156.6 L202.8,156.9 L204.3,157.2 L205.9,157.5 L207.4,157.8 L209.0,158.1 L210.6,158.5 L212.1,158.8 L213.7,159.1 L215.2,159.4 L216.8,159.7 L218.4,160.0 L219.9,160.2 L221.5,160.5 L223.1,160.8 L224.6,161.1 L226.2,161.4 L227.8,161.6 L229.3,161.9 L230.9,162.2 L232.4,162.4 L234.0,162.7 L235.6,162.9 L237.1,163.2 L238.7,163.4 L240.2,163.6 L241.8,163.9 L243.4,164.1 L244.9,164.3 L246.5,164.5 L248.1,164.7 L249.6,164.9 L251.2,165.1 L252.8,165.3 L254.3,165.5 L255.9,165.7 L257.4,165.9 L259.0,166.1 L260.6,166.2 L262.1,166.4 L263.7,166.6 L265.2,166.7 L266.8,166.9 L268.4,167.0 L269.9,167.2 L271.5,167.3 L273.1,167.5 L274.6,167.6 L276.2,167.7 L277.8,167.9 L279.3,168.0 L280.9,168.1 L282.4,168.2 L284.0,168.3" fill="none" stroke="#8FB3D1" stroke-width="1.6" stroke-linecap="round"/><text x="38" y="22">I(t), three values of β</text><text x="250" y="188">time</text><text x="150" y="60" text-anchor="middle" font-style="italic">dI/dt = βSI − γI</text></g></svg>'''
ANIM_SCIML = _anim_sciml()
ANIM_BIOMED = '''<svg viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Animated reliability diagram: predicted probabilities are compared with observed frequencies; points fall below the diagonal for a model that systematically overestimates risk, and recalibration returns them to it"><g font-family="Source Sans 3, sans-serif" font-size="10" fill="#4B5866"><path d="M40 26v146h220" stroke="#294766" stroke-opacity=".35" fill="none"/><path d="M40 172L260 26" stroke="#B9C3CC" stroke-width="1" stroke-dasharray="3 3"/><path class="pa-draw pa-late" pathLength="1" d="M40.0,172.0 L67.5,162.7 L95.0,152.0 L122.5,138.8 L150.0,122.4 L177.5,102.3 L205.0,79.0 L232.5,53.2 L260.0,26.0 L260.0,26.0" fill="none" stroke="#294766" stroke-width="1.6"/><path class="pa-draw pa-later" pathLength="1" d="M40 172L260 26" fill="none" stroke="#2E7D86" stroke-width="2.2"/><circle class="pa-pop" cx="67.5" cy="162.7" r="3.4" fill="#294766" style="animation-delay:0.40s"/><circle class="pa-pop" cx="95.0" cy="152.0" r="3.4" fill="#294766" style="animation-delay:0.75s"/><circle class="pa-pop" cx="122.5" cy="138.8" r="3.4" fill="#294766" style="animation-delay:1.10s"/><circle class="pa-pop" cx="150.0" cy="122.4" r="3.4" fill="#294766" style="animation-delay:1.45s"/><circle class="pa-pop" cx="177.5" cy="102.3" r="3.4" fill="#294766" style="animation-delay:1.80s"/><circle class="pa-pop" cx="205.0" cy="79.0" r="3.4" fill="#294766" style="animation-delay:2.15s"/><circle class="pa-pop" cx="232.5" cy="53.2" r="3.4" fill="#294766" style="animation-delay:2.50s"/><circle class="pa-pop" cx="260.0" cy="26.0" r="3.4" fill="#294766" style="animation-delay:2.85s"/><text x="44" y="20">observed frequency</text><text x="150" y="188" text-anchor="middle">predicted probability</text><text x="180" y="150" fill="#2E7D86">after recalibration</text></g></svg>'''
ANIM_NEURO = _anim_neuro()
