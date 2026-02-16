/* =============================================================================
   ALSAMMANI FACULTY WEBSITE — SHARED JAVASCRIPT
   =============================================================================
   
   Contents:
   1. Active navigation highlighting (sidebar + topbar)
   2. Scroll reveal animations
   3. Mobile hamburger menu
   4. Neural network canvas animation (homepage only)
   
   ============================================================================= */


/* =============================================================================
   1. ACTIVE NAVIGATION — Highlights current page in sidebar & topbar
   ============================================================================= */

(function initActiveNav() {
  // Get current page filename
  const path = window.location.pathname;
  const page = path.substring(path.lastIndexOf('/') + 1) || 'index.html';

  // Map filenames to nav IDs
  const pageMap = {
    'index.html':    'home',
    '':              'home',
    'research.html': 'research',
    'teaching.html': 'teaching',
    'team.html':     'team',
  };

  const currentId = pageMap[page] || 'home';

  // Highlight matching links in sidebar and topbar
  document.querySelectorAll('.sidebar-nav a, .topbar-nav a').forEach(link => {
    link.classList.remove('active');
    const href = link.getAttribute('href');

    // Match by page filename or by hash
    if (
      (currentId === 'home'     && (href === 'index.html' || href === '#home')) ||
      (currentId === 'research' && href === 'research.html') ||
      (currentId === 'teaching' && href === 'teaching.html') ||
      (currentId === 'team'     && href === 'team.html') ||
      (currentId === 'home'     && href === '#contact')
    ) {
      // Only mark the page link active, not #contact
      if (href !== '#contact') {
        link.classList.add('active');
      }
    }
  });

  // Special handling: if on index.html, handle scroll-based contact activation
  if (currentId === 'home') {
    const contactSection = document.getElementById('contact');
    if (contactSection) {
      window.addEventListener('scroll', function() {
        const rect = contactSection.getBoundingClientRect();
        const inView = rect.top < window.innerHeight * 0.5;

        document.querySelectorAll('.sidebar-nav a, .topbar-nav a').forEach(link => {
          if (link.getAttribute('href') === '#contact') {
            link.classList.toggle('active', inView);
          }
          // Remove active from Home when scrolled to contact
          if (link.getAttribute('href') === 'index.html' || link.getAttribute('href') === '#home') {
            link.classList.toggle('active', !inView);
          }
        });
      });
    }
  }
})();


/* =============================================================================
   2. SCROLL REVEAL — Fade-up elements as they enter viewport
   =============================================================================
   Add class="reveal" to any element you want to animate in.
   Add class="reveal reveal-delay-1" for staggered timing.
   ============================================================================= */

(function initScrollReveal() {
  const reveals = document.querySelectorAll('.reveal');
  if (!reveals.length) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
        }
      });
    },
    {
      threshold: 0.06,
      rootMargin: '0px 0px -30px 0px'
    }
  );

  reveals.forEach(el => observer.observe(el));
})();


/* =============================================================================
   3. MOBILE HAMBURGER MENU — Toggle navigation
   ============================================================================= */

function toggleMobileNav() {
  const nav = document.getElementById('mobileNav');
  if (nav) nav.classList.toggle('open');
}

function closeMobileNav() {
  const nav = document.getElementById('mobileNav');
  if (nav) nav.classList.remove('open');
}


/* =============================================================================
   4. NEURAL NETWORK CANVAS ANIMATION — Homepage hero visualization
   =============================================================================
   Creates an animated AI/ML-themed visualization with:
   - Neural network layers with interconnected nodes
   - Flowing data particles along connections
   - Pulsing activation effects
   - Mathematical symbols floating in background
   
   Only runs if #nnCanvas exists on the page.
   ============================================================================= */

(function initNeuralNetwork() {
  const canvas = document.getElementById('nnCanvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  const W = 380, H = 380;
  const dpr = window.devicePixelRatio || 1;

  canvas.width = W * dpr;
  canvas.height = H * dpr;
  canvas.style.width = W + 'px';
  canvas.style.height = H + 'px';
  ctx.scale(dpr, dpr);

  const cx = W / 2;
  const cy = H / 2;
  let time = 0;

  // --- Neural Network Layers ---
  // Define layers: x position, array of y positions
  const layers = [
    { x: cx - 115, nodes: [-65, -22, 22, 65] },      // Input layer (4 nodes)
    { x: cx - 38,  nodes: [-52, -17, 17, 52] },       // Hidden layer 1
    { x: cx + 38,  nodes: [-40, 0, 40] },             // Hidden layer 2
    { x: cx + 115, nodes: [-22, 22] },                // Output layer
  ];

  // --- Floating Particles ---
  // Particles travel along connections to represent data flow
  const particles = [];
  const maxParticles = 18;

  function createParticle() {
    // Pick random connection between adjacent layers
    const li = Math.floor(Math.random() * (layers.length - 1));
    const fromLayer = layers[li];
    const toLayer = layers[li + 1];
    const fromIdx = Math.floor(Math.random() * fromLayer.nodes.length);
    const toIdx = Math.floor(Math.random() * toLayer.nodes.length);

    return {
      fromX: fromLayer.x,
      fromY: cy + fromLayer.nodes[fromIdx],
      toX: toLayer.x,
      toY: cy + toLayer.nodes[toIdx],
      progress: 0,
      speed: 0.004 + Math.random() * 0.006,
      size: 1.5 + Math.random() * 1.5,
      opacity: 0.4 + Math.random() * 0.4,
    };
  }

  // Initialize particles
  for (let i = 0; i < maxParticles; i++) {
    const p = createParticle();
    p.progress = Math.random(); // Start at random positions
    particles.push(p);
  }

  // --- Background Math Symbols ---
  const symbols = ['∑', '∇', 'σ', 'θ', 'λ', '∂', 'π', 'μ', '∫', 'Δ'];
  const floatingSymbols = symbols.map((s, i) => ({
    char: s,
    x: 30 + Math.random() * (W - 60),
    y: 30 + Math.random() * (H - 60),
    size: 10 + Math.random() * 6,
    opacity: 0.04 + Math.random() * 0.04,
    drift: 0.15 + Math.random() * 0.3,
    phase: Math.random() * Math.PI * 2,
  }));

  // --- Draw Function ---
  function draw() {
    ctx.clearRect(0, 0, W, H);
    time += 0.008;

    // --- Draw floating math symbols ---
    floatingSymbols.forEach(s => {
      const y = s.y + Math.sin(time * s.drift + s.phase) * 8;
      ctx.font = `${s.size}px 'Playfair Display', serif`;
      ctx.fillStyle = `rgba(41, 128, 176, ${s.opacity})`;
      ctx.textAlign = 'center';
      ctx.fillText(s.char, s.x, y);
    });

    // --- Draw connections (edges) between layers ---
    for (let li = 0; li < layers.length - 1; li++) {
      const from = layers[li];
      const to = layers[li + 1];

      from.nodes.forEach(fy => {
        to.nodes.forEach(ty => {
          ctx.beginPath();
          ctx.moveTo(from.x, cy + fy);
          // Bezier curve for smooth connections
          const midX = (from.x + to.x) / 2;
          ctx.bezierCurveTo(
            midX, cy + fy,
            midX, cy + ty,
            to.x, cy + ty
          );
          ctx.strokeStyle = `rgba(41, 128, 176, 0.07)`;
          ctx.lineWidth = 0.8;
          ctx.stroke();
        });
      });
    }

    // --- Draw data flow particles ---
    particles.forEach(p => {
      p.progress += p.speed;
      if (p.progress >= 1) {
        // Reset particle on a new random connection
        Object.assign(p, createParticle());
      }

      const t = p.progress;
      const midX = (p.fromX + p.toX) / 2;

      // Bezier interpolation
      const mt = 1 - t;
      const px = mt * mt * p.fromX + 2 * mt * t * midX + t * t * p.toX;
      const py = mt * mt * p.fromY + 2 * mt * t * ((p.fromY + p.toY) / 2) + t * t * p.toY;

      // Glow
      ctx.beginPath();
      ctx.arc(px, py, p.size + 3, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(41, 128, 176, ${p.opacity * 0.15})`;
      ctx.fill();

      // Core
      ctx.beginPath();
      ctx.arc(px, py, p.size, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(95, 184, 222, ${p.opacity})`;
      ctx.fill();
    });

    // --- Draw neural network nodes ---
    layers.forEach((layer, li) => {
      layer.nodes.forEach((ny, ni) => {
        const nx = layer.x;
        const nodeY = cy + ny;

        // Pulsing activation
        const pulse = Math.sin(time * 1.8 + li * 1.2 + ni * 0.8) * 0.15 + 0.85;
        const radius = (4.5 + li * 0.5) * pulse;

        // Outer glow
        ctx.beginPath();
        ctx.arc(nx, nodeY, radius + 8, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(41, 128, 176, ${0.04 * pulse})`;
        ctx.fill();

        // Node ring
        ctx.beginPath();
        ctx.arc(nx, nodeY, radius + 1.5, 0, Math.PI * 2);
        ctx.strokeStyle = `rgba(41, 128, 176, ${0.12 * pulse})`;
        ctx.lineWidth = 1;
        ctx.stroke();

        // Node body
        ctx.beginPath();
        ctx.arc(nx, nodeY, radius, 0, Math.PI * 2);
        const grad = ctx.createRadialGradient(
          nx - radius * 0.3, nodeY - radius * 0.3, 0,
          nx, nodeY, radius
        );
        grad.addColorStop(0, `rgba(95, 184, 222, ${0.6 * pulse})`);
        grad.addColorStop(1, `rgba(41, 128, 176, ${0.45 * pulse})`);
        ctx.fillStyle = grad;
        ctx.fill();

        // Inner highlight
        ctx.beginPath();
        ctx.arc(nx - radius * 0.2, nodeY - radius * 0.2, radius * 0.35, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(255, 255, 255, ${0.3 * pulse})`;
        ctx.fill();
      });
    });

    // --- Layer labels ---
    ctx.font = '8px "IBM Plex Mono", monospace';
    ctx.textAlign = 'center';
    ctx.fillStyle = 'rgba(41, 128, 176, 0.2)';
    const labels = ['Input', 'Hidden₁', 'Hidden₂', 'Output'];
    layers.forEach((layer, i) => {
      ctx.fillText(labels[i], layer.x, cy + 95);
    });

    requestAnimationFrame(draw);
  }

  draw();
})();
