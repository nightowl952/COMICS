#!/usr/bin/env python3
"""One-time scraper for omnibus cover art and printed-edition metadata.

Run this once, on a machine with network access. Everything it fetches is
written to disk -- covers to Art/covers/<id>.<ext>, metadata to
tools/omnibus_editions.json -- and then baked into the tracker by
build_omnibus_data.py. Nothing here runs at page load: the published trackers
must work with no network at all, and the Artifact CSP blocks remote images
outright, so a linked cover would render as a hole rather than a picture.

    python3 tools/scrape_covers.py              # fetch anything still missing
    python3 tools/scrape_covers.py --force      # refetch everything
    python3 tools/scrape_covers.py --reparse    # re-read the cache, no network
    python3 tools/scrape_covers.py --width 600  # bigger covers (default 400)

Every response is cached under tools/scrape_cache/ before it is parsed, so a
parsing bug costs a re-parse rather than another pass over a rate-limited API.

Source: the Marvel Database wiki (marvel.fandom.com), which is already where
the volume *contents* come from. Text there is CC BY-SA 4.0 and wants
attribution. Cover scans are Marvel's, hosted by Fandom under a fair-use claim.
Open Library is used as a fallback for covers only, keyed by the scraped ISBN.

If a volume never resolves, just drop a JPEG at Art/covers/<id>.jpg by hand --
the generator picks up whatever is in that directory and does not care where it
came from.
"""
import argparse, json, os, re, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CACHE = os.path.join(HERE, 'scrape_cache')
ART = os.path.join(ROOT, 'Art', 'covers')
OUT = os.path.join(HERE, 'omnibus_editions.json')
API = 'https://marvel.fandom.com/api.php'
UA = ('COMICS-reading-tracker/1.0 (personal, non-commercial; '
      'https://github.com/nightowl952/COMICS)')

# Infobox keys vary by template and the omnibus pages do not all use the same
# one, so match on aliases rather than assuming a single template's field set.
FIELDS = {
    'image':       ['Image', 'Cover', 'Image1'],
    'format':      ['Format'],
    'pages':       ['PageCount', 'Pages'],
    'released':    ['ReleaseDate', 'Released', 'CoverDate'],
    'isbn':        ['ISBN13', 'ISBN'],
    'price':       ['Price', 'CoverPrice'],
    'coverArtist': ['CoverArtists', 'CoverArtist', 'Image_Artist'],
    'editor':      ['Editors', 'Editor'],
    'publisher':   ['Publisher'],
}


def get(url, binary=False, tries=5):
    """Fetch with backoff. 403/429 from either host means slow down, not stop."""
    for n in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=45) as r:
                return r.read() if binary else r.read().decode('utf-8', 'replace')
        except urllib.error.HTTPError as e:
            if e.code in (403, 429, 503) and n < tries - 1:
                wait = 5 * (n + 1)
                print(f"    {e.code} -- backing off {wait}s", flush=True)
                time.sleep(wait); continue
            print(f"    HTTP {e.code} for {url[:90]}")
            return None
        except Exception as e:
            if n < tries - 1:
                time.sleep(3 * (n + 1)); continue
            print(f"    {type(e).__name__}: {e}")
            return None
    return None


def api(**params):
    params.setdefault('format', 'json')
    return get(API + '?' + urllib.parse.urlencode(params))


def cached(name, produce):
    """Read from tools/scrape_cache/, else produce and store."""
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, re.sub(r'[^A-Za-z0-9._-]', '_', name))
    if os.path.exists(path):
        return open(path, encoding='utf-8').read()
    if REPARSE:
        return None
    val = produce()
    if val is not None:
        open(path, 'w', encoding='utf-8').write(val)
        time.sleep(PAUSE)
    return val


def _link(m):
    """[[Target|Display]] -> the more useful of the two.

    Creator fields are often [[Steve Ditko|Ditko, Steve]], where the display
    text is a sort key and the target is the natural name. Prefer the target
    when the display looks like "Last, First"; otherwise the display wins."""
    target = (m.group(1) or '')[:-1].strip()
    disp = m.group(2).strip()
    if target and re.fullmatch(r'[^,]+,\s*[^,]+', disp):
        return target
    return disp or target


def clean(v):
    """Wikitext value -> plain text.

    A template wrapping a value ({{USD|99.99}}) keeps its last argument rather
    than being deleted -- dropping those silently loses every cover price."""
    v = re.sub(r'<ref[^>]*>.*?</ref>', '', v, flags=re.S)
    v = re.sub(r'\{\{([^{}]*)\}\}', lambda m: m.group(1).split('|')[-1], v)
    v = re.sub(r'\[\[([^\]|]*\|)?([^\]]*)\]\]', _link, v)
    v = re.sub(r'<br\s*/?>', ', ', v, flags=re.I)
    v = re.sub(r"'''?", '', v)
    v = re.sub(r'<[^>]+>', '', v)
    v = re.sub(r'\s+', ' ', v).strip().strip(',').strip()
    return v


def infobox(wikitext):
    """Every `| Key = Value` in the page, flattened. Later keys do not overwrite
    earlier ones -- the lead infobox wins over anything repeated further down."""
    out = {}
    for m in re.finditer(r'^\s*\|\s*([A-Za-z0-9_ ]+?)\s*=\s*(.*)$', wikitext, re.M):
        k = m.group(1).strip()
        if k not in out:
            out[k] = m.group(2)
    return out


def pick(box, names):
    for n in names:
        if n in box:
            v = clean(box[n])
            if v:
                return v
    return None


def resolve_page(title):
    """Confirm the wiki page title, searching if the stored one is wrong."""
    j = cached(f'resolve_{title}.json',
               lambda: api(action='query', titles=title, prop='info'))
    if j:
        try:
            pages = json.loads(j)['query']['pages']
            if '-1' not in pages:
                return title
        except Exception:
            pass
    j = cached(f'search_{title}.json',
               lambda: api(action='query', list='search', srsearch=title, srlimit='5'))
    if not j:
        return None
    try:
        hits = json.loads(j)['query']['search']
    except Exception:
        return None
    for h in hits:
        if 'omnibus' in h['title'].lower() or 'omnibus' in title.lower():
            print(f"    resolved via search -> {h['title']}")
            return h['title']
    return hits[0]['title'] if hits else None


def image_url(title, box, width):
    """Cover URL at roughly `width` px. Ask the API for the thumbnail so no
    local image library is needed to resize."""
    fn = box.get('image')
    if fn:
        fn = re.sub(r'^(File|Image):', '', fn, flags=re.I).strip()
        j = cached(f'img_{fn}.json',
                   lambda: api(action='query', titles='File:' + fn,
                               prop='imageinfo', iiprop='url', iiurlwidth=str(width)))
        if j:
            try:
                for p in json.loads(j)['query']['pages'].values():
                    ii = p.get('imageinfo', [{}])[0]
                    if ii.get('thumburl') or ii.get('url'):
                        return ii.get('thumburl') or ii.get('url')
            except Exception:
                pass
    j = cached(f'pageimg_{title}.json',
               lambda: api(action='query', titles=title, prop='pageimages',
                           piprop='thumbnail', pithumbsize=str(width)))
    if j:
        try:
            for p in json.loads(j)['query']['pages'].values():
                t = p.get('thumbnail', {}).get('source')
                if t:
                    return t
        except Exception:
            pass
    return None


def openlibrary(isbn):
    if not isbn:
        return None
    digits = re.sub(r'[^0-9Xx]', '', isbn)
    return f'https://covers.openlibrary.org/b/isbn/{digits}-L.jpg?default=false'


def have_cover(vid):
    return any(os.path.splitext(f)[0] == vid for f in os.listdir(ART)) if os.path.isdir(ART) else False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--force', action='store_true', help='refetch volumes already done')
    ap.add_argument('--reparse', action='store_true', help='parse the cache only, no network')
    ap.add_argument('--width', type=int, default=400, help='cover width in px (default 400)')
    ap.add_argument('--pause', type=float, default=1.0, help='seconds between requests')
    ap.add_argument('--only', help='comma-separated volume ids')
    a = ap.parse_args()

    global REPARSE, PAUSE
    REPARSE, PAUSE = a.reparse, a.pause

    sys.path.insert(0, HERE)
    import omnibus_meta as M
    wiki = {m['id']: k for k, m in M.ORDER}
    titles = {m['id']: (m.get('title', '') + ' ' + m.get('vol', '')).strip()
              for _, m in M.ORDER}
    for ph in M.PLACEHOLDERS:
        wiki[ph['id']] = ph.get('wiki')
        titles[ph['id']] = (ph['title'] + ' ' + ph.get('vol', '')).strip()

    os.makedirs(ART, exist_ok=True)
    editions = json.load(open(OUT)) if os.path.exists(OUT) else {}
    want = a.only.split(',') if a.only else M.SHELF

    for vid in want:
        if vid not in wiki:
            print(f"{vid}: not on the shelf, skipped"); continue
        done = vid in editions and have_cover(vid)
        if done and not a.force:
            print(f"{vid}: already done"); continue
        print(f"{vid}:")

        page = wiki[vid] or titles[vid]
        page = resolve_page(page)
        if not page:
            print("    no wiki page found"); continue

        wt = cached(f'wikitext_{page}.json',
                    lambda: api(action='parse', page=page, prop='wikitext'))
        box = {}
        if wt:
            try:
                box = {k: v for k, v in
                       ((f, pick(infobox(json.loads(wt)['parse']['wikitext']['*']), names))
                        for f, names in FIELDS.items()) if v}
            except Exception as e:
                print(f"    wikitext parse failed: {e}")
        meta = {k: v for k, v in box.items() if k != 'image'}
        if re.fullmatch(r'[\d.]+', meta.get('price', '')):
            meta['price'] = '$' + meta['price']
        if meta:
            # Wiki values win over anything seeded from retail listings, and the
            # provenance goes with them -- leaving a stale "retail" source note
            # on wiki-sourced fields would misreport where the data came from.
            prev = {k: v for k, v in editions.get(vid, {}).items()
                    if k not in ('printing', 'note')}
            editions[vid] = {**prev, **meta, 'source': f'Marvel Database wiki: {page}'}
            print("    " + ", ".join(f"{k}={v[:34]}" for k, v in meta.items()))
        else:
            print("    no edition fields found")

        if have_cover(vid) and not a.force:
            continue
        url = image_url(page, box, a.width) or openlibrary(editions.get(vid, {}).get('isbn'))
        if not url:
            print("    no cover url"); continue
        if REPARSE:
            print(f"    cover url (not downloaded, --reparse): {url[:90]}"); continue
        blob = get(url, binary=True)
        if not blob or len(blob) < 2000:
            print(f"    cover download failed or too small ({len(blob or b'')} bytes)"); continue
        ext = '.png' if blob[:4] == b'\x89PNG' else '.jpg'
        for old in os.listdir(ART):
            if os.path.splitext(old)[0] == vid:
                os.remove(os.path.join(ART, old))
        open(os.path.join(ART, vid + ext), 'wb').write(blob)
        print(f"    cover -> Art/covers/{vid}{ext} ({len(blob)//1024} KB)")
        time.sleep(PAUSE)

    json.dump(editions, open(OUT, 'w'), indent=1, sort_keys=True, ensure_ascii=False)
    covers = sum(1 for v in M.SHELF if have_cover(v))
    print(f"\n{covers}/{len(M.SHELF)} covers on disk, {len(editions)} volumes with metadata")
    print("now run: python3 tools/build_omnibus_data.py && python3 tools/build_single_file.py")


if __name__ == '__main__':
    REPARSE, PAUSE = False, 1.0
    main()
