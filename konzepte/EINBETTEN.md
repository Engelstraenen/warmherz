# WARMHERZ + Werkakte · Links und Einbettungs-Code

## Links
- Website (Demo): https://engelstraenen.github.io/warmherz/
- App Werkakte (Demo, ohne Anmeldung): https://engelstraenen.github.io/werkakte/
- Code Website: https://github.com/Engelstraenen/warmherz
- Code App: https://github.com/Engelstraenen/werkakte

## Website einbetten (Browserfenster, passt sich der Breite an)
```html
<div style="position:relative;width:100%;max-width:1200px;aspect-ratio:16/10;margin:0 auto;border-radius:16px;overflow:hidden;box-shadow:0 30px 60px -20px rgba(0,0,0,.45)">
  <iframe src="https://engelstraenen.github.io/warmherz/" title="WARMHERZ – Demo-Website" loading="lazy"
    style="position:absolute;inset:0;width:100%;height:100%;border:0"></iframe>
</div>
```

## App einbetten (Handy-Rahmen)
```html
<div style="width:390px;max-width:100%;height:820px;margin:0 auto;padding:12px;border-radius:48px;background:#0E0E0E;box-shadow:0 30px 60px -20px rgba(0,0,0,.5)">
  <iframe src="https://engelstraenen.github.io/werkakte/" title="Werkakte – Demo-App" loading="lazy" allow="camera; web-share; clipboard-write"
    style="width:100%;height:100%;border:0;border-radius:36px;background:#0E0E0E"></iframe>
</div>
```

## Website und App nebeneinander (auf dem Handy untereinander)
```html
<div style="display:flex;flex-wrap:wrap;gap:32px;align-items:center;justify-content:center">
  <div style="flex:1 1 640px;max-width:900px;aspect-ratio:16/10;border-radius:16px;overflow:hidden;box-shadow:0 30px 60px -20px rgba(0,0,0,.45)">
    <iframe src="https://engelstraenen.github.io/warmherz/" title="WARMHERZ – Demo-Website" loading="lazy" style="width:100%;height:100%;border:0"></iframe>
  </div>
  <div style="flex:0 0 340px;height:720px;padding:10px;border-radius:44px;background:#0E0E0E;box-shadow:0 30px 60px -20px rgba(0,0,0,.5)">
    <iframe src="https://engelstraenen.github.io/werkakte/" title="Werkakte – Demo-App" loading="lazy" allow="camera; web-share; clipboard-write" style="width:100%;height:100%;border:0;border-radius:34px"></iframe>
  </div>
</div>
```

## Button „Demo im neuen Tab öffnen“ (unter den Rahmen setzen)
```html
<p style="text-align:center;margin-top:20px">
  <a href="https://engelstraenen.github.io/warmherz/" target="_blank" rel="noopener" style="display:inline-block;padding:14px 26px;border-radius:10px;background:#FF5B1F;color:#0E0E0E;font-weight:700;text-decoration:none">Website-Demo öffnen →</a>
  <a href="https://engelstraenen.github.io/werkakte/" target="_blank" rel="noopener" style="display:inline-block;margin-left:10px;padding:14px 26px;border-radius:10px;border:2px solid #FF5B1F;color:#FF5B1F;font-weight:700;text-decoration:none">App-Demo öffnen →</a>
</p>
```

Hinweis: Im iframe zeigt die Website ihre Handy- oder Desktop-Ansicht je nach Breite des Rahmens. Für den vollen „Wow“-Effekt (Scroll-Video) lieber zusätzlich einen Button „Demo im neuen Tab öffnen“ mit dem Link oben.
