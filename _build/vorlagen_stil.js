// Gemeinsamer Stil für alle Word-Vorlagen der Aufträge (Pastellfarben und Berge wie in der Bullet-Journal-Werkstatt).
// Verwendung:  const S = require("./vorlagen_stil");  const v = S.mit("bergsee", "stadt");  v.kopf(...), v.h(...), v.tabelle(...)
const fs = require("fs");
const path = require("path");
const {
  Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle, AlignmentType,
  Header, Footer, PageNumber, PageOrientation, LevelFormat, PageBreak, VerticalAlign, HeightRule, ImageRun,
} = require("docx");

const FONT = "Arial";
const TEXT = "333B36", GRAU = "6B7368";
const W_HOCH = 9638, W_QUER = 14570; // nutzbare Breite A4 bei 2 cm Rand
const BILDER = path.join(__dirname, "vorlagen-bilder");

const FARBEN = { // hell, mittel, dunkel, Rahmen
  bergsee:    { hell: "E3EDE8", mittel: "C9DDD3", dunkel: "3F6B5A", rand: "A9C7BA" },
  alpenrose:  { hell: "F5E1E5", mittel: "EBC7CF", dunkel: "9B4D5E", rand: "DDB0BB" },
  gletscher:  { hell: "E2E8F2", mittel: "CBD6E6", dunkel: "4A6178", rand: "B2C1D6" },
  terrakotta: { hell: "F4E4D7", mittel: "EBCFB8", dunkel: "A8682F", rand: "E0BE9F" },
  lavendel:   { hell: "E9E5F3", mittel: "D6CEEA", dunkel: "6B5592", rand: "C4B8DD" },
};

const r = (t, o = {}) => new TextRun({ text: t, font: FONT, size: o.size || 20, bold: o.bold, italics: o.italics, color: o.color || TEXT, characterSpacing: o.spacing });
const box = (size = 20) => new TextRun({ text: "☐", font: "MS Gothic", size });
function runs(x, o = {}) {
  // **fett** und [] (Ankreuzkästchen in MS Gothic)
  if (Array.isArray(x)) return x;
  const out = [];
  String(x).split(/(\*\*[^*]+\*\*|\[\])/).forEach(t => {
    if (!t) return;
    if (t === "[]") out.push(box(o.size || 20));
    else if (t.startsWith("**")) out.push(r(t.slice(2, -2), { ...o, bold: true }));
    else out.push(r(t, o));
  });
  return out;
}
const bild = (datei, breiteCm, hoeheCm) => new ImageRun({
  type: datei.endsWith(".png") ? "png" : "jpg", data: fs.readFileSync(datei),
  transformation: { width: Math.round(breiteCm * 37.8), height: Math.round(hoeheCm * 37.8) },
});
const OHNE = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const OHNE_RAND = { top: OHNE, bottom: OHNE, left: OHNE, right: OHNE };

function mit(farbname, motiv = "berge") {
  const F = FARBEN[farbname];
  const RAND = { style: BorderStyle.SINGLE, size: 6, color: F.rand };
  const RAENDER = { top: RAND, bottom: RAND, left: RAND, right: RAND };

  const p = (t, o = {}) => new Paragraph({ children: runs(t, o), spacing: { before: o.before || 0, after: o.after ?? 100, line: 276 }, alignment: o.align });
  const klein = t => p(t, { size: 17, color: GRAU });
  // Zwischentitel als farbiges Etikett wie in den Wochenplanern
  const h = (t, farbe = F) => new Paragraph({
    children: [r("  " + t + "  ", { size: 23, bold: true, color: farbe.dunkel })], keepNext: true,
    spacing: { before: 260, after: 120 }, shading: { type: ShadingType.CLEAR, fill: farbe.hell, color: "auto" },
    border: { left: { style: BorderStyle.SINGLE, size: 24, color: farbe.dunkel, space: 4 } },
  });
  const bullets = list => list.map(t => new Paragraph({ children: runs(t), numbering: { reference: "punkte", level: 0 }, spacing: { after: 60, line: 264 } }));
  const linien = (n, farbe = F) => Array.from({ length: n }, () => new Paragraph({ children: [r("")], spacing: { before: 0, after: 0, line: 420 },
    border: { bottom: { style: BorderStyle.DOTTED, size: 6, color: farbe.rand, space: 1 } } }));
  const umbruch = () => new Paragraph({ children: [new PageBreak()] });
  const leer = (after = 120) => new Paragraph({ children: [], spacing: { after } });

  function zelle(inhalt, breite, o = {}) {
    const kinder = (Array.isArray(inhalt) && inhalt.length && (inhalt[0] instanceof Paragraph || inhalt[0] instanceof Table)) ? inhalt
      : [new Paragraph({ children: runs(inhalt ?? "", { size: o.size || 18, bold: o.bold, color: o.color }), alignment: o.align, spacing: { after: 0, line: 252 } })];
    return new TableCell({
      children: kinder, width: { size: breite, type: WidthType.DXA }, borders: o.ohneRand ? OHNE_RAND : (o.rand ? (() => { const x = { style: BorderStyle.SINGLE, size: 6, color: o.rand }; return { top: x, bottom: x, left: x, right: x }; })() : RAENDER),
      shading: o.fill ? { fill: o.fill, type: ShadingType.CLEAR, color: "auto" } : undefined,
      margins: { top: o.pad ?? 90, bottom: o.pad ?? 90, left: 120, right: 120 }, verticalAlign: o.valign || VerticalAlign.TOP,
      columnSpan: o.span,
    });
  }
  // tabelle(breiten, kopf, zeilen, {label, hoehe, mitte, farbe})
  function tabelle(breiten, kopf, zeilen, o = {}) {
    const f = o.farbe || F;
    const gesamt = breiten.reduce((a, b) => a + b, 0);
    const rows = [];
    if (kopf) rows.push(new TableRow({ tableHeader: true, children: kopf.map((k, i) => zelle(k, breiten[i], { rand: f.rand, fill: f.mittel, color: f.dunkel, bold: true, align: o.mitte && i > 0 ? AlignmentType.CENTER : undefined })) }));
    zeilen.forEach((z, zi) => rows.push(new TableRow({
      height: o.hoehe ? { value: o.hoehe, rule: HeightRule.ATLEAST } : undefined, cantSplit: true,
      children: z.map((c, i) => {
        if (c && typeof c === "object" && !Array.isArray(c) && c.text !== undefined)
          return zelle(c.text, c.span ? breiten.slice(i, i + c.span).reduce((a, b) => a + b, 0) : breiten[i], { rand: f.rand, ...c, fill: c.fill === true ? f.hell : c.fill });
        return zelle(c, breiten[i], { rand: f.rand, fill: o.label && i === 0 ? f.hell : (o.streifen && zi % 2 ? "FBFAF7" : undefined), bold: o.label && i === 0, color: o.label && i === 0 ? f.dunkel : undefined, align: o.mitte && i > 0 ? AlignmentType.CENTER : undefined });
      }),
    })));
    return [new Table({ width: { size: gesamt, type: WidthType.DXA }, columnWidths: breiten, rows }), leer()];
  }
  const felder = (breite, liste, hoehe = 560) => tabelle([Math.round(breite * 0.3), breite - Math.round(breite * 0.3)], null, liste.map(x => [x, ""]), { label: true, hoehe });

  // Kopfbereich: farbige Karte mit Titel links und Bergen rechts
  function kopf({ kicker, titel, unter, breite = W_HOCH, felder: kopfFelder }) {
    const bildB = 3400, textB = breite - bildB;
    const text = [
      new Paragraph({ children: [r(kicker.toUpperCase(), { size: 15, bold: true, color: F.dunkel, spacing: 40 })], spacing: { after: 60 } }),
      new Paragraph({ children: [r(titel, { size: 34, bold: true, color: F.dunkel })], spacing: { after: 80, line: 300 } }),
      ...(unter ? [new Paragraph({ children: runs(unter, { size: 17, color: TEXT }), spacing: { after: 40 } })] : []),
    ];
    const bildP = new Paragraph({ children: [bild(path.join(BILDER, `banner-${farbname}-${motiv}.png`), 6.0, 2.26)], alignment: AlignmentType.RIGHT, spacing: { after: 0 } });
    const t = new Table({ width: { size: breite, type: WidthType.DXA }, columnWidths: [textB, bildB], rows: [new TableRow({ children: [
      zelle(text, textB, { fill: F.hell, ohneRand: true, valign: VerticalAlign.CENTER, pad: 160 }),
      zelle([bildP], bildB, { fill: F.hell, ohneRand: true, valign: VerticalAlign.BOTTOM, pad: 0 }),
    ] })] });
    const out = [t];
    if (kopfFelder) {
      const n = kopfFelder.length, b = Math.floor(breite / n);
      out.push(leer(80), new Table({ width: { size: b * n, type: WidthType.DXA }, columnWidths: Array(n).fill(b), rows: [new TableRow({ children:
        kopfFelder.map(k => new TableCell({ width: { size: b, type: WidthType.DXA }, borders: { top: OHNE, left: OHNE, right: OHNE, bottom: { style: BorderStyle.SINGLE, size: 6, color: F.rand } },
          margins: { top: 60, bottom: 40, left: 60, right: 200 }, children: [new Paragraph({ children: [r(k, { size: 16, bold: true, color: F.dunkel })], spacing: { after: 160 } })] })) })] }));
    }
    out.push(leer(160));
    return out;
  }

  // farbiger Hinweiskasten
  function kasten(titel, inhalt, farbe = F) {
    const kinder = [new Paragraph({ children: [r(titel, { size: 19, bold: true, color: farbe.dunkel })], spacing: { after: 60 } }),
      ...(Array.isArray(inhalt) ? inhalt : [new Paragraph({ children: runs(inhalt, { size: 19 }), spacing: { after: 0, line: 264 } })])];
    return [new Table({ width: { size: W_HOCH, type: WidthType.DXA }, columnWidths: [W_HOCH], rows: [new TableRow({ children: [new TableCell({
      children: kinder, width: { size: W_HOCH, type: WidthType.DXA }, shading: { fill: farbe.hell, type: ShadingType.CLEAR, color: "auto" },
      borders: { top: OHNE, bottom: OHNE, right: OHNE, left: { style: BorderStyle.SINGLE, size: 24, color: farbe.dunkel } },
      margins: { top: 120, bottom: 120, left: 200, right: 200 } })] })] }), leer()];
  }

  function abschnitt(kopfzeile, kinder, quer = false) {
    return {
      properties: { page: { size: { width: 11906, height: 16838, orientation: quer ? PageOrientation.LANDSCAPE : PageOrientation.PORTRAIT },
        margin: { top: 1000, bottom: 1000, left: 1134, right: 1134, header: 500, footer: 500 } } },
      headers: { default: new Header({ children: [new Paragraph({ children: [r(kopfzeile, { size: 15, color: F.dunkel })],
        border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: F.rand, space: 4 } } })] }) },
      footers: { default: new Footer({ children: [new Paragraph({ children: [r("mugglionline.ch · Vorlage frei nutzbar und anpassbar mit Quellenangabe", { size: 15, color: GRAU }), r("\t", { size: 15 }), new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 15, color: F.dunkel, bold: true })],
        tabStops: [{ type: "right", position: quer ? W_QUER : W_HOCH }] })] }) },
      children: kinder,
    };
  }
  return { F, p, klein, h, bullets, linien, umbruch, leer, zelle, tabelle, felder, kopf, kasten, abschnitt, runs, r, box, bild };
}

const STIL = { default: { document: { run: { font: FONT, size: 20, color: TEXT } } } };
const NUM = { config: [{ reference: "punkte", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 240 } } } }] }] };

module.exports = { mit, FARBEN, STIL, NUM, W_HOCH, W_QUER, bild, runs, r, box, OHNE_RAND };
