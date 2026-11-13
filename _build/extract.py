from html.parser import HTMLParser
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent.parent
ATTRS={'alt','title','aria-label','placeholder'}
class P(HTMLParser):
    def __init__(s): super().__init__(convert_charrefs=True); s.skip=0; s.out=[]
    def handle_starttag(s,tag,attrs):
        if tag in('script','style'): s.skip+=1
        a=dict(attrs)
        for k in ATTRS:
            if a.get(k,'').strip(): s.out.append(a[k].strip())
        if tag=='meta' and a.get('name')=='description' and a.get('content'): s.out.append(a['content'].strip())
    def handle_endtag(s,tag):
        if tag in('script','style'): s.skip-=1
    def handle_data(s,d):
        if s.skip==0 and d.strip(): s.out.append(d.strip())
seen=[]
for f in sorted(ROOT.glob('*.html')):
    p=P(); p.feed(f.read_text())
    for x in p.out:
        if x not in seen: seen.append(x)
json.dump(seen,open(ROOT/'_build/strings_de.json','w'),ensure_ascii=False,indent=0)
print(len(seen), sum(len(x) for x in seen))
