# -*- coding: utf-8 -*-
# The hand-written half of the Avengers shelf. Same shape as every other
# <hero>_meta.py -- ORDER (wiki-backed volumes), PLACEHOLDERS (tiles with no
# contents), SHELF (display order by id), PLACEHOLDER_PAGES, and SERIES_EXTRA
# for the series the shared SERIES table in build_omnibus_data.py does not
# already carry.
#
# SCOPE. This is the shelf CLAUDE.md had been calling "the hard one", and it
# was: the Avengers have more omnibuses than any other subject on the site, and
# roughly half the Marvel universe has appeared in one. The spine needed no
# judgement -- the Avengers' own title, start to finish, is 21 volumes -- and
# the four calls that were genuinely arguable were put to the user, who took
# all four:
#
#   * WEST COAST AVENGERS Vol. 1-2 are ON. A second Avengers team with its own
#     title, and the Byrne volume already carries 21 West Coast issues, so
#     leaving these off would have made his book read as an orphan.
#   * ULTIMATES by Millar & Hitch is ON, matching the precedent that puts
#     Ultimate Spider-Man on the Spider-Man shelf and Ultimate Fantastic Four
#     on the FF shelf.
#   * SECRET INVASION by Bendis is ON. 29 of its 34 issues are New Avengers,
#     Mighty Avengers or Secret Invasion itself.
#   * AVENGERS: THE CROSSING and AVENGERS VS. X-MEN are ON, and both are the
#     shape that keeps Heroes Reborn off the FF shelf and Devil's Reign off
#     Daredevil's -- The Crossing is only 6 Avengers issues out of 29, and AvX
#     is 74 issues of which most are X-books. The user was shown exactly that
#     and put them on anyway, which is what makes this shelf a complete run of
#     the team's own line rather than a selection from it.
#
# Deliberately OFF, and all for the reason that keeps She-Hulk off the Hulk
# shelf: Young Avengers (both volumes), Squadron Supreme (both), Hawkeye by
# Fraction & Aja, Black Widow Strikes. Different characters, or a member's solo
# book. The user was offered all four and declined them.
#
# Also off, and worth naming because they turn up in any Avengers enumeration:
# Heroes Reborn and Heroes Reborn: The Return (already recorded as off the FF
# and Captain America shelves -- a mixed Avengers/FF/Iron Man/Captain America
# book), Secret Wars, Secret Wars II, House of M and Acts of Vengeance (all
# line-wide events rather than the team's book), and the Infinity Gauntlet /
# War / Crusade omnibuses, which are Thanos's.
#
# ENUMERATION. Both traps CLAUDE.md records for the Captain America shelf fired
# again. `apprefix=Avengers` does not see ULTIMATES, HEROES REBORN or SECRET
# INVASION, so the sweep had to be run across three dozen prefixes and then
# checked by search. And the Marvel Database has no global Omnibus category to
# enumerate instead -- the only categories on an omnibus page are its own and
# its reprints'.
#
# TWO HAND FIXES are in avengers_contents_raw.json and a re-pull will undo both:
#
#   * `busiek-o2` was missing AVENGERS (1998) #55, #56 and #1/2. Its own solicit
#     says "Collecting AVENGERS (1998) #24-56, #1-1/2 and ANNUAL 2000-2001",
#     where the ReprintOf fields and the gallery both stop at #54. Same shape as
#     Fantastic Four #171 and Incredible Hulk (2000) #75-76, and invisible for
#     the same reason: johns-o1 opens at #57, so the hole fell exactly on a
#     volume boundary and nothing on the shelf looked short. The half issue is
#     the 1999 Wizard mail-away; the wiki has no page for it at all and
#     marvel.com has no record of it either, so it is on the shelf with a grey
#     Read button, which is the honest answer.
#   * `unc-o1` listed UNCANNY AVENGERS #8AU in the short form (`Uncanny
#     Avengers #8AU`), which the <series>/<issue> split on the last space
#     cannot survive -- it comes out as series "Uncanny" and issue
#     "Avengers #8AU". Rewritten long.
#
# Nothing else needed repairing: no doubled spaces, no subtitles after an issue
# number, and the ReprintOf order matched the rendered gallery on all 27 volumes
# once the cover-credit link that renders ahead of the reprint gallery is
# discounted (the Marvel Fanfare #45 hazard from the Daredevil shelf -- it fires
# on eleven of these pages).
#
# CHAPTERING. Four volumes carry chapterby="series" because the average-run-
# length heuristic would have chunked them into "Part N": wca-o1 (3.44),
# nav-o1 (3.07), si-o1 (2.83) and forever-o1 (2.08). Three are the ordinary
# anthology shape. si-o1 is the interesting one -- it IS a month-by-month
# crossover, which is what the "parts" strategy exists for -- but it rotates
# only three titles and the whole point of the book is that it is assembled in
# reading order, so a chapter that says "Mighty Avengers #12-19" tells you where
# you are and "Part 3" does not. Same call the Ghost Rider shelf makes for
# dk-o2 and dk-o3.

ORDER = [
("Avengers Omnibus Vol 1 1", dict(id="av-o1", title="Avengers Omnibus", vol="Vol. 1",
  creators="Stan Lee, Jack Kirby & Don Heck", era="1963–1966", released="Feb 2012",
  art="o-assemble", tex="tex-krackle", spine="Avengers",
  cover="Art/Avengers/av-o1.jpg",
  note="The first thirty issues, and the team barely holds still for any of them. Lee and Kirby put five heroes who do not like each other in a room, lose the Hulk by issue #2, find Captain America frozen in ice in #4, and then in #16 do the thing nobody does with a hit book — they fire the entire cast and replace it with three reformed criminals and Cap. That gamble is why the Avengers is a franchise and not a Justice League tribute: the door revolves, so the roster is the story.")),
("Avengers Omnibus Vol 1 2", dict(id="av-o2", title="Avengers Omnibus", vol="Vol. 2",
  creators="Roy Thomas, Don Heck & John Buscema", era="1966–1968", released="Mar 2015",
  art="o-assemble", tex="tex-krackle", spine="Avengers",
  cover="Art/Avengers/av-o2.jpg",
  note="Roy Thomas takes over and starts building the continuity engine. The Black Panther joins — the first Black superhero on an American team book — Hercules and the Black Widow drift in and out, Ultron arrives, and the Vision is built in #57 to kill the Avengers and joins them instead. John Buscema comes aboard at #41 and the book stops looking like Kirby's and starts looking like itself.")),
("Avengers Omnibus Vol 1 3", dict(id="av-o3", title="Avengers Omnibus", vol="Vol. 3",
  creators="Roy Thomas, John Buscema & Neal Adams", era="1968–1971", released="Mar 2018",
  art="o-assemble", tex="tex-halftone", spine="Avengers",
  cover="Art/Avengers/av-o3.jpg",
  note="The stretch where Thomas turns the book political and Neal Adams turns up to draw it. The Vision and the Scarlet Witch start their long unhappy romance, Yellowjacket and the Wasp marry, and #83 invents the Lady Liberators. Adams's issues on the run-up to the Kree/Skrull War are the ones people mean when they say the art changed — deep-focus figures with real weight, in a book that had been staged flat.")),
("Avengers Omnibus Vol 1 4", dict(id="av-o4", title="Avengers Omnibus", vol="Vol. 4",
  creators="Roy Thomas, Neal Adams & John Buscema", era="1971–1974", released="Mar 2019",
  art="o-kree", tex="tex-starfield", spine="Avengers",
  cover="Art/Avengers/av-o4.jpg",
  note="Two of the biggest things the book ever did, back to back. The Kree/Skrull War is the first Marvel story to treat the whole galaxy as the setting, and it is where Rick Jones ends a war by imagining one. Then the Avengers/Defenders War, printed here with its four Defenders chapters in reading order — the template every crossover since has copied, including the ones on this shelf that are eight books wide.")),
("Avengers Omnibus Vol 1 5", dict(id="av-o5", title="Avengers Omnibus", vol="Vol. 5",
  creators="Steve Englehart, Sal Buscema & Don Heck", era="1974–1976", released="Sep 2023",
  art="o-madonna", tex="tex-halftone", spine="Avengers",
  cover="Art/Avengers/av-o5.jpg",
  note="Englehart's run, and the strangest the book has been. The Celestial Madonna saga marries Mantis to a tree, walks the Vision through his own origin as the original Human Torch, and hands Kang a defeat that takes three time periods to land. Also here: the Serpent Crown, the Squadron Supreme, Patsy Walker becoming Hellcat, and three issues of F.O.O.M. — Marvel's own fanzine — which is a genuinely odd thing to find in an omnibus and exactly right for 1975.")),
("Avengers Omnibus Vol 1 6", dict(id="av-o6", title="Avengers Omnibus", vol="Vol. 6",
  creators="Jim Shooter, George Pérez & John Byrne", era="1976–1979", released="Mar 2026",
  art="o-korvac", tex="tex-starfield", spine="Avengers",
  cover="Art/Avengers/av-o6.jpg",
  note="Gerry Conway and then Jim Shooter, with George Pérez learning to draw crowds. The Korvac Saga is the centrepiece and it is not like the other Bronze Age epics: the villain wins, quietly, and the last chapter is the entire roster standing in a room losing an argument with a man who has already become God. Wonder Man comes back, Ultron takes another run at them, and Byrne turns up to draw the end.")),
("Avengers: West Coast Avengers Omnibus Vol 1 1", dict(id="wca-o1", title="Avengers: West Coast Avengers Omnibus", vol="Vol. 1",
  creators="Roger Stern, Steve Englehart & Al Milgrom", era="1984–1986", released="Apr 2013",
  # era is 1984-1986 although YEARS says 1984-1993: the 1993 is a fragment of
  # Avengers West Coast #100, printed as "material from" rather than as an
  # issue. Widening it would put a Chromium dot on a Bronze/Copper book.
  art="o-sunset", tex="tex-halftone", chapterby="series", spine="West Coast Avengers",
  cover="Art/Avengers/wca-o1.jpg",
  note="Marvel franchises the team. Hawkeye gets a branch office in Los Angeles, four issues to prove it, and then an ongoing — and the joke that the book is the B-squad is one it makes about itself for years before Englehart quietly makes it good. Mockingbird, Wonder Man, Tigra and Iron Man in the Jim Rhodes armour; the Vision and the Scarlet Witch's own mini is printed here too, because their marriage is about to be the thing the whole line breaks over.")),
("Avengers: West Coast Avengers Omnibus Vol 1 2", dict(id="wca-o2", title="Avengers: West Coast Avengers Omnibus", vol="Vol. 2",
  creators="Steve Englehart & Al Milgrom", era="1986–1989", released="Nov 2013",
  art="o-sunset", tex="tex-halftone", spine="West Coast Avengers",
  cover="Art/Avengers/wca-o2.jpg",
  note="Englehart's second act, and it goes places the main book never would: a time-travel arc that strands the team in the Old West and in ancient Egypt, Mockingbird letting the Phantom Rider fall, and the marriage that comes apart afterwards. This is also where the Vision is taken to pieces by a government committee and rebuilt white and blank — the single cruellest thing done to a character on this shelf, and the engine for twenty years of stories after it.")),
("Avengers by John Byrne Omnibus Vol 1 1", dict(id="byrne-o1", title="Avengers by John Byrne Omnibus", vol="",
  creators="John Byrne, Paul Ryan & Rich Buckler", era="1989–1990", released="Jul 2016",
  art="o-byrne", tex="tex-crosshatch", spine="By John Byrne",
  cover="Art/Avengers/byrne-o1.jpg",
  note="Byrne writing both Avengers books at once, which is why this volume is half West Coast and half the main title and reads as one thing. He picks up the white Vision and the wreckage of the Scarlet Witch's marriage and drives it all the way down — Wanda's children turn out never to have existed, and she comes apart. Then the Evolutionary War and Acts of Vengeance on top. Hard, clean, unsentimental cartooning; the plotting is another matter, and readers have argued about it for thirty-five years.")),
("Avengers: The Gathering Omnibus Vol 1 1", dict(id="gather-o1", title="Avengers: The Gathering Omnibus", vol="",
  creators="Bob Harras & Steve Epting", era="1992–1996", released="Mar 2021",
  art="o-gathering", tex="tex-crosshatch", spine="The Gathering",
  cover="Art/Avengers/gather-o1.jpg",
  note="Bob Harras and Steve Epting's long run, which is the most underrated stretch the book has. Operation: Galactic Storm is a nineteen-part war the Avengers lose morally — they take a decision at the end that splits the team in half — and Proctor's Gatherers arc runs the Black Knight and Sersi into the ground over three years. The last issues here are the Vision and the Scarlet Witch's endgame and the start of the collapse that Onslaught finishes off.")),
("Avengers: The Crossing Omnibus Vol 1 1", dict(id="crossing-o1", title="Avengers: The Crossing Omnibus", vol="",
  creators="Terry Kavanagh, Bob Harras & Mike Deodato", era="1995–1996", released="May 2012",
  art="o-gathering", tex="tex-shatter", spine="The Crossing",
  cover="Art/Avengers/crossing-o1.jpg",
  note="The famous disaster, collected whole so you can see how it happened. Iron Man is revealed to have been Kang's agent for his entire career, a teenage Tony Stark is imported from another timeline to replace him, and the plot spills across Force Works, War Machine and Iron Man to the point that only six of these twenty-nine issues are Avengers. It is on this shelf because it is where the line ends: Onslaught follows immediately, and everything after it is a relaunch. Read it as a case study, not as a good time.")),
("Avengers by Kurt Busiek and George Perez Omnibus Vol 1 1", dict(id="busiek-o1", title="Avengers by Busiek & Pérez Omnibus", vol="Vol. 1",
  creators="Kurt Busiek & George Pérez", era="1998–2000", released="Mar 2015",
  art="o-heroesreturn", tex="tex-krackle", spine="By Busiek & Pérez",
  cover="Art/Avengers/busiek-o1.jpg",
  note="Heroes Return, and the most purely satisfying run the character has. Busiek's premise is that the Avengers are an institution with thirty-five years of paperwork, and Pérez draws every page as if the roster photograph matters — which it does, because #4 is a general muster of dozens of heroes and it is legible. Avengers Forever is printed here too: twelve issues of Busiek, Roger Stern and Carlos Pacheco arguing with the whole publishing history at once, and the best time-travel comic Marvel has.")),
("Avengers by Kurt Busiek and George Perez Omnibus Vol 1 2", dict(id="busiek-o2", title="Avengers by Busiek & Pérez Omnibus", vol="Vol. 2",
  creators="Kurt Busiek & George Pérez", era="2000–2002", released="Nov 2015",
  art="o-heroesreturn", tex="tex-krackle", spine="By Busiek & Pérez",
  cover="Art/Avengers/busiek-o2.jpg",
  note="The back half, and it goes out on Ultron. #19–22 is the story where Ultron kills the population of a country before the first page is over and the Avengers spend four issues failing to be enough — Pérez's most brutal work anywhere. Then the Kang Dynasty, the largest thing the book has attempted: Kang conquers the Earth, holds it, and the ending costs more than the win is worth. Note #55–56 and #1½ were missing from the wiki's own contents here and are restored from Marvel's collecting line.")),
("Avengers by Johns and Coipel Omnibus Vol 1 1", dict(id="johns-o1", title="Avengers by Johns & Coipel Omnibus", vol="",
  creators="Geoff Johns, Olivier Coipel & Ivan Reis", era="2002–2004", released="Dec 2025",
  art="o-heroesreturn", tex="tex-crosshatch", spine="By Johns & Coipel",
  cover="Art/Avengers/johns-o1.jpg",
  note="The last stretch of Avengers (1998) before Bendis takes it apart, and the volume that finally makes it available. Johns runs the team through Red Zone — a bioweapon attack on American soil, written in 2003, about exactly what you would expect — and the Search for She-Hulk, and Coipel arrives drawing figures with a weight the book had not had since Pérez. The four-issue Vision mini is here too, which is the character's own answer to what Byrne did to him.")),
("New Avengers Omnibus Vol 1 1", dict(id="nav-o1", title="New Avengers Omnibus", vol="Vol. 1",
  creators="Brian Michael Bendis & David Finch", era="2004–2007", released="Sep 2012",
  art="o-bendis", tex="tex-crosshatch", chapterby="series", spine="New Avengers",
  cover="Art/Avengers/nav-o1.jpg",
  note="Avengers Disassembled opens the volume — the Scarlet Witch takes the mansion apart in four issues — and then Bendis rebuilds the team out of whoever happened to be standing in a prison riot: Spider-Man, Wolverine, Luke Cage, Spider-Woman. That roster is the argument. It made the book the best-selling thing Marvel had for a decade and it made a lot of readers furious, and both reactions are about the same thing, which is that these are not the Avengers as anyone had defined them.")),
("New Avengers Omnibus Vol 1 2", dict(id="nav-o2", title="New Avengers Omnibus", vol="Vol. 2",
  creators="Brian Michael Bendis, Leinil Yu & Stuart Immonen", era="2006–2010", released="Nov 2025",
  art="o-bendis", tex="tex-crosshatch", spine="New Avengers",
  cover="Art/Avengers/nav-o2.jpg",
  note="After Civil War the team is illegal, and the book becomes very good at being a comic about people hiding. The Illuminati mini is here — the retcon that puts Iron Man, Reed Richards and Namor in a room deciding things for everyone — and then Secret Invasion turns the paranoia literal and Dark Reign hands the country to Norman Osborn. Note the book after this one on the shelf assembles that crossover in reading order, so a couple of dozen issues appear twice, on purpose.")),
("Secret Invasion by Brian Michael Bendis Omnibus Vol 1 1", dict(id="si-o1", title="Secret Invasion by Bendis Omnibus", vol="",
  creators="Brian Michael Bendis, Leinil Yu & Billy Tan", era="2006–2009", released="Aug 2018",
  art="o-bendis", tex="tex-shatter", chapterby="series", spine="Secret Invasion",
  cover="Art/Avengers/si-o1.jpg",
  note="The crossover assembled the way it was meant to be read: the eight-issue core, plus the New Avengers and Mighty Avengers issues carrying the flashbacks, printed in order rather than in blocks. The premise is the best paranoid hook Marvel has run — anyone might have been replaced, for years, and some of them were — and its problem is the one every such story has, which is that the reveal cannot be as good as the wondering. The Skrull landing in the Savage Land is where it is at its best.")),
("New Avengers Omnibus Vol 1 3", dict(id="nav-o3", title="New Avengers Omnibus", vol="Vol. 3",
  creators="Brian Michael Bendis, Stuart Immonen & John Romita Jr.", era="2010–2012", released="Nov 2026",
  art="o-bendis", tex="tex-halftone", spine="New Avengers",
  cover="Art/Avengers/nav-o3.jpg",
  note="Ships November 2026 — it is on the shelf ahead of that because its contents, its links and its jacket are all real, which is the bar a tile has to clear. The Heroic Age relaunch: Luke Cage buys the mansion and runs an Avengers team out of it as a small business, which is the most likeable idea Bendis had on the book. Bundled with it is the first year of the flagship Avengers (2010) with John Romita Jr., which is otherwise uncollected in omnibus.")),
("Avengers vs. X-Men Omnibus Vol 1 1", dict(id="avx-o1", title="Avengers vs. X-Men Omnibus", vol="",
  creators="Bendis, Aaron, Brubaker, Fraction & Hickman", era="2011–2012", released="Jul 2022",
  art="o-clash", tex="tex-shatter", spine="Avengers vs. X-Men",
  cover="Art/Avengers/avx-o1.jpg",
  note="Seventy-four issues, and the honest thing to say is that most of them are X-Men comics. It is here because it is the hinge: the Phoenix Force comes back, five X-Men take it, Cyclops kills Charles Xavier, and the mutant and Avengers lines are joined at the hip for the decade after. The AVX: Vs issues are a fight comic and nothing else, which is either the best or the worst part depending on what you came for.")),
("Avengers by Jonathan Hickman Omnibus Vol 1 1", dict(id="hick-o1", title="Avengers by Jonathan Hickman Omnibus", vol="Vol. 1",
  creators="Jonathan Hickman, Jerome Opeña & Esad Ribíc", era="2012–2013", released="Jul 2017",
  # era is 2012-2013 although YEARS says 2008-2013: the six Astonishing Tales:
  # Mojoworld chapters and the Shang-Chi one-shot in the back are 2008-09
  # reprints. Seven issues out of fifty are not worth a Plastic-Age dot on a
  # Modern-Age Hickman book. Those seven are the ISSUE_ALIAS pins in
  # link_issues.py, for the same reason.
  art="o-hickman", tex="tex-grid", spine="By Hickman",
  cover="Art/Avengers/hick-o1.jpg",
  note="Hickman runs two books as one machine. Avengers is the team getting bigger — “we have to get bigger” is the thesis and very nearly the first line — and New Avengers is the Illuminati in a dark room discovering that universes are colliding and someone has to destroy a world every few weeks. One book is about hope at scale and the other is about what the same men do when nobody is watching, and reading them interleaved, as this volume prints them, is the whole point.")),
("Avengers by Jonathan Hickman Omnibus Vol 1 2", dict(id="hick-o2", title="Avengers by Jonathan Hickman Omnibus", vol="Vol. 2",
  creators="Jonathan Hickman, Leinil Yu & Mike Deodato", era="2013–2015", released="Jul 2018",
  art="o-hickman", tex="tex-grid", spine="By Hickman",
  cover="Art/Avengers/hick-o2.jpg",
  note="The second half, and it is a long controlled fall. Infinity is behind them, Time Runs Out jumps the story eight months forward with the Illuminati as fugitives and Steve Rogers hunting them, and the incursions stop being a problem to solve and become a countdown. It ends with the last two Earths in existence about to touch. Note it stops before Secret Wars itself, which is not on this shelf — that is the whole line's book, not the Avengers'.")),
("Uncanny Avengers Omnibus Vol 1 1", dict(id="unc-o1", title="Uncanny Avengers Omnibus", vol="",
  creators="Rick Remender, John Cassaday & Daniel Acuña", era="2012–2014", released="Feb 2015",
  art="o-clash", tex="tex-crosshatch", spine="Uncanny Avengers",
  cover="Art/Avengers/unc-o1.jpg",
  note="Straight out of AvX: Captain America builds a joint Avengers/X-Men unit as a public-relations answer to a war, and Remender spends twenty-five issues showing why that does not work. The Apocalypse Twins arc goes to the end of the world and stays there — the Scarlet Witch and Rogue's argument in the middle of it is as bleak as this book gets. Cassaday opens it; Acuña's washes are what people remember.")),
("Avengers: No Surrender/No Road Home Omnibus Vol 1 1", dict(id="nsnrh-o1", title="Avengers: No Surrender / No Road Home Omnibus", vol="",
  creators="Al Ewing, Mark Waid, Jim Zub & Pepe Larraz", era="2018–2019", released="Mar 2026",
  art="o-worldtree", tex="tex-starfield", spine="No Surrender",
  cover="Art/Avengers/nsnrh-o1.jpg",
  note="Two weekly experiments, and both are far better than a gimmick has any right to be. No Surrender is sixteen issues in sixteen weeks by three writers working as one — the Earth is stolen and the Grandmaster plays a game with it, and Ewing uses the space to give Voyager a whole invented history and then take it back. No Road Home does the same trick a year later with Nyx and a much smaller cast. Larraz and Larroca on alternating weeks and no visible seam.")),
("Avengers by Jason Aaron Omnibus Vol 1 1", dict(id="aaron-o1", title="Avengers by Jason Aaron Omnibus", vol="Vol. 1",
  creators="Jason Aaron, Ed McGuinness & David Marquez", era="2018–2021", released="Mar 2027",
  art="o-worldtree", tex="tex-krackle", spine="By Jason Aaron",
  cover="Art/Avengers/aaron-o1.jpg",
  note="Ships March 2027, and it is on the shelf under the same rule as the other two unshipped books here. Aaron's premise is that the Avengers are a million years old: Celestials, an Iron Fist and a Ghost Rider in the Stone Age, and a present-day team squatting in a dead god's skull in the Arctic. It is the loudest the book has ever been and it means it — the War of the Realms and the Phoenix tournament are both in here, and McGuinness draws all of it at maximum volume.")),
("Avengers Forever by Jason Aaron Omnibus Vol 1 1", dict(id="forever-o1", title="Avengers Forever by Jason Aaron Omnibus", vol="",
  creators="Jason Aaron, Aaron Kuder & Jim Towe", era="2021–2023", released="Apr 2025",
  art="o-worldtree", tex="tex-grid", chapterby="series", spine="Avengers Forever",
  cover="Art/Avengers/forever-o1.jpg",
  note="The companion book, which is a Multiversal Avengers: a Ghost Rider who is Robbie Reyes, a Deathlok Wonder Man, an Ant-Man who is Tony Stark, and a Moon Knight who is Khonshu's fist, recruited against a Council of Red Skulls. It converges with the main title in Avengers Assemble, which is why this volume alternates the two and why the Alpha and Omega one-shots bracket it. Aaron's exit, and a genuinely strange, generous piece of work.")),
("Avengers by Jed MacKay Omnibus Vol 1 1", dict(id="mackay-o1", title="Avengers by Jed MacKay Omnibus", vol="Vol. 1",
  creators="Jed MacKay, C.F. Villa & Farid Karami", era="2021–2026", released="May 2027",
  art="o-mackay", tex="tex-grid", spine="By Jed MacKay",
  cover="Art/Avengers/mackay-o1.jpg",
  note="Ships May 2027. MacKay's answer to a decade of Avengers books that were about the concept of the Avengers is to write one about a team doing jobs: Captain Marvel leading, Iron Man paying for it, and a Twilight Court of villains organising against them. Blood Hunt runs through it, and so does the Impossible City, which is the best new toy the book has been given in years. This is the shelf's current end — everything after it is still coming out.")),
("Ultimates by Mark Millar & Bryan Hitch Omnibus Vol 1 1", dict(id="ult-o1", title="Ultimates by Millar & Hitch Omnibus", vol="",
  creators="Mark Millar & Bryan Hitch", era="2002–2007", released="Jun 2009",
  art="o-ultimate", tex="tex-widescreen", spine="The Ultimates",
  cover="Art/Avengers/ult-o1.jpg",
  note="The other Avengers, out of continuity and enormously more influential than that sounds — this is the book the films are adapted from, down to Nick Fury's face. Millar writes them as a government asset with a public-relations department and Hitch draws it “widescreen”: six panels a page, every one a shot. The second series is the better one and the harder one, because the argument it is making about American power in 2004 is not subtle and is not flattering either.")),
]

# Nothing pending on this shelf -- every one of the 27 tiles has real contents.
PLACEHOLDERS = []

# Display order of the shelf, by id. A reading order, which here runs close to
# publication order of the MATERIAL rather than of the books. Four placements
# are deliberate:
#
#   * si-o1 sits after nav-o2, not before it. The run comes first; the crossover
#     assembled in reading order comes second, and duplicates part of it.
#   * hick-o1 and hick-o2 stay together and unc-o1 follows them, even though
#     Uncanny Avengers is concurrent with both -- a creator run reads as a unit,
#     the same call that puts millar-o1 before aaron-o1 on the Wolverine shelf.
#   * nsnrh-o1 sits before aaron-o1. No Surrender is early 2018 and is the way
#     out of the previous era; No Road Home is 2019 and overlaps Aaron, but the
#     book bundles them and it reads as the way in.
#   * ult-o1 goes last. It is a different universe rather than a different year,
#     so it is the cross-era outsider, which is the slot the Ultimate volumes
#     take at the end of the Fantastic Four shelf.
SHELF = [
  "av-o1", "av-o2", "av-o3", "av-o4", "av-o5", "av-o6",
  "wca-o1", "wca-o2", "byrne-o1",
  "gather-o1", "crossing-o1",
  "busiek-o1", "busiek-o2", "johns-o1",
  "nav-o1", "nav-o2", "si-o1", "nav-o3",
  "avx-o1", "hick-o1", "hick-o2", "unc-o1",
  "nsnrh-o1", "aaron-o1", "forever-o1", "mackay-o1",
  "ult-o1",
]

PLACEHOLDER_PAGES = {}

# Series these books collect that the shared SERIES table does not carry.
# Only the ones worth PINNING are here: autocode() derives a stable id for
# anything else and reuses a code another shelf already owns, so this table is
# for the cases where the derived code would be ugly or ambiguous. An issue id
# is a saved-progress key, so pin before anyone reads -- which is the window
# CLAUDE.md says to use.
#
# Display names are the marvel.com form (name plus start year) rather than the
# wiki's volume number, because that is what link_issues.py matches on. The
# catalog carries eight series simply called "Avengers" and five called "New
# Avengers", which is exactly the reused-title case its tiebreak() exists for.
SERIES_EXTRA = {
 "Avengers Vol 4":                                     ("av4",     "Avengers (2010)"),
 "Avengers Vol 5":                                     ("av5",     "Avengers (2012)"),
 "Avengers Vol 9":                                     ("av9",     "Avengers (2023)"),
 "Avengers Annual Vol 4":                              ("avann4",  "Avengers Annual (2023)"),
 "New Avengers Vol 1":                                 ("nav",     "New Avengers (2004)"),
 "New Avengers Vol 2":                                 ("nav2",    "New Avengers (2010)"),
 "New Avengers Vol 3":                                 ("nav3",    "New Avengers (2013)"),
 "New Avengers Annual Vol 1":                          ("navann",  "New Avengers Annual"),
 "New Avengers: Illuminati Vol 2":                     ("nail2",   "New Avengers: Illuminati"),
 "Uncanny Avengers Vol 1":                             ("uav",     "Uncanny Avengers (2012)"),
 "Uncanny Avengers Annual Vol 1":                      ("uavann",  "Uncanny Avengers Annual"),
 # NOT `mav`: the Wolverine shelf already keys Maverick (1997) that way, and
 # unlike the West Coast and X-Men adoptions below those are two different
 # comics. A shared, code-keyed id store cannot carry both.
 "Mighty Avengers Vol 1":                              ("mtyav",   "Mighty Avengers (2007)"),
 "Avengers Forever Vol 1":                             ("avfor",   "Avengers Forever (1998)"),
 "Avengers Forever Vol 2":                             ("avfor2",  "Avengers Forever (2021)"),
 "Avengers Forever Infinity Comics Vol 1":             ("avforic", "Avengers Forever Infinity Comic"),
 "Avengers vs. X-Men Vol 1":                           ("avx",     "Avengers Vs. X-Men"),
 "Avengers vs. X-Men: Infinite Vol 1":                 ("avxinf",  "Avengers Vs. X-Men: Infinite"),
 "AVX: Vs Vol 1":                                      ("avxvs",   "Avengers Vs. X-Men: Versus"),
 "AVX: Consequences Vol 1":                            ("avxcon",  "AVX: Consequences"),
 "Avengers Academy Vol 1":                             ("avac",    "Avengers Academy"),
 "Secret Avengers Vol 1":                              ("secav",   "Secret Avengers (2010)"),
 "Avengers No Road Home Vol 1":                        ("anrh",    "Avengers: No Road Home"),
 "Quicksilver: No Surrender Vol 1":                    ("qns",     "Quicksilver: No Surrender"),
 "Avengers Mech Strike Vol 1":                         ("avms",    "Avengers Mech Strike"),
 # `wca` is West Coast Avengers Vol 2 (the 1985 ongoing) on the Fantastic Four
 # shelf, so the 1984 four-issue mini cannot have it -- and autocode's fallback
 # would have called it `wca2`, which reads as the LATER book. Pinned by year.
 "West Coast Avengers Vol 1":                          ("wca84",   "West Coast Avengers (1984)"),
 "West Coast Avengers Annual Vol 1":                   ("wcaann",  "West Coast Avengers Annual"),
 "Vision and the Scarlet Witch Vol 2":                 ("vsw2",    "Vision And The Scarlet Witch (1985)"),
 "Ultimates Vol 1":                                    ("ult",     "Ultimates (2002)"),
 "Ultimates 2 Vol 1":                                  ("ult2",    "Ultimates 2 (2004)"),
 "Ultimates Annual Vol 1":                             ("ultann",  "Ultimates Annual"),
 "Secret Invasion Vol 1":                              ("si",      "Secret Invasion (2008)"),
 "Secret Invasion Prologue Vol 1":                     ("sipro",   "Secret Invasion Prologue"),
 "Secret Invasion: Dark Reign Vol 1":                  ("sidr",    "Secret Invasion: Dark Reign"),
 "Infinity Vol 1":                                     ("inf",     "Infinity (2013)"),
 "Force Works Vol 1":                                  ("fw",      "Force Works"),
 "War Machine Vol 1":                                  ("wm",      "War Machine (1994)"),
 "Thunderbolts Vol 1":                                 ("tbolts",  "Thunderbolts (1997)"),
 "Maximum Security Vol 1":                             ("maxsec",  "Maximum Security"),
 "Avengers Icons: The Vision Vol 1":                   ("vision2", "Vision (2002)"),
 "Giant-Size Avengers Vol 1":                          ("gsav",    "Giant-Size Avengers"),
 "X-Men: Legacy Vol 1":                                ("xmleg",   "X-Men: Legacy"),
 "Wolverine & the X-Men Vol 1":                        ("wxm",     "Wolverine & The X-Men"),
 "Uncanny X-Men Vol 2":                                ("uxm2",    "Uncanny X-Men (2011)"),
 "Avengers: Finale Vol 1":                             ("avfin",   "Avengers Finale"),
 # autocode() keeps one- and two-word names whole, which truncates these three
 # mid-word ("avengersstrikefi", "avengerstimeslid") or acronymises them into
 # noise ("aoitroim"). Pinned before anyone reads with them.
 "Avengers: Strikefile Vol 1":                         ("avstrike", "Avengers: Strikefile"),
 "Avengers: Timeslide Vol 1":                          ("avtime",  "Avengers: Timeslide"),
 "Age of Innocence: The Rebirth of Iron Man Vol 1":    ("aoi",     "Age Of Innocence: The Rebirth Of Iron Man"),
 "New Avengers Finale Vol 1":                          ("navfin",  "New Avengers Finale"),
 "Avengers Assemble Alpha Vol 1":                      ("aalpha",  "Avengers Assemble Alpha"),
 "Avengers Assemble Omega Vol 1":                      ("aomega",  "Avengers Assemble Omega"),
}

# Reused verbatim from the other shelves' own tables. A hero only ever sees the
# shared SERIES table plus its OWN extras, so a series another shelf already
# names has to be repeated here -- with exactly the same short code, because
# marvel_ids.json is shared and the same comic must key the same way on every
# shelf. autocode() would reuse them anyway; they are written out so the codes
# are readable beside the ones above.
SERIES_EXTRA.update({
 "Avengers Vol 1":                                     ("av",      "Avengers"),
 # Two wiki keys, one marvel.com series -- the case CLAUDE.md says needs a
 # person. The Marvel Database splits the 1985 run at its retitling (West Coast
 # Avengers Vol 2 #1-41, then Avengers West Coast Vol 1 #48-102) where the
 # catalog keeps one West Coast Avengers (1985 - 1994) across the whole thing,
 # so the second key has to carry the FIRST key's code or link_issues.py refuses
 # every issue with "already belongs to another shelf series". Same shape for
 # X-Men: the Avengers pages write `X-Men Vol 1` where the FF and Wolverine
 # modules write `Uncanny X-Men Vol 1`, and CLAUDE.md predicted this exact one.
 "Avengers West Coast Vol 1":                          ("wca",     "West Coast Avengers"),
 "X-Men Vol 1":                                        ("uxm",     "X-Men (1963 - 2011)"),
 "Avengers Vol 3":                                     ("av3",     "Avengers (1998)"),
 "Avengers Vol 7":                                     ("av7",     "Avengers (2016)"),
 "Avengers Vol 8":                                     ("av18",    "Avengers (2018)"),
 "West Coast Avengers Vol 2":                          ("wca",     "West Coast Avengers"),
 "Iron Man Vol 1":                                     ("im",      "Iron Man"),
 "Iron Man Vol 3":                                     ("im3",     "Iron Man (1998)"),
 "Captain America Vol 3":                              ("cap3",    "Captain America (1998)"),
 "Thor Vol 2":                                         ("thor2",   "Thor (1998)"),
 "Uncanny X-Men Vol 1":                                ("uxm",     "X-Men (1963 - 2011)"),
 "X-Men Vol 2":                                        ("xm2",     "X-Men (1991)"),
 "Defenders Vol 1":                                    ("defs",    "Defenders (1972)"),
})
