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
    ("vision.html", "Vision"),
    ("english.html", "Englisch"),
    ("didaktik.html", "Didaktik"),
    ("lernende.html", "Für Lernende"),
    ("werkstatt.html", "App-Werkstatt"),
    ("ueber-anja.html", "Über Anja"),
]

RIDGE = """<svg class="ridge" viewBox="0 0 1200 100" preserveAspectRatio="none" aria-hidden="true">
      <path d="M0,100 L0,76 L120,44 L190,64 L300,18 L390,58 L470,40 L560,72 L660,34 L740,54 L840,14 L930,52 L1010,36 L1100,64 L1200,42 L1200,100 Z" fill="#4c6b57"/>
      <path d="M0,100 L0,86 L140,66 L260,82 L380,62 L520,84 L640,68 L780,82 L920,64 L1060,80 L1200,70 L1200,100 Z" fill="#f4f1ea"/>
    </svg>"""


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
    <nav><a href="kontakt.html">Kontakt</a><a href="impressum.html">Impressum</a><a href="datenschutz.html">Datenschutz</a></nav>
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


def area(filename, crumb, kicker, h1, lead, intro, plans, note="", cols="grid3"):
    body = f"""<main class="wrap">
{hero(crumb, kicker, h1, lead)}
  <section class="section">
    <h2>Was hier entsteht</h2>
    <p class="intro">{intro}</p>
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

kacheln = "\n".join(
    f'''      <a class="plan entile" href="{datei}"><span class="badge live">{"Für Lehrpersonen" if _ == "nur-lp" else "Für Lehrpersonen und Lernende"}</span><h3>{titel}</h3><p>{text}</p><ul>{"".join(f"<li>{x}</li>" for x in punkte)}</ul><span class="go">Zum Bereich →</span></a>'''
    for datei, titel, text, punkte, _ in EN_BEREICHE)
page("english.html", "Englisch – MuggliOnline", f"""<main class="wrap">
{hero("Englisch", "Für Lehrpersonen und Lernende", "Englisch", "Übungen für Lernende und Materialien für Lehrpersonen, von Basic English bis Fachenglisch an Berufsschulen.")}
  <section class="section">
    <h2>Wähle deinen Bereich</h2>
    <p class="intro">Jeder Bereich bietet Übungen für Lernende und Materialien für Lehrpersonen.</p>
    <div class="grid2">
{kacheln}
    </div>
  </section>
</main>""", active="english.html", description="Englisch für Lernende und Lehrpersonen.")

INFORMATIK_THEMEN = [
    ("OSI Model", "Die sieben Schichten des OSI-Modells verstehen und auf Englisch erklären."),
    ("Smart City", "Vernetzte Technologien in der Stadt der Zukunft erkunden und präsentieren."),
    ("Software Tutorial", "Eine Software Schritt für Schritt erklären und ein eigenes Tutorial erstellen."),
    ("IT Job Abroad", "Stelleninserate lesen, sich bewerben und ein Vorstellungsgespräch üben."),
    ("Cybersecurity & Data Protection", "Risiken im Netz erkennen und Massnahmen zum Datenschutz diskutieren."),
]

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
    return (f'      <div class="plan thema"><div class="thema-art"><svg viewBox="0 0 220 120" aria-hidden="true">{THEMEN_ART[titel]}</svg></div>'
            f'<span class="badge">In Vorbereitung</span><h3>{titel}</h3><p>{text}</p></div>')
INFORMATIK_INTRO = ("Unter den folgenden Themenbereichen findest du Unterrichtsideen mit Materialien und Bewertungsrastern. "
    "Sie wurden für den Unterricht in Technischem Englisch an der Berufsschule entwickelt, lassen sich aber übersetzen und für andere Fächer anpassen.")
INFORMATIK_INTRO2 = ("Weil sie für den Fremdsprachenunterricht gedacht sind, ist das sprachliche Niveau entsprechend angepasst. "
    "In der Erstsprache eignen sie sich deshalb auch gut als Projekte in der Oberstufe oder in der 6. Klasse.")
for datei, titel, text, punkte, lern in EN_BEREICHE:
    if lern == "nur-lp":
        themen = "\n".join(themen_karte(t, d) for t, d in INFORMATIK_THEMEN)
        page(datei, f"{titel} – MuggliOnline", f"""<main class="wrap">
{hero(f'<a href="english.html">Englisch</a> › {titel}', "Für Lehrpersonen", titel, text)}
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
{hero(f'<a href="english.html">Englisch</a> › {titel}', "Englisch", titel, text)}
  <section class="section">
    <div class="grid2">
{spalte("Für Lehrpersonen", "Materialien für den eigenen Unterricht.", LEHRPERSONEN)}
{spalte("Für Lernende", "Übungen mit direkter Rückmeldung.", lern)}
    </div>
  </section>
</main>""", active="english.html", description=text)

area("didaktik.html", "Didaktik", "Für Lehrpersonen",
     "Didaktik Zyklus 2",
     "Hilfsmittel, Unterrichtsvorlagen und Zusammenfassungen für die Praxis, fachlich fundiert und direkt einsetzbar.",
     "Die Inhalte stützen sich auf wissenschaftlich fundierte Quellen. Geplant sind:",
     [plan("Hilfsmittel", "Praktische Werkzeuge für Planung, Durchführung und Reflexion von Unterricht."),
      plan("Unterrichtsvorlagen", "Vorlagen, die sich direkt an die eigene Klasse anpassen lassen."),
      plan("Zusammenfassungen", "Kompakte Zusammenfassungen zu didaktischen Themen, jeweils mit Quellenangaben.")])

area("lernende.html", "Für Lernende", "6. Klasse und Oberstufe",
     "Für Lernende",
     "Probeprüfungen und Übungen zur Vorbereitung auf Prüfungen in verschiedenen Themen, mit Lösungen zur Selbstkontrolle.",
     "Hier kannst du dich gezielt auf Prüfungen vorbereiten. Geplant sind:",
     [plan("Probeprüfungen", "Prüfungen zum Üben unter echten Bedingungen, mit Lösungen."),
      plan("Übungsserien", "Kurze Übungen zu einzelnen Themen, um gezielt Lücken zu schliessen."),
      plan("Selbstkontrolle", "Lösungen und Tipps, damit du selbst überprüfen kannst, wo du stehst.")])

# ---------------- App-Werkstatt ----------------
page("werkstatt.html", "App-Werkstatt – MuggliOnline", f"""<main class="wrap">
{hero("App-Werkstatt", "Werkzeuge", "App-Werkstatt", "Kleine Web-Apps für Schule und Alltag. Einzelne Apps nutzen künftig KI und sind dann passwortgeschützt.")}
  <section class="section">
    <h2>Apps</h2>
    <p class="intro">Die Apps laufen direkt im Browser, ohne Installation.</p>
    <div class="cards">
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
          <div class="tags"><span>A5</span><span>Druckfertig</span><span>27 Vorlagen</span><span>Bald mit KI</span></div>
          <span class="go">App öffnen →</span>
        </div>
      </a>
    </div>
    <div class="grid2" style="margin-top:-56px">
{plan("Weitere Apps", "Weitere kleine Werkzeuge für Unterricht und Alltag sind in Planung.")}
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
        <p class="intro">Dr. Anja Muggli absolvierte in den USA einen Bachelor in K–12 Education mit Major in Germanistik und Minor in Englisch als Zweitsprache, einen Master in Education mit Major in E-Learning Technology and Design sowie ein Doktorat in Education mit Schwerpunkten in englischer Linguistik und (Fremd-)Sprachdidaktik. Seit ihrer Rückkehr in die Schweiz im Jahr 2022 bringt sie ihre fachlichen und internationalen Erfahrungen in die Berufsbildung ein. Ergänzend erwarb sie das schweizerische Lehrdiplom für den berufskundlichen Unterricht im Fach Technisches Englisch.</p>
        <h2>Schwerpunkte</h2>
        <p class="intro">Ihre fachlichen Schwerpunkte liegen in der Gestaltung und Begleitung von Lernprozessen, der Förderung selbstregulierten Lernens sowie der Verbindung von erziehungswissenschaftlichen Erkenntnissen und Unterrichtspraxis. Weitere Schwerpunkte bilden die Interdisziplinarität in der Berufsbildung, der berufsbezogene Englischunterricht, die Fremdsprachendidaktik und der sprachsensible Unterricht. Ein besonderes Interesse gilt digitalen Lernangeboten und dem reflektierten Einsatz künstlicher Intelligenz in der Bildung. Im Zentrum steht dabei die Frage, wie didaktische Ansätze und Werkzeuge das Verständnis, die Selbstständigkeit und das kritische Denken von Lernenden fördern können.</p>
        <h2>Aktuelle Tätigkeiten</h2>
        <p class="intro">Anja unterrichtet Englisch an der Gewerblichen Berufsschule Chur und ist als Dozentin für Erziehungswissenschaften im Masterstudiengang Sekundarstufe I &amp; II an der Pädagogischen Hochschule Graubünden tätig. In diesen Funktionen begleitet sie Berufslernende und angehende Lehrpersonen und verbindet schulische Praxis mit wissenschaftlichen Perspektiven auf Lehren und Lernen. Mit MuggliOnline möchte sie selbst erstellte Unterrichtsmaterialien, Lernübungen und digitale Werkzeuge für Lehrpersonen und Lernende zugänglich machen und damit selbstständiges Lernen sowie die Unterrichtsgestaltung unterstützen.</p>
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
{plan("E-Mail", "Die E-Mail-Adresse wird hier bald ergänzt.", badge="Folgt")}
{plan("LinkedIn", "Der Link zu meinem LinkedIn-Profil wird hier bald ergänzt.", badge="Folgt")}
    </div>
  </section>
</main>""", active="kontakt.html", description="Kontakt zu Dr. Anja Muggli.")

page("impressum.html", "Impressum – MuggliOnline", f"""<main class="wrap">
{hero("Impressum", "Rechtliches", "Impressum", "Angaben zur verantwortlichen Person dieser Website.")}
  <section class="section"><p class="intro">Wird ergänzt.</p></section>
</main>""", description="Impressum MuggliOnline.")

page("datenschutz.html", "Datenschutz – MuggliOnline", f"""<main class="wrap">
{hero("Datenschutz", "Rechtliches", "Datenschutzerklärung", "Wie auf dieser Website mit Daten umgegangen wird.")}
  <section class="section"><p class="intro">Wird ergänzt.</p></section>
</main>""", description="Datenschutzerklärung MuggliOnline.")

print("Seiten gebaut.")


import subprocess
subprocess.run(["python3", str(B / "i18n.py")], check=True)
