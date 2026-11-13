"""Erzeugt aus den deutschen Seiten die Sprachversionen in /rm, /en, /it, /fr, /es.

Wird automatisch am Ende von build.py aufgerufen. Übersetzungen stehen in _build/i18n.json.
Fehlt eine Übersetzung, bleibt der deutsche Text stehen und das Skript meldet ihn.
"""
import json, re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = json.loads((Path(__file__).parent / "i18n.json").read_text())
TEXTE, JS, KAT, TITEL = D["texte"], D["js"], D["kategorien"], D["titel"]

SPRACHEN = [("de", "Deutsch"), ("rm", "Romontsch"), ("en", "English"),
            ("it", "Italiano"), ("fr", "Français"), ("es", "Español")]
NEUTRAL = {"Muggli", "Online", "›", "×", "✨", "Aa", "Hi!", "A5", "4 mm", "5 mm", "6 mm", "LinkedIn",
           "Bullet Journal", "Basic English", "Writing", "Dr. Anja Muggli", "Apps",
           "© 2026 MuggliOnline · Dr. Anja Muggli, Chur", "Agenda"}
ATTRS = ("alt", "title", "aria-label", "placeholder")
GLOBUS = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-5.7-3.8-9S9.5 5.7 12 3z"/></svg>'


def sprachmenue(lang, datei):
    links = []
    for code, name in SPRACHEN:
        if lang == "de":
            href = datei if code == "de" else f"{code}/{datei}"
        else:
            href = f"../{datei}" if code == "de" else f"../{code}/{datei}"
        cls = ' class="aktiv"' if code == lang else ""
        links.append(f'<li><a href="{href}" hreflang="{code}" lang="{code}"{cls}>{name}<small>{code.upper()}</small></a></li>')
    label = "Sprache wählen" if lang == "de" else TEXTE["Sprache wählen"][lang]
    return (f'<div class="lang"><button class="lang-btn" type="button" aria-label="{label}" '
            f'onclick="this.parentNode.classList.toggle(\'open\')">{GLOBUS}{lang.upper()}</button>'
            f'<ul class="lang-list">{"".join(links)}</ul></div>')


def hreflang(lang, datei):
    pre = "" if lang == "de" else "../"
    out = []
    for code, _ in SPRACHEN:
        href = f"{pre}{datei}" if code == "de" else f"{pre}{code}/{datei}"
        out.append(f'<link rel="alternate" hreflang="{code}" href="{href}">')
    return "\n".join(out) + "\n"


class Uebersetzer(HTMLParser):
    def __init__(self, lang, fehlend):
        super().__init__(convert_charrefs=False)
        self.lang, self.out, self.fehlend = lang, [], fehlend
        self.in_json = False

    def tr(self, text):
        if text in NEUTRAL or not text:
            return text
        if text in TEXTE:
            return TEXTE[text][self.lang]
        self.fehlend.add(text)
        return text

    def tag(self, raw):
        def attr(m):
            k, v = m.group(1), m.group(2)
            if k in ATTRS or k == "content":
                return f'{k}="{self.tr(v)}"'
            if k in ("href", "src") and not v.startswith(("http", "#", "mailto:", "data:", "../")) and ".html" not in v:
                return f'{k}="../{v}"'
            return m.group(0)
        raw = re.sub(r'\b(alt|title|aria-label|placeholder|content|href|src)="([^"]*)"', attr, raw)
        return raw

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.in_json = tag == "script" and a.get("id") == "vorlagen-daten"
        raw = self.get_starttag_text()
        if tag == "meta" and a.get("name") != "description":
            self.out.append(raw); return
        self.out.append(self.tag(raw))

    def handle_startendtag(self, tag, attrs):
        self.out.append(self.tag(self.get_starttag_text()))

    def handle_endtag(self, tag):
        self.in_json = False
        self.out.append(f"</{tag}>")

    def handle_data(self, d):
        tag = self.lasttag
        if self.in_json:
            daten = json.loads(d)
            for v in daten:
                v["titel"] = TITEL.get(v["titel"], {}).get(self.lang, v["titel"])
            self.out.append(json.dumps(daten, ensure_ascii=False)); return
        if tag in ("script", "style"):
            self.out.append(d); return
        s = d.strip()
        if not s:
            self.out.append(d); return
        vorne, hinten = d[: len(d) - len(d.lstrip())], d[len(d.rstrip()):]
        self.out.append(vorne + self.tr(s) + hinten)

    def handle_entityref(self, name): self.out.append(f"&{name};")
    def handle_charref(self, name): self.out.append(f"&#{name};")
    def handle_comment(self, data): self.out.append(f"<!--{data}-->")
    def handle_decl(self, decl): self.out.append(f"<!{decl}>")


def js_texte(lang):
    werte = {k: v[lang] for k, v in JS.items()}
    werte["kategorien"] = {k: v[lang] for k, v in KAT.items()}
    return werte


def fertig(html, lang, datei):
    html = html.replace(f"<!--LANG:{datei}-->", sprachmenue(lang, datei))
    html = html.replace("</head>", hreflang(lang, datei) + "</head>", 1)
    if lang == "de":
        html = html.replace("<!--I18N-->", "")
    else:
        html = html.replace('<html lang="de">', f'<html lang="{lang}">', 1)
        html = html.replace("<!--I18N-->", f"<script>window.SITE_BASE='../';window.I18N={json.dumps(js_texte(lang), ensure_ascii=False)};</script>")
    return html


seiten = sorted(p for p in ROOT.glob("*.html"))
fehlend = set()
for p in seiten:
    de = p.read_text()
    for code, _ in SPRACHEN[1:]:
        u = Uebersetzer(code, fehlend)
        u.feed(de); u.close()
        ordner = ROOT / code; ordner.mkdir(exist_ok=True)
        (ordner / p.name).write_text(fertig("".join(u.out), code, p.name))
    p.write_text(fertig(de, "de", p.name))

if fehlend:
    print("Ohne Übersetzung (bleibt deutsch):")
    for f in sorted(fehlend):
        print("  -", f)
print(f"Sprachversionen erstellt: {len(seiten)} Seiten × {len(SPRACHEN)-1} Sprachen.")
