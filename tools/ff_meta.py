# The hand-written half of the Fantastic Four shelf. Same shape as
# omnibus_meta.py and hulk_meta.py -- ORDER (wiki-backed), PLACEHOLDERS (tiles
# with no contents), SHELF (display order by id), PLACEHOLDER_PAGES, and
# SERIES_EXTRA for the series the shared SERIES table in build_omnibus_data.py
# does not already carry.
#
# Scope: the Fantastic Four's own books, plus the two family volumes the user
# asked for by name -- the Thing's solo omnibus and Doctor Doom's Book of Doom.
# Deliberately off the shelf: Marvel Two-In-One (the Thing's team-up book, the
# same call that dropped Marvel Team-Up from the Spider-Man shelf), Fantastic
# Four/Doom 2099, Heroes Reborn, and the Silver Surfer omnibuses.
#
# `chapterby` overrides the automatic chaptering heuristic for one volume.

ORDER = [
("Fantastic Four Omnibus Vol 1 1", dict(id="ff-o1", title="Fantastic Four Omnibus", vol="Vol. 1",
  creators="Stan Lee & Jack Kirby", era="1961–1964", released="Jan 2005",
  art="o-kirby", tex="tex-krackle", spine="Fantastic Four",
  note="Where the Marvel Universe starts. Thirty issues and the first annual, inventing the Skrulls, Doctor Doom, the Puppet Master and Namor's return one month at a time.")),
("Fantastic Four Omnibus Vol 1 2", dict(id="ff-o2", title="Fantastic Four Omnibus", vol="Vol. 2",
  creators="Stan Lee & Jack Kirby", era="1964–1967", released="Jun 2007",
  art="o-kirby", tex="tex-cosmic", spine="Fantastic Four",
  note="The imperial run: the Frightful Four, the Inhumans, Wyatt Wingfoot — and #48–50, the Galactus Trilogy, which is where the book stops being a superhero comic and starts being cosmic.")),
("Fantastic Four Omnibus Vol 1 3", dict(id="ff-o3", title="Fantastic Four Omnibus", vol="Vol. 3",
  creators="Stan Lee & Jack Kirby", era="1967–1970", released="Apr 2015",
  art="o-kirby", tex="tex-negzone", spine="Fantastic Four",
  note="The end of Lee and Kirby together. The Black Panther's debut, Annihilus and the Negative Zone, the Kree Sentry, and Franklin Richards born.")),
("Fantastic Four Omnibus Vol 1 4", dict(id="ff-o4", title="Fantastic Four Omnibus", vol="Vol. 4",
  creators="Stan Lee, John Buscema & John Romita Sr.", era="1969–1972", released="Aug 2021",
  art="o-bronze", tex="tex-halftone", spine="Fantastic Four",
  note="After Kirby. Lee writes on with Buscema and Romita — Agatha Harkness, the Overmind, Annihilus again — and the book closes with The Lost Adventure, the Kirby story Marvel did not print until 2008.")),
("Fantastic Four Omnibus Vol 1 5", dict(id="ff-o5", title="Fantastic Four Omnibus", vol="Vol. 5",
  creators="Roy Thomas, Gerry Conway & John Buscema", era="1972–1975", released="Nov 2024",
  art="o-bronze", tex="tex-krackle", spine="Fantastic Four",
  note="Thomas and Conway hold the line: Thundra, Quicksilver and Crystal's wedding, and Reed shutting down his own son's mind — the decision the next twenty years keep coming back to.")),
("Fantastic Four Omnibus Vol 1 6", dict(id="ff-o6", title="Fantastic Four Omnibus", vol="Vol. 6",
  creators="Roy Thomas, Len Wein, Marv Wolfman & George Pérez", era="1975–1978", released="Jun 2025",
  art="o-perez", tex="tex-cosmic", spine="Fantastic Four",
  note="Pérez arrives on the book that made him, and the Impossible Man, Galactus and the Brute run through it. Closes with the What If? that asks what the Marvel Bullpen would have done with the powers.")),
("Fantastic Four by John Byrne Omnibus Vol 1 1", dict(id="byrne-o1", title="Fantastic Four by John Byrne Omnibus", vol="Vol. 1",
  creators="John Byrne", era="1977–1983", released="Nov 2011",
  art="o-byrne", tex="tex-cosmic", spine="By John Byrne",
  note="Writing and drawing both, Byrne makes this the best-regarded run since Kirby. Opens with the Marvel Team-Ups he drew first, then FF #232 onward — Doom, the Negative Zone, and Sue finally written as the most powerful one in the room.")),
("Fantastic Four by John Byrne Omnibus Vol 1 2", dict(id="byrne-o2", title="Fantastic Four by John Byrne Omnibus", vol="Vol. 2",
  creators="John Byrne", era="1984–1986", released="Dec 2013",
  art="o-byrne", tex="tex-negzone", spine="By John Byrne",
  note="Secret Wars breaks the team up: the Thing stays behind on Battleworld, She-Hulk takes his chair, and Doom comes back remade. Runs to where Byrne walked off the book.")),
("Fantastic Four by Waid & Wieringo Omnibus Vol 1 1", dict(id="waid-o1", title="Fantastic Four by Waid & Wieringo Omnibus", vol="",
  creators="Mark Waid & Mike Wieringo", era="2002–2005", released="Dec 2018",
  art="o-waid", tex="tex-krackle", spine="Waid & Wieringo",
  note="Note the jump — Fantastic Four #296–488 has never been collected in omnibus, so sixteen years pass between this book and Byrne's last one. Waid and Wieringo restart from first principles, and Unthinkable is the best Doom story in decades.")),
("Fantastic Four by Millar & Hitch Omnibus Vol 1 1", dict(id="millar-o1", title="Fantastic Four by Millar & Hitch Omnibus", vol="",
  creators="Mark Millar & Bryan Hitch", era="2008–2009", released="Apr 2023",
  art="o-millar", tex="tex-cosmic", spine="Millar & Hitch",
  note="Widescreen and loud: the Marquis of Death, Doom's origin retold, Ben's wedding, and Marvel 1985 collected alongside as the odd one out.")),
("Fantastic Four by Jonathan Hickman Omnibus Vol 1 1", dict(id="hick-o1", title="Fantastic Four by Jonathan Hickman Omnibus", vol="Vol. 1",
  creators="Jonathan Hickman, Dale Eaglesham & Steve Epting", era="2009–2011", released="Oct 2013",
  art="o-hickman", tex="tex-negzone", spine="By Hickman",
  note="The long game. The Council of Reeds, the Future Foundation, the War of Four Cities being set up years before it lands — and the death that turns Fantastic Four into FF.")),
("Fantastic Four by Jonathan Hickman Omnibus Vol 1 2", dict(id="hick-o2", title="Fantastic Four by Jonathan Hickman Omnibus", vol="Vol. 2",
  creators="Jonathan Hickman, Steve Epting & Barry Kitson", era="2011–2012", released="Nov 2014",
  art="o-hickman", tex="tex-cosmic", spine="By Hickman",
  note="Both books at once — FF and the restored Fantastic Four, month by month — through to #611, where every thread planted in Vol. 1 is paid off at the same time.")),
("Fantastic Four by Matt Fraction Omnibus Vol 1 1", dict(id="frac-o1", title="Fantastic Four by Matt Fraction Omnibus", vol="",
  creators="Matt Fraction, Mark Bagley & Michael Allred", era="2012–2013", released="Feb 2015",
  art="o-fraction", tex="tex-krackle", spine="By Fraction",
  note="A family road trip through space and time, while a substitute team minds the Baxter Building and Allred draws them. Both Marvel NOW! series in one book.")),
("Fantastic Four by Dan Slott Omnibus Vol 1 1", dict(id="slott-o1", title="Fantastic Four by Dan Slott Omnibus", vol="Vol. 1",
  creators="Dan Slott, Sara Pichelli & Aaron Kuder", era="2018–2020", released="Jul 2026",
  art="o-slott", tex="tex-cosmic", spine="By Dan Slott",
  note="The family comes home after Secret Wars. Ben and Alicia's wedding, the Griever at the End of All Things, and Doom written as the most dangerous man alive again.")),
("Fantastic Four by Dan Slott Omnibus Vol 1 2", dict(id="slott-o2", title="Fantastic Four by Dan Slott Omnibus", vol="Vol. 2",
  creators="Dan Slott, R.B. Silva & Rachael Stott", era="2020–2022", released="Announced",
  art="o-slott", tex="tex-negzone", spine="By Dan Slott",
  note="The back half of the run, ending in the Reckoning War. Solicited for December 2026.")),
("Thing Omnibus Vol 1 1", dict(id="thing-o1", title="Thing Omnibus", vol="",
  creators="John Byrne, Mike Carlin & Ron Wilson", era="1983–1991", released="Dec 2022",
  art="o-thing", tex="tex-halftone", spine="The Thing",
  note="Ben Grimm on his own, spun out of Byrne's run and meant to be read alongside it — which is why it sits between the two Byrne volumes here. Its first two issues are in Byrne Vol. 1 as well, and share their ids.")),
("Doctor Doom: The Book of Doom Omnibus Vol 1 1", dict(id="doom-o1", title="Doctor Doom: The Book of Doom Omnibus", vol="",
  creators="Stan Lee, Jack Kirby, Roy Thomas & Wally Wood", era="1962–1977", released="Aug 2022",
  art="o-doom", tex="tex-halftone", chapterby="series", spine="Book of Doom",
  note="Latveria's side of the story, gathered across fifteen years and a dozen titles, so it doubles back over the Lee/Kirby volumes and shares their ids. Astonishing Tales and Super-Villain Team-Up are the parts hardest to find anywhere else.")),
("Ultimate Fantastic Four Omnibus Vol 1 1", dict(id="uff-o1", title="Ultimate Fantastic Four Omnibus", vol="Vol. 1",
  creators="Brian Michael Bendis, Mark Millar & Adam Kubert", era="2004–2006", released="Mar 2025",
  art="o-ultimate", tex="tex-negzone", spine="Ultimate FF",
  note="A separate universe and a younger team — the accident is a teleporter, not a rocket, and Reed is a prodigy the government keeps in a building with the others. Marvel Zombies starts here.")),
("Ultimate Fantastic Four Omnibus Vol 1 2", dict(id="uff-o2", title="Ultimate Fantastic Four Omnibus", vol="Vol. 2",
  creators="Mike Carey, Mark Millar & Pasqual Ferry", era="2006–2009", released="Apr 2026",
  art="o-ultimate", tex="tex-cosmic", spine="Ultimate FF",
  note="Ultimate Doom, the back half of Ultimate Extinction, and the crossovers that close the line out before Ultimatum ends it.")),
]

# Nothing pending on this shelf.
PLACEHOLDERS = []

# Display order of the shelf, by id. A reading order, not publication order:
# the Thing's solo book sits between the two Byrne volumes because that is
# where it was published and where it reads, and the two cross-era anthologies
# (Doom, Ultimate) sit at the end rather than interrupting the main line.
SHELF = [
  "ff-o1", "ff-o2", "ff-o3", "ff-o4", "ff-o5", "ff-o6",
  "byrne-o1", "thing-o1", "byrne-o2",
  "waid-o1", "millar-o1",
  "hick-o1", "hick-o2", "frac-o1",
  "slott-o1", "slott-o2",
  "doom-o1",
  "uff-o1", "uff-o2",
]

PLACEHOLDER_PAGES = {}

# Series these books collect that the shared SERIES table does not carry.
SERIES_EXTRA = {
}
