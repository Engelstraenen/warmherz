#!/usr/bin/env python3
"""WARMHERZ · „Ein Tag bei uns“ als ~21-s-Motion-Video (1920x1080, 30 fps).
Fotos mit Ken-Burns-Fahrt, Uhr zählt zur nächsten Uhrzeit, Sätze gleiten ein, Fortschrittsbalken,
Schlusskarte. Stil A Signal: Schwarz/Weiß/#FF5B1F, IBM Plex Sans.
Nutzung: python3 tools/make_tag_video.py  -> site/assets/video/ein-tag.mp4 (+ 720p, webm, poster)
"""
import math, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, 'site/assets/img')
OUT = os.path.join(ROOT, 'site/assets/video')
FONT = os.path.join(ROOT, 'tools/fonts')
os.makedirs(OUT, exist_ok=True)

W, H, FPS = 1920, 1080, 30
ACC = (255, 91, 31)
SCENE, FADE, END = 2.7, 0.5, 3.0

def F(name, size): return ImageFont.truetype(os.path.join(FONT, f'IBMPlexSans-{name}.ttf'), size)
f_clock, f_head, f_place, f_logo, f_small, f_end = F('Bold', 150), F('Bold', 78), F('SemiBold', 30), F('Bold', 34), F('Medium', 28), F('Bold', 120)

SCENES = [
    ('kaffee', '06:58', 'Werkstatt, Bielefeld', 'Der Tag fängt mit Kaffee an.', (1.12, 1.0), (0.5, 0.45)),
    ('transporter', '07:40', 'Unterwegs nach Schildesche', 'Lukas fährt. Lea lernt mit.', (1.0, 1.1), (0.55, 0.45)),
    ('baustelle', '08:15', 'Bei Familie Hartmann', 'Folie auf den Boden. Sauber.', (1.1, 1.0), (0.5, 0.5)),
    ('lea', '11:30', 'Technikraum im Keller', 'Lea verpresst ihr erstes Rohr.', (1.0, 1.1), (0.45, 0.4)),
    ('display', '14:30', 'Inbetriebnahme', 'Die Wärmepumpe läuft.', (1.1, 1.0), (0.5, 0.4)),
    ('feierabend', '16:30', 'Zurück in der Werkstatt', 'Feierabend um halb fünf.', (1.0, 1.1), (0.5, 0.45)),
    ('familie', '19:00', 'Familie Hartmann, abends', 'Abends ist es warm. Überall.', (1.12, 1.0), (0.5, 0.5)),
]
photos = {}
for n, *_ in SCENES:
    im = Image.open(os.path.join(IMG, n + '.webp')).convert('RGB')
    sc = max(W / im.width, H / im.height) * 1.0
    photos[n] = im.resize((round(im.width * sc * 1.13), round(im.height * sc * 1.13)), Image.LANCZOS)

ease = lambda t: 1 - (1 - max(0, min(1, t))) ** 3
ease_io = lambda t: (lambda x: 4 * x ** 3 if x < .5 else 1 - (-2 * x + 2) ** 3 / 2)(max(0, min(1, t)))

# Verlauf unten für Lesbarkeit
shade = Image.new('L', (W, H), 0)
d = ImageDraw.Draw(shade)
for y in range(H):
    a = 0
    if y > H * .38: a = int(225 * ((y - H * .38) / (H * .62)) ** 1.4)
    if y < 160: a = max(a, int(140 * (1 - y / 160)))
    d.line([(0, y), (W, y)], fill=a)
black = Image.new('RGB', (W, H), (0, 0, 0))

def photo_frame(i, t):
    n, _, _, _, (z0, z1), (cx, cy) = SCENES[i]
    src = photos[n]
    k = ease_io(t / (SCENE + FADE))
    z = z0 + (z1 - z0) * k
    cw, ch = W / z * (src.width / (W * 1.13)), H / z * (src.height / (H * 1.13))
    cw, ch = src.width / 1.13 / z, src.height / 1.13 / z
    x = (src.width - cw) * (cx + (k - .5) * .06); y = (src.height - ch) * cy
    return src.crop((int(x), int(y), int(x + cw), int(y + ch))).resize((W, H), Image.BILINEAR)

def tmin(s): h, m = s.split(':'); return int(h) * 60 + int(m)

def logo(dr, alpha=255):
    dr.rounded_rectangle([70, 64, 122, 116], 12, fill=ACC + (alpha,))
    # Herz
    dr.ellipse([81, 78, 97, 94], fill=(255, 255, 255, alpha)); dr.ellipse([95, 78, 111, 94], fill=(255, 255, 255, alpha))
    dr.polygon([(81, 88), (111, 88), (96, 106)], fill=(255, 255, 255, alpha))
    dr.text((138, 70), 'WARMHERZ', font=f_logo, fill=(255, 255, 255, alpha))

def render(frame):
    t = frame / FPS
    total_scenes = len(SCENES) * SCENE
    if t < total_scenes + FADE:
        i = min(int(t // SCENE), len(SCENES) - 1)
        lt = t - i * SCENE
        base = photo_frame(i, lt)
        if lt > SCENE - FADE and i + 1 < len(SCENES):   # Überblendung zur nächsten Szene
            nxt = photo_frame(i + 1, lt - SCENE)
            base = Image.blend(base, nxt, ease_io((lt - (SCENE - FADE)) / FADE))
        img = Image.composite(black, base, shade).convert('RGBA')
        ov = Image.new('RGBA', (W, H), (0, 0, 0, 0)); dr = ImageDraw.Draw(ov)
        logo(dr)
        tag = 'EIN TAG BEI UNS'
        tw = dr.textlength(tag, font=f_small)
        dr.text((W - 70 - tw, 76), tag, font=f_small, fill=(255, 255, 255, 220))
        # Uhr: zählt in 0,6 s zur Szenenzeit
        cur = tmin(SCENES[i][1]); prev = tmin(SCENES[i - 1][1]) if i else cur
        m = prev + (cur - prev) * ease(lt / .6)
        clock = f'{int(m // 60):02d}:{int(m % 60):02d}'
        dr.text((70, 640), clock, font=f_clock, fill=ACC + (255,))
        # Ort + Satz gleiten ein, gleiten am Ende raus
        a_in = ease((lt - .15) / .45); a_out = 1 - ease((lt - (SCENE - .35)) / .3) if i + 1 < len(SCENES) else 1
        a = a_in * a_out; dy = (1 - a_in) * 40 - (1 - a_out) * 20
        dr.text((74, 815 + dy), SCENES[i][2].upper(), font=f_place, fill=(255, 255, 255, int(200 * a)))
        dr.text((70, 855 + dy), SCENES[i][3], font=f_head, fill=(255, 255, 255, int(255 * a)))
        # Fortschritt
        seg = (W - 140 - 6 * 10) / 7
        for j in range(7):
            x0 = 70 + j * (seg + 10)
            dr.rounded_rectangle([x0, 1000, x0 + seg, 1006], 3, fill=(255, 255, 255, 70))
            fill = 1 if j < i else (min(1, lt / SCENE) if j == i else 0)
            if fill > 0: dr.rounded_rectangle([x0, 1000, x0 + seg * fill, 1006], 3, fill=ACC + (255,))
        img = Image.alpha_composite(img, ov)
        # Schlusskarte blendet ein
        et = t - total_scenes
        if et > -FADE:
            img = Image.blend(img, end_card(et + FADE), ease_io((et + FADE) / .7))
        return img.convert('RGB')
    return end_card(t - total_scenes + FADE).convert('RGB')

def end_card(et):
    c = Image.new('RGBA', (W, H), (14, 14, 14, 255)); dr = ImageDraw.Draw(c)
    logo(dr)
    a = ease((et - .3) / .6); dy = (1 - a) * 50
    l1, l2a, l2b = 'Wir machen', 'Bielefeld ', 'warm.'
    dr.text((140, 330 + dy), l1, font=f_end, fill=(255, 255, 255, int(255 * a)))
    dr.text((140, 470 + dy), l2a, font=f_end, fill=(255, 255, 255, int(255 * a)))
    dr.text((140 + dr.textlength(l2a, font=f_end), 470 + dy), l2b, font=f_end, fill=ACC + (int(255 * a),))
    b = ease((et - .8) / .5)
    dr.rounded_rectangle([140, 690, 520, 770], 14, fill=ACC + (int(255 * b),))
    dr.text((172, 710), 'Zuschuss berechnen', font=F('Bold', 32), fill=(255, 255, 255, int(255 * b)))
    dr.rounded_rectangle([544, 690, 860, 770], 14, outline=(255, 255, 255, int(200 * b)), width=3)
    dr.text((576, 710), 'Jobs bei uns', font=F('Bold', 32), fill=(255, 255, 255, int(255 * b)))
    dr.text((140, 980), 'Demo · WARMHERZ ist eine erfundene Firma', font=f_small, fill=(160, 160, 160, int(255 * b)))
    return c

def main():
    total = len(SCENES) * SCENE + FADE + END
    n = int(total * FPS)
    hi = os.path.join(OUT, 'ein-tag-1080.mp4')
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-preset', 'slow', '-crf', '19', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', hi], stdin=subprocess.PIPE)
    for f in range(n):
        p.stdin.write(render(f).tobytes())
        if f % 60 == 0: print(f'{f}/{n}', flush=True)
    p.stdin.close(); p.wait()
    render(int(2 * FPS)).save(os.path.join(OUT, 'ein-tag-poster.jpg'), quality=85)
    print('fertig', hi, n, 'Frames')

if __name__ == '__main__':
    main()
