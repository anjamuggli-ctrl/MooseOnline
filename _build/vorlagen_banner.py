"""Erzeugt die Kopfbilder (Berge in Pastellfarben, im Stil der Bullet-Journal-Vorlagen) für die Word-Vorlagen der Aufträge.
Aufruf:  python3 _build/vorlagen_banner.py   →  _build/vorlagen-bilder/banner-<farbe>-<motiv>.png
"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

OUT = Path(__file__).parent / "vorlagen-bilder"
OUT.mkdir(exist_ok=True)

FARBEN = {  # Hintergrund, Berg hinten, Berg vorne, Akzent
    "bergsee":    ("#E3EDE8", "#A9C7BA", "#5F8C7A", "#3F6B5A"),
    "alpenrose":  ("#F5E1E5", "#DDB0BB", "#B56F80", "#9B4D5E"),
    "gletscher":  ("#E2E8F2", "#B2C1D6", "#6F87A3", "#4A6178"),
    "terrakotta": ("#F4E4D7", "#E0BE9F", "#C08453", "#A8682F"),
    "lavendel":   ("#E9E5F3", "#C4B8DD", "#8C78B3", "#6B5592"),
}
W, H = 530, 200


def berge(bg, hinten, vorne, akzent, motiv):
    s = [f'<rect width="{W}" height="{H}" fill="{bg}"/>',
         f'<circle cx="{W-92}" cy="58" r="22" fill="#F2C97E" opacity=".75"/>',
         f'<path d="M150 {H} L235 92 L275 128 L340 60 L410 120 L455 86 L{W} 140 L{W} {H} Z" fill="{hinten}"/>',
         f'<path d="M330 66 L340 60 L352 70 L345 74 Z M228 100 L235 92 L243 101 Z" fill="#fff" opacity=".75"/>']
    if motiv == "stadt":
        # kleine Stadtsilhouette vor den Bergen
        x, haeuser = 210, [(26, 70), (18, 46), (30, 92), (20, 58), (34, 110), (22, 64), (28, 84), (18, 50), (30, 74)]
        for b, h in haeuser:
            s.append(f'<rect x="{x}" y="{H-h}" width="{b}" height="{h}" rx="2" fill="{vorne}"/>')
            for yy in range(H - h + 10, H - 8, 14):
                s.append(f'<rect x="{x+5}" y="{yy}" width="4" height="5" fill="{bg}" opacity=".8"/>')
                if b > 22:
                    s.append(f'<rect x="{x+b-9}" y="{yy}" width="4" height="5" fill="{bg}" opacity=".8"/>')
            x += b + 4
        s.append(f'<path d="M{W-70} {H} v-58 M{W-82} {H-58} h24 M{W-70} {H-58} l-12 -14 M{W-70} {H-58} l12 -14" stroke="{akzent}" stroke-width="3" fill="none" stroke-linecap="round"/>')
        s.append(f'<circle cx="{W-70}" cy="{H-58}" r="4" fill="{akzent}"/>')
    elif motiv == "weg":
        s.append(f'<path d="M200 {H} L300 110 L345 140 L420 70 L490 130 L{W} 110 L{W} {H} Z" fill="{vorne}"/>')
        s.append(f'<path d="M260 {H} C 300 170, 380 175, 370 140 S 400 95, 420 72" stroke="#fff" stroke-width="3" fill="none" stroke-dasharray="6 7" stroke-linecap="round" opacity=".9"/>')
        s.append(f'<path d="M420 72 v-34" stroke="{akzent}" stroke-width="3" stroke-linecap="round"/><path d="M421 38 l22 7 l-22 7 Z" fill="#F2C97E" stroke="{akzent}" stroke-width="2" stroke-linejoin="round"/>')
    else:
        s.append(f'<path d="M200 {H} L300 110 L345 140 L420 70 L490 130 L{W} 110 L{W} {H} Z" fill="{vorne}"/>')
    # Tannen
    for tx, th in [(170, 34), (186, 26), (500, 30)]:
        s.append(f'<path d="M{tx} {H} l{-th*0.32} 0 l{th*0.32} {-th} l{th*0.32} {th} Z" fill="{akzent}"/>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(s)}</svg>'


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = await b.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
        for name, f in FARBEN.items():
            for motiv in ("stadt", "weg", "berge"):
                await pg.set_content(f'<html><body style="margin:0">{berge(*f, motiv)}</body></html>')
                await pg.locator("svg").screenshot(path=str(OUT / f"banner-{name}-{motiv}.png"))
        await b.close()

asyncio.run(main())
