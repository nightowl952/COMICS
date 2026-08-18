#!/usr/bin/env python3
"""Resilient marvel.com ID harvester.
Detects 403 throttling, backs off, and resumes the same batch instead of
burning through the range while blocked. Appends to a JSON store so reruns
never redo banked work."""
import json,os,re,subprocess,sys,time
from concurrent.futures import ThreadPoolExecutor

UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
STORE="ids.json"
store=json.load(open(STORE)) if os.path.exists(STORE) else {}

def fetch(i):
    r=subprocess.run(['curl','-s','-r','0-8000','--max-time','20','-A',UA,'-w','\n@@%{http_code}',
        f'https://www.marvel.com/comics/issue/{i}/x'],capture_output=True,text=True).stdout
    code=r.rsplit('@@',1)[-1].strip()
    if code=='403': return (i,'__403__')
    m=re.search(r'<title>([^<]*)',r)
    if not m: return (i,None)
    t=m.group(1).replace(' | Comic Issues | Marvel','').strip()
    if 'Marvel.com |' in t: return (i,None)
    return (i,t)

def run(lo,hi,label,batch=12,workers=3,pause=1.5):
    todo=[i for i in range(lo,hi+1) if str(i) not in store]
    print(f"[{label}] {len(todo)} ids to probe ({lo}-{hi})",flush=True)
    idx=0; blocked=0
    while idx<len(todo):
        chunk=todo[idx:idx+batch]
        with ThreadPoolExecutor(max_workers=workers) as ex:
            res=list(ex.map(fetch,chunk))
        if any(t=='__403__' for _,t in res):
            blocked+=1
            wait=min(60*blocked,300)
            print(f"[{label}] 403 at {chunk[0]} — backing off {wait}s",flush=True)
            time.sleep(wait); continue          # retry same chunk
        blocked=0
        for i,t in res: store[str(i)] = t or ""
        idx+=batch
        json.dump(store,open(STORE,'w'))
        if idx % 120 == 0:
            found=sum(1 for v in store.values() if v)
            print(f"[{label}] {idx}/{len(todo)} probed, {found} titles banked",flush=True)
        time.sleep(pause)
    json.dump(store,open(STORE,'w'))
    print(f"[{label}] done",flush=True)

if __name__=="__main__":
    for spec in sys.argv[1:]:
        lo,hi,label=spec.split(':')
        run(int(lo),int(hi),label)
