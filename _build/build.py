"""Baut alle Seiten von MuggliOnline.

Aufruf (im Repository-Ordner):  python3 _build/build.py
Ordner mit Unterstrich (_build) werden von GitHub Pages nicht veröffentlicht.
Kopfbalken, Fusszeile und Stylesheet sind für alle Seiten gleich und werden hier zentral gepflegt.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
B = Path(__file__).resolve().parent

LOGO = (B / "logo_inline.svg").read_text()
CSS = (B / "base.css").read_text() + (B / "extra.css").read_text()
(ROOT / "style.css").write_text(CSS)
import hashlib
def version(text): return hashlib.md5(text.encode()).hexdigest()[:8]
CSS_V = version(CSS)
JS_V = {n: version((ROOT / n).read_text()) for n in ("bullet-journal.js", "vorlagen.js")}

MENU = [
    ("didaktik.html", "Pädagogik"),
    ("english.html", "Lehrpersonen"),
    ("lernende.html", "Lernende"),
    ("werkstatt.html", "App-Werkstatt"),
    ("vision.html", "Vision"),
    ("ueber-anja.html", "Über Anja"),
]

def banner_ridge(h):
    """Bergsilhouette unten im grünen Banner: Grün, Dunkelblau, Sandfront und dunkelblaue Tannen."""
    tannen = [(x, round(113 - 22 * k, 1), k) for x, k in [(60, 1.1), (92, .85), (380, .7), (870, .75), (1090, 1.15), (1126, .85)]]
    baeume = "".join(
        f'<g transform="translate({x} {y}) scale({k})"><polygon points="0,-34 -10,-14 10,-14"/><polygon points="0,-24 -14,0 14,0"/><polygon points="0,-12 -18,14 18,14"/><rect x="-2" y="14" width="4" height="8"/></g>'
        for x, y, k in tannen)
    return (f'<svg class="ridge" viewBox="0 0 1200 120" preserveAspectRatio="none" aria-hidden="true" style="height:{h}px">'
            '<path d="M0,120 L0,88 L120,52 L190,72 L300,22 L390,64 L470,46 L560,80 L660,38 L740,60 L840,16 L930,58 L1010,40 L1100,70 L1200,46 L1200,120 Z" fill="#4c6b57"/>'
            '<path d="M0,120 L0,98 L90,80 L200,96 L330,66 L450,92 L560,74 L700,98 L820,68 L960,94 L1080,76 L1200,90 L1200,120 Z" fill="#5f8069"/>'
            '<path d="M0,120 L0,104 L160,94 L300,107 L460,97 L640,109 L800,97 L980,107 L1200,99 L1200,120 Z" fill="#d6e0d3"/></svg>'
            f'<svg class="ridge" viewBox="0 0 1200 120" preserveAspectRatio="xMidYMax meet" aria-hidden="true" style="height:{h}px"><g fill="#2a3a4b">{baeume}</g></svg>')

RIDGE = banner_ridge(150)


def silhouette(v):
    """Sanfte Berg- und Baumsilhouette im Hintergrund der Vision-Balken (drei Varianten)."""
    berge = [
        "M0,120 L0,78 L90,52 L170,70 L260,30 L340,62 L420,48 L520,80 L600,40 L700,70 L800,34 L900,66 L1000,50 L1100,74 L1200,46 L1200,120 Z",
        "M0,120 L0,64 L110,40 L200,66 L300,44 L380,72 L480,26 L580,60 L660,50 L760,78 L860,38 L960,64 L1080,30 L1200,58 L1200,120 Z",
        "M0,120 L0,70 L80,58 L190,32 L290,64 L400,46 L470,70 L560,36 L680,68 L780,44 L880,72 L990,28 L1090,60 L1200,40 L1200,120 Z",
    ][v]
    vorne = [
        "M0,120 L0,96 L150,80 L300,98 L450,84 L620,100 L780,86 L950,102 L1100,88 L1200,96 L1200,120 Z",
        "M0,120 L0,92 L180,100 L330,84 L500,98 L640,88 L820,102 L990,84 L1200,98 L1200,120 Z",
        "M0,120 L0,100 L140,86 L320,100 L470,88 L650,102 L800,84 L980,98 L1200,90 L1200,120 Z",
    ][v]
    tannen = [[(60, 92, 1.0), (88, 96, .75), (1030, 94, .9), (1060, 98, .7), (1120, 92, 1.1)],
              [(40, 96, .8), (980, 92, 1.0), (1010, 98, .7), (1150, 94, .95)],
              [(70, 98, .9), (100, 94, 1.1), (130, 99, .7), (1100, 96, .85)]][v]
    baeume = "".join(
        f'<g transform="translate({x} {y}) scale({k})"><polygon points="0,-34 -10,-14 10,-14"/><polygon points="0,-24 -14,0 14,0"/><polygon points="0,-12 -18,14 18,14"/><rect x="-2" y="14" width="4" height="8"/></g>'
        for x, y, k in tannen)
    return (f'<svg class="vsil" viewBox="0 0 1200 120" preserveAspectRatio="none" aria-hidden="true">'
            f'<path d="{berge}" fill="#c9d8cb"/><path d="{vorne}" fill="#9fb8a5"/></svg>'
            f'<svg class="vtrees" viewBox="0 0 1200 120" preserveAspectRatio="xMidYMax slice" aria-hidden="true"><g fill="#34475c">{baeume}</g></svg>')



def page(filename, title, body, active=None, description="", extra_head=""):
    act = ' class="active"'
    items = "\n".join(
        f'      <li><a href="{href}"{act if href == active else ""}>{label}</a></li>'
        for href, label in MENU
    )
    kontakt_cls = "cta active" if active == "kontakt.html" else "cta"
    html = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" href="logo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Fraunces:ital,wght@0,500;0,600;1,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css?v={CSS_V}">
{extra_head}</head>
<body>

<header>
  <div class="wrap nav">
    <a class="brand" href="index.html" aria-label="MuggliOnline Startseite">
      {LOGO}
      <span class="name">Muggli<span>Online</span></span>
    </a>
    <ul class="menu" id="menu">
{items}
      <li><a class="{kontakt_cls}" href="kontakt.html">Kontakt</a></li>
    </ul>
    <!--LANG:{filename}-->
    <button class="burger" aria-label="Menü öffnen" onclick="document.getElementById('menu').classList.toggle('open')"><span></span><span></span><span></span></button>
  </div>
</header>

{body}

<footer>
  <div class="wrap">
    <span>© 2026 MuggliOnline · Anja Muggli, Chur</span>
    <nav><a href="mailto:anja@mugglionline.ch">anja@mugglionline.ch</a><a href="kontakt.html">Kontakt</a><a href="impressum.html">Impressum</a><a href="datenschutz.html">Datenschutz</a></nav>
  </div>
</footer>
<script>document.addEventListener('click',function(e){{document.querySelectorAll('.lang.open').forEach(function(l){{if(!l.contains(e.target))l.classList.remove('open')}})}});</script>
</body>
</html>
"""
    (ROOT / filename).write_text(html)


def hero(crumb, kicker, h1, lead):
    return f"""  <section class="page-hero">
    <div class="inner">
      <div class="crumbs"><a href="index.html">Startseite</a> › {crumb}</div>
{f'      <div class="kicker">{kicker}</div>\n' if kicker else ""}      <h1>{h1}</h1>
      <p class="lead">{lead}</p>
    </div>
    {RIDGE}
  </section>"""


def plan(title, text, bullets=(), badge="In Vorbereitung"):
    ul = ("<ul>" + "".join(f"<li>{b}</li>" for b in bullets) + "</ul>") if bullets else ""
    return f"""      <div class="plan"><span class="badge">{badge}</span><h3>{title}</h3><p>{text}</p>{ul}</div>"""


def einleitung(titel, absaetze, v=1):
    """Cremefarbener Einleitungsbalken mit Bergen und Tannen (wie auf der Vision-Seite)."""
    return (f'    <article class="vrow einleitung-bar">{silhouette(v)}<div class="vhead"><h2>{titel}</h2></div>'
            f'<div class="vtext">{"".join(f"<p>{p}</p>" for p in absaetze)}</div></article>')


def area(filename, crumb, kicker, h1, lead, intro, plans, note="", cols="grid3", bar=None):
    oben = einleitung(*bar) if bar else f"""    <h2>Was hier entsteht</h2>
    <p class="intro">{intro}</p>"""
    body = f"""<main class="wrap">
{hero(crumb, kicker, h1, lead)}
  <section class="section">
{oben}
    <div class="{cols}">
{chr(10).join(plans)}
    </div>
  </section>
{note}
</main>"""
    page(filename, f"{h1} – MuggliOnline", body, active=ACTIVE.get(filename), description=lead)


ACTIVE = {
    "english.html": "english.html",
    "didaktik.html": "didaktik.html", "lernende.html": "lernende.html",
    "werkstatt.html": "werkstatt.html", "bullet-journal.html": "werkstatt.html",
    "vision.html": "vision.html", "ueber-anja.html": "ueber-anja.html", "kontakt.html": "kontakt.html",
}

# ---------------- Startseite ----------------
main = (B / "index_main.html").read_text()
import re as _re
main = _re.sub(r'<svg class="ridge".*?</svg>', lambda m: banner_ridge(180), main, count=1, flags=_re.S)
for old, new in {
    'href="#english-lernende"': 'href="english.html"',
    'href="#english-lehrpersonen"': 'href="english.html"',
    'href="#didaktik"': 'href="didaktik.html"',
    'href="#lernende"': 'href="lernende.html"',
    'href="#werkstatt"': 'href="werkstatt.html"',
    'href="#ueber-anja"': 'href="ueber-anja.html"',
    'href="#vision"': 'href="vision.html"',
}.items():
    main = main.replace(old, new)
page("index.html", "MuggliOnline – Materialien und Werkzeuge für gutes Lernen", main,
     description="Unterrichtsmaterialien, Online-Übungen und didaktische Hilfsmittel für Lernende und Lehrpersonen.")

# ---------------- Englisch: Übersicht und vier Bereiche ----------------
EN_BEREICHE = [
    ("english-basic.html", "Basic English", "Grundlagen des Englischen in kleinen Schritten.",
     ["Grammatik", "Writing", "Wortschatz"],
     [("Grammatik", "Übungen zu den wichtigsten Grammatikthemen, mit Sofortkontrolle."),
      ("Writing", "Schreibaufträge mit Checklisten."),
      ("Wortschatz", "Vokabeltrainer für den Grundwortschatz.")]),
    ("english-maschinenbau.html", "Berufsschule: Maschinenbau", "Fachenglisch rund um Maschinen, Werkstoffe und Fertigung.",
     ["Fachwortschatz", "Leseverständnis", "Prüfungsvorbereitung"], None),
    ("english-informatik.html", "Berufsschule: Informatik", "Fachenglisch für IT, Netzwerke und Software.",
     ["Unterrichtsideen", "Materialien", "Bewertungsraster"], "nur-lp"),
    ("english-mediamatik.html", "Berufsschule: Mediamatik", "Fachenglisch rund um Medien, Design und Kommunikation.",
     ["Fachwortschatz", "Leseverständnis", "Prüfungsvorbereitung"], None),
]
LERNENDE_BERUF = [("Fachwortschatz", "Vokabeltrainer mit den wichtigsten Fachbegriffen."),
                  ("Leseverständnis", "Texte aus dem Berufsalltag mit Verständnisfragen."),
                  ("Probeprüfungen", "Prüfungen zum Üben, mit Lösungen.")]
LEHRPERSONEN = [("Unterrichtsmaterialien", "Arbeitsblätter, Texte und Aufgaben für den Unterricht."),
                ("Bewertungsraster", "Raster und Kriterien für Writing und Speaking."),
                ("Prüfungen", "Prüfungen und Probeprüfungen mit Lösungen und Bewertungshinweisen.")]
for datei, *_ in EN_BEREICHE:
    ACTIVE[datei] = "english.html"

AUFGABENFORMEN = [
    ("Einzel-Projekte", [
        "Selbstständig ein Thema recherchieren und aufbereiten",
        "Klare Aufträge mit Zwischenschritten und Checklisten",
        "Bewertungsraster für Produkt und Prozess"],
     '<circle cx="110" cy="34" r="13"/><path d="M84 92 c0 -22 12 -34 26 -34 s26 12 26 34"/><rect x="138" y="40" width="40" height="52" rx="4" fill="#e7ede6"/><path d="M146 54 h24 M146 64 h24 M146 74 h16"/><path d="M40 100 h140"/>'),
    ("Gruppen-Arbeiten", [
        "Zusammenarbeit mit verteilten Rollen",
        "Projektaufträge mit Zeitplan und Meilensteinen",
        "Raster für die Bewertung von Gruppe und Einzelnen"],
     '<circle cx="70" cy="40" r="11"/><path d="M48 92 c0 -18 10 -28 22 -28 s22 10 22 28"/><circle cx="150" cy="40" r="11"/><path d="M128 92 c0 -18 10 -28 22 -28 s22 10 22 28"/><circle cx="110" cy="32" r="13" fill="#e7ede6"/><path d="M84 96 c0 -22 12 -34 26 -34 s26 12 26 34" fill="#e7ede6"/>'),
    ("Präsentationen", [
        "Redemittel und Vorlagen für Präsentationen",
        "Tipps zu Aufbau, Körpersprache und Visualisierung",
        "Feedback- und Bewertungsraster"],
     '<rect x="70" y="14" width="96" height="62" rx="4" fill="#e7ede6"/><path d="M118 76 v20 M100 102 l18 -6 18 6"/><path d="M84 62 v-12 M100 62 v-22 M116 62 v-16 M132 62 v-28 M148 62 v-20" stroke-width="5"/><circle cx="40" cy="44" r="10"/><path d="M22 100 c0 -20 8 -32 18 -32 s18 10 18 26 M50 60 l24 -16"/>'),
    ("Grammatik", [
        "Erklärungen mit Beispielen",
        "Übungen von einfach bis anspruchsvoll",
        "Lösungen zur Selbstkontrolle"],
     '<rect x="42" y="52" width="40" height="40" rx="5" fill="#e7ede6"/><rect x="90" y="52" width="40" height="40" rx="5"/><rect x="138" y="52" width="40" height="40" rx="5" fill="#e7ede6"/><rect x="66" y="10" width="40" height="40" rx="5"/><rect x="114" y="10" width="40" height="40" rx="5" fill="#e7ede6"/>'
     '<text x="62" y="80" text-anchor="middle" font-family="Fraunces, serif" font-size="22" fill="#3f5d4a" stroke="none">A</text><text x="110" y="80" text-anchor="middle" font-family="Fraunces, serif" font-size="22" fill="#3f5d4a" stroke="none">B</text><text x="158" y="80" text-anchor="middle" font-family="Fraunces, serif" font-size="22" fill="#3f5d4a" stroke="none">C</text><text x="86" y="38" text-anchor="middle" font-family="Fraunces, serif" font-size="20" fill="#3f5d4a" stroke="none">is</text><text x="134" y="38" text-anchor="middle" font-family="Fraunces, serif" font-size="20" fill="#3f5d4a" stroke="none">are</text>'),
    ("Schreiben", [
        "Schreibaufträge für verschiedene Textsorten wie E-Mail, Bericht oder Anleitung",
        "Checklisten und Beispieltexte",
        "Bewertungsraster für das Schreiben"],
     '<rect x="50" y="14" width="86" height="96" rx="4" fill="#e7ede6"/><path d="M62 34 h62 M62 48 h62 M62 62 h62 M62 76 h40"/><path d="M178 18 l12 12 -46 46 -16 4 4 -16 z" fill="#fff"/><path d="M168 28 l12 12"/>'),
    ("Posters", [
        "Aufträge für informative Poster und Infografiken",
        "Gestaltungstipps und Vorlagen",
        "Raster für Inhalt und Gestaltung"],
     '<rect x="60" y="14" width="100" height="94" rx="3" fill="#fff"/><circle cx="70" cy="22" r="3" fill="#3f5d4a"/><circle cx="150" cy="22" r="3" fill="#3f5d4a"/><rect x="72" y="32" width="76" height="34" rx="2" fill="#e7ede6"/><path d="M80 60 l14 -14 10 10 8 -6 14 10"/><circle cx="132" cy="42" r="4"/><path d="M72 78 h76 M72 88 h56 M72 98 h66"/>'),
    ("Digitalität", [
        "Projekte mit digitalen Werkzeugen und KI",
        "Reflektierter Umgang mit Medien und Daten",
        "Tutorials, Videos und Online-Aufgaben"],
     '<rect x="56" y="20" width="108" height="66" rx="5" fill="#e7ede6"/><path d="M42 98 h136 l-10 -12 h-116 z"/><circle cx="88" cy="52" r="5"/><circle cx="112" cy="38" r="5"/><circle cx="134" cy="58" r="5"/><circle cx="108" cy="68" r="5"/><path d="M92 50 l16 -9 M116 41 l15 14 M130 61 l-17 6 M104 66 l-12 -11"/><path d="M178 20 l3 8 8 3 -8 3 -3 8 -3 -8 -8 -3 8 -3 z" fill="#3f5d4a"/>'),
]
LINE2 = 'fill="none" stroke="#3f5d4a" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"'

# ---------------- Lehrpersonen: Aufträge ----------------
# Jeder Auftrag erscheint als Kachel auf allen Seiten der Aufgabenformen, zu denen er passt.
# Der Inhalt der Auftragsseite liegt in _build/<ordner>/*.html (Übersetzungen später in Unterordnern en/, it/, rm/).
SMART_CITY_ART = f'''<g {LINE2}><path d="M20 106 h180"/><rect x="34" y="56" width="26" height="50" rx="2"/><rect x="66" y="36" width="30" height="70" rx="2" fill="#e7ede6"/>
<rect x="102" y="64" width="22" height="42" rx="2"/><rect x="130" y="28" width="28" height="78" rx="2" fill="#e7ede6"/><rect x="164" y="60" width="24" height="46" rx="2"/>
<path d="M74 48 h6 M84 48 h4 M74 60 h6 M84 60 h4 M74 72 h6 M138 40 h5 M147 40 h5 M138 52 h5 M147 52 h5 M138 64 h5 M147 64 h5"/>
<path d="M73 20 a12 12 0 0 1 16 0 M68 14 a19 19 0 0 1 26 0" /><circle cx="81" cy="27" r="1.6" fill="#3f5d4a"/>
<circle cx="47" cy="44" r="4"/><circle cx="113" cy="52" r="4"/><circle cx="176" cy="48" r="4"/><path d="M51 42 l58 8 M117 51 l55 -2" stroke-dasharray="3 4"/></g>
<g fill="none" stroke="#a8682f" stroke-width="2.4" stroke-linecap="round"><circle cx="190" cy="20" r="7"/><path d="M190 6 v4 M190 30 v4 M176 20 h4 M200 20 h4"/></g>'''
TRAUMJOB_ART = '''<rect x="0" y="0" width="220" height="120" rx="10" fill="#efe9f6"/><circle cx="178" cy="30" r="11" fill="#f2c97e"/>
<path d="M0 120 L58 52 L86 78 L128 30 L168 74 L196 56 L220 70 L220 120 Z" fill="#c4b8dd"/>
<path d="M120 38 L128 30 L137 40 L130 44 Z M52 59 L58 52 L64 60 Z" fill="#fff" opacity=".85"/>
<path d="M0 120 L40 88 L78 104 L128 62 L176 98 L220 86 L220 120 Z" fill="#8c78b3"/>
<path d="M60 120 C 80 108, 120 112, 112 96 S 118 74, 128 62" stroke="#fff" stroke-width="2.4" fill="none" stroke-dasharray="4 5" stroke-linecap="round"/>
<path d="M128 62 v-22" stroke="#4b3a6e" stroke-width="2.4" stroke-linecap="round"/><path d="M129 40 l15 5 l-15 5 Z" fill="#f2c97e" stroke="#4b3a6e" stroke-width="1.6" stroke-linejoin="round"/>
<g stroke="#a8682f" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M34 120 v-38"/><path d="M34 86 h20 l6 5 l-6 5 h-20 Z M34 98 h-18 l-6 5 l6 5 h18 Z" fill="#f4e4d7"/></g>
<g fill="#3f6b5a"><path d="M176 120 l-7 0 l7 -20 l7 20 Z"/><path d="M190 120 l-6 0 l6 -15 l6 15 Z"/></g>'''
AUFTRAEGE = [
    dict(datei="auftrag-smart-city.html", ordner="auftrag-smart-city", titel="Smart City Projekt",
         kategorien=["Gruppen-Arbeiten", "Präsentationen", "Digitalität"], art=SMART_CITY_ART, bild="img/smart-city/stadt-nacht-vernetzt.jpg",
         badge="Gruppen-Arbeit · Real bis Berufsschule",
         text="Gruppen planen als Firma eine «Smart City» und bewerben sich mit einer Offerte beim «Stadtrat», gespielt von der Klasse.",
         punkte=["Fächer: Englisch, Deutsch, RZG/Geografie, Medien und Informatik, WAH/Wirtschaft, ABU",
                 "Kompetenzen: recherchieren, planen, budgetieren, argumentieren, präsentieren",
                 "Gruppenarbeit mit Rollen und Gruppenvertrag",
                 "Projektmanagement nach Stufe: von der Vorlage bis HERMES",
                 "Digitalität: Arbeitsjournal, digitale Werkzeuge, Optionen mit und ohne KI",
                 "BNE: erneuerbare Energie, Mobilität, lebenswerte Stadt",
                 "Lernende bewerten als Stadtrat mit und schätzen sich selbst ein"],
         lead="Ein Gruppenprojekt mit Recherche, Projektmanagement, digitalen Medien und einer Offerte-Präsentation vor dem Stadtrat.",
         einleitung=["In kleinen Gruppen gründen die Lernenden eine Firma und bewerben sich mit einer Offerte um den Auftrag, eine Stadt zur «Smart City» zu machen. Die Stadt ist frei wählbar, zum Beispiel die eigene Gemeinde. Sie recherchieren, was eine Smart City ausmacht, entwickeln eigene Ideen mit Bezug zu nachhaltiger Entwicklung, planen Phasen, Zeitplan und Budget und präsentieren ihre Offerte. Die übrige Klasse spielt den Stadtrat, macht sich Notizen und vergibt am Schluss den Auftrag. Es gibt eine realitätsnahe Variante und eine Fantasy-Variante, in der auch fliegende Taxis erlaubt sind.",
                     "Unten findest du zuerst die Hauptschritte der Lernenden und die wichtigsten Angaben pro Stufe. Danach folgt der Ablauf für Lehrpersonen in sieben Schritten, jeweils mit Optionen mit und ohne KI, Hinweisen aus der Forschung und Vorlagen zum Herunterladen."]),
    dict(datei="auftrag-traumjob.html", ordner="auftrag-traumjob", titel="Mein Traumjob",
         kategorien=["Einzel-Projekte", "Präsentationen", "Posters", "Schreiben", "Digitalität"], art=TRAUMJOB_ART, bild="img/traumjob/velowerkstatt.jpg",
         badge="Einzel-Projekt · Real bis Berufsschule",
         text="Lernende erkunden ihren Traumberuf bei einem Betrieb in der Region, bereiten eine Bewerbung vor und zeigen ihren Plan auf einem Poster oder in einem digitalen Portfolio.",
         punkte=["Fächer: Berufliche Orientierung, Deutsch, Fremdsprachen, WAH, ABU, Medien und Informatik",
                 "Kompetenzen: sich selbst einschätzen, recherchieren, Bewerbung schreiben, Gespräch führen, präsentieren",
                 "Einzelarbeit mit Lernpartnerin oder Lernpartner",
                 "Poster (Real, Sek) oder digitales Portfolio (Gymnasium, Berufsschule)",
                 "Variante Region für die Berufswahl, Variante Ausland für den Fremdsprachenunterricht",
                 "Digitalität: Optionen mit und ohne KI, Datenschutz bei Bewerbungen",
                 "Schlusspräsentation als Berufsmesse oder mit Vorstellungsgespräch"],
         lead="Ein Einzel-Projekt zur Berufswahl: Beruf, Betrieb und Arbeitsort erkunden, eine Bewerbung vorbereiten und den eigenen Plan präsentieren.",
         einleitung=["Die Lernenden stellen sich vor, sie hätten ihre Ausbildung abgeschlossen oder stünden kurz vor der Lehrstellensuche. Sie wählen einen Beruf, der sie interessiert, und suchen dafür einen echten Betrieb in der Region. Sie recherchieren, was der Beruf verlangt, wie der Betrieb arbeitet und wie ihr Arbeitsweg und Alltag aussehen würden. Dann bereiten sie eine Bewerbung vor und üben das Vorstellungsgespräch. Zum Schluss zeigen sie ihren Plan auf einem Poster oder in einem digitalen Portfolio und präsentieren ihn. Im Fremdsprachenunterricht gibt es eine Variante mit einem Arbeitsort im Ausland.",
                     "Unten findest du zuerst die Hauptschritte der Lernenden und die wichtigsten Angaben pro Stufe. Danach folgt der Ablauf für Lehrpersonen in sieben Schritten, jeweils mit Optionen mit und ohne KI, Hinweisen aus der Forschung und Vorlagen zum Herunterladen."]),
]
AUFGABEN_SEITEN = {
    "Einzel-Projekte": "lp-einzel-projekte.html", "Gruppen-Arbeiten": "lp-gruppen-arbeiten.html",
    "Präsentationen": "lp-praesentationen.html", "Grammatik": "lp-grammatik.html", "Schreiben": "lp-schreiben.html",
    "Posters": "lp-posters.html", "Digitalität": "lp-digitalitaet.html",
}
AUFGABEN_INTRO = {
    "Einzel-Projekte": "Hier findest du Aufträge, in denen Lernende selbstständig an einem persönlichen Projekt arbeiten und dabei begleitet werden.",
    "Posters": "Hier findest du Aufträge, deren Ergebnis ein Poster ist, oft mit einer kurzen Präsentation oder einer Ausstellung.",
    "Schreiben": "Hier findest du Aufträge mit echten Schreibanlässen, zum Beispiel Bewerbungen, Offerten oder Berichte.",
    "Gruppen-Arbeiten": "Hier findest du Aufträge, in denen Lernende in Gruppen planen, recherchieren und ein gemeinsames Produkt erarbeiten.",
    "Präsentationen": "Hier findest du Aufträge, die mit einer Präsentation enden, mit Hinweisen zu Vorbereitung, Probe und Bewertung.",
    "Digitalität": "Hier findest du Aufträge, in denen digitale Werkzeuge und KI eine wichtige Rolle spielen. Sie zeigen, wann KI das Lernen unterstützt und wann bewusst ohne gearbeitet wird.",
}
def auftrag_kachel(a):
    kopf = (f'<div class="thema-art bild"><img src="{a["bild"]}" alt="" loading="lazy"></div>' if a.get("bild")
            else f'<div class="thema-art"><svg viewBox="0 0 220 120" aria-hidden="true">{a["art"]}</svg></div>')
    return (f'      <a class="plan thema entile" href="{a["datei"]}">{kopf}'
            f'<span class="badge live">{a["badge"]}</span><h3>{a["titel"]}</h3><p>{a["text"]}</p>'
            f'<ul>{"".join(f"<li>{x}</li>" for x in a["punkte"])}</ul><span class="go">Zum Auftrag →</span></a>')
def auftraege_in(kat):
    return [a for a in AUFTRAEGE if kat in a["kategorien"]]
def form_kachel(titel, punkte, art):
    svg = f'<div class="thema-art"><svg viewBox="0 0 220 120" aria-hidden="true"><g {LINE2}>{art}</g></svg></div>'
    liste = f'<ul>{"".join(f"<li>{x}</li>" for x in punkte)}</ul>'
    n = len(auftraege_in(titel))
    if not n:
        return f'      <div class="plan thema">{svg}<span class="badge">In Vorbereitung</span><h3>{titel}</h3>{liste}</div>'
    return (f'      <a class="plan thema entile" href="{AUFGABEN_SEITEN[titel]}">{svg}<span class="badge live">{n} {"Auftrag" if n == 1 else "Aufträge"}</span>'
            f'<h3>{titel}</h3>{liste}<span class="go">Zu den Aufträgen →</span></a>')
kacheln = "\n".join(form_kachel(t, p, a) for t, p, a in AUFGABENFORMEN)
for titel, punkte, art in AUFGABENFORMEN:
    liste = auftraege_in(titel)
    if not liste:
        continue
    datei = AUFGABEN_SEITEN[titel]
    ACTIVE[datei] = "english.html"
    page(datei, f"{titel} – MuggliOnline", f"""<main class="wrap">
{hero(f'<a href="english.html">Lehrpersonen</a> › {titel}', "Für Lehrpersonen · Aufgabenform", titel, " · ".join(punkte))}
  <section class="section">
{einleitung("Aufträge", [AUFGABEN_INTRO.get(titel, "") + " Jeder Auftrag enthält Angaben zu Stufen, Lektionen und Noten, einen kurzen Ablauf für Lehrpersonen und Vorlagen zum Herunterladen.", "Hinweis: Viele Aufträge passen in mehrere Aufgabenformen. Sie erscheinen deshalb auf allen passenden Seiten, zum Beispiel unter Gruppen-Arbeiten, Präsentationen und Digitalität."], 2)}
    <div class="grid2 themen">
{chr(10).join(auftrag_kachel(a) for a in liste)}
    </div>
  </section>
</main>""", active="english.html", description=f"{titel}: Aufträge für den Unterricht mit Ablauf, Kompetenzen und Vorlagen.")

for a in AUFTRAEGE:
    ACTIVE[a["datei"]] = "english.html"
    erste = AUFGABEN_SEITEN[a["kategorien"][0]]
    inhalt = "".join((B / a["ordner"] / f).read_text() for f in sorted(x.name for x in (B / a["ordner"]).glob("*.html")))
    page(a["datei"], f"{a['titel']} – MuggliOnline", f"""<main class="wrap">
{hero(f'<a href="english.html">Lehrpersonen</a> › <a href="{erste}">{a["kategorien"][0]}</a> › {a["titel"]}', "Für Lehrpersonen · Auftrag", a["titel"], a["lead"])}
  <section class="section">
{einleitung("Worum es geht", a["einleitung"], 0)}
<!--BODY:{a["ordner"]}-->{inhalt}<!--/BODY-->
  </section>
</main>""", active="english.html", description=a["lead"])

page("english.html", "Lehrpersonen – MuggliOnline", f"""<main class="wrap">
{hero("Lehrpersonen", "", "Lehrpersonen", "Unterrichtsmaterialien, Projektideen und Vorlagen. Sie wurden für den Englischunterricht erstellt, können aber auch in anderen Fächern verwendet werden.")}
  <section class="section">
    <article class="vrow einleitung-bar">{silhouette(2)}<div class="vhead"><h2>Aufgabenformen</h2></div><div class="vtext"><p>Die Materialien wurden für den Englischunterricht an der Berufsschule erstellt, lassen sich aber übersetzen und in anderen Fächern einsetzen.</p><p>Sie sind nach Aufgabenform geordnet. Zu den meisten gibt es Vorlagen und Bewertungsraster.</p></div></article>
    <div class="grid3">
{kacheln}
    </div>
  </section>
</main>""", active="english.html", description="Unterrichtsmaterialien, Projektideen und Vorlagen für den Englischunterricht, geordnet nach Aufgabenform.")

LINE = 'fill="none" stroke="#3f5d4a" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"'
THEMEN_ART = {
"OSI Model": f'''<g {LINE}>{"".join(f'<rect x="{60+i*2}" y="{14+i*13}" width="{100-i*4}" height="9" rx="3" fill="{"#e7ede6" if i%2==0 else "#cfdacd"}"/>' for i in range(7))}
<path d="M178 20 v80 M172 92 l6 8 6-8 M42 100 v-80 M36 28 l6-8 6 8"/></g>''',
"Smart City": f'''<g {LINE}><path d="M20 106 h180"/><rect x="34" y="56" width="26" height="50" rx="2"/><rect x="66" y="36" width="30" height="70" rx="2" fill="#e7ede6"/>
<rect x="102" y="64" width="22" height="42" rx="2"/><rect x="130" y="28" width="28" height="78" rx="2" fill="#e7ede6"/><rect x="164" y="60" width="24" height="46" rx="2"/>
<path d="M74 48 h6 M84 48 h4 M74 60 h6 M84 60 h4 M74 72 h6 M138 40 h5 M147 40 h5 M138 52 h5 M147 52 h5 M138 64 h5 M147 64 h5"/>
<path d="M81 24 a8 8 0 0 1 0 -0.1 M73 20 a12 12 0 0 1 16 0 M68 14 a19 19 0 0 1 26 0" /><circle cx="81" cy="27" r="1.6" fill="#3f5d4a"/>
<circle cx="47" cy="44" r="4"/><circle cx="113" cy="52" r="4"/><circle cx="176" cy="48" r="4"/><path d="M51 42 l58 8 M117 51 l55 -2" stroke-dasharray="3 4"/></g>''',
"Software Tutorial": f'''<g {LINE}><rect x="54" y="16" width="112" height="70" rx="6" fill="#e7ede6"/><path d="M40 98 h140 l-10 -12 h-120 z"/>
<circle cx="110" cy="51" r="17" fill="#fff"/><path d="M104 42 v18 l14 -9 z" fill="#3f5d4a"/>
<path d="M150 64 l10 22 4 -9 9 -3 z" fill="#fff"/><circle cx="22" cy="30" r="9"/><circle cx="22" cy="58" r="9"/><circle cx="22" cy="86" r="9"/>
<path d="M19 27 l3 -2 v10 M19 55 q3 -4 6 0 q0 3 -6 7 h6 M19 82 h6 l-3 4 q4 0 4 3 q-1 4 -7 2"/></g>''',
"IT Job Abroad": f'''<g {LINE}><circle cx="70" cy="60" r="38" fill="#e7ede6"/><path d="M32 60 h76 M70 22 v76 M70 22 c-16 20 -16 56 0 76 M70 22 c16 20 16 56 0 76 M38 40 h64 M38 80 h64"/>
<rect x="136" y="62" width="50" height="38" rx="5" fill="#fff"/><path d="M152 62 v-8 h18 v8 M136 78 h50"/>
<path d="M106 34 q30 -26 62 -6" stroke-dasharray="4 5"/><path d="M168 22 l12 4 -9 8 z" fill="#3f5d4a"/></g>''',
"Cybersecurity & Data Protection": f'''<g {LINE}><path d="M110 12 l36 12 v28 c0 26 -16 44 -36 54 c-20 -10 -36 -28 -36 -54 v-28 z" fill="#e7ede6"/>
<rect x="96" y="56" width="28" height="24" rx="4" fill="#fff"/><path d="M102 56 v-8 a8 8 0 0 1 16 0 v8"/><circle cx="110" cy="66" r="2.4" fill="#3f5d4a"/><path d="M110 68 v5"/></g>
<g font-family="Inter, sans-serif" font-size="11" fill="#9fb3a5"><text x="20" y="30">1010</text><text x="30" y="60">0110</text><text x="18" y="90">1101</text><text x="166" y="34">0011</text><text x="176" y="64">1001</text><text x="164" y="94">0101</text></g>''',
}
def themen_karte(titel, text):
    if titel == "Smart City":
        return (f'      <a class="plan thema entile" href="auftrag-smart-city.html"><div class="thema-art"><svg viewBox="0 0 220 120" aria-hidden="true">{THEMEN_ART[titel]}</svg></div>'
                f'<span class="badge live">Auftrag</span><h3>{titel}</h3><p>{text}</p><span class="go">Zum Auftrag →</span></a>')
    return (f'      <div class="plan thema"><div class="thema-art"><svg viewBox="0 0 220 120" aria-hidden="true">{THEMEN_ART[titel]}</svg></div>'
            f'<span class="badge">In Vorbereitung</span><h3>{titel}</h3><p>{text}</p></div>')
INFORMATIK_THEMEN = [
    ("OSI Model", "Die sieben Schichten des OSI-Modells verstehen und auf Englisch erklären."),
    ("Smart City", "Vernetzte Technologien in der Stadt der Zukunft erkunden und präsentieren."),
    ("Software Tutorial", "Eine Software Schritt für Schritt erklären und ein eigenes Tutorial erstellen."),
    ("IT Job Abroad", "Stelleninserate lesen, sich bewerben und ein Vorstellungsgespräch üben."),
    ("Cybersecurity & Data Protection", "Risiken im Netz erkennen und Massnahmen zum Datenschutz diskutieren."),
]
INFORMATIK_INTRO = ("Unter den folgenden Themenbereichen findest du Unterrichtsideen mit Materialien und Bewertungsrastern. "
    "Sie wurden für den Unterricht in Technischem Englisch an der Berufsschule entwickelt, lassen sich aber übersetzen und für andere Fächer anpassen.")
INFORMATIK_INTRO2 = ("Weil sie für den Fremdsprachenunterricht gedacht sind, ist das sprachliche Niveau entsprechend angepasst. "
    "In der Erstsprache eignen sie sich deshalb auch gut als Projekte in der Oberstufe oder in der 6. Klasse.")
for datei, titel, text, punkte, lern in EN_BEREICHE:
    if lern != "nur-lp":
        continue
    if lern == "nur-lp":
        themen = "\n".join(themen_karte(t, d) for t, d in INFORMATIK_THEMEN)
        page(datei, f"{titel} – MuggliOnline", f"""<main class="wrap">
{hero(f'<a href="english.html">Lehrpersonen</a> › {titel}', "Für Lehrpersonen", titel, text)}
  <section class="section">
    <article class="vrow einleitung-bar">{silhouette(1)}<div class="vhead"><h2>Themenbereiche</h2></div><div class="vtext"><p>{INFORMATIK_INTRO}</p><p>{INFORMATIK_INTRO2}</p></div></article>
    <div class="grid3">
{themen}
    </div>
  </section>
</main>""", active="english.html", description=text)
        continue
    lern = lern or LERNENDE_BERUF
    spalte = lambda h, intro, items: (f'''    <div><h2>{h}</h2><p class="intro">{intro}</p><div class="stack">'''
                                      + "".join(plan(t, d) for t, d in items) + "</div></div>")
    page(datei, f"{titel} – MuggliOnline", f"""<main class="wrap">
{hero(f'<a href="english.html">Lehrpersonen</a> › {titel}', "Englisch", titel, text)}
  <section class="section">
    <div class="grid2">
{spalte("Für Lehrpersonen", "Materialien für den eigenen Unterricht.", LEHRPERSONEN)}
{spalte("Für Lernende", "Übungen mit direkter Rückmeldung.", lern)}
    </div>
  </section>
</main>""", active="english.html", description=text)

# ---------------- Pädagogik: Themenkarten ----------------
BEGLEITUNG_ART = ('<svg viewBox="0 0 220 120" aria-hidden="true"><g fill="none" stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M24 104 C70 98 74 70 110 64 S 160 40 170 22" stroke="#cdc6b6" stroke-width="2.4" stroke-dasharray="2 7"/>'
    '<path d="M44 110 V70 M84 110 V58 M44 70 H84 M44 90 H84 M44 110 L84 70" stroke="#3f5d4a" stroke-width="2.6"/>'
    '<path d="M112 92 V54 M140 92 V46 M112 54 H140" stroke="#3f5d4a" stroke-width="2.6" opacity=".55"/>'
    '<path d="M160 50 V36" stroke="#3f5d4a" stroke-width="2.6" opacity=".25"/></g>'
    '<g fill="#a8682f"><circle cx="24" cy="104" r="6"/><circle cx="66" cy="86" r="6.5"/><circle cx="110" cy="64" r="7"/><circle cx="148" cy="40" r="7.5"/><circle cx="172" cy="20" r="9"/></g>'
    '<circle cx="172" cy="20" r="14" fill="none" stroke="#a8682f" stroke-width="1.5" opacity=".5"/></svg>')
THEMA_BEGLEITUNG = f"""      <a class="plan thema entile" href="lernbegleitung.html"><div class="thema-art">{BEGLEITUNG_ART}</div><span class="badge live">Neu</span><h3>Lernprozesse begleiten</h3>
        <p>Hier geht es um die Begleitung individueller Lernprozesse: Wie unterstütze ich Lernende so, dass sie fachlich weiterkommen und zunehmend selbstständig lernen? Die Seite fasst zusammen, was die Forschung dazu sagt, und zeigt, wie sich das im Unterricht umsetzen lässt.</p>
        <ul><li>Zone der nächsten Entwicklung: Hilfe wirkt nur im individuellen Lernfenster</li><li>Scaffolding: so viel Hilfe wie nötig, so wenig wie möglich</li><li>Feedback, das Weiterlernen ermöglicht</li><li>Selbstreguliertes Lernen und das Turbinen-Modell</li><li>Lernbegleitungsgespräche mit dem GROW-Modell</li><li>Neun Instrumente, Toolbox und Planungs-Check</li></ul>
        <span class="go">Zum Thema →</span></a>"""

LV_ART = ('<svg viewBox="0 0 220 120" aria-hidden="true"><g fill="none" stroke-linecap="round">'
    '<circle cx="62" cy="64" r="30" stroke="#3f5d4a" stroke-width="2.6"/><circle cx="62" cy="64" r="9" fill="#3f5d4a" opacity=".35" stroke="none"/>'
    '<circle cx="112" cy="40" r="20" stroke="#3f5d4a" stroke-width="2.6" opacity=".6"/><circle cx="118" cy="88" r="22" stroke="#3f5d4a" stroke-width="2.6" opacity=".45"/>'
    '<path d="M150 64 H182" stroke="#cdc6b6" stroke-width="2.4" stroke-dasharray="2 7"/></g>'
    '<g fill="#a8682f"><circle cx="196" cy="64" r="11"/></g><circle cx="196" cy="64" r="17" fill="none" stroke="#a8682f" stroke-width="1.5" opacity=".5"/></svg>')
THEMA_LV = f"""      <a class="plan thema entile" href="lernvoraussetzungen.html"><div class="thema-art">{LV_ART}</div><span class="badge live">Neu</span><h3>Lernvoraussetzungen berücksichtigen</h3>
        <p>Hier geht es um die Berücksichtigung der Lernvoraussetzungen: Was bringen Lernende mit, wie erfasse ich das möglichst unverzerrt, und was folgt daraus für die Planung? Die Seite verbindet Lernpsychologie, Entwicklung, Heil- und Sonderpädagogik und Sozialpsychologie mit der Bedingungsanalyse.</p>
        <ul><li>Das INVO-Modell: fünf Bereiche individueller Voraussetzungen</li><li>Vorwissen als wichtigster Anknüpfungspunkt</li><li>Lernschwierigkeiten und Behinderung als Passungsfrage</li><li>Entwicklungsaufgaben, Bindung und die Gruppe</li><li>Wahrnehmungsfehler erkennen: beschreiben vor deuten</li><li>Bedingungsanalyse, Binnendifferenzierung und Planungs-Check</li></ul>
        <span class="go">Zum Thema →</span></a>"""

LA_ART = ('<svg viewBox="0 0 220 120" aria-hidden="true"><g fill="none" stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M20 100 H200" stroke="#cdc6b6" stroke-width="2"/>'
    '<path d="M30 92 L62 78 L94 84 L126 60 L158 52 L190 30" stroke="#3f5d4a" stroke-width="2.6"/>'
    '<circle cx="132" cy="52" r="26" stroke="#a8682f" stroke-width="2.6"/><path d="M151 71 L174 94" stroke="#a8682f" stroke-width="5"/></g>'
    '<g fill="#3f5d4a"><circle cx="30" cy="92" r="4.5"/><circle cx="62" cy="78" r="4.5"/><circle cx="94" cy="84" r="4.5"/><circle cx="126" cy="60" r="5"/><circle cx="158" cy="52" r="4.5"/><circle cx="190" cy="30" r="5.5"/></g></svg>')
THEMA_LA = f"""      <a class="plan thema entile" href="lernanalyse.html"><div class="thema-art">{LA_ART}</div><span class="badge live">Neu</span><h3>Lernen analysieren</h3>
        <p>Hier geht es um das genaue Hinschauen: Was ist Lernen, woran erkenne ich es bei Kindern und Jugendlichen, und wie nutze ich Beobachtungen, Lernspuren und Gespräche für passende Förderung? Die Seite verbindet Lernpsychologie, Entwicklung und pädagogische Diagnostik.</p>
        <ul><li>Was Lernen ist und wie es sich im Jugendalter verändert</li><li>Vorgehen, Ergebnisse und Fortschritte lesen</li><li>Hindernisse, Stärken und Begabungen erkennen</li><li>Diagnostik-Förder-Kreislauf und Beobachtungsprotokolle</li><li>Urteilsfehler erkennen und Entscheide gut begründen</li><li>Neun Instrumente und ein Analyse-Check</li></ul>
        <span class="go">Zum Thema →</span></a>"""

LG_ART = ('<svg viewBox="0 0 220 120" aria-hidden="true"><g fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.6">'
    '<path d="M28 22 H120 a10 10 0 0 1 10 10 V66 a10 10 0 0 1 -10 10 H64 L44 94 V76 H28 a10 10 0 0 1 -10 -10 V32 a10 10 0 0 1 10 -10 Z" fill="#e7ede6" stroke="#3f5d4a"/>'
    '<path d="M110 46 H192 a10 10 0 0 1 10 10 V86 a10 10 0 0 1 -10 10 H180 V112 L160 96 H110 a10 10 0 0 1 -10 -10 V56 a10 10 0 0 1 10 -10 Z" fill="#fff" stroke="#a8682f"/>'
    '<path d="M36 40 H108 M36 54 H92" stroke="#3f5d4a"/><path d="M118 64 H184 M118 78 H170" stroke="#a8682f"/></g></svg>')
THEMA_LG = f"""      <a class="plan thema entile" href="lerngespraeche.html"><div class="thema-art">{LG_ART}</div><span class="badge live">Neu</span><h3>Lerngespräche führen</h3>
        <p>Vom kurzen Feedback im Unterricht bis zum Standortgespräch mit Eltern: Hier geht es darum, wie Gespräche das Lernen voranbringen. Die Seite verbindet Feedbackforschung, Selbstwirksamkeit und lösungsorientierte Beratung mit konkreten Gesprächsmodellen.</p>
        <ul><li>Gesprächsformen und Feedbackebenen</li><li>Haltung, Sprache und Gleichwürdigkeit</li><li>Selbstwirksamkeit, Lernstrategien und Fehler</li><li>GROW, lösungsorientierte Fragen und «Ich schaffs»</li><li>Kritik, WOWW, dialogisches Lernen und Standortgespräche</li><li>Acht Instrumente und ein Gesprächs-Check</li></ul>
        <span class="go">Zum Thema →</span></a>"""

DIG_ART = ('<svg viewBox="0 0 220 120" aria-hidden="true"><g fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.4">'
    '<path d="M30 30 H92 a6 6 0 0 1 6 6 V88 H30 a6 6 0 0 1 -6 -6 V36 a6 6 0 0 1 6 -6 Z" fill="#e7ede6" stroke="#3f5d4a"/><path d="M38 46 H84 M38 58 H84 M38 70 H72" stroke="#3f5d4a"/>'
    '<path d="M104 60 H122" stroke="#cdc6b6" stroke-dasharray="2 6"/>'
    '<path d="M150 34 L176 50 L176 80 L150 96 L124 80 L124 50 Z" fill="#fff" stroke="#a8682f"/>'
    '<path d="M150 34 V96 M124 50 L176 80 M176 50 L124 80" stroke="#a8682f" stroke-width="1.6" opacity=".6"/></g>'
    '<g fill="#a8682f"><circle cx="150" cy="34" r="5"/><circle cx="176" cy="50" r="5"/><circle cx="176" cy="80" r="5"/><circle cx="150" cy="96" r="5"/><circle cx="124" cy="80" r="5"/><circle cx="124" cy="50" r="5"/></g>'
    '<circle cx="194" cy="24" r="8" fill="#3f5d4a"/></svg>')
THEMA_DIG = f"""      <a class="plan thema entile" href="digitalitaet.html"><div class="thema-art">{DIG_ART}</div><span class="badge live">Neu</span><h3>Lernen und Digitalität verbinden</h3>
        <p>Vom Buch zum vernetzten Computer: Hier geht es darum, was Lernen in einer Kultur der Digitalität bedeutet und wie Lernangebote darauf antworten. Die Seite verbindet Stalder, Döbeli Honegger und Krommer mit Klafki, Projektunterricht, Spieltheorie und multimodalem Erklären.</p>
        <ul><li>Digitalität, Leitmedienwechsel und die drei Formen nach Stalder</li><li>Was wichtiger wird: Filtern, Fragen, Nichtautomatisierbares</li><li>Unterrichten mit, über und trotz Medien</li><li>Digitale Identität, Medienkritik und Ethik der Automatisierung</li><li>Planen mit Klafki, multimodal erklären, Tools kriterienbasiert prüfen</li><li>Projekte, HERZ-Theorie des Spiels und ein Planungs-Check</li></ul>
        <span class="go">Zum Thema →</span></a>"""

BEU_ART = ('<svg viewBox="0 0 220 120" aria-hidden="true"><g fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.4">'
    '<rect x="26" y="18" width="78" height="92" rx="6" fill="#e7ede6" stroke="#3f5d4a"/><path d="M38 38 H92 M38 54 H92 M38 70 H78" stroke="#3f5d4a"/>'
    '<path d="M40 90 l6 6 l12 -12" stroke="#a8682f" stroke-width="3"/>'
    '<circle cx="152" cy="44" r="16" fill="#fff" stroke="#a8682f"/><path d="M124 104 c0 -22 12 -34 28 -34 s28 12 28 34" fill="#fff" stroke="#a8682f"/>'
    '<path d="M108 64 H126" stroke="#cdc6b6" stroke-dasharray="2 6"/></g>'
    '<g fill="#3f5d4a"><circle cx="190" cy="22" r="7"/></g></svg>')
THEMA_BEU = f"""      <a class="plan thema entile" href="beurteilung.html"><div class="thema-art">{BEU_ART}</div><span class="badge live">Neu</span><h3>Lernende in Beurteilungsprozesse involvieren</h3>
        <p>Beurteilung ist nicht nur Sache der Lehrperson: Hier geht es darum, wie Lernende Ziele und Kriterien mitbestimmen, sich selbst und einander beurteilen und an Portfolio, Präsentation und Beurteilungsgespräch beteiligt sind. Die Seite verbindet Winter, Lötscher et al., Fraefel, Oser und Ruf &amp; Gallin.</p>
        <ul><li>Begleitung und Allokation, formativ und summativ</li><li>Neue Beurteilungskultur und echte Partizipation</li><li>Ziele und Kriterien klären, Single-Point-Rubric</li><li>Selbst- und Peer-Beurteilung, dialogisches Lernen</li><li>Portfolio, Präsentation und angepasste Lernkontrollen</li><li>Gesamtbeurteilung, Laufbahn und ein Beurteilungs-Check</li></ul>
        <span class="go">Zum Thema →</span></a>"""

KON_ART = ('<svg viewBox="0 0 220 120" aria-hidden="true"><g fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.4">'
    '<circle cx="62" cy="40" r="13" fill="#fff" stroke="#3f5d4a"/><path d="M38 100 c0 -24 10 -36 24 -36 s24 12 24 36" fill="#e7ede6" stroke="#3f5d4a"/>'
    '<circle cx="158" cy="40" r="13" fill="#fff" stroke="#a8682f"/><path d="M134 100 c0 -24 10 -36 24 -36 s24 12 24 36" fill="#f6ebdc" stroke="#a8682f"/>'
    '<path d="M92 58 l10 8 l-6 4 l12 10" stroke="#9b4d5e" stroke-width="3"/><path d="M128 58 l-10 8 l6 4 l-12 10" stroke="#9b4d5e" stroke-width="3"/>'
    '<path d="M90 104 H130" stroke="#3f5d4a" stroke-width="3"/></g>'
    '<g fill="#fff" font-size="11" font-weight="700" font-family="sans-serif" text-anchor="middle"><circle cx="20" cy="18" r="10" fill="#b8902f"/><text x="20" y="22">1</text><circle cx="42" cy="12" r="10" fill="#3a7d84"/><text x="42" y="16">2</text><circle cx="64" cy="8" r="10" fill="#6d5a8e"/><text x="64" y="12">3</text></g></svg>')
THEMA_KON = f"""      <a class="plan thema entile" href="konflikte.html"><div class="thema-art">{KON_ART}</div><span class="badge live">Neu</span><h3>Umgang mit Konflikten, Gewalt und Mobbing</h3>
        <p>Streit gehört zum Aufwachsen, Mobbing nicht: Hier geht es darum, Konflikt, Gewalt und Mobbing zu unterscheiden, Mobbing als Gruppenphänomen zu verstehen und stufengerecht vorzubeugen und einzugreifen, mit Bezug zu Zyklus 1, 2 und 3. Die Seite verbindet Alsaker, Schubarth, Jannan, den No Blame Approach und SchoolMatters.</p>
        <ul><li>Konflikt, Aggression, Gewalt und Mobbing unterscheiden</li><li>Cybermobbing erkennen und rechtlich einordnen</li><li>Rollen in der Gruppe und der Mobbingprozess</li><li>Soziales Verhalten von Zyklus 1 bis Zyklus 3</li><li>Prävention, Programme und No Blame Approach</li><li>Intervention, Elternarbeit und ein Klassen-Check</li></ul>
        <span class="go">Zum Thema →</span></a>"""

GAME_PT_ART = ('<svg viewBox="0 0 220 120" aria-hidden="true"><rect x="40" y="10" width="140" height="100" rx="10" fill="#f6ebdc" stroke="#2f3a32" stroke-width="2.5"/>'
    '<rect x="62" y="30" width="96" height="60" rx="6" fill="#cfe3c4" stroke="#3f5d4a" stroke-width="1.5"/>'
    '<g stroke="#2f3a32" stroke-width="1.2" fill="#fff"><rect x="44" y="14" width="16" height="14" rx="2"/><rect x="62" y="14" width="16" height="14" rx="2"/><rect x="80" y="14" width="16" height="14" rx="2"/><rect x="98" y="14" width="16" height="14" rx="2"/><rect x="116" y="14" width="16" height="14" rx="2"/><rect x="134" y="14" width="16" height="14" rx="2"/><rect x="160" y="14" width="16" height="14" rx="2"/>'
    '<rect x="44" y="92" width="16" height="14" rx="2"/><rect x="62" y="92" width="16" height="14" rx="2"/><rect x="80" y="92" width="16" height="14" rx="2"/><rect x="98" y="92" width="16" height="14" rx="2"/><rect x="116" y="92" width="16" height="14" rx="2"/><rect x="134" y="92" width="16" height="14" rx="2"/><rect x="160" y="92" width="16" height="14" rx="2"/></g>'
    '<path d="M95 75 V50 M95 50 l-9 -5 M95 50 l9 -5 M95 50 v-10" stroke="#4f8fbf" stroke-width="2.5" fill="none" stroke-linecap="round"/>'
    '<rect x="112" y="62" width="30" height="16" fill="#2f3a32" transform="skewX(-15)"/><circle cx="125" cy="44" r="8" fill="#e0a526"/>'
    '<rect x="186" y="62" width="26" height="26" rx="5" fill="#fff" stroke="#2f3a32" stroke-width="2"/><circle cx="193" cy="69" r="2.5" fill="#2f3a32"/><circle cx="205" cy="81" r="2.5" fill="#2f3a32"/><circle cx="199" cy="75" r="2.5" fill="#2f3a32"/></svg>')
GAME_IE_ART = ('<svg viewBox="0 0 220 120" aria-hidden="true"><rect width="220" height="120" rx="10" fill="#2b3d4f"/>'
    '<path d="M0 92 Q55 84 110 92 T220 90 V120 H0 Z" fill="#46627a"/><path d="M50 92 Q80 52 112 58 Q150 50 176 92 Z" fill="#5f8a5a"/>'
    '<rect x="88" y="70" width="14" height="14" fill="#1f2b33"/><rect x="108" y="66" width="18" height="18" fill="#1f2b33"/><rect x="132" y="72" width="12" height="12" fill="#1f2b33"/>'
    '<rect x="91" y="74" width="4" height="4" fill="#ffd55a"/><rect x="113" y="70" width="5" height="5" fill="#ffd55a"/>'
    '<path d="M150 72 V42 M150 42 l-10 -6 M150 42 l10 -6 M150 42 v-12" stroke="#fff" stroke-width="2.5" stroke-linecap="round"/>'
    '<g transform="translate(26 22)"><rect x="0" y="12" width="28" height="22" rx="4" fill="#ffd55a"/><path d="M6 12 V7 a8 8 0 0 1 16 0 V12" fill="none" stroke="#ffd55a" stroke-width="3.5"/><circle cx="14" cy="22" r="3" fill="#2b3d4f"/></g>'
    '<path d="M180 18 l-6 12 h6 l-4 12" stroke="#ffd55a" stroke-width="2.5" fill="none"/></svg>')

INSTR_ART = ('<svg viewBox="0 0 220 120" aria-hidden="true"><g fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.4">'
    '<rect x="40" y="24" width="64" height="84" rx="6" fill="#e7ede6" stroke="#3f5d4a"/><path d="M52 44 H92 M52 58 H92 M52 72 H80" stroke="#3f5d4a"/>'
    '<rect x="116" y="14" width="64" height="84" rx="6" fill="#fff" stroke="#3f5d4a"/><path d="M128 34 H168 M128 48 H168 M128 62 H156" stroke="#3f5d4a"/>'
    '<path d="M148 76 V100 M138 90 L148 100 L158 90" stroke="#a8682f" stroke-width="3"/></g></svg>')
THEMA_INSTR = f"""      <a class="plan thema entile breit" href="instrumente.html"><div class="thema-art">{INSTR_ART}</div><span class="badge live">Gratis</span><h3>Instrumente</h3>
        <p>Raster, Bögen und Leitfäden für Praktikum und Unterricht, geordnet nach Handlungskompetenz. Alle Instrumente dürfen gratis heruntergeladen, genutzt und angepasst werden.</p>
        <ul><li>als bearbeitbare Word-Datei oder als PDF</li><li>einzeln oder als Sammlung pro Thema</li><li>mit Quellenangaben zur Theorie</li></ul>
        <span class="go">Zu den Instrumenten →</span></a>"""

area("didaktik.html", "Pädagogik", "",
     "Pädagogik",
     "Zusammenfassungen, Verknüpfungen und Handlungsansätze zu wissenschaftlich fundierten Theorien und Konzepten, teils mit Instrumenten für die Praxis.",
     "Die Inhalte stützen sich auf wissenschaftlich fundierte Quellen. Geplant sind:",
     [THEMA_BEGLEITUNG,
      THEMA_LV,
      THEMA_LA,
      THEMA_LG,
      THEMA_DIG,
      THEMA_BEU,
      THEMA_KON,
      THEMA_INSTR], cols="grid2 themen",
     bar=("Theorie trifft Praxis", ["Hier findest du Zusammenfassungen zu pädagogischen und didaktischen Theorien und Konzepten. Sie stützen sich auf wissenschaftlich fundierte Quellen, die jeweils angegeben sind.",
          "Verknüpfungen und Handlungsansätze zeigen, was die Theorie für den Unterrichtsalltag bedeutet. Teilweise gibt es dazu Instrumente für die Praxis."], 1))

# ---------------- Pädagogik: Thema Begleitung ----------------
ACTIVE["lernbegleitung.html"] = "didaktik.html"
LB_BODY = "".join((B / "lernbegleitung" / f).read_text() for f in sorted(p.name for p in (B / "lernbegleitung").glob("*.html")))
page("lernbegleitung.html", "Lernprozesse begleiten – MuggliOnline", f"""<main class="wrap">
{hero('<a href="didaktik.html">Pädagogik</a> › Lernprozesse begleiten', "Pädagogik · Thema", "Lernprozesse begleiten", "Was sagt die Wissenschaft? Theorien und Konzepte, Verknüpfungen, Spannungsfelder und Handlungsmöglichkeiten für die Praxis.")}
  <section class="section">
{einleitung("Worum es geht", ["Lernende einer Klasse stehen nie am selben Ort. Individuelle Lernbegleitung heisst, Denkwege und Lernbedingungen sichtbar zu machen, die Unterstützung darauf abzustimmen und zu prüfen, ob die Lernenden fachlich und in ihrer Selbstregulation weiterkommen.", "Diese Seite verbindet zentrale Theorien – von Wygotskis Zone der nächsten Entwicklung über Scaffolding und Feedback bis zum selbstregulierten Lernen – mit Gesprächsmodellen, Werkzeugen und einem Planungs-Check. Du kannst sie von oben nach unten durcharbeiten oder über das Inhaltsverzeichnis gezielt springen."], 1)}
<!--BODY:lernbegleitung-->{LB_BODY}<!--/BODY-->
  </section>
</main>""", active="didaktik.html", description="Begleitung individueller Lernprozesse: Theorien, Konzepte, Spannungsfelder und Werkzeuge für die Unterrichtspraxis, wissenschaftlich fundiert.")

# ---------------- Pädagogik: Thema Lernvoraussetzungen ----------------
ACTIVE["lernvoraussetzungen.html"] = "didaktik.html"
LV_BODY = "".join((B / "lernvoraussetzungen" / f).read_text() for f in sorted(p.name for p in (B / "lernvoraussetzungen").glob("*.html")))
page("lernvoraussetzungen.html", "Lernvoraussetzungen berücksichtigen – MuggliOnline", f"""<main class="wrap">
{hero('<a href="didaktik.html">Pädagogik</a> › Lernvoraussetzungen berücksichtigen', "Pädagogik · Thema", "Lernvoraussetzungen berücksichtigen", "Was bringen Lernende mit, wie nehme ich das wahr, und was folgt daraus für den Unterricht? Theorien, Konzepte, Spannungsfelder und Handlungsmöglichkeiten.")}
  <section class="section">
{einleitung("Worum es geht", ["Lernende bringen Vorwissen, Strategien, Motivation, Gefühle, Entwicklungsthemen und Beziehungserfahrungen mit. Ob daraus Schwierigkeiten werden, hängt davon ab, wie gut Unterricht und Voraussetzungen zueinander passen.", "Diese Seite klärt zuerst, was Lernvoraussetzungen sind, stellt dann zentrale Bereiche vor (vom INVO-Modell über Lernschwierigkeiten bis zur Gruppe), zeigt, wie die eigene Wahrnehmung das Bild verzerren kann, und führt zur Bedingungsanalyse, zur Binnendifferenzierung und zu einem Planungs-Check. Du kannst sie von oben nach unten durcharbeiten oder über das Inhaltsverzeichnis springen."], 1)}
<!--BODY:lernvoraussetzungen-->{LV_BODY}<!--/BODY-->
  </section>
</main>""", active="didaktik.html", description="Lernvoraussetzungen berücksichtigen: INVO-Modell, Vorwissen, Lernschwierigkeiten, Wahrnehmung, Bedingungsanalyse und Binnendifferenzierung, wissenschaftlich fundiert.")

# ---------------- Pädagogik: Thema Lernen analysieren ----------------
ACTIVE["lernanalyse.html"] = "didaktik.html"
LA_BODY = "".join((B / "lernanalyse" / f).read_text() for f in sorted(p.name for p in (B / "lernanalyse").glob("*.html")))
page("lernanalyse.html", "Lernen analysieren – MuggliOnline", f"""<main class="wrap">
{hero('<a href="didaktik.html">Pädagogik</a> › Lernen analysieren', "Pädagogik · Thema", "Lernen analysieren", "Was ist Lernen, woran erkenne ich es, und was folgt daraus? Theorien, Konzepte, Spannungsfelder und Handlungsmöglichkeiten für die Praxis.")}
  <section class="section">
{einleitung("Worum es geht", ["Gezielt fördern kann nur, wer versteht, wie Lernende lernen. Weil Lernen im Kopf stattfindet, bleiben dafür nur Spuren: Vorgehen, Ergebnisse, Fehler, Fortschritte und Äusserungen. Lernen zu analysieren heisst, diese Spuren sorgfältig zu sammeln, vorsichtig zu deuten und daraus passende Lernangebote abzuleiten.", "Diese Seite klärt zuerst, was Lernen ist und wie Kinder und Jugendliche lernen. Dann zeigt sie, worauf sich der Blick richten kann, mit welchen Methoden sich Lernen erfassen lässt, wo das eigene Urteil verzerrt sein kann und was aus der Analyse folgt, bis hin zu Zusammenarbeit, Abklärung und Laufbahnentscheiden. Du kannst sie von oben nach unten durcharbeiten oder über das Inhaltsverzeichnis springen."], 1)}
<!--BODY:lernanalyse-->{LA_BODY}<!--/BODY-->
  </section>
</main>""", active="didaktik.html", description="Lernen analysieren: Lernbegriff, Lernen im Jugendalter, Lernprozesse und Ergebnisse, Fortschritte, Hindernisse und Begabungen, Diagnostik-Förder-Kreislauf, Beobachtung und Urteilsfehler, wissenschaftlich fundiert.")

# ---------------- Pädagogik: Thema Lerngespräche führen ----------------
ACTIVE["lerngespraeche.html"] = "didaktik.html"
LG_BODY = "".join((B / "lerngespraeche" / f).read_text() for f in sorted(p.name for p in (B / "lerngespraeche").glob("*.html")))
page("lerngespraeche.html", "Lerngespräche führen – MuggliOnline", f"""<main class="wrap">
{hero('<a href="didaktik.html">Pädagogik</a> › Lerngespräche führen', "Pädagogik · Thema", "Lerngespräche führen", "Wie bringen Gespräche das Lernen voran? Theorien, Gesprächsformen, Modelle, Spannungsfelder und Handlungsmöglichkeiten für die Praxis.")}
  <section class="section">
{einleitung("Worum es geht", ["Lehrpersonen sprechen ständig mit Lernenden: kurz im Vorbeigehen, in Coachinggesprächen, bei Rückmeldungen zu Arbeiten und in Standortgesprächen mit Eltern. Lerngespräche sind die Gespräche, in denen das Lernen selbst zum Thema wird: Wo stehst du, wohin willst du, und was ist dein nächster Schritt?", "Diese Seite klärt zuerst, was ein Lerngespräch ausmacht, welche Formen und Feedbackebenen es gibt und welche Haltung und Sprache tragen. Dann zeigt sie, wie Gespräche Selbstwirksamkeit, Lernstrategien und den Umgang mit Fehlern stärken, und stellt Modelle für die Praxis vor, von GROW über lösungsorientierte Fragen und «Ich schaffs» bis zum Standortgespräch. Du kannst sie von oben nach unten durcharbeiten oder über das Inhaltsverzeichnis springen."], 1)}
<!--BODY:lerngespraeche-->{LG_BODY}<!--/BODY-->
  </section>
</main>""", active="didaktik.html", description="Lerngespräche führen: Gesprächsformen, Feedbackebenen, Haltung und Sprache, Selbstwirksamkeit, GROW, lösungsorientierte Fragen, Ich schaffs, Kritik, WOWW, dialogisches Lernen und Standortgespräche, wissenschaftlich fundiert.")

# ---------------- Pädagogik: Thema Lernen und Digitalität ----------------
ACTIVE["digitalitaet.html"] = "didaktik.html"
DIG_BODY = "".join((B / "digitalitaet" / f).read_text() for f in sorted(p.name for p in (B / "digitalitaet").glob("*.html")))
page("digitalitaet.html", "Lernen und Digitalität verbinden – MuggliOnline", f"""<main class="wrap">
{hero('<a href="didaktik.html">Pädagogik</a> › Lernen und Digitalität verbinden', "Pädagogik · Thema", "Lernen und Digitalität verbinden", "Was bedeutet Lernen in einer Kultur der Digitalität? Theorien, Konzepte, Spannungsfelder und Handlungsmöglichkeiten für die Praxis.")}
  <section class="section">
{einleitung("Worum es geht", ["Das Leitmedium wechselt vom gedruckten Buch zu digitalen Netzwerken. Informationen sind im Überfluss vorhanden, Algorithmen sortieren vor, und KI übernimmt Aufgaben, die früher als Lernziele galten. Lernen heisst darum immer weniger, Wissen aufzunehmen, und immer mehr, verantwortungsvoll mit vielen Handlungsmöglichkeiten umzugehen.", "Diese Seite klärt zuerst, was Digitalität ist und welche Kompetenzen wichtiger werden. Dann fragt sie, warum und wie digitale Medien in die Schule gehören, mit Blick auf Identität, Medienkritik und Ethik, und zeigt, wie Lernangebote unter diesen Bedingungen geplant, erklärt, geprüft und gestaltet werden. Du kannst sie von oben nach unten durcharbeiten oder über das Inhaltsverzeichnis springen."], 1)}
<!--BODY:digitalitaet-->{DIG_BODY}<!--/BODY-->
  </section>
</main>""", active="didaktik.html", description="Lernen und Digitalität verbinden: Leitmedienwechsel, Kultur der Digitalität nach Stalder, Kompetenzen, Unterrichten mit, über und trotz Medien, Medienbildung, Ethik der Automatisierung, Klafki, multimodales Erklären, Tools evaluieren, Projekte und HERZ-Theorie, wissenschaftlich fundiert.")

# ---------------- Pädagogik: Thema Beurteilung ----------------
ACTIVE["beurteilung.html"] = "didaktik.html"
BEU_BODY = "".join((B / "beurteilung" / f).read_text() for f in sorted(p.name for p in (B / "beurteilung").glob("*.html")))
page("beurteilung.html", "Lernende in Beurteilungsprozesse involvieren – MuggliOnline", f"""<main class="wrap">
{hero('<a href="didaktik.html">Pädagogik</a> › Lernende in Beurteilungsprozesse involvieren', "Pädagogik · Thema", "Lernende in Beurteilungsprozesse involvieren", "Wie werden Lernende von Beurteilten zu Beteiligten? Theorien, Konzepte, Spannungsfelder und Handlungsmöglichkeiten für die Praxis.")}
  <section class="section">
{einleitung("Worum es geht", ["Heterogene Lern- und Leistungsvoraussetzungen sind im Schulalltag Realität. Auch bei der Beurteilung sollen Lernende einbezogen werden und ihre Leistungsanforderungen aktiv mitgestalten: Sie klären Ziele und Kriterien mit, beurteilen sich selbst und einander und bringen ihre Sicht in Gespräche und Entscheide ein.", "Diese Seite klärt zuerst, wozu beurteilt wird, was eine neue Beurteilungskultur ausmacht und was echte Partizipation ist. Dann zeigt sie, wie Lernende Kriterien mitbestimmen, sich selbst und einander beurteilen, und stellt Portfolio, Präsentation, angepasste Lernkontrollen und die Gesamtbeurteilung für Laufbahnentscheide vor. Du kannst sie von oben nach unten durcharbeiten oder über das Inhaltsverzeichnis springen."], 1)}
<!--BODY:beurteilung-->{BEU_BODY}<!--/BODY-->
  </section>
</main>""", active="didaktik.html", description="Lernende in Beurteilungsprozesse involvieren: Begleitung und Allokation, neue Beurteilungskultur, Partizipation, Erfolgskriterien, Single-Point-Rubric, Selbst- und Peer-Beurteilung, dialogisches Lernen, Portfolio, Präsentation, Lernkontrollen und Gesamtbeurteilung, wissenschaftlich fundiert.")

# ---------------- Pädagogik: Thema Konflikte, Gewalt und Mobbing ----------------
ACTIVE["konflikte.html"] = "didaktik.html"
KON_BODY = "".join((B / "konflikte" / f).read_text() for f in sorted(p.name for p in (B / "konflikte").glob("*.html")))
page("konflikte.html", "Umgang mit Konflikten, Gewalt und Mobbing – MuggliOnline", f"""<main class="wrap">
{hero('<a href="didaktik.html">Pädagogik</a> › Umgang mit Konflikten, Gewalt und Mobbing', "Pädagogik · Thema", "Umgang mit Konflikten, Gewalt und Mobbing", "Wann ist ein Streit ein Streit, und wann ist es Mobbing? Theorien, Konzepte, Spannungsfelder und Handlungsmöglichkeiten für Zyklus 1, 2 und 3.")}
  <section class="section">
{einleitung("Worum es geht", ["Konflikte gehören zum Aufwachsen und fördern die soziale Entwicklung. Gewalt und Mobbing dagegen verletzen, isolieren und behindern das Lernen aller in der Klasse. Lehrpersonen müssen unterscheiden können, was vor ihnen liegt, und wissen, wie sie stufengerecht vorbeugen und eingreifen.", "Diese Seite klärt zuerst die Begriffe und zeigt, warum Mobbing ein Gruppenphänomen ist, wie es in Phasen verläuft und wie sich soziales Verhalten vom Kindergarten bis zur Oberstufe verändert. Dann stellt sie Prävention, Programme, den No Blame Approach, Intervention und Elternarbeit vor, jeweils mit Hinweisen zu Zyklus 1, 2 und 3. Du kannst sie von oben nach unten durcharbeiten oder über das Inhaltsverzeichnis springen."], 1)}
<!--BODY:konflikte-->{KON_BODY}<!--/BODY-->
  </section>
</main>""", active="didaktik.html", description="Umgang mit Konflikten, Gewalt und Mobbing: Konflikt und Mobbing unterscheiden, Cybermobbing, Rollen in der Gruppe, Mobbingprozess, Entwicklung von Zyklus 1 bis 3, Prävention, FAUSTLOS, Be-Prox, No Blame Approach, Intervention und Elternarbeit, wissenschaftlich fundiert.")

# ---------------- Pädagogik: Instrumente ----------------
ACTIVE["instrumente.html"] = "didaktik.html"
INSTRUMENTE = [
    ("Lernprozesse begleiten", "lernbegleitung.html", BEGLEITUNG_ART,
     ("downloads/lernbegleitung/Instrumente_Lernprozesse_begleiten", "Alle 9 Instrumente in einer Datei"),
     [("Lernfenster-Planer", "LB1_Lernfenster-Planer"),
      ("Hilfen-Treppe (Scaffolding)", "LB2_Hilfen-Treppe"),
      ("Formative Kurzerhebung", "LB3_Formative-Kurzerhebung"),
      ("Feedback-Matrix", "LB4_Feedback-Matrix"),
      ("Begleitbogen selbstreguliertes Lernen", "LB5_SRL-Begleitbogen"),
      ("Strategie-Check «Warum nutzt sie die Strategie nicht?»", "LB6_Strategie-Check"),
      ("Vier-Felder-Blick bei Lernblockaden", "LB7_Vier-Felder-Blick"),
      ("Lernspur-Blatt für Lernende", "LB8_Lernspur-Blatt"),
      ("Planungs-Check Lernbegleitung", "LB9_Planungs-Check")]),
    ("Lernvoraussetzungen berücksichtigen", "lernvoraussetzungen.html", LV_ART,
     ("downloads/lernvoraussetzungen/Instrumente_Lernvoraussetzungen", "Alle 4 Instrumente in einer Datei"),
     [("Bedingungsanalyse-Raster", "LV1_Bedingungsanalyse-Raster"),
      ("Beobachtungsbogen «Beschreiben vor Deuten»", "LV2_Beobachtungsbogen_Beschreiben_vor_Deuten"),
      ("Leitfaden «Verdacht auf Lernschwierigkeiten»", "LV3_Leitfaden_Verdacht_auf_Lernschwierigkeiten"),
      ("Differenzierungs-Planer", "LV4_Differenzierungs-Planer")]),
    ("Lernen analysieren", "lernanalyse.html", LA_ART,
     ("downloads/lernanalyse/Instrumente_Lernen_analysieren", "Alle 9 Instrumente in einer Datei"),
     [("Beobachtungsprotokoll «Beschreiben, deuten, prüfen»", "LA1_Beobachtungsprotokoll"),
      ("Lernspuren-Analyse «Die Logik einer Lösung»", "LA2_Lernspuren-Analyse"),
      ("Lernverlaufsbogen", "LA3_Lernverlaufsbogen"),
      ("Single-Point-Rubric", "LA4_Single-Point-Rubric"),
      ("Hypothesen-Fächer «Was bremst das Lernen?»", "LA5_Hypothesen-Faecher"),
      ("Stärken- und Potenzialprofil", "LA6_Staerken-und-Potenzialprofil"),
      ("Passungs-Check für die eigene Lektion", "LA7_Passungs-Check"),
      ("Vorbereitung Standort- oder Übertrittsgespräch", "LA8_Gespraechsvorbereitung"),
      ("Lernjournal für Lernende", "LA9_Lernjournal")]),
    ("Lerngespräche führen", "lerngespraeche.html", LG_ART,
     ("downloads/lerngespraeche/Instrumente_Lerngespraeche_fuehren", "Alle 8 Instrumente in einer Datei"),
     [("Gesprächsleitfaden Lerngespräch", "LG1_Gespraechsleitfaden"),
      ("Fragekarten «lösungsorientiert fragen»", "LG2_Fragekarten"),
      ("Feedback-Planer", "LG3_Feedback-Planer"),
      ("«Ich schaffs»-Plan für Jugendliche", "LG4_Ich-schaffs-Plan"),
      ("Kritische Rückmeldung vorbereiten", "LG5_Kritische_Rueckmeldung"),
      ("WOWW-Beobachtungsbogen und Klassenskala", "LG6_WOWW-Beobachtung"),
      ("Standortgespräch: Vorbereitung und Fördervereinbarung", "LG7_Standortgespraech"),
      ("Gesprächsreflexion", "LG8_Gespraechsreflexion")]),
    ("Lernen und Digitalität", "digitalitaet.html", DIG_ART,
     ("downloads/digitalitaet/Instrumente_Lernen_und_Digitalitaet", "Alle 8 Instrumente in einer Datei"),
     [("Planungsraster Klafki digital", "DI1_Planungsraster-Klafki-digital"),
      ("Mit-über-trotz-Raster", "DI2_Mit-ueber-trotz-Raster"),
      ("Tool-Check", "DI3_Tool-Check"),
      ("KI-Antwort prüfen", "DI4_KI-Antwort-pruefen"),
      ("Projektplaner in fünf Phasen", "DI5_Projektplaner"),
      ("Lernspiel-Check nach der HERZ-Theorie", "DI6_Lernspiel-Check-HERZ"),
      ("Klassenvereinbarung digital", "DI7_Klassenvereinbarung-digital"),
      ("Planungs-Check Digitalität", "DI8_Planungs-Check")]),
    ("Lernende in Beurteilungsprozesse involvieren", "beurteilung.html", BEU_ART,
     ("downloads/beurteilung/Instrumente_Beurteilung", "Alle 8 Instrumente in einer Datei"),
     [("Kriterien-Werkstatt", "BE1_Kriterien-Werkstatt"),
      ("Qualitätensuche", "BE2_Qualitaetensuche"),
      ("Selbstbeurteilung nach einer grösseren Arbeit", "BE3_Selbstbeurteilung"),
      ("Peer-Feedback in sieben Schritten", "BE4_Peer-Feedback"),
      ("Portfolio-Planer", "BE5_Portfolio-Planer"),
      ("Rückmeldebogen Präsentation", "BE6_Rueckmeldebogen-Praesentation"),
      ("Lernkontrolle anpassen", "BE7_Lernkontrolle-anpassen"),
      ("Beurteilungs-Check", "BE8_Beurteilungs-Check")]),
    ("Umgang mit Konflikten, Gewalt und Mobbing", "konflikte.html", KON_ART,
     ("downloads/konflikte/Instrumente_Konflikte_Gewalt_Mobbing", "Alle 8 Instrumente in einer Datei"),
     [("Konflikt oder Mobbing? Einschätzungsbogen", "KO1_Konflikt-oder-Mobbing"),
      ("Beobachtungsprotokoll Gruppe und Pause", "KO2_Beobachtungsprotokoll"),
      ("Klassenregeln gegen Mobbing erarbeiten", "KO3_Klassenregeln"),
      ("No Blame Approach: Leitfaden", "KO4_No-Blame-Approach"),
      ("Interventionsplan bei Mobbing", "KO5_Interventionsplan"),
      ("Elterngespräch bei Mobbing vorbereiten", "KO6_Elterngespraech"),
      ("Cybermobbing: Was ich tun kann", "KO7_Cybermobbing-Lernende"),
      ("Klassen-Check gegen Mobbing", "KO8_Klassen-Check")]),
]
def instr_kachel(titel, href, art, alle, liste):
    ordner = href.replace(".html", "").replace("lernbegleitung", "lernbegleitung")
    if liste:
        dl = ordner if ordner != "lernanalyse" else "lernanalyse"
        items = "".join(
            f'<li><span>{name}</span><span class="dl"><a href="downloads/{dl}/{datei}.docx" download>Word</a><a href="downloads/{dl}/{datei}.pdf" target="_blank" rel="noopener">PDF</a></span></li>'
            for name, datei in liste)
        alle_html = (f'<div class="instr-alle"><span>{alle[1]}</span><span class="dl"><a href="{alle[0]}.docx" download>Word</a>'
                     f'<a href="{alle[0]}.pdf" target="_blank" rel="noopener">PDF</a></span></div>')
        inhalt = f'<ul class="instr-liste" tabindex="0" aria-label="Instrumente: {titel}">{items}</ul>{alle_html}'
        badge = f'<span class="badge live">{len(liste)} Instrumente</span>'
    else:
        inhalt = '<p class="instr-leer">Die Instrumente zu diesem Thema sind in Vorbereitung. Bis dahin findest du Werkzeuge und einen Planungs-Check direkt auf der Themenseite.</p>'
        badge = '<span class="badge">In Vorbereitung</span>'
    return (f'      <div class="plan thema instr"><div class="thema-art">{art}</div>{badge}<h3>{titel}</h3>{inhalt}'
            f'<a class="go" href="{href}">Zum Thema →</a></div>')
page("instrumente.html", "Instrumente – MuggliOnline", f"""<main class="wrap">
{hero('<a href="didaktik.html">Pädagogik</a> › Instrumente', "Pädagogik", "Instrumente", "Raster, Bögen und Leitfäden für Praktikum und Unterricht, gratis zum Herunterladen.")}
  <section class="section">
{einleitung("Frei nutzbar", ["Die Instrumente sind nach Handlungskompetenz geordnet. Jede Kachel gehört zu einem Thema auf der Pädagogik-Seite, wo die Theorie dazu erklärt ist.", "Alle Instrumente dürfen gratis heruntergeladen, genutzt und für den eigenen Unterricht angepasst werden, als bearbeitbare Word-Datei oder als PDF zum Ausdrucken. Ich freue mich über einen Hinweis auf die Quelle mugglionline.ch."], 2)}
    <div class="grid3 instr-grid">
{chr(10).join(instr_kachel(*k) for k in INSTRUMENTE)}
    </div>
  </section>
</main>""", active="didaktik.html", description="Gratis Instrumente für Praktikum und Unterricht, geordnet nach Handlungskompetenz: Lernprozesse begleiten, Lernvoraussetzungen berücksichtigen, Lernen analysieren, Lerngespräche führen, Lernen und Digitalität, Beurteilung sowie Konflikte, Gewalt und Mobbing.")

# ---------------- Lernende: Klassen ----------------
EXAM_ART = ('<svg viewBox="0 0 220 120" aria-hidden="true"><path d="M0 120 L0 98 L60 82 L110 96 L170 76 L220 90 L220 120 Z" fill="#cfdacd"/>'
    '<rect x="70" y="10" width="80" height="100" rx="6" fill="#fff" stroke="#3f5d4a" stroke-width="2.5"/>'
    '<g stroke="#9fb3a5" stroke-width="3" stroke-linecap="round"><path d="M100 32 H136 M100 56 H136 M100 80 H128"/></g>'
    '<g fill="none" stroke="#a8682f" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M80 31 l5 5 l8 -10 M80 55 l5 5 l8 -10"/></g>'
    '<rect x="80" y="74" width="12" height="12" rx="2" fill="none" stroke="#3f5d4a" stroke-width="2.5"/>'
    '<g transform="rotate(35 172 70)"><rect x="166" y="36" width="10" height="50" rx="2" fill="#6f8f78"/><polygon points="166,86 176,86 171,97" fill="#2f4a39"/></g></svg>')
ENERGY_ART = ('<svg viewBox="0 0 220 120" aria-hidden="true"><path d="M0 120 L0 100 L50 86 L110 98 L170 80 L220 92 L220 120 Z" fill="#cfdacd"/>'
    '<g fill="#e7ebe7" stroke="#b8c2b9" stroke-width="1.5"><circle cx="78" cy="20" r="12"/><circle cx="94" cy="13" r="14"/><circle cx="111" cy="21" r="11"/></g>'
    '<path d="M68 104 Q80 70 72 34 H116 Q108 70 120 104 Z" fill="#fff" stroke="#3f5d4a" stroke-width="2.5"/>'
    '<rect x="132" y="66" width="48" height="38" rx="4" fill="#fff" stroke="#3f5d4a" stroke-width="2.5"/><path d="M144 66 Q156 46 168 66" fill="#fff" stroke="#3f5d4a" stroke-width="2.5"/>'
    '<g fill="none" stroke="#a8682f" stroke-width="2"><ellipse cx="156" cy="85" rx="12" ry="5"/><ellipse cx="156" cy="85" rx="12" ry="5" transform="rotate(60 156 85)"/><ellipse cx="156" cy="85" rx="12" ry="5" transform="rotate(-60 156 85)"/></g>'
    '<circle cx="156" cy="85" r="2.5" fill="#a8682f"/></svg>')
PRIMAR_ART = ('<svg viewBox="0 0 220 120" aria-hidden="true"><path d="M0 120 L0 100 L60 86 L120 98 L180 82 L220 94 L220 120 Z" fill="#cfdacd"/>'
    '<rect x="58" y="22" width="104" height="74" rx="6" fill="#3f5d4a"/><rect x="64" y="28" width="92" height="62" rx="3" fill="#4f7a5e"/>'
    '<g fill="none" stroke="#e9e3d6" stroke-width="2.5" stroke-linecap="round"><path d="M74 44 H112 M74 58 H128 M74 72 H104"/></g>'
    '<g transform="translate(128 60)"><rect x="0" y="0" width="7" height="18" fill="#2e7d4f"/><rect x="7" y="0" width="7" height="18" fill="#fff"/><rect x="14" y="0" width="7" height="18" fill="#b0392e"/></g>'
    '<path d="M100 96 L96 112 M120 96 L124 112" stroke="#3f5d4a" stroke-width="3"/>'
    '<g transform="rotate(35 178 70)"><rect x="172" y="40" width="9" height="44" rx="2" fill="#e0a526"/><polygon points="172,84 181,84 176.5,94" fill="#2f4a39"/></g></svg>')
GRAMMAR_ART = ('<svg viewBox="0 0 220 120" aria-hidden="true"><path d="M0 120 L0 102 L70 88 L140 100 L220 86 V120 Z" fill="#cfdacd"/>'
    '<rect x="28" y="20" width="96" height="62" rx="12" fill="#2f6f8f"/><path d="M54 82 L48 98 L70 82 Z" fill="#2f6f8f"/>'
    '<text x="76" y="59" text-anchor="middle" font-family="Georgia,serif" font-size="26" font-weight="700" fill="#fff">ABC</text>'
    '<rect x="134" y="40" width="74" height="48" rx="10" fill="#c9762b"/><path d="M186 88 L194 102 L172 88 Z" fill="#c9762b"/>'
    '<text x="171" y="71" text-anchor="middle" font-family="Georgia,serif" font-size="20" font-weight="700" fill="#fff">-ing</text></svg>')
KLASSEN = [
 f"""      <a class="plan thema entile" href="pomg25a-materials.html"><div class="thema-art">{EXAM_ART}</div><span class="badge live">Technical English</span><h3>PomG25A</h3>
        <p>Polymechanikerinnen und Polymechaniker, G-Modul, 2. Lehrjahr</p>
        <ul><li>Properties of Materials Exam: Practice Exercises to the Exam about Study Packet II</li></ul>
        <span class="go">Zur Probeprüfung →</span></a>""",
 f"""      <a class="plan thema entile" href="pome24b.html"><div class="thema-art">{ENERGY_ART}</div><span class="badge live">Technical English</span><h3>Pome24B</h3>
        <p>Polymechanikerinnen und Polymechaniker, E-Modul, 3. Lehrjahr</p>
        <ul><li>Energy and the Environment</li><li>Nuclear Energy: video and tasks</li><li>Practice for the Exam</li><li>Lernspiele: Power Town und Island Escape</li></ul>
        <span class="go">Zur Klassenseite →</span></a>""",
 f"""      <a class="plan thema entile" href="primar6.html"><div class="thema-art">{PRIMAR_ART}</div><span class="badge live">Primarschule</span><h3>6. Primarklasse</h3>
        <p>Übungen zu verschiedenen Fächern der 6. Primarstufe, mit Selbstkontrolle</p>
        <ul><li>Italiano Unità 4: Un nuovo compagno</li><li>Deutsch: die vier Fälle</li></ul>
        <span class="go">Zu den Übungen →</span></a>""",
 f"""      <a class="plan thema entile" href="english-grammar.html"><div class="thema-art">{GRAMMAR_ART}</div><span class="badge live">English</span><h3>English Grammar</h3>
        <p>Grammar notes and practice exercises with self-check</p>
        <ul><li>Present Simple vs. Present Continuous</li><li>Present Perfect vs. Past Simple</li></ul>
        <span class="go">To the grammar →</span></a>""",
]
ACTIVE["pomg25a-materials.html"] = "lernende.html"
POM_BODY = "".join((B / "pomg25a" / f).read_text() for f in sorted(p.name for p in (B / "pomg25a").glob("*.html")))
page("pomg25a-materials.html", "PomG25A: Properties of Materials Exam – MuggliOnline", f"""<main class="wrap">
{hero('<a href="lernende.html">Lernende</a> › PomG25A', "Probeprüfung · Technical English", "PomG25A: Properties of Materials Exam", "Practice Exercises to the Exam about Study Packet II (OneNote: 2. Properties of Materials)")}
  <section class="section">
<!--BODY:pomg25a-->{POM_BODY}<!--/BODY-->
  </section>
</main>""", active="lernende.html", description="Practice exercises for the Technical English exam Properties of Materials (PomG25A): fill in the blanks, matching, sorting, true or false, vocabulary, short answers and open-ended questions with model answers.")

ACTIVE["pome24b.html"] = "lernende.html"
page("pome24b.html", "Pome24B – MuggliOnline", f"""<main class="wrap">
{hero('<a href="lernende.html">Lernende</a> › Pome24B', "Technical English", "Pome24B", "Energy and the Environment")}
  <section class="section">
{einleitung("How to use this page", ["This is the page for the class Pome24B. Each tile below belongs to one part of the unit “Energy and the Environment”. Click a tile to open it. Work through the parts in the order your teacher tells you.", "On each page you will find tasks that you can do directly in your browser, also on your phone. Your answers are saved on your device. When you have finished, click “Check my answers” and compare your answers with the solutions."], 0)}
    <div class="grid2 themen">
      <a class="plan thema entile" href="pome24b-nuclear.html"><div class="thema-art">{ENERGY_ART}</div><span class="badge live">Unit 9</span><h3>Nuclear Energy</h3>
        <p>Gap-fill text in the book, a video about how a nuclear power plant works, and tasks with model answers.</p>
        <span class="go">Open →</span></a>
      <a class="plan thema entile" href="pome24b-exam.html"><div class="thema-art">{EXAM_ART}</div><span class="badge live">Unit 9 Practice Exercises</span><h3>Energy and the Environment</h3>
        <p>Practice exercises to the entire Unit 9 as preparation for the exam: eight sections with labelling, gap-fill texts, statistics and critical-thinking questions, each with its own answer check.</p>
        <span class="go">Open →</span></a>
      <a class="plan thema entile" href="pome24b-power-town.html"><div class="thema-art bild"><img src="img/pome24b/games/pt-tile.jpg" alt="" loading="lazy"></div><span class="badge live">Unit 9 Review Game</span><h3>Power Town</h3>
        <p>A board game for 1 to 4 players or teams: buy solar, wind, hydro and nuclear plants, answer questions about the whole unit and keep the climate meter low until 2050.</p>
        <span class="go">Play →</span></a>
      <a class="plan thema entile" href="pome24b-island-escape.html"><div class="thema-art bild"><img src="img/pome24b/games/ie-tile.jpg" alt="" loading="lazy"></div><span class="badge live">Unit 9 Review Game</span><h3>Island Escape</h3>
        <p>An escape game for your team: after a storm, Mira Island is dark. Solve the puzzles in four rooms and switch the island back on before the time runs out.</p>
        <span class="go">Play →</span></a>
    </div>
  </section>
</main>""", active="lernende.html", description="Pome24B, Technical English: Energy and the Environment, nuclear energy and practice for the exam.")

ACTIVE["pome24b-nuclear.html"] = "lernende.html"
PE_BODY = "".join((B / "pome24b" / f).read_text() for f in sorted(p.name for p in (B / "pome24b").glob("*.html")))
page("pome24b-nuclear.html", "Pome24B: Nuclear Energy – MuggliOnline", f"""<main class="wrap">
{hero('<a href="lernende.html">Lernende</a> › <a href="pome24b.html">Pome24B</a> › Nuclear Energy', "Pome24B · Energy and the Environment", "Nuclear Energy", "How does a nuclear power plant produce electricity? A gap-fill text, a video and tasks to practise the technical vocabulary.")}
  <section class="section">
{einleitung("How to use this page", ["Work through the page from top to bottom: first the gap-fill text in your book, then the video, then the tasks A to F. You can watch the video here or scan the QR code to watch it on your phone. Pause it as often as you need.", "Drag the words into the right places (on a phone: tap a word, then tap the place) and answer the questions in complete sentences. Your answers are saved in this browser. At the bottom, click “Check my answers” to see your result and the model answers."], 0)}
<!--BODY:pome24b-->{PE_BODY}<!--/BODY-->
  </section>
</main>""", active="lernende.html", description="Pome24B, Energy and the Environment: nuclear energy, with a video and interactive tasks with model answers.")

ACTIVE["pome24b-exam.html"] = "lernende.html"
PX_BODY = "".join((B / "pome24b_exam" / f).read_text() for f in sorted(p.name for p in (B / "pome24b_exam").glob("*.html")))
page("pome24b-exam.html", "Pome24B: Unit 9 Practice Exercises – MuggliOnline", f"""<main class="wrap">
{hero('<a href="lernende.html">Lernende</a> › <a href="pome24b.html">Pome24B</a> › Practice Exercises', "Pome24B · Energy and the Environment", "Practice Exercises: Energy and the Environment", "Practice exercises to the entire Unit 9 as preparation for the exam: greenhouse effect, sea levels, solar, water, wind and nuclear power, statistics and the island project, section by section.")}
  <section class="section">
<!--BODY:pome24b_exam-->{PX_BODY}<!--/BODY-->
  </section>
</main>""", active="lernende.html", description="Pome24B, Technical English: Unit 9 practice exercises (Energy and the Environment) as preparation for the exam, with labelling tasks, gap-fill texts, charts to interpret and critical-thinking questions with model answers.")

ACTIVE["pome24b-power-town.html"] = "lernende.html"
PT_BODY = "".join((B / "powertown" / f).read_text() for f in sorted(p.name for p in (B / "powertown").glob("*.html")))
page("pome24b-power-town.html", "Pome24B: Power Town – MuggliOnline", f"""<main class="wrap">
{hero('<a href="lernende.html">Lernende</a> › <a href="pome24b.html">Pome24B</a> › Power Town', "Pome24B · Unit 9 Review Game", "Power Town", "A board game about energy and the environment: build a clean energy supply for your town by 2050.")}
  <section class="section">
<!--BODY:powertown-->{PT_BODY}<!--/BODY-->
  </section>
</main>""", active="lernende.html", description="Power Town: a board game for Pome24B to review Unit 9 Energy and the Environment, with questions on the greenhouse effect, sea levels, solar, water, wind and nuclear power and statistics.")

ACTIVE["pome24b-island-escape.html"] = "lernende.html"
IE_BODY = "".join((B / "islandescape" / f).read_text() for f in sorted(p.name for p in (B / "islandescape").glob("*.html")))
page("pome24b-island-escape.html", "Pome24B: Island Escape – MuggliOnline", f"""<main class="wrap">
{hero('<a href="lernende.html">Lernende</a> › <a href="pome24b.html">Pome24B</a> › Island Escape', "Pome24B · Unit 9 Review Game", "Island Escape", "An escape game: solve four energy puzzles and switch Mira Island back on.")}
  <section class="section">
<!--BODY:islandescape-->{IE_BODY}<!--/BODY-->
  </section>
</main>""", active="lernende.html", description="Island Escape: an escape game for Pome24B to review Unit 9 Energy and the Environment, with puzzles on the greenhouse effect, sea levels, energy conversion, nuclear power and the island project.")

ACTIVE["lindenhof.html"] = "werkstatt.html"
LH_BODY = "".join((B / "lindenhof" / f).read_text() for f in sorted(p.name for p in (B / "lindenhof").glob("*.html")))
page("lindenhof.html", "Schulhaus Lindenhof – App-Werkstatt – MuggliOnline", f"""<main class="wrap">
{hero('<a href="werkstatt.html">App-Werkstatt</a> › Schulhaus Lindenhof', "Lernspiel · Konflikte, Gewalt und Mobbing", "Schulhaus Lindenhof", "Ein kooperatives Brettspiel für angehende Lehrpersonen in Zyklus 1 und 2: würfeln, ziehen, Fälle rechtzeitig erreichen und gemeinsam entscheiden, mit Theorie bei jedem Zug. Zur <a href=\"konflikte.html\" style=\"text-decoration:underline;color:inherit;font-weight:600\">Themenseite</a>.")}
  <section class="section">
<!--BODY:lindenhof-->{LH_BODY}<!--/BODY-->
  </section>
</main>""", active="werkstatt.html", description="Schulhaus Lindenhof: ein kooperatives Brettspiel zu Konflikten, Gewalt und Mobbing in Zyklus 1 und 2, mit Wissenskarten und Theorie aus der Fachliteratur.")

ACTIVE["power-town.html"] = "werkstatt.html"
PTDE_BODY = "".join((B / "powertown_de" / f).read_text() for f in sorted(p.name for p in (B / "powertown_de").glob("*.html")))
page("power-town.html", "Power Town – App-Werkstatt – MuggliOnline", f"""<main class="wrap">
{hero('<a href="werkstatt.html">App-Werkstatt</a> › Power Town', "Lernspiel · Energie und Umwelt", "Power Town", "Ein Brettspiel zu Energie und Umwelt: Baut für eure Stadt bis 2050 eine saubere Energieversorgung auf. <a href=\"pome24b-power-town.html\" style=\"text-decoration:underline;color:inherit;font-weight:600\">English version →</a>")}
  <section class="section">
<!--BODY:powertown_de-->{PTDE_BODY}<!--/BODY-->
  </section>
</main>""", active="werkstatt.html", description="Power Town: ein Brettspiel zu Energie und Umwelt mit Fragen zu Treibhauseffekt, Meeresspiegel, Solar-, Wasser-, Wind- und Kernenergie sowie Statistik.")

ACTIVE["island-escape.html"] = "werkstatt.html"
IEDE_BODY = "".join((B / "islandescape_de" / f).read_text() for f in sorted(p.name for p in (B / "islandescape_de").glob("*.html")))
page("island-escape.html", "Island Escape – App-Werkstatt – MuggliOnline", f"""<main class="wrap">
{hero('<a href="werkstatt.html">App-Werkstatt</a> › Island Escape', "Lernspiel · Energie und Umwelt", "Island Escape", "Ein Escape-Game: Löst vier Energierätsel und schaltet die Insel Mira wieder ein. <a href=\"pome24b-island-escape.html\" style=\"text-decoration:underline;color:inherit;font-weight:600\">English version →</a>")}
  <section class="section">
<!--BODY:islandescape_de-->{IEDE_BODY}<!--/BODY-->
  </section>
</main>""", active="werkstatt.html", description="Island Escape: ein Escape-Game zu Energie und Umwelt mit Rätseln zu Treibhauseffekt, Meeresspiegel, Energieumwandlung und Kernenergie.")

ACTIVE["primar6.html"] = "lernende.html"
page("primar6.html", "6. Primarklasse – MuggliOnline", f"""<main class="wrap">
{hero('<a href="lernende.html">Lernende</a> › 6. Primarklasse', "Primarschule", "6. Primarklasse", "Übungsaufgaben zu Fächern der 6. Primarstufe")}
  <section class="section">
{einleitung("So funktioniert diese Seite", ["Diese Seite enthält Übungsaufgaben zu verschiedenen Fächern der 6. Primarstufe. Die Übungen sind nach Fach und Thema eingeordnet: Jede Kachel gehört zu einem Thema aus dem Unterricht.", "Wenn du eine Kachel anklickst, gelangst du zu den Übungen. Du kannst sie direkt im Browser lösen, auch auf dem Handy. Am Ende jedes Abschnitts kontrollierst du deine Antworten selbst: Du siehst sofort, was richtig ist, und kannst deine Fehler verbessern."], 0)}
    <div class="grid2 themen">
      <a class="plan thema entile" href="primar6-italiano-4.html"><div class="thema-art">{PRIMAR_ART}</div><span class="badge live">Italienisch</span><h3>Italiano Unità 4</h3>
        <p>Un nuovo compagno: Personen beschreiben, die Schule, «Di chi è?», Verben und Aussprache. Drei Abschnitte mit Selbstkontrolle als Vorbereitung auf die Prüfung.</p>
        <span class="go">Zu den Übungen →</span></a>
      <a class="plan thema entile" href="primar6-deutsch-faelle.html"><div class="thema-art">{EXAM_ART}</div><span class="badge live">Deutsch</span><h3>Deutsch: die vier Fälle</h3>
        <p>Probeprüfung in vier Abschnitten: die Namen der Fälle, Fallfehler finden und verbessern, Fragewörter und Ersatzprobe, Fälle im Text bestimmen.</p>
        <span class="go">Zu den Übungen →</span></a>
    </div>
  </section>
</main>""", active="lernende.html", description="6. Primarklasse: Übungsaufgaben nach Fach und Thema, mit Selbstkontrolle.")

ACTIVE["primar6-deutsch-faelle.html"] = "lernende.html"
DF_BODY = "".join((B / "primar6_de_faelle" / f).read_text() for f in sorted(p.name for p in (B / "primar6_de_faelle").glob("*.html")))
page("primar6-deutsch-faelle.html", "Deutsch: die vier Fälle – MuggliOnline", f"""<main class="wrap">
{hero('<a href="lernende.html">Lernende</a> › <a href="primar6.html">6. Primarklasse</a> › Deutsch: die vier Fälle', "6. Primarklasse · Deutsch", "Deutsch: die vier Fälle", "Probeprüfung als Vorbereitung auf die Prüfung: Nominativ, Akkusativ, Dativ und Genitiv erkennen, bestimmen und richtig anwenden.")}
  <section class="section">
<!--BODY:primar6_de_faelle-->{DF_BODY}<!--/BODY-->
  </section>
</main>""", active="lernende.html", description="Deutsch 6. Primarklasse: Probeprüfung zu den vier Fällen mit Fallproben, Fehlersätzen und Selbstkontrolle.")

ACTIVE["primar6-italiano-4.html"] = "lernende.html"
IT4_BODY = "".join((B / "primar6_ital4" / f).read_text() for f in sorted(p.name for p in (B / "primar6_ital4").glob("*.html")))
page("primar6-italiano-4.html", "Italiano Unità 4: Un nuovo compagno – MuggliOnline", f"""<main class="wrap">
{hero('<a href="lernende.html">Lernende</a> › <a href="primar6.html">6. Primarklasse</a> › Italiano Unità 4', "6. Primarklasse · Italienisch", "Italiano Unità 4: Un nuovo compagno", "Übungen zur ganzen Unità 4 als Vorbereitung auf die Prüfung: Personen beschreiben, die Schule, Possessivpronomen, Verben und Aussprache.")}
  <section class="section">
<!--BODY:primar6_ital4-->{IT4_BODY}<!--/BODY-->
  </section>
</main>""", active="lernende.html", description="Italienisch 6. Primarklasse, Unità 4 «Un nuovo compagno»: interaktive Übungen mit Selbstkontrolle.")

ACTIVE["english-grammar.html"] = "lernende.html"
page("english-grammar.html", "English Grammar – MuggliOnline", f"""<main class="wrap">
{hero('<a href="lernende.html">Lernende</a> › English Grammar', "Technical English", "English Grammar", "Grammar notes and practice exercises with self-check")}
  <section class="section">
{einleitung("How to use this page", ["Each tile covers one grammar topic. On every topic page, you first find the grammar notes: the rules with examples, the signal words and how to form the tenses.", "Below the notes, you practise: write the correct verb form into each box. At the end, click «Check my answers». You see at once which answers are correct, and for every gap you get the correct form and a short reason."], 0)}
    <div class="grid2 themen">
      <a class="plan thema entile" href="english-grammar-present.html"><div class="thema-art">{GRAMMAR_ART}</div><span class="badge live">Tenses</span><h3>Present Simple vs. Present Continuous</h3>
        <p>Habits and facts or happening right now? Grammar notes, signal words, stative verbs and 20 practice sentences.</p>
        <span class="go">Open →</span></a>
      <a class="plan thema entile" href="english-grammar-past.html"><div class="thema-art">{GRAMMAR_ART}</div><span class="badge live">Tenses</span><h3>Present Perfect vs. Past Simple</h3>
        <p>Finished or connected to now? Grammar notes, signal words and 20 practice sentences.</p>
        <span class="go">Open →</span></a>
    </div>
  </section>
</main>""", active="lernende.html", description="English Grammar: grammar notes and practice exercises with self-check.")

for _f, _d, _t, _lead, _desc in [
    ("english-grammar-present.html", "eng_present", "Present Simple vs. Present Continuous", "Habits, facts and timetables or actions happening right now: the rules, signal words and 20 practice sentences with self-check.", "English Grammar: Present Simple vs. Present Continuous – grammar notes and practice exercises with self-check."),
    ("english-grammar-past.html", "eng_past", "Present Perfect vs. Past Simple", "Finished in the past or connected to now: the rules, signal words and 20 practice sentences with self-check.", "English Grammar: Present Perfect vs. Past Simple – grammar notes and practice exercises with self-check.")]:
    ACTIVE[_f] = "lernende.html"
    _body = "".join((B / _d / f).read_text() for f in sorted(p.name for p in (B / _d).glob("*.html")))
    page(_f, f"{_t} – MuggliOnline", f"""<main class="wrap">
{hero('<a href="lernende.html">Lernende</a> › <a href="english-grammar.html">English Grammar</a> › ' + _t, "English Grammar", _t, _lead)}
  <section class="section">
{einleitung("How to use this page", ["First read the grammar notes: the rules with examples, the signal words and how to form the tenses.", "Then do the practice exercise below. Write the correct verb form into each box and click «Check my answers» at the end. Your answers are saved in this browser."], 0)}
<!--BODY:{_d}-->{_body}<!--/BODY-->
  </section>
</main>""", active="lernende.html", description=_desc)

area("lernende.html", "Lernende", "",
     "Lernende",
     "Übungen, Probeprüfungen und Material für meine Klassen, mit Lösungen zum selbstständigen Lernen.",
     "",
     KLASSEN,
     cols="grid2 themen",
     bar=("Deine Klasse", ["Hier findest du eine Kachel für jede Klasse. Wähle deine Klasse aus: Dort findest du Übungen, Videos und Probeprüfungen zum aktuellen Thema.",
          "Zu allen Übungen gibt es Lösungen. So kannst du selbst überprüfen, wo du stehst, und gezielt weiterüben."], 0))

# ---------------- App-Werkstatt ----------------
page("werkstatt.html", "App-Werkstatt – MuggliOnline", f"""<main class="wrap">
{hero("App-Werkstatt", "", "App-Werkstatt", "Kleine Web-Apps für Schule und Alltag. Gerne erstelle ich auch individuelle Apps für deinen Unterricht! Einfach Kontakt aufnehmen :)")}
  <section class="section">
{einleitung("Apps für Schule und Alltag", ["Die Apps laufen direkt im Browser, ohne Installation und ohne Anmeldung.", "Einzelne Apps werden künftig KI nutzen und sind dann passwortgeschützt. Du hast eine Idee für eine eigene App? Ich setze sie gerne für deinen Unterricht um."], 0)}
    <div class="cards">
      <a class="card" href="lindenhof.html">
        <div class="art foto"><img src="img/lindenhof/lh-tile.jpg" alt="" loading="lazy"></div>
        <div class="body">
          <div class="kicker"><span class="badge live">Lernspiel</span></div>
          <h3>Schulhaus Lindenhof</h3>
          <p>Ein kooperatives Brettspiel zu Konflikten, Gewalt und Mobbing für 1 bis 4 Spielende an einem Gerät. Alle sind Lehrpersonen im selben Schulhaus, vom Kindergarten bis zur 6. Klasse, und ziehen mit ihren Figuren über das Brett. Fälle tauchen als Marker auf und müssen rechtzeitig erreicht werden. Jeder Entscheid verändert den Verlauf, und nach jedem Zug zeigt ein Theorie-Kärtchen, was die Forschung dazu sagt, mit Link zur Themenseite und zu den Instrumenten.</p>
          <p><b>Einsatz:</b> Lehrpersonenbildung für Zyklus 1 und 2 (Module Erziehungswissenschaften, Praktikumsvorbereitung), Weiterbildungen in Schulteams und Fallbesprechungen in Kollegien. Mit Auswertung und Fragen für die Nachbesprechung.</p>
          <div class="tags"><span>1–4 Personen</span><span>45–80 Min.</span><span>Zyklus 1 und 2</span><span>Spielsprache Deutsch</span></div>
          <span class="go">Spiel öffnen →</span>
        </div>
      </a>
      <a class="card" href="power-town.html">
        <div class="art foto"><img src="img/pome24b/games/pt-tile.jpg" alt="" loading="lazy"></div>
        <div class="body">
          <div class="kicker"><span class="badge live">Lernspiel</span></div>
          <h3>Power Town</h3>
          <p>Ein Brettspiel zu Energie und Umwelt für 1 bis 4 Spielende oder Teams an einem Gerät. Die Lernenden führen als Gemeindepräsidien eine Stadt bis 2050 zu einer sauberen Energieversorgung: Wer ein Solar-, Wind-, Wasser- oder Kernkraftwerk kaufen will, beantwortet zuerst eine Frage. Ereigniskarten, Statistikfelder und ein gemeinsames Klimabarometer sorgen für Spannung.</p>
          <p><b>Einsatz:</b> Sekundarstufe I (Zyklus 3) in Natur und Technik oder Geografie, Berufsfachschule (Fachkunde, ABU) und mit der englischen Version auch im Englischunterricht ab Niveau A2/B1 sowie Gymnasium (Geografie, Physik), etwa zur Repetition vor einer Prüfung.</p>
          <div class="tags"><span>1–4 Teams</span><span>20–50 Min.</span><span>Spielsprache Deutsch</span><span>auch auf Englisch</span></div>
          <p class="vermerk">Ursprünglich erstellt für den Technical-English-Unterricht an der Berufsschule.</p>
          <span class="go">Spiel öffnen →</span>
        </div>
      </a>
      <a class="card" href="island-escape.html">
        <div class="art foto"><img src="img/pome24b/games/ie-tile.jpg" alt="" loading="lazy"></div>
        <div class="body">
          <div class="kicker"><span class="badge live">Lernspiel</span></div>
          <h3>Island Escape</h3>
          <p>Ein Escape-Game für Teams: Nach einem Sturm ist die Insel Mira dunkel. In vier Räumen lösen die Lernenden Rätsel zum Treibhauseffekt, zum Meeresspiegel, zur Energieumwandlung und zur Kernenergie, finden Codes und schalten den Strom wieder ein. Zeitlimit wählbar, mit Hinweisen, Strafminuten und einer Bestenliste.</p>
          <p><b>Einsatz:</b> Sekundarstufe I ab der 8. Klasse in Natur und Technik, Physik oder Geografie, Berufsfachschule und Gymnasium, mit der englischen Version auch im Englischunterricht ab Niveau B1, als Repetition, Postenarbeit oder Abschluss einer Unterrichtseinheit.</p>
          <div class="tags"><span>Teams</span><span>20–45 Min.</span><span>Spielsprache Deutsch</span><span>auch auf Englisch</span></div>
          <p class="vermerk">Ursprünglich erstellt für den Technical-English-Unterricht an der Berufsschule.</p>
          <span class="go">Spiel öffnen →</span>
        </div>
      </a>
      <a class="card wide" href="bullet-journal.html">
        <div class="art">
          <svg viewBox="0 0 220 140" aria-hidden="true">
            <path d="M0,140 L0,112 L70,92 L120,108 L180,86 L220,100 L220,140 Z" fill="#cfdacd"/>
            <rect x="66" y="34" width="72" height="96" rx="6" fill="#3f5d4a"/>
            <rect x="74" y="42" width="58" height="80" rx="3" fill="#e9e3d6"/>
            <g fill="#3f5d4a"><circle cx="66" cy="48" r="3.5"/><circle cx="66" cy="64" r="3.5"/><circle cx="66" cy="80" r="3.5"/><circle cx="66" cy="96" r="3.5"/><circle cx="66" cy="112" r="3.5"/></g>
            <g fill="#9fb3a5">{''.join(f'<circle cx="{x}" cy="{y}" r="1.3"/>' for x in range(82, 130, 8) for y in range(52, 118, 8))}</g>
            <g transform="rotate(35 160 112)"><rect x="150" y="84" width="10" height="44" rx="2" fill="#6f8f78"/><polygon points="150,128 160,128 155,138" fill="#2f4a39"/></g>
          </svg>
        </div>
        <div class="body">
          <div class="kicker"><span class="badge live">Verfügbar</span></div>
          <h3>Bullet-Journal-Generator</h3>
          <p>Erstelle druckfertige A5-Seiten für dein Bullet Journal: Tagesplaner, Wochen- und Monatsübersicht oder Habit-Tracker, mit Punkten, Kästchen oder Linien. Dazu kommt eine Bibliothek mit 27 fertig gestalteten Vorlagen zum Drucken oder Herunterladen.</p>
          <div class="tags"><span>A5</span><span>Druckfertig</span><span>31 Vorlagen</span><span>Bald mit KI</span></div>
          <span class="go">App öffnen →</span>
        </div>
      </a>
    </div>
    <div class="grid2" style="margin-top:-56px">
      <div class="plan" style="border-style:solid"><span class="badge live">Auf Anfrage</span><h3>Individuelle Apps</h3><p>Du hast eine Idee für eine App für deinen Unterricht? Ich erstelle gerne individuelle Apps, die genau zu deiner Klasse passen.</p><p style="margin-top:14px"><a class="btn green" href="kontakt.html">Kontakt aufnehmen</a></p></div>
{plan("KI-Funktionen", "Apps mit KI werden mit einem Passwort geschützt, damit nur berechtigte Personen sie nutzen können.", badge="Bald")}
    </div>
  </section>
</main>""", active="werkstatt.html", description="Kleine Web-Apps für Schule und Alltag.")

# ---------------- Bullet-Journal-Generator ----------------
import json
VORLAGEN_JSON = json.dumps(json.loads((B / "vorlagen.json").read_text()), ensure_ascii=False)
page("bullet-journal.html", "Bullet-Journal-Generator – MuggliOnline", f"""<main class="wrap">
{hero('<a href="werkstatt.html">App-Werkstatt</a> › Bullet-Journal-Generator', "App-Werkstatt", "Bullet-Journal-Generator", "Stelle deine Seite zusammen, schau sie dir in der Vorschau an und drucke sie in A5 aus oder speichere sie als PDF.")}
  <section class="section">
    <div class="bj">
      <div class="panel">
        <h3>Seite gestalten</h3>
        <div class="field"><label>Seitentyp</label>
          <div class="seg" id="bj-layout">
            <button class="on" data-v="tag">Tagesplaner</button><button data-v="woche">Woche</button><button data-v="monat">Monat</button><button data-v="habits">Habit-Tracker</button><button data-v="leer">Leere Seite</button>
          </div>
        </div>
        <div class="field row" id="bj-monatwahl" style="display:none">
          <div><label for="bj-monat">Monat</label><select id="bj-monat"></select></div>
          <div><label for="bj-jahr">Jahr</label><input id="bj-jahr" type="number" min="2020" max="2100"></div>
        </div>
        <div class="field"><label>Raster</label>
          <div class="seg" id="bj-raster">
            <button class="on" data-v="punkte">Punkte</button><button data-v="kaestchen">Kästchen</button><button data-v="linien">Linien</button><button data-v="ohne">Ohne</button>
          </div>
        </div>
        <div class="field"><label for="bj-abstand">Rasterabstand</label>
          <select id="bj-abstand"><option value="4">4 mm</option><option value="5" selected>5 mm</option><option value="6">6 mm</option></select>
        </div>
        <div class="field"><label for="bj-titel">Titel (optional)</label><input id="bj-titel" type="text" maxlength="40" placeholder="z. B. Montag oder Lernplan"></div>
        <div class="field"><label>Akzentfarbe</label>
          <div class="seg" id="bj-farbe">
            <button class="on" data-v="#3f5d4a">Tannengrün</button><button data-v="#8a6d3b">Sand</button><button data-v="#4a5568">Schiefer</button><button data-v="#9b4d5e">Beere</button>
          </div>
        </div>
        <div class="field locked"><label>KI-Motiv zum Nachzeichnen <span class="lock">🔒 folgt</span></label>
          <textarea disabled placeholder="Beschreibe ein Motiv, z. B. «Steinbock auf einem Berggipfel». Diese Funktion wird später mit KI ergänzt und ist dann passwortgeschützt."></textarea>
        </div>
      </div>
      <div class="preview">
        <svg id="sheet" viewBox="0 0 148 210" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Vorschau der A5-Seite"></svg>
        <div class="actions">
          <button class="btn green" id="bj-drucken" type="button">Drucken / als PDF speichern</button>
        </div>
        <small>Tipp: Im Druckdialog «Papierformat A5» und «Ränder: keine» wählen.</small>
      </div>
    </div>
  </section>
  <section class="section" id="vorlagen">
    <h2>Vorlagen-Bibliothek</h2>
    <p class="intro">Fertig gestaltete Seiten zum Ausdrucken: Notizseiten, Agenda-Seiten für Woche und Monat, To-do-Listen und illustrierte Seiten. Klicke auf eine Vorlage, um sie gross anzusehen, zu drucken oder als PDF herunterzuladen. Alle Vorlagen sind im Format A5.</p>
    <div class="filter" id="filter">
      <button class="alle on" data-f="alle">Alle</button>
      <button data-f="To-do" style="--chip:#e1efe8">To-do-Listen</button>
      <button data-f="Notizen" style="--chip:#f4ece2">Notizen</button>
      <button data-f="Agenda" style="--chip:#ebe7f6">Agenda</button>
      <button data-f="1 Feld" style="--chip:#e3ecf4">1 Feld</button>
      <button data-f="2 Felder" style="--chip:#f6e6ea">2 Felder</button>
      <button data-f="3 Felder" style="--chip:#e7f0e3">3 Felder</button>
      <button data-f="4 Felder" style="--chip:#fbe9df">4 Felder</button>
    </div>
    <div class="lib" id="lib"></div>
  </section>
  <div class="modal" id="modal" role="dialog" aria-modal="true" aria-labelledby="m-titel">
    <div class="box">
      <button class="x" id="m-x" type="button" aria-label="Schliessen">×</button>
      <img id="m-bild" src="" alt="">
      <div>
        <span class="badge live">Vorlage</span>
        <h3 id="m-titel"></h3>
        <p id="m-kat"></p>
        <div class="acts">
          <button class="btn green" id="m-drucken" type="button">Drucken</button>
          <a class="btn outline" id="m-pdf" href="#" download>PDF herunterladen</a>
        </div>
        <p style="margin-top:16px;font-size:13.5px">Tipp: Im Druckdialog «Papierformat A5» und «Ränder: keine» wählen. Auf A4 gedruckt wird die Seite automatisch verkleinert.</p>
        <div class="nav2"><button id="m-zur" type="button">← Vorherige</button><button id="m-vor" type="button">Nächste →</button></div>
      </div>
    </div>
  </div>
  <div id="pv-print" aria-hidden="true"></div>
  <script type="application/json" id="vorlagen-daten">{VORLAGEN_JSON}</script>
  <section class="section" style="margin-top:0">
    <div class="note"><span>✨</span><span><b>Was noch kommt:</b> KI-Motive zum Nachzeichnen und das Speichern deiner Lieblingseinstellungen. Diese Funktionen werden passwortgeschützt.</span></div>
  </section>
</main>
<!--I18N-->
<script src="bullet-journal.js?v={JS_V['bullet-journal.js']}"></script>
<script src="vorlagen.js?v={JS_V['vorlagen.js']}"></script>""", active="werkstatt.html", description="Druckfertige A5-Seiten für das Bullet Journal erstellen.")

# ---------------- Vision ----------------
VISION = [
    ("Lernen verstehen", [
        "Wie lernen Menschen? Was weckt ihre Neugier, was hilft ihnen weiter und wo entstehen Hindernisse? Diese Fragen stehen im Zentrum meiner Arbeit. Ich möchte Lernprozesse besser verstehen und dieses Wissen für Lehrpersonen und Lernende zugänglich machen.",
        "Dabei verbinde ich Erkenntnisse aus den Erziehungswissenschaften mit Erfahrungen aus dem Unterricht. So entstehen Materialien und Impulse, die Lehrpersonen sowie Lernenden helfen können, Lernwege zu erkennen, Schwierigkeiten einzuordnen und passende nächste Schritte zu finden."]),
    ("Lehren gestalten", [
        "Lehren bedeutet für mich, Bedingungen zu schaffen, unter denen Menschen lernen und sich entwickeln können. Dazu gehören klare Ziele, anregende Aufgaben, hilfreiche Rückmeldungen und eine vertrauensvolle Beziehung.",
        "Mit MuggliOnline möchte ich Lehrpersonen dabei unterstützen, Unterricht bewusst und fundiert zu gestalten. Ich teile Materialien, didaktische Hilfsmittel und Ideen, die sich an unterschiedliche Lerngruppen anpassen lassen und Raum für eigene Wege bieten."]),
    ("Zukunft mitprägen", [
        "Bildung eröffnet Möglichkeiten, das eigene Leben und unsere Gesellschaft mitzugestalten. Ich möchte Lernende darin stärken, selbstständig zu denken, Fragen zu stellen, unterschiedliche Perspektiven zu prüfen und Verantwortung zu übernehmen. Dazu gehört für mich auch ein neugieriger und reflektierter Umgang mit digitalen Werkzeugen und künstlicher Intelligenz.",
        "Gleichzeitig möchte ich Lernende bei den Anforderungen unterstützen, denen sie im Schulalltag begegnen. Deshalb bietet MuggliOnline auch Lernübungen und Probeprüfungen zur Vorbereitung auf klassische Prüfungen. Diese gehören zu unserem Schulsystem, auch wenn sie aus meiner Sicht die vielfältigen Kompetenzen und Potenziale von Lernenden nur begrenzt abbilden. Mein Anliegen ist es, Lernenden Sicherheit für diese Prüfungen zu geben und zugleich ihr Vertrauen in die eigenen Fähigkeiten über einzelne Noten hinaus zu stärken."]),
]
rows = "\n".join(
    f'''    <article class="vrow">{silhouette(i)}<div class="vhead"><h2>{titel}</h2></div><div class="vtext">{"".join(f"<p>{p}</p>" for p in absaetze)}</div></article>'''
    for i, (titel, absaetze) in enumerate(VISION))
page("vision.html", "Vision – MuggliOnline", f"""<main class="wrap">
{hero("Vision", "Meine Vision", "Vision", "Lernen verstehen, Lehren gestalten, Zukunft mitprägen. Was ich mit MuggliOnline erreichen möchte.")}
  <section class="section vision">
{rows}
  </section>
</main>""", active="vision.html", description="Lernen verstehen, Lehren gestalten, Zukunft mitprägen: die Vision hinter MuggliOnline.")

# ---------------- Über Anja ----------------
page("ueber-anja.html", "Über Anja – MuggliOnline", f"""<main class="wrap">
{hero("Über Anja", "", "Dr. Anja Muggli", "Dozentin Erziehungswissenschaften · Englischlehrperson")}
  <section class="section">
    <div class="about">
      <div class="photo"><img src="foto-anja.jpg" alt="Porträt von Dr. Anja Muggli" width="560" height="672"></div>
      <div>
        <h2>Werdegang</h2>
        <p class="intro">Dr. Anja Muggli absolvierte in den USA einen Bachelor in K–12 Education mit Major in Germanistik und Minor in Englisch als Zweitsprache, einen Master in Education mit Major in E-Learning Technology and Design sowie ein Doktorat in Education mit Schwerpunkten in englischer Linguistik und (Fremd-)Sprachdidaktik. Seit ihrer Rückkehr in die Schweiz im Jahr 2022 bringt sie ihre fachlichen und internationalen Erfahrungen in die Lehrpersonenausbildung sowie in die Berufsbildung ein. Ergänzend erwarb sie das schweizerische Lehrdiplom für den berufskundlichen Unterricht im Fach Technisches Englisch.</p>
        <h2>Schwerpunkte</h2>
        <p class="intro">Ihre fachlichen Schwerpunkte liegen in der Gestaltung und Begleitung von Lernprozessen, der Förderung selbstregulierten Lernens sowie der Verbindung von erziehungswissenschaftlichen Erkenntnissen und Unterrichtspraxis. Weitere Schwerpunkte bilden die Interdisziplinarität in der Berufsbildung, der berufsbezogene Englischunterricht, die Fremdsprachendidaktik und der sprachsensible Unterricht. Ein besonderes Interesse gilt digitalen Lernangeboten und dem reflektierten Einsatz künstlicher Intelligenz in der Bildung. Im Zentrum steht dabei die Frage, wie didaktische Ansätze und Werkzeuge das Verständnis, die Selbstständigkeit und das kritische Denken von Lernenden fördern können.</p>
        <h2>Aktuelle Tätigkeiten</h2>
        <p class="intro">Anja unterrichtet an der Gewerblichen Berufsschule Chur Technical English als Ergänzung zum Fachunterricht für elf verschiedene Berufe aus den Bereichen Maschinenbau, Informatik und Mediamatik. Zudem ist sie als Dozentin für Erziehungswissenschaften im Masterstudiengang Sekundarstufe I &amp; II an der Pädagogischen Hochschule Graubünden tätig. In diesen Funktionen begleitet sie Berufslernende und angehende Lehrpersonen und verbindet schulische Praxis mit wissenschaftlichen Perspektiven auf Lehren und Lernen. Mit MuggliOnline möchte sie selbst erstellte Unterrichtsmaterialien, Lernübungen und digitale Werkzeuge für Lehrpersonen und Lernende zugänglich machen und damit selbstständiges Lernen sowie die Unterrichtsgestaltung unterstützen.</p>
        <h2>Berufserfahrung</h2>
        <p class="intro">Anja verfügt über mehr als 15 Jahre Praxiserfahrung im Unterrichten. In den USA unterrichtete sie an Highschools in Wisconsin, Georgia und New York Jugendliche im Alter von 14 bis 18 Jahren. Zudem dozierte sie während mehrerer Jahre an einem College in New York und an einer Universität in Montana. In der Lehrpersonenbildung ist sie bereits im zehnten Jahr tätig. Dazu gehören Lehrveranstaltungen in verschiedenen erziehungswissenschaftlichen und didaktischen Modulen auf Bachelor- und Masterstufe, die Mentorierung von Studierenden in Praktika sowie die Begleitung von Bachelor- und Masterarbeiten.</p>
        <a class="btn green" href="kontakt.html">Kontakt aufnehmen</a>
      </div>
    </div>
  </section>
</main>""", active="ueber-anja.html", description="Über Dr. Anja Muggli.")

# ---------------- Kontakt, Impressum, Datenschutz ----------------
page("kontakt.html", "Kontakt – MuggliOnline", f"""<main class="wrap">
{hero("Kontakt", "Kontakt", "Kontakt", "Fragen, Anregungen oder Interesse an einer Zusammenarbeit? Ich freue mich auf deine Nachricht.")}
  <section class="section">
    <div class="grid2">
      <div class="plan"><h3>E-Mail</h3><p>Schreib mir gerne eine E-Mail.</p><p style="margin-top:16px"><a class="btn green" href="mailto:anja@mugglionline.ch">anja@mugglionline.ch</a></p></div>
{plan("LinkedIn", "Der Link zu meinem LinkedIn-Profil wird hier bald ergänzt.", badge="Folgt")}
    </div>
  </section>
</main>""", active="kontakt.html", description="Kontakt zu Dr. Anja Muggli.")

page("impressum.html", "Impressum – MuggliOnline", f"""<main class="wrap">
{hero("Impressum", "Rechtliches", "Impressum", "Angaben zur verantwortlichen Person dieser Website.")}
  <section class="section"><div class="legal">
    <h2>Verantwortlich für diese Website</h2>
    <p><b>Dr. Anja Muggli</b><br>Chur, Schweiz<br>E-Mail: <a href="mailto:anja@mugglionline.ch">anja@mugglionline.ch</a></p>
    <p>MuggliOnline (mugglionline.ch) ist eine private, nicht kommerzielle Website. Sie bietet Lernmaterial für Lernende, Unterlagen für Lehrpersonen und Inhalte zur Pädagogik und Didaktik an. Es werden keine Waren oder Dienstleistungen verkauft.</p>

    <h2>Haftung für Inhalte</h2>
    <p>Die Inhalte dieser Website werden mit grosser Sorgfalt erstellt und regelmässig überprüft. Für die Richtigkeit, Vollständigkeit und Aktualität der Inhalte kann ich jedoch keine Gewähr übernehmen. Die Materialien dienen der Information und dem Lernen; sie ersetzen keine fachliche, rechtliche oder medizinische Beratung.</p>

    <h2>Haftung für Links</h2>
    <p>Diese Website enthält Links zu Websites Dritter. Auf deren Inhalte habe ich keinen Einfluss, und für sie sind ausschliesslich die jeweiligen Anbieterinnen und Anbieter verantwortlich. Zum Zeitpunkt der Verlinkung waren keine rechtswidrigen Inhalte erkennbar. Sollte ich von Rechtsverletzungen erfahren, entferne ich den betreffenden Link umgehend.</p>

    <h2>Urheberrecht</h2>
    <p>Texte, Übungen, Grafiken und Spiele auf dieser Website sind, soweit nicht anders angegeben, von mir erstellt und urheberrechtlich geschützt. Für die nicht kommerzielle Nutzung im eigenen Unterricht dürfen sie gerne verwendet werden. Jede andere Verwendung, insbesondere die Veröffentlichung oder der Verkauf, braucht meine vorherige Zustimmung.</p>
    <p>Inhalte Dritter sind als solche gekennzeichnet: Zitate und Abbildungen aus Fachliteratur werden als Zitat mit Quellenangabe wiedergegeben (Art. 25 Urheberrechtsgesetz, URG). Fotos und Grafiken anderer Urheberinnen und Urheber tragen einen Bildnachweis mit Lizenz. Einige Abbildungen und Spielbilder wurden mit KI-Werkzeugen (ChatGPT von OpenAI) erzeugt, einige Grafiken, Texte und Übungen mit Unterstützung von Claude (Anthropic) erstellt und von mir überarbeitet.</p>
    <p>Falls du der Meinung bist, dass ein Inhalt deine Rechte verletzt, schreib mir bitte an <a href="mailto:anja@mugglionline.ch">anja@mugglionline.ch</a>. Ich prüfe das Anliegen rasch und entferne den Inhalt bei Bedarf.</p>

    <h2>Datenschutz</h2>
    <p>Wie auf dieser Website mit Personendaten umgegangen wird, steht in der <a href="datenschutz.html">Datenschutzerklärung</a>.</p>
    <p class="stand">Stand: 25. November 2026</p>
  </div></section>
</main>""", description="Impressum von MuggliOnline: verantwortliche Person, Haftung, Urheberrecht.")

page("datenschutz.html", "Datenschutz – MuggliOnline", f"""<main class="wrap">
{hero("Datenschutz", "Rechtliches", "Datenschutzerklärung", "Wie auf dieser Website mit Daten umgegangen wird.")}
  <section class="section"><div class="legal">
    <p class="kurz"><b>Kurz gesagt:</b> Diese Website verwendet keine Cookies, keine Analyse- oder Werbedienste und keine Formulare. Antworten in Übungen und Spielständen bleiben auf deinem eigenen Gerät. Beim Aufruf der Seiten werden technisch nötige Verbindungsdaten (insbesondere die IP-Adresse) an den Hosting-Anbieter und an einzelne eingebundene Dienste übermittelt. Die Details stehen unten.</p>

    <h2>1. Verantwortliche Person</h2>
    <p>Verantwortlich für die Bearbeitung von Personendaten auf dieser Website ist:<br><b>Dr. Anja Muggli</b>, Chur, Schweiz<br>E-Mail: <a href="mailto:anja@mugglionline.ch">anja@mugglionline.ch</a></p>
    <p>Diese Datenschutzerklärung erfüllt die Informationspflicht nach Art. 19 des Bundesgesetzes über den Datenschutz (DSG, SR 235.1).</p>

    <h2>2. Welche Daten bearbeitet werden und wozu</h2>
    <h3>a) Aufruf der Website (Hosting)</h3>
    <p>Die Website wird über <b>GitHub Pages</b> bereitgestellt, einen Dienst von GitHub, Inc. (USA, ein Unternehmen von Microsoft). Wenn du eine Seite aufrufst, verarbeitet der Server automatisch technische Verbindungsdaten: IP-Adresse, Datum und Uhrzeit, aufgerufene Seite, Browser und Betriebssystem sowie die zuvor besuchte Seite. GitHub speichert die IP-Adresse aus Sicherheitsgründen, etwa zur Abwehr von Angriffen. Ich selbst erhalte keine Besucherstatistiken und werte keine Daten aus.</p>
    <p><b>Zweck:</b> technische Bereitstellung, Stabilität und Sicherheit der Website. Die Domain mugglionline.ch ist bei Infomaniak Network SA (Schweiz) registriert.</p>
    <h3>b) Schriftarten (Google Fonts)</h3>
    <p>Für die Darstellung der Schriften werden Google Fonts von Servern der Google LLC (USA) bzw. Google Ireland Limited geladen. Dabei übermittelt dein Browser deine IP-Adresse und technische Angaben zum Browser an Google. <b>Zweck:</b> einheitliche und gut lesbare Darstellung der Website.</p>
    <h3>c) Eingebettete Videos (YouTube)</h3>
    <p>Auf einzelnen Lernseiten sind Videos von YouTube (Google) im <b>erweiterten Datenschutzmodus</b> (youtube-nocookie.com) eingebettet. Beim Laden dieser Seiten wird eine Verbindung zu Servern von Google hergestellt und deine IP-Adresse übermittelt. Erst wenn du ein Video abspielst, kann YouTube weitere Daten bearbeiten und Cookies oder ähnliche Speicher setzen. Wenn du das nicht möchtest, spiele die Videos nicht ab oder öffne sie über den angegebenen Link bzw. QR-Code direkt bei YouTube. Es gelten die Datenschutzbestimmungen von Google.</p>
    <h3>d) Bilder von Wikimedia Commons</h3>
    <p>Auf einer Übungsseite wird ein frei lizenziertes Foto direkt von Wikimedia Commons (Wikimedia Foundation, USA) geladen. Dabei wird deine IP-Adresse an die Server von Wikimedia übermittelt. <b>Zweck:</b> Anzeige des Bildes.</p>
    <h3>e) Speicherung auf deinem Gerät (Übungen und Spiele)</h3>
    <p>Bei den interaktiven Übungen und Spielen werden deine Antworten, Spielstände, Teamnamen und Bestzeiten im <b>lokalen Speicher deines Browsers</b> (localStorage) abgelegt, damit du später weiterarbeiten kannst. Diese Daten werden nicht an mich oder an Dritte übermittelt. Du kannst sie jederzeit löschen, indem du in der Übung «Start again» bzw. im Spiel «New game» wählst oder die Website-Daten in deinem Browser löschst.</p>
    <h3>f) Kontakt per E-Mail</h3>
    <p>Wenn du mir eine E-Mail schreibst, bearbeite ich deine E-Mail-Adresse, deinen Namen und den Inhalt deiner Nachricht, um deine Anfrage zu beantworten. Die E-Mails werden bei meinem E-Mail-Anbieter gespeichert. Ich gebe sie nicht weiter und lösche sie, wenn sie für die Beantwortung und allfällige Rückfragen nicht mehr gebraucht werden, sofern keine gesetzliche Aufbewahrungspflicht besteht.</p>

    <h2>3. Was diese Website nicht macht</h2>
    <ul>
      <li>keine Cookies durch die Website selbst</li>
      <li>keine Analyse- oder Statistikdienste (z.&nbsp;B. Google Analytics)</li>
      <li>keine Werbung, kein Tracking, keine Profilbildung</li>
      <li>keine Benutzerkonten, keine Formulare, keine automatisierten Einzelentscheidungen</li>
    </ul>

    <h2>4. Empfängerinnen und Empfänger und Bekanntgabe ins Ausland</h2>
    <p>Personendaten können an folgende Kategorien von Empfängern gelangen: Hosting-Anbieter (GitHub), Anbieter eingebundener Inhalte (Google für Schriften und Videos, Wikimedia für ein Bild) sowie mein E-Mail-Anbieter. Dabei können Daten in die <b>USA</b> und in Länder der <b>Europäischen Union</b> übermittelt werden.</p>
    <p>Die Staaten der EU gelten nach Anhang 1 der Datenschutzverordnung (DSV) als Staaten mit angemessenem Datenschutz. Für die USA hat der Bundesrat seit dem 15. September 2024 festgestellt, dass Unternehmen, die unter dem <b>Swiss-U.S. Data Privacy Framework</b> zertifiziert sind, einen angemessenen Schutz bieten. Ob ein Unternehmen zertifiziert ist, lässt sich auf <a href="https://www.dataprivacyframework.gov/list" target="_blank" rel="noopener">dataprivacyframework.gov</a> überprüfen. Soweit keine Zertifizierung besteht, stützen sich die Anbieter nach eigenen Angaben auf Standardvertragsklauseln.</p>

    <h2>5. Aufbewahrung</h2>
    <p>Ich bewahre Personendaten nur so lange auf, wie es für den jeweiligen Zweck nötig ist. Wie lange GitHub, Google und Wikimedia technische Verbindungsdaten speichern, richtet sich nach deren eigenen Datenschutzbestimmungen. Daten im lokalen Speicher deines Browsers bleiben, bis du sie löschst.</p>

    <h2>6. Deine Rechte</h2>
    <p>Du hast nach dem DSG insbesondere das Recht,</p>
    <ul>
      <li>Auskunft darüber zu verlangen, ob und welche Personendaten ich über dich bearbeite (Art. 25 DSG),</li>
      <li>die Berichtigung unrichtiger Daten zu verlangen (Art. 32 DSG),</li>
      <li>der Bearbeitung zu widersprechen und die Löschung deiner Daten zu verlangen,</li>
      <li>die Herausgabe oder Übertragung deiner Daten zu verlangen (Art. 28 DSG).</li>
    </ul>
    <p>Schreib mir dazu an <a href="mailto:anja@mugglionline.ch">anja@mugglionline.ch</a>. Für Daten, die GitHub, Google oder Wikimedia in eigener Verantwortung bearbeiten, wende dich bitte direkt an diese Anbieter. Du kannst dich ausserdem an den <a href="https://www.edoeb.admin.ch" target="_blank" rel="noopener">Eidgenössischen Datenschutz- und Öffentlichkeitsbeauftragten (EDÖB)</a> wenden.</p>

    <h2>7. Kinder und Jugendliche</h2>
    <p>Die Lernmaterialien richten sich auch an Kinder und Jugendliche. Die Website verlangt keine Angaben zur Person. Bitte gib in Übungen und Spielen keine vollständigen Namen oder andere persönliche Angaben ein. Teamnamen wie «The Energy Team» genügen.</p>

    <h2>8. Datensicherheit</h2>
    <p>Ich treffe angemessene technische und organisatorische Massnahmen, um Personendaten zu schützen, und verzichte bewusst auf Dienste, die nicht nötig sind. Eine vollständig sichere Übertragung von Daten im Internet kann jedoch niemand garantieren.</p>

    <h2>9. Änderungen</h2>
    <p>Ich passe diese Datenschutzerklärung an, wenn sich die Website oder die Rechtslage ändert. Es gilt die jeweils hier veröffentlichte Fassung.</p>
    <p class="stand">Stand: 25. November 2026</p>
  </div></section>
</main>""", description="Datenschutzerklärung von MuggliOnline nach dem Schweizer Datenschutzgesetz (DSG): Hosting, Google Fonts, YouTube, lokale Speicherung, deine Rechte.")

print("Seiten gebaut.")


import subprocess
subprocess.run(["python3", str(B / "i18n.py")], check=True)
