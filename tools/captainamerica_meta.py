# The hand-written half of the Captain America shelf. Same shape as
# omnibus_meta.py and the rest -- ORDER (wiki-backed), PLACEHOLDERS (tiles with
# no contents), SHELF (display order by id), PLACEHOLDER_PAGES, and SERIES_EXTRA
# for the series the shared SERIES table in build_omnibus_data.py does not carry.
#
# Scope: Steve Rogers' own title, from Captain America Comics #1 in 1941 to the
# end of the Coates run. Twenty-two volumes, and everything on the shelf has
# shipped -- unusually for this project there is no unreleased tile here at all.
#
# Two things were deliberately left off, and both are the "different book"
# call rather than a rule:
#
#   * INVADERS OMNIBUS is the Invaders' own title, a WWII team book with Namor
#     and the original Human Torch. Same call that keeps Marvel Two-In-One off
#     the FF shelf and Marvel Team-Up off Spider-Man's.
#   * CAPTAIN AMERICA BY JACK KIRBY OMNIBUS is a strict SUBSET of Captain
#     America Omnibus Vol. 4 -- all 25 of its issues are in Vol. 4, which adds
#     FOOM #11 on top. Keeping both would put 25 duplicate issues on the shelf
#     and two near-identical tiles next to each other for no extra reading. Its
#     entry stays in captainamerica_contents_raw.json, so putting it back is an
#     edit here plus a regenerate.
#
# One inclusion is genuinely arguable and is flagged rather than hidden:
# BLACK WIDOW & CAPTAIN AMERICA BY WAID & SAMNEE is 12 Black Widow issues and
# 10 of Captain America's own title. It is on the shelf because those ten --
# Captain America (2017) #695-704, Waid's run -- are collected in omnibus
# nowhere else, so dropping it opens a hole rather than removing a duplicate.
# If it should go, that is a one-line edit to ORDER and SHELF.
#
# Two enumeration traps this shelf hit, both worth knowing before adding a hero:
#   * `apprefix=Captain America` MISSES books whose title starts elsewhere.
#     DEATH OF CAPTAIN AMERICA OMNIBUS is exactly the volume that closes the
#     Captain America (2004) #26-42 gap, and a prefix sweep never sees it.
#     Search as well as enumerate.
#   * The same book can have two page titles. This one is filed as both
#     "Captain America & Black Widow..." (no contents) and "Black Widow &
#     Captain America..." (the real one). Take the page that has ReprintOf
#     fields.

ORDER = [
("Golden Age Captain America Omnibus Vol 1 1", dict(id="ga-o1", title="Golden Age Captain America Omnibus", vol="Vol. 1",
  creators="Joe Simon & Jack Kirby", era="1941–1942", released="Feb 2014",
  art="o-goldenage", tex="tex-halftone", spine="Golden Age",
 cover="Art/Captain-America/ga-o1.jpg",
  note="Where he starts: Simon and Kirby, twelve anthology issues, and a cover of Cap punching Hitler that ran a year before America entered the war. Each issue is a full book rather than a single story, so this is 12 issues and a great deal of comics.")),
("Golden Age Captain America Omnibus Vol 1 2", dict(id="ga-o2", title="Golden Age Captain America Omnibus", vol="Vol. 2",
  creators="Stan Lee, Al Avison & Syd Shores", era="1942–1943", released="Jun 2021",
  art="o-goldenage", tex="tex-crosshatch", spine="Golden Age",
 cover="Art/Captain-America/ga-o2.jpg",
  note="Simon and Kirby leave after #10 and the book carries on without them — this is #13–24, the stretch where a nineteen-year-old Stan Lee is writing some of it. The Golden Age run goes to #75 and the omnibus line stops here, so everything after 1943 is uncollected in this format.")),
("Captain America Omnibus Vol 1 1", dict(id="ca-o1", title="Captain America Omnibus", vol="Vol. 1",
  creators="Stan Lee & Jack Kirby", era="1964–1969", released="May 2011",
  art="o-shield", tex="tex-halftone", spine="Captain America",
 cover="Art/Captain-America/ca-o1.jpg",
  note="The thaw. Tales of Suspense #59–99 is Cap sharing a book with Iron Man ten pages at a time, and it is where Kirby works out what a Captain America fight scene looks like; then the split, and Captain America #100 onward as his own title again. The Red Skull, the Cosmic Cube, and Bucky's death told properly for the first time.")),
("Captain America Omnibus Vol 1 2", dict(id="ca-o2", title="Captain America Omnibus", vol="Vol. 2",
  creators="Stan Lee, Gene Colan & John Romita Sr.", era="1969–1972", released="Mar 2016",
  art="o-shield", tex="tex-crosshatch", spine="Captain America",
 cover="Art/Captain-America/ca-o2.jpg",
  note="#114–148, and the book stops being a war comic. Cap and the Falcon become a partnership and the title changes to say so; Colan draws New York like a crime film, and the stories start being about whether the man out of time has anything to say about 1971.")),
("Captain America Omnibus Vol 1 3", dict(id="ca-o3", title="Captain America Omnibus", vol="Vol. 3",
  creators="Steve Englehart, Sal Buscema & Frank Robbins", era="1972–1975", released="Jul 2021",
  art="o-secret", tex="tex-halftone", spine="Captain America",
 cover="Art/Captain-America/ca-o3.jpg",
  note="#149–192, which is mostly Englehart, and contains the single most famous thing anyone has done with the character: the Secret Empire story, where the trail of a government conspiracy leads to the White House and Steve Rogers quits being Captain America over it. Published while Watergate was on television.")),
("Captain America Omnibus Vol 1 4", dict(id="ca-o4", title="Captain America Omnibus", vol="Vol. 4",
  creators="Jack Kirby", era="1976–1977", released="Mar 2024",
  art="o-kirbycap", tex="tex-fourdot", spine="Captain America",
 cover="Art/Captain-America/ca-o4.jpg",
  note="Kirby comes back to the character he made and writes as well as draws him — #193–214, the Madbomb, the Swine, Arnim Zola, and the Bicentennial Battles treasury. Note this supersedes the separate Captain America by Jack Kirby Omnibus, which holds the same issues minus FOOM #11.")),
("Captain America Omnibus Vol 1 5", dict(id="ca-o5", title="Captain America Omnibus", vol="Vol. 5",
  creators="Roger Stern, John Byrne & Roger McKenzie", era="1978–1981", released="Jul 2026",
  art="o-shield", tex="tex-crosshatch", spine="Captain America",
 cover="Art/Captain-America/ca-o5.jpg",
  note="#215–260. The run people mean when they say Stern and Byrne only lasted nine issues but fixed the character — they give him an apartment, a job and a reason to be Steve Rogers, and the book keeps that shape after they leave.")),
("Captain America by Mark Gruenwald Omnibus Vol 1 1", dict(id="gru-o1", title="Captain America by Mark Gruenwald Omnibus", vol="Vol. 1",
  creators="Mark Gruenwald, Paul Neary & Kieron Dwyer", era="1985–1989", released="Jul 2024",
  art="o-cap80s", tex="tex-halftone", spine="By Gruenwald",
 cover="Art/Captain-America/gru-o1.jpg",
  note="Ten years on the book, which is still the longest anyone has managed. This is #307–350: the Scourge of the Underworld, Diamondback, and the Captain — the year the government takes the identity off Steve and gives it to John Walker, which is the story every screen version has borrowed since.")),
("Captain America by Mark Gruenwald Omnibus Vol 1 2", dict(id="gru-o2", title="Captain America by Mark Gruenwald Omnibus", vol="Vol. 2",
  creators="Mark Gruenwald, Kieron Dwyer & Ron Lim", era="1989–1991", released="Jul 2025",
  art="o-cap80s", tex="tex-crosshatch", spine="By Gruenwald",
 cover="Art/Captain-America/gru-o2.jpg",
  note="#351–386, plus the Adventures of Captain America retelling of the origin. The Red Skull is back with a body he did not have before, Crossbones arrives, and Bloodstone hunts through a book that has settled into being a very well-made superhero comic every month.")),
("Captain America by Mark Gruenwald Omnibus Vol 1 3", dict(id="gru-o3", title="Captain America by Mark Gruenwald Omnibus", vol="Vol. 3",
  creators="Mark Gruenwald, Rik Levins & Dave Hoover", era="1991–1993", released="Jul 2026",
  art="o-cap80s", tex="tex-fourdot", spine="By Gruenwald",
 cover="Art/Captain-America/gru-o3.jpg",
  note="#387–418, Blood and Glory with the Punisher, and U.S.Agent's own mini. Operation: Galactic Storm runs through the middle of it. The run goes on to #443 and the omnibus line stops at #418, so the last two years of Gruenwald — Fighting Chance, and Cap's body failing him — are not collected here.")),
("Captain America by Mark Waid, Ron Garney and Andy Kubert Omnibus Vol 1 1", dict(id="waid-o1", title="Captain America by Waid, Garney & Kubert Omnibus", vol="",
  creators="Mark Waid, Ron Garney & Andy Kubert", era="1995–1998", released="Dec 2017",
  art="o-heroes", tex="tex-halftone", chapterby="series", spine="By Waid",
 cover="Art/Captain-America/waid-o1.jpg",
  note="Two runs with Heroes Reborn in the gap between them. Waid and Garney take #444–454 and immediately bring Sharon Carter back from the dead; then the book is cancelled for the Heroes Reborn year, and they return for Captain America (1998) #1–23 plus the Sentinel of Liberty mini. The Heroes Reborn year itself is a different book and is not here.")),
("Captain America by Dan Jurgens Omnibus Vol 1 1", dict(id="jurgens-o1", title="Captain America by Dan Jurgens Omnibus", vol="",
  creators="Dan Jurgens & Andy Kubert", era="2000–2002", released="Aug 2021",
  art="o-heroes", tex="tex-crosshatch", spine="By Jurgens",
 cover="Art/Captain-America/jurgens-o1.jpg",
  note="Captain America (1998) #25–50, which finishes that volume. Jurgens writes and draws most of it — Protocide, the Red Skull's return, and a Korea story that is the book at its best. After this the title relaunches twice more before anything is collected again.")),
("Captain America by Ed Brubaker Omnibus Vol 1 1", dict(id="bru-o1", title="Captain America by Ed Brubaker Omnibus", vol="",
  creators="Ed Brubaker, Steve Epting & Michael Lark", era="2005–2007", released="Sep 2007",
  art="o-wintersoldier", tex="tex-crosshatch", spine="By Brubaker",
 cover="Art/Captain-America/bru-o1.jpg",
  note="Captain America (2004) #1–25, and the run that reset the character for twenty years. Brubaker writes it as a spy thriller, Epting draws it like one, and the thing everyone said could not be done — bringing Bucky back — turns out to be the best idea anyone had had about Cap in decades.")),
("Death of Captain America Omnibus Vol 1 1", dict(id="death-o1", title="Death of Captain America Omnibus", vol="",
  creators="Ed Brubaker & Steve Epting", era="2007–2008", released="Dec 2009",
  art="o-mourning", tex="tex-crosshatch", spine="Death of Cap",
 cover="Art/Captain-America/death-o1.jpg",
  note="#25–42, straight on from the Brubaker volume, which is why #25 is in both books. Steve is shot on the courthouse steps and the book keeps going for eighteen issues about everyone else — Bucky, Sharon, the Falcon, the Red Skull — which is the trick of it: the title character is dead and it is still the best comic Marvel is publishing.")),
("Captain America Lives! Omnibus Vol 1 1", dict(id="lives-o1", title="Captain America Lives! Omnibus", vol="",
  creators="Ed Brubaker, Butch Guice & Bryan Hitch", era="2008–2010", released="Mar 2011",
  art="o-mourning", tex="tex-halftone", chapterby="series", spine="Cap Lives!",
 cover="Art/Captain-America/lives-o1.jpg",
  note="#43–601 and the Reborn mini — how they undid it. Bucky is wearing the costume and carrying a gun, which the book takes seriously as a problem, and Steve is unstuck in his own timeline rather than simply dead. Note the numbering jumps to #600 partway through: the title reverted to its original count for the anniversary.")),
("Captain America: The Trial of Captain America Omnibus Vol 1 1", dict(id="trial-o1", title="Captain America: The Trial of Captain America Omnibus", vol="",
  creators="Ed Brubaker, Butch Guice & Mitch Breitweiser", era="2010–2011", released="Dec 2014",
  art="o-wintersoldier", tex="tex-fourdot", chapterby="series", spine="The Trial",
 cover="Art/Captain-America/trial-o1.jpg",
  note="#602–619 and then Captain America (2011) #1–10, with Steve Rogers: Super-Soldier alongside. Bucky is put on trial for what he did as the Winter Soldier, which is the question the whole Brubaker run has been circling: whether a man is guilty of things done while he was someone else's weapon.")),
("Captain America: Return of the Winter Soldier Omnibus Vol 1 1", dict(id="rows-o1", title="Captain America: Return of the Winter Soldier Omnibus", vol="",
  creators="Ed Brubaker, Butch Guice & Chris Samnee", era="2011–2012", released="May 2015",
  art="o-wintersoldier", tex="tex-halftone", chapterby="series", spine="Return of WS",
 cover="Art/Captain-America/rows-o1.jpg",
  note="The end of Brubaker's eight years. Captain America and Bucky, the Fear Itself tie-ins, Captain America (2011) #11–19, and the whole Winter Soldier ongoing — fourteen issues of Bucky running black operations that Cap is not told about, which is the closest this run comes to a spy book with no superheroes in it at all.")),
("Captain America by Rick Remender Omnibus Vol 1 1", dict(id="rem-o1", title="Captain America by Rick Remender Omnibus", vol="",
  creators="Rick Remender, John Romita Jr. & Carlos Pacheco", era="2012–2015", released="Sep 2021",
  art="o-dimensionz", tex="tex-fourdot", chapterby="series", spine="By Remender",
 cover="Art/Captain-America/rem-o1.jpg",
  note="Captain America (2012) #1–25 and then All-New Captain America. Remender opens by stranding Steve in Dimension Z for a year of publishing, raising a child there, which is either the boldest thing anyone has done with the book or a very long detour depending on who you ask. It ends with the serum gone and Sam Wilson carrying the shield.")),
("Captain America by Nick Spencer Omnibus Vol 1 1", dict(id="spencer-o1", title="Captain America by Nick Spencer Omnibus", vol="Vol. 1",
  creators="Nick Spencer, Daniel Acuña & Jesus Saiz", era="2015–2016", released="Jan 2023",
  art="o-hydra", tex="tex-halftone", chapterby="series", spine="By Spencer",
 cover="Art/Captain-America/spencer-o1.jpg",
  note="Two Captains at once: Sam Wilson has the shield and a book about how much of America hates him for what he says with it, and Steve Rogers gets his youth back and a secret. Standoff runs through the middle. This is the setup for the thing everyone remembers, and it is better read as the argument it actually is than as the twist.")),
("Captain America by Nick Spencer Omnibus Vol 1 2", dict(id="spencer-o2", title="Captain America by Nick Spencer Omnibus", vol="Vol. 2",
  creators="Nick Spencer, Andrea Sorrentino & Daniel Acuña", era="2017–2018", released="May 2024",
  art="o-hydra", tex="tex-crosshatch", chapterby="series", spine="By Spencer",
 cover="Art/Captain-America/spencer-o2.jpg",
  note="Secret Empire, and the rest of both books around it. Cap has been a Hydra sleeper the whole time and wins; the story is about what the country does while he does it. Divisive on publication and still is. Ends with Generations and the restoration.")),
("Black Widow & Captain America by Waid & Samnee Omnibus Vol 1 1", dict(id="bwca-o1", title="Black Widow & Captain America by Waid & Samnee Omnibus", vol="",
  creators="Mark Waid & Chris Samnee", era="2016–2018", released="Mar 2026",
  art="o-heroes", tex="tex-fourdot", chapterby="series", spine="Waid & Samnee",
 cover="Art/Captain-America/bwca-o1.jpg",
  note="Half of this is Black Widow's book, and it is on the shelf anyway because the other half — Captain America (2017) #695–704 — is collected in omnibus nowhere else. Waid and Samnee put Steve back in the costume after Secret Empire and write ten issues of deliberately uncomplicated Captain America, which after the previous volume is the point.")),
("Captain America by Ta-Nehisi Coates Omnibus Vol 1 1", dict(id="coates-o1", title="Captain America by Ta-Nehisi Coates Omnibus", vol="",
  creators="Ta-Nehisi Coates, Leinil Francis Yu & Adam Kubert", era="2018–2021", released="Jul 2023",
  art="o-coates", tex="tex-crosshatch", spine="By Coates",
 cover="Art/Captain-America/coates-o1.jpg",
  note="Captain America (2018) #1–30, the whole run. Coates writes a Steve Rogers who has come out of Secret Empire with his reputation wrecked and no idea what the symbol is worth any more, and answers it slowly, through the Power Elite and a Red Skull who fights with rhetoric rather than a gun.")),
]

# Nothing pending on this shelf.
PLACEHOLDERS = []

# Display order, by id. A reading order, which on this shelf is also
# publication order of the material -- the character's own title from 1941 to
# 2021, with the uncollected stretches between volumes noted on the tiles.
SHELF = [
  "ga-o1", "ga-o2",
  "ca-o1", "ca-o2", "ca-o3", "ca-o4", "ca-o5",
  "gru-o1", "gru-o2", "gru-o3",
  "waid-o1", "jurgens-o1",
  "bru-o1", "death-o1", "lives-o1", "trial-o1", "rows-o1",
  "rem-o1",
  "spencer-o1", "spencer-o2",
  "bwca-o1", "coates-o1",
]

PLACEHOLDER_PAGES = {}

# Series these books collect that the shared SERIES table does not carry.
# Display names are the marvel.com form (name plus start year) rather than the
# wiki's volume number, because that is what link_issues.py matches on -- the
# catalog carries a dozen series called simply "Captain America", which is
# exactly the reused-title case its tiebreak() exists for.
SERIES_EXTRA = {
 "Captain America Comics Vol 1":                       ("cac",    "Captain America Comics"),
 "Captain America Vol 1":                              ("cap",    "Captain America (1968)"),
 "Captain America Vol 3":                              ("cap3",   "Captain America (1998)"),
 "Captain America Vol 5":                              ("cap5",   "Captain America (2004)"),
 "Captain America Vol 6":                              ("cap6",   "Captain America (2011)"),
 "Captain America Vol 7":                              ("cap7",   "Captain America (2012)"),
 # Vol 8 is the 2017 Spencer series; marvel.com has no #25 for it, so this
 # one issue is reported unlinked rather than mislinked onto Coates' #25.
 "Captain America Vol 8":                              ("cap8",   "Captain America (2017)"),
 # Vol 9 (#695-704, Waid) is marvel.com's "Captain America (2017 - 2018)".
 # The code and display name match wolverine_meta.py exactly -- the id store
 # is shared and that shelf already links #697 through this prefix.
 "Captain America Vol 9":                              ("cap18",  "Captain America (2018)"),
 "Captain America Vol 10":                             ("cap10",  "Captain America (2018)"),
 # Same code as wolverine_meta.py: Annual #8 is on both shelves and has to
 # key the same way in the shared id store.
 "Captain America Annual Vol 1":                       ("caan1",  "Captain America Annual"),
 "Tales of Suspense Vol 1":                            ("tos",    "Tales of Suspense"),
 "Captain America and Bucky Vol 1":                    ("capbuck","Captain America And Bucky"),
 "Captain America: Sam Wilson Vol 1":                  ("capsam", "Captain America: Sam Wilson"),
 "Captain America: Steve Rogers Vol 1":                ("capsr",  "Captain America: Steve Rogers"),
 "Captain America: Sentinel of Liberty Vol 1":         ("capsol", "Captain America Sentinel Of Liberty (1998)"),
 "Captain America: Sentinel of Liberty Rough Cut Vol 1":("capsolrc","Captain America: Sentinel of Liberty Rough Cut"),
 "Captain America: Reborn Vol 1":                      ("capreb", "Captain America: Reborn"),
 "Captain America: Reborn Digital Prologue Vol 1":     ("caprebp","Captain America: Reborn Digital Prologue"),
 "Captain America: The Legend Vol 1":                  ("caplgd", "Captain America: The Legend"),
 "Captain America: Red, White & Blue Vol 1":           ("caprwb", "Captain America: Red, White & Blue"),
 "Captain America: 65th Anniversary Special Vol 1":    ("cap65",  "Captain America 65th Anniversary"),
 "Captain America: Who Will Wield the Shield? Vol 1":  ("capwws", "Captain America: Who Will Wield  the Shield?"),
 "Captain America's Bicentennial Battles Vol 1":       ("capbb",  "Captain America's Bicentennial Battles"),
 "All-New Captain America Vol 1":                      ("ancap",  "All-New Captain America"),
 "All-New Captain America: Fear Him Vol 1":            ("ancapfh","All-New Captain America: Fear Him"),
 "Adventures of Captain America Vol 1":                ("advcap", "Adventures Of Captain America"),
 "Steve Rogers: Super-Soldier Vol 1":                  ("srss",   "Steve Rogers: Super-Soldier"),
 "Winter Soldier Vol 1":                               ("wsol",   "Winter Soldier (2012)"),
 "Winter Soldier: Winter Kills Vol 1":                 ("wsolwk", "Winter Soldier: Winter Kills"),
 "Winter Soldier: The Bitter March Vol 1":             ("wsolbm", "Winter Soldier: The Bitter March"),
 "Secret Empire Vol 1":                                ("sempire","Secret Empire"),
 "Secret Empire Omega Vol 1":                          ("sempo",  "Secret Empire Omega"),
 "Hail Hydra Vol 1":                                   ("hhydra", "Captain America: Hail Hydra"),
 "Blood and Glory Vol 1":                              ("bandg",  "Punisher/Captain America: Blood and Glory"),
 "U.S.Agent Vol 1":                                    ("usagent","U.S.Agent"),
 "Ghost Rider/Captain America: Fear Vol 1":            ("grcapf", "Ghost Rider/Captain America: Fear"),
 "Iron Man & Captain America Annual Vol 1":            ("imcaann","Iron Man & Captain America Annual"),
 "Avengers Standoff: Welcome to Pleasant Hill Vol 1":  ("stndw",  "Avengers Standoff: Welcome to Pleasant Hill"),
 "Avengers Standoff: Assault On Pleasant Hill Alpha Vol 1": ("stnda","Avengers Standoff: Assault on Pleasant Hill Alpha"),
 "Avengers Standoff: Assault On Pleasant Hill Omega Vol 1": ("stndo","Avengers Standoff: Assault on Pleasant Hill Omega"),
 "Civil War II: The Oath Vol 1":                       ("cw2oath","Civil War II: The Oath"),
 "Generations: Sam Wilson Captain America & Steve Rogers Captain America Vol 1": ("gencap","Generations: Sam Wilson Captain America & Steve Rogers Captain America"),
 "Free Comic Book Day 2016 (Captain America) Vol 1":   ("fcbd16", "Free Comic Book Day 2016 (Captain America)"),
 "Free Comic Book Day 2017 (Secret Empire) Vol 1":     ("fcbd17", "Free Comic Book Day 2017 (Secret Empire)"),
 "Free Comic Book Day 2018 (Avengers/Captain America) Vol 1": ("fcbd18","Free Comic Book Day 2018 (Avengers/Captain America)"),
 "Black Widow Vol 6":                                  ("bwid6",  "Black Widow (2016)"),
 "Fear Itself Vol 1":                                  ("fearit", "Fear Itself"),
 "FOOM Vol 1":                                         ("foom",   "FOOM"),
 "Not Brand Echh Vol 2":                               ("nbe2",   "Not Brand Echh (2017)"),
}

# Reused verbatim from the other shelves' own SERIES_EXTRA. A hero only ever
# sees the shared SERIES table plus its OWN extras, so a series another shelf
# already carries has to be repeated here -- with exactly the same short code,
# because the marvel.com id store is shared and the same series must key the
# same way on every shelf.
SERIES_EXTRA.update({
 "Marvel Fanfare Vol 1":                               ("mfan",   "Marvel Fanfare"),
 "Punisher Annual Vol 1":                              ("punann", "Punisher Annual"),
 "Iron Man Vol 1":                                     ("im",     "Iron Man"),
 "Daredevil Annual Vol 1":                             ("ddann",  "Daredevil Annual"),
})
