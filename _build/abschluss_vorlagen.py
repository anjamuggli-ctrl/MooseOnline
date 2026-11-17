"""Journalvorlagen für Master- und Bachelorarbeiten (A5) im Stil der Bullet-Journal-Bibliothek.
Aufruf:  python3 _build/abschluss_vorlagen.py
Erzeugt vorlagen/vorlage-28 … 31 (PDF), Vorschaubilder in vorlagen/vorschau/ und PNG-Bilder für die Word-Datei in /tmp/abschluss/.
"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parent.parent
PNG_OUT = Path("/tmp/abschluss"); PNG_OUT.mkdir(exist_ok=True)

# Varianten wie in der Word-Vorlage: Farben für oben, Vorbesprechung, Kompetenzen, Bemerkungen
VARIANTEN = [
    dict(nr=28, datei="vorlage-28-masterarbeit-salbei", titel="Masterarbeit Salbei", art="Masterarbeit", linie=False,
         oben=("#e3ebdc", "#cdd9c4"), rechts=[("Situierte Kompetenzen", "#d8e3ee", "#bfcfdf", 2.7), ("Vorbesprechung mit", "#f1dfc8", "#e2c7a6", 1)],
         unten=("#e6e3f0", "#d0cbe3"), mitte_label=True),
    dict(nr=29, datei="vorlage-29-masterarbeit-sand", titel="Masterarbeit Sand", art="Masterarbeit", linie=True,
         oben=("#f0e6d9", "#e2d3bf"), rechts=[("Vorbesprechung mit", "#ead6d6", "#dbbcbc", 1), ("Situierte Kompetenzen", "#e0e9d9", "#c9d8bf", 3)],
         unten=("#f9f6ee", "#e6e0cf"), mitte_label=False),
    dict(nr=30, datei="vorlage-30-bachelorarbeit-minze", titel="Bachelorarbeit Minze", art="Bachelorarbeit", linie=True,
         oben=("#e1eee7", "#c9ddd1"), rechts=[("Vorbesprechung mit", "#f5e2d0", "#e8c9ab", 1), ("Situierte Kompetenzen", "#e3eaf4", "#cad6e6", 3)],
         unten=("#f2f7f2", "#d8e6d9"), mitte_label=False),
    dict(nr=31, datei="vorlage-31-bachelorarbeit-lavendel", titel="Bachelorarbeit Lavendel", art="Bachelorarbeit", linie=True,
         oben=("#e7e3f2", "#d2cbe5"), rechts=[("Vorbesprechung mit", "#f2dfe5", "#e3c3cd", 1), ("Situierte Kompetenzen", "#e1e7f3", "#c8d3e8", 3)],
         unten=("#f4f2f9", "#ddd8ec"), mitte_label=False),
]


def html(v, titel_text):
    rechts = "".join(f'<div class="box" style="background:{bg};border-color:{rd};flex:{fl}"><b>{lbl}</b></div>' for lbl, bg, rd, fl in v["rechts"])
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@page {{ size: 148mm 210mm; margin: 0 }}
* {{ box-sizing: border-box; margin: 0; padding: 0 }}
html, body {{ width: 148mm; height: 210mm; background: #fff }}
.seite {{ width: 148mm; height: 210mm; padding: 9mm 8mm 8mm; display: flex; flex-direction: column; gap: 3mm }}
h1 {{ font-family: Caladea, serif; font-weight: 400; font-size: 19pt; letter-spacing: .05em; text-transform: uppercase; color: #3a3f3c; text-align: center; line-height: 1 }}
.linie {{ width: 30mm; height: .35mm; background: #bdb7ad; margin: -0.5mm auto 1mm }}
.box {{ border: .3mm solid; border-radius: 2.2mm; padding: 2.4mm 2.6mm;
  background-image: radial-gradient(circle, rgba(70,70,70,.28) .28mm, transparent .32mm) !important; background-size: 5mm 5mm; background-position: 1.5mm 6mm }}
.box b {{ display: block; font-family: Inter, sans-serif; font-weight: 600; font-size: 6.2pt; letter-spacing: .07em; text-transform: uppercase; color: #3b3b3b; background: transparent }}
.reihe {{ display: flex; gap: 3mm; height: 21mm }} .reihe .box {{ flex: 1 }}
.haupt {{ display: flex; gap: 3mm; flex: 1 }}
.links {{ flex: 1.75; background-color: #fff; border-color: #cfcac2 }}
.rechts {{ flex: 1; display: flex; flex-direction: column; gap: 3mm }}
.unten {{ height: 31mm }}
</style></head><body><div class="seite">
<h1>{titel_text}</h1>{'<div class="linie"></div>' if v["linie"] else ''}
<div class="reihe"><div class="box" style="background-color:{v['oben'][0]};border-color:{v['oben'][1]}"><b>Studentin</b></div><div class="box" style="background-color:{v['oben'][0]};border-color:{v['oben'][1]}"><b>Themenbereich</b></div></div>
<div class="haupt"><div class="box links"><b{' style="text-align:center"' if v['mitte_label'] else ''}>Ausgangslage und mögliche<br>Fragestellung</b></div><div class="rechts">{rechts}</div></div>
<div class="box unten" style="background-color:{v['unten'][0]};border-color:{v['unten'][1]}"><b{' style="text-align:center"' if v['mitte_label'] else ''}>Bemerkungen</b></div>
</div></body></html>""".replace('style="background:', 'style="background-color:')


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = await b.new_page(viewport={"width": 560, "height": 794}, device_scale_factor=3)
        for v in VARIANTEN:
            seite = html(v, f'{v["art"]} Herbst 2026')
            await pg.set_content(seite); await pg.wait_for_timeout(300)
            await pg.pdf(path=str(ROOT / "vorlagen" / f'{v["datei"]}.pdf'), width="148mm", height="210mm", print_background=True)
            await pg.screenshot(path=str(PNG_OUT / f'{v["datei"]}.png'), clip={"x": 0, "y": 0, "width": 559.4, "height": 793.7})
        await b.close()
    # Vorschaubilder wie bei den übrigen Vorlagen (760 × 1078 und 300 × 425)
    from PIL import Image
    for v in VARIANTEN:
        im = Image.open(PNG_OUT / f'{v["datei"]}.png').convert("RGB")
        im.resize((760, 1078), Image.LANCZOS).save(ROOT / "vorlagen" / "vorschau" / f'{v["datei"]}.jpg', quality=85, optimize=True)
        im.resize((300, 425), Image.LANCZOS).save(ROOT / "vorlagen" / "vorschau" / f'{v["datei"]}-klein.jpg', quality=82, optimize=True)
    print("Vorlagen erstellt:", [v["datei"] for v in VARIANTEN])

asyncio.run(main())
