# The hand-written half of the Black Panther shelf. Same shape as
# omnibus_meta.py, hulk_meta.py, ff_meta.py, wolverine_meta.py,
# moonknight_meta.py, daredevil_meta.py, silversurfer_meta.py,
# captainamerica_meta.py and ironman_meta.py -- ORDER (wiki-backed),
# PLACEHOLDERS (tiles with no contents), SHELF (display order by id),
# PLACEHOLDER_PAGES, and SERIES_EXTRA for the series the shared SERIES table in
# build_omnibus_data.py does not already carry.
#
# Scope: every Black Panther omnibus Marvel has printed, which is seven. Like
# Moon Knight, Silver Surfer and Iron Man there was no family character to rule
# out -- Shuri, Killmonger and the Dora Milaje have no omnibus of their own --
# and nothing here is unreleased, so the eligibility rule excludes nothing.
#
# The one judgement call was WAKANDA: WORLD OF BLACK PANTHER, which is an
# anthology rather than a run: sixty-five issues of minis set in Wakanda, some
# of them T'Challa's (Rise of the Black Panther, Long Live the King, the three
# Wakanda Forever one-shots, Black Panther vs. Deadpool, Agents of Wakanda) and
# some of them other people's (World of Wakanda, Shuri, Killmonger, The Crew).
# The user put it ON. It is the only volume here that is not a Black Panther
# title or a creator-run collection, and it is why the shelf has any overlap at
# all -- it reprints Black Panther (2018) #23-25 from the Coates volume and the
# Black Panther Annual (2018) C story from the Hudlin one.
#
# Two enumeration notes, both the Captain America lesson repeating:
#   - `apprefix=Black Panther` never sees WAKANDA: WORLD OF BLACK PANTHER. A
#     wiki search for "Wakanda Omnibus" does. Search as well as enumerate.
#   - "Black Panther: Revenge of the Black Panther Omnibus Vol 1 1" is a live
#     wiki page and is a #REDIRECT: the book was retitled to Panther's Prey
#     before it shipped. It is one book, not two.
#
# Two hand repairs live in blackpanther_contents_raw.json and a re-pull of
# either volume will undo both -- see "Contents" in CLAUDE.md:
#   - early-o1's ReprintOf fields (and its rendered gallery) put JUNGLE ACTION
#     #6-24 FIRST, grouped by series. Marvel's own solicit puts it last, which
#     is also what the blurb describes ("Then, Don McGregor launched T'Challa's
#     first solo series"). Moved to the end; the rest of the wiki's order is
#     the solicit's order exactly. Same hazard as inc-o1 on the Hulk shelf.
#   - FANTASTIC FOUR #54 is in neither the fields nor the gallery. The official
#     collecting line reads "...#52-53, and #56, #119 and material from #54",
#     so it is restored by hand. Same shape as Fantastic Four #171 and
#     Wolverine #55.

ORDER = [
("Black Panther: The Early Marvel Years Omnibus Vol 1 1", dict(id="early-o1", title="Black Panther: The Early Marvel Years Omnibus", vol="",
  creators="Stan Lee, Jack Kirby, Roy Thomas & Don McGregor", era="1966–1976", released="Jul 2022",
  art="o-savannah", tex="tex-kente", spine="Early Marvel Years",
 cover="Art/Black-Panther/early-o1.jpg",
  note="Ten years of being the best character in other people's comics, and then his own. Fantastic Four #52 is the first Black superhero in mainstream American comics and Kirby draws him as a head of state rather than a jungle lord; the Avengers issues are Roy Thomas working out what T'Challa is when he is not a guest. Then the last third of the book is Don McGregor's Jungle Action — “Panther's Rage”, thirteen issues of one continuous story at a time when nobody serialised anything, with Rich Buckler and Billy Graham on it and a page density that still reads as unusual.")),
("Black Panther: Panther's Prey Omnibus Vol 1 1", dict(id="prey-o1", title="Black Panther: Panther's Prey Omnibus", vol="",
  creators="Jack Kirby, Peter B. Gillis & Don McGregor", era="1977–1995", released="Feb 2026",
  art="o-kirby", tex="tex-krackle", spine="Panther's Prey",
 cover="Art/Black-Panther/prey-o1.jpg",
  note="The messy two decades, and the most interesting book on the shelf for it. Kirby comes back for fifteen issues and writes an outright pulp adventure — King Solomon's Frogs, time travel, a six-armed collector — which readers of Jungle Action hated and which is now the reason people buy this. Then the 1988 Gillis mini, Don McGregor and Dwayne Turner's Panther's Prey in 1991, and twenty-five chapters of Panther's Quest serialised eight pages at a time in Marvel Comics Presents. Solicited as “Revenge of the Black Panther” and retitled before it shipped.")),
("Black Panther by Christopher Priest Omnibus Vol 1 1", dict(id="priest-o1", title="Black Panther by Christopher Priest Omnibus", vol="Vol. 1",
  creators="Christopher Priest, Mark Texeira & Sal Velluto", era="1998–2000", released="Sep 2022",
  art="o-attache", tex="tex-halftone", spine="By Priest",
 cover="Art/Black-Panther/priest-o1.jpg",
  note="The run that decided what the character is now. Priest tells it out of order through Everett K. Ross, a State Department attaché narrating a disaster from a chair, and the joke covers a straight political thriller about a head of state who joined the Avengers to spy on them. The Dora Milaje are invented here. So is the idea that T'Challa is always three moves ahead, which every later writer and both films inherited.")),
("Black Panther by Christopher Priest Omnibus Vol 1 2", dict(id="priest-o2", title="Black Panther by Christopher Priest Omnibus", vol="Vol. 2",
  creators="Christopher Priest, Sal Velluto & Jim Calafiore", era="1986–2003", released="Feb 2024",
  art="o-frog", tex="tex-crosshatch", spine="By Priest",
 cover="Art/Black-Panther/priest-o2.jpg",
  note="The back half of the run, where it goes strange: the Sturm und Drang of the Iron Man fight, the King Solomon's Frogs paying off in a second Panther out of the future, and then Marvel takes the title off T'Challa entirely and hands it to Kevin “Kasper” Cole, a crooked Harlem cop in a stolen costume. That becomes The Crew, cancelled at seven issues and quietly one of the best things Priest wrote. The 1986 date on this tile is Thor #370 — an eight-page Black Panther backup by James Owsley, which is Priest under his own earlier name and the first Panther story he ever wrote.")),
("Black Panther by Reginald Hudlin Omnibus Vol 1 1", dict(id="hudlin-o1", title="Black Panther by Reginald Hudlin Omnibus", vol="",
  creators="Reginald Hudlin, John Romita Jr. & Ken Lashley", era="2005–2010", released="Mar 2025",
  art="o-royal", tex="tex-vibranium", spine="By Hudlin",
 cover="Art/Black-Panther/hudlin-o1.jpg",
  note="A film-maker's Black Panther, and the one the MCU actually drew on. Hudlin restarts from the origin with Romita Jr. drawing Wakanda as a superpower that has never lost a war, marries T'Challa to Storm across a company-wide crossover, sends the two of them through Civil War and Secret Invasion, and then puts Shuri in the suit for the 2009 series — which is where nearly everything the films did with her comes from. The X-Men issues are printed in crossover order rather than after the run, which is how the book prints them.")),
("Black Panther by Ta-Nehisi Coates Omnibus Vol 1 1", dict(id="coates-o1", title="Black Panther by Ta-Nehisi Coates Omnibus", vol="",
  creators="Ta-Nehisi Coates, Brian Stelfreeze & Daniel Acuña", era="2016–2021", released="Aug 2022",
  art="o-empire", tex="tex-nanite", spine="By Coates",
 cover="Art/Black-Panther/coates-o1.jpg",
  note="An essayist's Black Panther: fifty issues asking whether a hereditary monarch can be a hero at all, and mostly answering no. Stelfreeze's first arc is a Wakandan insurrection T'Challa cannot punch, and the second half moves the whole argument into space as the Intergalactic Empire of Wakanda — a slave state flying his own flag, five thousand years old, which he has to bring down without a memory of who he is. The longest single Black Panther run there has been.")),
("Wakanda: World of Black Panther Omnibus Vol 1 1", dict(id="wakanda-o1", title="Wakanda: World of Black Panther Omnibus", vol="",
  creators="Nnedi Okorafor, Roxane Gay & Evan Narcisse", era="2017–2021", released="Oct 2022",
  art="o-nation", tex="tex-kente", chapterby="series", spine="Wakanda",
 cover="Art/Black-Panther/wakanda-o1.jpg",
  note="Everything that grew up around the Coates run — the country as a setting other writers were let into. Roxane Gay and Yona Harvey on the Dora Milaje in World of Wakanda, Nnedi Okorafor on Shuri and on Long Live the King, Bryan Hill on Killmonger's making, Evan Narcisse retelling the origin in Rise of the Black Panther, and the Wakanda Forever one-shots. Note this is the one book on the shelf that is not a Black Panther title: about a third of it stars somebody else, and it doubles back over the Coates and Hudlin volumes for four issues.")),
]

# Nothing pending on this shelf.
PLACEHOLDERS = []

# Display order of the shelf, by id. A reading order, which on the first six is
# also publication order -- the books tile 1966 to 2021 with only the two
# uncollected runs missing (see CLAUDE.md). wakanda-o1 sits last rather than
# between coates-o1 and the rest: it is a cross-era anthology, the same
# placement the Doom and Ultimate volumes take at the end of the FF shelf, and
# reading it inside the Coates run would mean stopping that run twice.
SHELF = [
  "early-o1", "prey-o1",
  "priest-o1", "priest-o2",
  "hudlin-o1", "coates-o1",
  "wakanda-o1",
]

PLACEHOLDER_PAGES = {}

# Series these books collect that the shared SERIES table in
# build_omnibus_data.py does not carry. Display names are the marvel.com form
# (name plus start year) rather than the wiki's volume number, because that is
# what link_issues.py matches on -- the catalog carries eight series simply
# called "Black Panther", which is exactly the reused-title case its tiebreak()
# exists for.
#
# `bp` on its own is deliberately not used: there is no single Black Panther
# series to give it to, and a bare code would read as if there were.
SERIES_EXTRA = {
 "Black Panther Vol 1":                                ("bp77",    "Black Panther (1977)"),
 "Black Panther Vol 2":                                ("bp88",    "Black Panther (1988)"),
 "Black Panther Vol 4":                                ("bp05",    "Black Panther (2005)"),
 "Black Panther Vol 5":                                ("bp09",    "Black Panther (2009)"),
 "Black Panther Vol 7":                                ("bp18",    "Black Panther (2018)"),
 "Black Panther Annual Vol 1":                         ("bpann08", "Black Panther Annual (2008)"),
 "Black Panther Annual Vol 2":                         ("bpann18", "Black Panther Annual (2018)"),
 "Black Panther Saga Vol 1":                           ("bpsaga",  "Black Panther Saga"),
 "Black Panther: Panther's Prey Vol 1":                ("bpprey",  "Black Panther: Panther's Prey"),
 "Black Panther: World of Wakanda Vol 1":              ("bpwow",   "Black Panther: World of Wakanda"),
 "Black Panther: Long Live The King Vol 1":            ("bpllk",   "Black Panther: Long Live the King"),
 "Black Panther and the Crew Vol 1":                   ("bpcrew",  "Black Panther and the Crew"),
 "Black Panther and the Agents of Wakanda Vol 1":      ("bpaow",   "Black Panther and the Agents of Wakanda"),
 "Black Panther vs. Deadpool Vol 1":                   ("bpvdp",   "Black Panther vs. Deadpool"),
 "Black Panther/Captain America: Flags of Our Fathers Vol 1": ("bpcafof", "Captain America/Black Panther: Flags of Our Fathers"),
 "Rise of the Black Panther Vol 1":                    ("rbp",     "Rise of the Black Panther"),
 "King in Black: Black Panther Vol 1":                 ("kibbp",   "King in Black: Black Panther"),
 "Last Annihilation: Wakanda Vol 1":                   ("lawak",   "The Last Annihilation: Wakanda"),
 "Amazing Spider-Man: Wakanda Forever Vol 1":          ("asmwf",   "Amazing Spider-Man: Wakanda Forever"),
 "Wakanda Forever: X-Men Vol 1":                       ("wfxm",    "X-Men: Wakanda Forever"),
 "Wakanda Forever Avengers Vol 1":                     ("wfav",    "Avengers: Wakanda Forever"),
 "Shuri Vol 1":                                        ("shuri",   "Shuri"),
 "Killmonger Vol 1":                                   ("killm",   "Killmonger"),
 "Jungle Action Vol 2":                                ("ja",      "Jungle Action"),
 "Crew Vol 1":                                         ("crew",    "The Crew"),
 "Deadpool Vol 2":                                     ("dp97",    "Deadpool (1997)"),
 "Thor Vol 1":                                         ("thor",    "Thor (1966)"),
 "Fantastic Four Unlimited Vol 1":                     ("ffunl",   "Fantastic Four Unlimited"),
 "Over the Edge Vol 1":                                ("ote",     "Over the Edge"),
 "Marvel's Voices Vol 1":                              ("mvoi",    "Marvel's Voices"),
 "Marvel's Voices: Legacy Vol 1":                      ("mvleg",   "Marvel's Voices: Legacy"),
 "Venomverse: War Stories Vol 1":                      ("vvws",    "Venomverse: War Stories"),
}

# Reused verbatim from the other shelves' own SERIES_EXTRA and from the shared
# table. A hero only ever sees SERIES plus its OWN extras, so a series another
# shelf already carries has to be repeated here -- with exactly the same short
# code, because marvel_ids.json is shared and the same comic must key the same
# way on every shelf. (autocode() would reuse them anyway; they are written out
# so the codes are readable beside the ones they sit next to.)
SERIES_EXTRA.update({
 "Black Panther Vol 3":                                ("bp98",    "Black Panther (1998)"),
 "Black Panther Vol 6":                                ("bp16",    "Black Panther (2016)"),
 "Marvel Comics Vol 1":                                ("mc1k",    "Marvel Comics"),
 "Marvel Double Shot Vol 1":                           ("mdshot",  "Marvel Double Shot"),
 "Solo Avengers Vol 1":                                ("solav",   "Solo Avengers"),
 "Marvel Fanfare Vol 1":                               ("mfan",    "Marvel Fanfare"),
 "Marvel Super-Heroes Vol 2":                          ("msh2",    "Marvel Super-Heroes (1990)"),
 "Defenders Vol 1":                                    ("defs",    "Defenders"),
 "Iron Man Annual Vol 1":                              ("imann",   "Iron Man Annual (1970)"),
 "Astonishing Tales Vol 1":                            ("astt",    "Astonishing Tales"),
 "Incredible Hulk Vol 2":                              ("hulk2",   "Incredible Hulk (2000)"),
 "X-Men Vol 2":                                        ("xm2",     "X-Men (1991)"),
 "Avengers Vol 1":                                     ("av",      "Avengers"),
 "Captain America Vol 1":                              ("cap",     "Captain America (1968)"),
 "Daredevil Vol 1":                                    ("dd",      "Daredevil (1964)"),
 "Daredevil Annual Vol 1":                             ("ddann",   "Daredevil Annual (1967)"),
 "Tales of Suspense Vol 1":                            ("tos",     "Tales of Suspense"),
 "What The--?! Vol 1":                                 ("wthe",    "What The--?!"),
})
