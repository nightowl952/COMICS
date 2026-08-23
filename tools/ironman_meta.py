# The hand-written half of the Iron Man shelf. Same shape as omnibus_meta.py,
# hulk_meta.py, ff_meta.py, wolverine_meta.py, moonknight_meta.py,
# daredevil_meta.py, silversurfer_meta.py and captainamerica_meta.py -- ORDER
# (wiki-backed), PLACEHOLDERS (tiles with no contents), SHELF (display order by
# id), PLACEHOLDER_PAGES, and SERIES_EXTRA for the series the shared SERIES
# table in build_omnibus_data.py does not already carry.
#
# Scope: Tony Stark's own book, which here is every Iron Man omnibus Marvel has
# printed. The Marvel Database lists exactly nine and all nine are on the shelf.
# Like Moon Knight and Silver Surfer there was no judgement call to make --
# there is no family character with an omnibus to rule out (War Machine,
# Ironheart and Superior Iron Man have none), no team book to argue about, and
# nothing unreleased: the most recent volume shipped in May 2026.
#
# What is NOT here is not a scope call either, it is an absence. The runs
# people ask for -- Fraction and Larroca, Ellis's Extremis, Duggan -- have no
# omnibus at all, only hardcovers and Complete Collection paperbacks. Searching
# the storyline as well as the character (the Captain America lesson) turned up
# nothing the prefix sweep had missed.
#
# TWO COVERS ARE NOT THE WIKI'S FIRST ANSWER, and `fetch_covers.py` will put
# the wrong ones back. Do NOT run `fetch_covers.py --hero iron-man --all`.
#
#   iim-o1  The page declares Image1 = "Invincible Iron Man Omnibus Vol 1 1.jpg"
#           with Image1_ReprintOf = "Tales of Suspense Vol 1 39.jpg", and the
#           file under the omnibus's own name is itself a scan of Tales of
#           Suspense #39 -- price box, Comics Code stamp and all. prop=pageimages
#           hands that back and it looks like a clean fetch. The jacket actually
#           on the shelf is the PAREL VARIANT (600x901), which is the only file
#           on the page carrying omnibus trade dress ("OMNIBUS", and Lee / Heck /
#           Colan along the foot). Added by hand with `covers.py add`.
#
#   iim-o2  The page declares Image1 = "Iron Man Vol 1 1.jpg" outright -- the
#           wiki has no jacket scan for this book at all. It is left as fetched,
#           because three independent sources (that file, the Larroca variant,
#           and Amazon's image keyed to the book's own ISBN 978-0785142249) all
#           show the same Iron Man #1 artwork: the printed jacket for this
#           volume really does reproduce the 1968 cover, trade dress included.
#           So the art is right for the book even though the scan is an issue.
#
# Both flat-jacket-by-ISBN endpoints CLAUDE.md lists were tried for these two
# and neither helps: Penguin Random House returns a "Cover Coming Soon"
# placeholder for both ISBNs.

# Only busiek-o1 carries `chapterby`: it scores 3.27 on the average-run-length
# test, just under the 3.5 threshold, because the Busiek run is followed by
# nine single crossover issues. Those nine are each a named book from "The
# Eighth Day", so one chapter per book reads far better than "Part N" -- the
# same call the Hulk anthologies take.

ORDER = [
("Invincible Iron Man Omnibus Vol 1 1", dict(id="iim-o1", title="Invincible Iron Man Omnibus", vol="Vol. 1",
  creators="Stan Lee, Don Heck & Gene Colan", era="1963–1966", released="May 2008",
  art="o-gold", tex="tex-halftone", spine="Invincible Iron Man",
 cover="Art/Iron-Man/iim-o1.jpg",
  note="A weapons manufacturer is wounded by his own landmine, builds a suit of armour to keep his heart beating, and spends the next sixty years failing to put it down. Tales of Suspense #39 is the origin; the grey armour is gold by #40 and red-and-gold by #48, which is Marvel deciding what the character looks like in real time. Heck, Ditko and then Colan draw it, the Mandarin and the Crimson Dynamo turn up, and the Tales to Astonish at the end is the Sub-Mariner crossover.")),
("Invincible Iron Man Omnibus Vol 1 2", dict(id="iim-o2", title="Invincible Iron Man Omnibus", vol="Vol. 2",
  creators="Stan Lee, Archie Goodwin & Gene Colan", era="1966–1970", released="May 2010",
  art="o-crimson", tex="tex-halftone", spine="Invincible Iron Man",
 cover="Art/Iron-Man/iim-o2.jpg",
  note="The back half of Tales of Suspense, then his own title at last. Iron Man and Sub-Mariner #1 is the hinge — a one-shot in April 1968 that exists purely because the shared book was splitting in two, and it sits here between Tales of Suspense #99 and Iron Man #1, which is where it was published and where it reads. Archie Goodwin takes over and brings Madame Masque and Whiplash with him.")),
("Invincible Iron Man Omnibus Vol 1 3", dict(id="iim-o3", title="Invincible Iron Man Omnibus", vol="Vol. 3",
  creators="Archie Goodwin, Gerry Conway & George Tuska", era="1970–1974", released="Aug 2024",
  art="o-crimson", tex="tex-repulsor", spine="Invincible Iron Man",
 cover="Art/Iron-Man/iim-o3.jpg",
  note="Fourteen years after the volume before it, which is Marvel finally finishing a numbered run. Goodwin closes out, Conway and Tuska take over, and Iron Man #55 quietly introduces Thanos, Drax and Moondragon in a single issue — the most consequential twenty pages on this shelf by some distance. The Daredevil at the end is the other half of a crossover.")),
("Invincible Iron Man Omnibus Vol 1 4", dict(id="iim-o4", title="Invincible Iron Man Omnibus", vol="Vol. 4",
  creators="Mike Friedrich, Bill Mantlo & George Tuska", era="1974–1978", released="May 2026",
  art="o-gold", tex="tex-plate", spine="Invincible Iron Man",
 cover="Art/Iron-Man/iim-o4.jpg",
  note="The stretch nobody quotes and most people have not read. Friedrich and then Bill Mantlo run the book for four years, rebuild the armour, bring back Madame Masque and thread Jack of Hearts through the drama; there are team-ups with Daredevil, Man-Thing and the Champions. It stops at #112, and Mantlo's #113–114 are collected nowhere at all — a two-issue hole before the next book opens at #115.")),
("Iron Man by Michelinie, Layton & Romita Jr. Omnibus Vol 1 1", dict(id="mlr-o1", title="Iron Man by Michelinie, Layton & Romita Jr. Omnibus", vol="",
  creators="David Michelinie, Bob Layton & John Romita Jr.", era="1978–1982", released="Feb 2013",
  art="o-bottle", tex="tex-halftone", spine="By Michelinie & Layton",
 cover="Art/Iron-Man/mlr-o1.jpg",
  note="The run that made Tony Stark a character rather than a suit. \"Demon in a Bottle\" is nine issues of him drinking himself out of his own company, and it is still the thing every later writer is answering; Doomquest drops him and Doctor Doom into Arthurian Britain, Justin Hammer arrives, and the space and stealth armours get built. Forty-three issues with no filler in them.")),
("Iron Man: Armor Wars Omnibus Vol 1 1", dict(id="armor-o1", title="Iron Man: Armor Wars Omnibus", vol="",
  creators="David Michelinie, Bob Layton & Mark Bright", era="1987–1991", released="Jan 2026",
  art="o-steel", tex="tex-plate", spine="Armor Wars",
 cover="Art/Iron-Man/armor-o1.jpg",
  note="Michelinie and Layton come back for the story with the best premise in the character: his technology has been stolen, it is inside half the armoured villains in the Marvel Universe, and he decides to go and take it back whether or not anyone has asked him to. Armor Wars is #219–232 and the sequel is #258–266; the twenty-five issues between them are not here because this is a storyline book, not a run. Mind the jump to get to it — #158–218 has never been collected in omnibus.")),
("Iron Man by Kurt Busiek & Sean Chen Omnibus Vol 1 1", dict(id="busiek-o1", title="Iron Man by Kurt Busiek & Sean Chen Omnibus", vol="",
  creators="Kurt Busiek & Sean Chen", era="1998–2000", released="Sep 2013",
  art="o-crimson", tex="tex-circuit", chapterby="series", spine="By Busiek & Chen",
 cover="Art/Iron-Man/busiek-o1.jpg",
  note="Heroes Return: the third Iron Man #1, and Busiek writing him as a man who is good at engineering and bad at everything else. The nine single issues after the run are \"The Eighth Day\" crossover, one chapter per book, and The Iron Age closes it. There is a long way to fall to get here — Iron Man #267–332 and the whole Heroes Reborn year sit in front of this book and none of it has an omnibus.")),
("Iron Man: The Mask in the Iron Man Omnibus Vol 1 1", dict(id="mask-o1", title="Iron Man: The Mask in the Iron Man Omnibus", vol="",
  creators="Joe Quesada, Frank Tieri & Sean Chen", era="2000–2002", released="Dec 2019",
  art="o-mask", tex="tex-circuit", spine="Mask in the Iron Man",
 cover="Art/Iron-Man/mask-o1.jpg",
  note="Quesada's answer to \"what if the armour woke up\": it becomes sentient, it is in love with him, and it is not going to take being switched off well. Tieri runs the back half into Sons of Yinsen. It picks up directly where the Busiek book stops, at #26, and runs to the end of the volume at #49 with both annuals and the Wizard mail-away half-issue.")),
("Tony Stark: Iron Man by Dan Slott Omnibus Vol 1 1", dict(id="tsim-o1", title="Tony Stark: Iron Man by Dan Slott Omnibus", vol="",
  creators="Dan Slott, Jim Zub & Valerio Schiti", era="2018–2020", released="Mar 2021",
  art="o-escape", tex="tex-circuit", spine="By Dan Slott",
 cover="Art/Iron-Man/tsim-o1.jpg",
  note="Slott builds the eScape, a virtual world nobody can prove they have left, and then asks Tony to work out whether he is a man or a very good copy of one. Iron Man 2020 hands the book to Arno Stark and a robot uprising. The Busiek issue printed at the back is not a mistake: Iron Man (1998) #25 is where Arno was set up, twenty years earlier, and the book reprints it so the ending lands. Another long jump to get here — everything between 2002 and 2018 is uncollected in omnibus.")),
]

# Nothing pending on this shelf.
PLACEHOLDERS = []

# Display order of the shelf, by id. A reading order, which on this shelf is
# also the order the material was published -- four numbered volumes carrying
# 1963 to 1978, then the creator books. Nothing needed resequencing.
SHELF = [
  "iim-o1", "iim-o2", "iim-o3", "iim-o4",
  "mlr-o1", "armor-o1", "busiek-o1", "mask-o1", "tsim-o1",
]

PLACEHOLDER_PAGES = {}

# Series these books collect that the shared SERIES table in
# build_omnibus_data.py does not carry. Display names are the marvel.com form
# (name plus start year) rather than the wiki's volume number, because that is
# what link_issues.py matches on -- the catalog carries several series simply
# called "Iron Man" (1968, 1996, 1998, 2005, 2012, 2020), which is exactly the
# reused-title case its tiebreak() exists for.
SERIES_EXTRA = {
 "Iron Man Vol 3":                                     ("im3",    "Iron Man (1998)"),
 "Iron Man Annual Vol 1":                              ("imann",  "Iron Man Annual (1970)"),
 "Iron Man and Sub-Mariner Vol 1":                     ("imsub",  "Iron Man and the Sub-Mariner (1968)"),
 "Iron Man & the Armor Wars Vol 1":                    ("imaw",   "Iron Man: The Armor Wars (2009)"),
 "Iron Man: The Iron Age Vol 1":                       ("imia",   "Iron Man: The Iron Age (1998)"),
 "Iron Man 2020 Vol 2":                                ("im2020", "Iron Man 2020 (2020)"),
 "Tony Stark: Iron Man Vol 1":                         ("tsim",   "Tony Stark: Iron Man (2018)"),
 "Avengers Vol 3":                                     ("av3",    "Avengers (1998)"),
 "Thor Vol 2":                                         ("thor2",  "Thor (1998)"),
 "Quicksilver Vol 1":                                  ("quick",  "Quicksilver (1997)"),
 "Juggernaut Vol 2":                                   ("jugg",   "Juggernaut (1999)"),
 "Peter Parker: Spider-Man Vol 1":                     ("ppsm",   "Peter Parker: Spider-Man (1999)"),
}

# Reused verbatim from the other shelves' own SERIES_EXTRA. A hero only ever
# sees the shared SERIES table plus its OWN extras, so a series another shelf
# already carries has to be repeated here -- with exactly the same short code,
# because the marvel.com id store is shared and the same series must key the
# same way on every shelf. `im` in particular is already owned by four shelves.
SERIES_EXTRA.update({
 "Iron Man Vol 1":                                     ("im",     "Iron Man (1968)"),
 "Tales of Suspense Vol 1":                            ("tos",    "Tales of Suspense"),
 "Tales to Astonish Vol 1":                            ("tta",    "Tales to Astonish"),
 "Captain America Vol 3":                              ("cap3",   "Captain America (1998)"),
 "Fantastic Four Vol 3":                               ("ff3",    "Fantastic Four (1998)"),
 "Iron Man & Captain America Annual Vol 1":            ("imcaann","Iron Man & Captain America Annual"),
})
