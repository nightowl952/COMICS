# The hand-written half of the Silver Surfer shelf. Same shape as
# omnibus_meta.py, hulk_meta.py, ff_meta.py, wolverine_meta.py,
# moonknight_meta.py and daredevil_meta.py -- ORDER (wiki-backed), PLACEHOLDERS
# (tiles with no contents), SHELF (display order by id), PLACEHOLDER_PAGES, and
# SERIES_EXTRA for the series the shared SERIES table in build_omnibus_data.py
# does not already carry.
#
# Scope: the Surfer's own books, which here is every Silver Surfer omnibus
# Marvel has actually printed. The Marvel Database lists exactly four and there
# was no judgement call to make on three of them -- like Moon Knight, there is
# no family character to rule out and no team book to argue about, so the only
# question was the release rule.
#
# All four are on the shelf, including Silver Surfer: The Infinity Gauntlet
# Omnibus, which does not ship until 3 NOVEMBER 2026. That is allowed under the
# amended rule -- see "A shelf holds books whose tile is finished" in CLAUDE.md
# -- because all three things a tile needs are real: the wiki carries its full
# ReprintOf contents, all 46 issues resolve to marvel.com, and the jacket exists
# as flat cover art. Its tile carries a "Ships Nov 2026" badge that retires
# itself in November without an edit.
#
# The one thing the wiki does NOT have is that jacket: the page declares
# Image1/Image2 and both are redlinks, so fetch_covers.py picks up Infinity
# Gauntlet #2's cover out of the reprint gallery instead. The cover here was
# added by hand with `covers.py add`. When refetching this shelf do NOT pass
# --all, or it will overwrite gauntlet-o1 with that wrong image.
#
# No volume needs `chapterby`: all three score well over the 3.5 average-run-
# length threshold, so the automatic per-series chaptering is right on each.

ORDER = [
("Silver Surfer Omnibus Vol 1 1", dict(id="ss-o1", title="Silver Surfer Omnibus", vol="",
  creators="Stan Lee & John Buscema", era="1967–1970", released="May 2007",
  art="o-chrome", tex="tex-starfield", spine="Silver Surfer",
 cover="Art/Silver-Surfer/ss-o1.jpg",
  note="The Lee and Buscema book, and still the one the character is measured against. Eighteen issues of Galactus's herald marooned inside a barrier over Earth, being magnificent about it and miserable about it in the same panel. It opens with the Fantastic Four Annual where he first got a story of his own, and closes on the Not Brand Echh parody, which is what happened to anything Marvel took seriously in 1969.")),
("Silver Surfer: Return to the Spaceways Omnibus Vol 1 1", dict(id="spaceways-o1", title="Silver Surfer: Return to the Spaceways Omnibus", vol="",
  creators="Steve Englehart, Marshall Rogers & Ron Lim", era="1980–1990", released="May 2025",
  art="o-cosmic", tex="tex-cosmic", spine="Return to Spaceways",
 cover="Art/Silver-Surfer/spaceways-o1.jpg",
  note="The barrier breaks and he goes back to the stars. A Stan Lee and John Byrne one-shot in 1982, then Englehart and Rogers relaunch him in 1987 for thirty-three issues — the Kree/Skrull war restarted, the Elders of the Universe hunting Galactus, Nova and Mantis and Shalla-Bal. The tail of the book is the odd material: both of Stan Lee's graphic novels, Moebius drawing Parable, Epic Illustrated #1 and the first Marvel Comics Presents. Note the jump to get here — he had no title at all between 1970 and 1982.")),
("Silver Surfer by Slott & Allred Omnibus Vol 1 1", dict(id="slott-o1", title="Silver Surfer by Slott & Allred Omnibus", vol="",
  creators="Dan Slott & Michael Allred", era="2014–2017", released="Dec 2018",
  art="o-dawn", tex="tex-popdot", spine="By Slott & Allred",
 cover="Art/Silver-Surfer/slott-o1.jpg",
  note="Doctor Who with a surfboard, and it works. Dawn Greenwood gets in the way of the most humourless character Marvel has and Allred draws the result in pop primaries. Both series here, #1–15 and #1–14, plus the Point One prologue. Mind the jump: Silver Surfer (1987) #67–146, the 2003 Straczynski series and the 2011 mini sit in front of this book and none of them has an omnibus. The book before this one closes the first third of that hole.")),
("Silver Surfer: The Infinity Gauntlet Omnibus Vol 1 1", dict(id="gauntlet-o1", title="Silver Surfer: The Infinity Gauntlet Omnibus", vol="",
  creators="Jim Starlin, Ron Marz & Ron Lim", era="1990–1992", released="Nov 2026",
  art="o-gauntlet", tex="tex-cosmic", spine="Infinity Gauntlet",
 cover="Art/Silver-Surfer/gauntlet-o1.jpg",
  note="Ships 3 November 2026 \u2014 it is on the shelf ahead of that because its contents, its links and its jacket are all real, which is the bar a tile has to clear. Starlin takes the book over at #34 and it stops being a story about the Surfer's conscience and becomes a story about Thanos. The Thanos Quest collects the six stones, Infinity Gauntlet spends them, and the Surfer's own title runs alongside the whole thing to #66 \u2014 which is the argument for reading the crossover here, in his book, rather than on its own. Note this is not the 2014 Infinity Gauntlet Omnibus: that one is the event edition, with the Hulk, Doctor Strange and Quasar tie-ins and no annuals.")),
]

# Nothing pending on this shelf.
PLACEHOLDERS = []

# Display order of the shelf, by id. A reading order, which on this shelf is
# also publication order -- four books running 1967 to 2017, with the
# uncollected 1990s and 2000s sitting between the last two (see slott-o1's
# note). Nothing to resequence.
SHELF = [
  "ss-o1", "spaceways-o1", "gauntlet-o1", "slott-o1",
]

PLACEHOLDER_PAGES = {}

# Series these books collect that the shared SERIES table in
# build_omnibus_data.py does not carry. Display names are the marvel.com form
# (name plus start year) rather than the wiki's volume number, because that is
# what link_issues.py matches on -- the catalog carries seven series simply
# called "Silver Surfer" (1968, 1982, 1987, 2003, 2011, 2014, 2016), which is
# exactly the reused-title case its tiebreak() exists for.
#
# "Silver Surfer Vol 4" is not a fourth ongoing: it is the two-issue Stan Lee
# and Moebius Parable from Epic, which the wiki files under the main title and
# marvel.com files under its own.
#
# `ss` was already taken by Scarlet Spider on the Spider-Man shelf, hence the
# `ssf` stem throughout -- the id store is shared and keyed by code.
SERIES_EXTRA = {
 "Silver Surfer Vol 1":                                ("ssf",    "Silver Surfer (1968)"),
 "Silver Surfer Vol 2":                                ("ssf2",   "Silver Surfer (1982)"),
 "Silver Surfer Vol 3":                                ("ssf3",   "Silver Surfer (1987)"),
 "Silver Surfer Vol 4":                                ("ssfpar", "Silver Surfer: Parable"),
 "Silver Surfer Vol 7":                                ("ssf7",   "Silver Surfer (2014)"),
 "Silver Surfer Vol 8":                                ("ssf8",   "Silver Surfer (2016)"),
 "Silver Surfer Annual Vol 1":                         ("ssfann", "Silver Surfer Annual (1988)"),
 "Super-Villain Classics Vol 1":                       ("svc",    "Super-Villain Classics"),
 "All-New Marvel NOW! Point One Vol 1":                ("anmpo",  "All-New Marvel NOW! Point One"),
 "Infinity Gauntlet Vol 1":                            ("infg",   "Infinity Gauntlet (1991)"),
 "Thanos Quest Vol 1":                                 ("tquest", "Thanos Quest"),
}

# Reused verbatim from the other shelves' own SERIES_EXTRA. A hero only ever
# sees the shared SERIES table plus its OWN extras, so a series another shelf
# already carries has to be repeated here -- with exactly the same short code,
# because the marvel.com id store is shared and the same series must key the
# same way on every shelf. (autocode() would reuse them anyway; these are
# written out so the codes are readable next to the ones they sit beside.)
SERIES_EXTRA.update({
 "Marvel Graphic Novel Vol 1":                         ("mgn",    "Marvel Graphic Novel"),
 "Epic Illustrated Vol 1":                             ("epic",   "Epic Illustrated"),
 "Marvel Fanfare Vol 1":                               ("mfan",   "Marvel Fanfare"),
})
