# The hand-written half of the Ghost Rider shelf. Same shape as
# omnibus_meta.py, hulk_meta.py, ff_meta.py, wolverine_meta.py,
# moonknight_meta.py, daredevil_meta.py, silversurfer_meta.py,
# captainamerica_meta.py, ironman_meta.py and blackpanther_meta.py -- ORDER
# (wiki-backed), PLACEHOLDERS (tiles with no contents), SHELF (display order by
# id), PLACEHOLDER_PAGES, and SERIES_EXTRA for the series the shared SERIES
# table in build_omnibus_data.py does not already carry.
#
# Scope: every Ghost Rider omnibus Marvel has printed, which is seven. Five of
# them needed no judgement -- the three Danny Ketch volumes and the Aaron and
# Percy books are the Ghost Rider ongoing title and its minis, start to finish.
#
# The other two were a real scope call and the USER made it, explicitly, on
# being shown the choice: both are ON.
#   - GHOST RIDER 2099 is Zero Cochrane, a murdered hacker downloaded into a
#     warbot in a cyberpunk future -- a different man under the name. It is on
#     for the reason Hulk: Maestro is on the Hulk shelf: it is an alternate-
#     future thread, but every issue in it is a Ghost Rider book.
#   - COSMIC GHOST RIDER is Frank Castle, and unlike 2099 it is not a solo run:
#     17 of its 35 issues are Thanos, Guardians of the Galaxy and Avengers
#     comics. That is the shape that keeps Heroes Reborn off the FF shelf and
#     Devil's Reign off Daredevil's. The user put it on anyway, which makes
#     this shelf complete -- every Ghost Rider omnibus in print is on it, as on
#     the Moon Knight, Silver Surfer and Iron Man shelves.
#
# TWO VOLUMES HAVE NOT SHIPPED: Danny Ketch Vol. 3 and the Percy book are both
# dated OCTOBER 2026. Both are on under the amended rule -- see "A shelf holds
# books whose tile is finished" in CLAUDE.md -- because all three things a tile
# is made of are real for each: the wiki carries full ReprintOf contents, the
# issues resolve to marvel.com (these are 1993-94 and 2022-24 comics, long in
# the catalog), and both jacket scans exist on the wiki rather than being
# redlinks. Their tiles carry a "Ships Oct 2026" badge that retires itself in
# October without an edit.
#
# WHAT IS NOT HERE IS MARVEL'S DOING, NOT A SCOPE CALL, and it is the biggest
# hole on any shelf on the site: JOHNNY BLAZE'S ORIGINAL RUN HAS NO OMNIBUS.
# Marvel Spotlight #5-12 and Ghost Rider (1973) #1-81 -- the 1972 debut, the
# whole Roy Thomas / Gary Friedrich / Mike Ploog era, Johnny Blaze's entire
# first life as the character -- exist only as Epic Collections and Masterworks.
# So this shelf opens in 1990 with the man who replaced him. Daniel Way's Ghost
# Rider (2006) #1-19 is missing for the same reason, which is why the Aaron
# volume opens at #20; so are Ennis's two miniseries and Robbie Reyes's
# All-New Ghost Rider entirely. The tile notes say so where the jump shows.
#
# One contents note, and it needs no repair: Danny Ketch Vol. 3 lists GHOST
# RIDER (1990) #50 twice, as ReprintOf28 and ReprintOf29 with ReprintOfStory 1
# and 2. That is the anniversary issue's two stories, not a duplicate -- gen()
# dedupes globally on first occurrence, so the volume comes out at 50 issues.
#
# The ReprintOf fields matched the rendered gallery on all seven volumes, in
# content and in order, so nothing here is hand-corrected. Note the gallery
# comparison needs the page's own COVER-CREDIT links discounted first: four of
# these pages carry an `Image2_ReprintOf` naming the issue whose art the DM
# variant reproduces, and it links ahead of the gallery proper. Same hazard as
# Marvel Fanfare #45 on the Daredevil shelf.

ORDER = [
("Ghost Rider: Danny Ketch Omnibus Vol 1 1", dict(id="dk-o1", title="Ghost Rider: Danny Ketch Omnibus", vol="Vol. 1",
  creators="Howard Mackie, Javier Saltares & Mark Texeira", era="1990–1992", released="Sep 2024",
  art="o-hellfire", tex="tex-flame", spine="Danny Ketch",
 cover="Art/Ghost-Rider/dk-o1.jpg",
  note="Marvel's best-selling book of 1990, and the shelf starts here because Johnny Blaze's 1972 run has never been collected in omnibus at all. Danny Ketch finds a motorcycle in a scrapyard, touches its gas cap and burns. Howard Mackie writes him as a teenager who cannot control the thing wearing him — the Rider does the talking, decides who is guilty and is not remotely on Danny's side. Javier Saltares lays it out and then Mark Texeira inks over him from #6 and the book turns into scratched black ink and hellfire, which is the look the whole decade copied. The Hearts of Darkness one-shot with Wolverine and the Punisher is in here, and so is fifty-five issues' worth of Marvel Comics Presents backups.")),
("Ghost Rider: Danny Ketch Omnibus Vol 1 2", dict(id="dk-o2", title="Ghost Rider: Danny Ketch Omnibus", vol="Vol. 2",
  creators="Howard Mackie, Andy Kubert & Adam Kubert", era="1992–1993", released="Oct 2025",
  art="o-midnight", tex="tex-chain", chapterby="series", spine="Danny Ketch",
 cover="Art/Ghost-Rider/dk-o2.jpg",
  note="Johnny Blaze comes back, the two of them get a second book — Spirits of Vengeance, with Adam Kubert drawing it — and then Marvel builds an entire horror line around them. Rise of the Midnight Sons runs through six titles at once and this volume prints all of it: Morbius, Nightstalkers, Darkhold and Doctor Strange alongside the two Ghost Rider titles, in the order the crossover was read. It is the most 1993 thing on the site and it is also the moment the character stopped being a solo book and became a franchise.")),
("Ghost Rider: Danny Ketch Omnibus Vol 1 3", dict(id="dk-o3", title="Ghost Rider: Danny Ketch Omnibus", vol="Vol. 3",
  creators="Howard Mackie, Ron Garney & Adam Kubert", era="1993–1994", released="Oct 2026",
  art="o-brimstone", tex="tex-crosshatch", chapterby="series", spine="Danny Ketch",
 cover="Art/Ghost-Rider/dk-o3.jpg",
  note="Ships October 2026 — it is on the shelf ahead of that because its contents, its links and its jacket are all real, which is the bar a tile has to clear. Ron Garney takes over the pencils and the run peaks: Siege of Darkness closes the Midnight Sons story across every book at once, and Ghost Rider #50 is the double-length anniversary issue with five artists on it. The tail of the book is the strangest material on the shelf — Blaze: Legacy of Blood, and the single issue of Ghost Rider and the Midnight Sons Magazine, neither of which is on Marvel Unlimited.")),
("Ghost Rider 2099 Omnibus Vol 1 1", dict(id="gr2099-o1", title="Ghost Rider 2099 Omnibus", vol="",
  creators="Len Kaminski & Chris Bachalo", era="1994–1996", released="Oct 2024",
  art="o-neon", tex="tex-circuit", spine="Ghost Rider 2099",
 cover="Art/Ghost-Rider/gr2099-o1.jpg",
  note="Zero Cochrane is shot to death by corporate security, has his mind uploaded to the net by three ghosts in the machine and comes back inside a cybernetic warbot. It is cyberpunk between Neuromancer and The Matrix, written by Len Kaminski with a straight face, and Chris Bachalo draws the first stretch of it — early Bachalo, all compressed panels and machinery. A different man under the name, on the shelf for the reason Maestro is on the Hulk shelf: every issue in it is a Ghost Rider book. All 25 issues, complete.")),
("Ghost Rider by Jason Aaron Omnibus Vol 1 1", dict(id="aaron-o1", title="Ghost Rider by Jason Aaron Omnibus", vol="",
  creators="Jason Aaron, Roland Boschi & Tony Moore", era="2008–2010", released="Oct 2010",
  art="o-heaven", tex="tex-halftone", spine="By Jason Aaron",
 cover="Art/Ghost-Rider/aaron-o1.jpg",
  note="Aaron's answer to the question nobody had asked: what if the thing that made Johnny Blaze a Ghost Rider was not the devil at all. Zadkiel is a rogue angel raiding heaven, the Riders turn out to be a lineage going back centuries, and the book becomes a road movie with a nun on a motorcycle and a caretaker with a shotgun. Note it opens at Ghost Rider (2006) #20 — Daniel Way wrote #1–19 and that stretch has no omnibus, so the volume starts where Aaron does. Ends on the Heaven's on Fire mini, which is the finale.")),
("Cosmic Ghost Rider Omnibus Vol 1 1", dict(id="cosmic-o1", title="Cosmic Ghost Rider Omnibus", vol="",
  creators="Donny Cates, Geoff Shaw & Dylan Burnett", era="2018–2021", released="Sep 2021",
  art="o-void", tex="tex-starfield", spine="Cosmic Ghost Rider",
 cover="Art/Ghost-Rider/cosmic-o1.jpg",
  note="Frank Castle made a deal with the devil, then a deal with Galactus, then a deal with Thanos, and turns up a thousand years in the future as a chain-swinging lunatic on a flaming space bike. He is a joke that Donny Cates keeps refusing to stop telling until it turns into something sad. The odd volume on this shelf and knowingly so: seventeen of its thirty-five issues are Thanos, Guardians of the Galaxy and Avengers comics rather than his own, because that is where the character was invented and where he kept turning up. Starts with the Thanos issues that created him.")),
("Ghost Rider by Benjamin Percy Omnibus Vol 1 1", dict(id="percy-o1", title="Ghost Rider by Benjamin Percy Omnibus", vol="",
  creators="Benjamin Percy & Cory Smith", era="2022–2024", released="Oct 2026",
  art="o-pyre", tex="tex-tread", chapterby="series", spine="By Benjamin Percy",
 cover="Art/Ghost-Rider/percy-o1.jpg",
  note="Ships October 2026, on the shelf early for the same reason Vol. 3 is. Percy is a horror novelist and he writes it as one: Johnny Blaze wakes up in a small town with a wife and two children and a life he does not remember earning, and the book spends five issues letting you work out what that is. It runs from there through the Wolverine crossover into Final Vengeance, which is the last Ghost Rider story before the title went away — so this is currently the end of the shelf as well as the end of the run.")),
]

# Nothing pending on this shelf.
PLACEHOLDERS = []

# Display order of the shelf, by id. A reading order, which on this shelf is
# also publication order of the material -- the three Ketch volumes run 1990 to
# 1994, Ghost Rider 2099 launches out of that same Midnight Sons moment in
# 1994, and Aaron, Cosmic and Percy follow in 2008, 2018 and 2022.
#
# gr2099-o1 sits with the era it came out of rather than being exiled to the
# end as a cross-era oddity: the Doom and Ultimate volumes go last on the FF
# shelf because their contents span decades, and this one does not -- it is two
# years of a single ongoing, published while dk-o3 was on the stands.
SHELF = [
  "dk-o1", "dk-o2", "dk-o3",
  "gr2099-o1",
  "aaron-o1",
  "cosmic-o1",
  "percy-o1",
]

PLACEHOLDER_PAGES = {}

# Series these books collect that the shared SERIES table in
# build_omnibus_data.py does not carry. Display names are the marvel.com form
# (name plus start year) rather than the wiki's volume number, because that is
# what link_issues.py matches on -- the catalog carries eleven series simply
# called "Ghost Rider" (1973, 1990, 2001, 2005, 2006, 2011, 2016, 2019, 2022
# and two more), which is exactly the reused-title case its tiebreak() exists
# for.
#
# `gr6` for Ghost Rider (2006) was already coded by another shelf and is reused
# verbatim by autocode(); the rest of the Ghost Rider ongoings are pinned here
# to the same `gr<wiki volume>` shape so they read consistently. `gr` on its
# own is deliberately not used: there is no single Ghost Rider series to give
# it to, and this shelf does not carry the 1973 run that would have earned it.
SERIES_EXTRA = {
 "Ghost Rider Vol 3":                                  ("gr3",       "Ghost Rider (1990)"),
 "Ghost Rider Vol 10":                                 ("gr10",      "Ghost Rider (2022)"),
 "Ghost Rider Annual Vol 3":                           ("grann3",    "Ghost Rider Annual (2023)"),
 "Ghost Rider 2099 Vol 1":                             ("gr2099",    "Ghost Rider 2099 (1994)"),
 # `grbsov`, not `sov`: two links under that prefix were already sitting in the
 # shared id store from an old series_harvest.py run, and link_issues.py
 # refuses to let a second shelf code claim a marvel.com series another one
 # already owns. Adopting the existing code is the fix, exactly as the Captain
 # America shelf adopted Wolverine's `caan1` and `cap18`.
 "Ghost Rider/Blaze: Spirits of Vengeance Vol 1":      ("grbsov",    "Ghost Rider/Blaze: Spirits of Vengeance"),
 "Ghost Riders: Heaven's on Fire Vol 1":               ("grhof",     "Ghost Riders: Heaven's on Fire"),
 "Ghost Rider: Vengeance Forever Vol 1":               ("grvf",      "Ghost Rider: Vengeance Forever"),
 "Ghost Rider: Final Vengeance Vol 1":                 ("grfv",      "Ghost Rider: Final Vengeance"),
 "Ghost Rider/Wolverine: Weapons of Vengeance Alpha Vol 1": ("grwova","Ghost Rider/Wolverine: Weapons of Vengeance Alpha"),
 "Ghost Rider/Wolverine: Weapons of Vengeance Omega Vol 1": ("grwovo","Ghost Rider/Wolverine: Weapons of Vengeance Omega"),
 "Ghost Rider and the Midnight Sons Magazine Vol 1":   ("grmsmag",   "Ghost Rider and the Midnight Sons Magazine"),
 "Blaze: Legacy of Blood Vol 1":                       ("blazelb",   "Blaze: Legacy of Blood"),
 "Midnight Sons Unlimited Vol 1":                      ("msu",       "Midnight Sons Unlimited"),
 "Morbius: The Living Vampire Vol 1":                  ("morb",      "Morbius: The Living Vampire (1992)"),
 "Darkhold: Pages from the Book of Sins Vol 1":        ("darkhold",  "Darkhold: Pages from the Book of Sins"),
 "Nightstalkers Vol 1":                                ("nstalk",    "Nightstalkers"),
 "Doctor Strange, Sorcerer Supreme Vol 1":             ("dsss",      "Doctor Strange, Sorcerer Supreme"),
 "Cosmic Ghost Rider Vol 1":                           ("cgr",       "Cosmic Ghost Rider (2018)"),
 "Cosmic Ghost Rider Destroys Marvel History Vol 1":   ("cgrdmh",    "Cosmic Ghost Rider Destroys Marvel History"),
 "Revenge of the Cosmic Ghost Rider Vol 1":            ("rcgr",      "Revenge of the Cosmic Ghost Rider"),
 "Thanos Vol 2":                                       ("thanos2",   "Thanos (2016)"),
 "Thanos Annual Vol 2":                                ("thanosann2","Thanos Annual (2018)"),
 "Thanos Legacy Vol 1":                                ("thanosleg", "Thanos Legacy"),
 "Guardians of the Galaxy Vol 6":                      ("gotg6",     "Guardians of the Galaxy (2020)"),
 "Wolverine: Black, White & Blood Vol 1":              ("wbwb",      "Wolverine: Black, White & Blood"),
}
