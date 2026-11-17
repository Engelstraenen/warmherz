/* WARMHERZ Demo · Interaktion & Motion */
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const SHOT = new URLSearchParams(location.search).has('shot');
  if (SHOT) document.documentElement.classList.add('shotmode');
  const reduce = SHOT || matchMedia('(prefers-reduced-motion: reduce)').matches;
  const hasGsap = typeof gsap !== 'undefined';
  const eur = n => Math.round(n).toLocaleString('de-DE');

  /* ---------- Nav ---------- */
  const nav = $('#nav');
  addEventListener('scroll', () => nav.classList.toggle('solid', scrollY > 40), { passive: true });
  const burger = $('.burger'), links = $('.links');
  burger.addEventListener('click', () => {
    const o = links.classList.toggle('open');
    burger.setAttribute('aria-expanded', o);
  });
  $$('.links a').forEach(a => a.addEventListener('click', () => links.classList.remove('open')));

  /* ---------- Countdown bis 1.2.2027 ---------- */
  const target = new Date('2027-02-01T00:00:00+01:00').getTime();
  const pad = n => String(n).padStart(2, '0');
  function tick() {
    let d = Math.max(0, target - Date.now());
    const days = Math.floor(d / 864e5); d -= days * 864e5;
    const h = Math.floor(d / 36e5); d -= h * 36e5;
    const m = Math.floor(d / 6e4); d -= m * 6e4;
    const s = Math.floor(d / 1e3);
    $$('[data-days]').forEach(e => e.textContent = days);
    const set = (k, v) => { const e = $(`[data-cd="${k}"]`); if (e && e.textContent !== v) e.textContent = v; };
    set('d', pad(days)); set('h', pad(h)); set('m', pad(m)); set('s', pad(s));
  }
  tick(); setInterval(tick, 1000);

  /* ---------- Hotspots auf object-fit:cover-Bild ---------- */
  function coverPoint(box, iw, ih, ox, oy, fx, fy) {
    const bw = box.clientWidth, bh = box.clientHeight;
    const sc = Math.max(bw / iw, bh / ih);
    const rw = iw * sc, rh = ih * sc;
    return [(bw - rw) * ox + fx * rw, (bh - rh) * oy + fy * rh];
  }
  function placeAll() {
    const media = $('.hero-media'), img = $('.hero-img');
    const iw = img.naturalWidth || 16, ih = img.naturalHeight || 9;
    const pos = getComputedStyle(img).objectPosition.split(' ').map(v => parseFloat(v) / 100);
    $$('.person, .hero .gap', media).forEach(el => {
      if (el.matches('.gap')) { el.style.transform = 'translate(-50%, calc(-100% * 0 - ' + (el.querySelector('.gap-label').offsetHeight + 10) + 'px))'; }
      const fx = parseFloat(el.style.getPropertyValue('--x')) / 100, fy = parseFloat(el.style.getPropertyValue('--y')) / 100;
      const [x, y] = coverPoint(media, iw, ih, pos[0], pos[1], fx, fy);
      el.style.left = x + 'px'; el.style.top = y + 'px';
      el.style.display = (x < 10 || x > media.clientWidth - 10) ? 'none' : '';
    });
    const pm = $('.platz-media'), pimg = $('.platz-bg'), g2 = $('.gap2');
    if (pm && g2) {
      const [x, y] = coverPoint(pm, pimg.naturalWidth || 16, pimg.naturalHeight || 9, .5, .4, .63, .37);
      g2.style.left = x + 'px'; g2.style.top = y + 'px';
      pm.style.transformOrigin = `${x}px ${y + 60}px`;
    }
  }
  $('.hero-img').addEventListener('load', placeAll);
  $('.platz-bg').addEventListener('load', placeAll);
  addEventListener('resize', placeAll); placeAll();

  /* Personen-Karten */
  const card = $('.person-card'), media = $('.hero-media');
  function showCard(p) {
    $$('.person').forEach(x => x.classList.toggle('on', x === p));
    card.querySelector('b').textContent = p.dataset.name;
    card.querySelector('small').textContent = p.dataset.role;
    card.querySelector('em').textContent = '„' + p.dataset.quote + '“';
    const mx = media.clientWidth;
    let left = p.offsetLeft + 40, top = p.offsetTop - 30;
    if (left + 280 > mx) left = p.offsetLeft - 300;
    card.style.left = Math.max(10, left) + 'px'; card.style.top = Math.max(10, top) + 'px';
    card.classList.add('show');
  }
  const hideCard = () => { card.classList.remove('show'); $$('.person').forEach(x => x.classList.remove('on')); };
  $$('.person').forEach(p => {
    p.addEventListener('mouseenter', () => showCard(p));
    p.addEventListener('focus', () => showCard(p));
    p.addEventListener('mouseleave', hideCard);
    p.addEventListener('blur', hideCard);
    p.addEventListener('click', e => { e.preventDefault(); p.classList.contains('on') ? hideCard() : showCard(p); });
  });

  /* Wärmebild folgt der Maus */
  const hero = $('.hero');
  hero.addEventListener('pointermove', e => {
    const r = hero.getBoundingClientRect();
    hero.style.setProperty('--mx', (e.clientX - r.left) + 'px');
    hero.style.setProperty('--my', (e.clientY - r.top) + 'px');
  });
  $('.heat').style.background = 'radial-gradient(420px circle at var(--mx,70%) var(--my,40%),rgba(255,140,70,.28),rgba(255,140,70,0) 70%)';

  /* ---------- Headline Buchstabe für Buchstabe ---------- */
  $$('.split').forEach(h => {
    const walk = node => {
      [...node.childNodes].forEach(n => {
        if (n.nodeType === 3) {
          const frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(word => {
            if (/^\s+$/.test(word)) { frag.append(' '); return; }
            if (!word) return;
            const w = document.createElement('span'); w.className = 'w';
            [...word].forEach(c => { const s = document.createElement('span'); s.className = 'ch'; s.textContent = c; w.append(s); });
            frag.append(w);
          });
          n.replaceWith(frag);
        } else walk(n);
      });
    };
    walk(h);
  });
  if (hasGsap && !reduce) {
    gsap.to('.split .ch', { opacity: 1, y: 0, rotate: 0, filter: 'blur(0px)', duration: 1, ease: 'power3.out', stagger: .035, delay: .25 });
    gsap.from('.hero .kicker, .hero .lead, .hero .ctas', { opacity: 0, y: 30, duration: 1, ease: 'power3.out', stagger: .12, delay: 1 });
    gsap.from('.person, .hero .gap', { scale: 0, opacity: 0, duration: .8, ease: 'back.out(2)', stagger: .08, delay: 1.6 });
  } else $$('.split .ch').forEach(c => { c.style.opacity = 1; c.style.transform = 'none'; c.style.filter = 'none'; });

  /* ---------- Reveal beim Scrollen ---------- */
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: .2 });
  $$('.reveal').forEach(el => io.observe(el));

  /* ---------- Ein Tag mit Lukas ---------- */
  const scenes = $$('.scene'), day = $('.day');
  const hh = $('[data-hh]'), mm = $('[data-mm]'), clabel = $('[data-clabel]'), prog = $('.progress span'), sun = $('.sun');
  let curMin = 6 * 60 + 58, anim;
  const toMin = t => { const [h, m] = t.split(':').map(Number); return h * 60 + m; };
  function setClock(min) {
    hh.textContent = pad(Math.floor(min / 60)); mm.textContent = pad(Math.round(min % 60));
    const p = Math.min(1, Math.max(0, (min - 6 * 60) / (13.5 * 60)));
    const a = Math.PI * (1 - p);
    sun.setAttribute('cx', 100 + 90 * Math.cos(a)); sun.setAttribute('cy', 100 - 90 * Math.sin(a));
  }
  function goTo(min) {
    cancelAnimationFrame(anim);
    const from = curMin, t0 = performance.now(), dur = reduce ? 1 : 900;
    const step = now => {
      const k = Math.min(1, (now - t0) / dur), e = 1 - Math.pow(1 - k, 3);
      curMin = from + (min - from) * e; setClock(curMin);
      if (k < 1) anim = requestAnimationFrame(step);
    };
    anim = requestAnimationFrame(step);
  }
  const sio = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return;
    const s = e.target, i = scenes.indexOf(s);
    scenes.forEach(x => x.classList.toggle('active', x === s));
    s.classList.add('seen');
    goTo(toMin(s.dataset.time));
    clabel.textContent = s.dataset.label;
    day.style.setProperty('--sky', s.dataset.sky);
    prog.style.width = ((i + 1) / scenes.length * 100) + '%';
  }), { rootMargin: '-45% 0px -45% 0px' });
  scenes.forEach(s => sio.observe(s));
  setClock(curMin);
  if (SHOT) { $$('.reveal').forEach(e => e.classList.add('in')); scenes.forEach(x => x.classList.add('seen')); }

  if (hasGsap && !reduce) {
    gsap.registerPlugin(ScrollTrigger);
    gsap.to('.hero-media', { yPercent: 14, ease: 'none', scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true } });
    gsap.to('.hero-copy', { yPercent: -30, opacity: 0, ease: 'none', scrollTrigger: { trigger: '.hero', start: '30% top', end: 'bottom top', scrub: true } });
    $$('.shot img').forEach(img => gsap.fromTo(img, { yPercent: -12 }, { yPercent: 0, ease: 'none', scrollTrigger: { trigger: img.closest('.scene'), start: 'top bottom', end: 'bottom top', scrub: true } }));
    gsap.fromTo('.platz-media', { scale: 2.4 }, { scale: 1, ease: 'none', scrollTrigger: { trigger: '.platz-hero', start: 'top 80%', end: 'bottom 60%', scrub: true } });
    gsap.from('.svc', { y: 60, opacity: 0, duration: 1, stagger: .08, ease: 'power3.out', scrollTrigger: { trigger: '.svc-grid', start: 'top 80%' } });
    gsap.from('.why article', { y: 50, opacity: 0, duration: .9, stagger: .1, ease: 'power3.out', scrollTrigger: { trigger: '.why', start: 'top 85%' } });
    gsap.from('.job', { x: -40, opacity: 0, duration: .8, stagger: .08, ease: 'power3.out', scrollTrigger: { trigger: '.jobs', start: 'top 85%' } });
    gsap.from('.house', { y: 80, rotate: 2, opacity: 0, duration: 1.2, ease: 'power3.out', scrollTrigger: { trigger: '.house', start: 'top 85%' } });
  }

  /* ---------- Tilt-Karten ---------- */
  if (!reduce && matchMedia('(hover:hover)').matches) {
    $$('[data-tilt]').forEach(c => {
      c.addEventListener('pointermove', e => {
        const r = c.getBoundingClientRect(), x = (e.clientX - r.left) / r.width, y = (e.clientY - r.top) / r.height;
        c.style.transform = `rotateY(${(x - .5) * 10}deg) rotateX(${(.5 - y) * 10}deg) translateY(-4px)`;
        c.style.setProperty('--gx', x * 100 + '%'); c.style.setProperty('--gy', y * 100 + '%');
      });
      c.addEventListener('pointerleave', () => c.style.transform = '');
    });
  }

  /* ---------- Wärmepumpe interaktiv ---------- */
  const HS = [
    ['Außengerät', 'Holt Wärme aus der Luft, sogar bei −15 °C. Steht leise im Garten, etwa so laut wie ein Kühlschrank in ein paar Metern Abstand.'],
    ['Inneneinheit & Speicher', 'Im Keller, wo früher der Öltank stand. Braucht etwa so viel Platz wie ein Kühlschrank. Den Rest des Raums bekommen Sie zurück.'],
    ['Fußbodenheizung', 'Ideal für die Wärmepumpe, weil sie mit 30 bis 35 °C auskommt. Fräsen wir auch nachträglich in den alten Estrich.'],
    ['Heizkörper', 'Oft reichen die alten. Manchmal tauschen wir zwei, drei gegen größere. Das rechnen wir raumweise aus, nicht nach Gefühl.'],
    ['Bad & Warmwasser', 'Warmes Wasser kommt aus dem Speicher. Auf Wunsch bauen wir das Bad gleich mit um, ein Team, ein Termin.'],
    ['Dach & Dämmung', 'Nicht jedes Haus muss erst gedämmt werden. Wir sagen ehrlich, was sich lohnt und was nicht.']
  ];
  const infoT = $('[data-info-t]'), infoP = $('[data-info-p]');
  $$('.hs').forEach(g => {
    const act = () => {
      $$('.hs').forEach(x => x.classList.toggle('on', x === g));
      const [t, p] = HS[+g.dataset.hs];
      infoT.textContent = t; infoP.textContent = p;
      if (hasGsap && !reduce) gsap.fromTo('.hp-info', { x: 14, opacity: .3 }, { x: 0, opacity: 1, duration: .5, ease: 'power3.out' });
    };
    g.addEventListener('mouseenter', act); g.addEventListener('click', act);
    g.setAttribute('tabindex', '0'); g.setAttribute('role', 'button'); g.setAttribute('aria-label', HS[+g.dataset.hs][0]);
    g.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); act(); } });
  });
  const temp = $('[data-temp]'), snow = $('[data-snow]'), house = $('.house');
  for (let i = 0; i < 46; i++) {
    const c = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    c.setAttribute('r', (Math.random() * 2 + 1).toFixed(1));
    c.setAttribute('cx', (Math.random() * 640).toFixed(0)); c.setAttribute('cy', (Math.random() * 420).toFixed(0));
    c.dataset.v = (Math.random() * .6 + .4).toFixed(2); snow.append(c);
  }
  let snowAmt = 0;
  (function fall() {
    $$('circle', snow).forEach((c, i) => {
      if (i >= snowAmt) { c.style.display = 'none'; return; }
      c.style.display = '';
      let y = +c.getAttribute('cy') + +c.dataset.v * 1.2; if (y > 425) y = -5;
      c.setAttribute('cy', y.toFixed(1));
      c.setAttribute('cx', (+c.getAttribute('cx') + Math.sin(y / 20) * .3).toFixed(1));
    });
    if (!reduce) requestAnimationFrame(fall);
  })();
  const lerp = (a, b, t) => a + (b - a) * t;
  const mix = (c1, c2, t) => '#' + [0, 2, 4].map(i => Math.round(lerp(parseInt(c1.substr(i + 1, 2), 16), parseInt(c2.substr(i + 1, 2), 16), t)).toString(16).padStart(2, '0')).join('');
  function updateHP() {
    const T = +temp.value, t = (T + 15) / 30;
    const cop = Math.min(4.6, Math.max(2.3, 3.3 + .07 * T));
    const copS = cop.toFixed(1).replace('.', ',');
    $('[data-cop-big]').textContent = copS;
    $('[data-tout]').textContent = (T > 0 ? '+' : T < 0 ? '−' : '') + Math.abs(T) + ' °C';
    $('[data-tout]').style.color = T < 0 ? '#9CC9D8' : T < 8 ? '#F2C48D' : '#FFB98A';
    const um = $('[data-umwelt]'); um.style.flex = (cop - 1).toFixed(2); um.textContent = 'Umwelt ' + (cop - 1).toFixed(1).replace('.', ',');
    $('[data-sky1]').setAttribute('stop-color', mix('#1E2A45', '#7FA9C9', t));
    $('[data-sky2]').setAttribute('stop-color', mix('#5E6E86', '#F2C48D', t));
    $('[data-ground]').setAttribute('fill', T <= 0 ? '#E8EEF2' : '#5B4636');
    snowAmt = T <= 0 ? Math.round((-T + 1) / 16 * 46) : 0;
    house.style.setProperty('--fan', (.35 + t * 1.1).toFixed(2) + 's');
    house.style.setProperty('--fs', (.9 + t * 1.2).toFixed(2) + 's');
    $('.warmglow').style.opacity = (1 - t * .5).toFixed(2);
  }
  temp.addEventListener('input', updateHP); updateHP();

  /* ---------- Förderrechner ---------- */
  const R = { grund: 30, klimaNow: 16, klimaLater: 12, einkommen: 30, effizienz: 5, max: 70, capNow: 28000, capLater: 27250 };
  const costIn = $('[data-cost]'), bars = $('[data-bars]');
  let shown = 0;
  function calc() {
    const owner = $('input[name=owner]:checked').value === '1';
    const fuel = $('input[name=fuel]:checked').value;
    const cost = +costIn.value, inc = $('[data-income]').checked, nat = $('[data-natural]').checked;
    $('[data-cost-out]').textContent = eur(cost) + ' €';
    const parts = (klima) => [
      ['Grundförderung', R.grund, true],
      ['Klimageschwindigkeitsbonus', klima, owner && ['oel', 'gas', 'kohle', 'nacht'].includes(fuel)],
      ['Einkommensbonus', R.einkommen, owner && inc],
      ['Effizienzbonus', R.effizienz, nat]
    ];
    const rate = ps => Math.min(R.max, ps.reduce((s, p) => s + (p[2] ? p[1] : 0), 0));
    const pNow = parts(R.klimaNow), pLater = parts(R.klimaLater);
    const now = Math.min(cost, R.capNow) * rate(pNow) / 100;
    const later = Math.min(cost, R.capLater) * rate(pLater) / 100;
    bars.innerHTML = pNow.map(p => `<div class="bar ${p[2] ? '' : 'off'}"><span>${p[0]}</span><span>${p[2] ? p[1] + ' %' : '–'}</span><i><b style="width:${p[2] ? p[1] / R.max * 100 : 0}%"></b></i></div>`).join('') +
      `<div class="bar"><span><b style="color:#fff">Zusammen</b></span><span><b style="color:#FFB98A">${rate(pNow)} %</b> von ${eur(Math.min(cost, R.capNow))} €</span></div>`;
    $('[data-grant-later]').textContent = eur(later);
    $('[data-loss]').textContent = eur(Math.max(0, now - later));
    const from = shown, t0 = performance.now(), el = $('[data-grant-now]');
    if (reduce) { el.textContent = eur(now); shown = now; return; }
    (function run(n) { const k = Math.min(1, (n - t0) / 600), e = 1 - Math.pow(1 - k, 3); el.textContent = eur(from + (now - from) * e); if (k < 1) requestAnimationFrame(run); else shown = now; })(t0);
  }
  $$('.calc input').forEach(i => i.addEventListener('input', calc)); calc();

  /* ---------- Vorher / Nachher ---------- */
  const ba = $('[data-ba]');
  const baImg = $('img', ba), hideBa = () => { $('#vorher-nachher').style.display = 'none'; };
  if (baImg.complete && !baImg.naturalWidth) hideBa(); else baImg.addEventListener('error', hideBa);
  $('[data-ba-range]').addEventListener('input', e => ba.style.setProperty('--p', e.target.value + '%'));
  if (hasGsap && !reduce) ScrollTrigger.create({ trigger: ba, start: 'top 70%', once: true, onEnter: () => gsap.fromTo(ba, { '--p': '85%' }, { '--p': '50%', duration: 1.6, ease: 'power3.inOut' }) });

  /* ---------- Vorab-Check ---------- */
  $$('[data-slot]').forEach(inp => inp.addEventListener('change', () => {
    const f = inp.files[0]; if (!f) return;
    const slot = inp.closest('.slot');
    slot.style.backgroundImage = `url(${URL.createObjectURL(f)})`; slot.classList.add('filled');
    slot.querySelector('i').textContent = '✓';
  }));
  $('[data-check-send]').addEventListener('click', () => $('[data-check-done]').classList.add('show'));

  /* ---------- 60-Sekunden-Bewerbung ---------- */
  const log = $('[data-chat-log]'), quick = $('[data-chat-quick]'), form = $('[data-chat-form]'), txt = $('[data-chat-text]');
  const A = {};
  const flow = [
    { q: 'Hi! Schön, dass du da bist. Wie heißt du?', key: 'name', free: true },
    { q: n => `Freut mich, ${A.name}! Was machst du gerade?`, key: 'jetzt', opts: ['Schule', 'Ausbildung woanders', 'Gesell/in', 'Was ganz anderes'] },
    { q: 'Was reizt dich bei uns am meisten?', key: 'job', opts: ['Monteur/in', 'Ausbildung', 'Quereinstieg', 'Kundendienst'] },
    { q: 'Letzte Frage: Wann darf Heinz dich anrufen?', key: 'zeit', opts: ['Vormittags', 'Mittags', 'Ab 17 Uhr'] }
  ];
  let stepI = 0;
  const add = (t, who) => { const m = document.createElement('div'); m.className = 'msg ' + who; m.textContent = t; log.append(m); log.scrollTop = log.scrollHeight; return m; };
  function ask() {
    quick.innerHTML = '';
    const typing = document.createElement('div'); typing.className = 'msg bot typing'; typing.innerHTML = '<i></i><i></i><i></i>'; log.append(typing); log.scrollTop = log.scrollHeight;
    setTimeout(() => {
      typing.remove();
      if (stepI >= flow.length) {
        add(`Danke, ${A.name}! Heinz ruft dich ${A.zeit.toLowerCase()} an. Bis gleich!`, 'bot');
        add('Demo: Hier wird nichts gesendet.', 'bot');
        const b = document.createElement('button'); b.textContent = 'Nochmal von vorn'; b.onclick = () => { log.innerHTML = ''; stepI = 0; ask(); }; quick.append(b);
        return;
      }
      const s = flow[stepI];
      add(typeof s.q === 'function' ? s.q() : s.q, 'bot');
      (s.opts || []).forEach(o => { const b = document.createElement('button'); b.type = 'button'; b.textContent = o; b.onclick = () => answer(o); quick.append(b); });
      if (s.free && matchMedia('(hover:hover)').matches) txt.focus({ preventScroll: true });
    }, reduce ? 50 : 750);
  }
  function answer(v) {
    v = v.trim(); if (!v || stepI >= flow.length) return;
    A[flow[stepI].key] = v; add(v, 'me'); stepI++; ask();
  }
  form.addEventListener('submit', e => { e.preventDefault(); answer(txt.value); txt.value = ''; });
  if (SHOT && new URLSearchParams(location.search).has('chat')) ['Jonas', 'Gesell/in', 'Monteur/in'].forEach((a, i) => setTimeout(() => answer(a), 400 + i * 400));
  const cio = new IntersectionObserver(es => { if (es[0].isIntersecting) { ask(); cio.disconnect(); } }, { threshold: .4 });
  cio.observe($('[data-chat]'));
})();

/* Vorschau-Hilfe: ?shot=<id>&y=<offset> springt direkt zu einem Abschnitt (für First Frames) */
(() => {
  const q = new URLSearchParams(location.search), id = q.get('shot');
  if (!id) return;
  document.documentElement.style.scrollBehavior = 'auto';
  if (id !== 'top') {
    document.querySelectorAll('body > section, body > footer, .demo-bar').forEach(s => { if (s.id !== id) s.style.display = 'none'; });
    const sc0 = q.get('scene');
    if (q.get('hide')) document.querySelectorAll(q.get('hide')).forEach(e => e.style.display = 'none');
    if (sc0 !== null) { document.querySelector('.day-intro').style.display = 'none'; document.querySelectorAll('.scene').forEach((s, i) => { if (i !== +sc0) s.style.display = 'none'; }); document.querySelector('.day-stage').style.paddingTop = '60px'; }
  }
  const go = () => {
    const el = document.getElementById(id); if (el && q.get('y')) scrollTo(0, el.getBoundingClientRect().top + scrollY - 70 + (+q.get('y') || 0));
    const sc = q.get('scene');
    if (sc !== null) {
      const all = [...document.querySelectorAll('.scene')], s = all[+sc];
      all.forEach(x => x.classList.toggle('active', x === s));
      const [h, m] = s.dataset.time.split(':');
      document.querySelector('[data-hh]').textContent = h; document.querySelector('[data-mm]').textContent = m;
      document.querySelector('[data-clabel]').textContent = s.dataset.label;
      document.querySelector('.day').style.setProperty('--sky', s.dataset.sky);
      document.querySelector('.progress span').style.width = ((+sc + 1) / all.length * 100) + '%';
      const p = Math.min(1, Math.max(0, (h * 60 + +m - 360) / 810)), a = Math.PI * (1 - p), sun = document.querySelector('.sun');
      sun.setAttribute('cx', 100 + 90 * Math.cos(a)); sun.setAttribute('cy', 100 - 90 * Math.sin(a));
    }
    const sel = q.get('hover');
    if (sel) { const e = document.querySelector(sel); if (e) e.dispatchEvent(new Event(e.matches('.person') ? 'mouseenter' : 'click')); }
  };
  addEventListener('load', () => { go(); setTimeout(go, 300); });
})();
