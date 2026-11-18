#!/bin/zsh
# Baut die Seiten, committet und veröffentlicht site/ auf GitHub Pages (Branch gh-pages).
# Nutzung: tools/deploy.sh "Kurze Beschreibung"
set -e
cd "$(dirname "$0")/.."
python3 tools/pages_content.py >/dev/null
python3 tools/build.py
git add -A
git commit -qm "${1:-Website aktualisiert}" || true
git push -q origin main
git subtree split --prefix site -b gh-pages >/dev/null
git push -qf origin gh-pages
echo "Online in ca. 1 Minute: https://engelstraenen.github.io/warmherz/"
