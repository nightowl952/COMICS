#!/usr/bin/env python3
"""Compose index.html + every tracker into ONE self-contained, hash-routed
page for publishing as a Claude Artifact (artifacts are one file per URL).

The source files are never modified. Rerun this after editing any of them.

The page list comes from tools/heroes.py, so registering an omnibus-shelf hero
there is enough -- nothing in this file names a hero.

What it has to solve:
  * CSS class names are defined in more than one file with different values
    -> every app's stylesheet is scoped under its own #app-<id> panel.
  * DOM ids collide (statRead, upnext, shelf, ...)
    -> every id is prefixed per app, in the markup AND in the JS that looks it up.
  * top-level JS names collide wholesale (SC, MARVEL, store, refresh, flat, ...)
    -> each script is wrapped in an IIFE, so nothing leaks.
"""
import re, json, sys, os, base64

SRC  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.dirname(os.path.abspath(__file__))

# The homescreen and the X-Men page are fixed (neither is an omnibus shelf);
# every shelf hero comes from the registry, so adding one does not mean editing
# this list. `shelf` marks the pages patch_app() treats as omnibus shelves.
def _apps():
    sys.path.insert(0, TOOLS)
    import heroes
    apps = [
        dict(key="home", pfx="hm", file="index.html",                route="/"),
        dict(key="xmen", pfx="xm", file="xmen-reading-tracker.html", route="/xmen"),
    ]
    for key in sorted(heroes.HEROES):
        h = heroes.HEROES[key]
        apps.append(dict(key=h["panel"], pfx=h["pfx"], file=h["tracker"],
                         route=h["route"], shelf=True))
    return apps

APPS = _apps()

def part(html, tag):
    m = re.search(r'<%s>(.*?)</%s>' % (tag, tag), html, re.S)
    return m.group(1) if m else ""

def body_html(html):
    m = re.search(r'<body>(.*?)<script>', html, re.S)
    return m.group(1)

# ---------------------------------------------------------------- CSS scoping
# selectors hoisted once, globally, instead of being scoped to a panel
GLOBAL_SELECTORS = {"*", ":root", "html", ".bubble", ".b1", ".b2", ".b3", ".b4"}

def split_rules(css):
    """Yield (kind, header, block) walking top level only. kind: 'at' | 'rule'."""
    out, i, n = [], 0, len(css)
    while i < n:
        # skip whitespace / comments
        m = re.match(r'\s+', css[i:])
        if m: i += m.end(); continue
        if css.startswith("/*", i):
            j = css.find("*/", i); i = (j + 2) if j != -1 else n; continue
        brace = css.find("{", i)
        if brace == -1: break
        header = css[i:brace].strip()
        depth, j = 1, brace + 1
        while j < n and depth:
            if css[j] == "{": depth += 1
            elif css[j] == "}": depth -= 1
            j += 1
        block = css[brace + 1:j - 1]
        out.append(("at" if header.startswith("@") else "rule", header, block))
        i = j
    return out

def scope_selector(sel, root):
    sel = sel.strip()
    if not sel: return sel
    if sel in GLOBAL_SELECTORS: return sel
    # `body.hideopt .ch.tier3` -> keep the body hook, scope the descendant part
    m = re.match(r'^body([.#][\w-]+)?(\s+(.*))?$', sel)
    if m:
        bodypart = "body" + (m.group(1) or "")
        rest = m.group(3)
        return f"{bodypart} {root} {rest}" if rest else root
    return f"{root} {sel}"

def scope_css(css, root, seen_globals):
    out = []
    for kind, header, block in split_rules(css):
        if kind == "at":
            h = header.lower()
            if h.startswith("@keyframes") or h.startswith("@font-face"):
                if header in seen_globals: continue
                seen_globals.add(header)
                out.append(f"{header}{{{block}}}")
            elif h.startswith("@media"):
                inner = []
                for k2, h2, b2 in split_rules(block):
                    if k2 == "at":
                        inner.append(f"{h2}{{{b2}}}")
                    else:
                        sels = ",".join(scope_selector(s, root) for s in h2.split(","))
                        inner.append(f"{sels}{{{b2}}}")
                out.append(f"{header}{{{''.join(inner)}}}")
            else:
                out.append(f"{header}{{{block}}}")
            continue
        sels = [s.strip() for s in header.split(",") if s.strip()]
        # hoist shared chrome (:root vars, reset, bubbles) once only
        if all(s in GLOBAL_SELECTORS for s in sels):
            key = header.strip()
            if key in seen_globals: continue
            seen_globals.add(key)
            out.append(f"{header}{{{block}}}")
            continue
        if sels == ["body"]:
            if "body" in seen_globals:
                out.append(f"{root}{{{block}}}")     # later body rules style the panel
            else:
                seen_globals.add("body")
                out.append(f"body{{{block}}}")
            continue
        out.append(",".join(scope_selector(s, root) for s in sels) + "{" + block + "}")
    return "\n".join(out)

# ------------------------------------------------------------- id namespacing
def prefix_ids_html(html, pfx):
    return re.sub(r'\bid="([\w-]+)"', lambda m: f'id="{pfx}-{m.group(1)}"', html)

def prefix_ids_js(js, pfx):
    # DOM lookups become prefix-aware helpers defined in the IIFE preamble
    js = js.replace("document.getElementById(", "byId(")
    js = js.replace("document.querySelectorAll(", "qsa(")
    js = js.replace("document.querySelector(", "qs(")
    # ids baked into generated markup
    js = re.sub(r'id="(ch|sum|sumarc)-\'', lambda m: f'id="{pfx}-{m.group(1)}-\'', js)
    return js

PREAMBLE = '''
/* ---- scoped DOM helpers (injected by tools/build_single_file.py) ---- */
const PFX = "%s-";
const ROOT = document.getElementById("app-%s");
const byId = x => document.getElementById(PFX + x);
const qs  = s => ROOT.querySelector(fixSel(s));
const qsa = s => ROOT.querySelectorAll(fixSel(s));
function fixSel(s){ return String(s).replace(/#([A-Za-z][\\w-]*)/g, (m,n)=>"#"+PFX+n); }
'''

def build():
    styles, bodies, scripts = [], [], []
    seen_globals = set()
    for app in APPS:
        raw = open(os.path.join(SRC, app["file"]), encoding="utf-8").read()
        root = f'#app-{app["key"]}'
        styles.append(f'/* ===== {app["file"]} ===== */\n'
                      + scope_css(part(raw, "style"), root, seen_globals))

        b = body_html(raw)
        b = re.sub(r'<div class="bubble[^>]*></div>', "", b)   # bubbles live in the shell
        # cross-file links become hash routes
        b = b.replace('Works offline &middot; each protocol is its own file &middot; progress saved in this browser',
                      'Works offline &middot; mobile build &middot; progress saved in this browser &mdash; back it up from a subject page')
        b = b.replace('href="index.html"', 'href="#/"')
        for a2 in APPS:
            if a2["route"] != "/":
                b = b.replace('href="%s"' % a2["file"], 'href="#%s"' % a2["route"])
        b = prefix_ids_html(b, app["pfx"])
        bodies.append((app, b))

        js = part(raw, "script")
        js = prefix_ids_js(js, app["pfx"])
        js = patch_app(app, js)
        scripts.append(
            f'/* ================= {app["file"]} ================= */\n'
            f'(function(){{\n{PREAMBLE % (app["pfx"], app["key"])}\n{js}\n}})();'
        )
    return styles, bodies, scripts

# ------------------------------------------------- per-app behavioural patches
def patch_app(app, js):
    key = app["key"]
    if key == "home":
        # posters navigate by hash instead of loading another file
        js = js.replace('if(h && h.file) window.location.href = h.file;',
                        'if(h && h.file) location.hash = ROUTE_OF[h.file] || "#/";')
        js = js.replace("""    actions.innerHTML = '<a class="btn btn-go" href="' + h.file + '">' +""",
                        """    actions.innerHTML = '<a class="btn btn-go" href="' + (ROUTE_OF[h.file]||"#/") + '">' +""")
        js = js.replace('document.getElementById("contGo").href = h.file;',
                        'byId("contGo").href = ROUTE_OF[h.file] || "#/";')
        js = js.replace('byId("contGo").href = h.file;',
                        'byId("contGo").href = ROUTE_OF[h.file] || "#/";')
        js = js.replace('e.target.closest("#mClose")', 'e.target.closest("#hm-mClose")')
        js = ("const ROUTE_OF=%s;\n" % json.dumps(
                  {a["file"]: "#" + a["route"] for a in APPS if a["route"] != "/"})) + js
        # the shell drives (re)paint when this panel is shown
        js += '\nwindow.__COMICS.home = async function(){ await loadProgress(); buildShelf(); paintHUD(); paintContinue(); };\n'
    if key == "xmen" or app.get("shelf"):
        js = re.sub(
            r'const blob=new Blob\(\[(JSON\.stringify\(\{.*?\},null,1\))\],\{type:"application/json"\}\);\s*'
            r'const a=document\.createElement\("a"\);\s*'
            r'a\.href=URL\.createObjectURL\(blob\);\s*'
            r'a\.download="([^"]+)";\s*'
            r'document\.body\.appendChild\(a\); a\.click\(\); a\.remove\(\);\s*'
            r'setTimeout\(\(\)=>URL\.revokeObjectURL\(a\.href\),2000\);',
            lambda m: 'window.__COMICS_SAVE("%s", %s);' % (m.group(2), m.group(1)),
            js, flags=re.S)
    if key == "xmen":
        # api.anthropic.com is blocked by the artifact CSP -> force the existing
        # "no key" path, which already points the reader at the offline arc digests.
        js = js.replace('function getKey(){ try{ return localStorage.getItem("xmen-anthropic-key")||""; }catch(e){ return ""; } }',
                        'function getKey(){ return ""; }  /* bundled build: live per-issue summaries are CSP-blocked */')
        js = js.replace(
          "msg='Per-issue summaries need an Anthropic API key when this file runs outside Claude. '+\n"
          "        'Paste one into the key box at the top and it will be saved on this device. '+\n"
          "        'Every arc-level digest already works with no key and no connection \\u2014 use <b>Summarize this arc</b>.';",
          "msg='Live per-issue summaries are turned off in the mobile build \\u2014 this page cannot reach the API. '+\n"
          "        'All 27 arc digests are written into the page and work offline: use <b>Summarize this arc</b>. '+\n"
          "        'For per-issue summaries, open the desktop copy of the tracker.';")
        # the API-key box is dead weight in this build - hide the whole row
        js += ('\n/* bundled build: no key box, since the key can never be used here */\n'
               'try{ var _sr=qs(".setup .setup-row"); if(_sr) _sr.style.display="none"; }catch(e){}\n')
        js += '\nwindow.__COMICS.xmen = function(){ refresh(); };\n'
    if app.get("shelf"):
        # every shelf page routes on its own hash prefix, e.g. #/hulk/omni/imm-o1
        slug = app["route"].strip("/")
        js = js.replace('const h=location.hash.replace(/^#\\/?/,"");',
                        'const h=location.hash.replace(/^#\\/?/,"").replace(/^%s\\/?/,"");' % slug)
        js = js.replace('location.hash="#/omni/"+c.dataset.omni;',
                        'location.hash="#/%s/omni/"+c.dataset.omni;' % slug)
        js = js.replace('byId("backShelf").onclick=()=>{ location.hash=""; };',
                        'byId("backShelf").onclick=()=>{ location.hash="#/%s"; };' % slug)
        js = js.replace('<a class="backlink" href="index.html">', '<a class="backlink" href="#/">')
        js += '\nwindow.__COMICS.%s = function(){ route(); };\n' % key
        js = inline_covers(js)
    return js


# ------------------------------------------------------------- cover inlining
# The shelf points `cover` at a file under Art/ -- fine over HTTP, but the
# artifact has no sibling files and its CSP blocks the request outright, so a
# relative src renders as a broken tile. Baking each cover in as a data URI is
# the only thing that works on all three surfaces at once.
#
# Cost: base64 is ~33% bigger than the file, and the artifact caps at 16MB.
# Run `python3 tools/covers.py audit` if this trips.
MIME = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png",
        ".webp": "image/webp", ".gif": "image/gif"}
ARTIFACT_LIMIT = 16 * 1024**2


def inline_covers(js):
    def repl(m):
        rel = m.group(1)
        path = os.path.join(SRC, rel)
        if not os.path.exists(path):
            raise SystemExit(
                "cover file missing: %s\n"
                "fix the `cover` path in tools/omnibus_meta.py, regenerate with\n"
                "  python3 tools/build_omnibus_data.py" % rel)
        mime = MIME.get(os.path.splitext(path)[1].lower())
        if not mime:
            raise SystemExit("unsupported cover format: %s" % rel)
        b64 = base64.b64encode(open(path, "rb").read()).decode("ascii")
        return '"cover": "data:%s;base64,%s"' % (mime, b64)

    js, n = re.subn(r'"cover": "((?!data:)[^"]+)"', repl, js)
    if n:
        print("  inlined %d cover image(s)" % n)
    return js


# ---------------------------------------------------------------- ascii output
# The Artifact wrapper owns <head>, so we cannot rely on a <meta charset>.
# Emitting pure ASCII makes the page immune to charset guessing entirely
# (en-dashes, arrows and middot were rendering as mojibake without this).
def ascii_html(s):
    return re.sub(r'[^\x00-\x7F]', lambda m: '&#%d;' % ord(m.group()), s)

def ascii_js(s):
    return re.sub(r'[^\x00-\x7F]', lambda m: '\\u%04x' % ord(m.group()), s)

def ascii_css(s):
    return re.sub(r'[^\x00-\x7F]', lambda m: '\\%04x ' % ord(m.group()), s)

SHELL_CSS = """
/* ---- shell ---- */
.cb-panel{display:none;}
.cb-panel.on{display:block;}
"""

SHELL_JS = """
/* ---- saving a backup ----
   In the published artifact a plain <a download> is inert: the viewer must
   mediate the save via the downloads capability. Locally there is no
   window.claude, so the ordinary link is used. Clipboard is the last resort so
   progress can always be got out of the page somehow. */
window.__COMICS_SAVE = async function(filename, text){
  const inArtifact = (typeof window.claude !== "undefined" && typeof window.claude.use === "function");
  if(inArtifact){
    let dl = null;
    try{ dl = await window.claude.use("downloads"); }catch(e){}
    if(dl){
      try{ await dl.save({filename: filename, data: text}); return true; }
      catch(err){
        if(err && err.code === "declined") return false;   /* viewer said no - never retry */
        console.warn("downloads.save failed:", err && err.code);
      }
    }
    try{
      await navigator.clipboard.writeText(text);
      alert("This view can't save files directly, so your progress JSON was copied to the clipboard instead.\\n\\nPaste it into a note or file to keep it.");
      return true;
    }catch(e){
      alert("Couldn't save or copy automatically. Open this page on desktop to back up.");
      return false;
    }
  }
  try{
    const blob = new Blob([text], {type:"application/json"});
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob); a.download = filename;
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(()=>URL.revokeObjectURL(a.href), 2000);
    return true;
  }catch(e){ return false; }
};

/* ================= shell router ================= */
(function(){
  function show(which){
    __PANELS.forEach(k=>{
      document.getElementById("app-"+k).classList.toggle("on",k===which);
    });
    const fn=window.__COMICS[which];
    if(fn) try{ fn(); }catch(e){ console.error("panel init failed:",which,e); }
    window.scrollTo(0,0);
  }
  function route(){
    const h=location.hash.replace(/^#\/?/,"");
    const hit=__ROUTES.find(r=>h.startsWith(r.p));
    show(hit?hit.k:"home");
  }
  window.addEventListener("hashchange",route);
  route();
})();
"""

def emit():
    styles, bodies, scripts = build()
    panels = []
    for app, b in bodies:
        panels.append(f'<div class="cb-panel" id="app-{app["key"]}">{b}</div>')
    html = []
    html.append('<title>C.O.M.I.C.S.</title>')
    html.append("<style>\n" + ascii_css("\n".join(styles) + "\n" + SHELL_CSS) + "\n</style>")
    html.append('<div class="bubble b1"></div><div class="bubble b2"></div>'
                '<div class="bubble b3"></div><div class="bubble b4"></div>')
    html += [ascii_html(p) for p in panels]
    # longest prefix first, so "/spider-man" is not shadowed by a shorter route
    routes = sorted(((a["route"].strip("/"), a["key"]) for a in APPS if a["route"] != "/"),
                    key=lambda r: -len(r[0]))
    routes_js = ("const __PANELS=%s;\nconst __ROUTES=%s;\n"
                 % (json.dumps([a["key"] for a in APPS]),
                    json.dumps([{"p": p_, "k": k} for p_, k in routes])))
    html.append("<script>\nwindow.__COMICS={};\n"
                + ascii_js("\n".join(scripts) + "\n" + routes_js + SHELL_JS) + "\n</script>")
    doc = "\n".join(html)
    non = [c for c in doc if ord(c) > 127]
    assert not non, f"non-ascii survived: {set(non)}"
    return doc

if __name__ == "__main__":
    out = os.path.join(SRC, "comics-mobile.html")
    html = emit()
    if len(html) > ARTIFACT_LIMIT:
        sys.exit(f"{len(html)/1e6:.1f} MB exceeds the {ARTIFACT_LIMIT/1e6:.0f} MB artifact "
                 f"limit.\nShrink the covers: python3 tools/covers.py audit")
    open(out, "w", encoding="utf-8").write(html)
    print(f"wrote {out}  ({len(html):,} bytes, {len(html)/1e6:.1f} MB)")
