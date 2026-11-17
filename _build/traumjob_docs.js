// Erzeugt die Vorlagen zum Auftrag «Mein Traumjob» als Word-Dateien (Stil: _build/vorlagen_stil.js).
// Aufruf im Repository-Ordner:  node _build/traumjob_docs.js   danach  sh _build/vorlagen_pdf.sh downloads/traumjob
const fs = require("fs");
const path = require("path");
const { Document, Packer, Paragraph, Table, TableRow, TableCell, WidthType, AlignmentType, BorderStyle } = require("docx");
const S = require("./vorlagen_stil");

const OUT = path.join(__dirname, "..", "downloads", "traumjob");
fs.mkdirSync(OUT, { recursive: true });
const W = S.W_HOCH;
const KZ = (nr, t) => `Mein Traumjob · Vorlage ${nr} · ${t}`;
const F = S.FARBEN;

function farbSpalten(spalten, hoehe) {
  const b = Math.floor(W / spalten.length);
  return [new Table({ width: { size: b * spalten.length, type: WidthType.DXA }, columnWidths: Array(spalten.length).fill(b), rows: [new TableRow({
    height: hoehe ? { value: hoehe, rule: "atLeast" } : undefined,
    children: spalten.map(([titel, text, f]) => new TableCell({ width: { size: b, type: WidthType.DXA },
      borders: { top: { style: "single", size: 24, color: f.dunkel }, bottom: S.OHNE_RAND.bottom, left: { style: "single", size: 24, color: "FFFFFF" }, right: { style: "single", size: 24, color: "FFFFFF" } },
      shading: { fill: f.hell, type: "clear", color: "auto" }, margins: { top: 120, bottom: 120, left: 160, right: 160 },
      children: [new Paragraph({ children: S.runs(titel, { bold: true, color: f.dunkel, size: 21 }), spacing: { after: 60 } }),
        ...(Array.isArray(text) ? text : [new Paragraph({ children: S.runs(text, { size: 18 }), spacing: { after: 0, line: 252 } })])] })) })] }), new Paragraph({ children: [], spacing: { after: 120 } })];
}
const punkte = (liste, size = 18) => liste.map(t => new Paragraph({ children: S.runs("• " + t, { size }), spacing: { after: 30, line: 252 } }));

// ---------- TJ1 Auftragsblatt ----------
let v = S.mit("lavendel", "weg");
const TJ1 = v.abschnitt(KZ("TJ1", "Auftragsblatt"), [
  ...v.kopf({ kicker: "Vorlage TJ1 · für Lernende", titel: "Mein Traumjob: vom Interesse zum Plan", felder: ["Name", "Klasse", "Abgabe"] }),
  v.p("Stell dir vor, du hast deine Ausbildung abgeschlossen oder suchst bald eine Lehrstelle. Welcher Beruf würde zu dir passen? In welchem Betrieb würdest du gern arbeiten? Wie sähe dein Alltag aus?"),
  v.p("In diesem Projekt findest du es heraus. Du erkundest einen Beruf und einen echten Betrieb, bereitest eine Bewerbung vor und zeigst deinen Plan auf einem **Poster** oder in einem **digitalen Portfolio**. Zum Schluss präsentierst du ihn."),
  v.h("Meine Variante"),
  ...farbSpalten([
    ["[] Region", "Ein Betrieb in meiner Region. Ich erkunde meinen Arbeitsweg und die Ortschaft. Alles auf Deutsch.", F.bergsee],
    ["[] Ausland", "Eine Stelle in einem Land, in dem meine Fremdsprache gesprochen wird. Alles in der Fremdsprache, dazu Bewilligungen und Wohnen.", F.gletscher]]),
  v.h("Meine Schritte"),
  ...v.tabelle([500, 2300, 3800, 1800, 1238], ["", "Schritt", "Was ich mache", "Vorlage", "Termin"], [
    [{ text: "**1**", fill: true }, "Traumberuf entdecken", "Interessen-Check, Berufe erkunden, einen Beruf wählen", "TJ2, TJ6", ""],
    [{ text: "**2**", fill: true }, "Traumbetrieb finden", "Einen echten Betrieb suchen und kennenlernen", "TJ2", ""],
    [{ text: "**3**", fill: true }, "Arbeitsort erkunden", "Arbeitsweg, Ortschaft, Alltag, Lohn und Arbeitszeit", "TJ2", ""],
    [{ text: "**4**", fill: true }, "Bewerbung vorbereiten", "Inserat, Lebenslauf, Motivationsschreiben, Gespräch üben", "TJ3, TJ4", ""],
    [{ text: "**5**", fill: true }, "Poster oder Portfolio", "Ergebnisse übersichtlich gestalten", "TJ5", ""],
    [{ text: "**6**", fill: true }, "Präsentieren und reflektieren", "Berufsmesse oder Präsentation mit Gespräch, Selbsteinschätzung", "TJ10", ""],
  ]),
  ...v.kasten("Wichtig", "Dein Plan darf ehrgeizig sein, soll aber **realistisch** bleiben. Wenn dir für deinen Wunschberuf noch etwas fehlt, zeigst du, wie du es erreichen kannst. Belege alles mit Quellen in deinem Lernjournal (TJ6).", F.terrakotta),
  v.h("Bewertung"),
  ...v.bullets(["**Poster oder Portfolio:** 1 Note, Raster TJ8", "**Präsentation:** 1 Note, Raster TJ9", "Optional **Bewerbungsdossier:** 1 Note, Checkliste in TJ3"]),
  v.h("KI-Ampel"),
  ...farbSpalten([
    ["Grün: erlaubt", "nach deinem Interessen-Check ein Interview mit der KI führen; Fragen für Interviews finden; Rückmeldung zum Aufbau ohne Personendaten; Gespräch üben", F.bergsee],
    ["Gelb: nur mit Protokoll", "Infos zu Beruf, Lohn oder Betrieb erfragen und mit einer offiziellen Quelle bestätigen; Bilder erzeugen und kennzeichnen", F.terrakotta],
    ["Rot: nicht erlaubt", "Motivationsschreiben oder Lebenslauf schreiben oder übersetzen lassen; Adresse, Geburtsdatum, Foto oder Zeugnisse eingeben; Angaben erfinden", F.alpenrose]]),
]);

// ---------- TJ2 Recherche-Heft ----------
v = S.mit("bergsee", "weg");
const TJ2 = v.abschnitt(KZ("TJ2", "Recherche-Heft"), [
  ...v.kopf({ kicker: "Vorlage TJ2 · für Lernende", titel: "Recherche-Heft", unter: "Fülle für jeden Teil den Steckbrief aus. Notiere die Quellen im Lernjournal (TJ6).", felder: ["Name", "Variante"] }),
  v.h("Teil 1 · Mein Traumberuf", F.lavendel),
  ...v.tabelle([3000, W - 3000], null, [["Das mache ich gern", ""], ["Das fällt mir leicht", ""], ["Ergebnis meines Interessen-Checks", ""], ["Drei Berufe, die mich interessieren", ""]], { label: true, hoehe: 560, farbe: F.lavendel }),
  v.p("**Steckbrief Beruf:** ____________________________________", { before: 80 }),
  ...v.felder(W, ["Typische Tätigkeiten im Alltag", "Ausbildung (Dauer, Schule, Abschluss)", "Anforderungen: Schulfächer, Fähigkeiten, Eigenschaften", "Weiterbildungen und Karriere", "Darum passt der Beruf zu mir"], 620),
  v.h("Teil 2 · Mein Traumbetrieb", F.terrakotta),
  ...v.tabelle([3000, W - 3000], null, [["Name und Ort", ""], ["Produkte oder Dienstleistungen", ""], ["Grösse, Geschichte, Kundschaft", ""], ["Werte und Arbeitsklima", ""], ["Ausbildungsplätze oder offene Stellen", ""], ["Warum dieser Betrieb und nicht ein anderer?", ""]], { label: true, hoehe: 620, farbe: F.terrakotta }),
  v.h("Teil 3 · Mein Arbeitsort", F.gletscher),
  ...v.tabelle([3000, W - 3000], null, [["Arbeitsweg (Verkehrsmittel, Umsteigen)", ""], ["Pendelzeit pro Tag", ""], ["Das gibt es in der Ortschaft", ""], ["Freizeit nach der Arbeit", ""], ["Vergleich mit meinem Wohnort", ""]], { label: true, hoehe: 560, farbe: F.gletscher }),
  v.h("Teil 4 · Rahmenbedingungen", F.alpenrose),
  ...v.tabelle([3000, W - 3000], null, [["Lohn im Lehrjahr bzw. Einstiegslohn", ""], ["Arbeitszeit pro Woche", ""], ["Ferien", ""], ["Berufsschule (Tage, Ort)", ""], ["Variante Ausland: Bewilligung, Anerkennung meines Abschlusses (nur offizielle Quellen)", ""]], { label: true, hoehe: 560, farbe: F.alpenrose }),
  v.h("Teil 5 · Wohnen und Budget (Gymnasium und Berufsschule)", F.lavendel),
  ...v.tabelle([2400, 1800, 1800, 1800, 1838], ["", "Wohnung 1", "Wohnung 2", "Wohnung 3", "Meine Wahl"], [["Lage", "", "", "", ""], ["Grösse, Zimmer", "", "", "", ""], ["Miete pro Monat", "", "", "", ""], ["Weg zur Arbeit", "", "", "", ""]], { label: true, hoehe: 380, farbe: F.lavendel }),
  ...v.tabelle([4819, 2400, 2419], ["Monatsbudget", "Betrag CHF", "Quelle"], [["Einnahmen: Lohn netto", "", ""], ["Miete und Nebenkosten", "", ""], ["Krankenkasse", "", ""], ["Essen", "", ""], ["Verkehr", "", ""], ["Handy, Internet", "", ""], ["Freizeit", "", ""], ["Sparen", "", ""], [{ text: "**Bleibt übrig**", fill: true }, { text: "", fill: true }, { text: "", fill: true }]], { label: true, hoehe: 320, farbe: F.lavendel }),
]);

// ---------- TJ3 Bewerbungswerkstatt ----------
v = S.mit("terrakotta", "weg");
const TJ3 = v.abschnitt(KZ("TJ3", "Bewerbungswerkstatt"), [
  ...v.kopf({ kicker: "Vorlage TJ3 · für Lernende", titel: "Bewerbungswerkstatt", unter: "Deine Bewerbung ist fiktiv. Verwende keine echte Adresse und kein Foto, wenn du mit KI-Tools arbeitest.", felder: ["Name", "Betrieb"] }),
  v.h("1 · Inserat analysieren"),
  v.p("Markiere im Inserat alle Anforderungen. Trage sie links ein und schreibe rechts, wie du sie erfüllst oder erreichen kannst."),
  ...v.tabelle([4819, 4819], ["Das wird verlangt", "Das bringe ich mit oder so erreiche ich es"], Array.from({ length: 5 }, () => ["", ""]), { hoehe: 560 }),
  v.h("2 · Mein Lebenslauf", F.gletscher),
  ...v.tabelle([3000, W - 3000], null, [["Personalien (fiktive Adresse erlaubt)", ""], ["Schulbildung", ""], ["Schnupperlehren, Praktika, Jobs", ""], ["Sprachen", ""], ["Informatik-Kenntnisse", ""], ["Hobbys und Engagement", ""], ["Referenzen", ""]], { label: true, hoehe: 560, farbe: F.gletscher }),
  v.umbruch(),
  v.h("3 · Mein Motivationsschreiben in fünf Teilen", F.lavendel),
  ...v.tabelle([2600, 3200, 3838], ["Teil", "Darum geht es", "Meine Stichworte"], [
    ["**Einstieg**", "Für welche Stelle bewerbe ich mich? Woher kenne ich sie?", ""],
    ["**Warum dieser Beruf**", "Was fasziniert mich? Welche Erfahrung zeigt das?", ""],
    ["**Warum dieser Betrieb**", "Was weiss ich über den Betrieb? Was gefällt mir?", ""],
    ["**Was ich mitbringe**", "Stärken mit Beispielen, passend zum Inserat", ""],
    ["**Schluss**", "Wunsch nach einem Gespräch, Gruss", ""]], { hoehe: 900, farbe: F.lavendel }),
  v.h("4 · Checkliste für das Bewerbungsdossier", F.bergsee),
  ...v.tabelle([6638, 1000, 1000, 1000], ["", "ich", "Partner/in", "Lehrperson"], [
    ["Der Lebenslauf ist vollständig und übersichtlich.", "[]", "[]", "[]"],
    ["Das Schreiben hat alle fünf Teile.", "[]", "[]", "[]"],
    ["Das Schreiben passt zum Inserat und zum Betrieb.", "[]", "[]", "[]"],
    ["Meine Stärken sind mit Beispielen belegt.", "[]", "[]", "[]"],
    ["Alles ist in meinen eigenen Worten geschrieben.", "[]", "[]", "[]"],
    ["Rechtschreibung und Form sind überprüft.", "[]", "[]", "[]"],
    ["Ich habe keine Personendaten in KI-Tools eingegeben.", "[]", "[]", "[]"]], { mitte: true, farbe: F.bergsee, streifen: true }),
  v.p("**Feedback meiner Lernpartnerin oder meines Lernpartners:** zwei Sterne und ein Wunsch"), ...v.linien(3),
]);

// ---------- TJ4 Vorstellungsgespräch ----------
v = S.mit("gletscher", "berge");
const karte = (titel, fragen, f) => new TableCell({ width: { size: W / 2, type: WidthType.DXA }, shading: { fill: f.hell, type: "clear", color: "auto" },
  borders: { top: { style: BorderStyle.DASHED, size: 8, color: f.dunkel }, bottom: { style: BorderStyle.DASHED, size: 8, color: f.dunkel }, left: { style: BorderStyle.DASHED, size: 8, color: f.dunkel }, right: { style: BorderStyle.DASHED, size: 8, color: f.dunkel } },
  margins: { top: 140, bottom: 140, left: 200, right: 200 },
  children: [new Paragraph({ children: [S.r(titel, { size: 22, bold: true, color: f.dunkel })], spacing: { after: 80 } }), ...punkte(fragen)] });
const TJ4 = v.abschnitt(KZ("TJ4", "Vorstellungsgespräch"), [
  ...v.kopf({ kicker: "Vorlage TJ4 · für Lernende", titel: "Vorstellungsgespräch üben", unter: "Zu dritt: Eine Person bewirbt sich, eine stellt Fragen, eine beobachtet. Nach jedem Gespräch tauscht ihr die Rollen. Die Karten könnt ihr ausschneiden." }),
  new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: [W / 2, W / 2], rows: [
    new TableRow({ height: { value: 2400, rule: "atLeast" }, children: [
      karte("Über dich", ["Erzählen Sie etwas über sich.", "Was sind Ihre Stärken? Nennen Sie ein Beispiel.", "Woran möchten Sie noch arbeiten?"], F.bergsee),
      karte("Zum Beruf", ["Warum möchten Sie diesen Beruf lernen?", "Wie haben Sie den Beruf kennengelernt?", "Was stellen Sie sich unter einem typischen Arbeitstag vor?"], F.terrakotta)] }),
    new TableRow({ height: { value: 2400, rule: "atLeast" }, children: [
      karte("Zum Betrieb", ["Warum möchten Sie bei uns arbeiten?", "Was wissen Sie über unseren Betrieb?", "Wo sehen Sie sich in fünf Jahren?"], F.lavendel),
      karte("Knifflige Fragen", ["Wie gehen Sie mit Kritik um?", "Erzählen Sie von einem Problem, das Sie gelöst haben.", "Haben Sie Fragen an uns?"], F.alpenrose)] }),
  ] }),
  v.leer(),
  v.h("Beobachtungsbogen"),
  ...v.tabelle([4638, 1000, 1000, 1000, 2000], ["", "noch nicht", "teilweise", "gut", "Beispiel / Tipp"], [
    ["Begrüssung, Blickkontakt, Haltung", "[]", "[]", "[]", ""], ["Antworten mit Beispielen", "[]", "[]", "[]", ""], ["Wissen über Beruf und Betrieb", "[]", "[]", "[]", ""],
    ["Deutliche Sprache, passendes Tempo", "[]", "[]", "[]", ""], ["Eigene Fragen an den Betrieb", "[]", "[]", "[]", ""], ["Verabschiedung", "[]", "[]", "[]", ""]], { mitte: true, streifen: true }),
  v.p("**Das war besonders gut:**"), ...v.linien(2),
  v.p("**Mein Tipp für das nächste Mal:**", { before: 80 }), ...v.linien(2),
]);

// ---------- TJ5 Poster- und Portfolio-Planer ----------
v = S.mit("alpenrose", "berge");
const TJ5 = v.abschnitt(KZ("TJ5", "Poster- und Portfolio-Planer"), [
  ...v.kopf({ kicker: "Vorlage TJ5 · für Lernende", titel: "Poster- und Portfolio-Planer", felder: ["Name", "[] Poster   [] Portfolio"] }),
  v.h("Meine Layout-Skizze"),
  v.p("Zeichne die Bereiche ein: Titel, Beruf, Betrieb, Arbeitsort, Bewerbung, Fazit. Wo kommen Bilder hin?", { size: 18 }),
  ...(() => { const kas = new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: [W], rows: [new TableRow({ height: { value: 3900, rule: "atLeast" }, children: [new TableCell({ width: { size: W, type: WidthType.DXA },
    borders: { top: { style: BorderStyle.DOTTED, size: 8, color: F.alpenrose.rand }, bottom: { style: BorderStyle.DOTTED, size: 8, color: F.alpenrose.rand }, left: { style: BorderStyle.DOTTED, size: 8, color: F.alpenrose.rand }, right: { style: BorderStyle.DOTTED, size: 8, color: F.alpenrose.rand } },
    children: [new Paragraph({ children: [] })] })] })] }); return [kas, v.leer()]; })(),
  v.h("Aufbau", F.lavendel),
  ...farbSpalten([
    ["Poster", punkte(["Titel mit Beruf und Betrieb", "höchstens sechs Bereiche", "Bilder und Grafiken, wenig Text", "Schrift aus 2 Metern lesbar", "Schlusssatz: Darum passt der Beruf zu mir"]), F.alpenrose],
    ["Portfolio", punkte(["Startseite mit Foto oder Bild und Kurztext", "Seiten: Beruf, Betrieb, Arbeitsort, Bewerbung, Reflexion, Quellen", "auf jeder Seite: Was bedeutet das für mich?", "nur für Lehrperson und Klasse freigegeben"]), F.lavendel]]),
  v.h("Checkliste vor der Abgabe", F.bergsee),
  ...v.tabelle([8638, 1000], null, [["Alle Teile aus dem Recherche-Heft sind enthalten.", "[]"], ["Die wichtigste Aussage ist auf den ersten Blick sichtbar.", "[]"], ["Bilder haben eine Quelle, KI-Bilder sind gekennzeichnet.", "[]"],
    ["Texte sind kurz und in eigenen Worten.", "[]"], ["Es sind keine privaten Daten sichtbar (Adresse, Telefonnummer).", "[]"], ["Quellen sind angegeben.", "[]"]], { mitte: true, farbe: F.bergsee, streifen: true }),
]);

// ---------- TJ6 Lernjournal ----------
v = S.mit("bergsee", "berge");
const TJ6 = v.abschnitt(KZ("TJ6", "Lernjournal"), [
  ...v.kopf({ kicker: "Vorlage TJ6 · für Lernende", titel: "Lernjournal", unter: "Halte fest, was du herausfindest und woher du es weisst. Das Journal ist Grundlage für die Checkpoints.", felder: ["Name"] }),
  v.h("Quellenprotokoll"),
  ...v.tabelle([1000, 2600, 900, 2800, 2338], ["Datum", "Quelle (URL, Titel)", "Screen-shot", "Was habe ich gelernt? (eigene Worte)", "Vertrauenswürdig? Wer, wann, mit welchem Ziel?"],
    Array.from({ length: 6 }, () => ["", "", "[]", "", ""]), { hoehe: 900 }),
  v.h("KI-Protokoll", F.gletscher),
  ...v.tabelle([900, 1100, 2200, 1800, 1900, 1738], ["Datum", "Tool", "Eingabe (Prompt)", "Antwort kurz", "Übernommen?", "So habe ich geprüft"],
    Array.from({ length: 4 }, () => ["", "", "", "", "[] ja [] teilw. [] nein", ""]), { hoehe: 900, farbe: F.gletscher }),
  v.h("Meine Lernschritte", F.terrakotta),
  ...v.tabelle([1100, 3000, 3000, 2538], ["Datum", "Das habe ich gemacht", "Das habe ich herausgefunden", "Mein nächster Schritt"],
    Array.from({ length: 6 }, () => ["", "", "", ""]), { hoehe: 640, farbe: F.terrakotta }),
]);

// ---------- TJ7 Checkpoints ----------
v = S.mit("gletscher", "weg");
const check = (titelM, f, liste) => [v.h(titelM, f),
  ...v.tabelle([4800, 600, 600, 600, 3038], ["Kriterium", "✓", "~", "✗", "Notiz"], liste.map(t => [t, "[]", "[]", "[]", ""]), { mitte: true, farbe: f }),
  v.p("**Vereinbarung bis zum nächsten Mal:**"), ...v.linien(1, f)];
const TJ7 = v.abschnitt(KZ("TJ7", "Checkpoints"), [
  ...v.kopf({ kicker: "Vorlage TJ7 · für die Lehrperson", titel: "Checkpoints", felder: ["Name", "Variante"] }),
  ...check("C1 · Wahl   Datum: ________", F.bergsee, ["Interessen-Check gemacht und im Journal", "mindestens drei Berufe erkundet", "Beruf und Betrieb gewählt und begründet", "Wahl passt zu den Interessen oder ist bewusst offen"]),
  ...check("C2 · Recherche   Datum: ________", F.terrakotta, ["Steckbriefe Beruf, Betrieb und Arbeitsort vollständig", "offizielle Quellen, im Journal belegt", "Lebenslauf und Schreiben als Entwurf", "keine Personendaten in KI-Tools"]),
  ...check("C3 · Produkt   Datum: ________", F.lavendel, ["Skizze oder Entwurf übersichtlich", "zentrale Aussage klar", "Probe der Präsentation, Zeit eingehalten"]),
  ...v.kasten("Coaching-Fragen (GROW)", v.bullets(["**Ziel:** Was willst du heute fertig haben?", "**Stand:** Zeig mir dein Lernjournal. Was hast du schon herausgefunden?", "**Möglichkeiten:** Wen könntest du fragen, wenn du nicht weiterkommst?", "**Nächster Schritt:** Was machst du bis zur nächsten Lektion?"])),
]);

// ---------- Raster ----------
v = S.mit("alpenrose", "berge");
const raster = (teile) => teile.flatMap(([teil, f, krit]) => [v.h(teil, f), ...v.tabelle([5038, 650, 650, 650, 650, 2000], ["Kriterium", "0", "1", "2", "3", "Feedback"],
  [...krit.map(t => [t, "[]", "[]", "[]", "[]", ""]), [{ text: `**Total ${teil}**`, fill: true }, { text: `**____ / ${krit.length * 3}**`, span: 4, align: AlignmentType.CENTER, fill: true }, ""]], { mitte: true, farbe: f, streifen: true })]);
const TJ8_TEILE = [
  ["Inhalt", F.terrakotta, ["Beruf: Tätigkeiten, Ausbildung, Anforderungen", "Betrieb: Angebot, Grösse, Werte, Ausbildungsplätze", "Arbeitsort und Rahmenbedingungen", "Begründung: Darum passt der Beruf zu mir", "Bewerbung (Lebenslauf, Schreiben) eingebunden bzw. erwähnt", "Plan ist realistisch, nächste Schritte sind genannt"]],
  ["Gestaltung", F.lavendel, ["übersichtlich, klare Struktur", "Bilder und Grafiken passend, mit Quelle oder Kennzeichnung", "Texte kurz, in eigenen Worten, sprachlich korrekt"]],
  ["Arbeitsweise", F.bergsee, ["Quellen und Lernjournal nachvollziehbar", "Checkpoints genutzt, Abgabe termingerecht"]],
];
const TJ8 = v.abschnitt(KZ("TJ8", "Bewertungsraster Poster oder Portfolio"), [
  ...v.kopf({ kicker: "Vorlage TJ8 · Bewertung · 1 Note", titel: "Bewertungsraster Poster oder Portfolio", felder: ["Name", "[] Poster   [] Portfolio"] }),
  v.klein("**Skala:** 0 = fehlt · 1 = ansatzweise · 2 = grösstenteils erfüllt · 3 = vollständig und überzeugend"),
  ...raster(TJ8_TEILE),
  v.kasten("Gesamt und Note", "**____ / 33**    Note: Punkte ÷ 33 × 5 + 1 = ________   (gerundet nach den Vorgaben der Schule)")[0],
]);
const TJ9_TEILE = [
  ["Inhalt", F.terrakotta, ["Beruf, Betrieb und Arbeitsort verständlich vorgestellt", "Begründung der Wahl überzeugend", "realistische Einschätzung und nächste Schritte"]],
  ["Auftritt", F.lavendel, ["frei gesprochen, Blickkontakt", "deutliche Sprache, passendes Tempo", "Poster oder Portfolio als Unterstützung genutzt", "auf Fragen eingegangen"]],
  ["Gespräch (Sek II) bzw. Messestand (Sek I)", F.gletscher, ["Antworten mit Beispielen", "Wissen über Beruf und Betrieb", "eigene Fragen bzw. Besuchende aktiv einbezogen"]],
];
const TJ9 = v.abschnitt(KZ("TJ9", "Bewertungsraster Präsentation"), [
  ...v.kopf({ kicker: "Vorlage TJ9 · Bewertung · 1 Note", titel: "Bewertungsraster Präsentation", felder: ["Name", "[] Berufsmesse   [] Präsentation mit Gespräch"] }),
  v.klein("**Skala:** 0 = fehlt · 1 = ansatzweise · 2 = grösstenteils erfüllt · 3 = vollständig und überzeugend. In der Variante Ausland zählt die Fremdsprache bei «Auftritt» und «Gespräch»."),
  ...raster(TJ9_TEILE),
  v.kasten("Gesamt und Note", "**____ / 30**    Note: Punkte ÷ 30 × 5 + 1 = ________   (gerundet nach den Vorgaben der Schule)")[0],
]);

// ---------- TJ10 Berufsmesse und Selbsteinschätzung ----------
v = S.mit("lavendel", "weg");
const fbKarte = f => new TableCell({ width: { size: W / 2, type: WidthType.DXA }, shading: { fill: f.hell, type: "clear", color: "auto" },
  borders: { top: { style: BorderStyle.DASHED, size: 8, color: f.dunkel }, bottom: { style: BorderStyle.DASHED, size: 8, color: f.dunkel }, left: { style: BorderStyle.DASHED, size: 8, color: f.dunkel }, right: { style: BorderStyle.DASHED, size: 8, color: f.dunkel } },
  margins: { top: 120, bottom: 120, left: 180, right: 180 },
  children: [new Paragraph({ children: [S.r("Feedback für den Stand von ______________", { size: 18, bold: true, color: f.dunkel })], spacing: { after: 100 } }),
    new Paragraph({ children: S.runs("★ Das hat mir gefallen:", { size: 18 }), spacing: { after: 360 } }),
    new Paragraph({ children: S.runs("★ Das habe ich Neues erfahren:", { size: 18 }), spacing: { after: 360 } }),
    new Paragraph({ children: S.runs("? Meine Frage oder mein Wunsch:", { size: 18 }), spacing: { after: 360 } }),
    new Paragraph({ children: S.runs("Von: ______________", { size: 16 }), spacing: { after: 0 } })] });
const TJ10 = v.abschnitt(KZ("TJ10", "Berufsmesse und Selbsteinschätzung"), [
  ...v.kopf({ kicker: "Vorlage TJ10 · für Lernende", titel: "Berufsmesse: Feedbackkarten", unter: "Besuche drei bis vier Stände. Fülle für jeden Stand eine Karte aus und gib sie ab. Die Karten zählen nicht zur Note." }),
  new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: [W / 2, W / 2], rows: [
    new TableRow({ children: [fbKarte(F.bergsee), fbKarte(F.terrakotta)] }),
    new TableRow({ children: [fbKarte(F.gletscher), fbKarte(F.alpenrose)] }),
  ] }),
  v.umbruch(),
  ...v.kopf({ kicker: "Vorlage TJ10 · Selbsteinschätzung", titel: "Mein Traumjob: Rückblick", felder: ["Name"] }),
  v.h("So schätze ich mein Produkt ein", F.bergsee),
  v.p("Fülle das Raster TJ8 für dich aus und trage hier die Summen ein."),
  ...v.tabelle([3800, 1800, 1800, 2238], ["Bereich", "Meine Punkte", "Maximum", "Darauf bin ich stolz"], [["Inhalt", "", "18", ""], ["Gestaltung", "", "9", ""], ["Arbeitsweise", "", "6", ""], [{ text: "**Total und erwartete Note**", fill: true }, "", "33", ""]], { hoehe: 520, label: true, farbe: F.bergsee }),
  v.h("Das nehme ich mit", F.terrakotta),
  v.p("**Feedbackkarten:** Was haben die Besuchenden an meinem Stand am häufigsten genannt?"), ...v.linien(2, F.terrakotta),
  v.p("**Mein Plan:** Wie realistisch ist er? Was fehlt mir noch?", { before: 120 }), ...v.linien(3, F.terrakotta),
  v.p("**KI:** Wo hat mir KI geholfen, wo lag sie falsch, wo habe ich bewusst ohne gearbeitet?", { before: 120 }), ...v.linien(2, F.terrakotta),
  v.p("**Mein nächster Schritt in der Berufswahl** (zum Beispiel eine Schnupperlehre anfragen):", { before: 120 }), ...v.linien(2, F.terrakotta),
]);

const DOKS = [["TJ1_Auftragsblatt", TJ1], ["TJ2_Recherche-Heft", TJ2], ["TJ3_Bewerbungswerkstatt", TJ3], ["TJ4_Vorstellungsgespraech", TJ4], ["TJ5_Poster-und-Portfolio-Planer", TJ5],
  ["TJ6_Lernjournal", TJ6], ["TJ7_Checkpoints", TJ7], ["TJ8_Bewertungsraster_Produkt", TJ8], ["TJ9_Bewertungsraster_Praesentation", TJ9], ["TJ10_Berufsmesse_und_Selbsteinschaetzung", TJ10]];
(async () => {
  for (const [name, sec] of DOKS) {
    const doc = new Document({ creator: "Anja Muggli", title: name.replace(/_/g, " "), styles: S.STIL, numbering: S.NUM, sections: [sec] });
    fs.writeFileSync(path.join(OUT, name + ".docx"), await Packer.toBuffer(doc));
  }
  const alle = new Document({ creator: "Anja Muggli", title: "Mein Traumjob: alle Vorlagen", styles: S.STIL, numbering: S.NUM, sections: DOKS.map(d => d[1]) });
  fs.writeFileSync(path.join(OUT, "Traumjob_alle_Vorlagen.docx"), await Packer.toBuffer(alle));
  console.log("Word-Dateien erstellt:", DOKS.length + 1);
})();
