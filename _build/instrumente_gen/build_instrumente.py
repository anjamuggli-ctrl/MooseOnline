"""Erzeugt Word- und PDF-Dateien der Instrumente. Aufruf: python3 build_instrumente.py"""
import subprocess, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import new_doc, Inst
from inhalte import THEMEN

ROOT = pathlib.Path(__file__).resolve().parents[2]

for thema, ordner, alle_datei, liste in THEMEN:
    out = ROOT / "downloads" / ordner
    out.mkdir(parents=True, exist_ok=True)
    gesamt = new_doc(f"Instrumente · {thema} · Anja Muggli · mugglionline.ch")
    for k, (datei, titel, kurz, fn) in enumerate(liste, 1):
        d = new_doc(f"Instrument {k} · {thema} · Anja Muggli · mugglionline.ch")
        fn(Inst(d, thema, k)); d.save(out / f"{datei}.docx")
        I = Inst(gesamt, thema, k)
        if k > 1: I.pagebreak()
        fn(I)
    gesamt.save(out / f"{alle_datei}.docx")
    files = sorted(str(p) for p in out.glob("*.docx"))
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(out)] + files,
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(ordner, len(files), "Dateien")
