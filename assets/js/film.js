/* Notdienst-Film im Kopfbereich (Wartung).
   Ton: Der Film versucht MIT Sprecher zu starten. Blockiert der Browser das (Standard ohne Klick),
   läuft er stumm weiter und der Ton geht beim ersten Klick/Tippen/Tastendruck auf der Seite an –
   der Film beginnt dann von vorne mit Sprecher. Knopf schaltet Ton an/aus. */
(() => {
  const film = document.querySelector('[data-film]');
  if (!film) return;
  const v = film.querySelector('video');
  const items = [...film.querySelectorAll('[data-at]')];
  const bar = film.querySelector('[data-film-bar]');
  const clock = film.querySelector('[data-clock]');
  const btn = film.querySelector('[data-sound]');
  const btnT = film.querySelector('[data-sound-t]');
  v.src = (innerWidth < 800 ? v.dataset.srcM : v.dataset.src) || v.dataset.src;
  const still = matchMedia('(prefers-reduced-motion: reduce)').matches || /[?&]shot=/.test(location.search);

  const render = () => {
    const t = v.currentTime || 0, d = v.duration || 10;
    items.forEach(el => {
      const a = +el.dataset.at, o = el.dataset.out ? +el.dataset.out : d + 1;
      el.classList.toggle('on', t >= a && t < o);
    });
    if (bar) bar.style.transform = `scaleX(${Math.min(1, t / d)})`;
    if (clock) { const m = 14 + Math.floor(t / 10 * 3); clock.textContent = '02:' + String(m).padStart(2, '0'); }
  };

  if (still) { items.forEach(el => el.classList.add('on')); film.classList.add('still'); return; }

  let raf;
  const loop = () => { render(); raf = requestAnimationFrame(loop); };
  v.addEventListener('play', () => { cancelAnimationFrame(raf); loop(); });
  v.addEventListener('pause', () => cancelAnimationFrame(raf));
  v.addEventListener('seeked', render);

  const showState = () => {
    if (!btn) return;
    btn.setAttribute('aria-pressed', String(!v.muted));
    btnT.textContent = v.muted ? 'Film mit Ton ansehen' : 'Ton aus';
  };
  const soundOn = (restart) => {
    v.muted = false;
    if (restart) v.currentTime = 0;
    v.play().catch(() => { v.muted = true; v.play().catch(() => {}); showState(); });
    showState();
  };

  // 1) Versuch: direkt mit Ton starten. 2) Sonst stumm + Ton beim ersten Klick/Tippen.
  let armed = false;
  const firstGesture = (e) => {
    if (e.target.closest && e.target.closest('[data-sound]')) return; // Knopf regelt selbst
    off(); if (v.muted) soundOn(true);
  };
  const off = () => ['pointerdown', 'keydown', 'touchstart'].forEach(t => removeEventListener(t, firstGesture, true));
  const arm = () => { if (armed) return; armed = true; ['pointerdown', 'keydown', 'touchstart'].forEach(t => addEventListener(t, firstGesture, { capture: true, passive: true })); };

  const start = () => {
    v.muted = false;
    v.play().then(showState).catch(() => { v.muted = true; v.play().catch(() => {}); showState(); arm(); });
  };

  let started = false;
  new IntersectionObserver(es => {
    if (es[0].isIntersecting) { if (!started) { started = true; start(); } else v.play().catch(() => {}); }
    else v.pause();
  }, { threshold: .4 }).observe(film);

  btn && btn.addEventListener('click', () => {
    off();
    if (v.muted) soundOn(true); else { v.muted = true; showState(); }
  });
})();
