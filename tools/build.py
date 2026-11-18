#!/usr/bin/env python3
"""WARMHERZ Seiten-Baukasten.
src/layout.html  = gemeinsamer Rahmen (Kopf, Menü, Fußzeile)
src/pages/*.html = Seiteninhalt, erste Zeile: <!--{"title": "...", "desc": "...", "key": "...", "preload": "assets/img/x.webp"}-->
src/parts/*.html = wiederverwendbare Abschnitte, im Seiteninhalt einbinden mit {{> name}}
Nutzung: python3 tools/build.py   -> schreibt site/<seite>.html
"""
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC, OUT = os.path.join(ROOT, 'src'), os.path.join(ROOT, 'site')
layout = open(os.path.join(SRC, 'layout.html')).read()

def include(text, depth=0):
    def rep(m):
        p = os.path.join(SRC, 'parts', m.group(1).strip() + '.html')
        if not os.path.exists(p): sys.exit(f'Teil fehlt: {m.group(1)}')
        return include(open(p).read(), depth + 1)
    return re.sub(r'\{\{>\s*([\w-]+)\s*\}\}', rep, text) if depth < 5 else text

built = []
for fn in sorted(os.listdir(os.path.join(SRC, 'pages'))):
    if not fn.endswith('.html'): continue
    raw = open(os.path.join(SRC, 'pages', fn)).read()
    m = re.match(r'\s*<!--(\{.*?\})-->\s*', raw, re.S)
    meta = json.loads(m.group(1)); body = include(raw[m.end():])
    page = layout.replace('{{title}}', meta['title']).replace('{{desc}}', meta['desc']).replace('{{key}}', meta.get('key', ''))
    pre = meta.get('preload')
    page = page.replace('{{preload}}', f'<link rel="preload" href="{pre}" as="image">\n' if pre else '')
    page = page.replace('{{body}}', body)
    key = meta.get('key')
    if key:  # aktiven Menüpunkt markieren
        page = page.replace(f'data-key="{key}"', f'data-key="{key}" aria-current="page"')
        if key in ('waermepumpe', 'heizungstausch', 'fussbodenheizung', 'bad', 'wartung'):
            page = page.replace('data-key="leistungen"', 'data-key="leistungen" data-active="1"')
    open(os.path.join(OUT, fn), 'w').write(page)
    built.append(fn)

# Prüfen: jeder interne Link zeigt auf eine vorhandene Seite und einen vorhandenen Anker
pages = {fn: open(os.path.join(OUT, fn)).read() for fn in built}
bad = []
for fn, html in pages.items():
    for href in re.findall(r'href="([^"]+)"', html):
        if href.startswith(('http', 'tel:', 'mailto:', 'data:', 'assets/')): continue
        f, _, anchor = href.partition('#'); f = f.split('?')[0]
        f = f or fn
        if f not in pages: bad.append(f'{fn}: {href} (Seite fehlt)'); continue
        if anchor and f'id="{anchor}"' not in pages[f]: bad.append(f'{fn}: {href} (Anker fehlt)')
print('gebaut:', ', '.join(built))
print('Link-Fehler:', len(bad)); [print('  ', b) for b in sorted(set(bad))]
