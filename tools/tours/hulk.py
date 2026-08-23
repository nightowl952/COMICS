# -*- coding: utf-8 -*-
"""The Hulk guided tour.

A publishing history, not an in-universe one: who made the book, what the
decade did to it, and what the art is actually doing. Every section points at
volumes on the shelf, because the point is to go and look.

Fields, all optional except where noted:
    era        one of the ERAS names in the tracker -- paints the rail
    years      shown beside the era name
    h          section heading
    body       list of paragraphs, HTML allowed (b, i, em)
    fig        {"src":[paths], "cap":"..."} -- two paths render side by side
    makers     [{"n":name, "r":role, "b":what to look at}]
    quote      {"t":"...", "by":"..."}
    shelf      [volume ids] -> chips that jump to the book
    verdict    {"standing":..., "cls":""|"mixed"|"low"|"cult", "body":[paras]}
    tone       {"h":..., "sub":..., "modes":[{"l":..,"b":..,"vols":[..]}]}
"""

A = "Art/Tours/hulk/"

OVERVIEW = {
    "kicker": "Guided tour",
    "title": "The Hulk, decade by decade",
    "lede": (
        "The Hulk is the Marvel character who has been rebuilt the most times, and it "
        "started early: <b>his first series was cancelled after six issues</b>. Almost "
        "everything since has been an argument about what he is &mdash; a horror monster, "
        "a sad giant, a gangster, a psychiatric case study, a gladiator, a blockbuster, a "
        "haunted house. This is the tour of who did the rebuilding and why, so that when "
        "you open a 1968 book and a 1994 book you can see two different crafts rather than "
        "two versions of the same one."),
    "sections": [
        {
            "era": "Silver", "years": "1962–1968",
            "h": "A monster comic that happens to have a hero in it",
            "body": [
                "Stan Lee and Jack Kirby launched <i>The Incredible Hulk</i> in May 1962 as an "
                "explicit mash-up of the two horror stories everyone already knew &mdash; "
                "<b>Jekyll and Hyde for the transformation, Frankenstein for the sympathy</b>. "
                "That is the tone to read the first issues in. This is not an early superhero "
                "book with monster trappings; it is a monster book that keeps stumbling into "
                "superhero furniture.",
                "He was <b>grey</b>, because Lee wanted a colour that read as no ethnicity at "
                "all. The printer could not hold the tone consistently across a page, so from "
                "the second issue he is green &mdash; one of the great accidents in the medium. "
                "The grey is not forgotten, and it comes back as a whole personality twenty-five "
                "years later.",
                "Then the fact that shapes the next sixty years: <b>the book failed</b>. Six "
                "issues and cancelled. He came back in 1964 as half of <i>Tales to Astonish</i>, "
                "sharing the page count first with Giant-Man and then with the Sub-Mariner, and "
                "that is where the character actually learns to work &mdash; ten pages a month, "
                "no room for anything but the chase and the change."],
            "fig": {"src": [A + "hulk-1.jpg", A + "tta-93.jpg"],
                    "cap": "<b>Left:</b> Kirby's cover for #1, 1962 &mdash; the grey Hulk, and note "
                           "the copy is asking the reader a question rather than selling a hero. "
                           "<b>Right:</b> <i>Tales to Astonish</i> #93, the half-book years, where "
                           "the Hulk shared his own title with Namor."},
            "makers": [
                {"n": "Jack Kirby", "r": "Pencils, 1962–63",
                 "b": "Kirby's Hulk is <b>lumpen, not muscular</b> &mdash; a heavy, sloping "
                      "thing with a shelf of brow and short legs. Look at how little he is "
                      "posed. Kirby draws him standing in doorways and filling panels rather "
                      "than leaping through them; the menace is mass, not motion."},
                {"n": "Steve Ditko", "r": "Pencils, Tales to Astonish 1965–66",
                 "b": "Ditko's is <b>wirier and stranger</b>, with the nervous, spidery line "
                      "he was using on Spider-Man at the same time. His Hulk has hands that "
                      "are too big and a face that is genuinely unhappy. If Kirby's is a "
                      "boulder, Ditko's is a man with something wrong with him."},
                {"n": "Marie Severin", "r": "Pencils, Tales to Astonish #92–101 and Hulk #102–105",
                 "b": "Severin gives him the <b>first consistent design</b> &mdash; a settled "
                      "silhouette and a face that stays the same face from issue to issue. "
                      "Everything after 1968 is a variation on what she standardised."}],
            "shelf": ["inc-o1"],
        },
        {
            "era": "Silver", "years": "1968–1974",
            "h": "Herb Trimpe makes him a landscape",
            "body": [
                "<i>Tales to Astonish</i> became <i>The Incredible Hulk</i> again at #102 in 1968, "
                "keeping the old numbering, and <b>Herb Trimpe</b> took the book for roughly seven "
                "years. If you have a picture in your head of what a 1970s Hulk comic looks like, "
                "it is almost certainly Trimpe's.",
                "The tone settles into what people mean by the classic Hulk: <b>a wandering, "
                "sorrowful giant</b>, chased across deserts and continents by an army that will "
                "never catch him, occasionally finding somewhere he could be happy and then losing "
                "it. It is closer to <i>The Fugitive</i> or <i>Kung Fu</i> than to an Avengers "
                "book, and it is enormously sad on purpose.",
                "Trimpe also built most of the furniture the character still uses. Doc Samson, "
                "Jarella, the Hulkbusters and Jim Wilson are all his and Roy Thomas's."],
            "fig": {"src": [A + "hulk-102.jpg", A + "hulk-145.jpg"],
                    "cap": "The Hulk gets his title back at #102, and by the mid-70s the Trimpe "
                           "look is total &mdash; heavy black outline, the figure filling the "
                           "frame, and a lot of empty sky behind him."},
            "makers": [
                {"n": "Herb Trimpe", "r": "Pencils, 1968–75",
                 "b": "<b>Scale is the whole trick.</b> Trimpe draws the Hulk large in the frame "
                      "and everything else small, with a thick, almost woodcut outline that makes "
                      "him read as a solid object in a thin world. Watch for the low horizon and "
                      "the tiny running figures at his feet &mdash; he is composing landscapes "
                      "with a man in them, not fight scenes."}],
            "shelf": ["inc-o2", "inc-o3"],
        },
        {
            "era": "Bronze", "years": "1974–1977",
            "h": "The issue Wolverine walked out of",
            "body": [
                "The same book, two years on, and it produces the single most consequential page "
                "in Marvel's Bronze Age almost by accident. Roy Thomas, then editor-in-chief, "
                "asked <b>Len Wein</b> for a Canadian character; Wein and Trimpe put him in the "
                "last panel of <i>Incredible Hulk</i> #180 and gave him the cover of #181.",
                "It is worth reading #181 as a Hulk comic rather than as a Wolverine debut, "
                "because that is what it is &mdash; a fill-in-shaped fight in the Canadian woods "
                "with a Wendigo in it. The reason it matters is that Trimpe's Wolverine is "
                "<b>small</b>, and the smallness is the design. Everything the character became "
                "is downstream of an artist deciding to draw him as a short man who is not "
                "frightened.",
                "<b>Roger Stern</b> takes over the writing towards the end of this stretch, and "
                "#200 &mdash; Banner's mind toured from the inside &mdash; is the era's best "
                "single idea."],
            "fig": {"src": [A + "hulk-181.jpg"],
                    "cap": "<b>Incredible Hulk #181</b>, November 1974. Trimpe puts Wolverine "
                           "mid-air and mid-shout, and crucially draws him at a height that makes "
                           "the Hulk look enormous rather than making him look weak."},
            "shelf": ["inc-o4"],
        },
        {
            "era": "Bronze", "years": "1977–1987",
            "h": "The decade the shelf cannot show you",
            "body": [
                "<b>Nothing between Hulk #210 and #327 has ever been collected in omnibus</b>, so "
                "the shelf jumps 118 issues here. It is worth knowing what is in the hole, because "
                "it is not filler: this is <b>Bill Mantlo and Sal Buscema</b>, the longest "
                "continuous artist stint the book ever had, and the run that pushed hardest on "
                "Banner's childhood and on the Hulk as a damaged person rather than a force of "
                "nature.",
                "If the next volume feels like it starts mid-conversation, that is why. Marvel has "
                "collected the era in Epic Collections but not in omnibus, and until it does the "
                "shelf reads 1977 straight into 1987."],
            "shelf": ["inc-o4", "pad-o1"], "shelfLabel": "Either side of the gap",
        },
        {
            "era": "Copper", "years": "1987–1991",
            "h": "Peter David turns the book into a psychology",
            "body": [
                "<b>Peter David arrives at #328 in 1987 and stays for twelve years</b>, the "
                "longest single authorial run the character has had, and he does something none "
                "of his predecessors tried: he treats the transformations as a <i>diagnosis</i>. "
                "The Hulks are not moods, they are separate people, and the book is about a man "
                "with several of them.",
                "The first move is to bring back the grey Hulk and give him his own life. As "
                "<b>Joe Fixit</b> he is a Las Vegas casino enforcer &mdash; cunning, mean, funny, "
                "and out at night only, because the change is tied to sundown. For a stretch in "
                "the late 80s the Hulk book is essentially a <b>crime comedy</b>, which is a "
                "sentence nobody could have written in 1974.",
                "A young <b>Todd McFarlane</b> draws the first year of it. David has said he wrote "
                "to what his artists actually enjoyed drawing &mdash; McFarlane wanted machinery, "
                "so he got machinery &mdash; and you can see the book bending to each penciller in "
                "turn for the next decade."],
            "fig": {"src": [A + "hulk-340.jpg"],
                    "cap": "<b>Incredible Hulk #340</b>, McFarlane, 1988 &mdash; the most copied "
                           "Hulk cover there is. The whole image is Wolverine's claws with the "
                           "Hulk's face reflected in the blades. Note there is no action in it at "
                           "all; the tension is entirely in a reflection."},
            "quote": {"t": "Jack Kirby, just because, again, I don't draw like him, but his "
                           "storytelling was big and bombastic. John Byrne for the way that he "
                           "basically did some of his action. Gil Kane was a guy who when he hit "
                           "somebody, bam, it felt like you were getting shot out of a cannon. "
                           "George P&eacute;rez, he would draw machinery that still to this day "
                           "stuns me.",
                      "by": "Todd McFarlane, on his influences"},
            "makers": [
                {"n": "Todd McFarlane", "r": "Pencils, 1987–88",
                 "b": "Before the exaggeration he is famous for, this is McFarlane learning "
                      "<b>composition</b>. Look at how often he builds a page around one "
                      "off-centre shape and lets the rest go dark, and at how much of the "
                      "storytelling happens in reflections, shadows and framing devices rather "
                      "than in the figures."}],
            "shelf": ["pad-o1"],
        },
        {
            "era": "Copper", "years": "1990–1995",
            "h": "Keown, Frank, and the Hulk who could hold a conversation",
            "body": [
                "<b>Dale Keown</b> arrives and the Hulk gets the body he has arguably never lost: "
                "enormous trapezius, cross-hatched musculature, a physique drawn like an anatomy "
                "study performed by someone who is enjoying himself. It is the moment the book "
                "starts to look like the coming decade rather than the departing one.",
                "In <b>#377 (1991)</b> David and Keown merge the personalities into what everyone "
                "calls the Professor &mdash; the Hulk's body with Banner's mind and Joe Fixit's "
                "temperament. This is the single biggest tonal lever anyone ever pulled on the "
                "character. For most of the next few years the Hulk is <b>articulate, sarcastic "
                "and in charge</b>, leading a team, and if you have only ever met the "
                "'Hulk smash' version, this is the one that will surprise you.",
                "<b>Gary Frank</b> follows Keown and pulls the other way &mdash; smaller, more "
                "naturalistic, with genuine acting in the faces. And <b>George P&eacute;rez</b> "
                "drops in for <i>Future Imperfect</i>, which is two issues of the most densely "
                "furnished drawing on this shelf."],
            "fig": {"src": [A + "hulk-377.jpg", A + "hkfi-1.jpg"],
                    "cap": "<b>Left:</b> Keown's #377, the merged Hulk &mdash; a silhouette on "
                           "flat green, which is a strikingly modern design for 1991. "
                           "<b>Right:</b> P&eacute;rez's <i>Future Imperfect</i>. He fills the "
                           "Maestro's trophy room with decades of Marvel wreckage and expects "
                           "you to lean in and read it."},
            "makers": [
                {"n": "Dale Keown", "r": "Pencils, 1990–92",
                 "b": "The <b>silhouette</b> is the thing. Keown's Hulk reads correctly as a black "
                      "shape at thumbnail size, which is why #377 works as flat green and black. "
                      "Then get close and it is all rendering &mdash; cross-hatch on every muscle "
                      "boundary, a habit he took from the 80s and passed to the 90s."},
                {"n": "Gary Frank", "r": "Pencils, 1993–95",
                 "b": "Frank draws the <b>quiet</b> pages better than anyone else who worked on "
                      "this book. Watch what happens to the story when the Hulk is sitting down "
                      "and talking &mdash; Frank gives Betty and Bruce real expressions, so David "
                      "can write scenes that would collapse under a bigger artist."},
                {"n": "George Pérez", "r": "Pencils, Future Imperfect 1992",
                 "b": "P&eacute;rez's superpower is <b>density that stays readable</b>. Two-page "
                      "crowd shots where every figure is a specific person, and machinery drawn "
                      "with real mechanical logic. McFarlane singled him out for exactly this."}],
            "shelf": ["pad-o2", "pad-o3", "maestro-o1"],
        },
        {
            "era": "Chromium", "years": "1995–2000",
            "h": "The decade catches up with the book",
            "body": [
                "<b>Angel Medina</b> and <b>Adam Kubert</b> take the art to full 90s volume &mdash; "
                "bigger, angrier, more splash pages &mdash; while the line-wide machinery of "
                "Onslaught and Heroes Reborn starts reaching into the book and rearranging it. "
                "David has been open about the frustration; when the shelf's fourth Peter David "
                "volume goes strange, editorial is usually why.",
                "He leaves at <b>#467</b>, and the ending is one of the better-known exits in "
                "Marvel's 90s &mdash; a quiet, bleak issue that refuses to be a finale.",
                "Then <b>John Byrne</b> relaunches it in 1999 with <b>Ron Garney</b>, and is gone "
                "in seven issues after a dispute with editorial &mdash; the second time that had "
                "happened to Byrne on this exact title, having already lasted six issues in 1985. "
                "<b>Joe Casey</b> picks up the pieces. It is a genuine oddity of a book and it is "
                "on the shelf because the run it interrupts is worth seeing."],
            "fig": {"src": [A + "hulk-467.jpg", A + "hk99-1.jpg"],
                    "cap": "<b>Left:</b> #467, the last page of a twelve-year run. "
                           "<b>Right:</b> Byrne and Garney's 1999 relaunch, over almost as soon "
                           "as it starts."},
            "shelf": ["pad-o4", "byrne-o1"],
        },
        {
            "era": "Plastic", "years": "2001–2004",
            "h": "A paranoid thriller with a monster in it",
            "body": [
                "<b>Bruce Jones and John Romita Jr.</b> do the most radical thing on this shelf: "
                "they mostly <b>take the Hulk out of the Hulk comic</b>. Banner is on the run from "
                "a conspiracy, the storytelling is slow and decompressed in the Marvel Knights "
                "manner of the moment, and the smashing tends to happen off-panel or at the end "
                "of an issue.",
                "This is the 2000s house style in its purest form &mdash; cinematic pacing, few "
                "captions, dialogue doing the work, an arc built to be a trade paperback. Whether "
                "you love it depends almost entirely on whether you wanted a monster comic that "
                "withholds the monster.",
                "Look at what Romita Jr. does with it. He drops most of the line detail for "
                "<b>heavy black shapes and hard edges</b>, and the result is genuinely tense in a "
                "way his brighter superhero work is not."],
            "fig": {"src": [A + "hulk2-34.jpg", A + "hulk2-77.jpg"],
                    "cap": "<b>Left:</b> Romita Jr.'s <i>Return of the Monster</i> &mdash; a "
                           "silhouette, a fire, and no Hulk visible. <b>Right:</b> Peter David "
                           "returning to the character afterwards, in a completely different "
                           "register again."},
            "shelf": ["rotm-o1", "pad-o5"],
        },
        {
            "era": "Plastic", "years": "2006–2008",
            "h": "Cosmic: the Hulk as a sword-and-planet hero",
            "body": [
                "<b>Greg Pak</b> fires him into space and lands him on Sakaar, and the book stops "
                "being about Bruce Banner's problem for a year. <i>Planet Hulk</i> is "
                "<b>Gladiator, Conan and Flash Gordon</b> in a Marvel suit &mdash; slave, "
                "champion, rebel, king &mdash; with the Hulk as an actual protagonist who wants "
                "things and gets them.",
                "Then <i>World War Hulk</i> brings him home to take it out on the heroes who "
                "exiled him, and it is the rarest thing in this character's history: <b>the Hulk "
                "as the aggressor, and the reader on his side</b>.",
                "<b>Carlo Pagulayan</b> and <b>Aaron Lopresti</b> draw Sakaar as a real place with "
                "an economy and a costume department; <b>John Romita Jr.</b> comes back for the "
                "war and draws the best late-career action of his Marvel run."],
            "fig": {"src": [A + "hulk2-92.jpg", A + "wwh-1.jpg"],
                    "cap": "<b>Left:</b> <i>Planet Hulk</i> &mdash; note the armour and the "
                           "spear. He is being drawn as a barbarian hero, not as a monster. "
                           "<b>Right:</b> Romita Jr.'s <i>World War Hulk</i>, which is composed "
                           "as a disaster movie poster."},
            "shelf": ["planet-o1", "wwh-o1"],
        },
        {
            "era": "Plastic", "years": "2008–2010",
            "h": "Loud, red, and unembarrassed",
            "body": [
                "<b>Jeph Loeb and Ed McGuinness</b> follow the biggest Hulk story in decades with "
                "the most purely commercial one: a <b>Red Hulk</b>, a year-long whodunit about who "
                "is inside him, and a sequence of enormous fights staged like wrestling pay-per-"
                "views.",
                "It is the shelf's clearest example of a book built <b>for the art</b>. "
                "McGuinness's Hulk is cartoon-solid &mdash; huge silhouettes, clean thick line, "
                "colour blocked flat &mdash; and the writing exists mainly to arrange spectacular "
                "collisions in front of it. Read it as a poster book and it is tremendous fun; "
                "read it for character work and it will not give you any."],
            "fig": {"src": [A + "hulk08-1.jpg"],
                    "cap": "McGuinness, 2008. Flat red, no background, a shape that reads from "
                           "across a shop. This is cover design as advertising and it worked "
                           "&mdash; the book was a commercial hit."},
            "shelf": ["loeb-o1"],
        },
        {
            "era": "Modern", "years": "2018–2021",
            "h": "Horror comes back, and this time it stays",
            "body": [
                "<b>Al Ewing and Joe Bennett's <i>Immortal Hulk</i></b> is the run that reframed "
                "the character, and its move is disarmingly simple: it takes the horror premise "
                "of 1962 <i>literally</i>. He cannot die. He comes back at night. The "
                "transformations are wet and structural and hurt. Other books draw the Hulk as an "
                "athlete; this one draws him as something that should not be able to exist.",
                "Bennett's art is openly indebted to <b>Bernie Wrightson's <i>Swamp Thing</i></b> "
                "&mdash; heavy organic line, rendering that describes texture rather than muscle, "
                "and a willingness to leave a body in a state the rest of Marvel would cut away "
                "from. It is the best-reviewed Hulk run since Peter David, with multiple Eisner-"
                "winning issues.",
                "It also carries a genuine stain, and it is worth knowing before you get there: "
                "<b>issue #43 contained antisemitic imagery in a background detail</b>. Bennett "
                "apologised, Marvel corrected the art in reprints and collections and stopped "
                "assigning him work. The omnibus carries the corrected version."],
            "fig": {"src": [A + "imm-1.jpg"],
                    "cap": "Alex Ross's cover for <i>Immortal Hulk</i> #1. Compare it with #1 "
                           "from 1962 at the top of this tour &mdash; sixty years apart and both "
                           "are selling a monster, not a hero."},
            "shelf": ["imm-o1"],
        },
        {
            "era": "Contemporary", "years": "2021–2022",
            "h": "Science fiction at full throttle",
            "body": [
                "<b>Donny Cates and Ryan Ottley</b> deliberately swerve away from horror: Banner "
                "has turned his own body into a <b>vehicle</b>, piloting the Hulk from a cockpit "
                "in his head while the savage Hulk is kept in a permanent fight in the engine "
                "room. It is a high-concept, loud, blood-red action book.",
                "Ottley &mdash; who came from <i>Invincible</i>, a book about the physical cost of "
                "superhuman impact &mdash; draws collisions with weight and consequence, and this "
                "is the best-looking his Marvel work has been. Whether the concept lands is the "
                "single most argued-about thing on the modern half of this shelf."],
            "fig": {"src": [A + "hulk21-1.jpg"],
                    "cap": "Ottley's Hulk #1, 2021 &mdash; the character as machinery, lit from "
                           "below like a launch."},
            "shelf": ["cates-o1"],
        },
    ],
    "tone": {
        "h": "The tone map",
        "sub": "Same character, entirely different books. If you want a particular flavour of "
               "Hulk, this is where it lives on your shelf.",
        "modes": [
            {"l": "Most Jekyll-and-Hyde",
             "b": "The transformation as a curse the character is fighting, with real dread "
                  "attached. The 1962 issues invented it; <i>Immortal Hulk</i> is the version "
                  "that takes it most seriously.",
             "vols": ["inc-o1", "imm-o1"]},
            {"l": "Most sad-giant, most Bronze Age",
             "b": "A lonely, hunted, fundamentally gentle creature wandering the world. Trimpe's "
                  "seven years are the purest expression of it and the reason this is what most "
                  "people picture.",
             "vols": ["inc-o2", "inc-o3", "inc-o4"]},
            {"l": "Funniest",
             "b": "The Joe Fixit years &mdash; the grey Hulk as a Las Vegas leg-breaker in a "
                  "good suit. A genuine crime comedy, and unlike anything else here.",
             "vols": ["pad-o1"]},
            {"l": "Most psychological",
             "b": "Multiple personalities treated as a clinical problem rather than a plot "
                  "device, plus the articulate merged Hulk who can hold a conversation and "
                  "lead a team.",
             "vols": ["pad-o2", "pad-o3"]},
            {"l": "Most paranoid",
             "b": "Banner on the run, conspiracies, the monster mostly off-panel. A thriller "
                  "that happens to have the Hulk in it.",
             "vols": ["rotm-o1"]},
            {"l": "Most cosmic",
             "b": "Sword-and-planet adventure, then an invasion. The only period where he is "
                  "the protagonist with a plan rather than the problem.",
             "vols": ["planet-o1", "wwh-o1"]},
            {"l": "Loudest",
             "b": "Blockbuster slugfests drawn for maximum poster value. No subtext, "
                  "no apology.",
             "vols": ["loeb-o1"]},
            {"l": "Scariest",
             "b": "Body horror, night, and a creature that comes back. The modern classic, and "
                  "the one that most changes how the older books read.",
             "vols": ["imm-o1"]},
            {"l": "Bleakest",
             "b": "The Maestro &mdash; the Hulk who won, ruling the ruins. A dystopia the shelf "
                  "returns to across thirty years.",
             "vols": ["maestro-o1"]},
        ],
    },
}


VOLUMES = {

"inc-o1": {
    "kicker": "Volume 01 · 1962–1968",
    "title": "Incredible Hulk Omnibus Vol. 1",
    "lede": "The book that failed, and then quietly worked out what it was in half the page "
            "count. Six issues, forty-odd <i>Tales to Astonish</i> chapters, and four different "
            "artists finding four different Hulks.",
    "sections": [
        {"era": "Silver", "years": "1962–1963",
         "h": "Six issues and out",
         "body": [
             "Lee and Kirby's pitch was a monster as the lead &mdash; Jekyll and Hyde crossed "
             "with Frankenstein &mdash; and for six issues the book cannot decide what that "
             "means in practice. He is grey, then green; he changes at night, then by machine; "
             "he speaks in full sentences, then barely at all. <b>Read the inconsistency as "
             "process, not sloppiness.</b> Almost nothing about the character was settled.",
             "The colour change is the famous one: grey was chosen so he would read as no "
             "ethnicity, the printer could not hold it, and Lee liked the greenish tinge enough "
             "to keep it from #2."],
         "fig": {"src": [A + "hulk-1.jpg"],
                 "cap": "Kirby's #1. The cover is asking a question &mdash; <i>is he man or "
                        "monster?</i> &mdash; rather than selling a hero, which tells you "
                        "exactly what shelf Marvel thought this belonged on."}},
        {"era": "Silver", "years": "1964–1968",
         "h": "The half-book years, and where he actually gets good",
         "body": [
             "Revived in <i>Tales to Astonish</i> #59–60, he shares the title with Giant-Man and "
             "then Namor and gets about ten pages a month. The constraint does him a favour: "
             "every chapter has to be a chase, a change or a fight, and the strip develops a "
             "propulsive serial rhythm the failed solo book never had.",
             "Three artists to watch across it. <b>Ditko</b> brings the anxious, spidery line he "
             "was using on Spider-Man &mdash; his Hulk looks unwell. <b>Gil Kane</b> passes "
             "through with the most kinetic figure drawing in the book. Then <b>Marie Severin</b> "
             "settles the design from #92, and hers is the Hulk that gets handed to the 1970s.",
             "The volume closes on <i>Incredible Hulk</i> #102, where the title comes back and "
             "the numbering picks up as if nothing had happened."],
         "fig": {"src": [A + "tta-93.jpg", A + "hulk-102.jpg"],
                 "cap": "<b>Left:</b> the split book &mdash; his name is on it and he is sharing "
                        "it. <b>Right:</b> #102, and he has his title back."}},
    ],
    "verdict": {"standing": "Foundational", "cls": "",
                "body": [
                    "Universally treated as essential and rarely as anyone's favourite reading. "
                    "The consensus is that the <b>first six issues are historically fascinating "
                    "and genuinely rough</b> &mdash; the character is being invented in public "
                    "&mdash; while the <i>Tales to Astonish</i> run is much better paced than "
                    "its reputation and is where most readers say the book clicks.",
                    "The usual advice from long-time readers is to come to this volume "
                    "<b>second</b>, after you already like the character, and to read it for the "
                    "artists. It is also the only place to see how much of the Hulk was accident: "
                    "the colour, the cancellation, the revival as a back-up."]},
},

"inc-o2": {
    "kicker": "Volume 02 · 1968–1970",
    "title": "Incredible Hulk Omnibus Vol. 2",
    "lede": "Herb Trimpe takes the book and gives the character the look he will keep for a "
            "decade. This is where the 'classic' Hulk comic starts.",
    "sections": [
        {"era": "Silver", "years": "1968–1970",
         "h": "The Trimpe silhouette",
         "body": [
             "Trimpe's arrival is the single clearest before-and-after on this shelf. His Hulk is "
             "<b>drawn as an object with weight</b> &mdash; heavy black outline, mass over "
             "anatomy, and consistently big in the frame with the world scaled small around him. "
             "Fans and colleagues describe his storytelling as blunt and forceful, and that is a "
             "compliment: nothing on his pages is ambiguous.",
             "Roy Thomas is scripting, and the formula that will define the 70s locks in. The "
             "Hulk arrives somewhere, is misunderstood, is attacked, wins, and leaves alone. It "
             "sounds repetitive and it is; it is also <b>a machine for generating pathos</b>, and "
             "when it works the last panel of an issue is genuinely upsetting."],
         "makers": [{"n": "Herb Trimpe", "r": "Pencils",
                     "b": "Look at the <b>horizon line</b>. Trimpe drops it low so the Hulk is "
                          "always breaking the skyline, and fills the space behind him with flat "
                          "sky rather than detail. It is a cheap effect done extremely well and "
                          "it makes him read as huge on every page."}],
         "fig": {"src": [A + "hulk-102.jpg"],
                 "cap": "The relaunch cover, still Marie Severin's design being handed over. "
                        "Within a year Trimpe's version has replaced it entirely."}},
    ],
    "verdict": {"standing": "Classic era", "cls": "",
                "body": [
                    "Well liked rather than argued about. The consistent line from readers is "
                    "that <b>Trimpe is the definitive Bronze Age Hulk artist</b>, and this is "
                    "where you watch him take ownership.",
                    "The reservation people raise is the <b>repetitiveness of the plots</b> "
                    "&mdash; these are issue-length episodes built to the same shape, and read "
                    "in one sitting the shape shows. The standard advice is that these volumes "
                    "reward a few issues at a time rather than a marathon."]},
},

"inc-o3": {
    "kicker": "Volume 03 · 1971–1973",
    "title": "Incredible Hulk Omnibus Vol. 3",
    "lede": "The Bronze Age proper: Jarella, the Harpy, Doc Samson, and a book that finally "
            "lets its lead be loved by somebody.",
    "sections": [
        {"era": "Bronze", "years": "1971–1973",
         "h": "Marvel grows up around the book",
         "body": [
             "The early 70s is when Marvel becomes noticeably more serious &mdash; longer arcs, "
             "real consequences, social material &mdash; and the Hulk gets there through "
             "<b>relationships</b> rather than through grit. Jarella is the era's best idea: a "
             "world where the Hulk is intelligent, beloved and a king, which he then loses. The "
             "book had spent a decade insisting he could never be happy; this is the stretch that "
             "shows him happy so the loss lands.",
             "<b>Doc Samson</b> arrives here too, and he matters structurally: he is a "
             "psychiatrist, and once the book has one, the door to Peter David's version of the "
             "character in 1987 is open."],
         "fig": {"src": [A + "hulk-145.jpg"],
                 "cap": "Trimpe at full strength. The reading eye goes to the Hulk first and the "
                        "tiny fleeing figures second &mdash; his standard composition, and it "
                        "never stops working."}},
    ],
    "verdict": {"standing": "Fan favourite", "cls": "",
                "body": [
                    "The most affectionately regarded of the four numbered volumes. Jarella in "
                    "particular is the thing long-time readers bring up unprompted, and the Doc "
                    "Samson debut is treated as one of the era's few genuinely durable additions.",
                    "The critique is the same as Vol. 2's &mdash; <b>episodic to a fault</b> "
                    "&mdash; plus the observation that the guest-star density is climbing. If "
                    "you only read one Trimpe volume, this is usually the one people point at."]},
},

"inc-o4": {
    "kicker": "Volume 04 · 1974–1977",
    "title": "Incredible Hulk Omnibus Vol. 4",
    "lede": "The end of Trimpe's run, the arrival of Len Wein and Roger Stern, and one "
            "eleven-page fight in the Canadian woods that changed the company.",
    "sections": [
        {"era": "Bronze", "years": "1974",
         "h": "#180–181",
         "body": [
             "Roy Thomas wanted a Canadian character; Len Wein wrote him and Herb Trimpe drew "
             "him, and <b>Wolverine</b> appears in the last panel of #180 and on the cover of "
             "#181. It is now one of the most valuable Bronze Age comics in existence, which "
             "makes it easy to forget it is also just a good Hulk issue.",
             "The design decision worth studying is <b>height</b>. Trimpe draws Wolverine short "
             "and thick, and stages him leaping upward into frame, so the reader reads him as "
             "aggressive rather than outmatched. Every subsequent artist inherited that."],
         "fig": {"src": [A + "hulk-181.jpg"],
                 "cap": "Trimpe's #181, November 1974. Note the Hulk is drawn <i>above</i> the "
                        "logo and Wolverine <i>below</i> it, and it is still Wolverine your eye "
                        "goes to."}},
        {"era": "Bronze", "years": "1975–1977",
         "h": "Stern, and issue #200",
         "body": [
             "<b>Roger Stern</b> takes over and immediately does something the book had never "
             "tried: #200 goes <i>inside Banner's head</i> and tours it, with the Hulk as "
             "geography. It is the clearest ancestor of everything Peter David does a decade "
             "later, and it is the reason this volume is worth more than its Wolverine issue.",
             "Trimpe's departure is also in here. Seven years is an extraordinarily long stint "
             "and the book visibly loosens after it."]},
    ],
    "verdict": {"standing": "Key book", "cls": "",
                "body": [
                    "Its reputation is dominated by #181, and slightly unfairly so &mdash; the "
                    "issue's collector status has swallowed the discussion of everything around "
                    "it. Readers who get past that tend to rate <b>#200 and the late Stern "
                    "issues</b> as the strongest writing in any of the four numbered volumes.",
                    "This volume has <b>not shipped yet</b> &mdash; February 2027 &mdash; and is "
                    "on the shelf early because its contents, its links and its cover are all "
                    "real. See the note on its tile."]},
},

"pad-o1": {
    "kicker": "Volume 05 · 1987–1990",
    "title": "Incredible Hulk by Peter David Omnibus Vol. 1",
    "lede": "The most abrupt tonal change on the shelf. The Hulk becomes grey, verbal, "
            "calculating and funny, moves to Las Vegas, and takes a job as a casino enforcer.",
    "sections": [
        {"era": "Copper", "years": "1987–1990",
         "h": "Joe Fixit",
         "body": [
             "David's first structural move is to separate the Hulks into <b>people</b>. The grey "
             "one comes back, is smarter and meaner than the green one, only exists after dark, "
             "and given a few months of freedom he does not go on a rampage &mdash; he gets a "
             "suit, a hotel suite and a job breaking legs for a casino.",
             "For a long stretch this is a <b>crime comedy</b>, and it is genuinely funny. It is "
             "also the first time the book has an interior life to write about rather than a "
             "condition to depict.",
             "There is a jump to absorb before you start: <b>Hulk #210–327 has never been "
             "collected in omnibus</b>, so this opens 118 issues after Vol. 4 closes. Bill Mantlo "
             "and Sal Buscema's long run is in that hole."],
         "makers": [{"n": "Todd McFarlane", "r": "Pencils, the first year",
                     "b": "Early McFarlane, before the stylisation took over. What is already "
                          "fully formed is his <b>page architecture</b> &mdash; asymmetric "
                          "layouts, one dominant shape, heavy blacks, and storytelling that "
                          "happens through reflections and framing. #340 is the famous one and it "
                          "is famous for a compositional idea, not a rendering trick."},
                    {"n": "Jeff Purves", "r": "Pencils, 1988–90",
                     "b": "Purves is the run's underrated craftsman &mdash; a looser, more "
                          "cartoon-leaning line that suits the Las Vegas comedy far better than "
                          "McFarlane's moodiness would have. Watch how much acting he gets into "
                          "Fixit's face."}],
         "fig": {"src": [A + "hulk-340.jpg"],
                 "cap": "<b>#340.</b> The entire cover is a reflection. It is arguably the most "
                        "imitated Marvel cover of the decade, and there is no fight in it."}},
    ],
    "verdict": {"standing": "Strong start", "cls": "",
                "body": [
                    "Fondly regarded, and usually recommended as <b>the entry point to David's "
                    "run</b> rather than as its peak. The Joe Fixit material is the part people "
                    "single out &mdash; it is unlike any other Hulk comic and it holds up.",
                    "The McFarlane year is a large part of the volume's market value and a "
                    "smaller part of its critical reputation; readers coming for #340 sometimes "
                    "report that the writing around it is better than the art. The common "
                    "complaint is that the <b>first stretch is slow to establish itself</b> "
                    "before Fixit arrives."]},
},

"pad-o2": {
    "kicker": "Volume 06 · 1990–1992",
    "title": "Incredible Hulk by Peter David Omnibus Vol. 2",
    "lede": "Dale Keown arrives, the personalities merge, and the run hits the stretch most "
            "readers name as its peak.",
    "sections": [
        {"era": "Copper", "years": "1990–1992",
         "h": "#377, and the Hulk who talks",
         "body": [
             "In <b>#377</b> David and Keown fuse Banner, the savage Hulk and Joe Fixit into one "
             "person &mdash; the Hulk's body, Banner's intellect, Fixit's attitude. The character "
             "everyone calls the Professor. It is the largest tonal lever ever pulled on this "
             "book: for years afterwards the Hulk is <b>articulate, funny, competent and leading "
             "a team</b>.",
             "It also solves the problem the character had carried since 1962. A protagonist who "
             "cannot speak cannot drive a story; the Professor can, and David immediately starts "
             "writing arcs that would be impossible otherwise.",
             "<b>#400</b> is the anniversary issue and the era's showpiece."],
         "makers": [{"n": "Dale Keown", "r": "Pencils, 1990–92",
                     "b": "Two things at once. From across a room his Hulk is a <b>perfect black "
                          "silhouette</b> &mdash; #377's cover is literally that. Up close it is "
                          "dense cross-hatched rendering on every muscle boundary. That "
                          "combination of poster-clarity and rendering-density is the house style "
                          "the whole industry moves to in 1992, and Keown gets there first."}],
         "fig": {"src": [A + "hulk-377.jpg", A + "hulk-400.jpg"],
                 "cap": "<b>Left:</b> #377 &mdash; flat green, black shape, no rendering at all "
                        "on the cover of the issue that introduces the most rendered Hulk yet. "
                        "<b>Right:</b> #400."}},
    ],
    "verdict": {"standing": "The peak", "cls": "",
                "body": [
                    "When readers argue about the best part of Peter David's twelve years, "
                    "<b>this is the stretch that wins most often</b>. The combination of Keown's "
                    "art at its height and the merged-Hulk premise arriving fresh is the reason.",
                    "#377 is treated as one of the most important single Hulk issues ever "
                    "published, and Keown's run is routinely described as the character's "
                    "definitive modern look. The only real dissent comes from readers who prefer "
                    "the Hulk inarticulate and find the Professor a fundamental "
                    "de-clawing &mdash; a fair objection, and one the book itself starts "
                    "interrogating in the next volume."]},
},

"pad-o3": {
    "kicker": "Volume 07 · 1993–1995",
    "title": "Incredible Hulk by Peter David Omnibus Vol. 3",
    "lede": "Gary Frank makes the book quieter and better at acting, George Pérez shows up for "
            "two issues and steals the volume, and Bruce and Betty finally get married.",
    "sections": [
        {"era": "Chromium", "years": "1993–1995",
         "h": "Two artists pulling opposite ways",
         "body": [
             "<b>Gary Frank</b> follows Keown and deliberately dials the physique down. His Hulk "
             "is smaller, his people look like people, and his faces act &mdash; which lets David "
             "write long domestic scenes that would collapse under a more bombastic artist. The "
             "Betty and Bruce material in this volume is the most emotionally direct writing in "
             "the whole run.",
             "Then <b>George P&eacute;rez</b> arrives for <i>Future Imperfect</i> and does the "
             "opposite: maximum density, every panel crammed, a trophy room stacked with thirty "
             "years of Marvel wreckage that the reader is invited to inventory. Two issues, and "
             "they are the ones people remember."],
         "makers": [{"n": "Gary Frank", "r": "Pencils",
                     "b": "Watch the <b>eyebrows and mouths</b> in conversation scenes. Frank is "
                          "one of very few artists who worked on this book who can make a "
                          "seven-foot green man look embarrassed."},
                    {"n": "George Pérez", "r": "Pencils, Future Imperfect",
                     "b": "<b>Density that stays readable.</b> P&eacute;rez packs a page without "
                          "muddying the reading path &mdash; crowd scenes where every figure is a "
                          "specific person, machinery drawn with real mechanical logic. This is "
                          "the quality McFarlane singled him out for."}],
         "fig": {"src": [A + "hkfi-1.jpg", A + "hulk-435.jpg"],
                 "cap": "<b>Left:</b> <i>Future Imperfect</i>, P&eacute;rez. <b>Right:</b> mid-90s "
                        "<i>Incredible Hulk</i> &mdash; the decade's design language arriving on "
                        "the covers."}},
    ],
    "verdict": {"standing": "Classic", "cls": "",
                "body": [
                    "<i>Future Imperfect</i> is the reason this volume has the reputation it "
                    "does. It is widely treated as a <b>top-tier Hulk story</b> and the Maestro "
                    "as one of the few genuinely great late additions to the character's world; "
                    "P&eacute;rez's art is singled out constantly.",
                    "The Gary Frank issues are quieter in reputation but very well liked, and "
                    "readers who prefer character work to spectacle often rate them above the "
                    "Keown volume. The Troyjan War material is the part most often described as "
                    "forgettable."]},
},

"pad-o4": {
    "kicker": "Volume 08 · 1995–1997",
    "title": "Incredible Hulk by Peter David Omnibus Vol. 4",
    "lede": "The 90s at full volume, a line-wide crossover machine reaching into the book, and "
            "the end of a twelve-year run.",
    "sections": [
        {"era": "Chromium", "years": "1995–1997",
         "h": "Onslaught, and an author being overruled",
         "body": [
             "<b>Angel Medina</b> and <b>Adam Kubert</b> take the art to the decade's maximum "
             "&mdash; larger, angrier, more splash pages, more rendering. It is the most "
             "recognisably 1990s the book ever looks, and how much you enjoy it depends on your "
             "tolerance for that.",
             "Editorially this is the hardest stretch of the run. Onslaught and Heroes Reborn "
             "arrive, the Hulk is written into and out of line-wide plans, and David has been "
             "open since about the frustration of having stories rearranged around him. When the "
             "volume goes strange, that is usually why.",
             "It ends on <b>#467</b>, and the ending is the volume's best argument. After twelve "
             "years David closes not with a battle but with a quiet, bleak issue that refuses to "
             "resolve anything."],
         "fig": {"src": [A + "hulk-467.jpg"],
                 "cap": "#467 &mdash; the last issue of the longest run the character has had."}},
    ],
    "verdict": {"standing": "Divisive", "cls": "mixed",
                "body": [
                    "Consistently rated the <b>weakest of the four Peter David volumes</b>, and "
                    "the reasons given are usually external to David: crossover interference, a "
                    "book being pulled into Onslaught and Heroes Reborn, and an art direction "
                    "that has aged less well than Keown's or Frank's.",
                    "The counter-argument, which its defenders make firmly, is that <b>the final "
                    "stretch is excellent</b> &mdash; #454–467 in particular gets singled out as "
                    "some of David's best writing on the book, and #467 as one of the better "
                    "run-endings of the era. Read for the ending rather than the middle."]},
},

"maestro-o1": {
    "kicker": "Volume 09 · 1992–2022",
    "title": "Hulk: Maestro by Peter David Omnibus",
    "lede": "Thirty years of one idea: the Hulk who won, ruling the ruins of the world he "
            "helped end. Starts with a two-issue classic and follows the thread to the present.",
    "sections": [
        {"era": "Chromium", "years": "1992",
         "h": "Future Imperfect",
         "body": [
             "David and <b>George P&eacute;rez</b> throw the Hulk a century forward into a "
             "post-nuclear Earth ruled by a version of himself with Banner's intelligence and "
             "none of his restraint. It is a two-issue story and it has outlived most of the "
             "decade's much longer ones.",
             "The reason to read it as an <i>art</i> book: the Maestro's trophy room. "
             "P&eacute;rez fills a double-page spread with the remains of the Marvel Universe and "
             "expects the reader to stop and identify them. It is the most generous piece of "
             "drawing on this shelf."],
         "fig": {"src": [A + "hkfi-1.jpg"],
                 "cap": "P&eacute;rez, 1992. Compare the density here with the Keown cover on "
                        "Vol. 2 of the David run &mdash; same year, opposite philosophies."}},
        {"era": "Contemporary", "years": "2020–2022",
         "h": "The origin, thirty years later",
         "body": [
             "The later half of this book is David returning to the character in three modern "
             "miniseries to answer the question the original deliberately left alone: <b>how did "
             "he become that?</b> German Peralta draws most of it, and the tone is much closer to "
             "a post-apocalypse survival comic than to a superhero one.",
             "Note this volume <b>doubles back</b> over material in the numbered David volumes "
             "&mdash; <i>Future Imperfect</i> and Hulk #460–461 are in both. Those issues share "
             "ids on this shelf, so marking them here marks them there."]},
    ],
    "verdict": {"standing": "Classic core", "cls": "",
                "body": [
                    "<i>Future Imperfect</i> itself has an excellent reputation &mdash; commonly "
                    "named alongside <i>Planet Hulk</i> and <i>Immortal Hulk</i> when people "
                    "list the character's best stories, with P&eacute;rez's art doing much of the "
                    "lifting.",
                    "The modern Maestro miniseries are received more mildly: competent, "
                    "well-liked by readers already invested in the concept, and generally "
                    "considered to add texture rather than to justify themselves. This is a "
                    "volume most people buy for its first hundred pages."]},
},

"byrne-o1": {
    "kicker": "Volume 10 · 1998–2000",
    "title": "Incredible Hulk by Byrne & Casey Omnibus",
    "lede": "The awkward, interesting gap between two long runs: John Byrne relaunches the book, "
            "leaves in seven issues, and Joe Casey picks up the pieces.",
    "sections": [
        {"era": "Chromium", "years": "1998–2000",
         "h": "Byrne's second attempt, and second exit",
         "body": [
             "Byrne had already tried this book once, in 1985, and lasted six issues before a "
             "dispute with editor-in-chief Jim Shooter. He came back in 1999 with <b>Ron "
             "Garney</b> on art and was gone in seven, reportedly for similar reasons. There are "
             "very few creators with two aborted runs on the same title.",
             "What is here is a deliberate <b>back-to-basics</b> reading: strip out the "
             "Professor, strip out the Pantheon, return to Banner and a monster and General Ross. "
             "After twelve years of Peter David's elaboration that was a defensible instinct, and "
             "the fragments suggest it might have worked.",
             "<b>Joe Casey</b> takes over and writes the run that actually got told. It is the "
             "less discussed half and the more complete one."],
         "fig": {"src": [A + "hk99-1.jpg"],
                 "cap": "Garney's Hulk #1, 1999. Garney's line is looser and more brush-like than "
                        "the 90s house style &mdash; you can see the next decade coming."}},
    ],
    "verdict": {"standing": "Curiosity", "cls": "cult",
                "body": [
                    "Discussed mostly as <b>a might-have-been</b>. Byrne's Hulk has a small, "
                    "persistent following who regard both his aborted runs as among the more "
                    "interesting unrealised directions for the character, and the run has been "
                    "described as a cult favourite on exactly those grounds.",
                    "Casey's issues are the part with a real defence, and get respectful but "
                    "quiet notices. Nobody argues this is essential. It is on the shelf because "
                    "it is the only bridge between David and Bruce Jones, and because a run that "
                    "was cancelled twice tells you something about the book's editorial life that "
                    "the comics themselves do not."]},
},

"rotm-o1": {
    "kicker": "Volume 11 · 2001–2004",
    "title": "Incredible Hulk: Return of the Monster Omnibus",
    "lede": "The most formally radical book on the shelf, and the most argued about: a slow, "
            "cinematic conspiracy thriller that keeps the Hulk mostly off the page.",
    "sections": [
        {"era": "Plastic", "years": "2001–2004",
         "h": "Withholding the monster",
         "body": [
             "<b>Bruce Jones</b> writes Banner as a fugitive hunted by a shadow organisation, and "
             "the storytelling is <i>decompressed</i> in the way the early 2000s made standard "
             "&mdash; few captions, long silent sequences, dialogue carrying the load, each arc "
             "shaped to be a trade paperback. Whole issues go by with no transformation.",
             "This is the clearest example on the shelf of the <b>2000s house style</b>: Marvel "
             "chasing film pacing and new readers, and stripping out the caption-box tradition "
             "that had run since 1962. Read a Trimpe issue and then this and the difference in "
             "words-per-page is startling.",
             "<b>John Romita Jr.</b> is the reason it works as well as it does. He abandons most "
             "of his line detail for heavy black shapes and hard silhouettes, which is exactly "
             "right for a thriller and quite unlike his brighter superhero work."],
         "fig": {"src": [A + "hulk2-34.jpg"],
                 "cap": "Romita Jr.'s opening cover. A silhouette, a fire, and the title character "
                        "not actually visible &mdash; a statement of intent."}},
    ],
    "verdict": {"standing": "Divisive", "cls": "mixed",
                "body": [
                    "Genuinely split, and along a clean line. Readers who wanted a "
                    "<b>psychological thriller</b> rate it very highly &mdash; the opening arc in "
                    "particular is praised for atmosphere and for the nerve of keeping the Hulk "
                    "off-panel. Readers who came for a Hulk comic frequently find it frustrating "
                    "for exactly the same reason, and the phrase that recurs is that the smashing "
                    "happens off-camera.",
                    "The other common criticism is the <b>ending</b>: the conspiracy is built up "
                    "over dozens of issues and the resolution is broadly considered a let-down. "
                    "Romita Jr.'s art gets a much easier ride than the plotting, though even "
                    "there some readers find the faces hard to read emotionally.",
                    "Worth knowing: it is the whole run in one book, so you can judge the payoff "
                    "for yourself rather than taking the room's word for it."]},
},

"pad-o5": {
    "kicker": "Volume 12 · 2002–2021",
    "title": "Incredible Hulk by Peter David Omnibus Vol. 5",
    "lede": "Not a run &mdash; a collection. Everything Peter David wrote about the Hulk after "
            "1998, gathered rather than serialised, and it swings wildly in tone by design.",
    "sections": [
        {"era": "Plastic", "years": "2002–2010",
         "h": "The returns",
         "body": [
             "The substantial piece is <i>Tempest Fugit</i> &mdash; David back on the ongoing at "
             "#77–87, picking up directly from where Bruce Jones stops, and immediately "
             "reintroducing psychological ambiguity to a book that had spent three years being a "
             "thriller.",
             "<b><i>Hulk: The End</i></b> is the one to read first. It is a single issue about "
             "the last living thing on Earth being unable to die, and it is the bleakest thing "
             "David wrote for the character &mdash; and one of the most admired.",
             "The rest is genuinely a grab bag: a Fin Fang Foom one-shot, four issues of "
             "<i>Marvel Adventures</i> for children, a Symbiote Spider-Man mini. Do not read it "
             "front to back expecting a through-line; there isn't one."],
         "fig": {"src": [A + "hulk2-77.jpg"],
                 "cap": "<i>Tempest Fugit</i>. Note the register change from the Bruce Jones "
                        "covers &mdash; back to a visible Hulk, and back to ambiguity about what "
                        "is real."}},
    ],
    "verdict": {"standing": "Mixed bag", "cls": "mixed",
                "body": [
                    "Reception tracks the contents. <b><i>Hulk: The End</i> is highly regarded</b> "
                    "&mdash; frequently named among the best single Hulk issues &mdash; and "
                    "<i>Tempest Fugit</i> gets a warm, if not ecstatic, reception as a return to "
                    "form after the Jones years.",
                    "The volume as a whole is understood for what it is: a completist's book. "
                    "Nobody recommends it as an entry point, and the children's-line and "
                    "crossover material is generally treated as padding. It is on the shelf "
                    "because it closes David's account, and because <i>The End</i> deserves to be "
                    "somewhere."]},
},

"planet-o1": {
    "kicker": "Volume 13 · 2006–2007",
    "title": "Hulk: Planet Hulk Omnibus",
    "lede": "The best-regarded Hulk story of the century so far, and the one that proves the "
            "character works as a protagonist rather than a problem.",
    "sections": [
        {"era": "Plastic", "years": "2006–2007",
         "h": "Sword and planet",
         "body": [
             "<b>Greg Pak</b> exiles him to Sakaar and writes a full year of <i>Gladiator</i> "
             "crossed with <i>Conan</i> crossed with Flash Gordon &mdash; slave, arena champion, "
             "rebel, king. The Hulk has goals, allies, a romance and a plan, which is nearly "
             "unprecedented in forty years of the book.",
             "Structurally it works because <b>Sakaar removes Bruce Banner from the equation</b>. "
             "With nobody on the planet who knows or cares who Banner is, the Hulk stops being a "
             "condition and becomes a person, and the reader finds out how much of the character "
             "was being carried by the tragedy.",
             "<b>Carlo Pagulayan</b> and <b>Aaron Lopresti</b> build the planet properly &mdash; "
             "armour with a culture behind it, insects, tech, geology. The world-building is done "
             "in the drawing, not in captions."],
         "fig": {"src": [A + "hulk2-92.jpg"],
                 "cap": "He is being drawn as a barbarian hero &mdash; spear, armour, a heroic "
                        "low angle. Compare it with any cover in the first four volumes, where "
                        "the composition always makes him the thing going wrong."}},
    ],
    "verdict": {"standing": "Modern classic", "cls": "",
                "body": [
                    "About as close to consensus as this shelf gets. It is routinely named the "
                    "character's best modern story, sales on <i>Incredible Hulk</i> actually rose "
                    "during it, and it is one of the very few Hulk arcs to be adapted twice "
                    "&mdash; as an animated film and, in substance, as <i>Thor: Ragnarok</i>.",
                    "The praise is specifically for <b>the Hulk as a lead</b>, and for a "
                    "supporting cast readers genuinely cared about &mdash; which is what makes "
                    "the ending land as hard as it does.",
                    "If someone is going to read exactly one book on this shelf, this is usually "
                    "the one recommended, with <i>Immortal Hulk</i> the other answer."]},
},

"wwh-o1": {
    "kicker": "Volume 14 · 2007–2008",
    "title": "Hulk: World War Hulk Omnibus",
    "lede": "He comes home for the people who exiled him. The rarest configuration in the "
            "character's history: the Hulk as the aggressor, and the reader on his side.",
    "sections": [
        {"era": "Plastic", "years": "2007–2008",
         "h": "The one where he is right",
         "body": [
             "Every Hulk story before this is built on the reader wanting him <i>stopped</i>. "
             "<b>World War Hulk inverts it</b> &mdash; the Illuminati did something "
             "indefensible, he has an actual grievance, and the heroes trying to stop him are in "
             "the wrong. That single inversion is why the event has lasted.",
             "<b>John Romita Jr.</b> returns and delivers the best late-career action of his "
             "Marvel run &mdash; enormous, weighty, staged like a disaster film, with a Hulk who "
             "is drawn heavier and slower than the 90s versions and hits harder for it.",
             "Be aware of the shape of the book: the core series is five issues, and this omnibus "
             "collects <b>every tie-in and the whole Aftersmash line</b>, each as its own chapter. "
             "It is a complete event, not a curated one."],
         "fig": {"src": [A + "wwh-1.jpg"],
                 "cap": "Romita Jr., composing a movie poster. The Earth is behind him and he is "
                        "coming at you &mdash; the reverse of every Trimpe cover, where the world "
                        "is what he is running away into."}},
    ],
    "verdict": {"standing": "Well liked", "cls": "",
                "body": [
                    "Regarded as a rare event that <b>delivers what it promises</b>, and as the "
                    "proper payoff to <i>Planet Hulk</i> rather than a cash-in. Romita Jr.'s art "
                    "and the moral inversion are the two things praised most consistently.",
                    "The reservations are structural. Readers frequently note the "
                    "<b>tie-in bloat</b> &mdash; the core five issues are excellent and the "
                    "surrounding forty-odd are variable &mdash; and some find the ending abrupt. "
                    "The common advice is to read the core series and <i>Incredible Hulk</i> "
                    "#106–111 first and treat the rest as optional."]},
},

"loeb-o1": {
    "kicker": "Volume 15 · 2008–2010",
    "title": "Hulk by Loeb & McGuinness Omnibus",
    "lede": "A red Hulk, a year-long whodunit, and some of the loudest, most unembarrassed "
            "superhero art of its decade. The shelf's biggest gap between commercial success and "
            "critical standing.",
    "sections": [
        {"era": "Plastic", "years": "2008–2010",
         "h": "Built for the artist",
         "body": [
             "This is a book designed around <b>Ed McGuinness</b>, and understanding that is the "
             "key to enjoying it. His Hulk is cartoon-solid &mdash; vast simplified silhouettes, "
             "a thick confident line, flat blocked colour, and figures posed for maximum "
             "readability at a glance. The writing exists mainly to arrange spectacular "
             "collisions in front of it.",
             "<b>Jeph Loeb</b> runs a mystery &mdash; who is the Red Hulk? &mdash; across the "
             "whole first stretch, and stages set-piece fights against increasingly implausible "
             "opponents while it plays out.",
             "Tonally it is a deliberate throwback. Several readers describe it as reading like a "
             "<b>late-80s or early-90s comic published in 2008</b>, and that is fair. Whether it "
             "is a criticism depends on what you want."],
         "fig": {"src": [A + "hulk08-1.jpg"],
                 "cap": "Flat red, no background, one shape. This is cover-as-advertising and it "
                        "is extremely good at that job &mdash; the book sold enormously."}},
    ],
    "verdict": {"standing": "Low point for many", "cls": "low",
                "body": [
                    "The most negatively received book on this shelf, though 'panned' overstates "
                    "it &mdash; the reception is <b>sharply split rather than uniform</b>. The "
                    "recurring criticisms are that the plotting is thin and predictable, that the "
                    "book felt rudderless until the Red Hulk's identity was revealed, and that "
                    "the character is written so over-powered that the fights stop having stakes.",
                    "<b>McGuinness's art is the consistent exception</b>, and even readers who "
                    "dislike the run say his style is a natural fit for the character. It also "
                    "sold extremely well and the Red Hulk stuck as a permanent addition to the "
                    "cast, which is a kind of verdict too.",
                    "Read it directly after <i>World War Hulk</i> and the drop in ambition is "
                    "stark. Read it on its own as a spectacle book and it is a good time."]},
},

"imm-o1": {
    "kicker": "Volume 16 · 2018–2021",
    "title": "Immortal Hulk Omnibus",
    "lede": "Horror, taken literally. The run that reframed the character and the best-reviewed "
            "Hulk comic since Peter David.",
    "sections": [
        {"era": "Modern", "years": "2018–2021",
         "h": "Taking 1962 seriously",
         "body": [
             "<b>Al Ewing's</b> move is not to reinvent but to <i>believe</i> the original "
             "premise. If a man turns into a monster at night and cannot be killed, that is a "
             "horror story, and the book commits to it completely &mdash; a procedural structure, "
             "a rising cosmology, and genuine dread.",
             "The consequence is that the transformations get <b>bodily</b>. Bones move, tissue "
             "reassembles, injuries persist in ways other Marvel books cut away from. It is the "
             "first Hulk run where being the Hulk is depicted as something that <i>happens to a "
             "body</i>.",
             "<b>Joe Bennett</b> draws it with an open debt to <b>Bernie Wrightson's <i>Swamp "
             "Thing</i></b> &mdash; heavy organic line, rendering that describes wet texture "
             "rather than muscle definition, and a lot of low, upward-looking angles that make "
             "the reader the smaller thing in the panel."],
         "makers": [{"n": "Al Ewing", "r": "Writer",
                     "b": "Watch the <b>structure</b>. Early issues are near-standalone horror "
                          "episodes with a fixed shape; as the run goes on that shape is used "
                          "against you, and things you were taught to expect stop happening. It "
                          "is a long-form trick and it needs the full fifty issues to work."},
                    {"n": "Joe Bennett", "r": "Pencils",
                     "b": "Look at <b>where the light comes from</b>. Bennett lights faces from "
                          "below constantly &mdash; the oldest horror-cinema trick there is "
                          "&mdash; and renders skin as something with fluid under it rather than "
                          "as a surface over muscle."}],
         "fig": {"src": [A + "imm-1.jpg", A + "hulk-1.jpg"],
                 "cap": "<b>Left:</b> Alex Ross, 2018. <b>Right:</b> Kirby, 1962. Fifty-six years "
                        "apart, and both covers are selling the same thing &mdash; a monster you "
                        "are supposed to be afraid of."}},
        {"era": "Modern", "years": "2021",
         "h": "One thing to know before you get there",
         "body": [
             "<b>Issue #43 contained antisemitic imagery</b> in a background detail &mdash; a "
             "shop sign and a Star of David in a jewellery-store window. Bennett said the "
             "lettering error was a mistake but accepted there was no excuse for the "
             "depiction, and apologised; Marvel corrected the art in digital, reprints and "
             "collected editions and subsequently stopped assigning him work.",
             "The omnibus carries the corrected art. It is recorded here because it is part of "
             "the run's history and because finding out about it afterwards is worse."]},
    ],
    "verdict": {"standing": "Modern classic", "cls": "",
                "body": [
                    "Very widely held to be the <b>best Hulk run since Peter David</b>, with "
                    "multiple Eisner-winning issues, and credited with making the character "
                    "frightening again after a decade of blockbuster treatment. It has also "
                    "changed how the older books read &mdash; a lot of readers go back to 1962 "
                    "after this and find it much more of a horror comic than they remembered.",
                    "Criticism exists and is mostly about <b>the last act</b>: as the cosmology "
                    "expands the book moves away from the tight horror procedural that made its "
                    "reputation, and some readers feel the ending over-explains. The #43 "
                    "controversy is the other thing that comes up, and reasonably so.",
                    "With <i>Planet Hulk</i>, one of the two books people name when asked where "
                    "to start with the modern character."]},
},

"cates-o1": {
    "kicker": "Volume 17 · 2021–2022",
    "title": "Hulk by Cates & Ottley Omnibus",
    "lede": "A hard swerve away from horror into loud science fiction: Banner has turned his own "
            "body into a spacecraft and is flying it.",
    "sections": [
        {"era": "Contemporary", "years": "2021–2022",
         "h": "Starship Hulk",
         "body": [
             "<b>Donny Cates</b> follows the most acclaimed Hulk run in thirty years by refusing "
             "to compete with it. Where <i>Immortal Hulk</i> was gothic, slow and interior, this "
             "is <b>high-concept, fast and external</b>: Banner pilots the Hulk from a cockpit in "
             "his own mind while the savage Hulk is kept in the engine room in a permanent fight, "
             "generating the power.",
             "<b>Ryan Ottley</b> came from <i>Invincible</i>, a book fundamentally about what "
             "superhuman impacts do to bodies, and he brings that to this &mdash; collisions with "
             "real weight and real consequence, and the best-looking Marvel work of his career.",
             "It runs directly into <i>Banner of War</i>, the Thor crossover, which is why two "
             "Thor issues sit inside the reading order on the tile."],
         "fig": {"src": [A + "hulk21-1.jpg"],
                 "cap": "Ottley's #1. The character presented as machinery and lit from below "
                        "like a launch &mdash; a deliberate visual break from the Bennett era it "
                        "follows."}},
    ],
    "verdict": {"standing": "Divisive", "cls": "mixed",
                "body": [
                    "The most argued-about recent book on the shelf. The <b>art is close to "
                    "universally praised</b> &mdash; readers who dislike the run still rate "
                    "Ottley's work on it highly.",
                    "The premise is where opinion splits. Supporters read it as a bold, "
                    "committed swing and enjoy the sheer velocity; detractors find it a gimmick, "
                    "argue it strips away the thematic weight <i>Immortal Hulk</i> had just "
                    "spent fifty issues building, and say it does not tell you anything new about "
                    "Banner. The ending draws its own complaints for not delivering the "
                    "confrontation the run had been promising.",
                    "The fairest framing is that it is <b>a good action comic following a great "
                    "literary one</b>, and it has been judged against its predecessor more than "
                    "on its own terms."]},
},

}

TOUR = {"overview": OVERVIEW, "volumes": VOLUMES}
