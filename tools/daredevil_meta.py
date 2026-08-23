# The hand-written half of the Daredevil shelf. Same shape as omnibus_meta.py,
# hulk_meta.py, ff_meta.py, wolverine_meta.py and moonknight_meta.py -- ORDER
# (wiki-backed), PLACEHOLDERS (tiles with no contents), SHELF (display order by
# id), PLACEHOLDER_PAGES, and SERIES_EXTRA for the series the shared SERIES
# table in build_omnibus_data.py does not already carry.
#
# Scope: Matt Murdock's own books. The wiki lists twenty Daredevil-family
# omnibuses; seventeen are here. Three are deliberately off, and the last two
# were the user's call rather than a rule:
#
#   * Daredevil Omnibus Vol. 4 is solicited for September 2026 and has not been
#     printed -- see "A shelf holds books you can actually buy" in CLAUDE.md.
#     Its entry stays in daredevil_contents_raw.json so re-adding it next month
#     is an edit here plus a regenerate, not a fresh wiki pull.
#   * Elektra by Frank Miller Omnibus is Elektra's book, not Matt's -- the same
#     reasoning that keeps She-Hulk off the Hulk shelf and Laura Kinney off
#     Wolverine's. Elektra: Assassin and Elektra Lives Again are hers; Matt is
#     barely in either.
#   * Devil's Reign Omnibus is a line-wide event -- X-Men, Winter Soldier,
#     Spider-Woman, Superior Four and Villains for Hire tie-ins -- so it is off
#     for the same reason Heroes Reborn is off the FF shelf. Nothing is lost:
#     its Daredevil half (Devil's Reign #1-6, Omega, Woman Without Fear #1-3)
#     is printed inside the Zdarsky Vol. 2 omnibus, which is on the shelf.
#
# `chapterby` overrides the automatic chaptering heuristic on four volumes.

ORDER = [
("Daredevil Omnibus Vol 1 1", dict(id="dd-o1", title="Daredevil Omnibus", vol="Vol. 1",
  creators="Stan Lee, Wally Wood & Gene Colan", era="1964–1968", released="Feb 2017",
  art="o-hornhead", tex="tex-halftone", spine="Daredevil",
 cover="Art/Daredevil/dd-o1.jpg",
  note="The yellow suit, and then the red one. Bill Everett draws #1 and vanishes; Wally Wood arrives at #5, redesigns the costume into the thing everyone pictures, and leaves by #11. What holds it together is Gene Colan from #20 on — a fluid, cinematic pencil nobody else at Marvel had, and the reason this run outlived its own scripts."),),
("Daredevil Omnibus Vol 1 2", dict(id="dd-o2", title="Daredevil Omnibus", vol="Vol. 2",
  creators="Roy Thomas, Gene Colan & Barry Windsor-Smith", era="1968–1971", released="May 2023",
  art="o-crimson", tex="tex-halftone", spine="Daredevil",
 cover="Art/Daredevil/dd-o2.jpg",
  note="Colan's run at full stretch. The Jester frames Matt for murder, Starr Saxon works out who he is, and the book spends an embarrassing stretch on the Mike Murdock twin-brother lie before killing it off. Roy Thomas takes over the scripts; the two Iron Man issues at the end are the Zodiac crossover."),),
("Daredevil Omnibus Vol 1 3", dict(id="dd-o3", title="Daredevil Omnibus", vol="Vol. 3",
  creators="Gerry Conway, Steve Gerber & Gene Colan", era="1970–1975", released="Apr 2024",
  art="o-crimson", tex="tex-crosshatch", spine="Daredevil",
 cover="Art/Daredevil/dd-o3.jpg",
  note="Daredevil and the Black Widow, which is what the cover said for four years — Matt leaves New York for San Francisco and the book becomes a two-hander. Natasha's own Amazing Adventures strips are collected in front of it, so you get her solo run and the partnership it fed into."),),
("Daredevil Omnibus Vol 1 4", dict(id="dd-o4", title="Daredevil Omnibus", vol="Vol. 4",
  creators="Marv Wolfman, Jim Shooter & Gene Colan", era="1975–1979", released="Sep 2026",
  art="o-kitchen", tex="tex-halftone", spine="Daredevil",
 cover="Art/Daredevil/dd-o4.jpg",
  note="Ships September 2026 \u2014 on the shelf ahead of that because its contents, links and jacket are all real. The stretch nobody collects: Matt back in New York, Bullseye created, the Death-Stalker and the Purple Man, and Klaus Janson arriving as inker two issues before the book changes forever. It ends on #158, Frank Miller's first issue, which the Miller & Janson volume then opens with."),),
("Daredevil by Miller and Janson Omnibus Vol 1 1", dict(id="miller-o1", title="Daredevil by Miller & Janson Omnibus", vol="",
  creators="Frank Miller, Klaus Janson & Roger McKenzie", era="1979–1983", released="Mar 2007",
  art="o-kitchen", tex="tex-crosshatch", spine="Miller & Janson",
 cover="Art/Daredevil/miller-o1.jpg",
  note="The run that decided what Daredevil is. Miller arrives as the artist on #158 under Roger McKenzie, takes the writing at #168 with Elektra, and by the time he leaves at #191 the book is about Hell's Kitchen, the Hand, and Wilson Fisk. #162 is skipped because it is a Ditko fill-in, not theirs. Note it opens on #158, which Omnibus Vol. 4 also holds — that issue is Miller's first and both books want it, so it is the shelf's only overlap."),),
("Daredevil by Frank Miller Omnibus Companion Vol 1 1", dict(id="millerc-o1", title="Daredevil by Frank Miller Omnibus Companion", vol="",
  creators="Frank Miller, David Mazzucchelli & John Romita Jr.", era="1979–1993", released="Dec 2007",
  art="o-borna", tex="tex-brick", chapterby="series", spine="Miller Companion",
 cover="Art/Daredevil/millerc-o1.jpg",
  note="Everything Miller wrote about Matt without also drawing the monthly. The centre of it is Born Again — Karen Page sells his identity for a fix and Fisk takes him apart piece by piece — which is the best eight issues anyone has done with this character. Around it: Love and War, the Man Without Fear origin mini with Romita Jr., and two early Spectacular Spider-Man crossovers."),),
("Daredevil by Nocenti & Romita Jr. Omnibus Vol 1 1", dict(id="nocenti-o1", title="Daredevil by Nocenti & Romita Jr. Omnibus", vol="Vol. 1",
  creators="Ann Nocenti & John Romita Jr.", era="1986–1989", released="Mar 2025",
  art="o-nocenti", tex="tex-halftone", spine="Nocenti & JRJR",
 cover="Art/Daredevil/nocenti-o1.jpg",
  note="Nocenti picks the book up straight out of Born Again and takes it somewhere nobody expected — Inferno, Mephisto, the Kingpin's factory towns, and a running argument about what a blind Catholic lawyer is doing punching people. Typhoid Mary arrives at #254. Daredevil #192–218 and #220–225, the Denny O'Neil run in between, has never been omnibused."),),
("Daredevil by Nocenti & Romita Jr. Omnibus Vol 1 2", dict(id="nocenti-o2", title="Daredevil by Nocenti & Romita Jr. Omnibus", vol="Vol. 2",
  creators="Ann Nocenti, John Romita Jr. & Lee Weeks", era="1989–1994", released="Jul 2026",
  art="o-nocenti", tex="tex-crosshatch", chapterby="series", spine="Nocenti & JRJR",
 cover="Art/Daredevil/nocenti-o2.jpg",
  note="The back half, and it gets stranger — Matt loses the costume, the memory and most of the supporting cast, and the run ends up in Hell with Mephisto. The tail is the Marvel Comics Presents backups Nocenti kept writing afterwards, plus two Spectacular Spider-Man issues and a Christmas story."),),
("Daredevil by Brian Michael Bendis Omnibus Vol 1 1", dict(id="bendis-o1", title="Daredevil by Brian Michael Bendis Omnibus", vol="Vol. 1",
  creators="Brian Michael Bendis & Alex Maleev", era="2001–2004", released="Aug 2008",
  art="o-noir", tex="tex-rain", spine="By Bendis",
 cover="Art/Daredevil/bendis-o1.jpg",
  note="Bendis and Maleev do crime fiction: a tabloid prints Matt's name on the front page in #32 and the next fifty issues are about living with that. Only the Bendis issues are here, so #20–25 (Bob Gale) and #51–55 (David Mack's Echo) are skipped. Getting here means jumping Daredevil #292–380 and the whole Marvel Knights relaunch by Kevin Smith and Mack — none of it has an omnibus."),),
("Daredevil by Brian Michael Bendis Omnibus Vol 1 2", dict(id="bendis-o2", title="Daredevil by Brian Michael Bendis Omnibus", vol="Vol. 2",
  creators="Brian Michael Bendis & Alex Maleev", era="2001–2006", released="Dec 2009",
  art="o-noir", tex="tex-rain", spine="By Bendis",
 cover="Art/Daredevil/bendis-o2.jpg",
  note="Matt declares himself Kingpin of Hell's Kitchen, marries Milla Donovan, and ends the run in a federal prison cell. The Eisner-winning half. Three Ultimate Marvel Team-Up issues and a What If about Karen Page surviving Bendis's own best-known scene are collected after it."),),
("Daredevil by Ed Brubaker Omnibus Vol 1 1", dict(id="bru-o1", title="Daredevil by Ed Brubaker Omnibus", vol="Vol. 1",
  creators="Ed Brubaker & Michael Lark", era="2006–2008", released="May 2009",
  art="o-noir", tex="tex-brick", spine="By Brubaker",
 cover="Art/Daredevil/bru-o1.jpg",
  note="Brubaker and Lark pick the book up mid-sentence with Matt in Ryker's, which is the best possible way to inherit a run this good. The Devil in Cell-Block D, then Europe, then back to a Hell's Kitchen that has moved on without him. Lark's storytelling is tighter than Maleev's and the book loses nothing."),),
("Daredevil by Ed Brubaker Omnibus Vol 1 2", dict(id="bru-o2", title="Daredevil by Ed Brubaker Omnibus", vol="Vol. 2",
  creators="Ed Brubaker, Michael Lark & Greg Rucka", era="2007–2009", released="Jun 2010",
  art="o-noir", tex="tex-crosshatch", spine="By Brubaker",
 cover="Art/Daredevil/bru-o2.jpg",
  note="Lady Bullseye, Master Izo, and the long slide that puts the Hand's offer in front of Matt at exactly the moment he has nothing left to say no with. Ends on #500 and the decision that starts Shadowland."),),
("Daredevil: Shadowland Omnibus Vol 1 1", dict(id="shadow-o1", title="Daredevil: Shadowland Omnibus", vol="",
  creators="Andy Diggle, Antony Johnston & Roberto De La Torre", era="2009–2011", released="Feb 2018",
  art="o-shadow", tex="tex-brick", chapterby="series", spine="Shadowland",
 cover="Art/Daredevil/shadow-o1.jpg",
  note="Matt takes the Hand, builds a fortress on top of Hell's Kitchen and kills Bullseye in it. The whole event with every tie-in — Elektra, Ghost Rider, Spider-Man, Moon Knight, Power Man, Blood on the Streets — plus the Diggle run that leads in and Daredevil: Reborn, which is Matt walking out into New Mexico afterwards to work out whether he is still worth anything."),),
("Daredevil by Mark Waid Omnibus Vol 1 1", dict(id="waid-o1", title="Daredevil by Mark Waid Omnibus", vol="Vol. 1",
  creators="Mark Waid, Paolo Rivera & Marcos Martín", era="2011–2013", released="Mar 2017",
  art="o-devil", tex="tex-radar", spine="By Mark Waid",
 cover="Art/Daredevil/waid-o1.jpg",
  note="The tonal reset, and the reason it worked: Waid stops writing a man in a permanent depressive episode and starts writing a man performing not being in one. Rivera and Martín render the radar sense as something beautiful rather than something grim. The Omega Drive arc brings in Spider-Man and the Punisher."),),
("Daredevil by Mark Waid Omnibus Vol 1 2", dict(id="waid-o2", title="Daredevil by Mark Waid Omnibus", vol="Vol. 2",
  creators="Mark Waid & Chris Samnee", era="2013–2015", released="Mar 2018",
  art="o-devil", tex="tex-radar", spine="By Mark Waid",
 cover="Art/Daredevil/waid-o2.jpg",
  note="Samnee takes over and the book wins an Eisner for it. Foggy's cancer, the Sons of the Serpent, the identity finally becoming public on Matt's own terms, and then the move to San Francisco for the 2014 relaunch — the second time this character has answered a bad year by leaving New York."),),
("Daredevil by Charles Soule Omnibus Vol 1 1", dict(id="soule-o1", title="Daredevil by Charles Soule Omnibus", vol="",
  creators="Charles Soule, Ron Garney & Goran Sudžuka", era="2015–2019", released="Aug 2021",
  art="o-crimson", tex="tex-rain", spine="By Charles Soule",
 cover="Art/Daredevil/soule-o1.jpg",
  note="Soule is a lawyer, and it shows — this is the run that takes the day job seriously, with Matt as an ADA prosecuting the people he used to punch. Garney's black-and-red art strips the palette down to almost nothing. Runs from the 2015 relaunch through the renumbering back to #595 and out at #612."),),
("Daredevil by Chip Zdarsky Omnibus Vol 1 1", dict(id="zdarsky-o1", title="Daredevil by Chip Zdarsky Omnibus", vol="Vol. 1",
  creators="Chip Zdarsky, Marco Checchetto & Jorge Fornés", era="2019–2021", released="Jul 2024",
  art="o-borna", tex="tex-brick", spine="By Chip Zdarsky",
 cover="Art/Daredevil/zdarsky-o1.jpg",
  note="Matt kills a man in the second issue and the next fifty are the sentence. Zdarsky and Checchetto write the best long-form Daredevil since Bendis: prison, Elektra taking the costume, Fisk as mayor of New York, and a book that keeps insisting the Catholic guilt was always the point rather than the decoration."),),
("Daredevil by Chip Zdarsky Omnibus Vol 1 2", dict(id="zdarsky-o2", title="Daredevil by Chip Zdarsky Omnibus", vol="Vol. 2",
  creators="Chip Zdarsky, Marco Checchetto & Rafael De Latorre", era="2021–2023", released="Dec 2024",
  art="o-shadow", tex="tex-crosshatch", chapterby="series", spine="By Chip Zdarsky",
 cover="Art/Daredevil/zdarsky-o2.jpg",
  note="The end of it. Devil's Reign is here in full — Fisk outlawing costumed heroes from City Hall — and then the 2022 relaunch, where Matt and Elektra run a Hand of their own and the run walks itself into the ending it has been aiming at since the first issue. Woman Without Fear is Elektra's half of the same story."),),
]

# Nothing pending on this shelf.
PLACEHOLDERS = []

# Display order of the shelf, by id. A reading order, which on this shelf runs
# with publication order -- the seventeen books tile the character's history in
# sequence, and the only resequencing worth doing (the Miller Companion after
# the Miller run it comments on, rather than at its 1993 end date) is already
# what publication order gives.
SHELF = [
  "dd-o1", "dd-o2", "dd-o3", "dd-o4",
  "miller-o1", "millerc-o1",
  "nocenti-o1", "nocenti-o2",
  "bendis-o1", "bendis-o2",
  "bru-o1", "bru-o2",
  "shadow-o1",
  "waid-o1", "waid-o2",
  "soule-o1",
  "zdarsky-o1", "zdarsky-o2",
]

PLACEHOLDER_PAGES = {}

# Series these books collect that the shared SERIES table in
# build_omnibus_data.py does not carry. Display names are the marvel.com form
# (name plus start year) rather than the wiki's volume number, because that is
# what link_issues.py matches on -- and "Daredevil" is exactly the reused-title
# case its tiebreak() exists for: marvel.com carries seven of them. Years are
# the catalog's own: Daredevil (1964 - 1998), (1998 - 2011), (2011 - 2014),
# (2014 - 2015), (2015 - 2019), (2019 - 2022), (2022 - 2023).
#
# Note "Daredevil Vol 1" is overriding the shared table's ("dd", "Daredevil")
# to add the year. The CODE has to stay `dd` -- it is a saved-progress key and
# the marvel_ids.json store is shared -- but the display name is free, and
# naming the year is tiebreak()'s strongest rule.
SERIES_EXTRA = {
 "Ghost Rider Vol 2":                                  ("gr2",    "Ghost Rider (1973)"),
 "Daredevil Vol 1":                                    ("dd",     "Daredevil (1964)"),
 "Daredevil Vol 2":                                    ("dd2",    "Daredevil (1998)"),
 "Daredevil Vol 3":                                    ("dd3",    "Daredevil (2011)"),
 "Daredevil Vol 4":                                    ("dd4",    "Daredevil (2014)"),
 "Daredevil Vol 5":                                    ("dd5",    "Daredevil (2015)"),
 "Daredevil Vol 6":                                    ("dd6",    "Daredevil (2019)"),
 "Daredevil Vol 7":                                    ("dd7",    "Daredevil (2022)"),
 "Daredevil Annual Vol 1":                             ("ddann",  "Daredevil Annual (1967)"),
 "Daredevil Annual Vol 2":                             ("ddann2", "Daredevil Annual (2007)"),
 "Daredevil Annual Vol 4":                             ("ddann4", "Daredevil Annual (2016)"),
 "Daredevil Annual Vol 6":                             ("ddann6", "Daredevil Annual (2020)"),
 "Daredevil: The Man Without Fear Vol 1":              ("ddmwf",  "Daredevil: The Man Without Fear"),
 "Daredevil: Reborn Vol 1":                            ("ddreb",  "Daredevil: Reborn"),
 "Daredevil: Woman Without Fear Vol 1":                ("ddwwf",  "Daredevil: Woman Without Fear"),
 "Daredevil Blood of the Tarantula Vol 1":             ("ddbot",  "Daredevil: Blood of the Tarantula"),
 "Daredevil/Punisher: Seventh Circle Infinite Comic Vol 1": ("ddp7c", "Daredevil/Punisher"),
 "Dark Reign: The List - Daredevil Vol 1":             ("drlist", "Dark Reign: The List - Daredevil"),
 "Shadowland Vol 1":                                   ("shl",    "Shadowland"),
 "Shadowland: After the Fall Vol 1":                   ("shlatf", "Shadowland: After the Fall"),
 "Shadowland: Blood on the Streets Vol 1":             ("shlbos", "Shadowland: Blood on the Streets"),
 "Shadowland: Bullseye Vol 1":                         ("shlbul", "Shadowland: Bullseye"),
 "Shadowland: Daughters of the Shadow Vol 1":          ("shldos", "Shadowland: Daughters of the Shadow"),
 "Shadowland: Elektra Vol 1":                          ("shlele", "Shadowland: Elektra"),
 "Shadowland: Ghost Rider Vol 1":                      ("shlgr",  "Shadowland: Ghost Rider"),
 "Shadowland: Power Man Vol 1":                        ("shlpm",  "Shadowland: Power Man"),
 "Shadowland: Spider-Man Vol 1":                       ("shlsm",  "Shadowland: Spider-Man"),
 "Devil's Reign Vol 1":                                ("dvr",    "Devil's Reign"),
 "Devil's Reign: Omega Vol 1":                         ("dvrom",  "Devil's Reign: Omega"),
 "Amazing Adventures Vol 2":                           ("aa2",    "Amazing Adventures (1970)"),
 "Avenging Spider-Man Vol 1":                          ("avsm",   "Avenging Spider-Man"),
 "Indestructible Hulk Vol 1":                          ("ihulk",  "Indestructible Hulk"),
 "Punisher Vol 2":                                     ("pun2",   "Punisher (1987)"),
 "Punisher Vol 9":                                     ("pun9",   "Punisher (2011)"),
 "Thunderbolts Vol 2":                                 ("tbolt2", "Thunderbolts (2006)"),
 "Ultimate Marvel Team Up Vol 1":                      ("umtu",   "Ultimate Marvel Team-Up"),
 "What If Karen Page Had Lived? Vol 1":                ("wikp",   "What If Karen Page Had Lived?"),
 "All-New, All-Different Point One Vol 1":             ("anadp1", "All-New, All-Different Point One"),
}

# Reused verbatim from the other shelves' own SERIES_EXTRA. A hero only ever
# sees the shared SERIES table plus its OWN extras, so a series another shelf
# already carries has to be repeated here -- with exactly the same short code,
# because the marvel.com id store is shared and the same series must key the
# same way on every shelf. (autocode() would reuse them anyway; these are
# written out so the codes are readable next to the ones they sit beside.)
SERIES_EXTRA.update({
 "Avengers Vol 1":                                     ("av",     "Avengers"),
 "Marvel Graphic Novel Vol 1":                         ("mgn",    "Marvel Graphic Novel"),
 "Marvel Holiday Special Vol 1":                       ("mhs",    "Marvel Holiday Special"),
 "Big Shots Spotlight Vol 1":                          ("bshot",  "Big Shots Spotlight"),
 "Iron Man Vol 1":                                     ("im",     "Iron Man"),
 "Shadowland: Moon Knight Vol 1":                      ("slmk",   "Shadowland: Moon Knight"),
})
