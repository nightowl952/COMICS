# The hand-written half of the Moon Knight shelf. Same shape as omnibus_meta.py,
# hulk_meta.py, ff_meta.py and wolverine_meta.py -- ORDER (wiki-backed),
# PLACEHOLDERS (tiles with no contents), SHELF (display order by id),
# PLACEHOLDER_PAGES, and SERIES_EXTRA for the series the shared SERIES table in
# build_omnibus_data.py does not already carry.
#
# Scope: every Moon Knight omnibus Marvel has printed. The Marvel Database
# lists exactly seven and all seven are on the shelf -- unlike the Hulk, FF and
# Wolverine shelves there is no family character to rule out (no She-Hulk, no
# Laura Kinney) and no team book to argue about. Nothing is solicited-but-
# unprinted either, so the "a shelf holds books you can actually buy" rule
# excludes nothing here.
#
# `chapterby` overrides the automatic chaptering heuristic on one volume.

ORDER = [
("Moon Knight Omnibus Vol 1 1", dict(id="mk-o1", title="Moon Knight Omnibus", vol="Vol. 1",
  creators="Doug Moench, Don Perlin & Bill Sienkiewicz", era="1975–1981", released="Apr 2022",
  art="o-crescent", tex="tex-moonlit", spine="Moon Knight",
 cover="Art/Moon-Knight/mk-o1.jpg",
  note="Everything before he had his own book, then the book. A two-issue hired thug in Werewolf by Night, a Defenders villain, a Hulk! magazine serial where Sienkiewicz worked the look out in black and white — and then Moon Knight #1–20, which is where Moench and Sienkiewicz stop imitating Batman and start doing the thing about four men in one head.")),
("Moon Knight Omnibus Vol 1 2", dict(id="mk-o2", title="Moon Knight Omnibus", vol="Vol. 2",
  creators="Doug Moench, Bill Sienkiewicz & Kevin Nowlan", era="1982–1990", released="May 2022",
  art="o-morpheus", tex="tex-crosshatch", chapterby="series", spine="Moon Knight",
 cover="Art/Moon-Knight/mk-o2.jpg",
  note="The end of the original run and the first attempt to restart it. Morpheus, Stained Glass Scarlet and Black Spectre close out #21–38; Fist of Khonshu revives him in 1985 for six issues and does not take. The rest is guest spots — Iron Man, Power Man and Iron Fist, three Marvel Fanfares — and a handful of Marvel Age pieces about the two relaunches.")),
("Moon Knight: Marc Spector Omnibus Vol 1 1", dict(id="spector-o1", title="Moon Knight: Marc Spector Omnibus", vol="Vol. 1",
  creators="Chuck Dixon, Sal Velluto & Ron Garney", era="1989–1992", released="Mar 2023",
  art="o-spector", tex="tex-halftone", spine="Marc Spector",
 cover="Art/Moon-Knight/spector-o1.jpg",
  note="His longest-running title, sixty issues of it, and this is the first thirty-four. Dixon puts him back on the street and then back in Burunda against Bushman, and the volume ends inside Round Robin — six issues of Amazing Spider-Man where he, Spidey and the Punisher are all chasing the same frame-up.")),
("Moon Knight: Marc Spector Omnibus Vol 1 2", dict(id="spector-o2", title="Moon Knight: Marc Spector Omnibus", vol="Vol. 2",
  creators="Terry Kavanagh, Ron Garney & Stephen Platt", era="1992–2000", released="Mar 2024",
  art="o-bushman", tex="tex-hieroglyph", spine="Marc Spector",
 cover="Art/Moon-Knight/spector-o2.jpg",
  note="#35–60 and then the wilderness. Infinity War, the Punisher, Doctor Doom, and the Platt issues that briefly made this the hottest-drawn book at Marvel. After it folds he only surfaces in fours: Resurrection War in 1998, High Strangeness in 1999, and Priest's Black Panther in 2000.")),
("Moon Knight by Huston, Benson & Hurwitz Omnibus Vol 1 1", dict(id="huston-o1", title="Moon Knight by Huston, Benson & Hurwitz Omnibus", vol="",
  creators="Charlie Huston, David Finch & Mike Benson", era="2006–2010", released="May 2022",
  art="o-vengeance", tex="tex-halftone", spine="By Huston & Benson",
 cover="Art/Moon-Knight/huston-o1.jpg",
  note="The 2006 relaunch, which is the one that decided he was horror rather than crime. Huston opens with a cripple in a wheelchair talking to a corpse; Benson and then Hurwitz push it further; Vengeance of the Moon Knight walks him back toward being a hero, and Shadowland takes it away again.")),
("Moon Knight: From The Dead Omnibus Vol 1 1", dict(id="ftd-o1", title="Moon Knight: From The Dead Omnibus", vol="",
  creators="Warren Ellis, Declan Shalvey & Brian Wood", era="2014–2015", released="Nov 2022",
  art="o-shalvey", tex="tex-moonlit", spine="From The Dead",
 cover="Art/Moon-Knight/ftd-o1.jpg",
  note="Seventeen issues, nearly all done-in-one. Ellis and Shalvey's first six are the ones people mean — the white suit, the sharp tailoring, and a page grammar the book never really got back after they left. Note the jump to get here: Bendis and Maleev's 2011 series has never been collected in omnibus.")),
("Moon Knight by Jed MacKay Omnibus Vol 1 1", dict(id="mackay-o1", title="Moon Knight by Jed MacKay Omnibus", vol="",
  creators="Jed MacKay, Alessandro Cappuccio & Federico Sabbatini", era="2021–2024", released="Oct 2024",
  art="o-midnight", tex="tex-hieroglyph", spine="By Jed MacKay",
 cover="Art/Moon-Knight/mackay-o1.jpg",
  note="The Midnight Mission — Marc running a walk-in shelter for people the weird has come for, and thirty issues of the argument about whether that counts as atonement. All of MacKay's run, both annuals and the Devil's Reign tie-in. Lemire's 2016 series and Bemis's after it are the gap in front of it; neither has an omnibus.")),
]

# Nothing pending on this shelf.
PLACEHOLDERS = []

# Display order of the shelf, by id. A reading order, which on this shelf is
# also publication order -- the seven books tile the character's history end to
# end with only the two uncollected runs missing (see the notes on ftd-o1 and
# mackay-o1), so there is nothing to resequence.
SHELF = [
  "mk-o1", "mk-o2",
  "spector-o1", "spector-o2",
  "huston-o1", "ftd-o1", "mackay-o1",
]

PLACEHOLDER_PAGES = {}

# Series these books collect that the shared SERIES table in
# build_omnibus_data.py does not carry. Display names are the marvel.com form
# (name plus start year) rather than the wiki's volume number, because that is
# what link_issues.py matches on -- nine volumes of "Moon Knight" is exactly the
# reused-title case its tiebreak() exists for. Years are the catalog's own:
# Moon Knight (1980 - 1984), (1985), (1999), (2006 - 2009), (2014 - 2015),
# (2021 - 2023).
SERIES_EXTRA = {
 "Moon Knight Vol 1":                                  ("mk1",    "Moon Knight (1980)"),
 "Moon Knight Vol 2":                                  ("mk2",    "Moon Knight (1985)"),
 "Moon Knight Vol 3":                                  ("mk3",    "Moon Knight (1998)"),
 "Moon Knight Vol 4":                                  ("mk4",    "Moon Knight (1999)"),
 "Moon Knight Vol 5":                                  ("mk5",    "Moon Knight (2006)"),
 "Moon Knight Vol 7":                                  ("mk7",    "Moon Knight (2014)"),
 "Moon Knight Vol 9":                                  ("mk9",    "Moon Knight (2021)"),
 "Moon Knight Annual Vol 1":                           ("mkann",  "Moon Knight Annual (2007)"),
 "Moon Knight Annual Vol 3":                           ("mkann3", "Moon Knight Annual (2022)"),
 "Moon Knight Annual Vol 4":                           ("mkann4", "Moon Knight Annual (2023)"),
 "Moon Knight Special Vol 1":                          ("mksp",   "Moon Knight Special"),
 "Moon Knight: Divided We Fall Vol 1":                 ("mkdwf",  "Moon Knight: Divided We Fall"),
 "Moon Knight: Silent Knight Vol 1":                   ("mksk",   "Moon Knight: Silent Knight"),
 "Marc Spector: Moon Knight Vol 1":                    ("msmk",   "Marc Spector: Moon Knight"),
 "Vengeance of the Moon Knight Vol 1":                 ("vmk",    "Vengeance of the Moon Knight"),
 "Shadowland: Moon Knight Vol 1":                      ("slmk",   "Shadowland: Moon Knight"),
 "Devil's Reign: Moon Knight Vol 1":                   ("drmk",   "Devil's Reign: Moon Knight"),
 "Werewolf by Night Vol 1":                            ("wbn",    "Werewolf by Night"),
 "Marvel Spotlight Vol 1":                             ("mspot",  "Marvel Spotlight"),
 "Marvel Preview Vol 1":                               ("mprev",  "Marvel Preview"),
 "Defenders Vol 1":                                    ("defs",   "Defenders"),
 "Hulk! Vol 1":                                        ("hulkmag","Hulk! Magazine"),
 "Power Man and Iron Fist Vol 1":                      ("pmif",   "Power Man and Iron Fist"),
 "Solo Avengers Vol 1":                                ("solav",  "Solo Avengers"),
 "Marvel Age Vol 1":                                   ("mage",   "Marvel Age"),
 "Big Shots Spotlight Vol 1":                          ("bshot",  "Big Shots Spotlight"),
 "Punisher Annual Vol 1":                              ("punann", "Punisher Annual"),
 "Black Panther Vol 3":                                ("bp98",   "Black Panther (1998)"),
 "Avengers Vol 8":                                     ("av18",   "Avengers (2018)"),
}

# Reused verbatim from the other shelves' own SERIES_EXTRA. A hero only ever
# sees the shared SERIES table plus its OWN extras, so a series another shelf
# already carries has to be repeated here -- with exactly the same short code,
# because the marvel.com id store is shared and the same series must key the
# same way on every shelf. (autocode() would reuse them anyway; these are
# written out so the codes are readable next to the ones they sit beside.)
SERIES_EXTRA.update({
 "Marvel Fanfare Vol 1":                               ("mfan",   "Marvel Fanfare"),
 "Marvel Super-Heroes Vol 2":                          ("msh2",   "Marvel Super-Heroes (1990)"),
 "Marvel Age Annual Vol 1":                            ("maan",   "Marvel Age Annual"),
 "Iron Man Vol 1":                                     ("im",     "Iron Man"),
})
