# -*- coding: utf-8 -*-
"""The Captain America guided tour.  See tools/tours/hulk.py for the field list."""

A = "Art/Tours/captain-america/"

OVERVIEW = {
    "kicker": "Guided tour",
    "title": "Captain America, decade by decade",
    "lede": (
        "No other character on this site carries a country's name, and that is the whole "
        "problem and the whole appeal. <b>Every era of this book is an argument about what "
        "America is</b>, conducted by whoever happened to be writing it &mdash; which means "
        "Captain America is a Second World War propaganda hero, a 1970s conspiracy thriller, "
        "an 80s corporate satire, a spy novel and a book about national myth, and all of those "
        "are on this shelf."),
    "sections": [
        {
            "era": "Golden", "years": "1941–1943",
            "h": "A year before America was in the war",
            "body": [
                "<b>Captain America Comics</b> #1 is cover-dated March 1941. The United States "
                "did not enter the war until December. The cover is Cap punching Hitler in the "
                "jaw, and <b>Joe Simon and Jack Kirby</b>, both Jewish, meant it as a political "
                "statement at a moment when American opinion was genuinely divided about "
                "intervention. They received hate mail and threats over it.",
                "It sold enormously &mdash; reportedly close to a million copies a month at "
                "its peak, which was Superman territory.",
                "The comics themselves are Golden Age anthology books: each issue is several "
                "complete stories, breakneck, crude and enormously energetic. <b>Kirby's "
                "layouts are the reason to read them</b> &mdash; even in 1941 he is breaking "
                "panel borders and throwing figures at the reader in a way nobody else was.",
                "Simon and Kirby left after #10 in a dispute over money, and a nineteen-"
                "year-old Stan Lee wrote some of what followed."],
            "fig": {"src": [A + "cac-1.jpg"],
                    "cap": "March 1941. Nine months before Pearl Harbor, on newsstands across "
                           "a country arguing about whether to get involved."},
            "shelf": ["ga-o1", "ga-o2"],
        },
        {
            "era": "Silver", "years": "1964–1969",
            "h": "The thaw, and Kirby working out the fight scene",
            "body": [
                "He came back in 1964, frozen for twenty years and grieving, and for five years "
                "he shared <i>Tales of Suspense</i> with Iron Man at ten pages an issue.",
                "Those ten-page chapters are where <b>Kirby invents the Captain America action "
                "sequence</b> &mdash; the shield thrown and ricocheting, the leap into a room "
                "of soldiers, the whole visual grammar. With no space for plot he had to make "
                "the fighting itself the content, and it is a masterclass.",
                "The title splits at <b>#100</b> in 1968. The Red Skull and the Cosmic Cube "
                "arrive properly, and Bucky's death is finally told rather than referred to.",
                "<b>Jim Steranko</b> drops in for three issues (#110, #111 and #113) and they "
                "are among the most formally adventurous pages Marvel published in the decade "
                "&mdash; psychedelic, cinematic, built out of montage and unusual panel shapes."],
            "fig": {"src": [A + "tos-59.jpg", A + "cap-111.jpg"],
                    "cap": "<b>Left:</b> sharing a book with Iron Man. <b>Right:</b> "
                           "Steranko's #111 &mdash; a composition no other Marvel cover of 1969 "
                           "would have attempted."},
            "makers": [
                {"n": "Jack Kirby", "r": "Pencils, 1964–69 and 1976–77",
                 "b": "Watch the <b>shield</b>. Kirby choreographs it as a third character "
                      "&mdash; thrown, ricocheting off three surfaces, caught behind the back "
                      "&mdash; and he draws the arc with motion lines that make the throw "
                      "readable in a single panel. Every artist since is copying that."},
                {"n": "Jim Steranko", "r": "Pencils, #110–113",
                 "b": "Three issues, and they look like nothing else. Steranko imports "
                      "<b>graphic-design and film technique</b>: montage sequences, panels that "
                      "act as film frames, op-art backgrounds, and a famous four-panel strip "
                      "that reads as a single dissolving image."}],
            "shelf": ["ca-o1"],
        },
        {
            "era": "Bronze", "years": "1969–1975",
            "h": "The Falcon, and the run that made Steve Rogers quit",
            "body": [
                "The book stops being a war comic. <b>Gene Colan</b> draws New York like a "
                "crime film; the Falcon becomes a full partner and the title changes to "
                "<i>Captain America and the Falcon</i> to say so, which was not a small thing "
                "in 1971.",
                "Then <b>Steve Englehart</b> writes the most famous thing anyone has done with "
                "the character. In the <b>Secret Empire</b> story (1974) Cap follows a "
                "government conspiracy upward and it ends at the White House; the man behind it "
                "kills himself in front of him; and Steve Rogers, unable to reconcile what he "
                "has found with the flag on his chest, <b>quits</b> and becomes Nomad.",
                "It was published while Watergate was on television. Englehart never names "
                "Nixon and does not need to. It is the single clearest demonstration of what "
                "this character is <i>for</i>."],
            "fig": {"src": [A + "cap-117.jpg", A + "cap-176.jpg"],
                    "cap": "<b>Left:</b> #117, the Falcon's debut. <b>Right:</b> #176 &mdash; "
                           "the costume on the ground and the word <i>Forever?</i>"},
            "shelf": ["ca-o2", "ca-o3"],
        },
        {
            "era": "Bronze", "years": "1976–1981",
            "h": "Kirby comes back; Stern and Byrne fix the man",
            "body": [
                "<b>Kirby returned in 1976</b> to write as well as draw the character he made, "
                "and the result is one of the strangest and most enjoyable things on the shelf: "
                "the Madbomb, Arnim Zola, the Swine, and a Bicentennial treasury. It is pure "
                "Kirby &mdash; enormous concepts, breathless pacing, dialogue nobody else would "
                "write &mdash; and it divides readers completely.",
                "Then in 1980 <b>Roger Stern and John Byrne</b> get nine issues and use them to "
                "fix a problem nobody had solved: <b>who is Steve Rogers when he is not "
                "Captain America?</b> They give him an apartment, a job as a commercial artist, "
                "neighbours and a life. Every writer since has kept it.",
                "<b>#250</b> is the era's best single idea: he is offered the presidency, and "
                "turns it down, and the issue is his reasoning."],
            "fig": {"src": [A + "cap-193.jpg", A + "cap-250.jpg"],
                    "cap": "<b>Left:</b> Kirby's return. <b>Right:</b> #250 &mdash; "
                           "<i>Captain America for President</i>, and he says no."},
            "shelf": ["ca-o4", "ca-o5"],
        },
        {
            "era": "Copper", "years": "1985–1993",
            "h": "Mark Gruenwald, for ten years",
            "body": [
                "<b>Gruenwald wrote the book for a decade</b> &mdash; still the longest run "
                "anyone has managed &mdash; and his instinct was to test the symbol by "
                "attacking it from angles the character could not punch.",
                "The centrepiece is <b>The Captain</b> (1987): a government commission tells "
                "Steve Rogers the identity is federal property and he has to take orders or "
                "give it up. He gives it up. <b>John Walker</b> gets the shield, is entirely "
                "sincere, and is a disaster &mdash; not because he is evil but because he is "
                "not built for it.",
                "That storyline is the one every screen version has borrowed since, and it is "
                "the clearest statement of Gruenwald's thesis: the uniform is not the man, and "
                "the country cannot simply appoint a replacement.",
                "The rest of the decade is a very well-made monthly superhero comic &mdash; "
                "the Scourge of the Underworld, Diamondback, Crossbones, Bloodstone &mdash; "
                "and the run's steadiness is its own argument."],
            "fig": {"src": [A + "cap-333.jpg", A + "cap-350.jpg"],
                    "cap": "<b>Left:</b> #333, John Walker's first issue in the costume. "
                           "<b>Right:</b> #350, and the two of them fighting for it."},
            "shelf": ["gru-o1", "gru-o2", "gru-o3"],
        },
        {
            "era": "Chromium", "years": "1995–2002",
            "h": "Waid restores it, twice",
            "body": [
                "<b>Mark Waid and Ron Garney</b> arrive in 1995 and immediately bring Sharon "
                "Carter back from the dead, which sounds like a 90s move and functions as the "
                "opposite &mdash; the run is a deliberate return to clarity after a decade of "
                "deconstruction.",
                "Then the book is <b>cancelled</b> for the Heroes Reborn year, and they come "
                "back to relaunch it in 1998. That is why this volume has two runs in it with a "
                "hole between them.",
                "<b>Dan Jurgens</b> finishes that volume, writing and drawing most of it, and "
                "his Korea story is the best single thing in it."],
            "fig": {"src": [A + "cap-444.jpg", A + "cap3-1.jpg"],
                    "cap": "<b>Left:</b> Waid and Garney's run. <b>Right:</b> the 1998 "
                           "relaunch after Heroes Reborn."},
            "shelf": ["waid-o1", "jurgens-o1"],
        },
        {
            "era": "Plastic", "years": "2005–2012",
            "h": "Brubaker turns it into a spy novel, and kills him",
            "body": [
                "<b>Ed Brubaker</b>'s eight years reset the character for a generation, and "
                "they do it by changing genre: this is a <b>Cold War espionage thriller</b>, "
                "with a Second World War strand running under it, and superheroics almost "
                "entirely absent.",
                "His first move was the one everybody said could not be done. <b>Bucky was "
                "the one death in Marvel that had stayed dead</b>, and bringing him back as the "
                "Winter Soldier &mdash; a brainwashed Soviet assassin who does not know who he "
                "used to be &mdash; turned out to be the best idea anyone had had about Cap in "
                "decades.",
                "Then in 2007 he is <b>shot on the courthouse steps</b> and the book keeps "
                "going for eighteen issues about everyone else. That is the trick of it: the "
                "title character is dead and it is still the best comic Marvel is publishing.",
                "<b>Steve Epting</b> and <b>Butch Guice</b> draw it like a film &mdash; muted, "
                "heavy, grounded, with almost no primary colour."],
            "fig": {"src": [A + "cap5-1.jpg", A + "cap5-25.jpg"],
                    "cap": "<b>Left:</b> Epting's #1. <b>Right:</b> #25 &mdash; a newspaper, a "
                           "bloody glove, and <i>Death of the Dream</i>."},
            "shelf": ["bru-o1", "death-o1", "lives-o1", "trial-o1", "rows-o1"],
        },
        {
            "era": "Modern", "years": "2012–2018",
            "h": "Remender goes strange; Spencer detonates it",
            "body": [
                "<b>Rick Remender</b> follows Brubaker by refusing to write a spy book. He "
                "strands Steve in <b>Dimension Z</b> for a year of publishing, raising a child "
                "in an alien wasteland, in a run whose model is openly Kirby's 1976 material "
                "rather than anything recent. It is the boldest swing of the modern era and "
                "readers split hard on it.",
                "<b>Nick Spencer</b> then writes two books at once &mdash; Sam Wilson carrying "
                "the shield and being hated for what he says with it, and Steve Rogers restored "
                "to youth with a secret &mdash; and the secret is that a reality-altering "
                "artefact has made him a <b>Hydra sleeper agent his entire life</b>.",
                "<b>Secret Empire</b> is what happens next: he wins, takes over the country, "
                "and the story is about what everyone else does while he does it. It was "
                "enormously controversial on publication and remains so, and reading it as the "
                "argument it actually is &mdash; about complicity, and about how a country "
                "accommodates authoritarianism &mdash; is fairer than reading it as a twist."],
            "fig": {"src": [A + "cap7-1.jpg", A + "sempire-1.jpg"],
                    "cap": "<b>Left:</b> Remender and Romita Jr. <b>Right:</b> <i>Secret "
                           "Empire</i>."},
            "shelf": ["rem-o1", "spencer-o1", "spencer-o2"],
        },
        {
            "era": "Modern", "years": "2017–2021",
            "h": "Putting him back together, twice",
            "body": [
                "Two very different repairs. <b>Waid and Samnee</b> write ten issues of "
                "deliberately uncomplicated Captain America &mdash; a road trip across America, "
                "meeting people, being decent &mdash; which after <i>Secret Empire</i> is "
                "exactly the right medicine and is on this shelf inside the Black Widow book "
                "because it is collected nowhere else.",
                "<b>Ta-Nehisi Coates</b> takes the harder route. His Steve Rogers comes out of "
                "<i>Secret Empire</i> with his reputation destroyed and no confidence that the "
                "symbol means anything, and the run answers that slowly, over thirty issues, "
                "against a Red Skull who <b>fights with rhetoric rather than weapons</b> and a "
                "conspiracy of the wealthy called the Power Elite.",
                "It is the most essayistic run on this shelf and the one most interested in the "
                "actual question the character raises."],
            "fig": {"src": [A + "cap18-695.jpg", A + "cap10-1.jpg"],
                    "cap": "<b>Left:</b> Waid and Samnee. <b>Right:</b> Coates and Leinil Yu."},
            "shelf": ["bwca-o1", "coates-o1"],
        },
    ],
    "tone": {
        "h": "The tone map",
        "sub": "Twenty-two volumes, the biggest shelf on the site, and they are not the same "
               "comic. If you want a particular register, here is where it lives.",
        "modes": [
            {"l": "Most propaganda",
             "b": "1941. Anthology issues, breakneck pacing, and a hero created to argue for "
                  "a war America had not joined. Historically extraordinary, crude as comics.",
             "vols": ["ga-o1", "ga-o2"]},
            {"l": "Most Kirby",
             "b": "Two separate stretches, twelve years apart &mdash; the Tales of Suspense "
                  "fight scenes, and the 1976 return with the Madbomb. Enormous, bombastic, "
                  "unlike anyone else.",
             "vols": ["ca-o1", "ca-o4"]},
            {"l": "Most political",
             "b": "Englehart's Secret Empire, written during Watergate, where the trail leads "
                  "to the White House and Steve Rogers quits over it.",
             "vols": ["ca-o3"]},
            {"l": "Most human",
             "b": "Stern and Byrne giving him an apartment and a job, and #250 &mdash; the "
                  "issue where he is offered the presidency and declines.",
             "vols": ["ca-o5"]},
            {"l": "Best long haul",
             "b": "Ten years of Gruenwald, and the storyline where the government takes the "
                  "identity away and gives it to somebody sincere and wrong.",
             "vols": ["gru-o1", "gru-o2", "gru-o3"]},
            {"l": "Most spy novel",
             "b": "Brubaker. Cold War espionage with a war story under it, almost no "
                  "superheroics, and the best-executed resurrection in Marvel's history.",
             "vols": ["bru-o1", "death-o1", "rows-o1"]},
            {"l": "Saddest",
             "b": "Eighteen issues after the title character is shot, about everyone he left. "
                  "Widely considered the best thing Marvel published that year.",
             "vols": ["death-o1"]},
            {"l": "Strangest",
             "b": "Remender's Dimension Z &mdash; a year in an alien wasteland raising a "
                  "child, modelled on Kirby rather than on anything modern.",
             "vols": ["rem-o1"]},
            {"l": "Most argued about",
             "b": "Secret Empire. Cap as a lifelong Hydra agent who wins. Read it as an "
                  "argument about complicity rather than as a twist.",
             "vols": ["spencer-o1", "spencer-o2"]},
            {"l": "Most thoughtful",
             "b": "Coates, asking what the symbol is worth after it has been disgraced, with a "
                  "Red Skull who fights with words.",
             "vols": ["coates-o1"]},
            {"l": "Kindest",
             "b": "Waid and Samnee's ten issues of a man driving across America being decent "
                  "to people. Exactly what was needed and hard to find anywhere else.",
             "vols": ["bwca-o1"]},
        ],
    },
}


def _v(k, t, l, s, v):
    return {"kicker": k, "title": t, "lede": l, "sections": s, "verdict": v}


VOLUMES = {

"ga-o1": _v("Volume 01 · 1941–1942", "Golden Age Captain America Omnibus Vol. 1",
    "Simon and Kirby, twelve anthology issues, and a cover that punched Hitler nine months "
    "before America entered the war.",
    [{"era": "Golden", "years": "1941–1942",
      "h": "A political act on a newsstand",
      "body": [
          "<b>Joe Simon and Jack Kirby</b> were both Jewish, and in early 1941 American "
          "opinion on intervention was genuinely divided. They put Cap punching Hitler on the "
          "cover of #1 anyway, and received hate mail and threats for it. Reportedly the New "
          "York mayor's office offered protection.",
          "It sold in Superman numbers. Whatever else these comics are, they were among the "
          "most successful publications in America.",
          "As <i>comics</i> they are Golden Age anthologies &mdash; several complete stories "
          "per issue, plot at a sprint, characterisation nearly absent. <b>Kirby's layouts are "
          "the reason to read them</b>: even at 23 he is breaking borders and shoving figures "
          "at the reader in ways nobody else on the racks was attempting."],
      "fig": {"src": [A + "cac-1.jpg"],
              "cap": "March 1941."}}],
    {"standing": "Historic", "cls": "",
     "body": ["Treated as an <b>artefact first and a reading experience second</b>, and "
              "nobody pretends otherwise. The consensus is that the Kirby layouts are "
              "genuinely thrilling and the writing is what 1941 anthology comics were.",
              "Its cultural significance is not really contested. Read a few issues rather "
              "than the whole book in one go &mdash; twelve anthology issues is a great deal "
              "of comics, and they repeat."]}),

"ga-o2": _v("Volume 02 · 1942–1943", "Golden Age Captain America Omnibus Vol. 2",
    "Simon and Kirby leave after #10 and the book carries on without them &mdash; with a "
    "nineteen-year-old Stan Lee writing some of it.",
    [{"era": "Golden", "years": "1942–1943",
      "h": "After the creators",
      "body": [
          "Simon and Kirby left in a dispute over money, and #13&ndash;24 is the machine "
          "running without them. <b>Al Avison</b> and <b>Syd Shores</b> take over the art in a "
          "visibly Kirby-derived style, and it is competent rather than electric.",
          "The historical curiosity is that a very young <b>Stan Lee</b> is writing some of "
          "this &mdash; nearly twenty years before <i>Fantastic Four</i> #1.",
          "The Golden Age run continues to #75. The omnibus line stops here, so everything "
          "after 1943 is uncollected in this format."]}],
    {"standing": "For completists", "cls": "mixed",
     "body": ["Rated below Vol. 1 for the obvious reason: the thing that made Vol. 1 "
              "extraordinary has left the building. The art is a capable imitation of Kirby "
              "and reads as one.",
              "Its value is mostly historical &mdash; the early Stan Lee material, and "
              "watching a hit book try to sustain itself. Buy it if you bought Vol. 1; do not "
              "start here."]}),

"ca-o1": _v("Volume 03 · 1964–1969", "Captain America Omnibus Vol. 1",
    "The thaw. Five years of ten-page chapters in <i>Tales of Suspense</i> where Kirby invents "
    "the modern Captain America fight scene, then the title back at #100.",
    [{"era": "Silver", "years": "1964–1969",
      "h": "Ten pages a month",
      "body": [
          "Sharing a book with Iron Man meant no room for subplot, so the fighting had to "
          "carry the strip &mdash; and <b>that constraint produced the visual grammar the "
          "character still uses</b>. The shield thrown and ricocheting, the leap into a room, "
          "the single-panel readable arc: it is all worked out here.",
          "The emotional register is grief. This Cap is a man twenty years out of his own "
          "time who has lost everyone, and Lee plays it straight.",
          "At <b>#100</b> he gets the title back. The Red Skull returns properly, the Cosmic "
          "Cube arrives, and Bucky's death is finally dramatised.",
          "<b>Jim Steranko</b>'s three issues at the end are among the most formally "
          "adventurous pages Marvel published in the 1960s."],
      "makers": [{"n": "Jack Kirby", "r": "Pencils",
                  "b": "The <b>shield choreography</b>. Watch how he makes a ricochet legible "
                       "in one panel with motion lines and a sequence of impact points &mdash; "
                       "an entirely invented visual convention that every subsequent artist "
                       "has simply inherited."},
                 {"n": "Jim Steranko", "r": "Pencils, #110–113",
                  "b": "Film and graphic-design technique, imported wholesale: <b>montage</b>, "
                       "panels used as film frames, and op-art backgrounds. Look for the "
                       "sequence of near-identical panels that reads as a single dissolve."}],
      "fig": {"src": [A + "tos-59.jpg", A + "cap-111.jpg"],
              "cap": "<b>Left:</b> the shared book. <b>Right:</b> Steranko."}}],
    {"standing": "Classic", "cls": "",
     "body": ["Very well regarded, with the caveat that the <b>Tales of Suspense chapters are "
              "repetitive</b> read in bulk &mdash; ten pages of fighting, monthly, for years. "
              "Most readers recommend dipping rather than marathoning.",
              "<b>Steranko's three issues are the crown jewels</b> and get named constantly; "
              "they are worth the volume on their own. #100 onward is where the book starts "
              "having stories as well as sequences."]}),

"ca-o2": _v("Volume 04 · 1969–1972", "Captain America Omnibus Vol. 2",
    "The book stops being a war comic. Gene Colan draws New York like a crime film, and the "
    "title changes to say the Falcon is a partner.",
    [{"era": "Bronze", "years": "1969–1972",
      "h": "Cap and the Falcon",
      "body": [
          "The Falcon arrives in #117 and by #134 the title is <i>Captain America and the "
          "Falcon</i> &mdash; a Black co-lead with his name on the masthead, in 1971, which "
          "was not a small editorial decision.",
          "The stories start asking whether a man out of time has anything useful to say about "
          "the present, which is a question the book has never stopped asking.",
          "<b>Gene Colan</b> draws it, and his smoky tonal pencil turns Harlem and midtown "
          "into somewhere with weather. <b>John Romita Sr.</b> is also here."],
      "fig": {"src": [A + "cap-117.jpg"],
              "cap": "#117, the Falcon's first appearance."}}],
    {"standing": "Underrated", "cls": "cult",
     "body": ["Sits between two much-discussed volumes and gets less attention than it "
              "deserves. Readers who work through the shelf in order routinely report this as "
              "the surprise: <b>the book grows up here</b>, and the Falcon partnership is "
              "written with real warmth.",
              "The criticisms are that the plotting is loose and that some of the social "
              "material is handled with a 1971 clumsiness that has dated. Colan's art is the "
              "consistent draw."]}),

"ca-o3": _v("Volume 05 · 1972–1975", "Captain America Omnibus Vol. 3",
    "Englehart's Secret Empire &mdash; the trail leads to the White House, and Steve Rogers "
    "quits. Published while Watergate was on television.",
    [{"era": "Bronze", "years": "1972–1975",
      "h": "The most famous thing anyone has done with him",
      "body": [
          "<b>Steve Englehart</b> runs a conspiracy story upward through the government for "
          "months of publishing. At the top of it is a man in the White House, unnamed and "
          "unshown, who shoots himself in front of Captain America rather than be taken.",
          "Steve Rogers cannot reconcile it, gives up the identity, and spends months as "
          "<b>Nomad</b> &mdash; a hero with no country.",
          "The restraint is the craft. Englehart never names Nixon and never needs to; the "
          "readers of 1974 supplied it themselves. It remains the clearest statement of what "
          "this character is <i>for</i>: a symbol that can be turned against the state that "
          "made it."],
      "fig": {"src": [A + "cap-153.jpg", A + "cap-176.jpg"],
              "cap": "<b>Left:</b> the Englehart run under way. <b>Right:</b> #176 &mdash; "
                     "the uniform discarded."}}],
    {"standing": "Landmark", "cls": "",
     "body": ["Very widely named the <b>defining Captain America story</b>, and the one most "
              "often cited when people argue the character is inherently political rather "
              "than inherently patriotic.",
              "The reservation readers raise is the surrounding run: Englehart's four years "
              "contain some meandering stretches, and the Secret Empire arc is a peak rather "
              "than a plateau. Nobody argues with the peak."]}),

"ca-o4": _v("Volume 06 · 1976–1977", "Captain America Omnibus Vol. 4",
    "Kirby comes back to the character he made and writes as well as draws him. The strangest "
    "and most argued-about volume on the shelf.",
    [{"era": "Bronze", "years": "1976–1977",
      "h": "Pure Kirby",
      "body": [
          "Twenty issues of Kirby with nobody scripting over him: the <b>Madbomb</b>, Arnim "
          "Zola, the Swine, Agron, and a Bicentennial treasury in which Cap tours American "
          "history.",
          "It is enormous, breathless and completely uninterested in what the book had been "
          "doing for the previous three years. Kirby ignores Englehart's continuity almost "
          "entirely and writes concepts at a rate nobody else could sustain.",
          "The dialogue is the thing people either love or cannot get past. Kirby writes "
          "declamatory, rhythmic, capital-letter prose that sounds like nothing any human has "
          "said, and it is either magnificent or unreadable depending on the reader.",
          "Note this volume supersedes the separate <i>Captain America by Jack Kirby</i> "
          "omnibus, which holds the same issues minus FOOM #11."],
      "fig": {"src": [A + "cap-193.jpg"],
              "cap": "#193. <i>King Kirby is back!</i> is on the cover, which tells you how "
                     "Marvel was selling it."}}],
    {"standing": "Divisive", "cls": "mixed",
     "body": ["One of the most polarised books on this site. Its admirers call it "
              "<b>uncut Kirby imagination</b> and treat it as a late-career high point; its "
              "detractors find the plotting incoherent and the dialogue impenetrable, and "
              "point out that it discards the character work of the run before it.",
              "Both are describing the same book accurately. Read one issue before committing "
              "&mdash; you will know within twenty pages which camp you are in.",
              "Remender's 2012 run, later on this shelf, is explicitly modelled on it, which "
              "is a useful thing to know when you get there."]}),

"ca-o5": _v("Volume 07 · 1978–1981", "Captain America Omnibus Vol. 5",
    "Stern and Byrne get nine issues and answer the question the book had avoided for forty "
    "years: who is Steve Rogers when he takes the costume off?",
    [{"era": "Bronze", "years": "1978–1981",
      "h": "A man with an apartment",
      "body": [
          "<b>Roger Stern and John Byrne</b> were on the title briefly and the effect was "
          "permanent. They gave him a flat in Brooklyn Heights, a job as a commercial artist, "
          "neighbours who did not know, and a life that existed when he was not working. "
          "<b>Every writer since has kept it.</b>",
          "<b>#250</b> is the run's landmark: a political party offers to nominate him for "
          "president, and the issue is his reasoning for saying no. It is the best short "
          "statement of the character's ethics anyone has written.",
          "The volume also holds the surrounding Roger McKenzie run, which is more variable."],
      "fig": {"src": [A + "cap-250.jpg"],
              "cap": "#250. He declines."}}],
    {"standing": "Quietly essential", "cls": "",
     "body": ["The Stern/Byrne issues have a reputation far larger than nine issues normally "
              "earn, and it is deserved: this is where the <b>modern Steve Rogers is "
              "invented</b>, and #250 is on most best-of lists.",
              "The volume around them is rated as ordinary late-Bronze superhero comics. Buy "
              "it for the nine, and note that the rest is pleasant enough."]}),

"gru-o1": _v("Volume 08 · 1985–1989", "Captain America by Mark Gruenwald Omnibus Vol. 1",
    "The start of a decade on the book, and the storyline every screen version has borrowed "
    "since: the government takes the identity away.",
    [{"era": "Copper", "years": "1985–1989",
      "h": "The Captain",
      "body": [
          "A federal commission informs Steve Rogers that Captain America is <b>government "
          "property</b> and he must take orders. He refuses and gives up the name, the shield "
          "and the uniform.",
          "The replacement, <b>John Walker</b>, is the run's great achievement. He is not a "
          "villain and not a fraud &mdash; he is a sincere, patriotic man who genuinely wants "
          "to do it well and is temperamentally incapable, and watching him come apart is far "
          "more disturbing than a straightforward antagonist would have been.",
          "Also here: the <b>Scourge of the Underworld</b>, who murders D-list supervillains in "
          "a sustained purge that is one of the odder things Marvel published in the 80s, and "
          "Diamondback, who is the best supporting character Gruenwald added."],
      "fig": {"src": [A + "cap-333.jpg"],
              "cap": "#333 &mdash; Walker in the costume, and the cover is not treating it as "
                     "a joke."}}],
    {"standing": "Classic", "cls": "",
     "body": ["<b>The Captain</b> is very widely considered one of the best Captain America "
              "stories ever told and the single most influential on later adaptations. Walker "
              "in particular is praised as a genuinely difficult character rather than a "
              "straw man.",
              "The wider run gets a steadier reception: <b>consistently well-made monthly "
              "superhero comics</b> that some readers find a little plain next to the "
              "showier eras either side. The Scourge material divides people."]}),

"gru-o2": _v("Volume 09 · 1989–1991", "Captain America by Mark Gruenwald Omnibus Vol. 2",
    "The middle of the decade: the Red Skull with a new body, Crossbones, and a book that has "
    "settled into being extremely good at its job.",
    [{"era": "Copper", "years": "1989–1991",
      "h": "Craft over spectacle",
      "body": [
          "The Red Skull comes back in a cloned body &mdash; specifically, a clone of Steve "
          "Rogers &mdash; which is a properly nasty idea and gives the antagonist a physical "
          "presence he had lacked.",
          "<b>Crossbones</b> arrives and immediately works: an enforcer with no ideology at "
          "all, which contrasts usefully against a villain who is all ideology.",
          "This volume also holds the <i>Adventures of Captain America</i> retelling of the "
          "origin, which is beautifully painted and is the best-looking thing in the book.",
          "Mostly, though, this is a run being reliably good every month for two years, which "
          "is a harder achievement than it sounds and is the thing Gruenwald is respected for."]}],
    {"standing": "Solid", "cls": "",
     "body": ["Well liked without generating much argument. The recurring assessment is "
              "<b>reliable, dense, workmanlike superhero comics</b> by someone who understood "
              "the character better than almost anyone.",
              "Readers looking for a landmark find this stretch quieter than Vol. 1. Readers "
              "who like a well-run monthly book rate it highly. The Red Skull material is the "
              "part most often singled out."]}),

"gru-o3": _v("Volume 10 · 1991–1993", "Captain America by Mark Gruenwald Omnibus Vol. 3",
    "The last collected stretch of the ten-year run, and the point at which the 1990s start "
    "pulling the book around.",
    [{"era": "Chromium", "years": "1991–1993",
      "h": "The decade arrives",
      "body": [
          "<i>Blood and Glory</i> with the Punisher, U.S.Agent's own miniseries, and "
          "<i>Operation: Galactic Storm</i> running through the middle &mdash; the book is "
          "increasingly at the mercy of line-wide crossovers, which is what the early 90s did "
          "to every Marvel title.",
          "The run continues to #443 and <b>the omnibus line stops at #418</b>, so the last "
          "two years of Gruenwald &mdash; <i>Fighting Chance</i>, in which the super-soldier "
          "serum starts killing him &mdash; are not collected here. That is a real omission; "
          "it is the run's ending."]}],
    {"standing": "The weakest of the three", "cls": "mixed",
     "body": ["Rated below the first two volumes, and the reasons given are mostly external: "
              "<b>crossover interference</b>, a house art style readers find less appealing "
              "than Dwyer's or Neary's, and the sense of a long run running down.",
              "The frustration people voice most often is the <b>truncation</b> &mdash; "
              "stopping at #418 leaves Gruenwald's decade without its conclusion, and "
              "<i>Fighting Chance</i> has real defenders."]}),

"waid-o1": _v("Volume 11 · 1995–1998", "Captain America by Waid, Garney & Kubert Omnibus",
    "Two runs with a cancellation in the middle. Waid brings Sharon Carter back, Marvel "
    "cancels the book for Heroes Reborn, and then he comes back and relaunches it.",
    [{"era": "Chromium", "years": "1995–1998",
      "h": "Clarity as a strategy",
      "body": [
          "After a decade of Gruenwald testing the symbol, <b>Mark Waid</b>'s instinct is to "
          "make the book straightforwardly heroic again &mdash; and to do it without irony, "
          "which in 1995 was a genuinely unfashionable position.",
          "<b>Ron Garney</b>'s art is the engine: loose, kinetic, brush-heavy, and much more "
          "fluid than the cross-hatched house style around it.",
          "Then the title was <b>cancelled</b> for the Heroes Reborn year. Waid and Garney "
          "returned in 1998 to relaunch it, which is why this book has a hole in the middle. "
          "The Heroes Reborn year itself is a different book and is not here."],
      "fig": {"src": [A + "cap-444.jpg", A + "cap3-1.jpg"],
              "cap": "<b>Left:</b> the 1995 run. <b>Right:</b> the 1998 relaunch."}}],
    {"standing": "Very well liked", "cls": "",
     "body": ["Regularly named the <b>best Captain America between Gruenwald and Brubaker</b>, "
              "and singled out for treating sincerity as a strength at a moment when the "
              "industry was doing the opposite.",
              "Garney's art is the thing readers mention first. The criticism is structural: "
              "the Heroes Reborn interruption cuts the run in half and the 1998 relaunch "
              "never quite regains the momentum of the first stretch."]}),

"jurgens-o1": _v("Volume 12 · 2000–2002", "Captain America by Dan Jurgens Omnibus",
    "The end of the 1998 volume, written and drawn largely by one person, with a Korea story "
    "that is the best thing in it.",
    [{"era": "Plastic", "years": "2000–2002",
      "h": "A writer-artist finishing a volume",
      "body": [
          "<b>Dan Jurgens</b> writes and pencils most of Captain America (1998) #25&ndash;50 "
          "&mdash; a single sensibility, which is increasingly rare by 2000.",
          "Protocide, a failed earlier super-soldier, is the run's main original idea. The "
          "Red Skull returns. And there is a <b>Korean War story</b> that is the best single "
          "issue here, and the sort of thing this character can do that almost nobody else in "
          "Marvel can.",
          "After this the title relaunches twice more before anything is collected again."]}],
    {"standing": "Solid, overlooked", "cls": "cult",
     "body": ["Barely discussed, and the readers who have read it tend to describe it as "
              "<b>better than its invisibility suggests</b> &mdash; well-constructed, "
              "traditional superhero comics from someone who clearly likes the character.",
              "The criticism is that it is unambitious and that Protocide is a thin idea. The "
              "Korea material is what people remember, and it is genuinely good."]}),

"bru-o1": _v("Volume 13 · 2005–2007", "Captain America by Ed Brubaker Omnibus",
    "The run that reset the character for twenty years, by changing genre and by doing the one "
    "thing everybody said could not be done.",
    [{"era": "Plastic", "years": "2005–2007",
      "h": "Bringing back Bucky",
      "body": [
          "Marvel had a standing joke that only Bucky and Uncle Ben stayed dead. Brubaker "
          "brought Bucky back as the <b>Winter Soldier</b> &mdash; a brainwashed Soviet "
          "assassin, decades of black operations, no memory of who he was &mdash; and it "
          "worked because it is not a resurrection story. It is a story about what was done to "
          "him, and about Steve's guilt for not looking.",
          "The genre change is the other half. This is a <b>Cold War espionage thriller</b>: "
          "handlers, sleeper agents, dead drops, a war story running in flashback under a "
          "present-day plot. Superheroics are almost entirely absent.",
          "<b>Steve Epting</b> and <b>Michael Lark</b> draw it with a muted, heavy, "
          "photographic weight and almost no primary colour &mdash; a deliberate refusal of "
          "the character's own palette."],
      "makers": [{"n": "Steve Epting", "r": "Pencils",
                  "b": "Look at the <b>lighting</b>. Epting stages almost everything in "
                       "overcast grey or hard directional light, which drains the red-white-"
                       "and-blue and makes the book read as a thriller. Then watch what "
                       "happens the few times he lets full colour back in."}],
      "fig": {"src": [A + "cap5-1.jpg"],
              "cap": "Epting's #1. Note how little of the costume is actually visible."}}],
    {"standing": "Modern classic", "cls": "",
     "body": ["Almost universally named the <b>best modern Captain America run</b> and one of "
              "the best Marvel runs of the century. The Winter Soldier is treated as a rare "
              "genuinely great addition to a sixty-year-old mythology, and the MCU took it "
              "almost wholesale.",
              "There is essentially no negative consensus. The only recurring note is that "
              "readers who want superhero spectacle should know this is a spy comic and "
              "commits to it completely.",
              "If you read one book on this shelf, this is the one."]}),

"death-o1": _v("Volume 14 · 2007–2008", "Death of Captain America Omnibus",
    "He is shot on the courthouse steps in the first issue, and the book runs for eighteen "
    "more about everyone else. It is the best thing Marvel published that year.",
    [{"era": "Plastic", "years": "2007–2008",
      "h": "A book with no title character",
      "body": [
          "The death itself is over quickly &mdash; the point is not the assassination but the "
          "vacuum. Eighteen issues follow Bucky, Sharon Carter, the Falcon and the Red Skull "
          "through what happens to a country and a supporting cast when the symbol is removed.",
          "It works because Brubaker had spent two years making everyone around Steve into "
          "real characters first. Bucky picking up the shield &mdash; carrying a gun, which "
          "the book takes seriously as a problem &mdash; is the emotional centre.",
          "#25 is in both this book and the Brubaker volume, which is the shelf's deliberate "
          "overlap."],
      "fig": {"src": [A + "cap5-25.jpg"],
              "cap": "#25. A newspaper, a glove and a headline &mdash; no figure at all."}}],
    {"standing": "The peak", "cls": "",
     "body": ["Frequently rated <b>even higher than the run that precedes it</b>, on the "
              "grounds that sustaining a title for eighteen issues without its lead is a "
              "genuinely hard thing to do and this does it without strain.",
              "It also got mainstream news coverage in 2007, which is rare. The criticism "
              "&mdash; almost the only one &mdash; is that everybody knew the death would be "
              "undone, and the book is good enough that most readers stopped caring."]}),

"lives-o1": _v("Volume 15 · 2008–2010", "Captain America Lives! Omnibus",
    "How they undid it, and the eighteen months of Bucky carrying the shield first.",
    [{"era": "Plastic", "years": "2008–2010",
      "h": "A Captain America with a gun",
      "body": [
          "The genuinely interesting part is not the resurrection. It is that for a year and a "
          "half <b>Bucky is Captain America</b>, and the book keeps asking whether an "
          "assassin can wear that uniform &mdash; which is a much sharper version of the "
          "question Gruenwald asked with John Walker.",
          "The <i>Reborn</i> mini handles the return, and the mechanism is unusual: Steve is "
          "not dead so much as <b>unstuck in his own timeline</b>, reliving his life without "
          "being able to change it. It is a better idea than a resurrection needs to be.",
          "The numbering jumps to #600 partway through, which is the title reverting to its "
          "original count for the anniversary."]}],
    {"standing": "Well regarded", "cls": "",
     "body": ["Solidly liked, and rated below the two volumes before it for a structural "
              "reason rather than a quality one: <b>it is the book that has to undo the best "
              "story</b>, and everyone knew it was coming.",
              "The <b>Bucky-as-Cap material is what people defend</b>, and defend strongly. "
              "The resurrection mechanics divide readers; some find <i>Reborn</i> elegant and "
              "some find it convoluted."]}),

"trial-o1": _v("Volume 16 · 2010–2011", "Captain America: The Trial of Captain America Omnibus",
    "Bucky is put on trial for what he did as the Winter Soldier &mdash; which is the question "
    "the whole Brubaker run has been circling.",
    [{"era": "Modern", "years": "2010–2011",
      "h": "Guilt, legally",
      "body": [
          "The premise is the run's thesis made explicit: <b>is a man guilty of things done "
          "while he was someone else's weapon?</b> The story takes it to a courtroom and "
          "refuses to make it easy.",
          "It is the most legally-minded thing on this shelf and one of the few superhero "
          "trials that is actually about jurisprudence rather than about a fight in a "
          "courtroom.",
          "<b>Butch Guice</b> has taken over from Epting by now, and his heavier, scratchier "
          "line suits the material."]}],
    {"standing": "Strong", "cls": "",
     "body": ["Well received and somewhat overshadowed by the more famous volumes around it. "
              "Readers who rate it highly point at the <b>moral seriousness</b> &mdash; it is "
              "the payoff to five years of setup and it does not flinch.",
              "The criticism is pacing: the trial itself is slower than the material around "
              "it, and some readers find the resolution abrupt after the build."]}),

"rows-o1": _v("Volume 17 · 2011–2012", "Captain America: Return of the Winter Soldier Omnibus",
    "The end of Brubaker's eight years, including fourteen issues of Bucky running black "
    "operations Cap is not told about.",
    [{"era": "Modern", "years": "2011–2012",
      "h": "The spy book with no superheroes in it",
      "body": [
          "The <i>Winter Soldier</i> ongoing collected here is the closest this run ever gets "
          "to pure genre: Bucky and the Black Widow running deniable operations against old "
          "Soviet programmes, with the superhero apparatus entirely offstage.",
          "It is also, effectively, Brubaker writing <i>Criminal</i> inside Marvel, and it is "
          "very good indeed.",
          "The <i>Fear Itself</i> tie-ins are the weaker material and are here because the "
          "run passed through them."]}],
    {"standing": "Strong finish", "cls": "",
     "body": ["The <b><i>Winter Soldier</i> ongoing is the part people praise</b>, and it is "
              "often recommended on its own to readers who like espionage fiction and do not "
              "care about superheroes at all.",
              "The volume as a whole is rated a little below the earlier Brubaker books, "
              "mostly because of the crossover material threaded through it. As a conclusion "
              "to eight years it is considered a good one."]}),

"rem-o1": _v("Volume 18 · 2012–2015", "Captain America by Rick Remender Omnibus",
    "Follow the best modern run by doing the opposite: strand him in an alien dimension for a "
    "year and make him raise a child there.",
    [{"era": "Modern", "years": "2012–2015",
      "h": "Dimension Z",
      "body": [
          "<b>Rick Remender</b>'s model is explicitly Kirby's 1976 material rather than "
          "Brubaker's espionage &mdash; huge concepts, breathless pace, a hostile alien "
          "landscape, Arnim Zola as the antagonist. Steve is trapped there for over a decade "
          "of in-story time and raises a son.",
          "It is the boldest swing of the modern era and it does not much resemble anything "
          "else on this shelf. Whether that is a virtue is the argument.",
          "The run ends with the super-soldier serum gone, Steve aged into an old man, and "
          "<b>Sam Wilson carrying the shield</b> &mdash; which sets up the volume after it.",
          "One scene in #22, in which Sam Wilson wakes beside Jet Zola, drew significant "
          "online criticism at the time, including calls for Remender's firing; the character "
          "is established as an adult, and the complaint was about the framing rather than "
          "the facts."],
      "fig": {"src": [A + "cap7-1.jpg"],
              "cap": "Remender and John Romita Jr. The book looks like nothing Brubaker did."}}],
    {"standing": "Divisive", "cls": "mixed",
     "body": ["Genuinely split. Admirers call it <b>brave and ambitious</b> and the only "
              "modern run with the nerve to be strange; detractors call Dimension Z an "
              "enormous detour that removed Captain America from Captain America's book for "
              "a year.",
              "Both readings are defensible. What is agreed is that following Brubaker was an "
              "impossible position and that Remender did not try to imitate him.",
              "The Sam Wilson handover at the end is generally well regarded and leads "
              "directly into the next volume."]}),

"spencer-o1": _v("Volume 19 · 2015–2016", "Captain America by Nick Spencer Omnibus Vol. 1",
    "Two Captains at once: Sam Wilson holding the shield and being hated for what he says with "
    "it, and Steve Rogers restored to youth with a secret.",
    [{"era": "Modern", "years": "2015–2016",
      "h": "The argument, before the twist",
      "body": [
          "<b>Sam Wilson: Captain America</b> is the better half and the less discussed. Sam "
          "uses the platform to say things &mdash; about policing, immigration, inequality "
          "&mdash; and a large part of the country turns on him for it, which the book treats "
          "as the actual story rather than as background.",
          "It is the most directly political run on this shelf since Englehart, and the "
          "in-story backlash mirrors the real one the book received.",
          "Meanwhile Steve is restored to youth in <i>Steve Rogers: Captain America</i>, and "
          "the final page of #1 reveals he has been a Hydra agent his entire life. That is the "
          "setup; the next volume is the payoff.",
          "<i>Standoff</i> runs through the middle and is the mechanism."],
      "fig": {"src": [A + "capsr-1.jpg"],
              "cap": "The issue with the last page everybody was talking about."}}],
    {"standing": "Better than remembered", "cls": "cult",
     "body": ["Overshadowed entirely by what it sets up, which is a shame: the <b>Sam Wilson "
              "material is very well regarded</b> by the readers who got to it, and is "
              "frequently described as the most substantial political writing the book has "
              "had in decades.",
              "The criticism at the time was mostly aimed at the Hydra reveal rather than at "
              "these comics. Reading this volume as <i>the argument</i> rather than as "
              "<i>the setup</i> is the recommendation."]}),

"spencer-o2": _v("Volume 20 · 2017–2018", "Captain America by Nick Spencer Omnibus Vol. 2",
    "Secret Empire. Captain America has been a Hydra sleeper his whole life, and he wins. The "
    "most controversial Marvel story of its decade.",
    [{"era": "Modern", "years": "2017–2018",
      "h": "What it is actually about",
      "body": [
          "The premise generated genuine anger &mdash; a character created by two Jewish men "
          "to fight fascism, revealed as a fascist, at a politically raw moment. Marvel and "
          "Spencer both fielded a great deal of it publicly.",
          "What the story is doing, read whole, is <b>not about Steve at all</b>. He takes the "
          "country in the first act and the remaining bulk is about everyone else: who "
          "resists, who collaborates, who tells themselves it is temporary. It is a story "
          "about accommodation.",
          "Whether that justifies the premise is the argument, and it has not settled in "
          "eight years. It is worth reading before deciding, which is the whole reason it is "
          "on the shelf.",
          "It ends with <i>Generations</i> and the restoration."],
      "fig": {"src": [A + "sempire-1.jpg"],
              "cap": "<i>Secret Empire</i> #1."}}],
    {"standing": "Divisive", "cls": "mixed",
     "body": ["The most contested book on this shelf. Reviews at the time were <b>mixed</b>, "
              "and the discourse around it was substantially larger and angrier than the "
              "reviews.",
              "The case against: the premise is a betrayal of what the character was created "
              "for, the marketing leaned on shock, and a nineteen-month build-up is a long "
              "time to spend on a reveal that gets undone. The case for: the execution is "
              "more thoughtful than the premise sounds, the supporting cast material is "
              "strong, and the book knows exactly what it is saying about complicity.",
              "Read it. Then decide &mdash; it is genuinely not a story you can judge from a "
              "summary."]}),

"bwca-o1": _v("Volume 21 · 2016–2018", "Black Widow & Captain America by Waid & Samnee Omnibus",
    "Half of this is Black Widow's book. It is on the shelf because the other half &mdash; ten "
    "issues of deliberately uncomplicated Captain America &mdash; is collected nowhere else.",
    [{"era": "Modern", "years": "2017–2018",
      "h": "Straightforwardly decent, on purpose",
      "body": [
          "After <i>Secret Empire</i>, <b>Mark Waid and Chris Samnee</b> put Steve back in the "
          "costume and send him on a road trip across America meeting ordinary people. There "
          "is no twist. That is the point.",
          "It reads as a corrective and it works as one &mdash; after a year of the character "
          "being a fascist, ten issues of him being kind is a genuine editorial statement.",
          "The Black Widow half is the same team doing an entirely different thing: a fast, "
          "nearly silent action comic that is among Samnee's best-looking work.",
          "This is the same partnership as the Daredevil shelf's Waid/Samnee volumes, and it "
          "is a useful comparison."],
      "fig": {"src": [A + "cap18-695.jpg"],
              "cap": "<i>Home of the Brave</i>. The road trip issue."}}],
    {"standing": "Well liked", "cls": "",
     "body": ["The Captain America half is warmly received as <b>exactly the right book at "
              "exactly the right moment</b>, and Samnee's art gets consistent praise.",
              "The reservations are about the package rather than the comics: it is half a "
              "Black Widow book, and readers buying a Captain America omnibus sometimes "
              "object. The Black Widow issues are excellent on their own terms and are "
              "frequently the surprise for people who came for the other half."]}),

"coates-o1": _v("Volume 22 · 2018–2021", "Captain America by Ta-Nehisi Coates Omnibus",
    "The whole run: a Steve Rogers whose reputation has been destroyed, asking slowly whether "
    "the symbol is worth anything any more.",
    [{"era": "Modern", "years": "2018–2021",
      "h": "After the disgrace",
      "body": [
          "<b>Ta-Nehisi Coates</b> starts from the position <i>Secret Empire</i> left: the "
          "country watched Captain America take power, and it does not much matter that it "
          "was not really him. The trust is gone.",
          "The antagonists are chosen to match. The <b>Power Elite</b> is a conspiracy of "
          "wealth and influence rather than a supervillain team, and the <b>Red Skull</b> "
          "returns as a rhetorician &mdash; a demagogue who radicalises young men with "
          "speeches, which is a far more contemporary threat than a death ray.",
          "It is the most essayistic run on this shelf. Coates writes long internal narration "
          "and is more interested in the argument than in the plot, which is either the appeal "
          "or the problem depending on the reader.",
          "<b>Leinil Francis Yu</b> and <b>Adam Kubert</b> draw it."],
      "fig": {"src": [A + "cap10-1.jpg"],
              "cap": "Coates and Yu's #1."}}],
    {"standing": "Thoughtful and uneven", "cls": "mixed",
     "body": ["The recurring phrase in reviews is almost exactly that: <b>uneven but always "
              "thoughtful</b>. The ideas and the internal narration get consistent praise, and "
              "the conclusion in #30 was well received as a fitting end.",
              "The criticism is pacing and plot mechanics &mdash; the middle stretch is widely "
              "described as slow, and readers who want a superhero comic rather than an essay "
              "with fights in it find it heavy going.",
              "It is the most interesting failure-or-success on this shelf, and worth forming "
              "your own view on. The Red Skull as a rhetorician is an idea nobody else has "
              "had."]}),

}

TOUR = {"overview": OVERVIEW, "volumes": VOLUMES}
