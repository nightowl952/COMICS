#!/usr/bin/env python3
"""Harvest marvel.com issue ids a series at a time.

`harvest.py` probes a range of issue ids one at a time and hopes the range was
right. This does not have to guess:

  * `/comics/series/<id>/<anything>` resolves on the id alone and lists ~20 of
    that series' issues as `/comics/issue/<id>/<slug>` -- which is exactly the
    "<id>/<slug>" fragment the tracker stores.
  * an issue page links to its neighbours in the same series, so one known
    issue walks out to the whole run at about a request per issue.
  * the slug (`immortal_hulk_2018_31`) already carries series, launch year and
    issue number, so nothing has to be looked up to key it.

Blind id scanning is still needed for the pre-2008 material, where marvel.com's
series pages only surface the tail of a long run -- see "Marvel deep links" in
CLAUDE.md for which id regime is which.

    python3 tools/series_harvest.py probe  2350:2650        # id -> series title
    python3 tools/series_harvest.py series 2400 2418 2538   # series -> issues
    python3 tools/series_harvest.py walk   immortal_hulk_2018:77345
    python3 tools/series_harvest.py write                   # -> marvel_ids.json

The first three append to tools/series_links.json (slug -> id) and are
resumable. `write` is the only one that touches marvel_ids.json, and it only
adds slugs whose prefix is in SLUG_PFX below -- an unmapped prefix is reported,
not guessed at. Finish with `build_omnibus_data.py --hero <key>`.
"""
import json, os, re, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
LINKS = os.path.join(HERE, "series_links.json")
TITLES = os.path.join(HERE, "series_titles.json")
IDS = os.path.join(HERE, "marvel_ids.json")

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120 Safari/537.36")
SER = re.compile(r"/comics/series/(\d+)/([a-z0-9_-]+)")
ISS = re.compile(r"/comics/issue/(\d+)/([a-z0-9_-]+)")

# marvel.com slug prefix -> our issue-id prefix. A callable takes the issue
# number, for a series the Marvel Database splits and marvel.com does not
# (Hulk (1999) is our `hk99` for #1-11 and `hulk2` from #12, where the book was
# retitled back to Incredible Hulk).
SLUG_PFX = {
 "incredible_hulk_1962": "hulk",
 "tales_to_astonish_1959": "tta",
 "hulk_1999": lambda n: "hk99" if n.isdigit() and int(n) <= 11 else "hulk2",
 "hulk_2008": "hulk08",
 "hulk_2021": "hulk21",
 "immortal_hulk_2018": "imm",
 "incredible_hulk_2009": "hulk3",
 "incredible_hulk_annual_1976": "hkann",
 "incredible_hulk_annual_1968": "hkss",
 "incredible_hulk_the_end_2002": "hkend",
 "rampaging_hulk_1998": "rhulk",
 "savage_hulk_1996": "svh",
 "giant-size_hulk_2006": "gshulk",
 "king-size_hulk_2008": "kshulk",
 "marvel_adventures_hulk_2007": "mahulk",
 "hulk_monster-size_special_2008": "hkmss",
 "hulk-sized_mini_hulks_2010": "hsmh",
 "hulk_vs_fin_fang_foom_2007": "hkfff",
 "hulk_wolverine_6_hours_2003": "hkwolv",
 "hulk_thing_hard_knocks_2004": "hkthing",
 "hulk_destruction_2005": "hkdes",
 "hulk_broken_worlds_2009": "hkbw",
 "hulk_future_imperfect_1992": "hkfi",
 "future_imperfect_2015": "fimp",
 "maestro_2020": "mae",
 "maestro_war_and_pax_2021": "maewp",
 "maestro_world_war_m_2022": "maewwm",
 "abominations_1996": "abom",
 "world_war_hulk_2007": "wwh",
 "world_war_hulk_prologue_world_breaker_2007": "wwhwb",
 "world_war_hulk_x-men_2007": "wwhxm",
 "world_war_hulk_gamma_corps_2007": "wwhgc",
 "world_war_hulk_front_line_2007": "wwhfl",
 "world_war_hulk_aftersmash_2007": "wwhas",
 "world_war_hulk_aftersmash_damage_control_2007": "wwhdc",
 "wwh_aftersmash_warbound_2007": "wwhwar",
 "fall_of_the_hulks_gamma_2010": "fothg",
 "gamma_flight_2021": "gflt",
 "immortal_hulk_the_best_defense_2018": "immbd",
 "immortal_hulk_time_of_monsters_2021": "immtom",
 "immortal_she-hulk_2020": "immsh",
 "absolute_carnage_immortal_hulk_2019": "acimm",
 "king_in_black_immortal_hulk_2021": "kibimm",
 "defenders_the_best_defense_2018": "defbd",
 "hulk_vs_thor_banner_of_war_alpha_2022": "bowa",
 "heroes_for_hire_2006": "hfh2",
 "ghost_rider_2006": "gr6",
 "punisher_war_journal_2006": "pwj2",
 "wolverine_2003": "wolv3",
 "the_invincible_iron_man_2004": "iim",
 "the_irredeemable_ant-man_2006": "iam",
 "avengers_the_initiative_2007": "avin",
 "new_avengers_illuminati_2006": "nail",
 "thor_2020": "thor6",
 "avengers_2016": "av7",
 "avengers_1963": "av",
 "captain_marvel_1999": "cm4",
 "exiles_2001": "exi",
 "spider-man_2099_2014": "sm2099",
 "symbiote_spider-man_crossroads_2021": "sssxr",
 "new_fantastic_four_2022": "nff",
 "fantastic_four_1998": "ff3",
 "fantastic_four_1961": "ff",
 "amazing_fantasy_2004": "af2",
 "x-factor_1986": "xfac",
 "cable_1993": "cable",
 "marvel_comics_presents_1988": "mcp",
 "marvel_super-heroes_1967": "msh",
 "heroes_reborn_the_return_1997": "hrret",
 "onslaught_marvel_universe_1996": "onsmu",
 "cutting_edge_1995": "cedge",
 # Spider-Man shelf -- the id store is shared, so these land for free
 "the_amazing_spider-man_1963": "asm",
 "the_amazing_spider-man_1999": "asm2",
 "amazing_spider-man_annual_1964": "asmann",
 "web_of_spider-man_1985": "web",
}


def load(path):
    return json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {}


def save(path, d):
    json.dump(d, open(path, "w", encoding="utf-8"), ensure_ascii=False)


def get(url, head=None):
    cmd = ["curl", "-s", "--max-time", "40", "-A", UA, url, "-w", "\n@@%{http_code}"]
    if head:
        cmd[2:2] = ["-r", "0-%d" % head]
    body = subprocess.run(cmd, capture_output=True, text=True).stdout
    return body.rsplit("@@", 1)[-1].strip(), body


def batched(items, fn, label, batch=8, workers=3, pause=1.0):
    """Run fn over items in small batches, backing off on a 403 and retrying
    the same batch -- marvel.com throttles hard, and burning through a range
    while blocked silently returns nothing."""
    i, blocked = 0, 0
    while i < len(items):
        chunk = items[i:i + batch]
        with ThreadPoolExecutor(max_workers=workers) as ex:
            res = list(ex.map(fn, chunk))
        if any(r is None for r in res):
            blocked += 1
            wait = min(45 * blocked, 240)
            print("  [%s] 403 - backing off %ds" % (label, wait), flush=True)
            time.sleep(wait)
            continue
        blocked = 0
        yield res
        i += batch
        time.sleep(pause)


# --------------------------------------------------------------- probe titles
def cmd_probe(args):
    titles = load(TITLES)

    def one(sid):
        code, body = get("https://www.marvel.com/comics/series/%d/x" % sid, head=9000)
        if code == "403":
            return None
        m = re.search(r"<title>([^<]*)", body)
        t = m.group(1).replace(" | Comic Series | Marvel", "").strip() if m else ""
        return (sid, "" if "Marvel.com |" in t else t)

    for spec in args:
        lo, hi = (int(x) for x in spec.split(":"))
        todo = [i for i in range(lo, hi + 1) if str(i) not in titles]
        print("[%d-%d] %d series ids to probe" % (lo, hi, len(todo)), flush=True)
        for res in batched(todo, one, spec):
            for sid, t in res:
                titles[str(sid)] = t
                if t:
                    print("  %d  %s" % (sid, t), flush=True)
            save(TITLES, titles)


# ------------------------------------------------------------ series -> issues
def series_issues(body, sid, slug):
    """Issue links on a series page, minus the promo rail of unrelated comics.

    The series' own issues all share one slug stem and outnumber everything
    else on the page, so the largest stem group is the series. Matching the
    series slug directly does not work: series world_war_hulk_xmen_2007 holds
    issues world_war_hulk_x-men_2007_N.
    """
    groups = {}
    for iid, islug in ISS.findall(body):
        stem = islug.rsplit("_", 1)[0] if re.search(r"_-?\d+$", islug) else islug
        groups.setdefault(stem, {})[islug] = iid
    best = max(groups.values(), key=len) if groups else {}
    if len(best) >= 2:
        return best
    # a one-shot has nothing to out-number the rail, so fall back to matching
    # the series slug, ignoring the punctuation the two spellings disagree on
    flat = lambda t: re.sub(r"[^a-z0-9]", "", t)
    stem = flat(slug).rstrip("0123456789")
    return {k: v for g in groups.values() for k, v in g.items()
            if flat(k).startswith(stem[:max(8, len(stem) - 6)])}


def cmd_series(args):
    links, titles = load(LINKS), load(TITLES)

    def one(sid):
        code, body = get("https://www.marvel.com/comics/series/%s/x" % sid)
        if code == "403":
            return None
        if code != "200":
            return (sid, None, {})
        slug = next((b for a, b in SER.findall(body) if a == str(sid) and b != "x"), "x")
        return (sid, slug, series_issues(body, sid, slug))

    for res in batched([a for a in args], one, "series", batch=4):
        for sid, slug, issues in res:
            if slug is None:
                print("  %s  unreachable" % sid, flush=True); continue
            titles.setdefault(str(sid), slug)
            links.update(issues)
            print("  %-52s %d issues" % (slug, len(issues)), flush=True)
        save(LINKS, links); save(TITLES, titles)


# ---------------------------------------------------------------- walk a run
def cmd_walk(args):
    links = load(LINKS)

    def one(iid):
        code, body = get("https://www.marvel.com/comics/issue/%s/x" % iid)
        return None if code == "403" else (iid, ISS.findall(body))

    for spec in args:
        prefix, seed = spec.rsplit(":", 1)
        print("-- %s from %s" % (prefix, seed), flush=True)
        queue, visited = [seed], set()
        while queue:
            chunk = [i for i in queue[:6] if i not in visited]
            queue = queue[6:]
            if not chunk:
                continue
            got = None
            for res in batched(chunk, one, prefix, batch=6):
                got = res
            visited.update(i for i, _ in got)
            for _, found in got:
                for fid, fslug in found:
                    links.setdefault(fslug, fid)
                    # queue on the id, not on the slug being new: a slug
                    # already banked from a series page would otherwise stop
                    # the walk dead at the boundary
                    if (fslug.startswith(prefix + "_") and fid not in visited
                            and fid not in queue):
                        queue.append(fid)
            save(LINKS, links)
            n = sum(1 for s in links if s.startswith(prefix + "_"))
            print("   %s: %d issues known, %d queued" % (prefix, n, len(queue)), flush=True)


# ------------------------------------------------------------------- write out
def cmd_write(args):
    links, ids = load(LINKS), load(IDS)
    added, unknown = {}, {}
    for slug, iid in links.items():
        m = re.match(r"^(.*)_(-?\d+)$", slug)
        if not m:
            continue
        base, num = m.group(1), m.group(2)
        p = SLUG_PFX.get(base)
        if p is None:
            unknown[base] = unknown.get(base, 0) + 1
            continue
        if callable(p):
            p = p(num)
        key, val = "%s-%s" % (p, num), "%s/%s" % (iid, slug)
        if ids.get(key) != val:
            added[key] = val
    dry = "--dry-run" in args
    if not dry:
        ids.update(added)
        json.dump(ids, open(IDS, "w", encoding="utf-8"), indent=0, ensure_ascii=False)
    print("%d keys %s" % (len(added), "would be added" if dry else "written"))
    for s, n in sorted(unknown.items(), key=lambda x: -x[1]):
        print("  no SLUG_PFX entry (%3d issues): %s" % (n, s))
    if not dry:
        print("now run: python3 tools/build_omnibus_data.py --hero <key>")


CMDS = {"probe": cmd_probe, "series": cmd_series, "walk": cmd_walk, "write": cmd_write}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in CMDS:
        sys.exit(__doc__)
    CMDS[sys.argv[1]](sys.argv[2:])
