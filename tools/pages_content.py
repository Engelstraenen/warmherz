#!/usr/bin/env python3
"""Schreibt die Seiteninhalte nach src/pages und neue Teile nach src/parts. Danach: python3 tools/build.py"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P, T = os.path.join(ROOT, 'src/pages'), os.path.join(ROOT, 'src/parts')

def page(fn, meta, body): open(os.path.join(P, fn), 'w').write('<!--' + json.dumps(meta, ensure_ascii=False) + '-->\n' + body)
def part(fn, body): open(os.path.join(T, fn + '.html'), 'w').write(body)

def phero(img, crumb, kicker, h1, sub, ctas='', cls='', video=None):
    c = f'<div class="crumbs"><a href="index.html">Start</a><span>/</span>{crumb}</div>' if crumb else ''
    media = (f'<video src="assets/video/{video}.mp4" poster="assets/img/{img}.webp" autoplay muted loop playsinline preload="auto" aria-hidden="true"></video>'
             if video else f'<img src="assets/img/{img}.webp" alt="" fetchpriority="high">')
    return f'''<section class="phero {cls}">
  {media}
  <div class="shade"></div>
  <div class="in">{c}
    <p class="kicker">{kicker}</p>
    <h1 class="reveal">{h1}</h1>
    <p class="sub reveal">{sub}</p>
    {('<div class="ctas">' + ctas + '</div>') if ctas else ''}
  </div>
</section>
'''
def phero_ba(crumb, kicker, h1, sub, ctas):
    """Kopfbild mit Vorher/Nachher-Schieber (Keller 1990 / heute)."""
    return f'''<section class="phero ba-hero" id="vorher-nachher">
  <div class="ba-box" data-ba style="--p:50%">
    <img src="assets/img/keller-nachher.webp" alt="Nachher: heller Technikraum mit Wärmepumpe" fetchpriority="high">
    <div class="ba-before"><img src="assets/img/keller-vorher.webp" alt="Vorher: alter Heizungskeller mit Öltank"></div>
    <input type="range" min="0" max="100" value="50" aria-label="Vorher-Nachher-Regler" data-ba-range>
    <div class="ba-handle" aria-hidden="true"><span>⟷</span></div>
  </div>
  <div class="shade"></div>
  <span class="ba-tag l">Vorher · 1990</span><span class="ba-tag r">Nachher · heute</span>
  <div class="in"><div class="crumbs"><a href="index.html">Start</a><span>/</span>{crumb}</div>
    <p class="kicker">{kicker}</p>
    <h1 class="reveal">{h1}</h1>
    <p class="sub reveal">{sub}</p>
    <div class="ctas">{ctas}</div>
  </div>
</section>
'''
def btn(href, text, kind='acc'): return f'<a href="{href}" class="btn {kind}">{text} <span>→</span></a>'
def faq(items): return '<div class="faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items) + '</div>'
def cta(h, b1, b2=None): return f'''<section class="cta-band"><div class="wrap"><h2>{h}</h2><div class="ctas">{btn(*b1, 'dark')}{btn(*b2, 'white') if b2 else ''}</div></div></section>
'''

# ------------------------------------------------------------------ neue Teile
part('leistungen-teaser', f'''<!-- ============ LEISTUNGEN (TEASER) ============ -->
<section class="sec light" id="leistungen">
  <div class="wrap">
    <div class="sec-head"><div><p class="kicker">Was wir machen</p><h2 class="reveal">Alles, was Ihr Haus <em>warm</em> macht.</h2></div>
    <p class="sub reveal">Ein Team, ein Ansprechpartner, ein Termin. Wählen Sie, worum es bei Ihnen geht.</p></div>
    <div class="cards">
      <a href="waermepumpe.html" class="card"><div class="card-img"><img src="assets/img/lukas.webp" alt="Monteur Lukas an einer Wärmepumpe" loading="lazy"></div><h3>Wärmepumpe</h3><p>Luft, Erde oder Hybrid. Raumweise berechnet, nicht nach Gefühl.</p><span class="more">Mehr erfahren →</span></a>
      <a href="heizungstausch.html" class="card"><div class="card-img"><img src="assets/img/keller-nachher.webp" alt="Technikraum nach dem Heizungstausch" loading="lazy"></div><h3>Heizungstausch</h3><p>Öl oder Gas raus, neue Technik rein. Meist in 2–3 Tagen.</p><span class="more">Mehr erfahren →</span></a>
      <a href="fussbodenheizung.html" class="card"><div class="card-img"><img src="assets/img/p-fussboden.webp" alt="Fußbodenheizung wird in den Estrich gefräst" loading="lazy"></div><h3>Fußbodenheizung</h3><p>Auch nachträglich: gefräst in den alten Estrich.</p><span class="more">Mehr erfahren →</span></a>
      <a href="bad.html" class="card"><div class="card-img"><img src="assets/img/p-bad.webp" alt="Neues Bad mit bodengleicher Dusche" loading="lazy"></div><h3>Bad</h3><p>Vom Gäste-WC bis zum barrierefreien Bad, mit festem Endtermin.</p><span class="more">Mehr erfahren →</span></a>
      <a href="wartung.html" class="card"><div class="card-img"><img src="assets/img/p-wartung.webp" alt="Murat wartet eine Wärmepumpe im Schnee" loading="lazy"></div><h3>Wartung & Notdienst</h3><p>Jährliche Wartung und im Winter rund um die Uhr erreichbar.</p><span class="more">Mehr erfahren →</span></a>
      <a href="foerderung.html" class="card"><div class="card-img"><img src="assets/img/display.webp" alt="Lukas erklärt die neue Wärmepumpe" loading="lazy"></div><h3>Förderung</h3><p>Bis zu 70 % Zuschuss. Wir rechnen aus und stellen den Antrag mit Ihnen.</p><span class="more">Zuschuss berechnen →</span></a>
    </div>
  </div>
</section>

''')

part('foerder-teaser', f'''<!-- ============ FÖRDERUNG (TEASER) ============ -->
<section class="sec" id="foerderung-kurz">
  <div class="wrap duo">
    <div>
      <p class="kicker">Förderung</p>
      <h2 class="reveal">Bis zu <em>80 %</em> zahlt der Staat.</h2>
      <p class="sub">Grundförderung, Klimabonus und Einkommensbonus: Wir rechnen Ihren Zuschuss in einer Minute aus und stellen den Antrag mit Ihnen. Aber nicht mehr lange zum heutigen Satz.</p>
      <ul class="checks"><li>Zuschuss in Euro, sofort im Rechner</li><li>Antrag füllen wir gemeinsam aus</li><li>Ab 1. Februar 2027 sinkt der Klimabonus</li></ul>
      <div class="dayvid-ctas">{btn('foerderung.html', 'Meinen Zuschuss berechnen')}</div>
    </div>
    <div class="result">
      <small>Beispiel: Ölheizung, 32.000 € Kosten, selbst bewohnt</small>
      <div class="big">12.880 €</div>
      <div class="later"><div><small>ab 1. Februar 2027</small><b>11.445 €</b></div><div class="loss"><small>Wer wartet, verliert</small><b>− 1.435 €</b></div></div>
      <p class="fine">Beispielrechnung ohne Gewähr. Verbindlich ist die aktuelle BEG-Richtlinie.</p>
    </div>
  </div>
</section>

''')

part('foto-teaser', f'''<!-- ============ FOTO-CHECK (TEASER) ============ -->
<section class="check" id="foto-check-kurz">
  <div class="wrap check-grid">
    <div>
      <p class="kicker">Foto-Check</p>
      <h2 class="reveal">3 Fotos schicken. <em>Wir wissen sofort Bescheid.</em></h2>
      <p class="sub">Heizung macht Probleme, Fleck an der Decke, neue Heizung geplant? Schicken Sie 3 bis 5 Fotos und zwei Sätze. Wir sehen sofort, was los ist, und bringen gleich das passende Teil mit.</p>
      <ul class="steps"><li><b>1</b>Thema wählen</li><li><b>2</b>3 bis 5 Fotos machen</li><li><b>3</b>Abschicken, wir melden uns heute</li></ul>
      <div class="dayvid-ctas">{btn('foto-check.html', 'Zum Foto-Check', 'dark')}</div>
    </div>
    <div class="phone">
      <div class="phone-in">
        <div class="ph-head"><b>Foto-Check</b><small>WARMHERZ</small></div>
        <div class="slot filled" style="background-image:url(assets/img/keller-vorher.webp)"><span class="slot-ph"><i>✓</i>Heizraum</span></div>
        <div class="slot"><span class="slot-ph"><i>+</i>Typenschild</span></div>
        <div class="slot"><span class="slot-ph"><i>+</i>Heizkörper</span></div>
        <a href="foto-check.html" class="btn acc full">Weiter <span>→</span></a>
      </div>
    </div>
  </div>
</section>

''')

# ------------------------------------------------------------------ Startseite
page('index.html', {"title": "WARMHERZ · Heizung & Wärmepumpe in Bielefeld (Demo)", "desc": "Demo-Webseite eines fiktiven Familienbetriebs für Wärmepumpen, Heizung und Bad in Bielefeld.", "key": "start", "preload": "assets/img/h-luecke.webp"},
'''{{> hero}}{{> band}}{{> foto-teaser}}{{> warmflug}}{{> leistungen-teaser}}{{> foerder-teaser}}{{> vorher-nachher}}{{> jobs-teaser}}{{> chef}}''' + cta('Lieber kurz sprechen? <br>Wir gehen ran.', ('tel:+495210000000', '0521 000 00 00 anrufen'), ('kontakt.html', 'Rückruf anfordern')))

# ------------------------------------------------------------------ Leistungen
page('waermepumpe.html', {"title": "Wärmepumpe · WARMHERZ Bielefeld (Demo)", "desc": "Wärmepumpe vom Familienbetrieb: Luft-Wasser, Erdwärme oder Hybrid, raumweise berechnet, Einbau in 2–3 Tagen.", "key": "waermepumpe"},
phero('lukas', 'Leistungen<span>/</span>Wärmepumpe', 'Wärmepumpe', 'Wärme aus der Luft. <em>Auch bei −15 °C.</em>', 'Wir planen und bauen Wärmepumpen für Bestandshäuser in Ostwestfalen: raumweise berechnet, leise aufgestellt, in 2–3 Tagen eingebaut.', btn('foerderung.html', 'Zuschuss berechnen') + btn('foto-check.html', 'Fotos schicken', 'line')) +
'{{> waermepumpe-haus}}' + f'''<section class="sec light">
  <div class="wrap">
    <div class="sec-head"><div><p class="kicker">Drei Bauarten</p><h2 class="reveal">Welche passt zu <em>Ihrem</em> Haus?</h2></div><p class="sub">Wir empfehlen nicht das teuerste Gerät, sondern das, was zu Ihrem Haus passt.</p></div>
    <div class="cards">
      <div class="card"><div class="big-n">01</div><h3>Luft-Wasser</h3><p>Holt Wärme aus der Außenluft. Die häufigste Lösung im Bestand: schnell eingebaut, wenig Platz, keine Bohrung.</p><span class="pill">passt zu den meisten Häusern</span></div>
      <div class="card"><div class="big-n">02</div><h3>Erdwärme</h3><p>Nutzt die gleichbleibende Wärme im Boden. Sehr effizient und praktisch lautlos, braucht eine Bohrung oder Kollektoren.</p><span class="pill">große Häuser, Neubau</span></div>
      <div class="card"><div class="big-n">03</div><h3>Hybrid</h3><p>Wärmepumpe plus vorhandener Kessel für die kältesten Tage. Ein sanfter Einstieg, wenn die Heizkörper noch nicht passen.</p><span class="pill">unsanierte Häuser</span></div>
    </div>
  </div>
</section>
<section class="sec">
  <div class="wrap duo">
    <div class="split-img"><img src="assets/img/lea.webp" alt="Lea und Lukas verlegen Rohre im Technikraum" loading="lazy"></div>
    <div>
      <p class="kicker">Altbau?</p>
      <h2 class="reveal">Geht meistens. <em>Wir prüfen ehrlich.</em></h2>
      <p class="sub">Entscheidend ist nicht das Baujahr, sondern welche Vorlauftemperatur Ihre Heizkörper brauchen. Oft reicht es, zwei oder drei Heizkörper zu tauschen.</p>
      <ul class="checks"><li>Raumweise Heizlastberechnung statt Daumenregel</li><li>Aufstellort mit Blick auf die Nachbarn geplant</li><li>Festpreis-Angebot mit Ihrem Zuschuss in Euro</li><li>Einweisung am letzten Tag, Wartung jedes Jahr</li></ul>
    </div>
  </div>
</section>
<section class="sec light"><div class="wrap"><p class="kicker">Häufige Fragen</p><h2 class="reveal" style="margin-bottom:40px">Was Kunden uns <em>fragen.</em></h2>''' + faq([
    ('Wie laut ist das Außengerät?', 'Moderne Geräte sind etwa so leise wie ein Kühlschrank in einigen Metern Abstand. Den Aufstellort planen wir so, dass auch die Nachbarn nichts merken.'),
    ('Was kostet eine Wärmepumpe?', 'Im Einfamilienhaus meist zwischen 25.000 und 40.000 € inklusive Einbau. Davon übernimmt der Staat bis zu 70 %. Rechnen Sie es im Förderrechner aus.'),
    ('Wie lange dauert der Einbau?', 'Meist zwei bis drei Tage. Abends ist es bei Ihnen trotzdem warm, wir lassen niemanden frieren.'),
    ('Brauche ich eine Fußbodenheizung?', 'Nein. Oft reichen die vorhandenen Heizkörper oder ein paar größere. Fußbodenheizung ist ideal, aber kein Muss.')]) + '</div></section>\n' +
cta('Passt eine Wärmepumpe zu Ihrem Haus?', ('foto-check.html', 'Fotos schicken, wir prüfen'), ('foerderung.html', 'Zuschuss berechnen')))

page('heizungstausch.html', {"title": "Heizungstausch · WARMHERZ Bielefeld (Demo)", "desc": "Öl- oder Gasheizung tauschen: Rückbau, Einbau der Wärmepumpe in 2–3 Tagen, Förderantrag inklusive.", "key": "heizungstausch"},
phero_ba('Leistungen<span>/</span>Heizungstausch', 'Heizungstausch', 'Öl raus. <em>Platz rein.</em>', 'Wir bauen Ihre alte Öl- oder Gasheizung zurück, entsorgen den Tank und setzen eine Wärmepumpe ein. Meist in 2–3 Tagen, mit Förderantrag.', btn('foerderung.html', 'Zuschuss berechnen') + btn('ablauf.html', "So läuft's ab", 'line')) +
f'''<section class="sec light">
  <div class="wrap">
    <div class="sec-head"><div><p class="kicker">In drei Tagen</p><h2 class="reveal">Was bei Ihnen <em>passiert.</em></h2></div><p class="sub">Folie auf dem Boden, Überzieher an den Schuhen. Abends ist es wieder warm.</p></div>
    <div class="cards">
      <div class="card"><div class="big-n">Tag 1</div><h3>Rückbau</h3><p>Alter Kessel raus, Öltank leeren, zerlegen und fachgerecht entsorgen. Leitungen vorbereiten.</p></div>
      <div class="card"><div class="big-n">Tag 2</div><h3>Einbau</h3><p>Außengerät aufstellen, Inneneinheit und Speicher anschließen, Rohre sauber dämmen.</p></div>
      <div class="card"><div class="big-n">Tag 3</div><h3>Einweisung</h3><p>Inbetriebnahme, hydraulischer Abgleich, Einweisung am Gerät und Unterlagen für die Förderung.</p></div>
    </div>
  </div>
</section>
<section class="sec">
  <div class="wrap duo rev">
    <div class="split-img"><img src="assets/img/baustelle.webp" alt="Schutzfolie und Überzieher auf der Baustelle" loading="lazy"></div>
    <div><p class="kicker">Sauber</p><h2 class="reveal">Wir gehen, wie wir <em>gekommen</em> sind.</h2><p class="sub">Folie auf den Boden, bevor das erste Werkzeug den Koffer verlässt. Am Ende saugen wir durch. Versprochen.</p>
    <ul class="checks"><li>Tank-Entsorgung inklusive</li><li>Schornsteinfeger-Termine entfallen</li><li>Rund ein Drittel mehr Platz im Keller</li></ul></div>
  </div>
</section>
''' + cta('Ihre Heizung ist über 20 Jahre alt?', ('foerderung.html', 'Zuschuss berechnen'), ('foto-check.html', 'Heizraum fotografieren')))

page('fussbodenheizung.html', {"title": "Fußbodenheizung nachrüsten · WARMHERZ (Demo)", "desc": "Fußbodenheizung nachträglich einfräsen: ohne neuen Estrich, ideal für die Wärmepumpe.", "key": "fussbodenheizung"},
phero('p-fussboden', 'Leistungen<span>/</span>Fußbodenheizung', 'Fußbodenheizung', 'Warme Füße. <em>Ohne neuen Estrich.</em>', 'Wir fräsen die Rohre direkt in Ihren vorhandenen Estrich. Kein Aufreißen, kein wochenlanges Trocknen: meist ein Tag pro Raum.', btn('foto-check.html', 'Raum fotografieren') + btn('kontakt.html', 'Rückruf anfordern', 'line')) +
f'''{{{{> boden-flow}}}}<section class="sec"><div class="wrap duo"><div><p class="kicker">Warum?</p><h2 class="reveal">Der beste Partner für die <em>Wärmepumpe.</em></h2><p class="sub">Eine Fußbodenheizung braucht nur 30 bis 35 °C. Damit arbeitet die Wärmepumpe besonders sparsam.</p>
<ul class="checks"><li>Bis zu 15 % weniger Stromverbrauch</li><li>Keine Heizkörper unter dem Fenster</li><li>Gleichmäßige Wärme, weniger Staub in der Luft</li></ul></div>
<div class="split-img"><img src="assets/img/familie.webp" alt="Kind barfuß auf warmem Holzboden" loading="lazy"></div></div></section>
''' + cta('Welche Räume sollen warm werden?', ('foto-check.html', 'Fotos schicken'), ('kontakt.html', 'Rückruf anfordern')))

page('bad.html', {"title": "Bad · WARMHERZ Bielefeld (Demo)", "desc": "Badsanierung vom Familienbetrieb: vom Gäste-WC bis zum barrierefreien Bad, mit festem Endtermin.", "key": "bad"},
phero('p-bad', 'Leistungen<span>/</span>Bad', 'Bad', 'Ein neues Bad. <em>Mit festem Endtermin.</em>', 'Fliesen, Wasser, Wärme und Licht aus einer Hand. Wir sagen Ihnen vorher, an welchem Tag Sie wieder duschen.', btn('foto-check.html', 'Bad fotografieren') + btn('kontakt.html', 'Beratung anfragen', 'line')) +
f'''{{{{> bad-flow}}}}<section class="sec light">
  <div class="wrap">
    <div class="sec-head"><div><p class="kicker">Was wir bauen</p><h2 class="reveal">Für jedes Alter. <em>Für jedes Budget.</em></h2></div></div>
    <div class="cards">
      <div class="card"><div class="big-n">01</div><h3>Gäste-WC</h3><p>Klein, aber fein. Oft in einer Woche fertig.</p><span class="pill">ab ca. 1 Woche</span></div>
      <div class="card"><div class="big-n">02</div><h3>Familienbad</h3><p>Bodengleiche Dusche, Badewanne, viel Stauraum und warme Handtücher.</p><span class="pill">ca. 2–3 Wochen</span></div>
      <div class="card"><div class="big-n">03</div><h3>Barrierefrei</h3><p>Ohne Schwellen, mit Haltegriffen. Mit Zuschuss der Pflegekasse möglich.</p><span class="pill">Zuschuss möglich</span></div>
    </div>
  </div>
</section>
<section class="sec"><div class="wrap duo rev"><div class="split-img"><img src="assets/img/baustelle.webp" alt="Sauber abgeklebte Baustelle" loading="lazy"></div><div><p class="kicker">Ein Team</p><h2 class="reveal">Keine fünf Firmen. <em>Ein Ansprechpartner.</em></h2><p class="sub">Installateur, Fliesenleger und Elektriker stimmen wir für Sie ab. Sie haben nur eine Telefonnummer.</p>
<ul class="checks"><li>Fester Endtermin im Angebot</li><li>Staubschutz und tägliche Reinigung</li><li>3D-Planung auf Wunsch</li></ul></div></div></section>
''' + cta('Wie sieht Ihr Bad heute aus?', ('foto-check.html', 'Fotos schicken'), ('kontakt.html', 'Beratung anfragen')))

page('wartung.html', {"title": "Wartung & Notdienst · WARMHERZ (Demo)", "desc": "Wartung für Wärmepumpe und Heizung, Notdienst im Winter rund um die Uhr.", "key": "wartung"},
f'''{{{{> notdienst-film}}}}{{{{> notdienst-flow}}}}<section class="sec light">
  <div class="wrap">
    <div class="sec-head"><div><p class="kicker">Wartungsvertrag</p><h2 class="reveal">Einmal im Jahr. <em>Dann haben Sie Ruhe.</em></h2></div><p class="sub">Beispielpreise für die Demo, zzgl. Material.</p></div>
    <div class="plans">
      <div class="plan"><h3>Basis</h3><div class="price">149 € <small>/ Jahr</small></div><ul><li>Jährliche Wartung</li><li>Protokoll für Garantie und Förderung</li><li>Termin-Erinnerung</li></ul><a href="kontakt.html?thema=wartung#kontakt" class="btn dark">Anfragen <span>→</span></a></div>
      <div class="plan hot"><h3>Komfort</h3><div class="price">249 € <small>/ Jahr</small></div><ul><li>Alles aus Basis</li><li>Fernüberwachung der Wärmepumpe</li><li>Vorrang im Notdienst</li><li>Keine Anfahrtskosten</li></ul><a href="kontakt.html?thema=wartung#kontakt" class="btn acc">Anfragen <span>→</span></a></div>
      <div class="plan"><h3>Rundum</h3><div class="price">399 € <small>/ Jahr</small></div><ul><li>Alles aus Komfort</li><li>Kleinteile inklusive</li><li>Notdienst ohne Zuschlag</li></ul><a href="kontakt.html?thema=wartung#kontakt" class="btn dark">Anfragen <span>→</span></a></div>
    </div>
  </div>
</section>
<section class="sec"><div class="wrap duo"><div><p class="kicker">Störung?</p><h2 class="reveal">Fehlercode fotografieren. <em>Wir wissen Bescheid.</em></h2><p class="sub">Schicken Sie uns ein Foto vom Display und vom Typenschild. Murat sieht oft schon am Fehlercode, welches Teil er mitbringen muss.</p>
<div class="dayvid-ctas">{btn('foto-check.html', 'Störung per Foto melden')}</div></div>
<div class="split-img"><img src="assets/img/p-murat.webp" alt="Murat, Kundendienst" loading="lazy"></div></div></section>
''' + cta('Heizung aus? Rufen Sie an.', ('tel:+495210000099', 'Notdienst anrufen'), ('foto-check.html', 'Foto-Check')))

# ------------------------------------------------------------------ Förderung, Ablauf, Foto-Check
page('foerderung.html', {"title": "Förderrechner Wärmepumpe 2026 · WARMHERZ (Demo)", "desc": "Zuschuss für die Wärmepumpe in einer Minute berechnen. Ab 1. Februar 2027 sinkt der Klimageschwindigkeitsbonus.", "key": "foerderung"},
phero('display', 'Förderung', 'Förderung', 'Bis zu 80 % <em>vom Staat.</em>', 'Rechnen Sie Ihren Zuschuss in einer Minute aus. Den Antrag stellen wir gemeinsam mit Ihnen, bevor der Bonus am 1. Februar sinkt.', btn('#foerderung', 'Zum Rechner'), 'short') +
'{{> band}}{{> rechner}}' + f'''<section class="sec">
  <div class="wrap">
    <div class="sec-head"><div><p class="kicker">Die Bausteine</p><h2 class="reveal">Woraus sich Ihr <em>Zuschuss</em> zusammensetzt.</h2></div><p class="sub">Stand: KfW-Programm 458, gültig ab 21.07.2026.</p></div>
    <div class="cards c4">
      <div class="card"><div class="big-n">30 %</div><h3>Grundförderung</h3><p>Für jeden Heizungstausch auf eine Wärmepumpe.</p></div>
      <div class="card"><div class="big-n">16 %</div><h3>Klimabonus</h3><p>Wenn Sie selbst wohnen und eine alte Öl-, Gas-, Kohle- oder Nachtspeicherheizung ersetzen. Ab 1.2.2027: 12 %.</p></div>
      <div class="card"><div class="big-n">bis 40 %</div><h3>Einkommensbonus</h3><p>Gestaffelt nach zu versteuerndem Haushaltseinkommen: 40 % bis 30.000 €, 30 % bis 40.000 €, 10 % bis 50.000 €. Mit Kind unter 18 je 10.000 € mehr.</p></div>
      <div class="card"><div class="big-n">70–80 %</div><h3>Höchstgrenze</h3><p>Zusammen höchstens 70 % der förderfähigen Kosten, bei geringem Einkommen bis 80 %. Förderfähig sind bis 28.000 € (ab 1.2.2027: 27.250 €).</p></div>
    </div>
  </div>
</section>
<section class="sec light"><div class="wrap"><p class="kicker">Wichtig</p><h2 class="reveal" style="margin-bottom:40px">Fragen zur <em>Förderung.</em></h2>''' + faq([
    ('Muss ich den Antrag vor dem Auftrag stellen?', 'Ja. Der Antrag muss vor Beginn der Arbeiten gestellt sein. Wir unterschreiben einen Vertrag mit Vorbehalt der Förderzusage, damit Sie sicher sind.'),
    ('Was passiert am 1. Februar 2027?', 'Der Klimageschwindigkeitsbonus sinkt von 16 auf 12 Prozent und danach weiter. Wer früher beauftragt, bekommt mehr.'),
    ('Was ist der Wertschöpfungsbonus?', 'Ab 2027 ist ein neuer Baustein geplant: Wärmepumpen aus der EU sollen die volle Grundförderung behalten, andere weniger. Details stehen noch aus, wir halten Sie auf dem Laufenden.'),
    ('Wer stellt den Antrag?', 'Sie, mit uns zusammen. Wir füllen alles mit Ihnen aus und liefern alle Nachweise.'),
    ('Gilt das auch für Vermieter?', 'Ja, die Grundförderung von 30 % gilt auch für vermietete Häuser. Klima- und Einkommensbonus gibt es nur für Selbstnutzer.')]) + '</div></section>\n' +
cta('Ihr Zuschuss steht fest?', ('foto-check.html', 'Jetzt Fotos schicken'), ('kontakt.html', 'Rückruf anfordern')))

ablauf_old = open(os.path.join(T, 'ablauf-seite.html')).read()
page('ablauf.html', {"title": "So läuft Ihr Heizungstausch ab · WARMHERZ (Demo)", "desc": "In 5 Schritten zur Wärmepumpe: Fotos, Termin, Angebot mit Förderung, Einbau in 2–3 Tagen, Einweisung.", "key": "ablauf"},
ablauf_old.replace('<section class="sub-head" id="heizungstausch">', '<section class="sub-head" id="heizungstausch">').replace('href="index.html#check"', 'href="foto-check.html"').replace('3 Fotos schicken', 'Fotos schicken').replace('href="index.html#foerderung"', 'href="foerderung.html"') +
f'''<section class="sec" id="check">
  <div class="wrap duo">
    <div class="split-img"><img src="assets/img/display.webp" alt="Einweisung an der neuen Wärmepumpe" loading="lazy"></div>
    <div><p class="kicker">Schritt 1 in 2 Minuten</p><h2 class="reveal">Starten Sie mit <em>Fotos.</em></h2><p class="sub">Heizraum, Typenschild, Heizkörper: Damit können wir schon vor dem ersten Termin vieles einschätzen.</p>
    <div class="dayvid-ctas">{btn('foto-check.html', 'Zum Foto-Check')}</div></div>
  </div>
</section>
''' + cta('Fragen zum Ablauf?', ('tel:+495210000000', '0521 000 00 00 anrufen'), ('kontakt.html', 'Rückruf anfordern')))

page('foto-check.html', {"title": "Foto-Check · Problem per Foto schicken · WARMHERZ (Demo)", "desc": "3 bis 5 Fotos schicken, zwei Sätze schreiben, fertig. Wir melden uns heute und bringen gleich das Richtige mit.", "key": "foto-check"},
f'''<section class="sec" id="foto-check" style="padding-top:110px">
  <div class="wrap fc">
    <div>
      <div class="crumbs"><a href="index.html">Start</a><span>/</span>Foto-Check</div>
      <p class="kicker">Foto-Check</p>
      <h1 class="reveal" style="font-size:clamp(44px,5.6vw,84px);line-height:.95">Zeigen Sie uns, <em>wo es hakt.</em></h1>
      <p class="sub">3 bis 5 Fotos und zwei Sätze. Wir sehen sofort, was los ist, und kommen gleich mit dem richtigen Teil. Das spart Ihnen einen Termin und uns eine Fahrt.</p>
      <ol class="fc-steps"><li class="on" data-fc-step="1"><b>1</b>Thema wählen</li><li data-fc-step="2"><b>2</b>3 bis 5 Fotos machen</li><li data-fc-step="3"><b>3</b>Kurz beschreiben</li><li data-fc-step="4"><b>4</b>Abschicken, wir melden uns heute</li></ol>
      <div class="stats" style="grid-template-columns:1fr 1fr;margin-top:34px"><div><b>2 Min</b><span>dauert das Ausfüllen</span></div><div><b>heute</b><span>melden wir uns, werktags</span></div></div>
    </div>
    <form class="fc-form" data-fc novalidate>
      <h3>Ihr Foto-Check</h3><p>Demo: Fotos bleiben auf Ihrem Gerät und werden nicht gesendet.</p>
      <span class="fc-label">1 · Worum geht es?</span>
      <div class="fc-topics">
        <label><input type="radio" name="fc-topic" value="stoerung" checked><span>Heizung kaputt</span></label>
        <label><input type="radio" name="fc-topic" value="neu"><span>Neue Heizung</span></label>
        <label><input type="radio" name="fc-topic" value="bad"><span>Bad</span></label>
        <label><input type="radio" name="fc-topic" value="wasser"><span>Wasserschaden</span></label>
        <label><input type="radio" name="fc-topic" value="sonst"><span>Etwas anderes</span></label>
      </div>
      <p class="fc-hint" data-fc-hint></p>
      <span class="fc-label">2 · Fotos (mindestens 3)</span>
      <div class="fc-slots" data-fc-slots></div>
      <p class="fc-count" data-fc-count>0 von 3 Pflichtfotos</p>
      <span class="fc-label">3 · Was ist los?</span>
      <textarea data-fc-text placeholder="Zum Beispiel: Seit gestern zeigt das Display F28 und die Heizkörper bleiben kalt."></textarea>
      <span class="fc-label">4 · Wie erreichen wir Sie?</span>
      <div class="fc-row"><input type="text" autocomplete="name" placeholder="Name"><input type="tel" autocomplete="tel" placeholder="Telefon"></div>
      <button class="btn acc full" type="submit">Foto-Check abschicken <span>→</span></button>
      <div class="fc-done" data-fc-done><div class="akte"><small>Werkakte · neue Anfrage</small><b data-fc-title>Störung Heizung</b><span data-fc-sum>3 Fotos · Beschreibung</span><em>Sabine meldet sich heute</em></div></div>
    </form>
  </div>
</section>
<section class="sec light">
  <div class="wrap">
    <div class="sec-head"><div><p class="kicker">Was dann passiert</p><h2 class="reveal">Von Ihren Fotos <em>zur Lösung.</em></h2></div></div>
    <div class="cards">
      <div class="card"><div class="big-n">1</div><h3>Akte entsteht</h3><p>Ihre Fotos landen direkt als Akte in unserer Werkakte-App. Nichts geht im E-Mail-Postfach verloren.</p></div>
      <div class="card"><div class="big-n">2</div><h3>Profi schaut drauf</h3><p>Heinz oder Murat sehen sich alles an und erkennen meist schon, was fehlt.</p></div>
      <div class="card"><div class="big-n">3</div><h3>Richtig ausgerüstet</h3><p>Wir rufen an, nennen einen Termin und bringen das passende Teil gleich mit.</p></div>
    </div>
  </div>
</section>
''')

# ------------------------------------------------------------------ Karriere
jobs_old = open(os.path.join(T, 'jobs-seite.html')).read()
import re
why = re.search(r'<div class="why">.*?</div>\n', jobs_old, re.S).group(0)
joblist = re.search(r'<div class="jobs">.*?</details>\n    </div>\n', jobs_old, re.S).group(0)
apply = re.search(r'<div class="apply" id="bewerben">.*?</form>\n      </div>\n    </div>\n', jobs_old, re.S).group(0)
day = re.search(r'<section class="day" id="dein-tag">.*?</section>\n', jobs_old, re.S).group(0)
platz_hero = re.search(r'<div class="platz-hero">.*?</div>\n  </div>\n', jobs_old, re.S).group(0)

page('jobs.html', {"title": "Jobs bei WARMHERZ · Ausbildung & Fachkräfte (Demo)", "desc": "Jobs und Ausbildung bei WARMHERZ (Demo): Gehalt offen, Feierabend 16:30, Bewerbung in 60 Sekunden.", "key": "jobs"},
f'''<section class="platz sub-top" id="jobs">
  {platz_hero}<div class="wrap">
    {why}  </div>
</section>
<section class="sec" style="padding-top:40px">
  <div class="wrap">
    <div class="cards c2">
      <a href="ausbildung.html" class="card"><div class="card-img"><img src="assets/img/p-azubis.webp" alt="Heinz erklärt Azubis die Wärmepumpe" loading="lazy"></div><p class="kicker" style="margin:0 0 6px">Für Schüler & Schülerinnen</p><h3 style="font-size:36px">Ausbildung</h3><p>Anlagenmechaniker/in SHK. Ab Tag 1 auf der Baustelle, Übernahme garantiert, Meisterkurs bezahlt.</p><span class="more">Dein Tag als Azubi →</span></a>
      <a href="fachkraefte.html" class="card"><div class="card-img"><img src="assets/img/p-finn.webp" alt="Finn in der Werkstatt" loading="lazy"></div><p class="kicker" style="margin:0 0 6px">Für Gesellen & Quereinsteiger</p><h3 style="font-size:36px">Fachkräfte</h3><p>3.400–4.400 €, eigener Transporter, Freitag 13 Uhr frei, 6 Monate bezahlter Quereinstieg.</p><span class="more">Alles für Fachkräfte →</span></a>
    </div>
  </div>
</section>
<section class="platz" id="stellen" style="padding-bottom:120px">
  <div class="wrap">
    <p class="kicker">Offene Stellen</p>
    <h2 class="reveal">Gehalt steht <em>dabei.</em></h2>
    {joblist}
    {apply}  </div>
</section>
''')

page('ausbildung.html', {"title": "Ausbildung Anlagenmechaniker/in SHK · WARMHERZ (Demo)", "desc": "Ausbildung bei WARMHERZ (Demo): Dein Tag als Azubi, was wir dir bieten, dein Weg bis zum Meister.", "key": "jobs"},
phero('p-azubis', '<a href="jobs.html">Jobs</a><span>/</span>Ausbildung', 'Ausbildung Anlagenmechaniker/in SHK', 'Lern was, <em>das die Welt braucht.</em>', 'Wärmepumpen sind die Heizung der Zukunft. Und es gibt viel zu wenige, die sie einbauen können. Werde einer von ihnen.', btn('#bewerben', 'In 60 Sekunden bewerben') + btn('#dein-tag', 'Dein Tag als Azubi', 'line')) +
f'''<section class="sec">
  <div class="wrap">
    <div class="sec-head"><div><p class="kicker">Was wir dir bieten</p><h2 class="reveal">Keine Floskeln. <em>Fakten.</em></h2></div><p class="sub">Was bei uns für Azubis gilt, ab dem ersten Tag.</p></div>
    <div class="cards">
      <div class="card"><div class="big-n">1.050 €</div><h3>im 1. Lehrjahr</h3><p>Steigt jedes Jahr. Plus Prämie für gute Noten in der Berufsschule.</p></div>
      <div class="card"><div class="big-n">Tag 1</div><h3>auf der Baustelle</h3><p>Kein Lager, kein Kehren. Du fährst mit raus und lernst bei echten Kunden.</p></div>
      <div class="card"><div class="big-n">100 %</div><h3>Übernahme</h3><p>Bei gutem Abschluss garantiert. Wir bilden aus, weil wir dich brauchen.</p></div>
      <div class="card"><div class="big-n">Tablet</div><h3>statt Zettel</h3><p>Eigenes Tablet mit der Werkakte-App. Dein Berichtsheft füllt sich fast von allein.</p></div>
      <div class="card"><div class="big-n">500 €</div><h3>Führerschein</h3><p>Zuschuss zum Führerschein Klasse B. Damit du bald selbst fährst.</p></div>
      <div class="card"><div class="big-n">16:30</div><h3>Feierabend</h3><p>Freitag ab 13 Uhr frei. Freizeit ist Freizeit.</p></div>
    </div>
  </div>
</section>
''' + day.replace('href="index.html#foerderung" class="door acc"><small>Das will ich auch</small>Zuschuss berechnen →', 'href="#bewerben" class="door acc" data-job="Ausbildung"><small>Das will ich machen</small>In 60 Sekunden bewerben →').replace('href="#bewerben" class="door white" data-job="Monteur/in"><small>Das will ich machen</small>In 60 Sekunden bewerben →', 'href="#zukunft" class="door white"><small>Und dann?</small>Dein Weg nach der Ausbildung →').replace('href="#foerderung" class="mini-calc"', 'href="foerderung.html" class="mini-calc"') +
f'''<section class="sec" id="lernen">
  <div class="wrap">
    <div class="sec-head"><div><p class="kicker">Deine Ausbildung</p><h2 class="reveal">Das lernst du. <em>Jahr für Jahr.</em></h2></div><p class="sub">3,5 Jahre, abwechselnd Baustelle und Berufsschule. Du bist nie allein: Lukas ist dein fester Ansprechpartner.</p></div>
    <ol class="path learn">
      <li data-step="1"><b>1. Lehrjahr</b><small>Grundlagen</small><p>Werkzeug und Material kennenlernen. Rohre zuschneiden, pressen und löten. Heizkörper und Waschtische mit montieren.</p></li>
      <li data-step="2"><b>2. Lehrjahr</b><small>Wasser & Heizung</small><p>Trinkwasser- und Abwasserleitungen verlegen, Bäder mit einbauen, Heizungen anschließen. Gesellenprüfung Teil 1.</p></li>
      <li data-step="3"><b>3. Lehrjahr</b><small>Wärmepumpe</small><p>Wärmepumpen aufstellen und in Betrieb nehmen, Regelung und Elektrik verstehen, erste Kundengespräche.</p></li>
      <li data-step="3½"><b>Letztes halbes Jahr</b><small>Prüfung</small><p>Störungen finden, Wartung, eigene kleine Aufträge unter Aufsicht. Gesellenprüfung Teil 2, danach Übernahme.</p></li>
    </ol>
  </div>
</section>
''' +
f'''<section class="sec light" id="zukunft">
  <div class="wrap">
    <div class="sec-head"><div><p class="kicker">Deine Zukunft</p><h2 class="reveal">Vom Azubi bis zum <em>Chef.</em></h2></div><p class="sub">Heinz ist 61 und sucht jemanden, der den Betrieb weiterführt. Wer weiß, vielleicht bist das in zehn Jahren du.</p></div>
    <ol class="path">
      <li data-step="1"><b>Azubi</b><small>3,5 Jahre</small><p>Rohre, Heizung, Wasser, Wärmepumpe. Mit Lukas an deiner Seite.</p></li>
      <li data-step="2"><b>Geselle</b><small>ab 3.400 €</small><p>Übernahme garantiert. Eigener Transporter nach der Einarbeitung.</p></li>
      <li data-step="3"><b>Spezialist</b><small>Wärmepumpe</small><p>Zertifikat und Kälteschein, bezahlt von uns. Die gefragteste Fachkraft der Branche.</p></li>
      <li data-step="4"><b>Meister</b><small>wir zahlen den Kurs</small><p>Meisterkurs in Teilzeit, Kosten übernehmen wir komplett.</p></li>
      <li data-step="5"><b>Nachfolge</b><small>dein Betrieb?</small><p>Heinz sucht jemanden, der WARMHERZ weiterführt. Ernsthaft.</p></li>
    </ol>
  </div>
</section>
<section class="sec">
  <div class="wrap duo">
    <div><p class="kicker">Warum gerade jetzt?</p><h2 class="reveal">Ein Beruf, der <em>nicht verschwindet.</em></h2><p class="sub">Jedes Haus in Deutschland muss in den nächsten Jahren auf neue Heizungen umsteigen. Das macht keine KI und kein Roboter. Das machen Leute wie du.</p>
    <ul class="checks"><li>Handwerk mit Zukunft und sicherem Job</li><li>Du siehst jeden Abend, was du geschafft hast</li><li>Klimaschutz mit den eigenen Händen</li></ul></div>
    <div class="split-img"><img src="assets/img/lea.webp" alt="Azubi Lea verpresst ein Rohr" loading="lazy"></div>
  </div>
</section>
<section class="sec light"><div class="wrap"><p class="kicker">Für dich & deine Eltern</p><h2 class="reveal" style="margin-bottom:40px">Was viele <em>fragen.</em></h2>''' + faq([
    ('Welchen Schulabschluss brauche ich?', 'Einen Hauptschulabschluss oder höher. Wichtiger ist uns, dass du gern mit den Händen arbeitest und pünktlich bist.'),
    ('Kann ich vorher ein Praktikum machen?', 'Ja, gern. Eine Woche mitfahren, dann weißt du, ob es passt. Schreib uns einfach im Bewerbungs-Chat.'),
    ('Wie viel verdiene ich in der Ausbildung?', 'Im ersten Jahr 1.050 €, danach steigt es jedes Jahr. Dazu Prämien für gute Noten.'),
    ('Ist der Beruf auch was für Mädchen?', 'Klar. Lea ist im zweiten Lehrjahr und das beste Beispiel. Werkzeug ist heute leicht, Köpfchen zählt mehr als Kraft.')]) + f'''</div></section>
<section class="platz" style="padding:110px 0"><div class="wrap">{apply}</div></section>
''')

page('fachkraefte.html', {"title": "Jobs für Fachkräfte & Quereinsteiger · WARMHERZ (Demo)", "desc": "Monteur/in, Kundendienst, Quereinstieg: Gehalt offen, eigener Transporter, Freitag 13 Uhr frei.", "key": "jobs"},
phero('p-finn', '<a href="jobs.html">Jobs</a><span>/</span>Fachkräfte', 'Fachkräfte & Quereinstieg', 'Gutes Handwerk. <em>Gut bezahlt.</em>', 'Wir suchen Monteure, Kundendienst-Techniker und Quereinsteiger. Mit offenem Gehalt, eigenem Transporter und pünktlichem Feierabend.', btn('#bewerben', 'In 60 Sekunden bewerben') + btn('jobs.html#stellen', 'Alle Stellen', 'line')) +
f'''<section class="sec">
  <div class="wrap">
    <div class="stats"><div><b>3.400 €</b><span>Einstieg Geselle, bis 4.400 € im Kundendienst</span></div><div><b>38 Std</b><span>pro Woche, Freitag ab 13 Uhr frei</span></div><div><b>30</b><span>Tage Urlaub</span></div><div><b>1.000 €</b><span>Prämie, wenn du jemanden mitbringst</span></div></div>
  </div>
</section>
<section class="sec light">
  <div class="wrap duo">
    <div><p class="kicker">Quereinstieg</p><h2 class="reveal">Elektriker, KFZ, Metall? <em>Du passt.</em></h2><p class="sub">Sechs Monate Einarbeitung zur Wärmepumpen-Fachkraft, voll bezahlt ab dem ersten Tag. Danach arbeitest du als Monteur im Team.</p>
    <ul class="checks"><li>Ab 3.100 € schon in der Einarbeitung</li><li>Fester Pate: Lukas oder Murat</li><li>Zertifikat und Kälteschein inklusive</li></ul>
    <div class="dayvid-ctas">{btn('#bewerben', 'Als Quereinsteiger bewerben')}</div></div>
    <div class="split-img"><img src="assets/img/transporter.webp" alt="Lukas fährt den Transporter" loading="lazy"></div>
  </div>
</section>
<section class="sec">
  <div class="wrap duo rev">
    <div class="split-img"><img src="assets/img/feierabend.webp" alt="Feierabend an der Werkstatt" loading="lazy"></div>
    <div><p class="kicker">Kein Papierkram</p><h2 class="reveal">Bericht in 2 Minuten. <em>In der App.</em></h2><p class="sub">Fotos, Stunden, Material: alles gleich auf der Baustelle in die Werkakte-App. Abends musst du nichts mehr schreiben.</p>
    <ul class="checks"><li>Eigener Transporter, auch am Wochenende</li><li>Werkzeug vom Feinsten, Akku statt Kabel</li><li>Bereitschaft extra bezahlt, max. 1 Woche im Monat</li></ul></div>
  </div>
</section>
<section class="platz" style="padding:40px 0 120px"><div class="wrap"><p class="kicker">Offene Stellen</p><h2 class="reveal">Such dir <em>deine</em> aus.</h2>{joblist}{apply}</div></section>
''')

# ------------------------------------------------------------------ Über uns, Kontakt, Rechtliches
team = [('heinz', 'Heinz Brinkmann, 61', 'Meister & Inhaber', 'Hat WARMHERZ 1987 gegründet. Sucht jemanden, der weitermacht.'),
        ('lukas', 'Lukas, 31', 'Monteur seit 2019', 'Am liebsten Altbauten. Da sieht man den Unterschied.'),
        ('p-sabine', 'Sabine, 45', 'Büro & Termine', 'Nimmt ab, wenn Sie anrufen. Und ruft zurück, wenn nicht.'),
        ('p-murat', 'Murat, 38', 'Kundendienst', 'Samstags auch. Wenn es kalt ist, ist es kalt.'),
        ('p-finn', 'Finn, 26', 'Monteur', 'Wärmepumpe, Bad, Fußboden: macht alles.'),
        ('lea', 'Lea, 19', 'Azubi, 2. Lehrjahr', 'Wollte nie ins Büro. Ist jetzt sehr froh darüber.')]
team_html = ''.join(f'<article class="member"><figure><img src="assets/img/{i}.webp" alt="{n}" loading="lazy"></figure><div><b>{n}</b><small>{r}</small><p>„{q}“</p></div></article>' for i, n, r, q in team)
page('ueber-uns.html', {"title": "Über uns · Familienbetrieb seit 1987 · WARMHERZ (Demo)", "desc": "WARMHERZ (Demo): sechs Leute, ein Familienbetrieb aus Bielefeld seit 1987.", "key": "ueber-uns"},
phero('h-schuhe', 'Über uns', 'Über uns', 'Sechs Leute. <em>Seit 1987.</em>', 'Kein Konzern, kein Callcenter. Ein Familienbetrieb aus Bielefeld, der Häuser warm macht, und eine Lücke im Team, die wir gern füllen.', btn('jobs.html', 'Jobs bei uns') + btn('kontakt.html', 'Kontakt', 'line')) +
f'''<section class="sec light">
  <div class="wrap">
    <div class="sec-head"><div><p class="kicker">Das Team</p><h2 class="reveal">Die Leute, die bei Ihnen <em>klingeln.</em></h2></div><p class="sub">Sie wissen vorher, wer kommt. Versprochen.</p></div>
    <div class="team">{team_html}<a href="jobs.html" class="member open"><p class="kicker" style="margin:0 0 10px">Freier Platz</p><b>Du?</b><p style="margin-top:10px">Wir suchen 2 Monteure und Azubis für 2027.</p><span class="more" style="margin-top:16px;color:var(--acc);font-weight:800">Zu den Jobs →</span></a></div>
  </div>
</section>
<section class="sec">
  <div class="wrap duo">
    <div><p class="kicker">Geschichte</p><h2 class="reveal" style="margin-bottom:40px">Von der Ölheizung zur <em>Wärmepumpe.</em></h2>
    <ul class="years">
      <li><b>1987</b><p>Heinz gründet den Betrieb in einer kleinen Garage in Sieker. Erster Auftrag: eine Ölheizung.</p></li>
      <li><b>2004</b><p>Umzug in die Werkstatt Am Kupferhammer. Erste Azubis, erstes Bad.</p></li>
      <li><b>2015</b><p>Die erste Wärmepumpe. Heute sind es über 80 im Jahr.</p></li>
      <li><b>2024</b><p>Schluss mit Zetteln: Alle Aufträge laufen über die Werkakte-App.</p></li>
      <li><b>2027</b><p>Heinz sucht seine Nachfolge. Und neue Leute für das Team.</p></li>
    </ul></div>
    <div class="split-img" style="aspect-ratio:4/5"><img src="assets/img/heinz.webp" alt="Heinz Brinkmann in der Werkstatt" loading="lazy" style="object-position:28% 40%"></div>
  </div>
</section>
''' + '{{> chef}}' + cta('Lernen Sie uns kennen.', ('kontakt.html', 'Kontakt aufnehmen'), ('jobs.html', 'Bei uns arbeiten')))

page('kontakt.html', {"title": "Kontakt · WARMHERZ Bielefeld (Demo)", "desc": "WARMHERZ (Demo) erreichen: Telefon, Notdienst, Rückruf anfordern, Foto-Check.", "key": "kontakt"},
'{{> kontakt}}' + f'''<section class="sec light">
  <div class="wrap">
    <div class="cards">
      <div class="card"><div class="big-n">Mo–Fr</div><h3>7 bis 17 Uhr</h3><p>Samstag 8 bis 12 Uhr. Im Winter Notdienst rund um die Uhr.</p></div>
      <div class="card"><div class="big-n">Werkstatt</div><h3>Am Kupferhammer 12</h3><p>33602 Bielefeld (fiktive Adresse). Parkplätze direkt vor dem Tor.</p></div>
      <a href="foto-check.html" class="card"><div class="big-n">Foto</div><h3>Foto-Check</h3><p>Schneller als jedes Telefonat: 3 bis 5 Fotos schicken, wir melden uns heute.</p><span class="more">Zum Foto-Check →</span></a>
    </div>
  </div>
</section>
''')

legal = lambda h, txt: f'<section class="sec" style="padding-top:110px"><div class="wrap legal"><div class="crumbs"><a href="index.html">Start</a><span>/</span>{h}</div><h1 style="font-size:clamp(44px,5vw,72px)">{h}</h1>{txt}</div></section>'
page('impressum.html', {"title": "Impressum · WARMHERZ (Demo)", "desc": "Impressum der Demo-Webseite WARMHERZ.", "key": ""},
legal('Impressum', '<p><b>Dies ist eine Demo-Webseite.</b> WARMHERZ ist eine erfundene Firma. Es gibt keinen echten Betrieb, keine echten Personen und keine echten Angebote.</p><h2>Verantwortlich für diese Demo</h2><p>PROJEKT EX (Agentur), vertreten durch die Engelstränen UG. Die vollständigen Pflichtangaben stehen im Impressum von PROJEKT EX.</p><h2>Hinweis</h2><p>Alle Fotos sind mit KI erzeugt. Förderangaben sind Beispielwerte ohne Gewähr.</p>'))
page('datenschutz.html', {"title": "Datenschutz · WARMHERZ (Demo)", "desc": "Datenschutzhinweise der Demo-Webseite WARMHERZ.", "key": ""},
legal('Datenschutz', '<p><b>Diese Demo sendet keine Daten.</b> Formulare, Foto-Check und Bewerbungs-Chat funktionieren nur in Ihrem Browser. Nichts wird gespeichert oder übertragen.</p><h2>Schriften und Skripte</h2><p>Alle Schriften und Skripte liegen auf dem eigenen Server. Es werden keine Google Fonts, keine Analyse-Tools und keine Cookies genutzt.</p><h2>Im echten Betrieb</h2><p>Für einen echten Betrieb erstellen wir eine vollständige Datenschutzerklärung, abgestimmt auf Formulare, Foto-Upload und die Werkakte-App.</p>'))
print('Seiten geschrieben:', sorted(os.listdir(P)))
