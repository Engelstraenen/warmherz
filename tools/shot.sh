#!/bin/zsh
# Nutzung: tools/shot.sh "<query>" <breite> <hoehe> <ausgabe.png>
C="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$C" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --window-size=$2,$3 --virtual-time-budget=${VT:-6000} --screenshot="$4" "http://127.0.0.1:4360/$1" >/dev/null 2>&1
