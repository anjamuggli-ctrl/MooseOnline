"""Baut alle Seiten von MuggliOnline.

Aufruf (im Repository-Ordner):  python3 _build/build.py
Ordner mit Unterstrich (_build) werden von GitHub Pages nicht veröffentlicht.
Kopfbalken, Fusszeile und Stylesheet sind für alle Seiten gleich und werden hier zentral gepflegt.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
B = Path(__file__).resolve().parent

LOGO = (B / "logo_inline.svg").read_text()
(ROOT / "style.css").write_text((B / "base.css").read_text() + (B / "extra.css").read_text())

MENU = [
    ("vision.html", "Vision"),
    ("english.html", "English"),
    ("didaktik.html", "Didaktik"),
    ("lernende.html", "Für Lernende"),
    ("werkstatt.html", "App-Werkstatt"),
    ("ueber-anja.html", "Über Anja"),
]

RIDGE = """<svg class="ridge" viewBox="0 0 1200 100" preserveAspectRatio="none" aria-hidden="true">
      <path d="M0,100 L0,76 L120,44 L190,64 L300,18 L390,58 L470,40 L560,72 L660,34 L740,54 L840,14 L930,52 L1010,36 L1100,64 L1200,42 L1200,100 Z" fill="#4c6b57"/>
      <path d="M0,100 L0,86 L140,66 L260,82 L380,62 L520,84 L640,68 L780,82 L920,64 L1060,80 L1200,70 L1200,100 Z" fill="#f4f1ea"/>
    </svg>"""


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
<link rel="stylesheet" href="style.css">
{extra_head}</head>
<body>

<header>
  <div class="wrap nav">
    <a class="brand" href="index.html" aria-label="MuggliOnline Startseite">
      {LOGO}
      <span class="name">Muggli<span>Online</span></span>
    </a>
    <button class="burger" aria-label="Menü öffnen" onclick="document.getElementById('menu').classList.toggle('open')"><span></span><span></span><span></span></button>
    <ul class="menu" id="menu">
{items}
      <li><a class="{kontakt_cls}" href="kontakt.html">Kontakt</a></li>
    </ul>
  </div>
</header>

{body}

<footer>
  <div class="wrap">
    <span>© 2026 MuggliOnline · Dr. Anja Muggli, Chur</span>
    <nav><a href="kontakt.html">Kontakt</a><a href="impressum.html">Impressum</a><a href="datenschutz.html">Datenschutz</a></nav>
  </div>
</footer>

</body>
</html>
"""
    (ROOT / filename).write_text(html)


def hero(crumb, kicker, h1, lead):
    return f"""  <section class="page-hero">
    <div class="inner">
      <div class="crumbs"><a href="index.html">Startseite</a> › {crumb}</div>
      <div class="kicker">{kicker}</div>
      <h1>{h1}</h1>
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
    "english.html": "english.html", "english-lernende.html": "english.html", "english-lehrpersonen.html": "english.html",
    "didaktik.html": "didaktik.html", "lernende.html": "lernende.html",
    "werkstatt.html": "werkstatt.html", "bullet-journal.html": "werkstatt.html",
    "vision.html": "vision.html", "ueber-anja.html": "ueber-anja.html", "kontakt.html": "kontakt.html",
}

# ---------------- Startseite ----------------
main = (B / "index_main.html").read_text()
for old, new in {
    'href="#english-lernende"': 'href="english-lernende.html"',
    'href="#english-lehrpersonen"': 'href="english-lehrpersonen.html"',
    'href="#didaktik"': 'href="didaktik.html"',
    'href="#lernende"': 'href="lernende.html"',
    'href="#werkstatt"': 'href="werkstatt.html"',
    'href="#ueber-anja"': 'href="ueber-anja.html"',
    'href="#vision"': 'href="vision.html"',
}.items():
    main = main.replace(old, new)
page("index.html", "MuggliOnline – Materialien und Werkzeuge für gutes Lernen", main,
     description="Unterrichtsmaterialien, Online-Übungen und didaktische Hilfsmittel für Lernende und Lehrpersonen.")

# ---------------- English: Übersicht ----------------
page("english.html", "English – MuggliOnline", f"""<main class="wrap">
{hero("English", "Englisch", "English", "Übungen für Lernende und Materialien für Lehrpersonen, von Basic English bis Fachenglisch an Berufsschulen.")}
  <section class="section">
    <h2>Wähle deinen Bereich</h2>
    <p class="intro">Der English-Bereich ist in zwei Teile gegliedert.</p>
    <div class="grid2">
      <a class="plan" href="english-lernende.html" style="border-style:solid"><span class="badge live">Für Lernende</span><h3>English für Lernende →</h3><p>Online-Übungen mit direkter Rückmeldung zu Basic English, Grammatik, Writing und Fachenglisch.</p></a>
      <a class="plan" href="english-lehrpersonen.html" style="border-style:solid"><span class="badge live">Für Lehrpersonen</span><h3>English für Lehrpersonen →</h3><p>Unterrichtsmaterialien, Vorlagen und Prüfungen für den eigenen Englischunterricht.</p></a>
    </div>
  </section>
</main>""", active="english.html", description="Englisch für Lernende und Lehrpersonen.")

area("english-lernende.html", '<a href="english.html">English</a> › Für Lernende', "Für Lernende",
     "English für Lernende",
     "Übungen mit direkter Rückmeldung: Du schreibst deine Antworten hinein und siehst sofort, ob sie stimmen.",
     "Die Übungen werden laufend aufgebaut. Geplant sind diese Bereiche:",
     [plan("Basic English", "Grundlagen in kleinen Schritten, mit Sofortkontrolle.", ["Grammatik-Übungen und Lückentexte", "Wortschatz", "Writing-Aufgaben mit Checklisten"]),
      plan("Fachenglisch Maschinenbau", "Fachwortschatz und Texte aus dem Berufsalltag.", ["Vokabeltrainer", "Leseverständnis", "Lückentexte"]),
      plan("Fachenglisch Mediamatik", "Englisch rund um Medien, Design und Kommunikation.", ["Vokabeltrainer", "Leseverständnis", "Lückentexte"]),
      plan("Fachenglisch Informatik", "Englisch für IT, Netzwerke und Software.", ["Vokabeltrainer", "Leseverständnis", "Lückentexte"])],
     cols="grid2")

area("english-lehrpersonen.html", '<a href="english.html">English</a> › Für Lehrpersonen', "Für Lehrpersonen",
     "English für Lehrpersonen",
     "Unterrichtsmaterialien, Vorlagen und Prüfungen für Basic English und Fachenglisch an Berufsschulen.",
     "Hier entsteht eine Sammlung von erprobten Materialien für den eigenen Unterricht:",
     [plan("Unterrichtsmaterialien", "Arbeitsblätter, Dialoge und Aufgaben zu verschiedenen Themen."),
      plan("Vorlagen", "Vorlagen für Unterrichtsplanung, Aufträge und Bewertungsraster."),
      plan("Prüfungen", "Prüfungen und Probeprüfungen mit Lösungen und Bewertungshinweisen.")])

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
          <p>Erstelle druckfertige A5-Seiten für dein Bullet Journal: Tagesplaner, Wochen- und Monatsübersicht oder Habit-Tracker, mit Punkten, Kästchen oder Linien. Später kommen KI-Motive zum Nachzeichnen dazu.</p>
          <div class="tags"><span>A5</span><span>Druckfertig</span><span>Bald mit KI</span></div>
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
  <section class="section" style="margin-top:0">
    <div class="note"><span>✨</span><span><b>Was noch kommt:</b> KI-Motive zum Nachzeichnen, eine Bibliothek mit eigenen Vorlagen und das Speichern deiner Lieblingseinstellungen. Diese Funktionen werden passwortgeschützt.</span></div>
  </section>
</main>
<script src="bullet-journal.js"></script>""", active="werkstatt.html", description="Druckfertige A5-Seiten für das Bullet Journal erstellen.")

# ---------------- Vision ----------------
area("vision.html", "Vision", "Meine Vision", "Vision",
     "Lernen verstehen, Lehren gestalten, Zukunft mitprägen. Was ich mit MuggliOnline erreichen möchte.",
     "Die drei Teile meines Mottos bilden das Fundament dieser Website. Die ausführlichen Texte folgen.",
     [plan("Lernen verstehen", "Text folgt.", badge="Text folgt"),
      plan("Lehren gestalten", "Text folgt.", badge="Text folgt"),
      plan("Zukunft mitprägen", "Text folgt.", badge="Text folgt")])

# ---------------- Über Anja ----------------
page("ueber-anja.html", "Über Anja – MuggliOnline", f"""<main class="wrap">
{hero("Über Anja", "Über mich", "Dr. Anja Muggli", "Dozentin Erziehungswissenschaften · Englischlehrperson")}
  <section class="section">
    <div class="about">
      <div class="photo" aria-label="Platzhalter für Porträtfoto">
        <svg viewBox="0 0 170 200" aria-hidden="true"><circle cx="85" cy="78" r="38" fill="#c9d3c7"/><path d="M10,200 C14,148 46,124 85,124 C124,124 156,148 160,200 Z" fill="#c9d3c7"/></svg>
      </div>
      <div>
        <h2>Werdegang</h2>
        <p class="intro">Text folgt.</p>
        <h2>Schwerpunkte</h2>
        <p class="intro">Text folgt.</p>
        <h2>Aktuelle Tätigkeiten</h2>
        <p class="intro">Text folgt.</p>
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
