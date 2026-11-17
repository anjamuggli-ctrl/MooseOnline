#!/bin/sh
# Wandelt alle Word-Vorlagen eines Download-Ordners in PDF um.  Aufruf: sh _build/vorlagen_pdf.sh downloads/smart-city
cd "$1" || exit 1
rm -f ./*.pdf
for f in ./*.docx; do zip -d "$f" '*/' >/dev/null 2>&1; done
soffice --headless --convert-to pdf ./*.docx >/dev/null 2>&1
ls ./*.pdf | wc -l
