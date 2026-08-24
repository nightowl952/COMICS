# The hand-written half of the Venom shelf. Same shape as omnibus_meta.py and
# the twelve other hero modules -- ORDER (wiki-backed), PLACEHOLDERS (tiles
# with no contents), SHELF (display order by id), PLACEHOLDER_PAGES, and
# SERIES_EXTRA for the series the shared SERIES table in build_omnibus_data.py
# does not already carry.
#
# Scope: EVERY Venom-family omnibus Marvel has printed, which is ten. Five of
# them needed no judgement at all -- Venomnibus Vol. 1-3 are the 1990s solo
# run start to finish, the Cates & Stegman book is the definitive modern one,
# and Venom War is the current event. Agent Venomnibus is Flash Thompson rather
# than Eddie Brock, but it is the Venom ongoing itself (Venom (2011) #1-42),
# which is the call that put Danny Ketch on the Ghost Rider shelf and Ghost
# Rider 2099 beside him: a different man under the name is still the name.
#
# THE OTHER FOUR WERE A REAL SCOPE CALL AND THE USER MADE IT, explicitly, on
# being shown the four books and their issue counts. All four are ON:
#   - SPIDER-MAN VS. VENOM (50) is already on the SPIDER-MAN shelf. Putting it
#     here too is deliberate: the issue ids are shared, so ASM #300 marked read
#     on one shelf is read on the other and both tiles carry the gold "in 2
#     omnibuses" pill. Without it this shelf would open in 1993 with Lethal
#     Protector and carry no origin at all -- no black costume, no Eddie, no
#     ASM #300. It is the one duplicated volume on the site.
#   - CARNAGE OMNIBUS (52) is Cletus Kasady's own book, and by the reasoning
#     that keeps She-Hulk off the Hulk shelf and Laura Kinney off Wolverine's
#     it is a different character. About ten of its fifty-two are Venom or
#     Spider-Man titles; the rest is Carnage's own series and minis.
#   - ABSOLUTE CARNAGE (42) and KING IN BLACK (63) are the two Cates-era
#     events. Both are the shape that keeps Heroes Reborn off the FF shelf and
#     Devil's Reign off Daredevil's -- only 6 of Absolute Carnage's issues and
#     4 of King in Black's are Venom's own book, the rest being tie-ins across
#     the whole line. They are on because they are the Venom line's events,
#     and because the Cates volume beside them prints only the core minis, so
#     without these two the tie-in half of both stories is nowhere.
# That makes the shelf COMPLETE, as the Moon Knight, Silver Surfer, Iron Man,
# Black Panther and Ghost Rider shelves are.
#
# ONE VOLUME HAS NOT SHIPPED: Venom War. The wiki dates it NOVEMBER 2026 and
# Penguin Random House and Amazon both say DECEMBER 8, 2026; the shelf uses the
# retailer date, because a badge that retires a month early is the worse error.
# It is on under
# the amended rule -- see "A shelf holds books whose tile is finished" in
# CLAUDE.md -- because all three things a tile is made of are real for it.
# Its tile carries a "Ships Nov 2026" badge that retires itself in November
# without an edit.
#
# WHAT IS NOT HERE IS MARVEL'S DOING, NOT A SCOPE CALL, and there are two
# holes:
#   - VENOM (2016) #1-6 and #150-165, Mike Costa's run -- Lee Price wearing
#     the symbiote and then Eddie taking it back. No omnibus, which is why the
#     shelf jumps from Space Knight in 2016 to Cates in 2018.
#   - VENOM (2021) #1-34, the AL EWING and RAM V run, and every All-New Venom
#     issue after Venom War. This is the bigger loss: Ewing's run is the
#     best-reviewed Venom book since Cates and none of it is collected in
#     omnibus. Venom War opens at Venom (2021) #35, which is where the event
#     starts, so the whole three-year run in front of it is missing.
# The tile notes say so where the jump shows.
#
# Contents notes, both worth knowing if a volume is ever re-pulled:
#   - THE REPRINTOF FIELDS MATCHED THE RENDERED GALLERY ON ALL TEN VOLUMES, in
#     content and in order, once the page's own COVER-CREDIT links are
#     discounted (an Image1_ReprintOf/Image2_ReprintOf names the issue whose
#     art the jacket or its variant reproduces and renders ahead of the reprint
#     gallery -- same hazard as Marvel Fanfare #45 on the Daredevil shelf). So
#     nothing here needed reordering the way inc-o1 did on the Hulk shelf.
#   - AGENT VENOMNIBUS WRITES ITS WHOLE LIST IN THE SHORT FORM WITH A `#`
#     ("Venom Vol 2 #1", "Venom: Space Knight #1"), which the <series>/<issue>
#     split on the last space cannot survive -- it would key every issue as
#     `venom2-#1`. All 66 entries are rewritten to the canonical long form,
#     taken from that page's own rendered gallery. This is the Captain America
#     shelf's short-form repair and its stray-`#` repair at once. RE-APPLY IF
#     RE-PULLED.
#   - Spider-Man vs. Venom's Marvel Graphic Novel entry carries a subtitle
#     after the issue number on the wiki; the raw file holds the Spider-Man
#     shelf's already-repaired list verbatim, so the two shelves cannot drift.
#
# The solicit audit could check exactly ONE of the ten -- only Agent
# Venomnibus carries an explicit COLLECTING range -- and it matched the shelf
# exactly (66 issues). The other nine are marketing prose with no numbers, so
# the shelf-wide gap check did the rest: every gap it found is guest-appearance
# spacing in a Spider-Man title, which a Venom-appearance chronology is
# supposed to have. No Venom-titled run on the shelf has a hole in it.

ORDER = [
("Spider-Man vs. Venom Omnibus Vol 1 1", dict(id="vsvenom-o1", title="Spider-Man vs. Venom Omnibus", vol="",
  creators="David Michelinie, Todd McFarlane & Erik Larsen", era="1984–1994", released="Sep 2018",
  art="o-blacksuit", tex="tex-web", spine="Spider-Man vs. Venom",
 cover="Art/Venom/vsvenom-o1.jpg",
  note="The origin, and the reason this shelf does not open in 1993. Every Venom appearance from the black costume walking off Battleworld to Maximum Carnage: ASM #252 sets the suit up, #300 is where Eddie Brock puts it on and McFarlane draws the first real Venom, and the rest is Michelinie writing him as a stalker who knows where you live. The same book sits on the Spider-Man shelf, so the issue ids are shared — mark #300 read here and it is read there. Maximum Carnage is printed in crossover order, rotating Amazing, Web, Spider-Man and Spectacular month by month.")),
("Venomnibus Vol 1 1", dict(id="venom-o1", title="Venomnibus", vol="Vol. 1",
  creators="David Michelinie, Mark Bagley & Ron Lim", era="1993–1995", released="Jun 2018",
  art="o-lethal", tex="tex-tendril", chapterby="series", spine="Venomnibus",
 cover="Art/Venom/venom-o1.jpg",
  note="Marvel notices Venom outsells the book he was a villain in, and hands him his own. Lethal Protector is where the turn happens — Eddie moves to San Francisco, gets a sewer full of homeless people to protect and stops being a monster on purpose. What follows is eighteen months of three-issue minis, one after another, because Marvel would not risk an ongoing: Funeral Pyre with the Punisher, The Madness with the Hulk, Nights of Vengeance, Separation Anxiety, Carnage Unleashed. Ron Lim draws most of it. It is the most 1993 object on the site and it knows it.")),
("Venomnibus Vol 1 2", dict(id="venom-o2", title="Venomnibus", vol="Vol. 2",
  creators="Larry Hama, Howard Mackie & Duncan Fegredo", era="1995–1998", released="Feb 2019",
  art="o-sinner", tex="tex-halftone", chapterby="series", spine="Venomnibus",
 cover="Art/Venom/venom-o2.jpg",
  note="The mini treadmill keeps going and starts to buckle. Sinner Takes All puts Anne Weying in the symbiote and is the best thing in the volume; The Hunger has Eddie starving for the brain chemical the suit needs; On Trial has Matt Murdock defending him in court; Tooth and Claw is Wolverine. Then Venom goes to work for the government in License to Kill and The Finale, and Marvel stops. The whole of the 1993–98 mini era ends here, and the character disappears for a year — which is the gap the next volume opens across.")),
("Venomnibus Vol 1 3", dict(id="venom-o3", title="Venomnibus", vol="Vol. 3",
  creators="Paul Jenkins, Daniel Way & Humberto Ramos", era="1999–2007", released="Nov 2020",
  art="o-brock", tex="tex-crosshatch", chapterby="series", spine="Venomnibus",
 cover="Art/Venom/venom-o3.jpg",
  note="Venom comes back as a Spider-Man villain again and then, in 2003, gets an ongoing at last — Daniel Way and Francisco Herrera's Venom, eighteen issues of a symbiote thawed out of Antarctic ice, which is a much stranger book than its reputation. Around it: Paul Jenkins on Peter Parker, Venom Vs. Carnage where Toxin is born, and Mark Millar's Marvel Knights arc. The volume ends with Eddie Brock dying of cancer and selling the symbiote at auction, which is the last thing that happens to this version of the character.")),
("Agent Venomnibus Vol 1 1", dict(id="agent-o1", title="Agent Venomnibus", vol="",
  creators="Rick Remender, Cullen Bunn & Tony Moore", era="2011–2016", released="Jul 2025",
  art="o-agent", tex="tex-camo", chapterby="series", spine="Agent Venom",
 cover="Art/Venom/agent-o1.jpg",
  note="Flash Thompson lost both legs in Iraq, and the government gives him the symbiote for fifty missions with a hard time limit before it bonds permanently. Rick Remender writes it as a war comic with an addiction metaphor running underneath — the suit is the drink Flash's father could not put down — and Tony Moore draws it. Then Cullen Bunn takes it to Philadelphia, then into space, and Space Knight ends with Flash as a cosmic hero. A different man under the name, on for the reason Danny Ketch is on the Ghost Rider shelf. All 42 issues plus the point issues, complete.")),
("Carnage Omnibus Vol 1 1", dict(id="carnage-o1", title="Carnage Omnibus", vol="",
  creators="Zeb Wells, Clayton Crain & Gerry Conway", era="2004–2016", released="Apr 2018",
  art="o-carnage", tex="tex-splatter", chapterby="series", spine="Carnage",
 cover="Art/Venom/carnage-o1.jpg",
  note="Cletus Kasady's own shelf, gathered up. It opens on Venom Vs. Carnage, which is where Toxin gets born out of Carnage the way Carnage got born out of Venom, and then runs the whole solo line: Zeb Wells and Clayton Crain's Carnage, Carnage U.S.A. where he takes a town, Superior Carnage, Deadpool vs. Carnage, and finally Gerry Conway's sixteen-issue Carnage, which turns him into an underground horror book about a cult and an elder god. A different character on a Venom shelf, on because the user put him there.")),
("Venomnibus by Cates and Stegman Vol 1 1", dict(id="cates-o1", title="Venomnibus by Cates & Stegman", vol="",
  creators="Donny Cates & Ryan Stegman", era="2018–2021", released="Dec 2022",
  art="o-abyss", tex="tex-tendril", chapterby="series", spine="Cates & Stegman",
 cover="Art/Venom/cates-o1.jpg",
  note="The run that reinvented the character, and the reason there is a Venom shelf to build. Cates opens by inventing Knull — a god who made the symbiotes as weapons before there was light — and rewrites everything the suit is in one issue. Ryan Stegman draws Venom as a wet, elongated, wrong-shaped thing rather than a bodybuilder, and the whole modern look of the character comes from here. Thirty-five issues plus the Web of Venom one-shots, running through Absolute Carnage and King in Black to Eddie ending up as the King in Black himself. The two events' tie-in halves are the next two tiles.")),
("Absolute Carnage Omnibus Vol 1 1", dict(id="abscarn-o1", title="Absolute Carnage Omnibus", vol="",
  creators="Donny Cates, Ryan Stegman & various", era="2019", released="Oct 2020",
  art="o-maximum", tex="tex-splatter", chapterby="series", spine="Absolute Carnage",
 cover="Art/Venom/abscarn-o1.jpg",
  note="Cletus comes back wanting the spinal codex left behind in everyone who has ever worn a symbiote, which is a premise engineered to reach every corner of the line — and this book is that reach. The five-issue core is here (it is also in the Cates volume, so those ids are shared), and around it fourteen tie-in minis and one-shots: Deadpool, Miles Morales, Scream, Lethal Protectors, Immortal Hulk, Captain Marvel, Weapon Plus. The tail of the volume is the lead-in issues where Carnage picks his victims off one at a time.")),
("King in Black Omnibus Vol 1 1", dict(id="kib-o1", title="King in Black Omnibus", vol="",
  creators="Donny Cates, Ryan Stegman & various", era="2020–2021", released="Dec 2022",
  art="o-knull", tex="tex-void", chapterby="series", spine="King in Black",
 cover="Art/Venom/kib-o1.jpg",
  note="Knull finally arrives, blacks out the sun and drops a symbiote dragon on every hero at once — the payoff Cates had been building since his first issue. Sixty-three issues: the core five, four of Venom's own, and then the widest tie-in list on this shelf, from Namor and S.W.O.R.D. to Black Cat, Savage Avengers, Thunderbolts and Return of the Valkyries. The most line-wide book here by a distance, and the reason it is on the shelf is that the Cates volume prints the core and nothing else.")),
("Venom War Omnibus Vol 1 1", dict(id="venomwar-o1", title="Venom War Omnibus", vol="",
  creators="Al Ewing, Iban Coello & various", era="2024", released="Dec 2026",
  art="o-war", tex="tex-tooth", chapterby="series", spine="Venom War",
 # HAND-ADDED, AND fetch_covers.py MUST NOT BE RUN WITH --all ON THIS SHELF.
 # The wiki page declares Image1 as a redlink with Image1_ReprintOf = Venom War
 # Vol 1 1.jpg, so prop=pageimages answers with the wiki's literal
 # "NO COVER AVAILABLE" placeholder -- which fetch_covers reports as a clean
 # 10-of-10 success. The jacket here is Amazon's flat cover for ISBN
 # 9781302966850 (Iban Coello), 329x500, which covers.py audit flags `soft`.
 # Refetch from the wiki once the book ships. The other nine ARE the wiki's
 # own jackets and were checked on a contact sheet.
 cover="Art/Venom/venomwar-o1.jpg",
  note="Ships December 2026, and it is on the shelf ahead of that because its contents, its links and its jacket are all real, which is the bar a tile has to clear. Eddie Brock and his son Dylan both claim the symbiote and it has to choose, which is a much better hook than an event usually gets. Note where it starts: Venom (2021) #35. Al Ewing and Ram V's whole run in front of that — #1–34, the best-reviewed Venom book since Cates — has no omnibus at all, so the shelf jumps three years to get here.")),
]

# Nothing pending on this shelf.
PLACEHOLDERS = []

# Display order of the shelf, by id. A reading order, which here runs close to
# publication order of the material.
#
# Two placements are deliberate:
#   - carnage-o1 sits AFTER agent-o1 rather than in strict publication order.
#     Its contents open in 2004 (Venom Vs. Carnage, which is also the last
#     thing in venom-o3) and close in 2016, so it straddles the Agent Venom
#     years -- and the two books share Minimum Carnage and Venom (2011) #26-27
#     outright. Reading it directly after Flash's run puts that crossover in
#     one place and lands the book's 2015-16 bulk immediately before Cates
#     opens in 2018.
#   - abscarn-o1 and kib-o1 sit AFTER cates-o1 rather than interrupting it.
#     The Cates volume prints both events' core minis inside its own run, so
#     reading it straight through is the spine; these two are the tie-in halves
#     of the same two stories and read as companions to it.
SHELF = [
  "vsvenom-o1",
  "venom-o1", "venom-o2", "venom-o3",
  "agent-o1", "carnage-o1",
  "cates-o1", "abscarn-o1", "kib-o1",
  "venomwar-o1",
]

# Chaptering: eight of the ten take the automatic per-series chapters.
#   - cates-o1 carries chapterby="series" because it is the anthology shape --
#     one ongoing with the Web of Venom one-shots, an annual, two Free Comic
#     Book Day issues and both events' core minis printed inside it. It scores
#     under the 3.5 average-run-length threshold for the same reason the Hulk
#     anthologies do, and "Web of Venom: Carnage Born #1" tells you where you
#     are where "Part 4" does not.
#   - vsvenom-o1 is deliberately LEFT on "parts", which is what the heuristic
#     picks: it is a Venom-appearance chronology whose spine is Maximum
#     Carnage, printed in crossover order rotating Amazing, Web, Spider-Man
#     and Spectacular month by month -- the exact case the parts strategy
#     exists for. It also has to match the Spider-Man shelf, which prints the
#     same book as nine Parts.

PLACEHOLDER_PAGES = {}

# Series these books collect that the shared SERIES table in
# build_omnibus_data.py does not carry, and that are worth pinning rather than
# leaving to autocode(). Display names are the marvel.com form (name plus start
# year) rather than the wiki's volume number, because that is what
# link_issues.py matches on and what tiebreak() reads as "a year the shelf
# itself names" -- which matters more here than on any other shelf, since the
# catalog carries ELEVEN series simply called "Venom" and four called
# "Carnage".
#
# Everything not listed here -- the ~60 Absolute Carnage, King in Black and
# Venom War tie-in one-shots, and the 1990s Venom minis -- is left to
# autocode(), because each of those titles is unique in the catalog and needs
# no tiebreak. Codes reused verbatim from another shelf's table (im, dd, ff6,
# imm, av18, dd6, mgn, grbsov, hkven, vtc, vacs, acimm, kibimm, kibbp,
# anadp1, ppsm) are picked up automatically by autocode(); they are NOT
# repeated here, because the id store is shared and a hand-written code is the
# one thing that can collide -- see open item 21 in CLAUDE.md and the `mav`
# mistake on the Avengers shelf.
SERIES_EXTRA = {
 "Venom: The Mace Vol 1":              ("vmace",     "Venom: The Mace"),
 "Venom: The Hunger Vol 1":            ("vhunger",   "Venom: The Hunger"),
 "Venom War: Daredevil Vol 1":         ("vwdd",      "Venom War: Daredevil"),
 "Minimum Carnage: Alpha Vol 1":       ("mincarna",  "Minimum Carnage: Alpha"),
 "Minimum Carnage: Omega Vol 1":       ("mincarno",  "Minimum Carnage: Omega"),
 "Free Comic Book Day 2019 (Spider-Man/Venom) Vol 1": ("fcbd19", "Free Comic Book Day 2019 (Spider-Man/Venom)"),
 "Free Comic Book Day 2020 (Spider-Man/Venom) Vol 1": ("fcbd20", "Free Comic Book Day 2020 (Spider-Man/Venom)"),
 "Venom Vol 1":                        ("venom",     "Venom (2003)"),
 "Venom Vol 2":                        ("venom2",    "Venom (2011)"),
 "Venom Vol 4":                        ("venom4",    "Venom (2018)"),
 "Venom Vol 5":                        ("venom5",    "Venom (2021)"),
 "Venom Annual Vol 1":                 ("venomann",  "Venom Annual (2018)"),
 "Venom: Space Knight Vol 1":          ("vsk",       "Venom: Space Knight"),
 "Venom War Vol 1":                    ("venomwar",  "Venom War"),
 "Venom Vs. Carnage Vol 1":            ("vvc",       "Venom Vs. Carnage"),
 "Carnage Vol 1":                      ("carnage",   "Carnage (2010)"),
 "Carnage Vol 2":                      ("carnage2",  "Carnage (2015)"),
 "Carnage, U.S.A. Vol 1":              ("carnusa",   "Carnage, U.S.A."),
 "Superior Carnage Vol 1":             ("supcarn",   "Superior Carnage"),
 "Superior Carnage Annual Vol 1":      ("supcarnann","Superior Carnage Annual"),
 "Absolute Carnage Vol 1":             ("abscarn",   "Absolute Carnage"),
 "King in Black Vol 1":                ("kib",       "King in Black"),
 "Scarlet Spider Vol 2":               ("scarsp2",   "Scarlet Spider (2012)"),
 "Amazing Spider-Man Vol 5":           ("asm5",      "Amazing Spider-Man (2018)"),
 "Spectacular Spider-Man Vol 2":       ("pp2",       "Spectacular Spider-Man (2003)"),
 "Sensational Spider-Man Vol 2":       ("sens2",     "Sensational Spider-Man (2006)"),
 "Nova Vol 3":                         ("nova3",     "Nova (1999)"),
 "Nova Vol 5":                         ("nova5",     "Nova (2013)"),
 "Black Cat Vol 1":                    ("bcat",      "Black Cat (2019)"),
 "Black Cat Vol 2":                    ("bcat2",     "Black Cat (2020)"),
 "Deadpool Vol 6":                     ("dpool6",    "Deadpool (2018)"),
 "Deadpool Vol 7":                     ("dpool7",    "Deadpool (2020)"),
 "Guardians of the Galaxy Vol 7":      ("gotg7",     "Guardians of the Galaxy (2020)"),
 "Spider-Woman Vol 7":                 ("spwom7",    "Spider-Woman (2020)"),
 "Savage Avengers Vol 1":              ("savav",     "Savage Avengers (2019)"),
 "S.W.O.R.D. Vol 2":                   ("sword2",    "S.W.O.R.D. (2020)"),
 "Captain Marvel Vol 11":              ("cmar11",    "Captain Marvel (2019)"),
 "Invaders Vol 3":                     ("invad3",    "Invaders (2019)"),
 "Miles Morales: Spider-Man Vol 1":    ("mmsm",      "Miles Morales: Spider-Man (2018)"),
 "Symbiote Spider-Man Vol 1":          ("symsm",     "Symbiote Spider-Man"),
 "Marvel Knights: Spider-Man Vol 1":   ("mksm",      "Marvel Knights: Spider-Man"),
 # `darkhawk`, not `dhawk`: the Spider-Man vs. Venom volume already put
 # Darkhawk #13-14 in the shared id store under that prefix from the
 # Spider-Man shelf, and link_issues.py refuses a second code for a series
 # another shelf already owns. Adopting the existing one is the fix, as the
 # Captain America shelf adopted Wolverine's caan1 and the Ghost Rider
 # shelf adopted grbsov.
 "Darkhawk Vol 1":                     ("darkhawk",  "Darkhawk (1991)"),
 "Nightwatch Vol 1":                   ("nwatch",    "Nightwatch"),
 "Silver Sable and the Wild Pack Vol 1": ("ssable",  "Silver Sable and the Wild Pack"),
 "Uncanny Origins Vol 1":              ("uorig",     "Uncanny Origins"),
 "Union Vol 1":                        ("union",     "Union (2020)"),
 "Incoming Vol 1":                     ("incoming",  "Incoming!"),
}
