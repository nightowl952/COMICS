# -*- coding: utf-8 -*-
"""The X-Men guided tour.

This shelf is unlike the other nine: four books Marvel has never printed,
holding one researched chronological read of 2008-2010. So the character tour
does the franchise's publishing history first and then explains why the shelf
stops where it does -- and every volume tour has to be honest that the book
does not exist.

See tools/tours/hulk.py for the field list.
"""

A = "Art/Tours/xmen/"

OVERVIEW = {
    "kicker": "Guided tour",
    "title": "The X-Men, decade by decade",
    "lede": (
        "The X-Men failed. Lee and Kirby's 1963 series sold badly enough that Marvel stopped "
        "commissioning new stories for it in 1970 and ran reprints for five years. Everything "
        "the franchise became &mdash; the biggest property in American comics for two decades "
        "&mdash; comes from one relaunch in 1975 and one writer who then stayed for sixteen "
        "years. <b>This shelf is four books Marvel has never printed</b>, holding a researched "
        "reading order for 2008&ndash;2010; the tour below places that era in the sixty years "
        "around it."),
    "sections": [
        {
            "era": "Silver", "years": "1963–1970",
            "h": "The one that did not work",
            "body": [
                "<i>The X-Men</i> #1, September 1963. Lee and Kirby, and by the standards of "
                "what they were producing that year it is the least inspired: five teenagers in "
                "matching uniforms at a school, with a premise &mdash; born different, hated "
                "for it &mdash; that the book barely uses.",
                "It sold poorly for seven years. In 1970 Marvel stopped producing new material "
                "and <b>ran reprints in it until 1975</b>, which is as close to cancellation as "
                "a title gets while still existing.",
                "Worth knowing because it makes the point that nothing about this franchise was "
                "inevitable. The idea was there in 1963 and nobody could make it work."],
            "fig": {"src": [A + "xm1963-1.jpg"],
                    "cap": "#1, 1963. Five teenagers and Magneto, and it did not sell."},
            "shelf": [],
        },
        {
            "era": "Bronze", "years": "1975–1981",
            "h": "Giant-Size X-Men #1, and then Claremont for sixteen years",
            "body": [
                "<b>Giant-Size X-Men</b> #1 in 1975, by Len Wein and <b>Dave Cockrum</b>, "
                "replaces the cast with an international one &mdash; Storm, Nightcrawler, "
                "Colossus, Banshee, Sunfire, Thunderbird and Wolverine &mdash; and suddenly the "
                "premise has something to be about.",
                "<b>Chris Claremont</b> starts writing at #94 and does not stop until #279. "
                "<b>Sixteen years</b> is the longest run on a major Marvel title by anyone, and "
                "it is where nearly everything now associated with the X-Men was built: the "
                "soap-operatic ensemble, the thought-caption interiority, characters who change "
                "permanently, and women written as protagonists rather than as love interests.",
                "With <b>John Byrne</b> he produced the two stories the franchise is still "
                "living on. <b>The Dark Phoenix Saga</b> (#129&ndash;138) &mdash; a member of "
                "the team becomes a god, commits genocide, and dies for it &mdash; and "
                "<b>Days of Future Past</b> (#141&ndash;142), a two-issue dystopia that has "
                "been remade endlessly since.",
                "Look at the #141 cover: a wanted poster with faces crossed out. That single "
                "image is one of the most imitated in comics."],
            "fig": {"src": [A + "gsxm-1.jpg", A + "xm-141.jpg"],
                    "cap": "<b>Left:</b> the 1975 relaunch that saved it. <b>Right:</b> "
                           "<i>Days of Future Past</i> &mdash; a poster, and names struck "
                           "through."},
            "makers": [
                {"n": "Chris Claremont", "r": "Writer, 1975–91",
                 "b": "Watch the <b>thought captions</b>. Claremont gives everyone an interior "
                      "voice and runs several at once across a scene, so a fight is also four "
                      "people privately reacting to each other. It is enormously wordy by "
                      "modern standards and it is why readers cared about this cast rather "
                      "than any other team."},
                {"n": "John Byrne", "r": "Pencils, 1977–81",
                 "b": "Byrne's contribution is <b>clarity at scale</b> &mdash; regular grids, "
                      "readable staging, and the discipline to hold a splash page back. A "
                      "thirteen-person cast in a fight is legible because of the layouts."}],
            "shelf": [],
        },
        {
            "era": "Copper", "years": "1982–1991",
            "h": "The biggest thing in comics, and the best-selling issue ever printed",
            "body": [
                "Through the 1980s the X-Men become Marvel's commercial engine, and the "
                "franchise starts multiplying &mdash; <i>New Mutants</i>, <i>X-Factor</i>, "
                "<i>Excalibur</i>, <i>Wolverine</i>.",
                "The artists are the story of the decade: <b>Paul Smith</b>, <b>John Romita "
                "Jr.</b>, <b>Marc Silvestri</b>, and then <b>Jim Lee</b>, whose slick, "
                "high-detail rendering became the most imitated style in the industry.",
                "In 1991 Claremont and Jim Lee launched a second title, and <b><i>X-Men</i> #1 "
                "sold roughly 8.1 million copies</b> &mdash; still the Guinness record for the "
                "best-selling single comic issue ever published, and a number no comic will "
                "reach again.",
                "Claremont left within months, over creative control. Sixteen years ended "
                "immediately after the biggest commercial success in the medium's history, "
                "which tells you something about who the industry thought the value belonged "
                "to."],
            "fig": {"src": [A + "xm-137.jpg", A + "xm1991-1.jpg"],
                    "cap": "<b>Left:</b> #137, the end of Dark Phoenix. <b>Right:</b> the 1991 "
                           "#1 &mdash; 8.1 million copies, and Claremont was gone within the "
                           "year."},
            "shelf": [],
        },
        {
            "era": "Plastic", "years": "2001–2007",
            "h": "Morrison reinvents it; Whedon puts it back; House of M breaks it",
            "body": [
                "<b>Grant Morrison's New X-Men</b> (2001&ndash;2004) is the most drastic "
                "reinvention the franchise has had. Leather instead of spandex, the school "
                "actually functioning as a school, mutation as a <i>culture</i> with fashion "
                "and slang and politics rather than a metaphor, and <b>Frank Quitely</b> "
                "drawing it in a style nobody had used on a Marvel monthly.",
                "It is celebrated and genuinely divisive in equal measure, and almost every "
                "subsequent X-Men writer is responding to it.",
                "<b>Joss Whedon and John Cassaday's Astonishing X-Men</b> (2004) does the "
                "opposite: the costumes come back, the tone becomes classical adventure, and "
                "Cassaday's clean widescreen art makes it the most accessible X-Men book in "
                "twenty years.",
                "Then <b>House of M</b> (2005), and the line changes shape completely: the "
                "Scarlet Witch says <i>no more mutants</i> and the population drops from "
                "millions to <b>198</b>. Overnight the franchise stops being about a persecuted "
                "minority and becomes about an <b>endangered species</b>, which is what makes "
                "this shelf's era possible."],
            "fig": {"src": [A + "nxm-114.jpg", A + "axm-1.jpg"],
                    "cap": "<b>Left:</b> Quitely's <i>E is for Extinction</i>. <b>Right:</b> "
                           "Cassaday's <i>Astonishing</i> &mdash; two answers to the same "
                           "question, three years apart."},
            "shelf": [],
        },
        {
            "era": "Plastic", "years": "2007–2010",
            "h": "The Messiah trilogy — which is what this shelf actually is",
            "body": [
                "After <i>House of M</i> no mutant is born for two years. Then one is, and the "
                "line runs a <b>three-part story across three years</b>:",
                "<b>Messiah Complex</b> (2007) &mdash; the first mutant birth since M-Day, and "
                "everyone races for the child. <b>Messiah War</b> (2009) &mdash; Cable raising "
                "her on the run through the future, with X-Force sent after them. <b>Second "
                "Coming</b> (2010) &mdash; she comes home, and the cost is paid.",
                "This shelf is <b>the second and third chapters plus everything around them</b>, "
                "in a researched chronological order rather than publication order. "
                "<i>Messiah Complex</i> itself is not on it; the read opens on X-Men Legacy "
                "#208, which resolves the head wound Xavier takes on Complex's last page.",
                "What makes the era worth reading as a unit is that the whole line was pointed "
                "at one story for three years, which the X-books had not managed before and "
                "have rarely managed since. Utopia &mdash; the X-Men seceding onto an island "
                "&mdash; is set up here, and it is the direct ancestor of the Krakoa era a "
                "decade later.",
                "<b>These four books do not exist.</b> Marvel has collected almost none of this "
                "era and no part of it in omnibus. The volumes are mock-ups; the reading order "
                "inside them is the real work."],
            "fig": {"src": [A + "unc-500.jpg", A + "sc-1.jpg"],
                    "cap": "<b>Left:</b> Uncanny #500 &mdash; the move to San Francisco. "
                           "<b>Right:</b> <i>Second Coming</i>, where it ends."},
            "shelf": ["xm-o1", "xm-o2", "xm-o3", "xm-o4"],
        },
    ],
    "tone": {
        "h": "The tone map",
        "sub": "Four mock-up volumes covering three years, and they are not the same book. "
               "Every one of these is a different corner of the same line.",
        "modes": [
            {"l": "Most character-driven",
             "b": "The fallout volume &mdash; a team scattered, Xavier rebuilding himself, and "
                  "the quiet work of deciding what the X-Men are for now.",
             "vols": ["xm-o1"]},
            {"l": "Darkest",
             "b": "X-Force and the Messiah War. A black-ops mutant kill squad and a "
                  "post-apocalyptic future. This is the era at its most brutal.",
             "vols": ["xm-o2"]},
            {"l": "Most political",
             "b": "Utopia &mdash; Norman Osborn running national security, and the X-Men "
                  "responding by seceding onto an island. The direct ancestor of Krakoa.",
             "vols": ["xm-o3"]},
            {"l": "Biggest",
             "b": "Necrosha and Second Coming. The whole line pointed at one story, and a "
                  "finale that actually costs something.",
             "vols": ["xm-o4"]},
        ],
    },
}


def _v(k, t, l, s, v):
    return {"kicker": k, "title": t, "lede": l, "sections": s, "verdict": v}


NOT_PRINTED = ("<b>This book does not exist.</b> Marvel has never collected this era in "
               "omnibus, so the volume is a mock-up: the cover is the cover of the issue it is "
               "named after, and the cut points are the only new curation. Everything inside is "
               "a researched chronological reading order.")

VOLUMES = {

"xm-o1": _v("Volume 01 · 2008", "X-Men: Divided We Stand Omnibus",
    "The fallout. A team that has broken up, a leader shot in the head, and the line quietly "
    "deciding what the X-Men are for now.",
    [{"era": "Plastic", "years": "2008",
      "h": "Starting on a wound, not a bang",
      "body": [
          "The read opens on <b>X-Men Legacy #208</b> rather than on an event, and that is "
          "deliberate: it resolves the head wound Xavier takes on the last page of "
          "<i>Messiah Complex</i>, and <b>Mike Carey</b> then spends a long run walking through "
          "the character's memory and undoing forty years of his own worst decisions.",
          "The other half is the founding of <b>X-Force</b> as a black-ops kill squad under "
          "Wolverine &mdash; Kyle and Yost writing a book about people doing something the "
          "X-Men have always said they do not do &mdash; and Brubaker moving the team to San "
          "Francisco in <i>Uncanny</i>.",
          "It is the quietest of the four volumes and the one that does the most setup."],
      "fig": {"src": [A + "leg-208.jpg", A + "xfo-1.jpg"],
              "cap": "<b>Left:</b> <i>X-Men Legacy</i>. <b>Right:</b> the new X-Force &mdash; "
                     "note the costumes are black and the logo is a target."}},
     {"era": "Plastic", "years": "—",
      "h": "About this volume",
      "body": [NOT_PRINTED]}],
    {"standing": "The setup", "cls": "",
     "body": ["<b>Carey's <i>X-Men Legacy</i> is the sleeper of the whole era</b> and is "
              "regularly named by readers as the best-written X-book of its period &mdash; a "
              "slow, careful character study running underneath a line full of events.",
              "<b>X-Force</b> divides people sharply, and did at the time: a sanctioned "
              "mutant murder squad is either the honest consequence of a species facing "
              "extinction or a betrayal of the premise, depending on who you ask. The book "
              "knows it is provocative and leans in.",
              "The San Francisco relocation is generally well liked and under-used."]}),

"xm-o2": _v("Volume 02 · 2008–2009", "X-Men: Messiah War Omnibus",
    "The middle chapter of the trilogy, and the darkest stretch on this shelf: a child raised "
    "on the run through a ruined future, with a kill squad sent after her.",
    [{"era": "Plastic", "years": "2008–2009",
      "h": "Cable, Hope, and the future",
      "body": [
          "<b>Duane Swierczynski</b> writes Cable as a man carrying an infant across a "
          "post-apocalyptic timeline, jumping forward whenever he is caught, and it is the best "
          "use anyone has made of that character: the whole premise of a soldier from the "
          "future is finally about <i>protecting</i> something rather than shooting it.",
          "<b>Messiah War</b> is the crossover itself &mdash; X-Force sent after them, "
          "Stryfe waiting, and Deadpool of all people supplying the volume's best material.",
          "This is where the era is most openly about <b>what people will do for a species "
          "that is dying</b>, and the answer the book gives is not flattering.",
          "One reading-order note is flagged on the page: X-Force #12&ndash;13 sits before the "
          "crossover here, in publication order, and some guides argue it should follow it."]},
     {"era": "Plastic", "years": "—",
      "h": "About this volume",
      "body": [NOT_PRINTED]}],
    {"standing": "The strong middle", "cls": "",
     "body": ["<b>Swierczynski's Cable is widely underrated</b> and is the part of this era "
              "readers most often say they were surprised by &mdash; a genuinely affecting "
              "book about a soldier and a baby, in a line otherwise doing events.",
              "<i>Messiah War</i> itself gets a cooler reception: the recurring criticism is "
              "that it is <b>needlessly grim</b> and that the crossover machinery interrupts "
              "the better ongoing story. Middle chapters of trilogies rarely fare well and "
              "this is no exception.",
              "The 49 issues here make it the fattest of the four volumes."]}),

"xm-o3": _v("Volume 03 · 2009", "X-Men: Utopia Omnibus",
    "Norman Osborn is running national security, and the X-Men respond by seceding from the "
    "United States onto an island. The most political volume on the shelf.",
    [{"era": "Plastic", "years": "2009",
      "h": "Secession",
      "body": [
          "<b>Matt Fraction</b>'s answer to a hostile state is not to fight it but to leave: "
          "Cyclops moves the entire mutant population onto a raised platform off San Francisco "
          "and declares it sovereign.",
          "That is a much bigger idea than it was treated as at the time, and it is the "
          "<b>direct ancestor of the Krakoa era</b> ten years later &mdash; the X-Men as a "
          "nation rather than a team is first argued here.",
          "It is also where <b>Cyclops stops being a boy scout</b>. The Utopia era is the "
          "making of the modern Scott Summers: a wartime leader making decisions the book does "
          "not endorse.",
          "<i>Nation X</i> follows, and is quieter &mdash; life on the island, which is the "
          "kind of material the line almost never makes room for."]},
     {"era": "Plastic", "years": "—",
      "h": "About this volume",
      "body": [NOT_PRINTED]}],
    {"standing": "Better in hindsight", "cls": "",
     "body": ["Reception at the time was mixed &mdash; the Dark Reign crossover elements were "
              "criticised as an interruption, and Osborn-as-everything was wearing thin "
              "line-wide by 2009.",
              "It has <b>gained in reputation considerably</b> since Krakoa, because readers "
              "can now see that the central idea was not a one-off event but the beginning of "
              "the franchise's next twenty years.",
              "Fraction's Cyclops is the part that divides people most, and it is the part "
              "that mattered most."]}),

"xm-o4": _v("Volume 04 · 2009–2010", "X-Men: Second Coming Omnibus",
    "The finale. Necrosha first, then Hope comes home, and the trilogy pays what it owes.",
    [{"era": "Plastic", "years": "2009–2010",
      "h": "Paying it",
      "body": [
          "<b>Necrosha</b> opens the volume &mdash; Selene raising the X-Men's dead, which is a "
          "long shopping list of the franchise's history &mdash; and it reads better here than "
          "it did monthly, because the shelf places it as the deep breath before the finale.",
          "Then <b>Second Coming</b>: the entire line, thirteen weeks, one story, and a "
          "genuine cost. Characters die and stay dead. The dome over San Francisco is the "
          "era's best image.",
          "What makes it work is the three years underneath it. Everything the previous "
          "volumes set up &mdash; X-Force's methods, Cable's parenthood, Cyclops's hardening, "
          "the species question &mdash; is what the ending is about.",
          "Note the volume boundaries here are the shelf's own: cutting mid-Act-V rather than "
          "on the old act boundaries is what gives four books of real omnibus size."]},
     {"era": "Plastic", "years": "—",
      "h": "About this volume",
      "body": [NOT_PRINTED]}],
    {"standing": "The payoff", "cls": "",
     "body": ["<b><i>Second Coming</i> is very well regarded</b> and is generally treated as "
              "one of the better X-Men crossovers &mdash; specifically because it was allowed "
              "to have consequences that stuck, which the line had been bad at for years.",
              "<i>Necrosha</i> is the weaker half by consensus: an event about resurrected "
              "characters that is largely a nostalgia exercise, and one that sits awkwardly "
              "against a finale about death mattering.",
              "As an ending to three years it satisfies, which is rare. This is the volume the "
              "shelf is built toward."]}),

}

TOUR = {"overview": OVERVIEW, "volumes": VOLUMES}
