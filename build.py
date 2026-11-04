from pathlib import Path
import json,re
root=Path(__file__).parent
for kind in ('posts','materiale'):
    entries=[]
    for file in (root/'content'/kind).glob('*.md'):
        txt=file.read_text(encoding='utf-8')
        match=re.match(r'\A---\s*\n(.*?)\n---',txt,re.S)
        if not match: continue
        meta={}
        for line in match.group(1).splitlines():
            if ':' in line:
                k,v=line.split(':',1)
                meta[k.strip()]=v.strip().strip('"\'')
        entries.append({'title':meta.get('title',file.stem),'description':meta.get('description',''),'date':meta.get('date',''),'slug':file.stem,'file':meta.get('file','')})
    (root/'content'/kind/'index.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2),encoding='utf-8')
