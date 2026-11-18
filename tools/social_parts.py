"""Erzeugt Bewertungen (Google/Trustpilot, Demo), Bewertungs-Chips, Instagram-Feed und Social-Icons.
Läuft in pages_content.py-Kette: python3 tools/social_parts.py"""
import os
T = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src', 'parts')
def part(n, b): open(os.path.join(T, n + '.html'), 'w').write(b)

STAR = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.8l2.8 5.9 6.4.8-4.7 4.4 1.2 6.4L12 17.2 6.3 20.3l1.2-6.4L2.8 9.5l6.4-.8z"/></svg>'
stars = lambda n=5: '<span class="stars" aria-label="%d von 5 Sternen">%s</span>' % (n, STAR * n)
G = '<span class="src-mark g" aria-hidden="true">G</span>'
TP = '<span class="src-mark tp" aria-hidden="true">' + STAR + '</span>'

R = [
 ('Katrin M.', 'Bielefeld-Schildesche', 'g', 'vor 2 Wochen', 'Samstagabend Heizung aus, Murat war in 50 Minuten da. Das Ersatzteil hatte er schon dabei, weil wir vorher ein Foto vom Display geschickt hatten.'),
 ('Thomas R.', 'Gütersloh', 'tp', 'vor 1 Monat', 'Ölkessel raus, Wärmepumpe rein, in vier Tagen. Den Förderantrag hat WARMHERZ komplett für uns gemacht.'),
 ('Sabine K.', 'Herford', 'g', 'vor 3 Wochen', 'Lukas hat uns jeden Abend kurz geschrieben, was gemacht wurde. So stelle ich mir Handwerk vor.'),
 ('Jens W.', 'Bielefeld-Mitte', 'g', 'vor 2 Monaten', 'Fußbodenheizung im Altbau gefräst, an einem Tag und fast ohne Staub. Unglaublich sauber gearbeitet.'),
 ('Familie Özdemir', 'Bad Salzuflen', 'tp', 'vor 5 Tagen', 'Festpreis im Angebot, Festpreis auf der Rechnung. Keine Überraschungen.'),
 ('Petra L.', 'Enger', 'tp', 'vor 6 Wochen', 'Bad in neun Werktagen statt der befürchteten sechs Wochen. Ein Ansprechpartner für alles.'),
 ('Markus D.', 'Halle (Westf.)', 'g', 'vor 1 Woche', 'Drei Fotos geschickt, am nächsten Morgen war das Angebot da. Der Foto-Check ist genial.'),
 ('Gerd H.', 'Steinhagen', 'g', 'vor 4 Monaten', 'Wartungsvertrag Komfort: Die Wärmepumpe meldet sich selbst, wenn etwas ist. Zwei Winter ohne Ausfall.'),
 ('Anja B.', 'Bielefeld-Brackwede', 'tp', 'vor 3 Monaten', 'Freundlich, pünktlich und im Wohnzimmer Schuhe aus. Kleinigkeit, aber man merkt es.'),
 ('Ralf S.', 'Werther', 'g', 'vor 2 Wochen', 'Heinz hat uns ehrlich gesagt, dass sich die Wärmepumpe bei uns erst nach der Dämmung lohnt. Solche Beratung bekommt man selten.'),
]
def card(r):
    n, o, s, d, t = r
    src = (G + '<span>Google</span>') if s == 'g' else (TP + '<span>Trustpilot</span>')
    return f'<figure class="rv"><div class="rv-top">{stars()}<span class="rv-src">{src}</span></div><blockquote>„{t}“</blockquote><figcaption><b>{n}</b> · {o}<span>{d}</span></figcaption></figure>'
row1 = ''.join(card(r) for r in R[:5]); row2 = ''.join(card(r) for r in R[5:])

CHIPS = f'''<div class="rating-chips">
  <a href="index.html#bewertungen" class="rchip">{G}<b>4,9</b>{stars()}<span>127 Google-Bewertungen</span></a>
  <a href="index.html#bewertungen" class="rchip">{TP}<b>4,8</b>{stars()}<span>86 auf Trustpilot</span></a>
</div>'''
part('rating-chips', CHIPS)

part('bewertungen', f'''<!-- ============ BEWERTUNGEN (Google + Trustpilot, Demo) ============ -->
<section class="sec reviews" id="bewertungen">
  <div class="wrap">
    <div class="sec-head">
      <div><p class="kicker">Bewertungen</p><h2 class="reveal">213 Kunden. <em>4,9 Sterne.</em></h2></div>
      <div class="rv-score">
        <a href="https://www.google.com/maps" target="_blank" rel="noopener" class="score">{G}<div><b>4,9</b>{stars()}<span>127 Bewertungen auf Google</span></div></a>
        <a href="https://de.trustpilot.com/" target="_blank" rel="noopener" class="score">{TP}<div><b>4,8</b>{stars()}<span>„Hervorragend“ · 86 auf Trustpilot</span></div></a>
      </div>
    </div>
  </div>
  <div class="rv-rows" aria-label="Kundenbewertungen">
    <div class="rv-row"><div class="rv-track">{row1}{row1}</div></div>
    <div class="rv-row rev"><div class="rv-track">{row2}{row2}</div></div>
  </div>
  <div class="wrap rv-foot"><p>Beispielbewertungen für die Demo · echte Bewertungen werden live aus Google und Trustpilot eingebunden.</p>
    <div class="ctas"><a href="https://www.google.com/maps" target="_blank" rel="noopener" class="btn line">Auf Google bewerten <span>→</span></a><a href="https://de.trustpilot.com/" target="_blank" rel="noopener" class="btn line">Auf Trustpilot lesen <span>→</span></a></div></div>
</section>
''')

IG = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r="1.1" class="f"/></svg>'
FB = '<svg viewBox="0 0 24 24" aria-hidden="true"><path class="f" d="M13.5 21v-7.5h2.6l.4-3h-3V8.6c0-.9.3-1.5 1.6-1.5h1.6V4.4c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4V10.5H8v3h2.5V21z"/></svg>'
TT = '<svg viewBox="0 0 24 24" aria-hidden="true"><path class="f" d="M16.6 3c.4 2.2 1.8 3.6 4 3.8v3c-1.5 0-2.8-.4-4-1.2v6.3a5.6 5.6 0 1 1-5.6-5.6c.3 0 .6 0 .9.1v3.1a2.6 2.6 0 1 0 1.7 2.4V3z"/></svg>'
YT = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="5.5" width="19" height="13" rx="4"/><path class="f" d="M10 9.2v5.6l5-2.8z"/></svg>'
LI = '<svg viewBox="0 0 24 24" aria-hidden="true"><path class="f" d="M4 9h3.4v11H4zM5.7 3.5a2 2 0 1 1 0 4 2 2 0 0 1 0-4zM9.6 9h3.3v1.5c.5-.9 1.6-1.8 3.3-1.8 3.5 0 4.1 2.3 4.1 5.3v6H17v-5.3c0-1.3 0-2.9-1.8-2.9s-2.1 1.4-2.1 2.8V20H9.6z"/></svg>'
WA = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20l1.2-3.6A8 8 0 1 1 8 19z"/><path class="f" d="M9 8.3c.2-.4.4-.4.7-.4h.5c.2 0 .4 0 .5.4l.7 1.6c.1.2 0 .4-.1.5l-.5.6c-.1.1-.2.3 0 .5.5.9 1.4 1.8 2.4 2.3.2.1.4.1.5 0l.6-.7c.2-.2.3-.2.5-.1l1.6.8c.2.1.3.2.3.4 0 .5-.2 1.2-.8 1.5-.6.3-1.4.4-2.7-.1-2-.8-3.6-2.6-4.1-3.7-.4-.9-.4-1.9 0-2.6z"/></svg>'
SOC = [('Instagram', IG, 'https://www.instagram.com/'), ('Facebook', FB, 'https://www.facebook.com/'), ('TikTok', TT, 'https://www.tiktok.com/'),
       ('YouTube', YT, 'https://www.youtube.com/'), ('LinkedIn', LI, 'https://www.linkedin.com/'), ('WhatsApp', WA, 'https://wa.me/495210000000')]
part('social-icons', '<div class="social">' + ''.join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="WARMHERZ auf {n} (Demo)" title="{n}">{s}</a>' for n, s, u in SOC) + '</div>')

POSTS = [('keller-nachher', 'Vorher: Öltank. Nachher: Platz für die Tischtennisplatte. Keller in Schildesche, 4 Tage.', '1.204', 'reel'),
         ('lea', 'Lea, 2. Lehrjahr: „Die erste eigene Pressung vergisst man nicht.“', '987', ''),
         ('transporter', '06:58 Uhr. Die Flotte rollt.', '642', ''),
         ('team', 'Sechs Leute, ein Ziel: Bielefeld warm. Wir suchen Verstärkung, Link in Bio.', '1.531', 'reel'),
         ('kaffee', 'Erst Kaffee, dann Wärmepumpe.', '458', ''),
         ('p-fussboden', 'Fräsen statt Estrich raus: Fußbodenheizung an einem Tag.', '873', 'reel')]
REEL = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="4"/><path class="f" d="M10 8.8v6.4l5.2-3.2z"/></svg>'
HEART = '<svg viewBox="0 0 24 24" aria-hidden="true"><path class="f" d="M12 21S3 15.5 3 9a4.5 4.5 0 0 1 9-1.5A4.5 4.5 0 0 1 21 9c0 6.5-9 12-9 12z"/></svg>'
tiles = ''.join(f'''<a href="https://www.instagram.com/" target="_blank" rel="noopener" class="ig-tile"><img src="assets/img/{i}.webp" alt="" loading="lazy">{('<span class="ig-type">' + REEL + '</span>') if r else ''}<span class="ig-ov"><span class="ig-like">{HEART}{l}</span><span class="ig-cap">{c}</span></span></a>''' for i, c, l, r in POSTS)
part('instagram', f'''<!-- ============ INSTAGRAM (Demo-Kanal) ============ -->
<section class="sec ig-sec" id="instagram">
  <div class="wrap">
    <div class="ig-head">
      <div class="ig-prof">
        <span class="ig-ava"><span class="logo-mark"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21S3 15.5 3 9a4.5 4.5 0 0 1 9-1.5A4.5 4.5 0 0 1 21 9c0 6.5-9 12-9 12z"/></svg></span></span>
        <div><p class="kicker">Instagram</p><h2 class="reveal">@warmherz.<em>bielefeld</em></h2>
          <p class="ig-stats"><b>214</b> Beiträge <b>2.481</b> Follower <b>Baustellen, Team, Vorher/Nachher</b></p></div>
      </div>
      <a href="https://www.instagram.com/" target="_blank" rel="noopener" class="btn acc">{IG}Folgen <span>→</span></a>
    </div>
    <div class="ig-grid">{tiles}</div>
    <div class="ig-foot"><span>Auch hier:</span>{{{{> social-icons}}}}</div>
  </div>
</section>
''')
print('Teile: rating-chips, bewertungen, social-icons, instagram')
