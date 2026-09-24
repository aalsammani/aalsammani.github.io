/* =============================================================================
   explorers.js · interactive research illustrations · v6.0
   Vanilla JS + inline SVG/canvas. No dependencies. Every explorer is a
   self contained function keyed by a data-explorer attribute:
     sir     — SIR model with R0 readout and parameter uncertainty band
     ident   — structural identifiability: a+b identifiable, a and b not
     hybrid  — mechanistic (constant β) vs hybrid (time varying β) fit to synthetic data
     ieeg    — animated synthetic intracranial EEG with HFO events (canvas)
   All data shown are synthetic illustrations, never results from publications.
   ============================================================================= */
(function () {
  'use strict';
  var REDUCED = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var C = { navy: '#294766', teal: '#2E7D86', gray: '#7A8794', light: '#B9C3CC', band: 'rgba(46,125,134,0.18)' };
  var SVGNS = 'http://www.w3.org/2000/svg';

  function el(tag, attrs, parent) {
    var e = document.createElementNS(SVGNS, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(e);
    return e;
  }
  function fmt(x, d) { return Number(x).toFixed(d === undefined ? 2 : d); }

  /* Plot helper: axes on a 640x360 viewBox with margins ---------------------- */
  function Plot(svg, opts) {
    this.svg = svg; this.W = 640; this.H = 360;
    this.m = { l: 56, r: 16, t: 16, b: 44 };
    this.xmin = opts.xmin; this.xmax = opts.xmax; this.ymin = opts.ymin; this.ymax = opts.ymax;
    svg.setAttribute('viewBox', '0 0 ' + this.W + ' ' + this.H);
    while (svg.firstChild) svg.removeChild(svg.firstChild);
    this.g = el('g', {}, svg);
    var x0 = this.m.l, x1 = this.W - this.m.r, y0 = this.H - this.m.b, y1 = this.m.t;
    el('line', { x1: x0, y1: y0, x2: x1, y2: y0, stroke: C.gray, 'stroke-width': 1 }, this.g);
    el('line', { x1: x0, y1: y0, x2: x0, y2: y1, stroke: C.gray, 'stroke-width': 1 }, this.g);
    var i, t;
    for (i = 0; i <= 4; i++) {
      var yv = this.ymin + (this.ymax - this.ymin) * i / 4, yy = this.y(yv);
      el('line', { x1: x0, y1: yy, x2: x1, y2: yy, stroke: C.light, 'stroke-width': 0.6, 'stroke-dasharray': '2 3' }, this.g);
      t = el('text', { x: x0 - 8, y: yy + 4, 'text-anchor': 'end', 'font-size': 12, fill: C.gray }, this.g); t.textContent = fmt(yv, opts.ydec === undefined ? 2 : opts.ydec);
    }
    for (i = 0; i <= 4; i++) {
      var xv = this.xmin + (this.xmax - this.xmin) * i / 4, xx = this.x(xv);
      t = el('text', { x: xx, y: y0 + 18, 'text-anchor': 'middle', 'font-size': 12, fill: C.gray }, this.g); t.textContent = fmt(xv, 0);
    }
    t = el('text', { x: (x0 + x1) / 2, y: this.H - 8, 'text-anchor': 'middle', 'font-size': 13, fill: C.gray }, this.g); t.textContent = opts.xlabel || '';
    t = el('text', { x: 14, y: (y0 + y1) / 2, 'text-anchor': 'middle', 'font-size': 13, fill: C.gray, transform: 'rotate(-90 14 ' + (y0 + y1) / 2 + ')' }, this.g); t.textContent = opts.ylabel || '';
  }
  Plot.prototype.x = function (v) { return this.m.l + (v - this.xmin) / (this.xmax - this.xmin) * (this.W - this.m.l - this.m.r); };
  Plot.prototype.y = function (v) { return this.H - this.m.b - (v - this.ymin) / (this.ymax - this.ymin) * (this.H - this.m.t - this.m.b); };
  Plot.prototype.line = function (ts, ys, attrs) {
    var d = ''; for (var i = 0; i < ts.length; i++) d += (i ? 'L' : 'M') + fmt(this.x(ts[i]), 1) + ',' + fmt(this.y(ys[i]), 1);
    var a = { d: d, fill: 'none', 'stroke-width': 2, 'stroke-linejoin': 'round' }; for (var k in attrs) a[k] = attrs[k];
    return el('path', a, this.g);
  };
  Plot.prototype.band = function (ts, lo, hi) {
    var d = ''; var i;
    for (i = 0; i < ts.length; i++) d += (i ? 'L' : 'M') + fmt(this.x(ts[i]), 1) + ',' + fmt(this.y(hi[i]), 1);
    for (i = ts.length - 1; i >= 0; i--) d += 'L' + fmt(this.x(ts[i]), 1) + ',' + fmt(this.y(lo[i]), 1);
    return el('path', { d: d + 'Z', fill: C.band, stroke: 'none' }, this.g);
  };
  Plot.prototype.dots = function (ts, ys, attrs) {
    for (var i = 0; i < ts.length; i++) { var a = { cx: this.x(ts[i]), cy: this.y(ys[i]), r: 2.6, fill: C.navy }; for (var k in attrs) a[k] = attrs[k]; el('circle', a, this.g); }
  };
  Plot.prototype.legend = function (items, pos) {
    var x = pos === 'right' ? this.W - this.m.r - 236 : this.m.l + 12, y = this.m.t + 14;
    items.forEach(function (it, i) {
      var yy = y + i * 18;
      el('line', { x1: x, y1: yy - 4, x2: x + 22, y2: yy - 4, stroke: it.color, 'stroke-width': 2.2, 'stroke-dasharray': it.dash || 'none' }, this.g);
      var t = el('text', { x: x + 28, y: yy, 'font-size': 12.5, fill: '#1F2933' }, this.g); t.textContent = it.label;
    }, this);
  };

  /* RK4 integrator for SIR with β(t) ---------------------------------------- */
  function sir(betaFn, gamma, I0, T, n) {
    var h = T / n, S = 1 - I0, I = I0, R = 0, ts = [0], Ss = [S], Is = [I], Rs = [R];
    function f(t, s, i) { var b = betaFn(t); return [-b * s * i, b * s * i - gamma * i, gamma * i]; }
    for (var k = 0; k < n; k++) {
      var t = k * h, k1 = f(t, S, I), k2 = f(t + h / 2, S + h / 2 * k1[0], I + h / 2 * k1[1]),
          k3 = f(t + h / 2, S + h / 2 * k2[0], I + h / 2 * k2[1]), k4 = f(t + h, S + h * k3[0], I + h * k3[1]);
      S += h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]); I += h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]); R = 1 - S - I;
      ts.push(t + h); Ss.push(S); Is.push(I); Rs.push(R);
    }
    return { t: ts, S: Ss, I: Is, R: Rs };
  }
  function every(arr, step) { var o = []; for (var i = 0; i < arr.length; i += step) o.push(arr[i]); return o; }

  /* 1. SIR explorer ---------------------------------------------------------- */
  function initSIR(root) {
    var svg = root.querySelector('svg'), bS = root.querySelector('[data-p=beta]'), gS = root.querySelector('[data-p=gamma]'),
        uq = root.querySelector('[data-p=uq]'), out = root.querySelector('[data-out]');
    function draw() {
      var beta = +bS.value, gamma = +gS.value, T = 160, n = 400;
      var p = new Plot(svg, { xmin: 0, xmax: T, ymin: 0, ymax: 1, xlabel: 'time (days)', ylabel: 'fraction of population' });
      var base = sir(function () { return beta; }, gamma, 0.01, T, n);
      if (uq.checked) {
        var lo = [], hi = [], m = 40, runs = [];
        for (var j = 0; j < m; j++) { var b = beta * (0.8 + 0.4 * j / (m - 1)); runs.push(sir(function () { return b; }, gamma, 0.01, T, n).I); }
        for (var i = 0; i <= n; i++) { var a = Infinity, z = -Infinity; for (j = 0; j < m; j++) { a = Math.min(a, runs[j][i]); z = Math.max(z, runs[j][i]); } lo.push(a); hi.push(z); }
        p.band(every(base.t, 2), every(lo, 2), every(hi, 2));
      }
      p.line(every(base.t, 2), every(base.S, 2), { stroke: C.gray, 'stroke-width': 1.6 });
      p.line(every(base.t, 2), every(base.R, 2), { stroke: C.light, 'stroke-width': 1.6 });
      p.line(every(base.t, 2), every(base.I, 2), { stroke: C.teal, 'stroke-width': 2.4 });
      var items = [{ label: 'S(t) susceptible', color: C.gray }, { label: 'I(t) infectious', color: C.teal }, { label: 'R(t) recovered', color: C.light }];
      if (uq.checked) items.push({ label: 'I(t) envelope, β within ±20%', color: C.band });
      p.legend(items);
      var R0 = beta / gamma, peak = Math.max.apply(null, base.I);
      out.innerHTML = '<span>R<sub>0</sub> = β/γ = <strong>' + fmt(R0) + '</strong></span><span>peak I = <strong>' + fmt(peak, 3) + '</strong></span><span>' + (R0 > 1 ? 'R<sub>0</sub> &gt; 1: an outbreak grows from a small introduction' : 'R<sub>0</sub> ≤ 1: the infection dies out') + '</span>';
      root.querySelector('[data-v=beta]').textContent = fmt(beta); root.querySelector('[data-v=gamma]').textContent = fmt(gamma);
    }
    [bS, gS, uq].forEach(function (c) { c.addEventListener('input', draw); });
    draw();
  }

  /* 2. Identifiability explorer --------------------------------------------- */
  function initIdent(root) {
    var svg = root.querySelector('svg'), aS = root.querySelector('[data-p=a]'), bS = root.querySelector('[data-p=b]'),
        alt = root.querySelector('[data-p=alt]'), out = root.querySelector('[data-out]');
    function draw() {
      var a = +aS.value, b = +bS.value, s = a + b, T = 10, n = 200, ts = [], y = [], y2 = [];
      var a2 = Math.min(s - 0.05, Math.max(0.05, s - a)); // a different split with the same sum
      for (var i = 0; i <= n; i++) { var t = T * i / n; ts.push(t); y.push(Math.exp(-s * t)); y2.push(Math.exp(-((a2) + (s - a2)) * t)); }
      var p = new Plot(svg, { xmin: 0, xmax: T, ymin: 0, ymax: 1, xlabel: 'time t', ylabel: 'observed output y(t) = x(t)/x₀' });
      p.line(ts, y, { stroke: C.navy, 'stroke-width': alt.checked ? 6 : 2.4, 'stroke-opacity': alt.checked ? 0.35 : 1 });
      if (alt.checked) p.line(ts, y2, { stroke: C.teal, 'stroke-width': 2.2, 'stroke-dasharray': '7 5' });
      var items = [{ label: '(a, b) = (' + fmt(a) + ', ' + fmt(b) + ')', color: C.navy }];
      if (alt.checked) items.push({ label: '(a, b) = (' + fmt(a2) + ', ' + fmt(s - a2) + '), same sum', color: C.teal, dash: '7 5' });
      p.legend(items);
      out.innerHTML = '<span>a + b = <strong>' + fmt(s) + '</strong> is determined by the output</span><span>a and b separately are <strong>not</strong>: every pair with this sum gives the same curve</span>';
      root.querySelector('[data-v=a]').textContent = fmt(a); root.querySelector('[data-v=b]').textContent = fmt(b);
    }
    [aS, bS, alt].forEach(function (c) { c.addEventListener('input', draw); });
    draw();
  }

  /* 3. Mechanistic vs hybrid fit -------------------------------------------- */
  function initHybrid(root) {
    var svg = root.querySelector('svg'), amp = root.querySelector('[data-p=amp]'), out = root.querySelector('[data-out]');
    var T = 120, n = 240, gamma = 0.12, b0 = 0.3, per = 60;
    function lcg(seed) { var s = seed; return function () { s = (s * 1664525 + 1013904223) % 4294967296; return s / 4294967296; }; }
    function truthBeta(A) { return function (t) { return b0 * (1 + A * Math.sin(2 * Math.PI * t / per)); }; }
    function sse(pred, obs) { var e = 0; for (var i = 0; i < obs.length; i++) e += (pred[i] - obs[i]) * (pred[i] - obs[i]); return e; }
    function draw() {
      var A = +amp.value, truth = sir(truthBeta(A), gamma, 0.01, T, n), rnd = lcg(12345);
      var obsT = [], obsY = [], idx = [];
      for (var i = 0; i <= n; i += 8) { var u = rnd(), v = rnd(), z = Math.sqrt(-2 * Math.log(u + 1e-12)) * Math.cos(2 * Math.PI * v); obsT.push(truth.t[i]); obsY.push(Math.max(0, truth.I[i] + 0.008 * z)); idx.push(i); }
      // mechanistic: constant β, grid search
      var best = { e: Infinity }, b;
      for (b = 0.05; b <= 1.0; b += 0.01) { var r = sir(function () { return b; }, gamma, 0.01, T, n); var pr = idx.map(function (k) { return r.I[k]; }); var e = sse(pr, obsY); if (e < best.e) best = { e: e, b: b, r: r }; }
      // hybrid: β(t) = c0(1 + a sin(2πt/per + φ)), grid search (stands in for a learned component)
      var bestH = { e: Infinity }, c0, a, ph;
      for (c0 = 0.15; c0 <= 0.6; c0 += 0.025) for (a = 0; a <= 0.8; a += 0.1) for (ph = 0; ph < 2 * Math.PI; ph += Math.PI / 6) {
        var rr = sir((function (cc, aa, pp) { return function (t) { return cc * (1 + aa * Math.sin(2 * Math.PI * t / per + pp)); }; })(c0, a, ph), gamma, 0.01, T, n);
        var pr2 = idx.map(function (k) { return rr.I[k]; }); var e2 = sse(pr2, obsY); if (e2 < bestH.e) bestH = { e: e2, c0: c0, a: a, ph: ph, r: rr };
      }
      var ymax = Math.max(0.05, Math.max.apply(null, obsY) * 1.3);
      var p = new Plot(svg, { xmin: 0, xmax: T, ymin: 0, ymax: ymax, xlabel: 'time (days)', ylabel: 'infectious fraction I(t)', ydec: 3 });
      p.line(every(truth.t, 2), every(truth.I, 2), { stroke: C.light, 'stroke-width': 1.5 });
      p.line(every(best.r.t, 2), every(best.r.I, 2), { stroke: C.gray, 'stroke-width': 2.2, 'stroke-dasharray': '7 5' });
      p.line(every(bestH.r.t, 2), every(bestH.r.I, 2), { stroke: C.teal, 'stroke-width': 2.4 });
      p.dots(obsT, obsY);
      p.legend([{ label: 'synthetic observations', color: C.navy }, { label: 'truth: SIR with seasonal β(t)', color: C.light }, { label: 'mechanistic fit: constant β', color: C.gray, dash: '7 5' }, { label: 'hybrid fit: structure + flexible β(t)', color: C.teal }], 'right');
      var rmse = function (e) { return Math.sqrt(e / obsY.length); };
      out.innerHTML = '<span>seasonal amplitude of the true β(t): <strong>' + fmt(A, 1) + '</strong></span><span>RMSE, constant β: <strong>' + fmt(rmse(best.e), 4) + '</strong></span><span>RMSE, hybrid: <strong>' + fmt(rmse(bestH.e), 4) + '</strong></span>';
      root.querySelector('[data-v=amp]').textContent = fmt(A, 1);
    }
    amp.addEventListener('input', draw);
    draw();
  }

  /* 4. Animated synthetic iEEG (canvas) ------------------------------------- */
  function initIEEG(root) {
    var cv = root.querySelector('canvas'), btn = root.querySelector('[data-p=play]'), ctx = cv.getContext('2d');
    var W = cv.width, H = cv.height, N = 900, buf = [], hfo = [], phase = 0, playing = !REDUCED, raf = null, seed = 7;
    function rnd() { seed = (seed * 1664525 + 1013904223) % 4294967296; return seed / 4294967296; }
    var burst = 0, burstLeft = 0;
    function sample() {
      phase += 1;
      var v = 0.55 * Math.sin(phase * 0.05) + 0.25 * Math.sin(phase * 0.13 + 1) + 0.12 * (rnd() - 0.5);
      if (burstLeft > 0) { v += 0.35 * Math.sin(phase * 1.6) * (burstLeft / 40); burstLeft--; }
      else if (rnd() < 0.006) { burstLeft = 40; hfo.push(N - 1); }
      return v;
    }
    for (var i = 0; i < N; i++) buf.push(sample());
    function render() {
      ctx.clearRect(0, 0, W, H);
      ctx.fillStyle = '#F1F4F8'; ctx.fillRect(0, 0, W, H);
      ctx.strokeStyle = C.navy; ctx.lineWidth = 1.2; ctx.beginPath();
      for (var i = 0; i < N; i++) { var x = i / (N - 1) * W, y = H * 0.42 - buf[i] * H * 0.28; i ? ctx.lineTo(x, y) : ctx.moveTo(x, y); }
      ctx.stroke();
      ctx.strokeStyle = C.teal; ctx.lineWidth = 2;
      hfo.forEach(function (ix) { var x = ix / (N - 1) * W; ctx.beginPath(); ctx.moveTo(x, H * 0.78); ctx.lineTo(x, H * 0.92); ctx.stroke(); });
      ctx.fillStyle = C.gray; ctx.font = '12px Source Sans 3, sans-serif'; ctx.fillText('synthetic iEEG', 8, 16); ctx.fillText('detected HFO events', 8, H - 6);
    }
    function step() { for (var k = 0; k < 3; k++) { buf.shift(); buf.push(sample()); } for (var j = 0; j < hfo.length; j++) hfo[j] -= 3; while (hfo.length && hfo[0] < 0) hfo.shift(); render(); if (playing) raf = requestAnimationFrame(step); }
    function toggle() { playing = !playing; btn.textContent = playing ? 'Pause' : 'Play'; btn.setAttribute('aria-pressed', String(playing)); if (playing) raf = requestAnimationFrame(step); else if (raf) cancelAnimationFrame(raf); }
    btn.addEventListener('click', toggle);
    btn.textContent = playing ? 'Pause' : 'Play'; btn.setAttribute('aria-pressed', String(playing));
    render(); if (playing) raf = requestAnimationFrame(step);
    document.addEventListener('visibilitychange', function () { if (document.hidden && playing) toggle(); });
  }

  var inits = { sir: initSIR, ident: initIdent, hybrid: initHybrid, ieeg: initIEEG };
  document.querySelectorAll('[data-explorer]').forEach(function (root) { var f = inits[root.getAttribute('data-explorer')]; if (f) try { f(root); } catch (e) { console.error('explorer', e); } });
})();
