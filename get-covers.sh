#!/usr/bin/env bash
# Fetch the omnibus cover art and rebuild everything. Run from this folder:
#     ./get-covers.sh
# Needs internet. Safe to re-run -- it skips volumes it already has.
set -e
cd "$(dirname "$0")"
echo "==> fetching covers + metadata (a few minutes; it pauses to be polite)"
python3 tools/scrape_covers.py
echo "==> baking them into the trackers"
python3 tools/build_omnibus_data.py
python3 tools/build_single_file.py
echo
echo "Done. Open spiderman-reading-tracker.html to look."
echo "To publish: git add -A && git commit -m 'Add omnibus covers' && git push"
