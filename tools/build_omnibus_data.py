import json,re,collections

# wiki series title -> (short code, display name used in the UI)
# "Spectacular Spider-Man Vol 1" and "Peter Parker, The Spectacular Spider-Man Vol 1"
# are the SAME series -- the book was retitled at #134. Both map to `pp`.
SERIES = {
 "Amazing Fantasy Vol 1":                              ("af",   "Amazing Fantasy"),
 "Amazing Spider-Man Vol 1":                           ("asm",  "Amazing Spider-Man"),
 "Amazing Spider-Man Vol 2":                           ("asm2", "Amazing Spider-Man (1999)"),
 "Amazing Spider-Man Annual Vol 1":                    ("asmann","Amazing Spider-Man Annual"),
 "Amazing Spider-Man Annual Vol 2":                    ("asm2ann","Amazing Spider-Man Annual (1999)"),
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
    range so labels never read "#1--1"."""
    plain=[n for n in nums if re.fullmatch(r'\d+',n)]
    odd=[n for n in nums if not re.fullmatch(r'\d+',n)]
    parts=[]
    if plain: parts.append(f"#{plain[0]}" if len(plain)==1 else f"#{plain[0]}\u2013{plain[-1]}")
    parts += [f"#{o}" for o in odd]
    return ", ".join(parts)

def gen(pages, meta):
    out=[]
    d=json.load(open('omni.json'))
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
