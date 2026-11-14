"""Ergänzt Übersetzungen einer Sprache in i18n.json: python3 add_tr.py <lang> <datei.json>"""
import json, sys
lang, quelle = sys.argv[1], sys.argv[2]
d = json.load(open("i18n.json"))
neu = json.load(open(quelle))
for de, tr in neu.items():
    d["texte"].setdefault(de, {})[lang] = tr
json.dump(d, open("i18n.json", "w"), ensure_ascii=False, indent=1)
print(len(neu), "Einträge für", lang)
