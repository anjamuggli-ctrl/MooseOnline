// Erzeugt die Vorlagen zum Smart City Projekt als Word-Dateien (Stil: _build/vorlagen_stil.js).
// Aufruf im Repository-Ordner:  python3 _build/vorlagen_banner.py  (einmalig)  und  node _build/smartcity_docs.js
// PDF danach:  cd downloads/smart-city && soffice --headless --convert-to pdf *.docx
const fs = require("fs");
const path = require("path");
const { Document, Packer, Paragraph, Table, TableRow, TableCell, WidthType, AlignmentType } = require("docx");
const S = require("./vorlagen_stil");

const OUT = path.join(__dirname, "..", "downloads", "smart-city");
fs.mkdirSync(OUT, { recursive: true });
const IMG = path.join(__dirname, "..", "img", "smart-city");
const W = S.W_HOCH, WQ = S.W_QUER;
const KZ = (nr, t) => `Smart City Projekt · Vorlage ${nr} · ${t}`;
const F = S.FARBEN;
S.projekt("terrakotta", "stadt"); // gleicher Kopf für alle Smart-City-Vorlagen

// zwei Bilder nebeneinander mit Bildlegende
function bildPaar(v, links, rechts) {
  const b = W / 2;
  const zelle = ([datei, legende]) => new TableCell({ width: { size: b, type: WidthType.DXA }, borders: S.OHNE_RAND, margins: { top: 0, bottom: 0, left: 60, right: 60 },
    children: [new Paragraph({ children: [S.bild(path.join(IMG, datei), 8.2, 4.6)], alignment: AlignmentType.CENTER, spacing: { after: 40 } }),
      new Paragraph({ children: S.runs(legende, { size: 17, color: v.F.dunkel }), alignment: AlignmentType.CENTER, spacing: { after: 0 } })] });
  return [new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: [b, b], rows: [new TableRow({ children: [zelle(links), zelle(rechts)] })] }), v.leer()];
}
// mehrere Bilder nebeneinander, proportional eingepasst
function bildReihe(v, liste, hoeheCm = 3.6) {
  const b = Math.floor(W / liste.length);
  return [new Table({ width: { size: b * liste.length, type: WidthType.DXA }, columnWidths: Array(liste.length).fill(b), rows: [new TableRow({ children: liste.map(([datei, legende]) =>
    new TableCell({ width: { size: b, type: WidthType.DXA }, borders: S.OHNE_RAND, margins: { top: 0, bottom: 0, left: 60, right: 60 },
      children: [new Paragraph({ children: [S.bild(path.join(IMG, datei), b / 567 - 0.3, hoeheCm)], alignment: AlignmentType.CENTER, spacing: { after: 30 } }),
        new Paragraph({ children: S.runs(legende, { size: 16, color: v.F.dunkel, bold: true }), alignment: AlignmentType.CENTER, spacing: { after: 0 } })] })) })] }), v.leer()];
}
// farbige Spalten ohne Rahmen (KI-Ampel, Kanban)
function farbSpalten(spalten, hoehe) {
  const b = Math.floor(W / spalten.length);
  return [new Table({ width: { size: b * spalten.length, type: WidthType.DXA }, columnWidths: Array(spalten.length).fill(b), rows: [new TableRow({
    height: hoehe ? { value: hoehe, rule: "atLeast" } : undefined,
    children: spalten.map(([titel, text, f]) => new TableCell({ width: { size: b, type: WidthType.DXA },
      borders: { top: { style: "single", size: 24, color: f.dunkel }, bottom: S.OHNE_RAND.bottom, left: { style: "single", size: 24, color: "FFFFFF" }, right: { style: "single", size: 24, color: "FFFFFF" } },
      shading: { fill: f.hell, type: "clear", color: "auto" }, margins: { top: 120, bottom: 120, left: 160, right: 160 },
      children: [new Paragraph({ children: [S.r(titel, { bold: true, color: f.dunkel, size: 21 })], spacing: { after: 60 } }),
        new Paragraph({ children: S.runs(text, { size: 18 }), spacing: { after: 0, line: 252 } })] })) })] }), new Paragraph({ children: [], spacing: { after: 120 } })];
}

// ---------- SC1 Auftragsblatt ----------
let v = S.mit("bergsee", "stadt");
const SC1 = v.abschnitt(KZ("SC1", "Auftragsblatt"), [
  ...v.kopf({ kicker: "Vorlage SC1 · für Lernende", titel: "Smart City Projekt: Eure Offerte für die Stadt", felder: ["Gruppe", "Firma", "Stadt"] }),
  v.p("Die Stadt möchte eine **Smart City** werden: eine vernetzte Stadt mit hoher Lebensqualität, die Energie und Ressourcen klug einsetzt. Sie sucht eine Firma, die dieses Projekt plant."),
  v.p("Ihr gründet in Gruppen von drei bis vier Personen eine Firma und bewerbt euch mit einer **Offerte**. Die übrige Klasse spielt den **Stadtrat**. Er hört sich alle Offerten an und vergibt am Schluss den Auftrag."),
  v.h("Unsere Variante"),
  ...bildPaar(v, ["stadt-realitaetsnah.jpg", "[] **Realitätsnah:** nur Technik, die es heute gibt oder die getestet wird"], ["stadt-fantasy.jpg", "[] **Fantasy:** Zukunftsideen erlaubt, zum Beispiel fliegende Taxis"]),
  v.p("Bei der Fantasy-Variante braucht jede Idee eine plausible Erklärung, einen klaren Nutzen und eine begründete Kostenschätzung. Bei der realitätsnahen Variante belegt ihr die Kosten mit Quellen.", { size: 18 }),
  ...v.kasten("Pflicht für alle", "Mindestens eine Idee hat mit **erneuerbarer Energie oder Ressourcen** zu tun. Ihr zeigt, was die Stadt für Umwelt, Gesellschaft und Wirtschaft gewinnt.", F.terrakotta),
  v.h("Eure Schritte"),
  ...v.tabelle([500, 2300, 3600, 2000, 1238], ["", "Schritt", "Was ihr macht", "Ergebnis", "Termin"], [
    [{ text: "**1**", fill: true }, "Firma gründen", "Gruppe bilden, Rollen wählen, Gruppenvertrag", "SC4 unterschrieben", ""],
    [{ text: "**2**", fill: true }, "Methode kennen", "Projektmanagement-Modell kennenlernen, Projektplan anlegen", "Projektplan SC3", ""],
    [{ text: "**3**", fill: true }, "Recherchieren", "Was ist eine Smart City? Wie ist eure Stadt? Echte Beispiele. Alles ins Arbeitsjournal.", "Journal SC5, Ideenliste", ""],
    [{ text: "**4**", fill: true }, "Offerte schreiben", "Idee, Lieferobjekte, Phasen, Zeitplan, Budget, Nutzen", "Offerte SC2, Zwischen-Check", ""],
    [{ text: "**5**", fill: true }, "Präsentation vorbereiten", "Folien gestalten, Fragen voraussehen, proben", "Präsentation, Probe", ""],
    [{ text: "**6**", fill: true }, "Präsentieren und bewerten", "Offerte präsentieren, als Stadtrat zuhören, euch selbst einschätzen", "SC9, SC10", ""],
  ]),
  v.h("Das gehört in eure Präsentation"),
  ...v.bullets(["Titelfolie, eure Firma, Übersicht", "Hintergrund zur Stadt", "eure Idee und eure Lieferobjekte (was die Stadt bekommt)", "Phasen mit Beschreibung der Arbeiten, Zeitplan und Budget für jede Phase", "Zielgruppe und Nutzen für die Stadt", "ein starker Schluss: Warum sollte die Stadt euch wählen?"]),
  v.h("Bewertung"),
  ...v.bullets(["**Offerte** (Vorlage SC2): ½ Note, Raster SC7. Rechtschreibung wird nicht bewertet. Dafür schreibt ihr in **euren eigenen Worten**, ohne Übersetzer oder KI für ganze Sätze.",
    "**Präsentation**: 1 Note, Raster SC8.", "Die Lehrperson kann zusätzlich eine Prozessnote geben (Journal, Zwischen-Checks, Zusammenarbeit)."]),
  v.h("KI-Ampel"),
  ...farbSpalten([
    ["Grün: erlaubt", "nach eurem eigenen Brainstorming weitere Ideen holen; Suchbegriffe finden; Rückmeldung zum Aufbau; Fragen des Stadtrats üben", F.bergsee],
    ["Gelb: nur mit Protokoll", "Fakten und Kosten erfragen und danach mit einer Quelle belegen; Bilder erzeugen und auf der Folie kennzeichnen", F.terrakotta],
    ["Rot: nicht erlaubt", "Sätze oder Abschnitte der Offerte schreiben oder übersetzen lassen; Präsentationstext erzeugen; Personendaten eingeben", F.alpenrose]]),
  v.p("Jede KI-Nutzung kommt ins KI-Protokoll eures Arbeitsjournals.", { size: 18 }),
  v.h("Abgabe und Regeln"),
  ...v.bullets(["Offerte und Präsentation ladet ihr am Präsentationstag **vor Lektionsbeginn** auf Teams hoch, auch wenn ihr an diesem Tag fehlt.",
    "Für jeden Tag Verspätung gibt es einen Abzug. Arbeiten, die mehr als zwei Tage zu spät sind, werden nicht mehr angenommen.",
    "«Jemand anders hätte es hochladen sollen» gilt nicht als Entschuldigung. Die ganze Gruppe trägt den Abzug.",
    "Läuft es in der Gruppe nicht gut? Meldet euch **früh** bei der Lehrperson."]),
]);

// ---------- SC2 Offerte ----------
v = S.mit("terrakotta", "stadt");
const SC2 = v.abschnitt(KZ("SC2", "Offerte"), [
  ...v.kopf({ kicker: "Vorlage SC2 · für Lernende · zählt ½ Note", titel: "Offerte an den Stadtrat", unter: "Schreibt in euren eigenen Worten. Rechtschreibung wird nicht bewertet. Zeigt die Offerte beim Zwischen-Check, bevor ihr mit der Präsentation beginnt." }),
  v.h("1 · Unsere Firma"),
  ...v.felder(W, ["Name der Firma", "Logo oder Slogan", "Mitglieder und Rollen", "Was macht uns besonders?"]),
  v.h("2 · Die Stadt"),
  ...v.felder(W, ["Name, Land, Einwohnerzahl", "Drei Herausforderungen der Stadt", "Stärken der Stadt", "Quellen (Kürzel aus dem Journal)"]),
  v.h("3 · Unsere Idee"),
  ...bildReihe(v, [["stadt-illustration-gemeinschaft.jpg", "Wie lebt es sich in eurer Stadt?"], ["flugtaxi.jpg", "Fantasy: Was wäre möglich?"]], 4.4),
  ...v.felder(W, ["Variante", "Unsere Vision in zwei bis drei Sätzen: So sieht die Stadt nach unserem Projekt aus."], 900),
  v.h("4 · Lieferobjekte: Was bekommt die Stadt?"),
  ...bildReihe(v, [["haltestelle.jpg", "Mobilität"], ["energie.jpg", "Energie"], ["wasser-recycling.jpg", "Wasser und Recycling"]], 3.0),
  ...v.tabelle([2300, 2600, 2400, 2338], ["Komponente", "Was ist das? Wie funktioniert es?", "Welches Problem löst es?", "Nachhaltigkeit: Umwelt, Gesellschaft, Wirtschaft"], Array.from({ length: 5 }, () => ["", "", "", ""]), { hoehe: 900 }),
  v.h("5 · Phasen, Zeitplan und Budget"),
  v.p("Nutzt die Phasen eures Projektmanagement-Modells (zum Beispiel IPERKA oder HERMES)."),
  ...v.tabelle([2000, 3700, 2000, 1938], ["Phase", "Was passiert in dieser Phase?", "Dauer (von – bis)", "Kosten in CHF"],
    [...Array.from({ length: 5 }, () => ["", "", "", ""]), [{ text: "**Total**", span: 2, fill: true }, "", ""]], { hoehe: 800 }),
  v.p("So haben wir die Kosten geschätzt (Quellen, Annahmen):"), ...v.linien(3),
  v.h("6 · Zielgruppe"),
  ...v.felder(W, ["Wer profitiert? (Stadt, Bevölkerungsgruppen, Wirtschaft, Umwelt)"], 900),
  v.h("7 · Nutzen für die Stadt"),
  ...v.felder(W, ["Argument 1", "Argument 2", "Argument 3"]),
  v.h("8 · Risiken und Lösungen (Gymnasium und Berufsschule)"),
  ...v.tabelle([W / 2, W / 2], ["Was könnte schiefgehen?", "Wie reagieren wir?"], [["", ""], ["", ""]], { hoehe: 600 }),
  ...v.kasten("Zwischen-Check", "Datum: ______________   Visum Lehrperson: ______________   [] freigegeben für die Präsentation", F.gletscher),
]);

// ---------- SC3 Projektplan ----------
v = S.mit("gletscher", "berge");
const L = 12, lb = Math.round(7000 / L);
const SC3 = v.abschnitt(KZ("SC3", "Projektplan"), [
  ...v.kopf({ kicker: "Vorlage SC3 · für Lernende", titel: "Unser Projektplan", felder: ["Firma", "Projektleitung"] }),
  v.p("Das Modell **IPERKA** beschreibt, wie ein Projekt vollständig abläuft. **Realschule:** Ihr nutzt nur die vier farbigen Zeilen (Informieren, Planen, Realisieren, Auswerten). **Berufsschule:** Ihr ersetzt die Schritte durch die HERMES-Phasen Initialisierung, Konzept, Realisierung, Einführung, Abschluss."),
  ...v.tabelle([1500, 2700, 2700, 1200, 1100, 438], ["Schritt", "Leitfrage", "Was wir tun", "Wer", "Bis wann", "✓"], [
    [{ text: "**Informieren**", fill: true }, "Was müssen wir wissen? Was ist eine Smart City, wie ist unsere Stadt?", "", "", "", "[]"],
    [{ text: "**Planen**", fill: true }, "Welche Ideen haben wir? Welche Aufgaben, welche Reihenfolge?", "", "", "", "[]"],
    ["**Entscheiden**", "Welche drei bis fünf Ideen nehmen wir? Warum?", "", "", "", "[]"],
    [{ text: "**Realisieren**", fill: true }, "Offerte schreiben, Präsentation gestalten", "", "", "", "[]"],
    ["**Kontrollieren**", "Stimmen Zeitplan und Budget? Ist alles vollständig? Probe", "", "", "", "[]"],
    [{ text: "**Auswerten**", fill: true }, "Was lief gut, was machen wir nächstes Mal anders?", "", "", "", "[]"],
  ], { hoehe: 700 }),
  v.h("Zeitplan über die Lektionen"),
  v.p("Malt aus, in welchen Lektionen ihr woran arbeitet. Tragt Meilensteine (M1, M2, M3) ein."),
  ...v.tabelle([W - lb * L, ...Array(L).fill(lb)], ["Aufgabe", ...Array.from({ length: L }, (_, i) => `L${i + 1}`)],
    Array.from({ length: 6 }, () => Array(L + 1).fill("")), { hoehe: 380, mitte: true }),
  v.umbruch(),
  ...v.kopf({ kicker: "Vorlage SC3 · Kanban-Board", titel: "Kanban-Board", unter: "Schreibt jede Aufgabe auf eine Karte oder in eine Zeile. Am Anfang jeder Lektion schiebt ihr die Karten weiter (5-Minuten-Standup)." }),
  ...farbSpalten([["To do", "", F.alpenrose], ["Doing", "", F.terrakotta], ["Done", "", F.bergsee]], 10200),
]);

// ---------- SC4 Rollen ----------
v = S.mit("lavendel", "berge");
const rolle = (name, f, aufgaben, frage, gut) => new TableCell({ width: { size: W / 2, type: WidthType.DXA }, shading: { fill: f.hell, type: "clear", color: "auto" },
  borders: { top: { style: "single", size: 24, color: f.dunkel }, bottom: { style: "single", size: 24, color: "FFFFFF" }, left: { style: "single", size: 24, color: "FFFFFF" }, right: { style: "single", size: 24, color: "FFFFFF" } },
  margins: { top: 140, bottom: 140, left: 200, right: 200 }, children: [
    new Paragraph({ children: [S.r(name, { size: 26, bold: true, color: f.dunkel })], spacing: { after: 80 } }),
    ...aufgaben.map(t => new Paragraph({ children: S.runs("• " + t, { size: 18 }), spacing: { after: 30 } })),
    new Paragraph({ children: S.runs("**Leitfrage:** " + frage, { size: 18 }), spacing: { before: 80, after: 30 } }),
    new Paragraph({ children: S.runs("**Passt zu dir, wenn** " + gut, { size: 18 }), spacing: { after: 0 } })] });
const SC4 = v.abschnitt(KZ("SC4", "Rollen und Gruppenvertrag"), [
  ...v.kopf({ kicker: "Vorlage SC4 · für Lernende", titel: "Rollenkarten", unter: "Alle recherchieren, schreiben und präsentieren mit. Die Rolle bedeutet zusätzliche Verantwortung. Bei drei Personen übernimmt die Projektleitung auch die Finanzen." }),
  new Paragraph({ children: [S.bild(path.join(IMG, "team-modell.jpg"), 7.5, 4.2)], alignment: AlignmentType.CENTER, spacing: { after: 120 } }),
  new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: [W / 2, W / 2], rows: [
    new TableRow({ height: { value: 2600, rule: "atLeast" }, children: [
      rolle("Projektleitung", F.bergsee, ["führt das Kanban-Board und den Zeitplan", "leitet die Standups am Lektionsbeginn", "ist Kontaktperson zur Lehrperson"], "Sind wir im Zeitplan?", "du gern den Überblick behältst oder das lernen möchtest."),
      rolle("Recherche und Qualität", F.gletscher, ["sammelt und prüft Quellen", "achtet darauf, dass das Journal vollständig ist", "macht den Faktencheck, auch bei KI-Antworten"], "Stimmt das, und woher wissen wir es?", "du gern genau hinschaust.")] }),
    new TableRow({ height: { value: 2600, rule: "atLeast" }, children: [
      rolle("Finanzen und Planung", F.terrakotta, ["erstellt das Budget pro Phase", "prüft alle Zahlen nach", "plant, wie lange jede Phase dauert"], "Ist das realistisch und bezahlbar?", "du gern mit Zahlen arbeitest."),
      rolle("Design und Kommunikation", F.alpenrose, ["gestaltet Folien, Logo und Grafiken", "achtet auf Kennzeichnung von Bildern und KI-Bildern", "organisiert die Probe-Präsentation"], "Versteht der Stadtrat uns sofort?", "du gern gestaltest und präsentierst.")] }),
  ] }),
  v.leer(),
  v.h("Stärken-Runde"),
  ...v.tabelle([2400, 2800, 2800, 1638], ["Name", "Das kann ich gut", "Das möchte ich lernen", "Meine Rolle"], Array.from({ length: 4 }, () => ["", "", "", ""]), { hoehe: 600 }),
  v.umbruch(),
  ...v.kopf({ kicker: "Vorlage SC4 · Gruppenvertrag", titel: "Gruppenvertrag", felder: ["Firma", "Datum"] }),
  v.h("Unsere Regeln"), ...v.linien(5),
  v.h("So kommunizieren wir"),
  ...v.felder(W, ["Kanal (z. B. Teams-Chat)", "Wir antworten innerhalb von", "Wer fehlt, informiert so"]),
  v.h("Wenn jemand Abmachungen nicht einhält"),
  ...v.tabelle([600, W - 600], null, [["**1.**", "Wir sprechen es in der Gruppe direkt und freundlich an."], ["**2.**", ""], ["**3.**", "Wenn es nicht besser wird, holen wir die Lehrperson dazu."]], { hoehe: 480, label: true }),
  v.h("Unterschriften"),
  ...v.tabelle(Array(4).fill(Math.round(W / 4)), null, [["", "", "", ""]], { hoehe: 800 }),
  v.p("Überprüft nach dem Zwischen-Check M2:   [] Rollen passen   [] wir ändern: ______________________________"),
]);

// ---------- SC5 Journal ----------
v = S.mit("bergsee", "berge");
const SC5 = v.abschnitt(KZ("SC5", "Arbeitsjournal"), [
  ...v.kopf({ kicker: "Vorlage SC5 · für Lernende", titel: "Arbeitsjournal", unter: "Das Journal zeigt euren Weg. Es ist Grundlage für die Zwischen-Checks.", felder: ["Firma"] }),
  ...v.kasten("So legt ihr das Journal in OneNote an", v.bullets(["Abschnitt mit eurem Firmennamen im Klassennotizbuch",
    "Seite **Quellen**: ein Eintrag pro Website mit Screenshot (Windows: Windows + Shift + S, Mac: Cmd + Shift + 4), URL und Datum",
    "Seite **KI-Protokoll**: jede Nutzung von KI", "Seite **Standups**: kurze Notizen am Anfang jeder Lektion", "Seite **Ideen**: Brainstorming, Skizzen, Entscheide"]), F.gletscher),
  v.klein("Ohne OneNote könnt ihr die Tabellen unten verwenden."),
  v.h("Quellenprotokoll"),
  ...v.tabelle([1000, 2400, 900, 3000, 2338], ["Datum", "Quelle (URL, Titel)", "Screen-shot", "Was habe ich gelernt? (eigene Worte)", "Vertrauenswürdig? Wer, wann, mit welchem Ziel?"],
    Array.from({ length: 6 }, () => ["", "", "[]", "", ""]), { hoehe: 900 }),
  v.h("KI-Protokoll", F.gletscher),
  ...v.tabelle([900, 1100, 2200, 1800, 1900, 1738], ["Datum", "Tool", "Eingabe (Prompt)", "Antwort kurz", "Übernommen?", "So haben wir geprüft"],
    Array.from({ length: 5 }, () => ["", "", "", "", "[] ja [] teilw. [] nein", ""]), { hoehe: 900, farbe: F.gletscher }),
  v.h("Standups", F.terrakotta),
  ...v.tabelle([1100, 2900, 2900, 2738], ["Datum", "Das haben wir erledigt", "Das machen wir heute (wer?)", "Hier hängen wir"],
    Array.from({ length: 6 }, () => ["", "", "", ""]), { hoehe: 600, farbe: F.terrakotta }),
]);

// ---------- SC6 Zwischen-Check ----------
v = S.mit("gletscher", "weg");
const check = (titelM, f, punkte) => [v.h(titelM, f),
  ...v.tabelle([4800, 600, 600, 600, 3038], ["Kriterium", "✓", "~", "✗", "Notiz"], punkte.map(t => [t, "[]", "[]", "[]", ""]), { mitte: true, farbe: f }),
  v.p("**Vereinbarung bis zum nächsten Mal:**"), ...v.linien(2, f)];
const SC6 = v.abschnitt(KZ("SC6", "Zwischen-Checks"), [
  ...v.kopf({ kicker: "Vorlage SC6 · für die Lehrperson", titel: "Zwischen-Checks", felder: ["Firma", "Mitglieder"] }),
  ...check("M1 · Ideen   Datum: ________", F.bergsee, ["Rollen verteilt, Gruppenvertrag unterschrieben", "Projektplan angelegt, Kanban-Board läuft", "3 bis 5 Komponenten, mindestens eine zu erneuerbarer Energie oder Ressourcen", "mindestens drei Quellen im Journal, mit Screenshot und eigenen Worten", "Arbeit ist sichtbar auf alle verteilt"]),
  ...check("M2 · Offerte   Datum: ________", F.terrakotta, ["Offerte vollständig ausgefüllt", "Phasen logisch, passend zum Modell", "Zeitplan realistisch", "Budget nachvollziehbar und begründet", "in eigenen Worten geschrieben, KI-Protokoll geführt"]),
  v.p("[] **Freigabe für die Präsentation**", { before: 80 }),
  ...check("M3 · Probe   Datum: ________", F.lavendel, ["Zeit eingehalten", "weitgehend frei gesprochen", "Folien unterstützen, statt alles vorzulesen", "auf Fragen reagiert"]),
  ...v.kasten("Coaching-Fragen (GROW)", v.bullets(["**Ziel:** Was wollt ihr heute fertig haben?", "**Stand:** Zeigt mir euer Kanban-Board. Wo steht ihr?", "**Möglichkeiten:** Was könntet ihr tun, wenn ihr nicht weiterkommt?", "**Nächster Schritt:** Wer macht was bis wann?"])),
]);

// ---------- Raster ----------
v = S.mit("alpenrose", "berge");
const rasterZeilen = liste => liste.map(t => [t, "[]", "[]", "[]", "[]", ""]);
const SC7_KRIT = ["Firma vorgestellt (Name, Mitglieder, Rollen)", "Hintergrund zur Stadt mit Quellen", "Idee und Vision klar beschrieben", "Lieferobjekte: Was ist es, welches Problem löst es?", "Phasen mit Beschreibung der Arbeiten", "Zeitplan für jede Phase, realistisch", "Budget für jede Phase, begründet", "Zielgruppe benannt", "Nutzen für die Stadt überzeugend begründet", "Nachhaltigkeit: Umwelt, Gesellschaft, Wirtschaft", "in eigenen Worten, verständlich", "Quellen und Journal nachvollziehbar"];
const SC7 = v.abschnitt(KZ("SC7", "Bewertungsraster Offerte"), [
  ...v.kopf({ kicker: "Vorlage SC7 · Bewertung · ½ Note", titel: "Bewertungsraster Offerte", felder: ["Firma", "Mitglieder"] }),
  v.klein("**Skala:** 0 = fehlt · 1 = ansatzweise · 2 = grösstenteils erfüllt · 3 = vollständig und überzeugend"),
  ...v.tabelle([5038, 650, 650, 650, 650, 2000], ["Kriterium", "0", "1", "2", "3", "Feedback"],
    [...rasterZeilen(SC7_KRIT), [{ text: "**Total**", fill: true }, { text: "**____ / 36**", span: 4, align: AlignmentType.CENTER, fill: true }, ""]], { mitte: true, streifen: true }),
  v.p("Rechtschreibung wird nicht bewertet. Wurden ganze Sätze mit Übersetzer oder KI geschrieben, wird das Kriterium «in eigenen Worten» mit 0 bewertet und die Lehrperson bespricht das mit der Gruppe.", { size: 18 }),
  ...v.kasten("Note", "Punkte ÷ 36 × 5 + 1 = ________   (gerundet nach den Vorgaben der Schule)"),
  v.h("Rückmeldung"), ...v.linien(4),
]);
const SC8_TEIL = [
  ["Einstieg", F.bergsee, ["Titelfolie", "Firma vorgestellt", "Übersicht der Themen"], 1],
  ["Inhalt und Gestaltung", F.terrakotta, ["Hintergrund zur Stadt", "Idee der Firma", "Lieferobjekte", "Phasen (Beschreibung der Arbeiten)", "Zeitplan für jede Phase", "Budget für jede Phase", "Zielgruppe", "Nutzen für die Stadt", "Nachhaltigkeit (Umwelt, Gesellschaft, Wirtschaft)", "starker Schluss"], 3],
  ["Auftritt", F.lavendel, ["klar und professionell gesprochen", "angemessenes Tempo", "Fachbegriffe verwendet", "frei gesprochen", "Folien als visuelle Unterstützung genutzt", "mehr erklärt, als auf den Folien steht", "Fragen des Stadtrats beantwortet", "alle Mitglieder präsentieren"], 3],
];
const SC8 = v.abschnitt(KZ("SC8", "Bewertungsraster Präsentation"), [
  ...v.kopf({ kicker: "Vorlage SC8 · Bewertung · 1 Note", titel: "Bewertungsraster Präsentation", felder: ["Firma", "Mitglieder"] }),
  v.klein("**Einstieg:** 0 = fehlt, 1 = vorhanden. **Inhalt und Auftritt:** 0 = fehlt · 1 = ansatzweise · 2 = grösstenteils · 3 = vollständig und überzeugend"),
  ...SC8_TEIL.flatMap(([teil, f, krit, max]) => [v.h(teil, f), ...v.tabelle([5038, 650, 650, 650, 650, 2000], ["Kriterium", "0", "1", "2", "3", "Feedback"],
    [...krit.map(t => [t, "[]", "[]", max >= 2 ? "[]" : "–", max >= 3 ? "[]" : "–", ""]),
     [{ text: `**Total ${teil}**`, fill: true }, { text: `**____ / ${krit.length * max}**`, span: 4, align: AlignmentType.CENTER, fill: true }, ""]], { mitte: true, farbe: f, streifen: true })]),
  ...v.kasten("Gesamt und Note", [v.p("**____ / 57**    Note: Punkte ÷ 57 × 5 + 1 = ________", { size: 19, after: 40 }),
    v.p("Optional Anteil Stadtrat (vorher angekündigt): ________   Selbsteinschätzung der Gruppe (SC10): ________", { size: 19, after: 0 })]),
  v.h("Rückmeldung"), ...v.linien(4),
]);

// ---------- SC9 Stadtrat (quer) ----------
v = S.mit("lavendel", "stadt");
const SC9 = v.abschnitt(KZ("SC9", "Stadtrat-Notizen"), [
  ...v.kopf({ kicker: "Vorlage SC9 · für Lernende", titel: "Stadtrat: Unsere Notizen", unter: "Ihr seid der Stadtrat. Notiert zu jeder Firma Stichworte. Eure eigene Firma lasst ihr aus.", breite: WQ, felder: ["Name", "Stadt"] }),
  ...v.tabelle([1900, 2534, 2534, 2534, 2534, 2534], ["Firma", "Lieferobjekte: Welche Ideen haben sie für die Stadt?", "Zeitplan: Wie genau? Ist er machbar?", "Budget: Vernünftig? Stimmt das Preis-Leistungs-Verhältnis?", "Nutzen: Wer profitiert? Stadt, Bevölkerung?", "Kreativität: Wie überzeugend verkaufen sie ihre Idee?"],
    [...Array.from({ length: 5 }, () => [{ text: "", fill: true }, "", "", "", "", ""]), [{ text: "**Gewinner der Kategorie und warum**", fill: "F7E9C9" }, ...Array(5).fill({ text: "", fill: "FBF4E4" })]], { hoehe: 760 }),
  v.p("**Meine kritische Frage an eine Firma:** _____________________________________________________________________________________________"),
  v.p("**Den Gesamtauftrag gebe ich der Firma** ____________________, **weil** ___________________________________________________________________"),
], true);

// ---------- SC10 Selbsteinschätzung ----------
v = S.mit("terrakotta", "weg");
const skala = ["[]", "[]", "[]", "[]"];
const SC10 = v.abschnitt(KZ("SC10", "Selbsteinschätzung"), [
  ...v.kopf({ kicker: "Vorlage SC10 · für Lernende", titel: "Selbsteinschätzung der Gruppe", unter: "Füllt Teil A vor der Präsentation gemeinsam aus, Teil C allein und vertraulich.", felder: ["Firma"] }),
  v.h("A · So schätzen wir unsere Präsentation ein", F.bergsee),
  v.p("Füllt gemeinsam das Raster SC8 aus und tragt hier die Summen ein."),
  ...v.tabelle([3800, 1800, 1800, 2238], ["Bereich", "Unsere Punkte", "Maximum", "Darauf sind wir stolz"], [["Einstieg", "", "3", ""], ["Inhalt und Gestaltung", "", "30", ""], ["Auftritt", "", "24", ""], [{ text: "**Total und erwartete Note**", fill: true }, "", "57", ""]], { hoehe: 520, label: true, farbe: F.bergsee }),
  v.h("B · Unsere Zusammenarbeit", F.gletscher),
  ...v.tabelle([5638, 1000, 1000, 1000, 1000], ["", "trifft nicht zu", "eher nicht", "eher", "trifft zu"], [
    ["Wir haben Termine und Abmachungen eingehalten.", ...skala], ["Alle haben ihre Rolle wahrgenommen.", ...skala], ["Alle konnten ihre Ideen einbringen.", ...skala],
    ["Wir haben Probleme früh angesprochen.", ...skala], ["Unser Journal zeigt ehrlich, wer was gemacht hat.", ...skala]], { mitte: true, farbe: F.gletscher, streifen: true }),
  v.h("C · Beitragsverteilung (allein und vertraulich)", F.alpenrose),
  v.p("Verteile **100 Punkte** auf alle Mitglieder, dich selbst eingeschlossen. Haben alle gleich viel beigetragen, bekommen alle gleich viele Punkte."),
  ...v.tabelle([3000, 1500, 5138], ["Name", "Punkte", "Begründung (kurz)"], [["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""], [{ text: "**Summe**", fill: true }, { text: "**100**", fill: true }, { text: "", fill: true }]], { hoehe: 480, farbe: F.alpenrose }),
  v.p("Mein Name: ____________________"),
  v.h("D · Reflexion", F.lavendel),
  v.p("**Lessons learned:** Was hat gut funktioniert? Was machen wir beim nächsten Projekt anders?"), ...v.linien(3, F.lavendel),
  v.p("**KI:** Wo hat KI geholfen, wo hat sie Fehler gemacht, wo haben wir bewusst ohne gearbeitet?", { before: 120 }), ...v.linien(3, F.lavendel),
  v.p("**Mein Ziel:** Diese Kompetenz will ich weiterentwickeln:", { before: 120 }), ...v.linien(2, F.lavendel),
]);

// ---------- Speichern ----------
const DOKS = [["SC1_Auftragsblatt", SC1], ["SC2_Offerte-Vorlage", SC2], ["SC3_Projektplan", SC3], ["SC4_Rollenkarten_und_Gruppenvertrag", SC4], ["SC5_Arbeitsjournal", SC5],
  ["SC6_Zwischen-Check", SC6], ["SC7_Bewertungsraster_Offerte", SC7], ["SC8_Bewertungsraster_Praesentation", SC8], ["SC9_Stadtrat-Notizen", SC9], ["SC10_Selbsteinschaetzung", SC10]];
(async () => {
  for (const [name, sec] of DOKS) {
    const doc = new Document({ creator: "Anja Muggli", title: name.replace(/_/g, " "), styles: S.STIL, numbering: S.NUM, sections: [sec] });
    fs.writeFileSync(path.join(OUT, name + ".docx"), await Packer.toBuffer(doc));
  }
  const alle = new Document({ creator: "Anja Muggli", title: "Smart City Projekt: alle Vorlagen", styles: S.STIL, numbering: S.NUM, sections: DOKS.map(d => d[1]) });
  fs.writeFileSync(path.join(OUT, "Smart_City_alle_Vorlagen.docx"), await Packer.toBuffer(alle));
  console.log("Word-Dateien erstellt:", DOKS.length + 1);
})();
