/* =============================================================================
   ABDALLAH ALSAMMANI — ACADEMIC WEBSITE · shared script · v5.0
   1. Mobile navigation toggle
   2. Current-page marking (aria-current) — works with any page filename
   3. Publications filter by research area (publications.html only)
   ============================================================================= */
(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* 1. Mobile navigation ---------------------------------------------------- */
  var toggle = document.querySelector('.nav-toggle');
  var mobileNav = document.getElementById('mobile-nav');
  if (toggle && mobileNav) {
    toggle.addEventListener('click', function () {
      var open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!open));
      mobileNav.hidden = open;
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        toggle.setAttribute('aria-expanded', 'false');
        mobileNav.hidden = true;
        toggle.focus();
      }
    });
  }

  /* 2. Current page --------------------------------------------------------- */
  var path = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav a, .mobile-nav a').forEach(function (a) {
    var href = a.getAttribute('href');
    if (href === path || (path === '' && href === 'index.html')) {
      a.setAttribute('aria-current', 'page');
    }
  });

  /* 2b. Research pillars: expand/collapse, and diagram nodes that open them ---- */
  document.querySelectorAll('.pillar__toggle').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') === 'true', panel = document.getElementById(btn.getAttribute('aria-controls'));
      btn.setAttribute('aria-expanded', String(!open)); panel.hidden = open; btn.textContent = open ? 'Explore' : 'Close';
      btn.closest('.pillar').classList.toggle('is-active', !open);
    });
  });
  document.querySelectorAll('.rdiag__node').forEach(function (node) {
    node.addEventListener('click', function (e) {
      var target = document.querySelector(node.getAttribute('href'));
      if (!target) return;
      e.preventDefault();
      document.querySelectorAll('.rdiag__node').forEach(function (n) { n.classList.remove('is-active'); });
      node.classList.add('is-active');
      var btn = target.querySelector('.pillar__toggle');
      if (btn && btn.getAttribute('aria-expanded') !== 'true') btn.click();
      target.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
      target.querySelector('h3').setAttribute('tabindex', '-1'); target.querySelector('h3').focus({ preventScroll: true });
    });
  });

  /* 3. Publications filter (by research area) ------------------------------- */
  var toolbar = document.querySelector('.pub-filters');
  if (toolbar) {
    var buttons = toolbar.querySelectorAll('.filter-btn');
    var pubs = document.querySelectorAll('.pub-list .pub');
    var groups = document.querySelectorAll('.pub-list .pub-group');
    var years = document.querySelectorAll('.pub-list .pub-year');
    var empty = document.querySelector('.pub-empty');
    function applyFilter(area) {
      var shown = 0;
      pubs.forEach(function (p) {
        var areas = (p.getAttribute('data-areas') || '').split(' ');
        var match = area === 'all' || areas.indexOf(area) !== -1;
        p.hidden = !match; if (match) shown++;
      });
      groups.forEach(function (g) {
        var any = false, el = g.nextElementSibling;
        while (el && el.classList.contains('pub')) { if (!el.hidden) { any = true; break; } el = el.nextElementSibling; }
        g.hidden = !any;
      });
      years.forEach(function (y) {
        y.hidden = !Array.prototype.some.call(y.querySelectorAll('.pub'), function (p) { return !p.hidden; });
      });
      if (empty) empty.hidden = shown > 0;
    }
    buttons.forEach(function (b) {
      b.addEventListener('click', function () {
        buttons.forEach(function (x) { x.setAttribute('aria-pressed', 'false'); });
        b.setAttribute('aria-pressed', 'true');
        applyFilter(b.getAttribute('data-filter'));
      });
    });
  }
})();
