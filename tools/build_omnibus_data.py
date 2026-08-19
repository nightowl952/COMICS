import json,re,collections,os,sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
# Paths are per-hero now and come from tools/heroes.py; these are rebound in
# main() once --hero is parsed. They stay module-level so gen() can read RAW.
RAW     = os.path.join(HERE, 'omnibus_contents_raw.json')
TRACKER = os.path.join(ROOT, 'spiderman-reading-tracker.html')

# wiki series title -> (short code, display name used in the UI)
# "Spectacular Spider-Man Vol 1" and "Peter Parker, The Spectacular Spider-Man Vol 1"
# are the SAME series -- the book was retitled at #134. Both map to `pp`.
SERIES = {
 "Amazing Fantasy Vol 1":                              ("af",   "Amazing Fantasy"),
 "Amazing Spider-Man Vol 1":                           ("asm",  "Amazing Spider-Man"),
 "Amazing Spider-Man Vol 2":                           ("asm2", "Amazing Spider-Man (1999)"),
 "Amazing Spider-Man Annual Vol 1":                    ("asmann","Amazing Spider-Man Annual"),
 "Amazing Spider-Man Annual Vol 2":                    ("asm2ann","Amazing Spider-Man Annual (1999)"),
 "Ultimate Spider-Man Vol 1":                          ("usm",  "Ultimate Spider-Man"),
 "Ultimate Spider-Man Vol 2":                          ("ucsm", "Ultimate Comics Spider-Man"),
 "Ultimate Avengers vs. New Ultimates Vol 1":          ("uavn", "Ultimate Avengers vs. New Ultimates"),
 "Ultimate Fallout Vol 1":                             ("ufal", "Ultimate Fallout"),
 "Amazing Spider-Man Ashcan Vol 1":                    ("asmash","Amazing Spider-Man Ashcan"),
 "Amazing Spider-Man Super Special Vol 1":             ("asmss", "Amazing Spider-Man Super Special"),
 "Peter Parker, The Spectacular Spider-Man Vol 1":     ("pp",   "Spectacular Spider-Man"),
 "Spectacular Spider-Man Vol 1":                       ("pp",   "Spectacular Spider-Man"),
 "Peter Parker, The Spectacular Spider-Man Annual Vol 1":("ppann","Spectacular Spider-Man Annual"),
 "Spectacular Spider-Man Annual Vol 1":                ("ppann","Spectacular Spider-Man Annual"),
 "Spectacular Spider-Man Magazine Vol 1":              ("ppmag","Spectacular Spider-Man Magazine"),
 "Spectacular Spider-Man Super Special Vol 1":         ("ppss", "Spectacular Spider-Man Super Special"),
 "Web of Spider-Man Vol 1":                            ("web",  "Web of Spider-Man"),
 "Web of Spider-Man Annual Vol 1":                     ("webann","Web of Spider-Man Annual"),
 "Web of Spider-Man Super Special Vol 1":              ("webss","Web of Spider-Man Super Special"),
 "Spider-Man Vol 1":                                   ("spm",  "Spider-Man (1990)"),
 "Spider-Man Super Special Vol 1":                     ("spmss","Spider-Man Super Special"),
 "Spider-Man Unlimited Vol 1":                         ("spun", "Spider-Man Unlimited"),
 "Sensational Spider-Man Vol 1":                       ("sen",  "Sensational Spider-Man"),
 "Marvel Team-Up Vol 1":                               ("mtu",  "Marvel Team-Up"),
 "Marvel Team-Up Annual Vol 1":                        ("mtuann","Marvel Team-Up Annual"),
 "Untold Tales of Spider-Man Vol 1":                   ("utsm", "Untold Tales of Spider-Man"),
 "Untold Tales of Spider-Man Annual Vol 1":            ("utsmann","Untold Tales of Spider-Man Annual"),
 "Untold Tales of Spider-Man: Strange Encounters Vol 1":("utsmse","Untold Tales: Strange Encounters"),
 "Giant-Size Spider-Man Vol 1":                        ("gssm", "Giant-Size Spider-Man"),
 "Giant-Size Super-Heroes Featuring Spider-Man Vol 1": ("gssh", "Giant-Size Super-Heroes"),
 "Scarlet Spider Vol 1":                               ("ss",   "Scarlet Spider"),
 "Scarlet Spider Unlimited Vol 1":                     ("ssu",  "Scarlet Spider Unlimited"),
 "Web of Scarlet Spider Vol 1":                        ("wss",  "Web of Scarlet Spider"),
 "Amazing Scarlet Spider Vol 1":                       ("ass",  "Amazing Scarlet Spider"),
 "Spectacular Scarlet Spider Vol 1":                   ("pss",  "Spectacular Scarlet Spider"),
 "Green Goblin Vol 1":                                 ("gg",   "Green Goblin"),
 "New Warriors Vol 1":                                 ("nw",   "New Warriors"),
 "New Warriors Annual Vol 1":                          ("nwann","New Warriors Annual"),
 "Venom: Lethal Protector Vol 1":                      ("vlp",  "Venom: Lethal Protector"),
 "Venom: Along Came a Spider Vol 1":                   ("vacs", "Venom: Along Came a Spider"),
 "Venom Super Special Vol 1":                          ("vss",  "Venom Super Special"),
 "X-Force Vol 1":                                      ("xf",   "X-Force"),
 "Nova Vol 1":                                         ("nova", "Nova"),
 "Daredevil Vol 1":                                    ("dd",   "Daredevil"),
 "Fantastic Four Vol 1":                               ("ff",   "Fantastic Four"),
 "Fantastic Four Annual Vol 1":                        ("ffann","Fantastic Four Annual"),
 "Strange Tales Annual Vol 1":                         ("stann","Strange Tales Annual"),
 "Incredible Hulk Vol 1":                              ("hulk", "Incredible Hulk"),
 "Marvel Super-Heroes Vol 1":                          ("msh",  "Marvel Super-Heroes"),
 "Marvel Comics Presents Vol 1":                       ("mcp",  "Marvel Comics Presents"),
 "Marvel Treasury Edition Vol 1":                      ("mte",  "Marvel Treasury Edition"),
 "Marvel Two-In-One Vol 1":                            ("mtio", "Marvel Two-In-One"),
 "Marvel Premiere Vol 1":                              ("mprem","Marvel Premiere"),
 "Marvel Tales Vol 2":                                 ("mtales","Marvel Tales"),
 "What If? Vol 1":                                     ("wi",   "What If?"),
 "Not Brand Echh Vol 1":                               ("nbe",  "Not Brand Echh"),
 "Amazing Spider-Man: Soul of the Hunter Vol 1":       ("soul", "Soul of the Hunter"),
 "Spider-Man: Funeral for an Octopus Vol 1":           ("ffo",  "Funeral for an Octopus"),
 "Spider-Man The Clone Journal Vol 1":                 ("cj",   "The Clone Journal"),
 "Spider-Man Collectors' Preview Vol 1":               ("cp",   "Collectors' Preview"),
 "Spider-Man: The Jackal Files Vol 1":                 ("jf",   "The Jackal Files"),
 "Spider-Man: Maximum Clonage Alpha Vol 1":            ("mca",  "Maximum Clonage Alpha"),
 "Spider-Man: Maximum Clonage Omega Vol 1":            ("mco",  "Maximum Clonage Omega"),
 "Spider-Man Team-Up Vol 1":                           ("stu",  "Spider-Man Team-Up"),
 "Spider-Man: The Lost Years Vol 1":                   ("ly",   "The Lost Years"),
 "Spider-Man: The Parker Years Vol 1":                 ("py",   "The Parker Years"),
 "Spider-Man/Punisher: Family Plot Vol 1":             ("fp",   "Spider-Man/Punisher: Family Plot"),
 "Spider-Man Holiday Special Vol 1":                   ("hs",   "Spider-Man Holiday Special"),
 "Spider-Man: The Final Adventure Vol 1":              ("fa",   "The Final Adventure"),
 "Spider-Man: Redemption Vol 1":                       ("red",  "Spider-Man: Redemption"),
 "Spider-Man: Revelations Vol 1":                      ("rev",  "Spider-Man: Revelations"),
 "Osborn Journals Vol 1":                              ("oj",   "Osborn Journals"),
 "Spider-Man: Dead Man's Hand Vol 1":                  ("dmh",  "Dead Man's Hand"),
 "Spider-Man: 101 Ways to End the Clone Saga Vol 1":   ("101",  "101 Ways to End the Clone Saga"),
 "Wizard Mini-Comic Vol 1":                            ("wiz",  "Wizard Mini-Comic"),
 "Marvel Guide to Collecting Comics Vol 1":            ("mgcc", "Marvel Guide to Collecting Comics"),
 "Official Marvel Comics Try-Out Book Vol 1":          ("otb",  "Official Marvel Try-Out Book"),
 "Mighty Marvel Calendar for 1975 Vol 1":              ("cal75","Mighty Marvel Calendar 1975"),
 "Mighty Marvel Bicentennial Calendar for 1976 Vol 1": ("cal76","Marvel Bicentennial Calendar 1976"),
 "Marvel Comics Memory Album Calendar 1977 Vol 1":     ("cal77","Marvel Memory Album Calendar 1977"),
}

def parse(entry):
    m = re.match(r'^(.*) (\S+)$', entry.strip())
    if not m: return None
    base, num = m.group(1), m.group(2)
    if base not in SERIES: return ('??'+base, base, num)
    code, disp = SERIES[base]
    return (code, disp, num)

def spanlabel(nums):
    """Issue numbers are not all plain integers -- Untold Tales has a #-1
    (Flashback month) and annuals are numbered by year. Keep those out of the
    range so labels never read "#1--1".

    A run of one series is not necessarily contiguous: the JMS volume collects
    Amazing Spider-Man (1999) #30-58 and #500-514 across the renumbering, and
    Ultimate Comics Spider-Man does the same at #15 -> #150. Labelling that
    "#30-514" would claim 485 issues, so contiguous blocks are labelled
    separately and joined with commas."""
    plain=[n for n in nums if re.fullmatch(r'\d+',n)]
    odd=[n for n in nums if not re.fullmatch(r'\d+',n)]
    blocks=[]
    for n in plain:
        if blocks and int(n)==int(blocks[-1][-1])+1: blocks[-1].append(n)
        else: blocks.append([n])
    parts=[f"#{b[0]}" if len(b)==1 else f"#{b[0]}\u2013{b[-1]}" for b in blocks]
    parts += [f"#{o}" for o in odd]
    return ", ".join(parts)

def gen(pages, meta, series_extra=None):
    # SERIES is a shared lookup (wiki series title -> id prefix + display name).
    # It is not Spider-Man-only -- it already carries Nova, X-Force, New Warriors
    # and so on. A hero whose books collect series it lacks adds them through
    # SERIES_EXTRA in its own meta module rather than editing this table.
    if series_extra:
        SERIES.update(series_extra)
    out=[]
    d=json.load(open(RAW, encoding='utf-8'))
    for key in pages:
        v=d[key]; m=meta[key]
        seen=[];s=set()
        for x in v['issues']:
            if x not in s: s.add(x); seen.append(x)
        parsed=[]
        for x in seen:
            p=parse(x)
            if p is None or p[0].startswith('??'):
                print("  !! UNMAPPED:",x); continue
            parsed.append(p)
        # chapter strategy
        runs=[];cur=None
        for code,disp,num in parsed:
            if cur and cur[0]==code: cur[2].append((disp,num))
            else:
                if cur: runs.append(cur)
                cur=[code,disp,[(disp,num)]]
        if cur: runs.append(cur)
        avg=sum(len(r[2]) for r in runs)/len(runs)
        chapters=[]
        if avg>=3.5:
            for ci,(code,disp,items) in enumerate(runs):
                nums=[n for _,n in items]
                span = spanlabel(nums)
                chapters.append({'id':f"{m['id']}-c{ci+1}",'title':f"{disp} {span}",
                    'era':m['era'],'issues':[{'id':f"{code}-{n}",'t':f"{disp} #{n}",'s':disp} for _,n in items]})
        else:
            CH=6
            for ci in range(0,len(parsed),CH):
                blk=parsed[ci:ci+CH]
                first=f"{blk[0][1]} #{blk[0][2]}"; last=f"{blk[-1][1]} #{blk[-1][2]}"
                chapters.append({'id':f"{m['id']}-c{ci//CH+1}",'title':f"Part {ci//CH+1}",
                    'era':f"{first} → {last}",
                    'issues':[{'id':f"{c}-{n}",'t':f"{disp} #{n}",'s':disp} for c,disp,n in blk]})
        out.append({**{k:val for k,val in m.items()}, 'chapters':chapters,
                    'count':sum(len(c['issues']) for c in chapters)})
    return out


# ---------------------------------------------------------------------------
# Assembling and writing the shelf
#
# gen() only covers the wiki-backed volumes in ORDER. The full OMNI array is
# those plus PLACEHOLDERS, arranged in SHELF order. Key order is pinned so a
# regen produces a minimal diff instead of reshuffling all 18 entries.
# ---------------------------------------------------------------------------

KEY_ORDER = ["id","spine","cover","title","vol","creators","era","released",
             "art","tex","note","placeholder","chapters"]

MARK = "const OMNI = ["


def build_all(mod):
    """Return one hero's full OMNI array, in SHELF order."""
    ORDER, PLACEHOLDERS, SHELF = mod.ORDER, mod.PLACEHOLDERS, mod.SHELF
    meta = dict(ORDER)
    by_id = {o["id"]: o for o in gen(list(meta), meta,
                                     getattr(mod, "SERIES_EXTRA", None))}
    for p in PLACEHOLDERS:
        by_id[p["id"]] = dict(p)

    unknown = [v for v in SHELF if v not in by_id]
    if unknown:
        sys.exit("SHELF names ids with no entry in ORDER or PLACEHOLDERS: %s" % unknown)
    orphan = [v for v in by_id if v not in SHELF]
    if orphan:
        sys.exit("defined but missing from SHELF (it would not render): %s" % orphan)

    out = []
    for vid in SHELF:
        o = dict(by_id[vid])
        o.pop("count", None)          # derived at runtime by omniStats()
        extra = [k for k in o if k not in KEY_ORDER]
        if extra:
            sys.exit("unknown field(s) %s on %s -- add them to KEY_ORDER" % (extra, vid))
        out.append({k: o[k] for k in KEY_ORDER if k in o})
    return out


def render(arr):
    # indent=0 / ensure_ascii=False is the format already in the file; keeping it
    # byte-compatible is what makes a regen a small diff.
    return MARK[:-1] + json.dumps(arr, indent=0, ensure_ascii=False)


def splice(html, arr):
    s = html.index(MARK)
    e = html.index("\n];", s)
    return html[:s] + render(arr) + html[e + 2:]


MARK_IDS = "const MARVEL = {"


def splice_ids(html, ids_path):
    """Write marvel_ids.json into the tracker as the MARVEL map.

    The map was hand-synced before, which is how it drifted behind the store
    after a harvest. Same pinned serialization as the store itself so a regen
    that adds nothing is a no-op diff.
    """
    ids = json.load(open(ids_path, encoding="utf-8"))
    s0 = html.index(MARK_IDS)
    e0 = html.index("\n};", s0)
    return (html[:s0] + MARK_IDS[:-1]
            + json.dumps(ids, indent=0, ensure_ascii=False) + html[e0 + 2:])


def check_spine_colors(html, arr):
    """Every .o-* ramp a volume uses needs a SPINE_C entry.

    The book spine is painted from SPINE_C[o.art]; a ramp that is missing there
    silently falls back to the grey placeholder colour, which looks like a
    rendering bug rather than a missing map entry.
    """
    blk = html[html.index("const SPINE_C="):]
    blk = blk[:blk.index("};")]
    known = set(re.findall(r"'([\w-]+)':\s*\[", blk))
    missing = sorted({o["art"] for o in arr} - known)
    if missing:
        sys.exit("no SPINE_C entry for %s -- add one in %s or the spine renders grey"
                 % (missing, os.path.basename(TRACKER)))


def main():
    global RAW, TRACKER
    import heroes
    key, argv = heroes.arg(sys.argv[1:])
    h = heroes.resolve(key)
    RAW, TRACKER = h["raw_path"], h["tracker_path"]

    check = "--check" in argv
    arr = build_all(heroes.meta_module(h))
    html = open(TRACKER, encoding="utf-8").read()
    check_spine_colors(html, arr)
    new = splice_ids(splice(html, arr), h["ids_path"])

    print("[%s] %s" % (h["key"], h["tracker"]))
    slots = sum(len(c["issues"]) for o in arr for c in o["chapters"])
    uniq = len({i["id"] for o in arr for c in o["chapters"] for i in c["issues"]})
    covers = sum(1 for o in arr if o.get("cover"))
    print("%d volumes | %d issue slots | %d unique issues | %d covers wired"
          % (len(arr), slots, uniq, covers))
    ids = json.load(open(h["ids_path"], encoding="utf-8"))
    linked = len({i["id"] for o in arr for c in o["chapters"]
                  for i in c["issues"]} & set(ids))
    print("%d/%d unique issues (%d%%) have a marvel.com link | MARVEL carries %d ids"
          % (linked, uniq, round(linked * 100 / uniq) if uniq else 0, len(ids)))

    if check:
        print("in sync" if new == html else "OUT OF SYNC -- run without --check to rewrite")
        sys.exit(0 if new == html else 1)

    if new == html:
        print("%s already up to date" % os.path.basename(TRACKER))
    else:
        open(TRACKER, "w", encoding="utf-8").write(new)
        print("wrote %s" % os.path.basename(TRACKER))
    print("now run: python3 tools/build_single_file.py")


if __name__ == "__main__":
    sys.path.insert(0, HERE)
    # keep `... | head` from spewing a BrokenPipeError traceback
    try:
        import signal
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    except (ImportError, AttributeError, ValueError):
        pass
    main()
