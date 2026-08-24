# The hand-written half of the Doctor Strange shelf. Same shape as
# omnibus_meta.py, hulk_meta.py, ff_meta.py, wolverine_meta.py,
# moonknight_meta.py, daredevil_meta.py, silversurfer_meta.py,
# captainamerica_meta.py, ironman_meta.py, blackpanther_meta.py and
# ghostrider_meta.py -- ORDER (wiki-backed), PLACEHOLDERS (tiles with no
# contents), SHELF (display order by id), PLACEHOLDER_PAGES, and SERIES_EXTRA
# for the series the shared SERIES table in build_omnibus_data.py does not
# already carry.
#
# SCOPE: eight of the ten volumes are Stephen Strange's own solo title and
# needed no judgement -- the two Strange Tales books, Master of the Mystic
# Arts, the three Sorcerer Supreme volumes, Aaron & Bachalo and Jed MacKay.
# Two calls were real and the USER made both, explicitly, on being shown the
# choice:
#   - THE DEFENDERS Vol. 1-2 are ON. Strange convened the non-team and is in
#     nearly all of it, but so are the Hulk, Namor and the Silver Surfer, so
#     this is the shape that keeps Marvel Two-In-One off the FF shelf and
#     Marvel Team-Up off Spider-Man's -- and CLAUDE.md had already recorded
#     these exact two volumes as "the Defenders'" when they were ruled off the
#     Silver Surfer shelf. The user overrode that precedent: the Defenders is
#     Doctor Strange's one lasting team affiliation, he founds it inside his
#     own book (Marvel Feature #1 is the last thing in Doctor Strange Omnibus
#     Vol. 2), and Secret Defenders is already on the shelf inside Sorcerer
#     Supreme Vol. 2. It costs exactly one duplicated issue -- see the overlap
#     note below.
#   - STRANGE ACADEMY is OFF. Skottie Young and Humberto Ramos's 24-issue
#     magic-school book is set in Strange's corner of the universe, but the
#     leads are students and he is faculty. Off by the reasoning that keeps
#     All-New Wolverine and X-23 off the Wolverine shelf. Its entry is NOT in
#     doctorstrange_contents_raw.json, so adding it later means a fresh wiki
#     pull rather than a meta edit -- deliberate, because it was a decision
#     rather than a deferral.
#
# WHAT IS NOT HERE IS MARVEL'S DOING, NOT A SCOPE CALL, and there are two
# holes, the second of them the worst-served stretch of any shelf on the site:
#   - DOCTOR STRANGE (1974) #23-81, eleven years, 1977-1987. Master of the
#     Mystic Arts stops at #22 and no omnibus picks the run up, so Roger Stern
#     and Marshall Rogers's celebrated stretch and the whole run to the title's
#     1987 cancellation are Epic Collections and Masterworks only.
#   - 1996 TO 2015, nineteen years. Sorcerer Supreme ends at #90 and the next
#     omnibus is Aaron & Bachalo's. Everything between is uncollected in this
#     format, including J. Michael Straczynski and Brandon Peterson's Strange
#     (2004) and -- the painful one -- Brian K. Vaughan and Marcos Martin's
#     THE OATH (2006), which is the best-regarded Doctor Strange story of the
#     last thirty years and has no omnibus of any kind.
# The tile notes say so where the jump shows.
#
# ONE HAND FIX IS IN THE RAW FILE AND A RE-PULL WILL UNDO IT. `ds-o2`'s order
# is corrected: the wiki's ReprintOf fields AND its rendered gallery both group
# by series and so put DOCTOR STRANGE (1968) #169-183 first, ahead of STRANGE
# TALES #147-168 -- which is backwards, because Strange Tales #168 (May 1968)
# is the last issue of that book and Doctor Strange #169 (June 1968) continues
# its numbering directly. The 22-issue Strange Tales block is moved to the
# front; everything after it keeps the wiki's order exactly. Three things
# settle it: the numbering continuation, the page's own Solicit, which narrates
# Kaluu, the Ancient One's origin and the Living Tribunal (all Strange Tales)
# and only THEN says "and in 1968, Doctor Strange received his own solo title",
# and a review of the printed book describing it as "the remaining material
# from Masterworks volume 2, all of 3, and most of 4" -- a chronological
# progression that puts Strange Tales first. This is the `inc-o1` hazard from
# the Hulk shelf and the `early-o1` one from Black Panther, and like `iim-o2`
# on the Iron Man shelf it is a judgement against BOTH wiki sources rather than
# a repair of one.
#
# Note the opposite call was made on `def-o1` and it is worth not relitigating:
# the wiki puts AVENGERS (1963) #115-118 in a block at the end rather than
# interleaved with Defenders #8-11, which reads like the Avengers/Defenders War
# printed as an appendix. It is left alone, because Marvel's own collecting
# line lists it exactly that way too -- three sources agree, so there is no
# disagreement to arbitrate. The volume note tells the reader to read the two
# halves together.
#
# The only other repair was one short-form entry with a stray '#':
# "Doctor Strange: Last Days of Magic #1" -> "... Vol 1 1". The pipeline splits
# an issue title on its LAST space to get <series>/<issue>, which that form
# cannot survive.
#
# THE ONE OVERLAP is MARVEL FEATURE #1, and it is the join between two books:
# Doctor Strange Omnibus Vol. 2 ends on it (Strange founds the non-team in the
# last thing he does in his own book) and Defenders Omnibus Vol. 1 opens with
# it. Same shape as Captain America (2004) #25 sitting in both the Brubaker and
# Death of Captain America volumes. 349 slots, 348 unique issues.

ORDER = [
("Doctor Strange Omnibus Vol 1 1", dict(id="ds-o1", title="Doctor Strange Omnibus", vol="Vol. 1",
  creators="Stan Lee & Steve Ditko", era="1963–1966", released="Oct 2016",
  art="o-mystic", tex="tex-mandala", spine="Doctor Strange",
 cover="Art/Doctor-Strange/ds-o1.jpg",
  note="Five pages a month at the back of a Human Torch book, and it became the strangest thing Marvel published. Steve Ditko had nowhere to put a fight scene in that page count, so he drew rooms instead — folded staircases, floating rock, planes of colour with no horizon — and invented what a magic dimension looks like in comics. Stan Lee's captions name things rather than explain them, which is why the Vishanti and the Dread Dormammu sound like real oaths. The Eternity saga in #130–146 is the run everyone means: seventeen issues of a chase across realities that ends with Strange meeting the universe itself, drawn as a man-shaped hole full of stars. Starts at Strange Tales #110 — note the strip skipped #112–113, so the book does too."),
),
("Doctor Strange Omnibus Vol 1 2", dict(id="ds-o2", title="Doctor Strange Omnibus", vol="Vol. 2",
  creators="Roy Thomas, Gene Colan & Marie Severin", era="1966–1971", released="Jan 2022",
  art="o-eternity", tex="tex-dimension", spine="Doctor Strange",
 cover="Art/Doctor-Strange/ds-o2.jpg",
  note="Ditko walks, and the book has to work out what it is without him. Marie Severin and then Gene Colan take it somewhere softer and more fleshy — Colan draws Strange as a man with weight and worry, in smoke and half-light rather than Ditko's hard geometry. Roy Thomas gives him a mask and a costume for a while, which everyone remembers as a mistake and which is genuinely worth seeing. Strange Tales #168 is the last issue of that title and Doctor Strange #169 picks the numbering straight up, so the two halves of this book are one continuous run. It ends with the title cancelled at #183, three guest appearances keeping him alive, and Marvel Feature #1 — where he calls the Hulk and the Sub-Mariner and accidentally starts the Defenders."),
),
("Defenders Omnibus Vol 1 1", dict(id="def-o1", title="Defenders Omnibus", vol="Vol. 1",
  creators="Roy Thomas, Steve Englehart & Sal Buscema", era="1971–1975", released="Apr 2021",
  art="o-nonteam", tex="tex-crosshatch", spine="Defenders",
 cover="Art/Doctor-Strange/def-o1.jpg",
  note="Picks up on the issue the last book ended on. The joke of the Defenders is that it is an Avengers comic where nobody likes each other and there is no mansion, no butler and no charter — Strange is the only one who wants the team to exist, and he spends five years talking the Hulk and the Sub-Mariner into things. Sal Buscema draws almost all of it and gives the book its plain, sturdy, unglamorous look, which is exactly right for a group this shabby. The Avengers/Defenders War is here, the first great hero-versus-hero crossover and still one of the best-structured: pairs of heroes fight over the Evil Eye's fragments while both sides are being played. One warning about how it is printed — the four Avengers issues are collected as a block at the end rather than interleaved with Defenders #8–11, which is how Marvel lists them too, so read the two halves together rather than in the order the book prints them."),
),
("Defenders Omnibus Vol 1 2", dict(id="def-o2", title="Defenders Omnibus", vol="Vol. 2",
  creators="Steve Gerber & Sal Buscema", era="1975–1976", released="Jul 2023",
  art="o-headmen", tex="tex-halftone", spine="Defenders",
 cover="Art/Doctor-Strange/def-o2.jpg",
  note="Steve Gerber's run, and the strangest superhero comic Marvel published in the seventies. Gerber uses the non-team as a place to put ideas that fit nowhere else: the Headmen, four scientists who have each done something irreversible to their own skulls; Bambi and the Bozos; and the Elf With a Gun, who appears at random, murders a stranger and is never explained, because Gerber thought a universe that always explains itself is a lie. It is funny and then abruptly not. Strange spends much of it as the straight man, which is the most interesting he has ever been in a team book. The three 1950s horror shorts at the back — Mystery Tales #21, World of Fantasy #11, Tales of Suspense #9 — are reprinted as backmatter for the Headmen saga, so the volume's dates run wider than its run does."),
),
("Doctor Strange: Master of the Mystic Arts Omnibus Vol 1 1", dict(id="mystic-o1",
  title="Doctor Strange: Master of the Mystic Arts Omnibus", vol="",
  creators="Steve Englehart, Frank Brunner & Gene Colan", era="1972–1977", released="Mar 2025",
  art="o-brunner", tex="tex-astral", spine="Master of the Mystic Arts",
 cover="Art/Doctor-Strange/mystic-o1.jpg",
  note="The run people mean when they say Doctor Strange is the best-drawn book Marvel ever had. Frank Brunner comes off underground comix and draws Strange as Art Nouveau — whiplash linework, deep blacks, faces that actually look afraid — and Englehart writes him a story about Marvel's own universe being unmade and rebuilt by a Creator who turns out to be a frightened man. The Sise-Neg saga in Marvel Premiere #12–14 sends him back through the whole of human history to the moment of creation, and it got the Comics Code exercised for exactly the reason you would guess. Gene Colan returns for the back half and stays for years. This is also where Clea stops being a rescue object and becomes a person. Note the book stops at #22 of a run that goes to #81 — everything after 1977 is uncollected in omnibus."),
),
("Doctor Strange, Sorcerer Supreme Omnibus Vol 1 1", dict(id="sss-o1",
  title="Doctor Strange, Sorcerer Supreme Omnibus", vol="Vol. 1",
  creators="Peter B. Gillis, Roy & Dann Thomas & Jackson Guice", era="1988–1992", released="Jul 2017",
  art="o-supreme", tex="tex-runes", spine="Sorcerer Supreme",
 cover="Art/Doctor-Strange/sss-o1.jpg",
  note="A relaunch after a year with no book at all, and it opens by taking everything off him — the Sanctum burned, his library gone, his hands broken, the title Sorcerer Supreme actually in question. Peter Gillis writes the first stretch as a rebuild from nothing, then Roy and Dann Thomas settle it into the shape it keeps for ninety issues: a working occult procedural, heavy on lore, where the magic has rules and costs and paperwork. Jackson Guice's art is the late-eighties Marvel house style at its cleanest. It is not the flashiest era on this shelf and it is the one that treats being Sorcerer Supreme as a job."),
),
("Doctor Strange, Sorcerer Supreme Omnibus Vol 1 2", dict(id="sss-o2",
  title="Doctor Strange, Sorcerer Supreme Omnibus", vol="Vol. 2",
  creators="Roy & Dann Thomas, Geof Isherwood & Various", era="1992–1994", released="Jul 2018",
  art="o-midnightsons", tex="tex-halftone", spine="Sorcerer Supreme",
 cover="Art/Doctor-Strange/sss-o2.jpg",
  note="Marvel builds a horror line around him. Rise of the Midnight Sons runs through six books at once and Strange is the one who convenes them, which makes this the second time the character's main job is assembling people who do not want to be assembled. Secret Defenders is the other half of that idea and it is a genuinely good format — a different roster every arc, picked by Strange for the specific job, none of them told why. Geof Isherwood draws most of it. It is the most nineties material on the shelf, and the Ghost Rider, Morbius and Silver Surfer chapters here are the same crossover the Ghost Rider shelf reads from the other side."),
),
("Doctor Strange, Sorcerer Supreme Omnibus Vol 1 3", dict(id="sss-o3",
  title="Doctor Strange, Sorcerer Supreme Omnibus", vol="Vol. 3",
  creators="David Quinn, Warren Ellis & J.M. DeMatteis", era="1993–1998", released="Apr 2022",
  art="o-vapors", tex="tex-crosshatch", spine="Sorcerer Supreme",
 cover="Art/Doctor-Strange/sss-o3.jpg",
  note="The end of the ninety-issue run, and it gets strange in the other sense. David Quinn writes the bulk of it, from #60 to the high seventies, and takes the book somewhere genuinely odd: Strange loses his powers and starts drawing on a substance called the Vapors, a bargain the fandom has argued about for thirty years and which is at minimum unlike anything else in the character's history. Then Warren Ellis arrives around #80 for a short, cold, very early-Ellis stretch, and J.M. DeMatteis closes the run out. Mark Buckingham draws a lot of the back half and is the best reason to look at it. The tail of the book is the odd material — an ashcan, a magazine, Kurt Busiek's 1994 Strange Tales one-shot, and What Is It That Disturbs You, Stephen?, a 1997 painted graphic novel — so the dates run past the run's own end. After this the character has no ongoing title for nineteen years."),
),
("Doctor Strange by Jason Aaron & Chris Bachalo Omnibus Vol 1 1", dict(id="aaron-o1",
  title="Doctor Strange by Aaron & Bachalo Omnibus", vol="",
  creators="Jason Aaron & Chris Bachalo", era="2015–2017", released="Apr 2022",
  art="o-empirikul", tex="tex-mandala", spine="By Aaron & Bachalo",
 cover="Art/Doctor-Strange/aaron-o1.jpg",
  note="The first ongoing in nineteen years, and its one big idea is that magic has a price somebody has to pay. Aaron writes a Strange who eats things that are still moving, keeps a cellar full of obligations, and is quietly in enormous debt for every spell he has ever cast — which turns the character from a man with answers into a man with bills. Then the Empirikul arrive and burn magic out of the world entirely, and the back half is Strange with nothing, which is where the run gets good. Chris Bachalo draws it with the density turned all the way up: panels crammed with talking objects and impossible architecture, and a Sanctum that is clearly alive. Note the nineteen-year jump before this book — Straczynski's Strange and Vaughan and Martin's The Oath both fall in it and neither has an omnibus."),
),
("Doctor Strange by Jed MacKay Omnibus Vol 1 1", dict(id="mackay-o1",
  title="Doctor Strange by Jed MacKay Omnibus", vol="",
  creators="Jed MacKay, Lee Garbett & Marcelo Ferreira", era="2021–2024", released="Sep 2025",
  art="o-death", tex="tex-runes", spine="By Jed MacKay",
 cover="Art/Doctor-Strange/mackay-o1.jpg",
  note="Opens by killing him, which sounds like a stunt and is actually the setup for the best thing on the modern half of this shelf. The Death of Doctor Strange is a murder mystery where the detective is a younger Strange summoned from the past to investigate his own corpse, and it is fairly played — the clues are there. Then Strange hands the book to Clea, who becomes Sorcerer Supreme of Earth and is far better at it and much less nice about it, and Jed MacKay writes ten issues of her trying to bring him back that double as the best Clea material anyone has written. The 2023 ongoing puts them both in the Sanctum as a married couple running a practice together. Lee Garbett draws the first stretch; the whole thing is unusually tightly plotted for a book about magic."),
),
]

PLACEHOLDERS = []

# Reading order. It runs with publication order of the material, with one
# deliberate placement: THE TWO DEFENDERS VOLUMES SIT BETWEEN `ds-o2` AND
# `mystic-o1` rather than at the end as a cross-era block, because `ds-o2` ends
# on Marvel Feature #1 -- Strange founding the non-team -- and `def-o1` opens
# on the same issue. That hand-off is the shelf's one overlap and reading
# straight through it is the whole reason to put them there. The cost is a
# small step back at `mystic-o1`, whose Marvel Premiere issues (1972) are
# concurrent with early Defenders; that is the same trade `thing-o1` takes on
# the FF shelf, where a volume sits where it was published rather than where
# its numbering would put it.
SHELF = ["ds-o1", "ds-o2", "def-o1", "def-o2", "mystic-o1",
         "sss-o1", "sss-o2", "sss-o3", "aaron-o1", "mackay-o1"]

PLACEHOLDER_PAGES = {}

# Series these books collect that the shared SERIES table in
# build_omnibus_data.py does not carry. Display names are the marvel.com form
# (name plus start year where the title is reused) rather than the wiki's
# volume number, because that is what link_issues.py matches on -- the catalog
# carries six series simply called "Doctor Strange" and two called "Strange
# Tales", which is exactly the reused-title case its tiebreak() exists for.
SERIES_EXTRA = {
 "Strange Tales Vol 1":                                ("st",      "Strange Tales (1951)"),
 # The wiki's ReprintOf field for `sss-o3` said "Strange Tales Vol 2 1", which is
 # the APRIL 1987 Cloak and Dagger book. The omnibus actually collects STRANGE
 # TALES (1994) #1 -- Kurt Busiek and Ricardo Villagran, November 1994 -- which
 # the wiki files as Vol 3, and which Marvel's own collecting line names. The
 # raw file is corrected by hand and A RE-PULL WILL UNDO IT. era_fits() in
 # link_issues.py is what caught it: a 1987 series cannot be in a 1993-1998
 # volume, so the link was refused rather than made wrongly. Corrected, it links
 # cleanly to catalog series 5851, "STRANGE TALES 1 (1994)", published
 # 1994-11-01 -- which also confirms the fix. Note `catalog.py find
 # "strange_tales_1994"` returns NOTHING for it: marvel.com's slug is
 # `strange_tales_1_1994_1`, with the series' own "1" between the name and the
 # year, so a substring probe on the obvious form says the comic is absent when
 # it is not. Search on the name alone before believing a catalog miss.
 "Strange Tales Vol 3":                                ("st3",     "Strange Tales (1994)"),
 "Doctor Strange Vol 1":                               ("ds",      "Doctor Strange (1968)"),
 "Doctor Strange Vol 2":                               ("ds2",     "Doctor Strange (1974)"),
 "Doctor Strange Vol 4":                               ("ds4",     "Doctor Strange (2015)"),
 "Doctor Strange Vol 6":                               ("ds6",     "Doctor Strange (2023)"),
 "Doctor Strange Annual Vol 1":                        ("dsann",   "Doctor Strange Annual (1976)"),
 "Doctor Strange Annual Vol 2":                        ("dsann2",  "Doctor Strange Annual (2016)"),
 "Doctor Strange, Sorcerer Supreme Annual Vol 1":      ("dsssann", "Doctor Strange, Sorcerer Supreme Annual"),
 "Doctor Strange, Sorcerer Supreme Ashcan Vol 1":      ("dsssash", "Doctor Strange, Sorcerer Supreme Ashcan"),
 "Doctor Strange: Last Days of Magic Vol 1":           ("dsldm",   "Doctor Strange: Last Days of Magic"),
 "Doctor Strange What is it That Disturbs You Stephen? Vol 1":
                                                       ("dswiid",  "Doctor Strange: What Is It That Disturbs You, Stephen?"),
 "Death of Doctor Strange Vol 1":                      ("dods",    "Death of Doctor Strange"),
 "Death of Doctor Strange: Spider-Man Vol 1":          ("dodssm",  "Death of Doctor Strange: Spider-Man"),
 "Strange Vol 3":                                      ("strange3","Strange (2022)"),
 "Sub-Mariner Vol 2":                                  ("subm",    "Sub-Mariner (1968)"),
 "Namor, the Sub-Mariner Annual Vol 1":                ("namorann","Namor, the Sub-Mariner Annual"),
 "Marvel Feature Vol 1":                               ("mfeat",   "Marvel Feature"),
 "Giant-Size Defenders Vol 1":                         ("gsdef",   "Giant-Size Defenders"),
 "Defenders Annual Vol 1":                             ("defsann", "Defenders Annual"),
 "Secret Defenders Vol 1":                             ("secdef",  "Secret Defenders"),
 "Tomb of Dracula Vol 1":                              ("tod",     "Tomb of Dracula (1972)"),
 "Mystery Tales Vol 1":                                ("mystales","Mystery Tales"),
 "World of Fantasy Vol 1":                             ("wof",     "World of Fantasy"),
 'Spider-Man/Dr. Strange: "The Way to Dusty Death" Vol 1':
                                                       ("smds",    "Spider-Man/Doctor Strange: The Way to Dusty Death"),
}

# Reused verbatim from the other shelves' own SERIES_EXTRA. A hero only ever
# sees the shared SERIES table plus its OWN extras, so a series another shelf
# already carries has to be repeated here -- with exactly the same short code,
# because the marvel.com id store is shared and the same series must key the
# same way on every shelf. (autocode() would reuse them anyway; these are
# written out so the codes are readable next to the ones they sit beside.)
#
# `dsss` in particular is NOT this shelf's invention even though this is the
# shelf that reads all ninety issues of it: the Ghost Rider shelf already keys
# Doctor Strange, Sorcerer Supreme #28 that way for Rise of the Midnight Sons.
SERIES_EXTRA.update({
 "Doctor Strange, Sorcerer Supreme Vol 1":             ("dsss",    "Doctor Strange, Sorcerer Supreme"),
 "Defenders Vol 1":                                    ("defs",    "Defenders (1972)"),
 "Avengers Vol 1":                                     ("av",      "Avengers"),
 "Tales of Suspense Vol 1":                            ("tos",     "Tales of Suspense"),
 "Ghost Rider Vol 3":                                  ("gr3",     "Ghost Rider (1990)"),
 "Silver Surfer Vol 3":                                ("ssf3",    "Silver Surfer (1987)"),
 "Silver Surfer Annual Vol 1":                         ("ssfann",  "Silver Surfer Annual (1988)"),
 "Morbius: The Living Vampire Vol 1":                  ("morb",    "Morbius: The Living Vampire"),
 "Incredible Hulk Annual Vol 1":                       ("hkann",   "Incredible Hulk Annual"),
 "Midnight Sons Unlimited Vol 1":                      ("msu",     "Midnight Sons Unlimited"),
 "Ghost Rider and the Midnight Sons Magazine Vol 1":   ("grmsmag", "Ghost Rider and the Midnight Sons Magazine"),
})
