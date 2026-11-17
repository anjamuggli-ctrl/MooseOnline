// Erzeugt die Vorlagen zum Smart City Projekt als Word-Dateien.
// Aufruf im Repository-Ordner:  node _build/smartcity_docs.js   (danach PDF mit LibreOffice, siehe Ende)
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType,
  BorderStyle, AlignmentType, Header, Footer, PageNumber, PageOrientation, LevelFormat, PageBreak,
  VerticalAlign, HeightRule,
} = require("docx");

const OUT = path.join(__dirname, "..", "downloads", "smart-city");
fs.mkdirSync(OUT, { recursive: true });

const GRUEN = "3F5D4A", SAND = "F4F1EA", GRAU = "6B7368", LINIE = "C9CFC6";
const FONT = "Arial";
const W_HOCH = 9638, W_QUER = 14570; // nutzbare Breite A4 bei 2 cm Rand

// ---------- Bausteine ----------
const r = (t, o = {}) => new TextRun({ text: t, font: FONT, size: o.size || 20, bold: o.bold, italics: o.italics, color: o.color, characterSpacing: o.spacing });
const box = () => new TextRun({ text: "☐", font: "MS Gothic", size: 20 });
function runs(x, o = {}) {
  // "**fett**" im Text wird fett gesetzt, "[]" wird zu einem Ankreuzkästchen
  if (Array.isArray(x)) return x;
  const out = [];
  x.split(/(\*\*[^*]+\*\*|\[\])/).forEach(t => {
    if (!t) return;
    if (t === "[]") out.push(box());
    else if (t.startsWith("**")) out.push(r(t.slice(2, -2), { ...o, bold: true }));
    else out.push(r(t, o));
  });
  return out;
}
const p = (t, o = {}) => new Paragraph({ children: runs(t, o), spacing: { before: o.before || 0, after: o.after ?? 100, line: 276 }, alignment: o.align });
const kicker = t => new Paragraph({ children: [r(t.toUpperCase(), { size: 16, bold: true, color: GRAU, spacing: 40 })], spacing: { after: 60 } });
const titel = t => new Paragraph({ children: [r(t, { size: 36, bold: true, color: GRUEN })], spacing: { after: 80 }, keepNext: true });
const unter = t => new Paragraph({ children: runs(t, { color: GRAU, size: 20 }), spacing: { after: 200 } });
const h = t => new Paragraph({ children: [r(t, { size: 26, bold: true, color: GRUEN })], spacing: { before: 240, after: 100 }, keepNext: true });
const bullets = list => list.map(t => new Paragraph({ children: runs(t), numbering: { reference: "punkte", level: 0 }, spacing: { after: 60, line: 264 } }));
const linien = n => Array.from({ length: n }, () => new Paragraph({ children: [r("")], spacing: { before: 0, after: 0, line: 400 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: LINIE, space: 1 } } }));
const umbruch = () => new Paragraph({ children: [new PageBreak()] });

const RAND = { style: BorderStyle.SINGLE, size: 4, color: LINIE };
const RAENDER = { top: RAND, bottom: RAND, left: RAND, right: RAND };
function zelle(inhalt, breite, o = {}) {
  const kinder = (Array.isArray(inhalt) && inhalt.length && inhalt[0] instanceof Paragraph) ? inhalt
    : [new Paragraph({ children: runs(inhalt ?? "", { size: o.size || 18, bold: o.bold, color: o.color }), alignment: o.align, spacing: { after: 0, line: 252 } })];
  return new TableCell({
    children: kinder, width: { size: breite, type: WidthType.DXA }, borders: RAENDER,
    shading: o.fill ? { fill: o.fill, type: ShadingType.CLEAR, color: "auto" } : undefined,
    margins: { top: 80, bottom: 80, left: 110, right: 110 }, verticalAlign: o.valign || VerticalAlign.TOP,
    columnSpan: o.span,
  });
}
// tabelle(breiten, kopf, zeilen, {label:true, hoehe:Twips})
function tabelle(breiten, kopf, zeilen, o = {}) {
  const gesamt = breiten.reduce((a, b) => a + b, 0);
  const rows = [];
  if (kopf) rows.push(new TableRow({ tableHeader: true, children: kopf.map((k, i) => zelle(k, breiten[i], { fill: GRUEN, color: "FFFFFF", bold: true, align: o.kopfAlign && o.kopfAlign[i] })) }));
  zeilen.forEach(z => rows.push(new TableRow({
    height: o.hoehe ? { value: o.hoehe, rule: HeightRule.ATLEAST } : undefined, cantSplit: true,
    children: z.map((c, i) => {
      if (c && typeof c === "object" && !Array.isArray(c) && c.text !== undefined)
        return zelle(c.text, c.span ? breiten.slice(i, i + c.span).reduce((a, b) => a + b, 0) : breiten[i], c);
      return zelle(c, breiten[i], { fill: o.label && i === 0 ? SAND : undefined, bold: o.label && i === 0, align: o.mitte && i > 0 ? AlignmentType.CENTER : undefined });
    }),
  })));
  return [new Table({ width: { size: gesamt, type: WidthType.DXA }, columnWidths: breiten, rows }), new Paragraph({ children: [], spacing: { after: 120 } })];
}
const felder = (breite, liste, hoehe = 520) => tabelle([Math.round(breite * 0.3), breite - Math.round(breite * 0.3)], null, liste.map(x => [x, ""]), { label: true, hoehe });
const skala = ["[]", "[]", "[]", "[]"];

function abschnitt(nr, kopfText, kinder, quer = false) {
  return {
    properties: { page: { size: { width: 11906, height: 16838, orientation: quer ? PageOrientation.LANDSCAPE : PageOrientation.PORTRAIT },
      margin: { top: 1134, bottom: 1134, left: 1134, right: 1134, header: 567, footer: 567 } } },
    headers: { default: new Header({ children: [new Paragraph({ children: [r(`Smart City Projekt · Vorlage ${nr} · ${kopfText} · Anja Muggli · mugglionline.ch`, { size: 15, color: GRAU })] })] }) },
    footers: { default: new Footer({ children: [new Paragraph({ children: [r("Vorlage · frei nutzbar und anpassbar mit Quellenangabe", { size: 15, color: GRAU }), r("\t", { size: 15 }), new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 15, color: GRAU })],
      tabStops: [{ type: "right", position: quer ? W_QUER : W_HOCH }] })] }) },
    children: kinder,
  };
}

// ---------- SC1 Auftragsblatt ----------
const W = W_HOCH;
const SC1 = abschnitt("SC1", "Auftragsblatt", [
  kicker("Vorlage SC1 · für Lernende"), titel("Smart City Projekt: Eure Offerte für die Stadt"),
  unter("Gruppe: ______________________________   Firma: ______________________________"),
  p("Die Stadt **____________________** möchte eine **Smart City** werden: eine vernetzte Stadt mit hoher Lebensqualität, die Energie und Ressourcen klug einsetzt. Sie sucht eine Firma, die dieses Projekt plant."),
  p("Ihr gründet in Gruppen von drei bis vier Personen eine Firma und bewerbt euch mit einer **Offerte**. Die übrige Klasse spielt das **City Board** der Stadt. Es hört sich alle Offerten an und vergibt am Schluss den Auftrag."),
  h("Unsere Variante"),
  ...tabelle([600, W - 600], null, [
    ["[]", "**Realitätsnah:** Nur Technologien, die es heute gibt oder die schon getestet werden. Kosten belegt ihr mit Quellen."],
    ["[]", "**Fantasy:** Zukunftsideen sind erlaubt, zum Beispiel fliegende Taxis. Jede Idee braucht eine plausible Erklärung, einen klaren Nutzen und eine begründete Kostenschätzung."],
  ]),
  p("**Pflicht für alle:** Mindestens eine Idee hat mit erneuerbarer Energie oder Ressourcen zu tun. Ihr zeigt, was die Stadt für Umwelt, Gesellschaft und Wirtschaft gewinnt."),
  h("Eure Schritte"),
  ...tabelle([500, 2300, 3600, 2000, 1238], ["", "Schritt", "Was ihr macht", "Ergebnis", "Termin"], [
    ["1", "Firma gründen", "Gruppe bilden, Rollen wählen, Gruppenvertrag", "SC4 unterschrieben", ""],
    ["2", "Methode kennen", "Projektmanagement-Modell kennenlernen, Projektplan anlegen", "Projektplan SC3", ""],
    ["3", "Recherchieren", "Was ist eine Smart City? Wie ist eure Stadt? Echte Beispiele. Alles ins Arbeitsjournal.", "Journal SC5, Ideenliste", ""],
    ["4", "Offerte schreiben", "Idee, Lieferobjekte, Phasen, Zeitplan, Budget, Nutzen", "Offerte SC2, Zwischen-Check", ""],
    ["5", "Präsentation vorbereiten", "Folien gestalten, Fragen voraussehen, proben", "Präsentation, Probe", ""],
    ["6", "Präsentieren und bewerten", "Offerte präsentieren, als City Board zuhören, euch selbst einschätzen", "SC9, SC10", ""],
  ]),
  h("Das gehört in eure Präsentation"),
  ...bullets(["Titelfolie, eure Firma, Übersicht", "Hintergrund zur Stadt", "eure Idee und eure Lieferobjekte (was die Stadt bekommt)", "Phasen mit Beschreibung der Arbeiten, Zeitplan und Budget für jede Phase", "Zielgruppe und Nutzen für die Stadt", "ein starker Schluss: Warum sollte die Stadt euch wählen?"]),
  h("Bewertung"),
  ...bullets(["**Offerte** (Vorlage SC2): ½ Note, Raster SC7. Rechtschreibung wird nicht bewertet. Dafür schreibt ihr in **euren eigenen Worten**, ohne Übersetzer oder KI für ganze Sätze.",
    "**Präsentation**: 1 Note, Raster SC8.", "Die Lehrperson kann zusätzlich eine Prozessnote geben (Journal, Zwischen-Checks, Zusammenarbeit)."]),
  h("KI-Ampel"),
  ...tabelle([W / 3, W / 3, W - 2 * Math.round(W / 3)].map(Math.round), ["Grün: erlaubt", "Gelb: nur mit Protokoll", "Rot: nicht erlaubt"], [[
    "nach eurem eigenen Brainstorming weitere Ideen holen; Suchbegriffe finden; Rückmeldung zum Aufbau; Fragen des City Boards üben",
    "Fakten und Kosten erfragen und danach mit einer Quelle belegen; Bilder erzeugen und auf der Folie kennzeichnen",
    "Sätze oder Abschnitte der Offerte schreiben oder übersetzen lassen; Präsentationstext erzeugen; Personendaten eingeben"]]),
  p("Jede KI-Nutzung kommt ins KI-Protokoll eures Arbeitsjournals."),
  h("Abgabe und Regeln"),
  ...bullets(["Offerte und Präsentation ladet ihr am Präsentationstag **vor Lektionsbeginn** auf Teams hoch, auch wenn ihr an diesem Tag fehlt.",
    "Für jeden Tag Verspätung gibt es einen Abzug. Arbeiten, die mehr als zwei Tage zu spät sind, werden nicht mehr angenommen.",
    "«Jemand anders hätte es hochladen sollen» gilt nicht als Entschuldigung. Die ganze Gruppe trägt den Abzug.",
    "Läuft es in der Gruppe nicht gut? Meldet euch **früh** bei der Lehrperson."]),
]);

// ---------- SC2 Offerte ----------
const SC2 = abschnitt("SC2", "Offerte-Vorlage", [
  kicker("Vorlage SC2 · für Lernende · zählt ½ Note"), titel("Offerte an das City Board"),
  unter("Schreibt in euren eigenen Worten. Rechtschreibung wird nicht bewertet. Zeigt die Offerte beim Zwischen-Check, bevor ihr mit der Präsentation beginnt."),
  h("1 · Unsere Firma"),
  ...felder(W, ["Name der Firma", "Logo oder Slogan", "Mitglieder und Rollen", "Was macht uns besonders?"]),
  h("2 · Die Stadt"),
  ...felder(W, ["Name, Land, Einwohnerzahl", "Drei Herausforderungen der Stadt", "Stärken der Stadt", "Quellen (Kürzel aus dem Journal)"]),
  h("3 · Unsere Idee"),
  ...felder(W, ["Variante", "Unsere Vision in zwei bis drei Sätzen: So sieht die Stadt nach unserem Projekt aus."], 900),
  h("4 · Lieferobjekte: Was bekommt die Stadt?"),
  ...tabelle([2300, 2600, 2400, 2338], ["Komponente", "Was ist das? Wie funktioniert es?", "Welches Problem löst es?", "Nachhaltigkeit: Umwelt, Gesellschaft, Wirtschaft"], [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]], { hoehe: 900 }),
  h("5 · Phasen, Zeitplan und Budget"),
  p("Nutzt die Phasen eures Projektmanagement-Modells (zum Beispiel IPERKA oder HERMES)."),
  ...tabelle([2000, 3700, 2000, 1938], ["Phase", "Was passiert in dieser Phase?", "Dauer (von – bis)", "Kosten in CHF"],
    [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""], [{ text: "**Total**", span: 2, fill: SAND }, "", ""]], { hoehe: 800 }),
  p("So haben wir die Kosten geschätzt (Quellen, Annahmen):"), ...linien(3),
  h("6 · Zielgruppe"),
  ...felder(W, ["Wer profitiert? (Stadt, Bevölkerungsgruppen, Wirtschaft, Umwelt)"], 900),
  h("7 · Nutzen für die Stadt"),
  ...felder(W, ["Argument 1", "Argument 2", "Argument 3"]),
  h("8 · Risiken und Lösungen (Gymnasium und Berufsschule)"),
  ...tabelle([W / 2, W / 2], ["Was könnte schiefgehen?", "Wie reagieren wir?"], [["", ""], ["", ""]], { hoehe: 600 }),
  h("Zwischen-Check"),
  ...tabelle([3200, 3200, 3238], null, [["Datum:", "Visum Lehrperson:", "[] freigegeben für die Präsentation"]]),
]);

// ---------- SC3 Projektplan ----------
const L = 12;
const SC3 = abschnitt("SC3", "Projektplan", [
  kicker("Vorlage SC3 · für Lernende"), titel("Unser Projektplan"),
  unter("Firma: ____________________________   Projektleitung: ____________________________"),
  p("Das Modell **IPERKA** beschreibt, wie ein Projekt vollständig abläuft. **Realschule:** Ihr nutzt nur die vier farbigen Zeilen (Informieren, Planen, Realisieren, Auswerten). **Berufsschule:** Ihr ersetzt die Schritte durch die HERMES-Phasen Initialisierung, Konzept, Realisierung, Einführung, Abschluss."),
  ...tabelle([1500, 2700, 2700, 1200, 1100, 438], ["Schritt", "Leitfrage", "Was wir tun", "Wer", "Bis wann", "✓"], [
    [{ text: "**Informieren**", fill: SAND }, "Was müssen wir wissen? Was ist eine Smart City, wie ist unsere Stadt?", "", "", "", "[]"],
    [{ text: "**Planen**", fill: SAND }, "Welche Ideen haben wir? Welche Aufgaben, welche Reihenfolge?", "", "", "", "[]"],
    ["**Entscheiden**", "Welche drei bis fünf Ideen nehmen wir? Warum?", "", "", "", "[]"],
    [{ text: "**Realisieren**", fill: SAND }, "Offerte schreiben, Präsentation gestalten", "", "", "", "[]"],
    ["**Kontrollieren**", "Stimmen Zeitplan und Budget? Ist alles vollständig? Probe", "", "", "", "[]"],
    [{ text: "**Auswerten**", fill: SAND }, "Was lief gut, was machen wir nächstes Mal anders?", "", "", "", "[]"],
  ], { hoehe: 700 }),
  h("Zeitplan über die Lektionen"),
  p("Malt aus, in welchen Lektionen ihr woran arbeitet. Tragt Meilensteine (M1, M2, M3) ein."),
  ...tabelle([2638, ...Array(L).fill(Math.round(7000 / L))].map((x, i) => i === 0 ? 2638 + (7000 - Math.round(7000 / L) * L) : x),
    ["Aufgabe", ...Array.from({ length: L }, (_, i) => `L${i + 1}`)],
    Array.from({ length: 6 }, () => Array(L + 1).fill("")), { hoehe: 380 }),
  umbruch(), h("Kanban-Board"),
  p("Schreibt jede Aufgabe auf eine Karte oder in eine Zeile. Am Anfang jeder Lektion schiebt ihr die Karten weiter (5-Minuten-Standup)."),
  ...tabelle([W / 3, W / 3, W - 2 * Math.round(W / 3)].map(Math.round), ["To do", "Doing", "Done"], [["", "", ""]], { hoehe: 11000 }),
]);

// ---------- SC4 Rollen ----------
const rolle = (name, aufgaben, frage, gut) => [
  new Paragraph({ children: [r(name, { size: 24, bold: true, color: GRUEN })], spacing: { after: 60 } }),
  ...aufgaben.map(t => new Paragraph({ children: runs("– " + t, { size: 18 }), spacing: { after: 30 } })),
  new Paragraph({ children: runs("**Leitfrage:** " + frage, { size: 18 }), spacing: { before: 60, after: 30 } }),
  new Paragraph({ children: runs("**Passt zu dir, wenn** " + gut, { size: 18 }), spacing: { after: 0 } }),
];
const SC4 = abschnitt("SC4", "Rollen und Gruppenvertrag", [
  kicker("Vorlage SC4 · für Lernende"), titel("Rollenkarten und Gruppenvertrag"),
  unter("Alle recherchieren, schreiben und präsentieren mit. Die Rolle bedeutet zusätzliche Verantwortung. Bei drei Personen übernimmt die Projektleitung auch die Finanzen."),
  ...tabelle([W / 2, W / 2], null, [
    [rolle("Projektleitung", ["führt das Kanban-Board und den Zeitplan", "leitet die Standups am Lektionsbeginn", "ist Kontaktperson zur Lehrperson"], "Sind wir im Zeitplan?", "du gern den Überblick behältst oder das lernen möchtest."),
     rolle("Recherche und Qualität", ["sammelt und prüft Quellen", "achtet darauf, dass das Journal vollständig ist", "macht den Faktencheck, auch bei KI-Antworten"], "Stimmt das, und woher wissen wir es?", "du gern genau hinschaust.")],
    [rolle("Finanzen und Planung", ["erstellt das Budget pro Phase", "prüft alle Zahlen nach", "plant, wie lange jede Phase dauert"], "Ist das realistisch und bezahlbar?", "du gern mit Zahlen arbeitest."),
     rolle("Design und Kommunikation", ["gestaltet Folien, Logo und Grafiken", "achtet auf Kennzeichnung von Bildern und KI-Bildern", "organisiert die Probe-Präsentation"], "Versteht das City Board uns sofort?", "du gern gestaltest und präsentierst.")],
  ], { hoehe: 2600 }),
  h("Stärken-Runde"),
  ...tabelle([2400, 2800, 2800, 1638], ["Name", "Das kann ich gut", "Das möchte ich lernen", "Meine Rolle"], [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]], { hoehe: 600 }),
  umbruch(),
  kicker("Vorlage SC4 · Gruppenvertrag"), titel("Gruppenvertrag der Firma ______________"),
  h("Unsere Regeln"), ...linien(5),
  h("So kommunizieren wir"),
  ...felder(W, ["Kanal (z. B. Teams-Chat)", "Wir antworten innerhalb von", "Wer fehlt, informiert so"]),
  h("Wenn jemand Abmachungen nicht einhält"),
  ...tabelle([600, W - 600], null, [["1.", "Wir sprechen es in der Gruppe direkt und freundlich an."], ["2.", ""], ["3.", "Wenn es nicht besser wird, holen wir die Lehrperson dazu."]], { hoehe: 480 }),
  h("Unterschriften"),
  ...tabelle([W / 4, W / 4, W / 4, W / 4].map(Math.round), null, [["", "", "", ""]], { hoehe: 800 }),
  p("Datum: ______________   Überprüft nach dem Zwischen-Check M2: [] Rollen passen   [] wir ändern: ______________________"),
]);

// ---------- SC5 Journal ----------
const SC5 = abschnitt("SC5", "Arbeitsjournal", [
  kicker("Vorlage SC5 · für Lernende"), titel("Arbeitsjournal"),
  unter("Firma: ____________________________   Das Journal zeigt euren Weg. Es ist Grundlage für die Zwischen-Checks."),
  h("So legt ihr das Journal in OneNote an"),
  ...bullets(["Abschnitt mit eurem Firmennamen im Klassennotizbuch", "Seite **Quellen**: ein Eintrag pro Website mit Screenshot (Windows: Windows + Shift + S, Mac: Cmd + Shift + 4), URL und Datum",
    "Seite **KI-Protokoll**: jede Nutzung von KI", "Seite **Standups**: kurze Notizen am Anfang jeder Lektion", "Seite **Ideen**: Brainstorming, Skizzen, Entscheide"]),
  p("Ohne OneNote könnt ihr die Tabellen unten verwenden."),
  h("Quellenprotokoll"),
  ...tabelle([1000, 2400, 900, 3000, 2338], ["Datum", "Quelle (URL, Titel)", "Screen-shot", "Was habe ich gelernt? (eigene Worte)", "Vertrauenswürdig? Wer, wann, mit welchem Ziel?"],
    Array.from({ length: 6 }, () => ["", "", "[]", "", ""]), { hoehe: 900 }),
  h("KI-Protokoll"),
  ...tabelle([900, 1100, 2200, 1800, 1900, 1738], ["Datum", "Tool", "Eingabe (Prompt)", "Antwort kurz", "Übernommen?", "So haben wir geprüft"],
    Array.from({ length: 5 }, () => ["", "", "", "", "[] ja [] teilw. [] nein", ""]), { hoehe: 900 }),
  h("Standups"),
  ...tabelle([1100, 2900, 2900, 2738], ["Datum", "Das haben wir erledigt", "Das machen wir heute (wer?)", "Hier hängen wir"],
    Array.from({ length: 6 }, () => ["", "", "", ""]), { hoehe: 600 }),
]);

// ---------- SC6 Zwischen-Check ----------
const check = (titelM, punkte) => [h(titelM),
  ...tabelle([4800, 600, 600, 600, 3038], ["Kriterium", "✓", "~", "✗", "Notiz"], punkte.map(t => [t, "[]", "[]", "[]", ""]), { mitte: true }),
  p("**Vereinbarung bis zum nächsten Mal:**"), ...linien(2)];
const SC6 = abschnitt("SC6", "Zwischen-Checks", [
  kicker("Vorlage SC6 · für die Lehrperson"), titel("Zwischen-Checks"),
  unter("Firma: ________________________   Mitglieder: _______________________________________________"),
  ...check("M1 · Ideen   Datum: ________", ["Rollen verteilt, Gruppenvertrag unterschrieben", "Projektplan angelegt, Kanban-Board läuft", "3 bis 5 Komponenten, mindestens eine zu erneuerbarer Energie oder Ressourcen", "mindestens drei Quellen im Journal, mit Screenshot und eigenen Worten", "Arbeit ist sichtbar auf alle verteilt"]),
  ...check("M2 · Offerte   Datum: ________", ["Offerte vollständig ausgefüllt", "Phasen logisch, passend zum Modell", "Zeitplan realistisch", "Budget nachvollziehbar und begründet", "in eigenen Worten geschrieben, KI-Protokoll geführt"]),
  p("[] **Freigabe für die Präsentation**"),
  ...check("M3 · Probe   Datum: ________", ["Zeit eingehalten", "weitgehend frei gesprochen", "Folien unterstützen, statt alles vorzulesen", "auf Fragen reagiert"]),
  h("Coaching-Fragen (GROW)"),
  ...bullets(["**Ziel:** Was wollt ihr heute fertig haben?", "**Stand:** Zeigt mir euer Kanban-Board. Wo steht ihr?", "**Möglichkeiten:** Was könntet ihr tun, wenn ihr nicht weiterkommt?", "**Nächster Schritt:** Wer macht was bis wann?"]),
]);

// ---------- Raster ----------
const legende = p("**Skala:** 0 = fehlt · 1 = ansatzweise · 2 = grösstenteils erfüllt · 3 = vollständig und überzeugend", { color: GRAU, size: 18 });
const rasterZeilen = (liste, max = 3) => liste.map(t => [t, ...Array.from({ length: max + 1 }, () => "[]"), ""]);
const SC7_KRIT = ["Firma vorgestellt (Name, Mitglieder, Rollen)", "Hintergrund zur Stadt mit Quellen", "Idee und Vision klar beschrieben", "Lieferobjekte: Was ist es, welches Problem löst es?", "Phasen mit Beschreibung der Arbeiten", "Zeitplan für jede Phase, realistisch", "Budget für jede Phase, begründet", "Zielgruppe benannt", "Nutzen für die Stadt überzeugend begründet", "Nachhaltigkeit: Umwelt, Gesellschaft, Wirtschaft", "in eigenen Worten, verständlich", "Quellen und Journal nachvollziehbar"];
const SC7 = abschnitt("SC7", "Bewertungsraster Offerte", [
  kicker("Vorlage SC7 · Bewertung · ½ Note"), titel("Bewertungsraster Offerte"),
  unter("Firma: ________________________   Mitglieder: _______________________________________________"),
  legende,
  ...tabelle([5038, 650, 650, 650, 650, 2000], ["Kriterium", "0", "1", "2", "3", "Feedback"], [...rasterZeilen(SC7_KRIT), [{ text: "**Total**", fill: SAND }, { text: "**____ / 36**", span: 4, align: AlignmentType.CENTER, fill: SAND }, ""]], { mitte: true }),
  p("Rechtschreibung wird nicht bewertet. Wurden ganze Sätze mit Übersetzer oder KI geschrieben, wird das Kriterium «in eigenen Worten» mit 0 bewertet und die Lehrperson bespricht das mit der Gruppe."),
  p("**Note:** Punkte ÷ 36 × 5 + 1 = ________ (gerundet nach den Vorgaben der Schule)"),
  h("Rückmeldung"), ...linien(4),
]);
const SC8_TEIL = [
  ["Einstieg", ["Titelfolie", "Firma vorgestellt", "Übersicht der Themen"], 1],
  ["Inhalt und Gestaltung", ["Hintergrund zur Stadt", "Idee der Firma", "Lieferobjekte", "Phasen (Beschreibung der Arbeiten)", "Zeitplan für jede Phase", "Budget für jede Phase", "Zielgruppe", "Nutzen für die Stadt", "Nachhaltigkeit (Umwelt, Gesellschaft, Wirtschaft)", "starker Schluss"], 3],
  ["Auftritt", ["klar und professionell gesprochen", "angemessenes Tempo", "Fachbegriffe verwendet", "frei gesprochen", "Folien als visuelle Unterstützung genutzt", "mehr erklärt, als auf den Folien steht", "Fragen des City Boards beantwortet", "alle Mitglieder präsentieren"], 3],
];
const raster8 = () => {
  const out = [];
  SC8_TEIL.forEach(([teil, krit, max]) => {
    const kopf = ["Kriterium", "0", "1", "2", "3", "Feedback"];
    const zeilen = krit.map(t => [t, "[]", "[]", max >= 2 ? "[]" : "–", max >= 3 ? "[]" : "–", ""]);
    zeilen.push([{ text: `**Total ${teil}**`, fill: SAND }, { text: `**____ / ${krit.length * max}**`, span: 4, align: AlignmentType.CENTER, fill: SAND }, ""]);
    out.push(h(teil), ...tabelle([5038, 650, 650, 650, 650, 2000], kopf, zeilen, { mitte: true }));
  });
  return out;
};
const SC8 = abschnitt("SC8", "Bewertungsraster Präsentation", [
  kicker("Vorlage SC8 · Bewertung · 1 Note"), titel("Bewertungsraster Präsentation"),
  unter("Firma: ________________________   Mitglieder: _______________________________________________"),
  p("**Einstieg:** 0 = fehlt, 1 = vorhanden. **Inhalt und Auftritt:** 0 = fehlt · 1 = ansatzweise · 2 = grösstenteils · 3 = vollständig und überzeugend", { color: GRAU, size: 18 }),
  ...raster8(),
  p("**Gesamt:** ____ / 57   **Note:** Punkte ÷ 57 × 5 + 1 = ________", { before: 120 }),
  p("Optional Anteil City Board (vorher angekündigt): ________   Selbsteinschätzung der Gruppe (SC10): ________"),
  h("Rückmeldung"), ...linien(4),
]);

// ---------- SC9 City Board (quer) ----------
const WQ = W_QUER;
const SC9 = abschnitt("SC9", "City-Board-Notizen", [
  kicker("Vorlage SC9 · für Lernende"), titel("City Board: Unsere Notizen"),
  unter("Name: ____________________   Ihr seid das City Board der Stadt. Notiert zu jeder Firma Stichworte. Eure eigene Firma lasst ihr aus."),
  ...tabelle([1900, 2534, 2534, 2534, 2534, 2534], ["Firma", "Lieferobjekte: Welche Ideen haben sie für die Stadt?", "Zeitplan: Wie genau? Ist er machbar?", "Budget: Vernünftig? Stimmt das Preis-Leistungs-Verhältnis?", "Nutzen: Wer profitiert? Stadt, Bevölkerung?", "Kreativität: Wie überzeugend verkaufen sie ihre Idee?"],
    [...Array.from({ length: 6 }, () => ["", "", "", "", "", ""]), [{ text: "**Gewinner der Kategorie und warum**", fill: SAND }, "", "", "", "", ""]], { hoehe: 820 }),
  p("**Meine kritische Frage an eine Firma:** _____________________________________________________________________________________"),
  p("**Den Gesamtauftrag gebe ich der Firma** ____________________, **weil** _________________________________________________________"),
], true);

// ---------- SC10 Selbsteinschätzung ----------
const SC10 = abschnitt("SC10", "Selbsteinschätzung", [
  kicker("Vorlage SC10 · für Lernende"), titel("Selbsteinschätzung der Gruppe"),
  unter("Firma: ________________________   Füllt Teil A vor der Präsentation gemeinsam aus, Teil C allein und vertraulich."),
  h("A · So schätzen wir unsere Präsentation ein"),
  p("Füllt gemeinsam das Raster SC8 aus und tragt hier die Summen ein."),
  ...tabelle([3800, 1800, 1800, 2238], ["Bereich", "Unsere Punkte", "Maximum", "Darauf sind wir stolz"], [["Einstieg", "", "3", ""], ["Inhalt und Gestaltung", "", "30", ""], ["Auftritt", "", "24", ""], [{ text: "**Total und erwartete Note**", fill: SAND }, "", "57", ""]], { hoehe: 520 }),
  h("B · Unsere Zusammenarbeit"),
  ...tabelle([5638, 1000, 1000, 1000, 1000], ["", "trifft nicht zu", "eher nicht", "eher", "trifft zu"], [
    ["Wir haben Termine und Abmachungen eingehalten.", ...skala], ["Alle haben ihre Rolle wahrgenommen.", ...skala], ["Alle konnten ihre Ideen einbringen.", ...skala],
    ["Wir haben Probleme früh angesprochen.", ...skala], ["Unser Journal zeigt ehrlich, wer was gemacht hat.", ...skala]], { mitte: true }),
  h("C · Beitragsverteilung (allein und vertraulich)"),
  p("Verteile **100 Punkte** auf alle Mitglieder, dich selbst eingeschlossen. Haben alle gleich viel beigetragen, bekommen alle gleich viele Punkte."),
  ...tabelle([3000, 1500, 5138], ["Name", "Punkte", "Begründung (kurz)"], [["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""], [{ text: "**Summe**", fill: SAND }, "100", ""]], { hoehe: 480 }),
  p("Mein Name: ____________________"),
  h("D · Reflexion"),
  p("**Lessons learned:** Was hat gut funktioniert? Was machen wir beim nächsten Projekt anders?"), ...linien(3),
  p("**KI:** Wo hat KI geholfen, wo hat sie Fehler gemacht, wo haben wir bewusst ohne gearbeitet?", { before: 120 }), ...linien(3),
  p("**Mein Ziel:** Diese Kompetenz will ich weiterentwickeln:", { before: 120 }), ...linien(2),
]);

// ---------- Speichern ----------
const STIL = {
  default: { document: { run: { font: FONT, size: 20 } } },
};
const NUM = { config: [{ reference: "punkte", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 240 } } } }] }] };
const DOKS = [["SC1_Auftragsblatt", SC1], ["SC2_Offerte-Vorlage", SC2], ["SC3_Projektplan", SC3], ["SC4_Rollenkarten_und_Gruppenvertrag", SC4], ["SC5_Arbeitsjournal", SC5],
  ["SC6_Zwischen-Check", SC6], ["SC7_Bewertungsraster_Offerte", SC7], ["SC8_Bewertungsraster_Praesentation", SC8], ["SC9_City-Board-Notizen", SC9], ["SC10_Selbsteinschaetzung", SC10]];
(async () => {
  for (const [name, sec] of DOKS) {
    const doc = new Document({ creator: "Anja Muggli", title: name.replace(/_/g, " "), styles: STIL, numbering: NUM, sections: [sec] });
    fs.writeFileSync(path.join(OUT, name + ".docx"), await Packer.toBuffer(doc));
  }
  const alle = new Document({ creator: "Anja Muggli", title: "Smart City Projekt: alle Vorlagen", styles: STIL, numbering: NUM, sections: DOKS.map(d => d[1]) });
  fs.writeFileSync(path.join(OUT, "Smart_City_alle_Vorlagen.docx"), await Packer.toBuffer(alle));
  console.log("Word-Dateien erstellt:", DOKS.length + 1);
})();
// PDF:  cd downloads/smart-city && soffice --headless --convert-to pdf *.docx
