# The hand-written half of the Spider-Man shelf.
#
# ORDER holds the volumes whose contents come from the Marvel Database wiki --
# the key is the wiki page title, and it MUST exist in omnibus_contents_raw.json
# or gen() will KeyError.
#
# PLACEHOLDERS holds volumes that are on the shelf but have no issue list yet.
# They are not wiki-backed, carry no contents, and render as a "Cover pending"
# tile. Give one a real wiki page + a raw-contents entry and move it into ORDER
# to promote it to a full volume.
#
# SHELF is the display order of the whole shelf, by id. It is the curated
# reading order, not publication order.
#
# `art`/`tex` pick the CSS cover treatment.

ORDER = [
("Amazing Spider-Man Omnibus Vol 1 1", dict(id="asm-o1", title="Amazing Spider-Man Omnibus", vol="Vol. 1",
  creators="Stan Lee & Steve Ditko", era="1962–1966", released="Apr 2007", art="o-ditko", tex="tex-halftone",
  note="The complete Lee/Ditko run. Everything Spider-Man is starts here — Amazing Fantasy #15 through the Master Planner saga and Ditko's exit.")),
("Amazing Spider-Man Omnibus Vol 1 2", dict(id="asm-o2", title="Amazing Spider-Man Omnibus", vol="Vol. 2",
  creators="Stan Lee & John Romita Sr.", era="1966–1968", released="Apr 2012", art="o-romita", tex="tex-halftone",
  note="Romita takes over. The Green Goblin's identity, Mary Jane's entrance, the Kingpin's debut, and \"Spider-Man No More!\"")),
("Amazing Spider-Man Omnibus Vol 1 3", dict(id="asm-o3", title="Amazing Spider-Man Omnibus", vol="Vol. 3",
  creators="Lee, Romita Sr. & Gil Kane", era="1968–1971", released="May 2017", art="o-romita", tex="tex-web",
  note="The Stone Tablet saga, Captain Stacy's death, the Comics Code-defying drug issues, and Morbius's debut.")),
("Amazing Spider-Man Omnibus Vol 1 4", dict(id="asm-o4", title="Amazing Spider-Man Omnibus", vol="Vol. 4",
  creators="Gerry Conway & Ross Andru", era="1972–1975", released="May 2019", art="o-conway", tex="tex-web",
  note="The Night Gwen Stacy Died, the death of the Green Goblin, and the first Punisher and Clone Saga.")),
("Untold Tales of Spider-Man Omnibus Vol 1 1", dict(id="utsm-o1", title="Untold Tales of Spider-Man Omnibus", vol="",
  creators="Kurt Busiek & Pat Olliffe", era="Set 1962–1965", released="Apr 2012", art="o-untold", tex="tex-halftone",
  note="Published 1995–97 but set between the early Lee/Ditko issues. Slots here by story chronology, not print date — read it alongside Omnibus Vol. 1 or straight after.")),
("Spider-Man by Roger Stern Omnibus Vol 1 1", dict(id="stern-o1", title="Spider-Man by Roger Stern Omnibus", vol="",
  creators="Roger Stern, JRJR & John Byrne", era="1980–1984", released="Apr 2014", art="o-stern", tex="tex-web",
  note="The Hobgoblin mystery, \"The Kid Who Collects Spider-Man,\" and Nothing Can Stop the Juggernaut.")),
("Amazing Spider-Man by David Michelinie and Todd McFarlane Omnibus Vol 1 1", dict(id="mcf-o1", title="ASM by Michelinie & McFarlane Omnibus", vol="",
  creators="David Michelinie & Todd McFarlane", era="1987–1990", released="Aug 2011", art="o-mcfarlane", tex="tex-web",
  note="ASM #300 — the first full Venom. McFarlane's run that reset what a Spider-Man comic looked like.")),
("Spider-Man by David Michelinie and Erik Larsen Omnibus Vol 1 1", dict(id="larsen-o1", title="Spider-Man by Michelinie & Larsen Omnibus", vol="",
  creators="David Michelinie & Erik Larsen", era="1990–1991", released="Jun 2017", art="o-larsen", tex="tex-burst",
  note="Picks up directly from the McFarlane omnibus. Overlaps it at ASM #324, #327 and #329.")),
("Spider-Man by Todd McFarlane Omnibus Vol 1 1", dict(id="mcf-o2", title="Spider-Man by Todd McFarlane Omnibus", vol="",
  creators="Todd McFarlane", era="1990–1991", released="Aug 2016", art="o-mcfarlane", tex="tex-web",
  note="The adjectiveless Spider-Man #1 — one of the best-selling comics ever printed — and McFarlane's solo writer/artist run.")),
("Spider-Man: Clone Saga Omnibus Vol 1 1", dict(id="clone-o1", title="Spider-Man: Clone Saga Omnibus", vol="Vol. 1",
  creators="Various", era="1994–1995", released="Oct 2016", art="o-clone", tex="tex-burst",
  note="Printed in true crossover reading order — Web, Amazing, Spider-Man and Spectacular interleave month by month, which is how the chapters below are grouped.")),
("Spider-Man: Clone Saga Omnibus Vol 1 2", dict(id="clone-o2", title="Spider-Man: Clone Saga Omnibus", vol="Vol. 2",
  creators="Various", era="1995", released="Nov 2017", art="o-clone", tex="tex-burst",
  note="Maximum Clonage and the Jackal's endgame. Also interleaved in reading order.")),
("Spider-Man: Ben Reilly Omnibus Vol 1 1", dict(id="ben-o1", title="Spider-Man: Ben Reilly Omnibus", vol="Vol. 1",
  creators="Various", era="1995–1996", released="Jan 2019", art="o-benreilly", tex="tex-burst",
  note="Ben Reilly takes over as Spider-Man. The Scarlet Spider titles and the Sensational relaunch.")),
]

# No wiki page, no contents -- shelf tiles only. `released` is deliberately not a
# date: these are pending in the tracker, which says nothing about whether the
# book is in print.
PLACEHOLDERS = [
dict(id="vs-venom-o1", title="Spider-Man vs. Venom Omnibus", vol="",
  creators="Various", era="1988–1994", released="Contents pending",
  art="o-placeholder", tex="tex-halftone", placeholder=True, chapters=[],
  note="Placeholder — the issue list for this volume has not been added to the tracker yet."),
dict(id="venom-o1", title="Venomnibus", vol="Vol. 1",
  creators="Various", era="1988–1995", released="Contents pending",
  art="o-placeholder", tex="tex-halftone", placeholder=True, chapters=[],
  note="Placeholder — the issue list for this volume has not been added to the tracker yet."),
dict(id="venom-o2", title="Venomnibus", vol="Vol. 2",
  creators="Various", era="1995–1998", released="Contents pending",
  art="o-placeholder", tex="tex-halftone", placeholder=True, chapters=[],
  note="Placeholder — the issue list for this volume has not been added to the tracker yet."),
dict(id="jms-o1", title="Amazing Spider-Man by J. Michael Straczynski Omnibus", vol="",
  creators="J. Michael Straczynski & John Romita Jr.", era="2001–2007", released="Contents pending",
  art="o-placeholder", tex="tex-halftone", placeholder=True, chapters=[],
  note="Placeholder — the issue list for this volume has not been added to the tracker yet."),
dict(id="ult-o1", title="Ultimate Spider-Man Omnibus", vol="",
  creators="Brian Michael Bendis & Mark Bagley", era="2000–2009", released="Contents pending",
  art="o-placeholder", tex="tex-halftone", placeholder=True, chapters=[],
  note="Placeholder — the issue list for this volume has not been added to the tracker yet."),
dict(id="ult-death-o1", title="Death of Ultimate Spider-Man Omnibus", vol="",
  creators="Brian Michael Bendis & Mark Bagley", era="2010–2011", released="Contents pending",
  art="o-placeholder", tex="tex-halftone", placeholder=True, chapters=[],
  note="Placeholder — the issue list for this volume has not been added to the tracker yet."),
]

# Display order of the shelf, by id. Curated reading order.
SHELF = [
  "asm-o1", "asm-o2", "asm-o3", "asm-o4",
  "utsm-o1", "stern-o1", "mcf-o1", "larsen-o1",
  "vs-venom-o1", "venom-o1", "venom-o2",
  "mcf-o2", "clone-o1", "clone-o2", "ben-o1",
  "jms-o1", "ult-o1", "ult-death-o1",
]
