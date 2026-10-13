# The hand-written half of the Green Lantern shelf -- THE FIRST DC SHELF.
# Same shape as every Marvel meta module (ORDER, PLACEHOLDERS, SHELF,
# PLACEHOLDER_PAGES, SERIES_EXTRA); what differs is where the contents and the
# links come from. See "The DC side" in CLAUDE.md.
#
# CONTENTS COME FROM TWO SOURCES, and the split is DC Database's coverage, not
# a choice:
#   - SEVEN volumes have a DC Database page with an IssueList of {{C|...}}
#     entries -- the DC wiki's equivalent of Marvel's ReprintOf fields. Johns
#     Vol. 1-3, both Tomasi & Gleason Corps books, Red Lanterns and Brightest
#     Day. Johns Vol. 1 matches DC's own collecting line exactly; Johns Vol. 2
#     and 3 match it except for two solicit typos the printed contents settle
#     (the solicit says Blackest Night #0-7 where the book prints #8, and
#     Green Lantern #53-60 where it prints #53-67 -- War of the Green Lanterns
#     is in it, so #64-67 have to be).
#   - FIVE have no DC Database page at all -- both Silver Age volumes, Hard
#     Travelin' Heroes and both Venditti books. Their contents are DC's own
#     collecting lines, which on the Marvel shelves are the INDEPENDENT check
#     on the wiki rather than the source. Order for the three multi-series
#     ones (Hard Travelin' Heroes, Venditti 1-2) is by on-sale date from the
#     DCUI catalog, because no source gives the printed table of contents.
#     If a DC Database page appears for any of them, prefer it.
#
# SCOPE was the user's call. Eight books are plainly Green Lantern's own and
# went on without a question: The Silver Age Omnibus Vol. 1-2, Hard Travelin'
# Heroes, Johns Vol. 1-3 and Venditti Vol. 1-2. Four were offered and ALL FOUR
# CAME BACK... three on:
#   - GREEN LANTERN CORPS by Tomasi & Gleason Vol. 1-2 are ON -- the Corps'
#     own title, Guy Gardner and Kyle Rayner's book, crossing over with Johns
#     constantly.
#   - RED LANTERNS: THE NEW 52 is ON -- Atrocitus's book, the shape that keeps
#     She-Hulk off the Hulk shelf, and the user took it anyway.
#   - BRIGHTEST DAY is ON -- an ensemble event where Hal is barely present.
#   - HAL JORDAN AND THE GREEN LANTERN CORPS by Venditti (ships 1 Dec 2026)
#     is OFF. Not a gate failure; the user did not pick it.
# Also off, by the user: the BLACKEST NIGHT OMNIBUS -- Johns Vol. 2 already
# prints Blackest Night #0-8, so it would have added only other characters'
# tie-ins. And the 2010-11 THE GREEN LANTERN OMNIBUS Vol. 1-2 are off for the
# reason the Kirby omnibus is off the Captain America shelf: every issue in
# them is in the Silver Age Omnibus Vol. 1.
#
# WHAT IS NOT HERE IS DC'S DOING, and it is the biggest hole on any shelf on
# the site: GREEN LANTERN (1960) #124-224 AND THE WHOLE OF GREEN LANTERN (1990)
# -- 1979 to 2004, twenty-five years, including Englehart and Staton's Corps,
# Emerald Twilight and Kyle Rayner's entire decade as the only Green Lantern.
# None of it has an omnibus. The note on `johns-o1` says so.

ORDER = [
("Green Lantern: The Silver Age Omnibus Vol. 1", dict(id="sa-o1",
  title="Green Lantern: The Silver Age Omnibus", vol="Vol. 1",
  creators="John Broome & Gil Kane", era="1959–1965", released="Feb 2017",
  art="o-oa", tex="tex-starfield", spine="The Silver Age",
  cover="Art/Green-Lantern/sa-o1.jpg",
  note="Julius Schwartz had already brought back the Flash with a new man under an old name, and Showcase #22 does it again: Hal Jordan, a test pilot at Ferris Aircraft, pulled out of a flight simulator by a dying alien who needs someone \"utterly without fear\". Everything that makes Green Lantern a space book is invented in these first few years — the Guardians of Oa, the Corps, the oath, the yellow weakness, Sinestro in #7 and Star Sapphire in #16. John Broome writes almost all of it as clean science-fiction puzzle stories. The thing to look at is Gil Kane: his figures are lean and athletic and always mid-motion, and he is the artist who first understood that the ring meant drawing a fist coming straight out of the page at you."),
),
("Green Lantern: The Silver Age Omnibus Vol. 2", dict(id="sa-o2",
  title="Green Lantern: The Silver Age Omnibus", vol="Vol. 2",
  creators="John Broome, Gardner Fox & Gil Kane", era="1965–1970", released="Jun 2018",
  art="o-qward", tex="tex-construct", spine="The Silver Age",
  cover="Art/Green-Lantern/sa-o2.jpg",
  note="The back half of the original run. Green Lantern #40 is the one everybody means: Hal meets the Golden Age Green Lantern, Alan Scott, and the Guardians tell the story of Krona, the renegade who looked back at the creation of the universe and let evil into it — a single panel of a giant hand at the dawn of time that Geoff Johns would build a whole decade on forty years later. Gil Kane's drawing loosens and gets more ambitious as the sixties go on. By the end the book is running out of road; the sales are falling and #75 is the last issue before DC hands it to two people who will tear it up."),
),
("Green Lantern/Green Arrow: Hard Travelin' Heroes Omnibus", dict(id="hth-o1",
  title="Green Lantern/Green Arrow: Hard Travelin' Heroes Omnibus", vol="",
  creators="Dennis O'Neil, Neal Adams & Mike Grell", era="1970–1979", released="Nov 2024",
  art="o-highway", tex="tex-halftone", spine="Hard Travelin' Heroes",
  cover="Art/Green-Lantern/hth-o1.jpg",
  note="Green Lantern #76: an old man asks Hal Jordan why he has helped the blue skins and the orange skins on other planets and never once the black skins on his own, and Hal has no answer. Dennis O'Neil and Neal Adams put Green Arrow in the book as a loudmouth leftist conscience and send the two of them across America in a pickup truck, and comics have been arguing about relevance ever since. #85–86 is the one with Speedy and the needle. #87 introduces John Stewart. Look at Adams: photographic faces, real light, figures that weigh something — nothing at DC had looked like it. The book was cancelled at #89 and survived as a back-up in The Flash, then came back in 1976 with Mike Grell, and this omnibus prints all of it, the one skip being #88."),
),
("Green Lantern by Geoff Johns Omnibus Vol. 1", dict(id="johns-o1",
  title="Green Lantern by Geoff Johns Omnibus", vol="Vol. 1",
  creators="Geoff Johns, Ethan Van Sciver & Ivan Reis", era="2004–2007", released="Jan 2015",
  art="o-rebirth", tex="tex-construct", spine="By Geoff Johns",
  cover="Art/Green-Lantern/johns-o1.jpg",
  note="Twenty-five years jump between the last book and this one, and none of them has an omnibus: the rest of the 1960 run, Emerald Twilight, where Hal goes mad and kills the Corps, and Kyle Rayner's whole decade as the last Green Lantern. Rebirth exists to undo that, and its trick is to make the madness a monster — Parallax, the yellow fear entity — so Hal was possessed rather than broken. Ethan Van Sciver draws it in obsessive detail, every ring construct full of tiny machinery. Then Geoff Johns builds outward: the Sinestro Corps War is where the emotional spectrum stops being a weakness and becomes a cosmology, with Ivan Reis drawing armies of yellow and green across double-page spreads. It ends on a prophecy, and the prophecy is the next book."),
),
("Green Lantern Corps by Peter J. Tomasi and Patrick Gleason Omnibus Vol. 1", dict(id="glc-o1",
  title="Green Lantern Corps by Tomasi & Gleason Omnibus", vol="Vol. 1",
  creators="Peter J. Tomasi, Dave Gibbons & Patrick Gleason", era="2005–2009", released="Aug 2023",
  art="o-corps", tex="tex-starfield", spine="Corps by Tomasi & Gleason",
  cover="Art/Green-Lantern/glc-o1.jpg",
  note="The other half of the Johns years, and the book that made the Corps feel like a place rather than a backdrop. Guy Gardner and Kyle Rayner run the recruits; Kilowog yells at them; Mogo is a planet and Salaak files the paperwork. Dave Gibbons co-writes Recharge and the first stretch, then Peter Tomasi takes over and writes the Corps like a war novel — who dies, who breaks, who gets home. Patrick Gleason's art is the thing to watch: he loves alien bodies, and the book is full of Lanterns who are crystals, insects or a single giant eye. The Sinestro Corps War chapters are the same ones Johns Vol. 1 prints, interleaved here as they were published."),
),
("Green Lantern by Geoff Johns Omnibus Vol. 2", dict(id="johns-o2",
  title="Green Lantern by Geoff Johns Omnibus", vol="Vol. 2",
  creators="Geoff Johns, Ivan Reis & Doug Mahnke", era="2008–2010", released="Jul 2015",
  art="o-blackest", tex="tex-spectrum", spine="By Geoff Johns",
  cover="Art/Green-Lantern/johns-o2.jpg",
  note="Johns fills in the spectrum one colour at a time: Secret Origin retells Showcase #22 for a modern reader, the Red Lanterns vomit rage-blood in Rage of the Red Lanterns, Larfleeze hoards everything in Agent Orange, and then all seven Corps are on the board when the dead start to rise. Blackest Night is the event the whole run was built toward, and it is a zombie story with a rule: the Black Lanterns can see your emotions, so the only defence is to feel nothing. Ivan Reis draws the core series as wall-to-wall spectacle, every hero who ever died back in black rings. Doug Mahnke takes over the monthly from #43 and draws it uglier and better."),
),
("Green Lantern Corps by Peter J. Tomasi and Patrick Gleason Omnibus Vol. 2", dict(id="glc-o2",
  title="Green Lantern Corps by Tomasi & Gleason Omnibus", vol="Vol. 2",
  creators="Peter J. Tomasi & Patrick Gleason", era="2009–2013", released="Nov 2024",
  art="o-emerald", tex="tex-halftone", spine="Corps by Tomasi & Gleason",
  cover="Art/Green-Lantern/glc-o2.jpg",
  note="Blackest Night from the trenches, with Gleason drawing the dead Lanterns of Oa rising out of the crypts — his last stretch on the book. Then Guy Gardner's own title: Emerald Warriors is Tomasi writing Guy as what he always was under the bluster, the Lantern who goes where the others will not, and it runs straight into the War of the Green Lanterns, interleaved here with the Johns chapters. Then the New 52 relaunch, drawn by Fernando Pasarin: Guy and John Stewart lead a Corps being hunted by the Guardians' Third Army, and an early arc turns on John killing a captured fellow Lantern rather than let him be tortured into talking. Tomasi leaves at #20, the same month Johns does."),
),
("Green Lantern by Geoff Johns Omnibus Vol. 3", dict(id="johns-o3",
  title="Green Lantern by Geoff Johns Omnibus", vol="Vol. 3",
  creators="Geoff Johns & Doug Mahnke", era="2010–2013", released="Apr 2016",
  art="o-sinestro", tex="tex-spectrum", spine="By Geoff Johns",
  cover="Art/Green-Lantern/johns-o3.jpg",
  note="The end of nine years. The first third is the Brightest Day years and the War of the Green Lanterns, where Krona — the man from the 1965 Silver Age issue — finally gets his story. Then the New 52 relaunch does the bold thing: Sinestro wears a green ring again, and the best stretch of the run is Hal and Sinestro forced to work together, two men who know each other better than anyone. #0 introduces Simon Baz, a Lebanese-American from Dearborn who gets a ring in an interrogation room. Doug Mahnke draws it with heavy blacks and creased, sweating faces. #20 is Johns's last issue and it is extra-sized, with an epilogue that walks the cast into the future one at a time. It is widely held to be one of the best farewell issues any long run has had."),
),
("Red Lanterns: The New 52 Omnibus", dict(id="red-o1",
  title="Red Lanterns: The New 52 Omnibus", vol="",
  creators="Peter Milligan, Charles Soule & Various", era="2011–2015", released="Jun 2025",
  art="o-rage", tex="tex-crosshatch", spine="Red Lanterns",
  cover="Art/Green-Lantern/red-o1.jpg",
  note="Atrocitus's book, and the stranger end of the spectrum: a title about a corps whose members are powered by rage and mostly cannot speak. Peter Milligan writes the first stretch as a horror book about anger with nowhere to go. Then Charles Soule takes over and does the obvious, brilliant thing — he puts Guy Gardner in a red ring, undercover and then not, and the book becomes a story about a man who has always been furious discovering he is good at leading people who are worse. Supergirl joins for a crossover, which is exactly as odd as it sounds. The Lights Out and Godhead chapters are shared with the Venditti books."),
),
("Green Lantern by Robert Venditti Omnibus Vol. 1", dict(id="ven-o1",
  title="Green Lantern by Robert Venditti Omnibus", vol="Vol. 1",
  creators="Robert Venditti, Van Jensen & Billy Tan", era="2013–2014", released="Oct 2025",
  art="o-relic", tex="tex-starfield", spine="By Robert Venditti",
  cover="Art/Green-Lantern/ven-o1.jpg",
  note="Following Johns is impossible, and Robert Venditti does it by changing the job: Hal is no longer the hotshot, he is the leader of the Corps, and he is not good at it yet. The big idea is Relic, a scientist from the universe before this one, who discovers that the emotional spectrum is a finite reservoir and every ring is draining it — so the Lanterns are the threat. Lights Out turns the lights off. The Green Lantern Corps chapters, written by Van Jensen with Bernard Chang, run alongside as one story. Billy Tan's art is crisp, house-style superhero work."),
),
("Green Lantern by Robert Venditti Omnibus Vol. 2", dict(id="ven-o2",
  title="Green Lantern by Robert Venditti Omnibus", vol="Vol. 2",
  creators="Robert Venditti & Billy Tan", era="2014–2016", released="Jan 2026",
  art="o-godhead", tex="tex-construct", spine="By Robert Venditti",
  cover="Art/Green-Lantern/ven-o2.jpg",
  note="Godhead pits the whole spectrum against Kirby's New Gods, who want the white ring because they think it is the Life Equation, and it runs through every Lantern book at once. Then the run reinvents itself: Hal goes renegade with a stolen gauntlet, a beard and a truck, on the run from the Corps he used to lead — a Hal Jordan who is the outlaw for once instead of the cop. It closes the New 52 run at #52, and the next thing Venditti writes is the Rebirth relaunch that is not on this shelf."),
),
]

PLACEHOLDERS = []

# Reading order, which here is also publication order of the material with
# the two Corps books slotted beside the Johns volumes they run alongside.
#   - glc-o1 sits after johns-o1 because both print the Sinestro Corps War, and
#     reading Johns's half first is how it was published.
#   - red-o1 sits after johns-o3 rather than earlier, though it starts in
#     2011: it is the New 52 Red Lantern book and its chapters run into Lights
#     Out, which is ven-o1.
SHELF = ["sa-o1", "sa-o2", "hth-o1", "johns-o1", "glc-o1", "johns-o2",
         "glc-o2", "johns-o3", "red-o1", "ven-o1", "ven-o2"]

PLACEHOLDER_PAGES = {}

# Every series this shelf collects, pinned before anyone reads with them --
# an issue id is a saved-progress key. Display names are DCUI's form with the
# year a series started, and THE YEAR IS LOAD-BEARING: dc_link.py reads it to
# choose between same-named series (there are six called "Green Lantern").
SERIES_EXTRA = {
 "Green Lantern Vol 2":                                   ("gl2",     "Green Lantern (1960)"),
 "Green Lantern Vol 4":                                   ("gl4",     "Green Lantern (2005)"),
 "Green Lantern Vol 5":                                   ("gl5",     "Green Lantern (2011)"),
 "Green Lantern Annual Vol 5":                            ("gl5ann",  "Green Lantern Annual (2011)"),
 "Green Lantern Corps Vol 2":                             ("glc2",    "Green Lantern Corps (2006)"),
 "Green Lantern Corps Vol 3":                             ("glc3",    "Green Lantern Corps (2011)"),
 "Green Lantern Corps Annual Vol 3":                      ("glc3ann", "Green Lantern Corps Annual (2011)"),
 "Green Lantern Corps: Recharge Vol 1":                   ("glcr",    "Green Lantern Corps: Recharge (2005)"),
 "Green Lantern Corps: Futures End Vol 1":                ("glcfe",   "Green Lantern Corps: Futures End (2014)"),
 "Green Lantern: Futures End Vol 1":                      ("glfe",    "Green Lantern: Futures End (2014)"),
 "Green Lantern Secret Files and Origins":                ("glsf",    "Green Lantern Secret Files and Origins (2005)"),
 "Green Lantern/New Gods: Godhead Vol 1":                 ("glgod",   "Green Lantern/New Gods: Godhead (2014)"),
 "Green Lantern/Sinestro Corps Secret Files and Origins Vol 1": ("glscsf", "Green Lantern/Sinestro Corps Secret Files (2008)"),
 "Green Lantern: Emerald Warriors Vol 1":                 ("glew",    "Green Lantern: Emerald Warriors (2010)"),
 "Green Lantern: Larfleeze Christmas Special Vol 1":      ("gllarf",  "Green Lantern: Larfleeze Christmas Special (2010)"),
 "Green Lantern: New Guardians Vol 1":                    ("glng",    "Green Lantern: New Guardians (2011)"),
 "Green Lantern: Rebirth Vol 1":                          ("glreb",   "Green Lantern: Rebirth (2004)"),
 "Green Lantern: Sinestro Corps Special Vol 1":           ("glscs",   "Green Lantern: Sinestro Corps Special (2007)"),
 "Green Lantern 80th Anniversary 100-Page Super Spectacular Vol 1": ("gl80", "Green Lantern 80th Anniversary Special (2020)"),
 "Blackest Night Vol 1":                                  ("bn",      "Blackest Night (2009)"),
 "Blackest Night: Tales of the Corps Vol 1":              ("bntc",    "Blackest Night: Tales of the Corps (2009)"),
 "Untold Tales of Blackest Night Vol 1":                  ("utbn",    "Untold Tales of Blackest Night (2010)"),
 "Brightest Day Vol 1":                                   ("bd",      "Brightest Day (2010)"),
 "Brave and the Bold Vol 1":                              ("bab",     "The Brave and the Bold (1955)"),
 "DC Special Series Vol 1":                               ("dcss",    "DC Special Series (1977)"),
 "DC Super-Stars Vol 1":                                  ("dcsst",   "DC Super-Stars (1976)"),
 "DC Universe Vol 1":                                     ("dcu",     "DC Universe (2008)"),
 "Flash Vol 1":                                           ("fl",      "The Flash (1959)"),
 "Infinity Man and the Forever People Vol 1":             ("imfp",    "Infinity Man and the Forever People (2014)"),
 "Red Lanterns Vol 1":                                    ("rl",      "Red Lanterns (2011)"),
 "Red Lanterns Annual Vol 1":                             ("rlann",   "Red Lanterns Annual (2013)"),
 "Red Lanterns: Futures End Vol 1":                       ("rlfe",    "Red Lanterns: Futures End (2014)"),
 "Secret Origins Vol 3":                                  ("so3",     "Secret Origins (2014)"),
 "Showcase Vol 1":                                        ("sc",      "Showcase (1956)"),
 "Showcase '95 Vol 1":                                    ("sc95",    "Showcase '95 (1995)"),
 "Sinestro Vol 1":                                        ("sin",     "Sinestro (2014)"),
 "Stormwatch Vol 3":                                      ("sw3",     "Stormwatch (2011)"),
 "Supergirl Vol 6":                                       ("sg6",     "Supergirl (2011)"),
 "Tales of the Sinestro Corps: Superman-Prime Vol 1":     ("tscsp",   "Tales of the Sinestro Corps: Superman-Prime (2007)"),
 "World's Finest Comics Vol 1":                           ("wfc",     "World's Finest Comics (1941)"),
}

# Shelf issue id -> DCUI book uuid, for the books no rule in dc_link.py can
# reach. Every one is on DCUI and readable; what defeats the matcher is how
# DCUI files it, and each line says how. Keep this short -- prefer a rule
# when a shape repeats.
DC_ISSUE_ALIAS = {
    # slug carries a hash where the number should be: showcase-1956-1978-22-41d26
    "sc-22":      "a834c7a8-b60b-49eb-929a-b07c8c1394d4",
    # the point issue is "feat-relic" with the dot dropped: ...-feat-relic-2013-231
    "gl5-23.1":   "00839ad3-ea6f-4b49-849f-6682510cf4f0",
    # filed in the umbrella series "DC Secret Files" under a shortened name
    "glsf-2005":  "f29d51a3-c9ee-40bd-9e57-5421ebde0243",
    "glscsf-1":   "75a4dd75-d573-4626-b595-a51625db1126",
    # filed in "The Green Lantern Season Two", with the "100-Page Super
    # Spectacular" title the shelf's display name shortens
    "gl80-1":     "69686feb-7ee2-4bbc-b70c-e754e0dfb5bc",
}

# Catalog dates that are simply wrong, shelf issue id -> on-sale date. Used to
# order the issues inside a collection. DCUI dates Blackest Night #0 to July
# 2010; it was the Free Comic Book Day issue, 2 May 2009, and it is the event's
# prologue.
DATE_FIX = {
    "bn-0": "2009-05-02",
}


# ---- Collections -----------------------------------------------------------
# Custom omnibuses that DC never printed: the Geoff Johns run, Johns Vol. 1-3
# plus both Tomasi & Gleason Corps books, regrouped by story arc instead of by
# title. Brightest Day is left out, and so is the back matter that is not the
# run (Showcase '95 #7-8, the 80th Anniversary Special). The user's call, Oct
# 2026.
#
# A collection holds no issues of its own -- every id here is a shelf issue id,
# so a mark in a collection is the same mark in the omnibus that prints it.
# build_omnibus_data.py checks every id is on the shelf and sorts each
# chapter by on-sale date, so a chapter is listed by what goes in it, not in
# reading order. Chapters are named for the Green Lantern arc of the moment;
# Corps issues sit in the chapter whose months they came out in.

def rng(code, a, b):
    return ["%s-%d" % (code, n) for n in range(a, b + 1)]


COLLECTIONS = [
    dict(id="coll-rebirth", spine="Rebirth", title="Green Lantern: Rebirth",
         vol="Vol. 1", era="2004-2007", cover_issue="glreb-1",
         creators="Geoff Johns, Ethan Van Sciver, Dave Gibbons & Patrick Gleason",
         note="Hal Jordan comes back, and the Corps is rebuilt around him. Rebirth, "
              "Johns's first twenty issues of Green Lantern, and the Corps book "
              "from Recharge to the eve of the Sinestro Corps War, read month by "
              "month. Green Lantern Corps #4-6 are not in either omnibus, so they "
              "are not here either.",
         chapters=[
             ("Rebirth", rng("glreb", 1, 6) + ["glsf-2005"]),
             ("No Fear", rng("gl4", 1, 6) + rng("glcr", 1, 3)),
             ("Revenge of the Green Lanterns", rng("gl4", 7, 13) + rng("glcr", 4, 5) + rng("glc2", 1, 3)),
             ("Wanted: Hal Jordan", rng("gl4", 14, 20) + rng("glc2", 7, 13)),
         ]),
    dict(id="coll-scw", spine="Sinestro Corps War", title="The Sinestro Corps War",
         vol="Vol. 2", era="2007-2008", cover_issue="glscs-1",
         creators="Geoff Johns, Dave Gibbons, Ivan Reis & Patrick Gleason",
         note="The crossover that turned the book into an event engine: Green "
              "Lantern and Green Lantern Corps alternating chapter by chapter, "
              "bookended by the Special and the Secret Files.",
         chapters=[
             ("The Sinestro Corps War", ["glscs-1"] + rng("gl4", 21, 25) + rng("glc2", 14, 19)
              + ["tscsp-1", "glscsf-1"]),
         ]),
    dict(id="coll-origin", spine="Secret Origin", title="Secret Origin & the Red Lanterns",
         vol="Vol. 3", era="2007-2009", cover_issue="gl4-36",
         creators="Geoff Johns, Peter J. Tomasi, Ivan Reis & Patrick Gleason",
         note="The road to Blackest Night: the Alpha Lanterns, Hal's origin retold, "
              "Atrocitus and the Red Lanterns, Larfleeze and Agent Orange, with "
              "the Corps book running alongside.",
         chapters=[
             ("The Alpha Lanterns", rng("gl4", 26, 28) + rng("glc2", 20, 22)),
             ("Secret Origin", rng("gl4", 29, 35) + ["dcu-0"] + rng("glc2", 23, 29)),
             ("Rage of the Red Lanterns", rng("gl4", 36, 38) + rng("glc2", 30, 33)),
             ("Agent Orange", rng("gl4", 39, 42) + ["bn-0"] + rng("glc2", 34, 38)),
         ]),
    dict(id="coll-bn", spine="Blackest Night", title="Blackest Night",
         vol="Vol. 4", era="2009-2010", cover_issue="bn-1",
         creators="Geoff Johns, Peter J. Tomasi, Ivan Reis & Patrick Gleason",
         note="The event itself, read the way it came out: Blackest Night with "
              "both Lantern books' tie-ins slotted in by week.",
         chapters=[
             ("Blackest Night", rng("bn", 1, 8) + rng("bntc", 1, 3) + rng("gl4", 43, 52)
              + rng("glc2", 39, 47) + ["utbn-1"]),
         ]),
    dict(id="coll-war", spine="War of the Green Lanterns", title="War of the Green Lanterns",
         vol="Vol. 5", era="2010-2011", cover_issue="gl4-64",
         creators="Geoff Johns, Peter J. Tomasi, Doug Mahnke & Fernando Pasarin",
         note="Green Lantern during Brightest Day and Emerald Warriors beside it, "
              "then Krona and the war itself. Green Lantern Corps #48-57 are in "
              "no omnibus, so the Corps strand here is Emerald Warriors.",
         chapters=[
             ("Brightest Day", rng("gl4", 53, 62) + rng("glew", 1, 7) + ["gllarf-1"]),
             ("War of the Green Lanterns", rng("gl4", 63, 67) + rng("glc2", 58, 60) + rng("glew", 8, 10)),
             ("Aftermath", rng("glew", 11, 13)),
         ]),
    dict(id="coll-sinestro", spine="Sinestro", title="The New 52: Sinestro",
         vol="Vol. 6", era="2011-2012", cover_issue="gl5-1",
         creators="Geoff Johns, Peter J. Tomasi, Doug Mahnke & Fernando Pasarin",
         note="The 2011 relaunch: Sinestro wearing the green ring and Hal without "
              "one, with the new Corps book alongside.",
         chapters=[
             ("Sinestro", rng("gl5", 1, 6) + rng("glc3", 1, 6)),
             ("The Revenge of Black Hand", rng("gl5", 7, 12) + rng("glc3", 7, 12)),
         ]),
    dict(id="coll-wrath", spine="Wrath of the First Lantern",
         title="Rise of the Third Army & Wrath of the First Lantern",
         vol="Vol. 7", era="2012-2013", cover_issue="gl5-20",
         creators="Geoff Johns, Peter J. Tomasi, Doug Mahnke & Fernando Pasarin",
         note="The Guardians' Third Army, the First Lantern, and the end of the "
              "Johns run at Green Lantern #20.",
         chapters=[
             ("Rise of the Third Army", ["gl5ann-1", "gl5-0", "glc3-0"] + rng("gl5", 13, 16)
              + rng("glc3", 13, 16) + ["glc3ann-1"]),
             ("Wrath of the First Lantern", rng("gl5", 17, 20) + rng("glc3", 17, 20)),
         ]),
]
