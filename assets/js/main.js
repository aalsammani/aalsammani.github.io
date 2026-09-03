/* =============================================================================
   ABDALLAH ALSAMMANI — ACADEMIC WEBSITE · shared script · v4.0
   1. Mobile navigation toggle
   2. Current-page marking (aria-current) — works with any page filename
   3. Gentle section reveal (skipped when prefers-reduced-motion)
   4. Publications filter (publications.html only)
   ============================================================================= */
(function () {
  'use strict';

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

  /* 3. Reveal --------------------------------------------------------------- */
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var items = document.querySelectorAll('.reveal');
  if (items.length) {
    if (reduce || !('IntersectionObserver' in window)) {
      items.forEach(function (el) { el.classList.add('is-visible'); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add('is-visible'); io.unobserve(en.target); }
        });
      }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });
      items.forEach(function (el) { io.observe(el); });
    }
  }

  /* 4. Publications filter -------------------------------------------------- */
  var toolbar = document.querySelector('.pub-toolbar');
  if (toolbar) {
    var buttons = toolbar.querySelectorAll('.filter-btn');
    var pubs = document.querySelectorAll('.pub');
    var years = document.querySelectorAll('.pub-year');
    var empty = document.querySelector('.pub-empty');

    function applyFilter(type) {
      var shown = 0;
      pubs.forEach(function (p) {
        var match = type === 'all' || p.getAttribute('data-type') === type;
        p.hidden = !match;
        if (match) shown++;
      });
      years.forEach(function (y) {
        var any = Array.prototype.some.call(y.querySelectorAll('.pub'), function (p) { return !p.hidden; });
        y.hidden = !any;
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
