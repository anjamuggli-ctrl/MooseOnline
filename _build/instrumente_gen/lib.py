"""Erzeugt Instrumente (Word) im Stil der bestehenden MuggliOnline-Instrumente."""
from docx import Document
from docx.shared import Pt, RGBColor, Cm, Twips
from docx.enum.text import WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

GREEN = "3F5D4A"; GREY = "6B7368"; SAND = "F4F1EA"; LINE = "C9C3B6"; MINT = "E7EDE6"
FONT = "Arial"


def _font(run, size=9.5, bold=False, color=None, italic=False, font=FONT):
    run.font.name = font
    rpr = run._element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts"); rpr.insert(0, rf)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rf.set(qn(a), font)
    run.font.size = Pt(size); run.font.bold = bold; run.font.italic = italic
    if color: run.font.color.rgb = RGBColor.from_string(color)


def _spacing(p, before=0, after=80, line=None):
    pf = p.paragraph_format
    pf.space_before = Twips(before); pf.space_after = Twips(after)
    if line: pf.line_spacing = line


def rich(p, text, size=9.5, color=None, italic=False):
    """**fett** und ☐ (in MS Gothic) innerhalb eines Absatzes."""
    parts = text.split("**")
    for k, part in enumerate(parts):
        bold = k % 2 == 1
        segs = part.split("☐")
        for j, seg in enumerate(segs):
            if seg:
                _font(p.add_run(seg), size, bold, color, italic)
            if j < len(segs) - 1:
                _font(p.add_run("☐"), size, bold, color, italic, font="MS Gothic")


class Inst:
    def __init__(self, doc, topic, nr):
        self.d = doc; self.topic = topic; self.nr = nr

    def kicker(self, t):
        p = self.d.add_paragraph(); _spacing(p, 0, 40)
        r = p.add_run(t.upper()); _font(r, 8, True, GREY)
        r._element.get_or_add_rPr().append(_el("w:spacing", {"w:val": "40"}))

    def title(self, t):
        p = self.d.add_paragraph(); _spacing(p, 0, 100)
        p.paragraph_format.keep_with_next = True
        _font(p.add_run(t), 20, True, GREEN)

    def sub(self, t):
        p = self.d.add_paragraph(); _spacing(p, 0, 140); rich(p, t, 9, GREY)

    def p(self, t, after=100):
        p = self.d.add_paragraph(); _spacing(p, 0, after, 1.1); rich(p, t)

    def h2(self, t):
        p = self.d.add_paragraph(); _spacing(p, 220, 80)
        p.paragraph_format.keep_with_next = True
        _font(p.add_run(t), 12, True, GREEN)

    def bullets(self, items):
        for it in items:
            p = self.d.add_paragraph(); _spacing(p, 0, 50, 1.1)
            p.paragraph_format.left_indent = Cm(0.6); p.paragraph_format.first_line_indent = Cm(-0.4)
            rich(p, "•  " + it)

    def tip(self, t):
        p = self.d.add_paragraph(); _spacing(p, 60, 100); rich(p, t, 8, GREY, italic=True)

    def box(self, head, text):
        t = self.d.add_table(rows=1, cols=1); _tblw(t, [9638])
        c = t.rows[0].cells[0]; _cell(c, MINT, left=GREEN)
        p = c.paragraphs[0]; _spacing(p, 0, 40)
        r = p.add_run(head.upper()); _font(r, 7.5, True, GREEN)
        p2 = c.add_paragraph(); _spacing(p2, 0, 20, 1.1); rich(p2, text, 9)
        self.d.add_paragraph()

    def fields(self, labels, w=2600):
        """Zweispaltige Angabe-Tabelle: Label links (Sand), leer rechts."""
        t = self.d.add_table(rows=0, cols=2); _tblw(t, [w, 9638 - w])
        for lab in labels:
            row = t.add_row(); _cantsplit(row)
            a, b = row.cells
            if "☐" in lab:
                m = a.merge(b); _cell(m, SAND); rich(m.paragraphs[0], lab, 8.5)
                continue
            _cell(a, SAND); _cell(b, None)
            rich(a.paragraphs[0], lab, 8.5)
        self.d.add_paragraph().paragraph_format.space_after = Twips(0)
        return t

    def grid(self, head, rows=0, widths=None, first_col=None, height=600, body=None, sand_first=None):
        """Tabelle mit grüner Kopfzeile. first_col: Texte der ersten Spalte (Sand);
        body: ganze Zeilen mit Texten; sonst leere Zeilen."""
        n = len(head)
        widths = widths or [9638 // n] * n
        if sand_first is None: sand_first = bool(first_col or body)
        t = self.d.add_table(rows=1, cols=n); _tblw(t, widths)
        for c, txt in zip(t.rows[0].cells, head):
            _cell(c, GREEN); rich(c.paragraphs[0], "**" + txt + "**" if txt else "", 8.5, "FFFFFF")
        _repeat_header(t.rows[0])
        lines = body if body else ([[x] + [""] * (n - 1) for x in first_col] if first_col else [[""] * n for _ in range(rows)])
        for line in lines:
            row = t.add_row(); _cantsplit(row); _height(row, height)
            for k, (c, txt) in enumerate(zip(row.cells, line)):
                _cell(c, SAND if (k == 0 and sand_first) else None)
                rich(c.paragraphs[0], txt, 8.5)
        self.d.add_paragraph().paragraph_format.space_after = Twips(0)
        return t

    def checklist(self, items, cols=("Frage", "erfüllt")):
        t = self.d.add_table(rows=1, cols=2); _tblw(t, [8600, 1038])
        for c, txt in zip(t.rows[0].cells, cols):
            _cell(c, GREEN); rich(c.paragraphs[0], "**" + txt + "**", 8.5, "FFFFFF")
        _repeat_header(t.rows[0])
        for it in items:
            row = t.add_row(); _cantsplit(row)
            a, b = row.cells; _cell(a, None); _cell(b, None)
            rich(a.paragraphs[0], it, 8.5)
            pb = b.paragraphs[0]; pb.alignment = 1; rich(pb, "☐", 11)
        self.d.add_paragraph().paragraph_format.space_after = Twips(0)

    def lines(self, n=3):
        for _ in range(n):
            p = self.d.add_paragraph(); _spacing(p, 0, 0)
            p.paragraph_format.line_spacing = 1.8
            pPr = p._p.get_or_add_pPr()
            bdr = OxmlElement("w:pBdr"); b = OxmlElement("w:bottom")
            for k, v in (("w:val", "single"), ("w:sz", "4"), ("w:space", "1"), ("w:color", LINE)): b.set(qn(k), v)
            bdr.append(b); pPr.append(bdr)
        self.d.add_paragraph()

    def source(self, t):
        self.tip(t)

    def pagebreak(self):
        self.d.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def body_plain(line):
    return False


def _el(tag, attrs):
    e = OxmlElement(tag)
    for k, v in attrs.items(): e.set(qn(k), v)
    return e


def _tblw(t, widths):
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    tblPr = t._tbl.tblPr
    tblPr.append(_el("w:tblW", {"w:type": "dxa", "w:w": str(sum(widths))}))
    tblPr.append(_el("w:tblLayout", {"w:type": "fixed"}))
    for row in t.rows:
        for c, w in zip(row.cells, widths): c.width = Twips(w)
    t._widths = widths
    grid = t._tbl.tblGrid
    for gc, w in zip(grid.findall(qn("w:gridCol")), widths): gc.set(qn("w:w"), str(w))


def _cell(c, fill, left=None):
    tcPr = c._tc.get_or_add_tcPr()
    b = OxmlElement("w:tcBorders")
    for side in ("top", "left", "bottom", "right"):
        col, sz = (left, "18") if (side == "left" and left) else ((LINE, "4") if not left else ("auto", "0"))
        val = "single" if (not left or side == "left") else "nil"
        b.append(_el("w:" + side, {"w:val": val, "w:color": col, "w:sz": sz}))
    tcPr.append(b)
    if fill: tcPr.append(_el("w:shd", {"w:val": "clear", "w:color": "auto", "w:fill": fill}))
    m = OxmlElement("w:tcMar")
    for side, v in (("top", "70"), ("left", "110"), ("bottom", "70"), ("right", "110")):
        m.append(_el("w:" + side, {"w:type": "dxa", "w:w": v}))
    tcPr.append(m)
    t = c._tc.getparent().getparent()
    widths = getattr(c._parent, "_widths", None) if hasattr(c, "_parent") else None
    for p in c.paragraphs: _spacing(p, 0, 40, 1.1)


def _cantsplit(row):
    row._tr.get_or_add_trPr().append(_el("w:cantSplit", {}))


def _repeat_header(row):
    row._tr.get_or_add_trPr().append(_el("w:tblHeader", {}))


def _height(row, h):
    row._tr.get_or_add_trPr().append(_el("w:trHeight", {"w:val": str(h), "w:hRule": "atLeast"}))


def new_doc(header_text):
    d = Document()
    s = d.sections[0]
    s.page_width = Twips(11906); s.page_height = Twips(16838)
    for a in ("top_margin", "bottom_margin", "left_margin", "right_margin"): setattr(s, a, Twips(1134))
    s.header_distance = Twips(560); s.footer_distance = Twips(560)
    st = d.styles["Normal"]; st.font.name = FONT; st.font.size = Pt(9.5)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    hp = s.header.paragraphs[0]
    _font(hp.add_run(header_text), 7, False, GREY)
    pPr = hp._p.get_or_add_pPr(); bdr = OxmlElement("w:pBdr")
    bdr.append(_el("w:bottom", {"w:val": "single", "w:color": LINE, "w:sz": "4", "w:space": "4"})); pPr.append(bdr)
    fp = s.footer.paragraphs[0]
    from docx.enum.text import WD_TAB_ALIGNMENT
    fts = d.styles["Footer"].paragraph_format.tab_stops


    pPr_tabs = fp._p.get_or_add_pPr()
    tabs = OxmlElement("w:tabs")
    for pos in (4513, 9026, 4680, 9360):
        tabs.append(_el("w:tab", {"w:val": "clear", "w:pos": str(pos)}))
    tabs.append(_el("w:tab", {"w:val": "right", "w:pos": "9638"}))
    old = pPr_tabs.find(qn("w:tabs"))
    if old is not None: pPr_tabs.remove(old)
    pPr_tabs.insert(0, tabs)
    _font(fp.add_run("Instrumente · frei nutzbar mit Quellenangabe"), 7, False, GREY)
    r = fp.add_run("\t"); _font(r, 8, False, GREY)
    for tag, attrs in (("w:fldChar", {"w:fldCharType": "begin"}), ("w:instrText", {}), ("w:fldChar", {"w:fldCharType": "end"})):
        e = _el(tag, attrs)
        if tag == "w:instrText": e.set(qn("xml:space"), "preserve"); e.text = "PAGE"
        r._r.append(e)
    # leeren Startabsatz entfernen
    body = d.element.body
    first = body.find(qn("w:p"))
    if first is not None and not first.xpath(".//w:t"): body.remove(first)
    return d
