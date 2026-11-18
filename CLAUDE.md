# PROJEKT-MASTERFILE – WARMHERZ
Gilt zusätzlich zur globalen Masterfile (~/.claude/CLAUDE.md).

## 1. Ziel und Endprodukt
- Demo-Webseite für einen **fiktiven** Heizungs-/Wärmepumpen-Familienbetrieb „WARMHERZ“ (Bielefeld, seit 1987, Inhaber „Heinz Brinkmann“, Monteur „Lukas“, Azubi „Lea“ – alles erfunden, als Demo gekennzeichnet).
- Zweck: Akquise-Referenz von PROJEKT EX für Heizungsbetriebe in NRW. Kampagne jetzt bis Ende Januar 2027 (Förderbonus sinkt am 1.2.2027).
- Zwei Zielgruppen: Hausbesitzer (Förderrechner, Vorab-Check per Foto) und Bewerber (Nachwuchs/Monteure = größtes Problem der Branche).
- Verbindung zur App **Werkakte** (`~/Documents/handwerker-app`): Anfragen und Bewerbungen landen als Akte in der App.
- Vorgänger/Referenz: WÄRMEWERK-Demo (https://engelstraenen.github.io/demo-getlayers-01/pex-pr-preise-leere-punkte-v1/referenzen/waermewerk/), wirkte zu technisch/kalt.

## 2. Qualitätsanspruch & Referenzen
- STIL A „SIGNAL“ (Eugen 18.11.2026, verbindlich): Schwarz #0E0E0E, Weiß, Papier #F2EFEA, EINE Akzentfarbe Signal-Orange #FF5B1F. Schrift: IBM Plex Sans 700 (Überschriften, wie Werkakte-App, Eugen 18.11.2026) + Inter Tight (Text). Bricolage war „zu verspielt“. NIE Kursivschrift, keine Serifen-Akzente, kein Braun/Creme/Petrol. Hervorhebung nur per Farbe.
- Gruppenfotos immer eng, in Interaktion, echt (nie in einer Reihe mit Abstand). Freier Platz = Foto erzählt es selbst (Armgeste/leerer Stuhl) + kräftiger orange Leuchtring mit Etikett, nie dünne gestrichelte Linie.
- Jeder Button muss zum passenden Ziel führen (Chef → Kontakt/Anruf, Job-Button → Bewerbungs-Chat mit vorgewählter Stelle).
- Fotos fotorealistisch über sjinn (Nano Banana 2, Unlimited), keine Schrift in Bildern.

## 3. Regeln für dieses Projekt
- Fiktive Marke, überall als Demo kennzeichnen. Keine echten Personen/Firmen.
- Förderzahlen GEPRÜFT gegen KfW 458 (gültig ab 21.07.2026, Prüfung 18.11.2026): Grund 30 %, Klimabonus 16 % (−4 Pkt. halbjährlich ab 1.2.2027, Selbstnutzer), Einkommensbonus 40/30/10 % (≤30/40/50 Tsd. €, mit Kind +10 Tsd.), Deckel 70 % bzw. 80 % bei geringem Einkommen, förderfähig 28.000 € (−750 € halbjährlich ab 1.2.2027). Kein Effizienzbonus mehr aufgeführt. Wertschöpfungsbonus Q1/2027 geplant, Details offen. Vor Livegang erneut prüfen.

## 4. Skills, Plugins, Agenten, MCP
| Name | wofür |
|---|---|
| claude-in-chrome | sjinn.ai Bilder |
| ffmpeg / headless Chrome | Konzept-Boards rendern |

## 5. Zugänge
- sjinn.ai: in Chrome eingeloggt (17.11.2026) ✅
- GitHub (Engelstraenen) ✅

## 5b. Seitenstruktur (Eugen 18.11.2026)
- Mehrseitig, nie wieder alles auf einer langen Seite: Landing (index) kurz und stark mit Teasern, jede Leistung/Karriere/Service als eigene Unterseite.
- Seiten: index, waermepumpe, heizungstausch, fussbodenheizung, bad, wartung, foerderung, ablauf, foto-check, jobs, ausbildung, fachkraefte, ueber-uns, kontakt, impressum, datenschutz.
- Lange Scroll-Storys nur auf Unterseiten (z. B. „Dein Tag“ auf ausbildung.html), nie auf der Landing.
- Foto-Check (3–5 Fotos + Beschreibung → Akte in Werkakte) = Produktidee für ALLE Handwerkskunden von PROJEKT EX.

## 6. Workflow & Freigabepunkte
1. Konzept-Boards (A Zwei Türen, B Ein Tag mit Lukas, C Hier fehlt noch jemand) → Eugen wählt/kombiniert
2. Fotos auf sjinn (4K, 16:9), Eugen sieht sie im Chat
3. Seite bauen (statisches HTML/CSS/JS in `site/`), Desktop + Handy prüfen
4. Veröffentlichen (GitHub Pages) nur nach OK

## 7. Befehle
- Seiten bauen: `python3 tools/pages_content.py && python3 tools/build.py` (src/layout.html + src/pages + src/parts → site/, prüft alle internen Links). NIE site/*.html direkt bearbeiten.
- Seite lokal: `cd site && python3 -m http.server 4360 --bind 127.0.0.1` → http://localhost:4360
- Vorschau-Modus für First Frames: `?shot=<section-id>` (zeigt nur diesen Abschnitt, Animationen eingefroren), dazu `&scene=<0-6>`, `&hover=<selector>`, `&hide=<selector>`, `&chat`. Rendern: `tools/shot.sh "?shot=foerderung" 1440 900 out.png`.
- First-Frame-Boards: `konzepte/firstframe.html#<0-12>` mit headless Chrome 2400×1260.
- Headless Chrome: Mindestbreite ~500 px → Handy-Prüfung im Browser-Panel (mobile preset), nicht headless.
- Konzept-Boards neu rendern: headless Chrome auf `konzepte/board.html#a|b|c` (2520×1560), dann `sips` → JPEG.

## 8. Offene Fragen
- Eugens Feedback zu: mehrseitiger Website, Scroll-Video, App-Farben (Design „Signal“, seit 19.11.2026 in main der handwerker-app gemergt, noch nicht gepusht).
- Veröffentlichung (GitHub Pages) nur nach OK.
- App „Team & Nachwuchs“ (Job teilen, Bewerber-Akte, Berichtsheft) noch nicht gebaut.
- Motion-Video vom Startbereich (GIF/MP4) noch offen.

## 9. Entschieden
- 18.11.2026 (Claude, Eugen schläft, Vollmacht): Scroll-Video = MiniMax H3 (768p, ohne Kamin); Wan 3.0 verworfen (480p, Kamin passt nicht zu „ohne Öl/Gas“). Rechner auf KfW 458 korrigiert, Werbezahl „bis zu 22.400 €“ (80 %).
- 18.11.2026: Diashow-Video (Fotos mit Kamerafahrt) abgelehnt → echtes Video über sjinn. Landing bekommt Scroll-Video „Von −10 °C auf 21 °C“ (Startbild-Wahl offen).
- 18.11.2026: Mehrseitige Website mit Baukasten, Karriere-Bereich (Jobs/Ausbildung/Fachkräfte), Foto-Check-Seite.
- 18.11.2026: Stil A „Signal“ gewählt. Startfoto h-luecke (Armgeste in die Lücke), Jobs-Einstieg h-stuhl (leerer Stuhl, Kaffee). Neuer Kontaktbereich mit Rückruf-Formular und Themenvorwahl.
- 18.11.2026: Konzept B + C kombiniert (Teamfoto mit Lücke + Ein Tag mit Lukas + Countdown). Dazu Leistungen, Wärmepumpe interaktiv, Förderrechner, Vorab-Check, Karriere mit Chat-Bewerbung, Chef/Nachfolge.
- 18.11.2026: Statische Seite in `site/` (HTML/CSS/JS, GSAP 3.12.5 + Schriften Fraunces/Manrope lokal, kein Google-Abruf). Fotos 4K von sjinn → WebP 2000–2400 px.
- 17.11.2026: Neue fiktive Marke WARMHERZ statt WÄRMEWERK. Werkakte läuft unter Engelstränen UG (später PROJEKT EX UG).
- 17.11.2026: Größtes Branchenproblem = Nachwuchs/Mitarbeiter → Seite und App drehen sich um Recruiting + Förderrechner.

## 10. Ablage
- Projekt: `Dropbox/CLAUDE/Projekte/WARMHERZ/` (konzepte/, site/, brand/, tools/, verlauf/)
