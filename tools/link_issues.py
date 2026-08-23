#!/usr/bin/env python3
"""Link every shelf issue to its marvel.com page, using the local catalog.

This replaces the old hand-maintained route (harvest an id range, then add a
`SLUG_PFX` entry by hand so `series_harvest.py write` will keep it). That route
silently dropped anything nobody had thought to add a table entry for, which is
how Books of Doom sat unlinked while all six issues were live on marvel.com.

Here nothing is hand-maintained. The catalog (tools/catalog.py) holds every
Marvel issue with its series id and issue number, and this matches shelf issues
against it two ways:

  1. **Learn from what already works.** Every issue that IS linked tells us
     which marvel.com series its id prefix belongs to. `wolv-118` resolving to
     wolverine_1988_118 means prefix `wolv` is series 2014, so `wolv-55` must be
     issue 55 of series 2014. This is exact and needs no name matching.
  2. **Name-match the rest.** For a prefix with no linked issue yet, compare the
     shelf's series name against the catalog's series titles. A match is only
     accepted when it is unambiguous AND the series actually carries that issue
     number. Anything ambiguous is REPORTED, never guessed -- guessing quietly
     is the failure this tool exists to prevent.

    python3 tools/link_issues.py            # report only, writes nothing
    python3 tools/link_issues.py --write    # merge into tools/marvel_ids.json
"""
import json, os, re, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CAT = os.path.join(HERE, "marvel_catalog.json")
SER = os.path.join(HERE, "marvel_series.json")
IDS = os.path.join(HERE, "marvel_ids.json")

# Read from the hero registry, not a list here -- a shelf added to heroes.py
# has to be picked up without anyone remembering to edit this file. Silently
# skipping a hero is the exact failure this tool exists to end.
sys.path.insert(0, HERE)
import heroes                                                    # noqa: E402

TRACKERS = {k: h["tracker"] for k, h in heroes.HEROES.items()}


def load(p, d=None):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return {} if d is None else d


# The two sources name the same book differently in small, repetitive ways, so
# fold both sides hard rather than keeping a table of every difference:
#   "Hulk/Wolverine: 6 Hours"  vs  "Hulk/Wolverine: Six Hours"
#   "Wolverine and the Punisher: ..."  vs  "Wolverine/Punisher: ..."
#   "Wolverine: Doombringer"  vs  "WOLVERINE: DOOMBRINGER 1 (1997 - Present)"
NUMWORD = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
           "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten",
           "11": "eleven", "12": "twelve"}
ABBREV = {"ff": "fantastic four", "fcbd": "free comic book day",
          "gr": "ghost rider", "asm": "amazing spider man"}
NOISE = re.compile(r"\b(the|a|an|and|of|vs|volume|vol|one[- ]?shot|"
                   r"marvels|digital|comic)\b")


def norm(s):
    """Fold a series name to something comparable across the two sources."""
    s = s.lower()
    s = re.sub(r"\(\s*\d{4}.*?\)", " ", s)        # drop "(1988 - 1997)"
    s = re.sub(r"[^a-z0-9]+", " ", s)
    s = " ".join(ABBREV.get(w, NUMWORD.get(w, w)) for w in s.split())
    s = NOISE.sub(" ", s)
    s = re.sub(r"\b(19|20)\d\d\b", " ", s)
    # singularise: the two sources disagree on "Strange Encounter(s)"
    s = " ".join(w[:-1] if len(w) > 4 and w.endswith("s") and
                 not w.endswith("ss") else w for w in s.split())
    return re.sub(r"\s+", " ", s).strip()


# Genuine naming disagreements -- not spelling, different names for the same
# book. Keep this SHORT: it is a last resort, and the report at the bottom of a
# run names anything that might belong here, so it never grows silently.
ALIAS = {
    "uncanny x-men": "X-Men (1963 - 2011)",
    "aftersmash: damage control": "Wwh Aftersmash: Damage Control (2008)",
    "x-men spotlight": "X-Men Spotlight On Starjammers (1990)",
    "giant-size super-heroes": "Giant-Size Super-Heroes Featuring Spider-Man (1974)",
    # The book was retitled Power Man and Iron Fist at #50; marvel.com keeps
    # one series under the original name across the whole run, and the two
    # later series that DO carry the retitled name stop well short of #87.
    "power man and iron fist": "Power Man (1974 - 1986)",
}


# Series that only ever reprint someone else's issue. Never the thing a shelf
# means: "Giant-Size Super-Stars Facsimile Edition (2023)" is a 2023 reprint of
# the 1974 issue, and matching it would send the Read button to the wrong comic.
REPRINT_LINE = re.compile(
    r"\b(facsimile|true believers|director'?s cut|poster book|sketchbook|"
    r"mgc|omnibus|infinity comic)\b", re.I)


# The issue-number equivalent of ALIAS, keyed by shelf issue id. Same
# last-resort status and the same reason: not a spelling difference, the two
# sources genuinely numbering one comic differently. The Marvel Database files
# the 1989 Daredevil annual as "#4B" because its cover reprints the number 4;
# marvel.com numbers the run straight through and calls it #5. Keep this SHORT
# -- an unmatched issue is reported by name at the end of every run, so nothing
# lands here silently.
NUM_ALIAS = {
    "ddann-4B": "5",
    # All-New Marvel NOW! Point One shipped as #1.NOW -- ".NOW" is Marvel NOW!
    # branding on the cover, not an issue number -- and marvel.com files the
    # one issue that series has as #1. Deliberately NOT generalised into
    # numkey(): elsewhere a .NOW is a genuinely separate issue sitting beside a
    # plain #1 in the same run, so folding the suffix away would link those to
    # the wrong comic. This is the only .NOW on any shelf.
    "anmpo-1.NOW": "1",
    # Two more of the same shape from the Captain America shelf. Both are
    # ".NOW" cover branding on an issue marvel.com numbers plainly, and both
    # are pinned per-issue for the reason above rather than folded away.
    "cap7-16.NOW": "16",
    "wsolbm-1.NOW": "1",
}


# The last resort below both of those: a shelf issue pinned straight to its
# catalog id, because no rule can reach it from what the shelf knows.
#
# Every entry so far is a Marvel Graphic Novel. The wiki files that line by
# number ("Marvel Graphic Novel Vol 1 68"); marvel.com files each volume under
# its own story title ("Avengers Deathtrap - The Vault (1991)") as issue #1 of
# a one-issue series. The story title is the only thing that could match, and
# the pipeline strips it -- a raw-contents entry has to end in the issue number
# or the <series>/<issue> split fails -- so the information is gone by the time
# this runs. Hence a pin.
#
# Pin only after `catalog.py find "<story title>"` shows the issue really is
# there: these were read as "not on marvel.com" for months, which is the
# failure this is fixing. The id is enough -- the slug is read back out of the
# catalog, never typed here.
ISSUE_ALIAS = {
    "mgn-49": "61791",   # Doctor Strange & Doctor Doom: Triumph and Torment
    "mgn-65": "65023",   # Wolverine: Bloodlust
    "mgn-67": "65025",   # Wolverine: The Jungle Adventure
    "mgn-68": "67091",   # Avengers: Death Trap, The Vault
}


def name_keys(title):
    """Every way a catalog series title might be written on a shelf.

    Marvel titles a lot of one-shots "<NAME> 1", and prefixes minis with the
    lead character ("Spider-Man: Funeral For An Octopus" for a book the shelf
    just calls "Funeral for an Octopus"), so index the bare tail too.
    """
    keys = {norm(title)}
    bare = re.sub(r"\(\s*\d{4}.*?\)", "", title).strip()
    trail = re.sub(r"\s+(-?\d+(?:/\d+)?)$", "", bare)  # " 1", " -1", " 1/2"
    keys.add(norm(trail))
    if ":" in bare:
        tail = bare.rsplit(":", 1)[-1]
        keys.add(norm(re.sub(r"\s+(-?\d+(?:/\d+)?)$", "", tail)))
    return {k for k in keys if len(k) > 3}


def numkey(n):
    """Issue numbers arrive as 5, '5', '5.1', '5.50', '1/2'. Compare as text.

    Trailing zeros after the point are the trap. The wiki writes Daredevil
    (2014) #1.50 where the catalog stores 1.5, and an exact string compare
    misses a link that is sitting right there -- so normalise any decimal, not
    just the ".0" case.
    """
    if n is None:
        return None
    s = str(n).strip().replace("½", "0.5").replace("1/2", "0.5")
    if re.fullmatch(r"-?\d+\.\d+", s):
        s = s.rstrip("0").rstrip(".")
    return s


def era_range(era):
    """'1961-1964' -> (1961, 1964). The volume's era is what disambiguates a
    reused series name -- there are seven X-Forces, but only one of them was
    running while the book that collects it was set."""
    if not era:
        return None
    yrs = [int(y) for y in re.findall(r"(\d{4})", era)]
    return (min(yrs), max(yrs)) if yrs else None


def series_years(title):
    """'X-Men (1963 - 2011)' -> (1963, 2011). 'Present' means still running."""
    m = re.search(r"\((\d{4})\s*(?:-\s*(\d{4}|Present))?\)", title or "",
                  re.I)
    if not m:
        return None
    a = int(m.group(1))
    b = m.group(2)
    return (a, 9999 if (b or "").lower() == "present" else int(b or a))


def slug_year(slug):
    m = re.search(r"_(\d{4})_", slug)
    return int(m.group(1)) if m else None


def shelf_issues():
    """-> list of dicts for every issue on every shelf, linked or not."""
    out = []
    for hero, fn in TRACKERS.items():
        src = open(os.path.join(ROOT, fn), encoding="utf-8").read()
        omni = json.loads(re.search(r"const OMNI = (\[.*?\n\]);", src, re.S).group(1))
        mar = json.loads(re.search(r"const MARVEL = (\{.*?\n\});", src, re.S).group(1))
        seen = set()
        for o in omni:
            for ch in o.get("chapters", []):
                for it in ch["issues"]:
                    if it["id"] in seen:
                        continue
                    seen.add(it["id"])
                    m = re.match(r"^(.*?)-([0-9]+(?:\.[0-9]+)?|-1|½|.+)$", it["id"])
                    pfx, num = (m.group(1), m.group(2)) if m else (it["id"], None)
                    yr = re.search(r"\((\d{4})\)", it["s"])
                    out.append(dict(hero=hero, vol=o["id"], id=it["id"],
                                    t=it["t"], s=it["s"], pfx=pfx,
                                    num=NUM_ALIAS.get(it["id"]) or numkey(num),
                                    link=mar.get(it["id"]),
                                    year=int(yr.group(1)) if yr else None,
                                    era=era_range(o.get("era"))))
    return out


def is_point_issue(num):
    """#102.5 yes, #102 no. A .1/.5 issue is numbered inside its series' run."""
    try:
        return float(num) != int(float(num))
    except (TypeError, ValueError):
        return False


def tiebreak(hit, it, sers):
    """Narrow several same-named series down to one, or leave it ambiguous.

    A title gets reused a lot -- seven X-Forces, four Amazing Fantasys. Each
    rule below is tried in turn and the first that leaves exactly one candidate
    wins; if none does, the caller reports it rather than picking.
    """
    yrs = {c: series_years(sers.get(str(c), "")) for c in hit}
    lo, hi = it["era"] or (0, 9999)
    def overlap(c):
        """Years the series and the volume's era share."""
        if not yrs[c]:
            return 0
        return max(0, min(yrs[c][1], hi) - max(yrs[c][0], lo) + 1)

    best = max((overlap(c) for c in hit), default=0)
    rules = [
        # the shelf named a year ("Spider-Man 2099 (2014)") -- trust it first
        lambda c: it["year"] and yrs[c] and yrs[c][0] <= it["year"] <= yrs[c][1],
        # else the series running for MOST of the volume's span is the one it
        # collects. Plain overlap is not enough: Avengers (2010-2012) and
        # Avengers (2012-2015) both touch a 2012-2014 volume, but only one of
        # them was the book for three of those years.
        lambda c: best and overlap(c) == best,
        # a revival continuing the old numbering beats a later reboot
        lambda c: yrs[c] and yrs[c][0] == min(
            v[0] for v in yrs.values() if v),
        # an exact title match beats one found through a shortened key
        lambda c: norm(sers.get(str(c), "")) == norm(it["s"]),
    ]
    for rule in rules:
        got = [c for c in hit if rule(c)]
        if len(got) == 1:
            return got
        if got:
            hit = got            # narrowed but still tied -- keep going
    return hit


def match():
    """-> (added {issue id: 'cid/slug'}, ambiguous, unmatched, issues)."""
    cat, sers = load(CAT), load(SER)
    if not cat:
        sys.exit("no catalog yet -- run: python3 tools/catalog.py sweep")

    # (series_id, issue number) -> comic id, preferring the non-variant record
    by_ser = {}
    for cid, (slug, sid, num, mu, var) in cat.items():
        if sid is None:
            continue
        k = (sid, numkey(num))
        if k not in by_ser or (var == 0 and cat[by_ser[k]][4] == 1):
            by_ser[k] = cid
    # series name -> set of series ids
    by_name = defaultdict(set)
    for sid, title in sers.items():
        if REPRINT_LINE.search(title):
            continue
        for k in name_keys(title):
            by_name[k].add(int(sid))

    series_words = {int(sid): set(norm(t).split()) for sid, t in sers.items()
                    if not REPRINT_LINE.search(t)}
    series_issues = defaultdict(list)
    for cid, rec in cat.items():
        if rec[1] and not rec[4]:
            series_issues[rec[1]].append(cid)
    issues = shelf_issues()
    # step 1: learn prefix -> marvel series id from issues that already resolve
    votes = defaultdict(Counter)
    slug_to_cid = {v[0]: k for k, v in cat.items()}
    for it in issues:
        if not it["link"]:
            continue
        cid = it["link"].split("/", 1)[0]
        rec = cat.get(cid)
        if rec is None:
            rec = cat.get(slug_to_cid.get(it["link"].split("/", 1)[1], ""))
        if rec and rec[1]:
            votes[it["pfx"]][rec[1]] += 1
    learned = {p: c.most_common(1)[0][0] for p, c in votes.items()}
    # which prefix already owns each marvel series, from links that work
    claimed = {sid: p for p, sid in learned.items()}

    # which marvel series each volume is made of, and which (series, issue)
    # slots the shelves already point at -- both read off the links that work
    volume_series, taken_slots = defaultdict(Counter), set()
    for it in issues:
        if not it["link"]:
            continue
        rec = cat.get(it["link"].split("/", 1)[0])
        if rec and rec[1]:
            volume_series[it["vol"]][rec[1]] += 1
            taken_slots.add((rec[1], numkey(rec[2])))

    added, unmatched, ambiguous, mistimed, how = {}, [], [], [], {}
    for it in issues:
        if it["link"]:
            continue
        pin = ISSUE_ALIAS.get(it["id"])
        if pin:
            if pin not in cat:
                sys.exit("ISSUE_ALIAS pins %s to catalog id %s, which the "
                         "catalog does not hold" % (it["id"], pin))
            added[it["id"]] = "%s/%s" % (pin, cat[pin][0])
            how[it["id"]] = "pinned"
            continue
        if it["num"] is None:
            continue
        sid = learned.get(it["pfx"])
        why = "learned"
        if sid is not None and (sid, it["num"]) not in by_ser:
            # The prefix's usual series does not carry this number, so this
            # issue is not from it -- "Ultimate Spider-Man #1/2" is its own
            # series on marvel.com. Fall through rather than give up.
            sid = None
        if sid is None:                              # step 2: name match
            al = ALIAS.get(it["s"].lower())
            cands = by_name.get(norm(al if al else it["s"]), set())
            hit = [s for s in cands if (s, it["num"]) in by_ser]
            if not hit:
                # Marvel often carries the shelf's name inside a longer one:
                # "Peter Parker, The Spectacular Spider-Man Annual" for the
                # shelf's "Spectacular Spider-Man Annual", "Incredible Hulk:
                # Hercules Unleashed" for "Hulk: Hercules Unleashed". Accept a
                # series whose words are a superset of the shelf's, but only
                # when exactly one such series carries this issue number.
                want = set(norm(it["s"]).split())
                if len(want) > 1:
                    hit = [sid2 for sid2, ws in series_words.items()
                           if want <= ws and (sid2, it["num"]) in by_ser]
            if not hit:
                # Two exact shapes, and nothing looser -- an earlier version
                # accepted any single-issue series for any number, which read
                # Marvel Graphic Novel #49, #50, #65 and #67 as all being #38.
                #
                #  (a) a genuine one-shot the shelf calls #1, which marvel.com
                #      filed as #0 (Ghost Rider/Wolverine/Punisher: The Dark
                #      Design), and
                #  (b) a series named for the very issue asked for -- "UNTOLD
                #      TALES OF SPIDER-MAN -1" holds the #-1 issue, as #0.
                want_num = (it["num"] or "").lower()
                solo = []
                for sid2 in cands:
                    if len(series_issues[sid2]) != 1:
                        continue
                    title = re.sub(r"\(\s*\d{4}.*?\)", "", sers.get(str(sid2), ""))
                    named = title.strip().lower().endswith(" " + want_num)
                    if named or want_num in ("1", "0"):
                        solo.append(sid2)
                if len(solo) == 1:
                    only = series_issues[solo[0]][0]
                    hit, it = solo, dict(it, num=numkey(cat[only][2]))
            if not hit and re.fullmatch(r"(19|20)\d\d", it["num"] or ""):
                # An annual numbered by year ("Wolverine Annual #1995") is a
                # one-issue series of that year on marvel.com, not issue 1995.
                hit = [s for s in cands
                       if (s, "1") in by_ser
                       and slug_year(cat[by_ser[(s, "1")]][0]) == int(it["num"])]
                if len(hit) == 1:
                    it = dict(it, num="1")
            if len(hit) > 1:
                hit = tiebreak(hit, it, sers)
            if len(hit) == 1:
                sid, why = hit[0], "name"
            elif len(hit) > 1:
                ambiguous.append((it, sorted(hit)))
                continue
        cid = by_ser.get((sid, it["num"])) if sid else None
        if not cid and is_point_issue(it["num"]):
            # Step 3, and deliberately narrow: a POINT ISSUE only.
            #
            # marvel.com numbers these inside the run (Wolverine (1988)
            # #102.5); the wiki files them under a name marvel.com never used
            # ("Wolverine Special #102.5"), so no name match can work. The
            # volume around it is full of issues that do resolve, so the right
            # series is sitting right there.
            #
            # This is restricted to a fractional number on purpose. Trying it
            # for whole numbers reads "Epic Illustrated #26" as Fantastic Four
            # Annual #26 and "FOOM #4" as Secret Wars #4 -- a low number exists
            # in hundreds of series, so being in the same book proves nothing.
            # A .5 is rare enough that it does.
            for cand, _n in volume_series[it["vol"]].most_common():
                c2 = by_ser.get((cand, it["num"]))
                if c2 and (cand, it["num"]) not in taken_slots:
                    sid, cid, why = cand, c2, "point issue"
                    break
        if cid and why == "name" and claimed.get(sid, it["pfx"]) != it["pfx"]:
            # Two shelf series cannot be one marvel.com series. The shelf keeps
            # the wiki's volumes apart (`tta` is Tales to Astonish Vol 1, `tta3`
            # is Vol 3), so if a prefix whose links already work owns this
            # series, a second prefix matching it by name is a different comic
            # that merely shares a title and an issue number.
            mistimed.append((it, sers.get(str(sid), "?"),
                             claimed[sid]))
            continue
        if not cid:
            unmatched.append((it, sid))
            continue
        added[it["id"]] = "%s/%s" % (cid, cat[cid][0])
        how[it["id"]] = why

    return added, ambiguous, unmatched, mistimed, issues, how


def main(argv):
    added, ambiguous, unmatched, mistimed, issues, how = match()
    if "--dump" in argv:
        json.dump([dict(i, sid=s) for i, s in unmatched],
                  open(os.path.join(HERE, "unlinked.json"), "w"), indent=1)
    print("%d unlinked issues on the shelves" % sum(1 for i in issues if not i["link"]))
    print("  %d matched  (%d by learned series, %d by name)"
          % (len(added),
             sum(1 for v in how.values() if v == "learned"),
             sum(1 for v in how.values() if v == "name")),
          "+ %d point issues placed from their volume, %d pinned"
          % (sum(1 for v in how.values() if v == "point issue"),
             sum(1 for v in how.values() if v == "pinned")))
    print("  %d ambiguous (reported, never guessed)" % len(ambiguous))
    print("  %d not in the catalog" % len(unmatched))
    print("  %d rejected: that series already belongs to another shelf series"
          % len(mistimed))
    for it, t, owner in mistimed[:15]:
        print("    rejected:  %-14s %-34s already linked as '%s'"
              % (it["id"], t, owner))
    for it, hit in ambiguous[:25]:
        print("    ambiguous: %-34s %-30s -> series %s"
              % (it["id"], it["s"], hit))
    if unmatched:
        print("\n  not found, by series:")
        for s, n in Counter(i["s"] for i, _ in unmatched).most_common(25):
            print("    %-46s %d" % (s, n))

    if "--write" in argv:
        ids = load(IDS)
        ids.update(added)
        json.dump(ids, open(IDS, "w", encoding="utf-8"), indent=0,
                  ensure_ascii=False)
        print("\nwrote %d new ids -> tools/marvel_ids.json" % len(added))
        print("now run build_omnibus_data.py for each hero")


if __name__ == "__main__":
    main(sys.argv[1:])
