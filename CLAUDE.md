# PROJEKT-MASTERFILE – WARMHERZ
Gilt zusätzlich zur globalen Masterfile (~/.claude/CLAUDE.md).

## 1. Ziel und Endprodukt
- Demo-Webseite für einen **fiktiven** Heizungs-/Wärmepumpen-Familienbetrieb „WARMHERZ“ (Bielefeld, seit 1987, Inhaber „Heinz Brinkmann“, Monteur „Lukas“, Azubi „Lea“ – alles erfunden, als Demo gekennzeichnet).
- Zweck: Akquise-Referenz von PROJEKT EX für Heizungsbetriebe in NRW. Kampagne jetzt bis Ende Januar 2027 (Förderbonus sinkt am 1.2.2027).
- Zwei Zielgruppen: Hausbesitzer (Förderrechner, Vorab-Check per Foto) und Bewerber (Nachwuchs/Monteure = größtes Problem der Branche).
- Verbindung zur App **Werkakte** (`~/Documents/handwerker-app`): Anfragen und Bewerbungen landen als Akte in der App.
- Vorgänger/Referenz: WÄRMEWERK-Demo (https://engelstraenen.github.io/demo-getlayers-01/pex-pr-preise-leere-punkte-v1/referenzen/waermewerk/), wirkte zu technisch/kalt.

## 2. Qualitätsanspruch & Referenzen
- Herzlich statt technisch: warme Farben (Creme #F6EFE6, Glut #D9622B, Kupfer #B87333, Petrol #2F6F6A für Bewerber-Seite, Tinte #2B1D14), Serif-Headlines, echte Gesichter.
- Fotos fotorealistisch über sjinn (Nano Banana 2, Unlimited), keine Schrift in Bildern.

## 3. Regeln für dieses Projekt
- Fiktive Marke, überall als Demo kennzeichnen. Keine echten Personen/Firmen.
- Förderzahlen (16 % → 12 % ab 1.2.2027, max. förderfähige Kosten) vor Livegang gegen offizielle BEG-EM-Richtlinie (BAFA/KfW) prüfen.

## 4. Skills, Plugins, Agenten, MCP
| Name | wofür |
|---|---|
| claude-in-chrome | sjinn.ai Bilder |
| ffmpeg / headless Chrome | Konzept-Boards rendern |

## 5. Zugänge
- sjinn.ai: in Chrome eingeloggt (17.11.2026) ✅
- GitHub (Engelstraenen) ✅

## 6. Workflow & Freigabepunkte
1. Konzept-Boards (A Zwei Türen, B Ein Tag mit Lukas, C Hier fehlt noch jemand) → Eugen wählt/kombiniert
2. Fotos auf sjinn (4K, 16:9), Eugen sieht sie im Chat
3. Seite bauen (statisches HTML/CSS/JS in `site/`), Desktop + Handy prüfen
4. Veröffentlichen (GitHub Pages) nur nach OK

## 7. Befehle
- Konzept-Boards neu rendern: headless Chrome auf `konzepte/board.html#a|b|c` (2520×1560), dann `sips` → JPEG.

## 8. Offene Fragen
- Welches Konzept (oder Kombination)?

## 9. Entschieden
- 17.11.2026: Neue fiktive Marke WARMHERZ statt WÄRMEWERK. Werkakte läuft unter Engelstränen UG (später PROJEKT EX UG).
- 17.11.2026: Größtes Branchenproblem = Nachwuchs/Mitarbeiter → Seite und App drehen sich um Recruiting + Förderrechner.

## 10. Ablage
- Projekt: `Dropbox/CLAUDE/Projekte/WARMHERZ/` (konzepte/, site/, brand/, tools/, verlauf/)
