# The hand-written half of the Wolverine shelf. Same shape as omnibus_meta.py,
# hulk_meta.py and ff_meta.py -- ORDER (wiki-backed), PLACEHOLDERS (tiles with
# no contents), SHELF (display order by id), PLACEHOLDER_PAGES, and
# SERIES_EXTRA for the series the shared SERIES table in build_omnibus_data.py
# does not already carry.
#
# Scope: Logan's own books. Off the shelf by the user's call: Weapon X: The
# Return (the Weapon X programme's ensemble book -- Wolverine is in 9 of its 53
# issues), Wolverine & the X-Men (an X-Men team book, the same call that
# dropped Marvel Team-Up from the Spider-Man shelf), and the two Laura Kinney
# books, All-New Wolverine and X-23 (a different character, the same call that
# keeps She-Hulk off the Hulk shelf).
#
# Off the shelf by the "a shelf holds books you can actually buy" rule:
# Wolverine: Old Man Logan Omnibus (solicited December 2026) and Wolverine: The
# Return of Weapon X Omnibus (solicited June 2027). Both keep their entries in
# wolverine_contents_raw.json, so re-adding either when it ships is an edit
# here plus a regenerate rather than a fresh wiki pull.
#
# `chapterby` overrides the automatic chaptering heuristic on three volumes.

ORDER = [
("Wolverine Omnibus Vol 1 1", dict(id="wolv-o1", title="Wolverine Omnibus", vol="Vol. 1",
  creators="Chris Claremont, Frank Miller & Barry Windsor-Smith", era="1974–1989", released="Apr 2009",
  art="o-claw", tex="tex-slash", spine="Wolverine",
 cover="Art/Wolverine/wolv-o1.jpg",
  note="Opens on Weapon X rather than on his first appearance — the book puts the origin first and then goes back to Incredible Hulk #180. Everything that made him: the Claremont/Miller miniseries, Kitty Pryde and Wolverine, and the first ten issues of the solo ongoing.")),
("Wolverine Omnibus Vol 1 2", dict(id="wolv-o2", title="Wolverine Omnibus", vol="Vol. 2",
  creators="Chris Claremont, John Buscema & Peter David", era="1988–1990", released="Aug 2021",
  art="o-brown", tex="tex-stripe", spine="Wolverine",
 cover="Art/Wolverine/wolv-o2.jpg",
  note="Madripoor, and Logan working as Patch. The brown-and-tan run at full strength, with thirty-four Marvel Comics Presents chapters threaded through it and Havok and Wolverine: Meltdown as the odd painted one out.")),
("Wolverine Omnibus Vol 1 3", dict(id="wolv-o3", title="Wolverine Omnibus", vol="Vol. 3",
  creators="Larry Hama, Marc Silvestri & Peter David", era="1990–1992", released="Jan 2023",
  art="o-madripoor", tex="tex-halftone", spine="Wolverine",
 cover="Art/Wolverine/wolv-o3.jpg",
  note="Hama takes over and holds the book for the next eight years. Silvestri draws it, Hearts of Darkness pairs him with Ghost Rider and the Punisher, and the Marvel Comics Presents run reaches #108.")),
("Wolverine Omnibus Vol 1 4", dict(id="wolv-o4", title="Wolverine Omnibus", vol="Vol. 4",
  creators="Larry Hama, Marc Silvestri & Mark Texeira", era="1992–1993", released="Sep 2023",
  art="o-patch", tex="tex-slash", spine="Wolverine",
 cover="Art/Wolverine/wolv-o4.jpg",
  note="Runs to #75 — Fatal Attractions, where Magneto pulls the adamantium out through his skin and the character stops being indestructible. Sabretooth's first solo miniseries is here too.")),
("Wolverine Omnibus Vol 1 5", dict(id="wolv-o5", title="Wolverine Omnibus", vol="Vol. 5",
  creators="Larry Hama, Adam Kubert & Val Semeiks", era="1993–1996", released="May 2024",
  art="o-adamantium", tex="tex-steel", chapterby="series", spine="Wolverine",
 cover="Art/Wolverine/wolv-o5.jpg",
  note="Bone claws, and a body that is slowly failing without the metal. Hama writes the devolution the whole way down, through #100 and the Genesis story, with a tail of mid-nineties one-shots after it.")),
("Wolverine Omnibus Vol 1 6", dict(id="wolv-o6", title="Wolverine Omnibus", vol="Vol. 6",
  creators="Larry Hama, Val Semeiks & Anthony Winn", era="1996–1997", released="Jun 2025",
  art="o-bone", tex="tex-halftone", chapterby="series", spine="Wolverine",
 cover="Art/Wolverine/wolv-o6.jpg",
  note="Onslaught, the feral turn, and the end of Hama's run. Ends up more anthology than ongoing — Days of Future Past, Ben Grimm and Logan, Kitty Pryde: Agent of S.H.I.E.L.D. and the two-issue Wolverine Encyclopedia all sit alongside the main title.")),
("Wolverine: Not Dead Yet Omnibus Vol 1 1", dict(id="ndy-o1", title="Wolverine: Not Dead Yet Omnibus", vol="",
  creators="Warren Ellis, Erik Larsen & Leinil Francis Yu", era="1997–2001", released="Jun 2026",
  art="o-fang", tex="tex-slash", spine="Not Dead Yet",
 cover="Art/Wolverine/ndy-o1.jpg",
  note="Named for the four-issue Ellis and Yu story that is the best thing in it. Picks up at #119 and runs to #158, and that is where the shelf stops — #159–189 is uncollected until The Return of Weapon X Omnibus prints it in 2027. Only #175, the anniversary issue, escapes the gap, in the Jason Aaron volume.")),
("Wolverine by Mark Millar Omnibus Vol 1 1", dict(id="millar-o1", title="Wolverine by Mark Millar Omnibus", vol="",
  creators="Mark Millar, John Romita Jr. & Steve McNiven", era="2004–2009", released="Jul 2013",
  art="o-millar", tex="tex-steel", spine="By Mark Millar",
 cover="Art/Wolverine/millar-o1.jpg",
  note="Two runs in one book. Enemy of the State turns him into HYDRA's weapon and points him at everyone he knows; Old Man Logan, five years later, is the western about the version of him who quit.")),
("Wolverine by Jason Aaron Omnibus Vol 1 1", dict(id="aaron-o1", title="Wolverine by Jason Aaron Omnibus", vol="",
  creators="Jason Aaron, Ron Garney & Adam Kubert", era="2007–2010", released="Oct 2011",
  art="o-aaron", tex="tex-stripe", spine="By Jason Aaron",
 cover="Art/Wolverine/aaron-o1.jpg",
  note="Get Mystique, Manifest Destiny, and all sixteen issues of Wolverine: Weapon X — the run where Aaron works out that the character is funniest and worst when he is certain he deserves what is coming.")),
("Wolverine Goes to Hell Omnibus Vol 1 1", dict(id="hell-o1", title="Wolverine Goes to Hell Omnibus", vol="",
  creators="Jason Aaron, Renato Guedes & Jason Latour", era="2010–2011", released="May 2018",
  art="o-hell", tex="tex-slash", spine="Goes to Hell",
 cover="Art/Wolverine/hell-o1.jpg",
  note="Aaron's second stretch: his soul in Hell, his body driving around murdering people, and Schism at the end of it — the argument with Cyclops that splits the X-Men in two.")),
("Uncanny X-Force by Rick Remender Omnibus Vol 1 1", dict(id="xforce-o1", title="Uncanny X-Force by Rick Remender Omnibus", vol="",
  creators="Rick Remender, Jerome Opeña & Esad Ribić", era="2010–2012", released="Mar 2014",
  art="o-xforce", tex="tex-steel", spine="Uncanny X-Force",
 cover="Art/Wolverine/xforce-o1.jpg",
  note="Wolverine's black-ops team, and the best-regarded X-book of its decade. The Apocalypse Solution, Dark Angel Saga and The Final Execution, the whole run. Shares its Road to Hell prologue with Goes to Hell, so that issue carries the same id in both.")),
("Death of Wolverine Omnibus Vol 1 1", dict(id="death-o1", title="Death of Wolverine Omnibus", vol="",
  creators="Paul Cornell, Charles Soule & Steve McNiven", era="2013–2015", released="Dec 2024",
  art="o-death", tex="tex-halftone", spine="Death of Wolverine",
 cover="Art/Wolverine/death-o1.jpg",
  note="Cornell strips the healing factor, Soule spends four issues killing him, and the tie-ins deal with the hole it leaves. He goes out encased in the metal he spent forty years being defined by.")),
("Return of Wolverine Omnibus Vol 1 1", dict(id="return-o1", title="Return of Wolverine Omnibus", vol="",
  creators="Charles Soule, Ray-Anthony Height & Declan Shalvey", era="2015–2019", released="Nov 2025",
  art="o-return", tex="tex-slash", chapterby="series", spine="Return of Wolverine",
 cover="Art/Wolverine/return-o1.jpg",
  note="Four years of everyone else looking for him: Wolverines, the five Hunt for Wolverine minis, the Marvel Legacy one-shot that gave it away, and finally the return itself.")),
("Wolverine: Sabretooth War Omnibus Vol 1 1", dict(id="sabre-o1", title="Wolverine: Sabretooth War Omnibus", vol="",
  creators="Victor LaValle, Benjamin Percy & Geoff Shaw", era="2022–2024", released="Jun 2025",
  art="o-sabretooth", tex="tex-stripe", spine="Sabretooth War",
 cover="Art/Wolverine/sabre-o1.jpg",
  note="The oldest fight on the shelf, finished. LaValle's two Sabretooth minis set it up and Percy's Wolverine #41–50 pays it off — the shortest book here and the only one that is a single story.")),
]

# Nothing pending on this shelf.
PLACEHOLDERS = []

# Display order of the shelf, by id. A reading order, which here is also close
# to publication order: the six mainline volumes run 1974-1997 in sequence,
# Not Dead Yet continues them to 2001, and the creator-run and event books
# follow in story order after the shelf's one gap.
#
# millar-o1 sits before aaron-o1 even though Old Man Logan (2008) overlaps
# Aaron's start -- Millar's book is one creator's complete run and reads as a
# unit. hell-o1 sits before xforce-o1 because Wolverine's own title is the
# spine of that moment; the two books share a Road to Hell prologue.
SHELF = [
  "wolv-o1", "wolv-o2", "wolv-o3", "wolv-o4", "wolv-o5", "wolv-o6",
  "ndy-o1",
  "millar-o1", "aaron-o1", "hell-o1", "xforce-o1",
  "death-o1", "return-o1", "sabre-o1",
]

PLACEHOLDER_PAGES = {}

# Series these books collect that the shared SERIES table in
# build_omnibus_data.py does not carry. "Wolverine Vol 3" is deliberately
# absent -- hulk_meta.py already maps it as ("wolv3", "Wolverine (2003)"), and
# the marvel.com id store is shared, so the same series must key the same way.
SERIES_EXTRA = {
 "Wolverine Vol 1":                                    ("wolv1",  "Wolverine (1982)"),
 "Wolverine Vol 2":                                    ("wolv2",  "Wolverine"),
 "Wolverine Vol 4":                                    ("wolv4",  "Wolverine (2010)"),
 "Wolverine Vol 5":                                    ("wolv5",  "Wolverine (2013)"),
 "Wolverine Vol 6":                                    ("wolv6",  "Wolverine (2014)"),
 "Wolverine Vol 7":                                    ("wolv7",  "Wolverine (2020)"),
 "Wolverine Annual Vol 1":                             ("wvann",  "Wolverine Annual"),
 "Wolverine Annual Vol 4":                             ("wvann4", "Wolverine Annual (2012)"),
 "Uncanny X-Force Vol 1":                              ("uxf",    "Uncanny X-Force"),
 "Wolverine Weapon X Vol 1":                           ("wvwx",   "Wolverine Weapon X"),
 "X-Men Vol 2":                                        ("xm2",    "X-Men (1991)"),
 "Wolverines Vol 1":                                   ("wvs",    "Wolverines"),
 "Death of Wolverine: The Logan Legacy Vol 1":         ("dwll",   "Death of Wolverine: The Logan Legacy"),
 "Astonishing Spider-Man & Wolverine Vol 1":           ("aspw",   "Astonishing Spider-Man & Wolverine"),
 "Kitty Pryde and Wolverine Vol 1":                    ("kpw",    "Kitty Pryde and Wolverine"),
 "Death of Wolverine: The Weapon X Program Vol 1":     ("dwwxp",  "Death of Wolverine: The Weapon X Program"),
 "Return of Wolverine Vol 1":                          ("row",    "Return of Wolverine"),
 "Sabretooth & the Exiles Vol 1":                      ("sabex",  "Sabretooth & the Exiles"),
 "Sabretooth Vol 4":                                   ("sab22",  "Sabretooth (2022)"),
 "Wolverine: Infinity Watch Vol 1":                    ("wiw",    "Wolverine: Infinity Watch"),
 "X-Men: Schism Vol 1":                                ("schism", "X-Men: Schism"),
 "Death of Wolverine Vol 1":                           ("dow",    "Death of Wolverine"),
 "Havok and Wolverine - Meltdown Vol 1":               ("hwmelt", "Havok and Wolverine: Meltdown"),
 "Hunt for Wolverine: Adamantium Agenda Vol 1":        ("hfwaa",  "Hunt for Wolverine: Adamantium Agenda"),
 "Hunt for Wolverine: Claws of a Killer Vol 1":        ("hfwck",  "Hunt for Wolverine: Claws of a Killer"),
 "Hunt for Wolverine: Mystery in Madripoor Vol 1":     ("hfwmm",  "Hunt for Wolverine: Mystery in Madripoor"),
 "Hunt for Wolverine: Weapon Lost Vol 1":              ("hfwwl",  "Hunt for Wolverine: Weapon Lost"),
 "Iron Fist: Wolverine Vol 1":                         ("ifw",    "Iron Fist: Wolverine"),
 "Sabretooth Vol 1":                                   ("sab93",  "Sabretooth (1993)"),
 "Wolverine/Gambit: Victims Vol 1":                    ("wgv",    "Wolverine/Gambit: Victims"),
 "Wolverine/Punisher Revelation Vol 1":                ("wpr",    "Wolverine/Punisher: Revelation"),
 "Wolverine: Manifest Destiny Vol 1":                  ("wmd",    "Wolverine: Manifest Destiny"),
 "Before the Fantastic Four: Ben Grimm and Logan Vol 1": ("bffbgl", "Before the Fantastic Four: Ben Grimm and Logan"),
 "Kitty Pryde: Agent of S.H.I.E.L.D. Vol 1":           ("kpsh",   "Kitty Pryde: Agent of S.H.I.E.L.D."),
 "Venom: Tooth and Claw Vol 1":                        ("vtc",    "Venom: Tooth and Claw"),
 "Wolverine and The Punisher: Damaging Evidence Vol 1": ("wpde",   "Wolverine and the Punisher: Damaging Evidence"),
 "Wolverine: Days of Future Past Vol 1":               ("wdofp",  "Wolverine: Days of Future Past"),
 "Punisher War Journal Vol 1":                         ("pwj",    "Punisher War Journal"),
 "Storm Vol 3":                                        ("storm14", "Storm (2014)"),
 "Wolverine & the X-Men Vol 2":                        ("wax14",  "Wolverine & the X-Men (2014)"),
 "Wolverine Encyclopedia Vol 1":                       ("wenc",   "Wolverine Encyclopedia"),
 "Wolverine: Road to Hell Vol 1":                      ("wrth",   "Wolverine: Road to Hell"),
 "All-New Wolverine Saga Vol 1":                       ("anws",   "All-New Wolverine Saga"),
 "Amazing Spider-Man Vol 4":                           ("asm15",  "Amazing Spider-Man (2015)"),
 "Best of Marvel Comics Vol 1":                        ("bomc",   "Best of Marvel Comics"),
 "Black Panther Vol 6":                                ("bp16",   "Black Panther (2016)"),
 "Captain America Annual Vol 1":                       ("caan1",  "Captain America Annual"),
 "Captain America Vol 9":                              ("cap18",  "Captain America (2018)"),
 "Dark Reign: The List - Wolverine Vol 1":             ("drlw",   "Dark Reign: The List - Wolverine"),
 "Dark X-Men: The Beginning Vol 1":                    ("dxmb",   "Dark X-Men: The Beginning"),
 "Deadpool Vol 3":                                     ("dp08",   "Deadpool (2008)"),
 "Death of Wolverine: Deadpool & Captain America Vol 1": ("dwdpca", "Death of Wolverine: Deadpool & Captain America"),
 "Death of Wolverine: Life After Logan Vol 1":         ("dwlal",  "Death of Wolverine: Life After Logan"),
 "Ghost Rider/Wolverine/Punisher: Hearts of Darkness Vol 1": ("grwphd", "Ghost Rider/Wolverine/Punisher: Hearts of Darkness"),
 "Ghost Rider/Wolverine/Punisher: The Dark Design Vol 1": ("grwptd", "Ghost Rider/Wolverine/Punisher: The Dark Design"),
 "Hunt for Wolverine Vol 1":                           ("hfw",    "Hunt for Wolverine"),
 "Hunt for Wolverine: Dead Ends Vol 1":                ("hfwde",  "Hunt for Wolverine: Dead Ends"),
 "Incredible Hulk Vol 5":                              ("ih17",   "Incredible Hulk (2017)"),
 "Invincible Iron Man Vol 4":                          ("iim17",  "Invincible Iron Man (2017)"),
 "Logan: Path of the Warlord Vol 1":                   ("lpw",    "Logan: Path of the Warlord"),
 "Logan: Shadow Society Vol 1":                        ("lss",    "Logan: Shadow Society"),
 "Marvel 2-In-One Vol 1":                              ("m21",    "Marvel 2-In-One (2018)"),
 "Marvel 75th Anniversary Celebration Vol 1":          ("m75",    "Marvel 75th Anniversary Celebration"),
 "Marvel Age Annual Vol 1":                            ("maan",   "Marvel Age Annual"),
 "Marvel Comic Vol 1":                                 ("mcvol",  "Marvel Comic"),
 "Marvel Legacy Vol 1":                                ("mleg",   "Marvel Legacy"),
 "Marvel: Shadows & Light Vol 1":                      ("msl",    "Marvel: Shadows & Light"),
 "Maverick Vol 1":                                     ("mav",    "Maverick"),
 "Mighty Thor Vol 2":                                  ("mt16",   "Mighty Thor (2016)"),
 "Nightcrawler Vol 4":                                 ("nc14",   "Nightcrawler (2014)"),
 "Spider-Man Versus Wolverine Vol 1":                  ("smvw",   "Spider-Man Versus Wolverine"),
 "Spider-Man, Punisher, Sabretooth: Designer Genes Vol 1": ("spsdg",  "Spider-Man, Punisher, Sabretooth: Designer Genes"),
 "Wolverine & Nick Fury: Scorpio Rising Vol 1":        ("wnfsr",  "Wolverine & Nick Fury: Scorpio Rising"),
 "Wolverine Special Vol 1":                            ("wsp",    "Wolverine Special"),
 "Wolverine/Cable: Guts and Glory Vol 1":              ("wcgg",   "Wolverine/Cable: Guts and Glory"),
 "Wolverine: Black Rio Vol 1":                         ("wbr",    "Wolverine: Black Rio"),
 "Wolverine: Dangerous Games Vol 1":                   ("wdg",    "Wolverine: Dangerous Games"),
 "Wolverine: Doombringer Vol 1":                       ("wdb",    "Wolverine: Doombringer"),
 "Wolverine: Evilution Vol 1":                         ("wev",    "Wolverine: Evilution"),
 "Wolverine: Global Jeopardy Vol 1":                   ("wgj",    "Wolverine: Global Jeopardy"),
 "Wolverine: Inner Fury Vol 1":                        ("wif",    "Wolverine: Inner Fury"),
 "Wolverine: Killing Vol 1":                           ("wkl",    "Wolverine: Killing"),
 "Wolverine: Knight of Terra Vol 1":                   ("wkot",   "Wolverine: Knight of Terra"),
 "Wolverine: Old Man Logan Giant-Size Vol 1":          ("womls",  "Wolverine: Old Man Logan Giant-Size"),
 "Wolverine: Rahne of Terra Vol 1":                    ("wrot",   "Wolverine: Rahne of Terra"),
 "Wolverine: The Jungle Adventure Vol 1":              ("wtja",   "Wolverine: The Jungle Adventure"),
 "X-Men Spotlight Vol 1":                              ("xmsp",   "X-Men Spotlight"),
 "X-Men: Red Vol 1":                                   ("xmred",  "X-Men Red"),
}

# Reused verbatim from the Hulk and Fantastic Four shelves' own SERIES_EXTRA.
# A hero only ever sees the shared SERIES table plus its OWN extras, so a series
# another shelf already carries has to be repeated here -- with exactly the same
# short code, because the marvel.com id store is shared and the same series must
# key the same way on every shelf.
SERIES_EXTRA.update({
 "Wolverine Vol 3":                                    ("wolv3",  "Wolverine (2003)"),
 "Uncanny X-Men Vol 1":                                ("uxm",    "Uncanny X-Men"),
 "Marvel Graphic Novel Vol 1":                         ("mgn",    "Marvel Graphic Novel"),
 "Marvel Fanfare Vol 1":                               ("mfan",   "Marvel Fanfare"),
 "Marvel Holiday Special Vol 1":                       ("mhs",    "Marvel Holiday Special"),
 "Cable Vol 1":                                        ("cable",  "Cable"),
 "Hulk Vol 1":                                         ("hk99",   "Hulk (1999)"),
 "Avengers Vol 7":                                     ("av7",    "Avengers (2016)"),
})
