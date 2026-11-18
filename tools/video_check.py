"""Prüft ein Final-Video vor der Lieferung: echte Schärfe pro Sekunde (Kanten-Varianz)
gegen das Startbild in Zielgröße und gegen das Startbild über 1920/1280 heruntergerechnet.
Aufruf: python3 tools/video_check.py video.mp4 startbild.jpg"""
import subprocess, sys, tempfile, glob, os
from PIL import Image, ImageFilter
import numpy as np
v, s = sys.argv[1], sys.argv[2]
sh = lambda im: np.asarray(im.convert('L').filter(ImageFilter.FIND_EDGES), dtype=float).var()
d = tempfile.mkdtemp()
subprocess.run(['ffmpeg', '-v', 'error', '-i', v, '-vf', 'fps=1', f'{d}/t_%02d.png'], check=True)
fr = sorted(glob.glob(f'{d}/t_*.png')); size = Image.open(fr[0]).size
st = Image.open(s)
ref = {'Startbild': sh(st.resize(size, Image.LANCZOS))}
for w in (1920, 1280):
    ref[f'wie {w}p'] = sh(st.resize((w, int(w * 9 / 16)), Image.LANCZOS).resize(size, Image.BICUBIC))
print('Datei', size, '| Vergleich:', {k: round(x) for k, x in ref.items()})
for f in fr: print(os.path.basename(f), round(sh(Image.open(f))))
