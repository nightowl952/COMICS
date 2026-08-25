#!/usr/bin/env python3
"""Build the compact, deterministic knowledge index used by Ask AI.

The generated file contains shelf facts and the conclusions already written in
the guided tours. It deliberately excludes full tour prose; Claude can request
one complete tour through the client-side ``read_tour`` tool when it needs the
extra depth.

    python3 tools/build_ask_index.py
    python3 tools/build_ask_index.py --check
"""

from html import unescape
import importlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "ask-index.json")
CONTEXT_OUT = os.path.join(ROOT, "ask-context.txt")
TOURS_OUT = os.path.join(ROOT, "ask-tours")

sys.path.insert(0, HERE)
import heroes  # noqa: E402
import build_omnibus_data  # noqa: E402


def plain(value):
    """Turn the tours' small amount of presentational HTML into prompt text."""
    if not isinstance(value, str):
        return value
    value = re.sub(r"<br\s*/?>", "\n", value, flags=re.I)
    value = re.sub(r"<[^>]+>", "", value)
    return unescape(value).strip()


def tour_for(key):
    return importlib.import_module("tours." + key.replace("-", "_")).TOUR


def distilled(tour, volume_id):
    record = (tour.get("volumes") or {}).get(volume_id) or {}
    verdict = record.get("verdict") or {}
    body = verdict.get("body") or []
    return {
        "lede": plain(record.get("lede", "")),
        "standing": plain(verdict.get("standing", "")),
        "standing_class": verdict.get("cls", ""),
        "verdict": plain(body[0]) if body else "",
    }


def generated_shelf(key, config):
    """Read the same metadata pipeline that writes the fourteen printed shelves."""
    build_omnibus_data.RAW = os.path.join(HERE, config["raw"])
    arr = build_omnibus_data.build_all(heroes.meta_module(heroes.resolve(key)))
    tour = tour_for(key)
    volumes = []
    for volume in arr:
        chapters = volume.get("chapters") or []
        item = {
            "id": volume["id"],
            "title": volume.get("title", ""),
            "volume": volume.get("vol", ""),
            "creators": volume.get("creators", ""),
            "era": volume.get("era", ""),
            "released": volume.get("released", ""),
            "note": plain(volume.get("note", "")),
            "issue_count": sum(len(ch.get("issues") or []) for ch in chapters),
            "chapters": [plain(ch.get("title", "")) for ch in chapters],
            "issues": [
                {"id": issue["id"], "title": plain(issue.get("t", "")), "chapter": plain(ch.get("title", ""))}
                for ch in chapters for issue in (ch.get("issues") or [])
            ],
            "cover": volume.get("cover", ""),
            **distilled(tour, volume["id"]),
        }
        volumes.append(item)
    return shelf_record(key, config["name"], config["tracker"], tour, volumes)


def balanced_objects(source):
    """Yield top-level JS object literals without evaluating page JavaScript."""
    depth = 0
    start = None
    quote = None
    escaped = False
    for i, char in enumerate(source):
        if quote:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = None
            continue
        if char in "\"'`":
            quote = char
        elif char == "{":
            if depth == 0:
                start = i
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0 and start is not None:
                yield source[start:i + 1]
                start = None


def js_string(block, field):
    match = re.search(r"\b%s\s*:\s*([\"'])(.*?)\1" % re.escape(field), block, re.S)
    if not match:
        return ""
    # The hand-written shelf uses JSON-compatible escapes inside its strings.
    return json.loads('"' + match.group(2).replace('"', '\\"') + '"')


def js_unescape(value):
    return json.loads('"' + value.replace('"', '\\"') + '"')


def xmen_shelf():
    """Extract the hand-written X-Men shelf rather than duplicating it in Python."""
    path = os.path.join(ROOT, "xmen-reading-tracker.html")
    html = open(path, encoding="utf-8").read()
    start = html.index("const OMNI = [") + len("const OMNI = [")
    end = html.index("\n];", start)
    tour = tour_for("xmen")
    known_counts = {"xm-o1": 38, "xm-o2": 49, "xm-o3": 42, "xm-o4": 45}
    volumes = []
    for block in balanced_objects(html[start:end]):
        volume_id = js_string(block, "id")
        if not volume_id.startswith("xm-o"):
            continue
        chapter_titles = re.findall(r"\{\s*id\s*:\s*[\"']c-[^\"']+[\"']\s*,\s*title\s*:\s*[\"']([^\"']+)", block)
        issues = [
            {"id": match[0], "title": js_unescape(match[1]), "chapter": ""}
            for match in re.findall(r"\{\s*id:\"([^\"]+)\",\s*t:\"([^\"]+)\"", block)
        ]
        for title, first, last, prefix in re.findall(r'seq\("([^"]+)",(\d+),(\d+),"([^"]+)"', block):
            issues.extend({"id": "%s-%d" % (prefix, number), "title": "%s #%d" % (title, number), "chapter": ""}
                          for number in range(int(first), int(last) + 1))
        issues = list({issue["id"]: issue for issue in issues}.values())
        volumes.append({
            "id": volume_id,
            "title": js_string(block, "title"),
            "volume": js_string(block, "vol"),
            "creators": js_string(block, "creators"),
            "era": js_string(block, "era"),
            "released": "Never printed",
            "note": plain(js_string(block, "note")),
            "issue_count": known_counts[volume_id],
            "chapters": [plain(js_unescape(t)) for t in chapter_titles],
            "issues": issues,
            "cover": js_string(block, "cover"),
            **distilled(tour, volume_id),
        })
    if len(volumes) != 4:
        raise SystemExit("expected four X-Men shelf volumes, found %d" % len(volumes))
    return shelf_record("xmen", "X-Men", "xmen-reading-tracker.html", tour, volumes)


def shelf_record(key, name, tracker, tour, volumes):
    tone = ((tour.get("overview") or {}).get("tone") or {})
    modes = []
    for mode in tone.get("modes") or []:
        modes.append({
            "label": plain(mode.get("l", "")),
            "description": plain(mode.get("b", "")),
            "volume_ids": mode.get("vols") or [],
        })
    return {
        "id": key,
        "name": name,
        "tracker": tracker,
        "tone_modes": modes,
        "volumes": volumes,
    }


def build():
    shelves = [generated_shelf(key, config) for key, config in heroes.HEROES.items()]
    shelves.append(xmen_shelf())
    return {
        "schema_version": 1,
        "purpose": "Ground Ask AI answers in the volumes actually present on the C.O.M.I.C.S. shelves.",
        "rules": [
            "Recommend shelf volumes by exact shelf id only.",
            "Reception fields report reader and critical consensus, not objective fact.",
            "Full guided tours are available on demand through read_tour(hero_id).",
            "C.O.M.I.C.S. contains cover images, not interior comic pages.",
        ],
        "shelves": shelves,
    }


def prompt_context(data):
    """Render the same knowledge as token-friendly text instead of repeated JSON keys."""
    lines = ["C.O.M.I.C.S. SHELF INDEX", "Recommend only exact shelf and volume ids listed here."]
    for shelf in data["shelves"]:
        lines.extend(("", "SHELF %s | %s" % (shelf["id"], shelf["name"])))
        for mode in shelf["tone_modes"]:
            lines.append("TONE %s | %s | volumes %s" % (
                mode["label"], mode["description"], ",".join(mode["volume_ids"])))
        for volume in shelf["volumes"]:
            lines.append("VOLUME %s | %s%s | %s | %s | %d issues" % (
                volume["id"], volume["title"],
                (" " + volume["volume"]) if volume["volume"] else "",
                volume["creators"], volume["era"], volume["issue_count"]))
            lines.append("ABOUT " + volume["note"])
            lines.append("CHAPTERS " + " ; ".join(volume["chapters"]))
    return "\n".join(lines) + "\n"


def main():
    check = "--check" in sys.argv[1:]
    data = build()
    rendered = json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n"
    context_rendered = prompt_context(data)
    current = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else None
    context_current = open(CONTEXT_OUT, encoding="utf-8").read() if os.path.exists(CONTEXT_OUT) else None
    tours = {key: tour_for(key) for key in heroes.HEROES}
    tours["xmen"] = tour_for("xmen")
    tour_rendered = {
        key: json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n"
        for key, value in tours.items()
    }
    tours_current = {
        key: (open(os.path.join(TOURS_OUT, key + ".json"), encoding="utf-8").read()
              if os.path.exists(os.path.join(TOURS_OUT, key + ".json")) else None)
        for key in tours
    }
    if check:
        if current != rendered or context_current != context_rendered or tours_current != tour_rendered:
            print("ask-index.json is out of date; run tools/build_ask_index.py")
            return 1
        print("ask-index.json is in sync")
        return 0
    if current == rendered:
        print("ask-index.json already up to date")
    else:
        with open(OUT, "w", encoding="utf-8") as handle:
            handle.write(rendered)
        print("wrote ask-index.json")
    if context_current != context_rendered:
        with open(CONTEXT_OUT, "w", encoding="utf-8") as handle:
            handle.write(context_rendered)
        print("wrote ask-context.txt")
    os.makedirs(TOURS_OUT, exist_ok=True)
    for key, value in tour_rendered.items():
        path = os.path.join(TOURS_OUT, key + ".json")
        if tours_current[key] != value:
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(value)
    volumes = sum(len(s["volumes"]) for s in data["shelves"])
    print("%d shelves | %d volumes | %d JSON bytes | %d prompt bytes" % (
        len(data["shelves"]), volumes, len(rendered.encode("utf-8")), len(context_rendered.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
