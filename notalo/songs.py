"""곡 페이지 메타. 악보는 songs/<slug>.ly(내가 직접 입력한 퍼블릭 도메인 멜로디 + 단순 왼손), 산출물은 tools/build_songs.py가
static/songs/<slug>.{png,mid,json}으로 만듦. 저작권: 여기 있는 곡은 전부 작곡가 사후 70년 지난 PD. 가사는 안 씀. 편곡은 우리 것."""

SONGS = {
    "jingle-bells": {
        "title": "Jingle Bells", "composer": "James Lord Pierpont", "year": 1857, "key": "G major", "time": "4/4", "bpm": 120,
        "christmas": True,
        "intro": "The chorus everyone knows, then the first verse (“Dashing through the snow”), in G major with one sharp: every F is F♯. The right hand stays inside one octave, so it is a good first Christmas piece.",
        "tips": ["Chorus first: bars 1–8 are just B, D, G, A and C — five notes.", "The left hand is one chord per bar; hold it and let the melody do the work.", "Watch the F♯ in the verse (bar 22): it is the only sharp in the whole piece."],
    },
    "silent-night": {
        "title": "Silent Night", "composer": "Franz Xaver Gruber", "year": 1818, "key": "C major", "time": "6/8", "bpm": 60,
        "christmas": True,
        "intro": "Gruber’s carol in C major, so there are no sharps or flats at all. The 6/8 time means two gentle pulses per bar — count “1-2-3 4-5-6” and let the dotted rhythm (long–short) rock the melody.",
        "tips": ["The opening G–A–G–E shape comes back four times; learn it once.", "Bar 9 has the highest note (F) and bar 12 ends on a long C.", "Play the left-hand chords softly — this one is about the melody."],
    },
    "we-wish-you-a-merry-christmas": {
        "title": "We Wish You a Merry Christmas", "composer": "Traditional (West Country, England)", "year": 1500, "year_text": "16th century", "key": "G major", "time": "3/4", "bpm": 132,
        "christmas": True,
        "intro": "The English carol in G major, 3/4 time. It starts on a pick-up note (a single D before the first full bar), and the same four-bar phrase is sung three times before “and a happy new year”.",
        "tips": ["Bars 1–4 and 5–8 are the same pattern one note higher each time — G, then A, then B.", "“Good tidings we bring” (bar 9) is the only place the tune sits still: long G, long F♯.", "The pick-up D at the very start is not a mistake; the first bar has only one beat."],
    },
    "deck-the-halls": {
        "title": "Deck the Halls", "composer": "Traditional (Welsh melody “Nos Galan”)", "year": 1500, "year_text": "16th century", "key": "C major", "time": "4/4", "bpm": 120,
        "christmas": True,
        "intro": "The Welsh melody in C major with no sharps or flats. Every “fa-la-la-la-la” is the same descending run, so once you have bar 1 you have most of the piece.",
        "tips": ["The first phrase steps straight down: G–F–E–D–C.", "Lines 1, 2 and 4 are nearly identical; only line 3 (bars 9–12) is new.", "Bar 11 has the one F♯ in the piece, then it returns to C major."],
    },
    "happy-birthday": {
        "title": "Happy Birthday", "composer": "Mildred J. Hill and Patty S. Hill (\u201cGood Morning to All\u201d)", "year": 1893, "key": "F major", "time": "3/4", "bpm": 100,
        "intro": "The melody every beginner is asked to play, in F major (one flat: every B is B\u266d). It starts with two quick pick-up notes on C, and the whole tune fits in eight bars.",
        "tips": ["The two C\u2019s before the first bar line are the \u201cHap-py\u201d pick-up \u2014 short and light.", "Bar 5 jumps up to the high C; that is the one stretch in the piece.", "Bar 6 has the B\u266d \u2014 the key signature applies it automatically."],
    },
    "fur-elise": {
        "title": "F\u00fcr Elise", "composer": "Ludwig van Beethoven", "year": 1810, "key": "A minor", "time": "3/8", "bpm": 72,
        "intro": "The famous opening eight bars, in A minor. Where Beethoven wrote a rest after the first note of a bar, this beginner arrangement holds the note instead, so the letters and the MIDI line up beat for beat.",
        "tips": ["The E\u2013D\u266f\u2013E\u2013D\u266f\u2013E trill is two keys next to each other: white E, black D\u266f.", "Bar 3 has G\u266f in the right hand and in the left-hand chord \u2014 both black keys.", "Play the left-hand chords as gently as you can; the melody is the whole point."],
    },
    "twinkle-twinkle-little-star": {
        "title": "Twinkle Twinkle Little Star", "composer": "Traditional (French, \u201cAh! vous dirai-je, maman\u201d)", "year": 1761, "year_text": "18th century", "key": "C major", "time": "4/4", "bpm": 100,
        "intro": "All white keys, C major, twelve bars. The first and last four bars are identical, and the middle four are one phrase played twice \u2014 so you only learn two ideas.",
        "tips": ["The opening C\u2013C\u2013G\u2013G jump is the only leap; everything else moves by step.", "Bars 5\u20138 (\u201cup above the world so high\u201d) walk straight down from G to D, twice.", "Two chords in the left hand per bar \u2014 C, F and G only."],
    },
    "canon-in-d": {
        "title": "Canon in D", "composer": "Johann Pachelbel", "year": 1680, "year_text": "c. 1680", "key": "D major", "time": "4/4", "bpm": 66,
        "intro": "The first violin entry of Pachelbel\u2019s Canon over the famous eight-note ground bass, simplified for one player. D major has two sharps: every F and every C are sharp.",
        "tips": ["The left hand plays the same eight bass notes forever: D A B F\u266f G D G A. Learn it first, with eyes closed.", "The right hand mostly steps down; the only tricky bar is 7 (D B D A).", "Keep it slow \u2014 66 BPM \u2014 and let the bass line lead."],
    },
    "ode-to-joy": {
        "title": "Ode to Joy", "composer": "Ludwig van Beethoven (Symphony No. 9)", "year": 1824, "key": "C major", "time": "4/4", "bpm": 108,
        "intro": "The theme from the Ninth Symphony, moved to C major so there are no sharps or flats. Sixteen bars; the third line (bars 9\u201312) is the only part that differs from the first.",
        "tips": ["The right hand uses only five notes for the first eight bars: C D E F G.", "Bar 4 and bar 8 end with a dotted quarter + eighth \u2014 \u201clong\u2013short\u201d.", "Bar 12 dips to the G below middle C, the lowest note in the piece."],
    },
    "amazing-grace": {
        "title": "Amazing Grace", "composer": "Traditional (\u201cNew Britain\u201d, Southern Harmony)", "year": 1835, "key": "G major", "time": "3/4", "bpm": 80,
        "intro": "The hymn tune in G major, 3/4 time, starting on a single pick-up note. It uses only the five notes of the pentatonic scale \u2014 G A B D E \u2014 so there are no half-steps to catch you out.",
        "tips": ["No F\u266f is ever played in the right hand, even though the key has one.", "Bars 7\u20138 reach the high D \u2014 the top of the tune.", "Hold the long notes for their full two beats; the tune is about breathing."],
    },
    "moonlight-sonata": {
        "title": "Moonlight Sonata (1st movement, easy)", "composer": "Ludwig van Beethoven", "year": 1801, "key": "A minor", "time": "12/8", "bpm": 50,
        "intro": "The opening eight bars of the first movement, moved from C\u266f minor to A minor and written in 12/8 so the triplets become plain eighth notes. Same shape, far fewer sharps.",
        "tips": ["Each bar is the same three-note pattern (low, middle, high) four times \u2014 learn one, get the bar.", "Bar 4 introduces G\u266f, a black key; it comes back in bar 7.", "Left hand holds long two-note chords; keep them quiet under the arpeggios."],
    },
    "minuet-in-g": {
        "title": "Minuet in G", "composer": "Christian Petzold (from the Notebook for Anna Magdalena Bach)", "year": 1725, "year_text": "c. 1725", "key": "G major", "time": "3/4", "bpm": 112,
        "intro": "The minuet everyone learns from the Anna Magdalena Bach notebook, first half (16 bars). G major, one sharp. The second eight bars repeat the first with a different ending.",
        "tips": ["Bar 3 climbs to the high G \u2014 the peak of the phrase.", "Bars 7\u20138 and 15\u201316 are the two endings: first to A, then home to G.", "Count \u201c1 2 3\u201d out loud; the quarter-then-eighths rhythm is the whole character."],
    },
    "greensleeves": {
        "title": "Greensleeves", "composer": "Traditional (English)", "year": 1580, "year_text": "16th century", "key": "A minor", "time": "6/8", "bpm": 92,
        "intro": "Verse and chorus in A minor, 6/8 time. The G\u266f and F\u266f accidentals give it the old modal color \u2014 watch for them, they are written in the bars where they happen.",
        "tips": ["The verse (bars 1\u201310) and chorus (bars 11\u201320) share the same second half.", "G\u266f appears in bars 4, 5, 9, 14, 15 and 19 \u2014 always a black key.", "6/8: two big beats per bar, three eighths each. Sway, don\u2019t march."],
    },
    "mary-had-a-little-lamb": {
        "title": "Mary Had a Little Lamb", "composer": "Traditional (rhyme published by Sarah Josepha Hale)", "year": 1830, "key": "C major", "time": "4/4", "bpm": 110,
        "intro": "The nursery rhyme melody in C major \u2014 no sharps or flats, and every note falls between middle C and G. A good first piece: the whole right hand sits in one five-finger position.",
        "tips": ["Right hand never leaves the C-D-E-F-G position \u2014 no thumb-crossing needed.", "Bars 1 and 5 are identical; once you learn one you know both.", "Left hand is one chord per bar \u2014 C, then G, then back to C."],
    },
    "old-macdonald-had-a-farm": {
        "title": "Old MacDonald Had a Farm", "composer": "Traditional (American)", "year": 1917, "year_text": "early 20th century (verses published)", "key": "C major", "time": "4/4", "bpm": 120,
        "intro": "The main \u201cE-I-E-I-O\u201d phrase in C major, played twice. Simplified for easy piano \u2014 the many-verse \u201chere a moo, there a moo\u201d section is left out; this is the tune everyone actually remembers.",
        "tips": ["Bars 1\u20134 and 5\u20138 are exactly the same \u2014 learn one phrase, play the whole song.", "The left hand switches just once per phrase, C to F and back.", "The held whole note at the end of each phrase is the \u201cO\u201d \u2014 let it ring."],
    },
    "chopsticks": {
        "title": "Chopsticks", "composer": "Euphemia Allen (published as \u201cThe Celebrated Chop Waltz\u201d)", "year": 1877, "key": "C major", "time": "4/4", "bpm": 132,
        "intro": "The two-finger novelty piece everyone plays first, written out as three letters (F E D) sliding down to C, four times. No sharps, no flats, no left-hand melody to learn.",
        "tips": ["Only four different notes in the whole piece: F, E, D and C.", "Every bar has the exact same shape \u2014 once it's memorized, speed is the only challenge.", "The left hand just holds a C chord throughout \u2014 focus all your attention on the right hand."],
    },
    "joy-to-the-world": {
        "title": "Joy to the World", "composer": "Lowell Mason (adapted from themes attributed to Handel)", "year": 1848, "key": "C major", "time": "4/4", "bpm": 100,
        "christmas": True,
        "intro": "Famous for its opening: a full descending scale from high C down to middle C, one note per word (\u201cJoy-to-the-world-the-Lord-is-come\u201d). C major, no sharps or flats.",
        "tips": ["Bars 1\u20132 are just the C major scale played backwards \u2014 the easiest \u201chard-sounding\u201d line in piano.", "Bars 7\u20138 repeat bars 1\u20132, so the piece is shorter to learn than it looks.", "Keep the descending scale even \u2014 no note should be louder or slower than the others."],
    },
    "the-first-noel": {
        "title": "The First Noel", "composer": "Traditional (English)", "year": 1823, "year_text": "early 19th century (first published)", "key": "C major", "time": "4/4", "bpm": 100,
        "christmas": True,
        "intro": "The opening verse and the \u201cNoel, Noel\u201d refrain, in C major. Simplified to the two most recognizable phrases of this English carol \u2014 the middle verses are left out.",
        "tips": ["The verse climbs step by step from C up to the high C \u2014 a good stretch for a beginner.", "\u201cNoel, Noel\u201d (the refrain) is the same short phrase sung twice.", "The last line \u2014 \u201cBorn is the King of Israel\u201d \u2014 is the highest and longest phrase; take it slowly."],
    },
    "auld-lang-syne": {
        "title": "Auld Lang Syne", "composer": "Traditional (Scottish), words by Robert Burns", "year": 1788, "key": "D major", "time": "4/4", "bpm": 100,
        "intro": "The New Year's Eve song everyone hums but few can name past the first line, in D major (two sharps: F\u266f and C\u266f). A pentatonic Scottish melody \u2014 mostly skips, few steps.",
        "tips": ["The tune leans on just five notes (D, E, G, A, B) \u2014 very few half-steps to worry about.", "F\u266f and C\u266f come from the key signature \u2014 every F and C in the piece is sharp.", "The last line repeats the second line almost exactly \u2014 free repetition."],
    },
    "o-holy-night": {
        "title": "O Holy Night", "composer": "Adolphe Adam", "year": 1847, "key": "C major", "time": "4/4", "bpm": 84,
        "christmas": True,
        "intro": "The opening verse \u2014 \u201cO holy night, the stars are brightly shining, it is the night of our dear Savior's birth\u201d \u2014 in C major. Simplified to this one phrase; the famous \u201cFall on your knees\u201d climax reaches a full octave higher and is left for a later, more advanced arrangement.",
        "tips": ["The whole phrase stays within one octave \u2014 no big jumps to worry about.", "Bar 3's high C is the peak of this phrase \u2014 lean into it, then ease back down.", "Left hand holds one chord per bar throughout \u2014 keep it soft under the melody."],
    },
    "twelve-days-of-christmas": {
        "title": "The Twelve Days of Christmas", "composer": "Traditional (English)", "year": 1780, "year_text": "18th century (melody by Frederic Austin, 1909)", "key": "F major", "time": "4/4", "bpm": 112,
        "christmas": True,
        "intro": "The first two verses — “On the first day of Christmas” through “two turtle doves and a partridge in a pear tree” — in F major with one flat. Every later verse just repeats the same two phrases, so once you have these nine bars you have the whole song.",
        "tips": ["The only black key is B♭, which appears in almost every bar — keep the fourth finger ready for it.", "“A partridge in a pear tree” climbs to the high D in bar 3 and bar 8: that is the top of the piece.", "The pickup “On the” starts on C before the first bar line — count “3, 4” and come in."],
    },
    "ave-maria": {
        "title": "Ave Maria (Schubert, easy)", "composer": "Franz Schubert", "year": 1825, "key": "C major", "time": "4/4", "bpm": 60,
        "intro": "The opening of Schubert's Ave Maria, moved from B♭ major to C major and simplified to a single melodic line: the long held note, the turn that follows it, and the first “gratia plena” phrase with its two chromatic notes.",
        "tips": ["Bar 1 is one long G — count all three beats before the turn starts.", "Bar 5 has a G♯ and a B♭ in the same bar: both are black keys, both are passing notes back to the white keys either side.", "Play everything legato and very slowly; the piece is a prayer, not a march."],
    },
    "eine-kleine-nachtmusik": {
        "title": "Eine kleine Nachtmusik (opening)", "composer": "Wolfgang Amadeus Mozart", "year": 1787, "key": "G major", "time": "4/4", "bpm": 120,
        "intro": "The first eight bars of the first movement: the rising G major fanfare, its answer on D, and the three trilled notes that climb to the top of the phrase before the scale runs back down to G. One sharp (F♯), plus a single C♯ in bar 7.",
        "tips": ["Bars 1–4 use only the notes of two chords, G major and D major — learn the shapes, not the letters.", "The rests in Mozart's original are written here as longer notes, so the MIDI keeps the same timing.", "Bar 8 is a straight G major scale down from the high G: one finger per note."],
    },
    "god-rest-ye-merry-gentlemen": {
        "title": "God Rest Ye Merry, Gentlemen", "composer": "Traditional (English)", "year": 1650, "year_text": "16th–17th century", "key": "E minor", "time": "4/4", "bpm": 104,
        "christmas": True,
        "intro": "Verse and refrain in E minor, one sharp. The two verse lines share the same melody, the refrain (“O tidings of comfort and joy”) climbs to the high E and comes back down to the tonic.",
        "tips": ["The verse starts and ends on E, the key note, and the chorus does too — use it as your anchor.", "Bars 3 and 7 are a plain scale from D up to G; the D is natural even though the key is E minor.", "The D♯ in the left-hand B major chords (bars 4, 8, 17) is the leading note that makes the minor key sound right."],
    },
    "in-the-hall-of-the-mountain-king": {
        "title": "In the Hall of the Mountain King", "composer": "Edvard Grieg", "year": 1875, "key": "A minor", "time": "4/4", "bpm": 100,
        "intro": "The creeping main theme from Peer Gynt, moved from B minor to A minor so there are no sharps in the key signature. Eight bars: the low statement twice, then the same tune an octave up.",
        "tips": ["Bar 1 is just the A minor scale from A up to E and back to C — the whole theme is built from it.", "D♯ in bars 2 and 8 is the only black key; it is answered by a plain D in bar 3.", "Start very slowly and quietly. The piece is famous for speeding up — but only after you can play it evenly."],
    },
    "nocturne-op9-no2": {
        "title": "Nocturne in E-flat, Op. 9 No. 2 (easy)", "composer": "Frédéric Chopin", "year": 1832, "key": "C major", "time": "12/8", "bpm": 50,
        "intro": "The opening melody of Chopin's most famous nocturne, moved from E♭ major to C major and reduced to its bare tune over one chord per bar. Written in 12/8 so the lilting rhythm reads as plain dotted quarters and eighths.",
        "tips": ["12/8 means four big beats per bar, each divided into three — count “1-and-a 2-and-a…”.", "The pickup G before bar 1 leads up to the high E: make that first E sing.", "Bar 3 has the piece's only black key, G♯, as a quick neighbour note under the A."],
    },
    "o-christmas-tree": {
        "title": "O Christmas Tree (O Tannenbaum)", "composer": "Traditional (German)", "year": 1824, "year_text": "16th century melody, 1824 lyrics", "key": "F major", "time": "3/4", "bpm": 100,
        "christmas": True,
        "intro": "The complete carol in F major, 3/4 time: the “O Christmas Tree” phrase, the middle section (“Not only green when summer's here”), and the return. One flat, B♭.",
        "tips": ["The dotted rhythm on “Christ-mas” (bars 1, 2, 11, 12) is the whole character of the song — long-short, not two equal notes.", "Bar 3 dips to a low E under the B♭ — the widest leap in the piece.", "The middle section (bars 5–10) sits higher, up to the D above the staff."],
    },
    "star-spangled-banner": {
        "title": "The Star-Spangled Banner", "composer": "John Stafford Smith", "year": 1773, "year_text": "1773 melody, 1814 words", "key": "C major", "time": "3/4", "bpm": 100,
        "intro": "The first half of the American national anthem in C major, 3/4 time, from “O say can you see” to “last gleaming”. The range is wide — from the low C to the E above the staff — which is exactly why it is famously hard to sing.",
        "tips": ["The pickup “O say” is a dotted rhythm: long G, short E.", "Bar 3's F♯ is the only black key; it leads up to the G in bar 4.", "Bars 5–6 are the peak: high E, then D, C, B on the way down. Do not rush the B."],
    },
    "spring-vivaldi": {
        "title": "Spring (The Four Seasons, opening)", "composer": "Antonio Vivaldi", "year": 1725, "key": "C major", "time": "4/4", "bpm": 100,
        "intro": "The opening ritornello of Spring from The Four Seasons, moved from E major to C major so there are no sharps. The same two-bar idea is stated four times, exactly as Vivaldi has the whole orchestra do.",
        "tips": ["Bars 1 and 2 are the entire piece — learn them and you have all eight bars.", "The quick D–C in bar 1 is a pair of sixteenths: think of it as one gesture, not two notes.", "Left hand alternates C and G chords; keep it light and short like a string orchestra playing detached."],
    },
    "wedding-march": {
        "title": "Wedding March (Mendelssohn)", "composer": "Felix Mendelssohn", "year": 1842, "key": "C major", "time": "4/4", "bpm": 112,
        "intro": "The main theme of the Wedding March from A Midsummer Night's Dream in C major: three rising statements of the “long, short-short, long” figure, a run back down, and the same again ending on the high C.",
        "tips": ["The rhythm is the same in bars 1, 2, 3, 5, 6, 7: quarter, two eighths, half. Get it once and repeat.", "Bar 4 is the only bar that moves quickly — a small leap up to E and a walk back down to D.", "All white keys; the left hand only alternates C and G chords."],
    },
    "hark-the-herald-angels-sing": {
        "title": "Hark! The Herald Angels Sing", "composer": "Felix Mendelssohn", "year": 1840, "year_text": "1840 melody, 1739 words", "key": "G major", "time": "4/4", "bpm": 108,
        "christmas": True,
        "intro": "The first two lines of the carol in G major, one sharp: “Hark! the herald angels sing, glory to the newborn King” and “Peace on earth and mercy mild, God and sinners reconciled”. Lines 1 and 3 share a melody.",
        "tips": ["Every F is F♯ — it appears in bars 1, 5 and 8.", "Bar 3 jumps to the high D and stays there for three notes: “Glo-ry to”.", "The last phrase walks straight down from A to D: A, G, F♯, E, D."],
    },
    "london-bridge": {
        "title": "London Bridge Is Falling Down", "composer": "Traditional (English)", "year": 1744, "year_text": "17th century", "key": "C major", "time": "4/4", "bpm": 108,
        "intro": "The nursery rhyme in C major, eight bars, all white keys, within the five notes from C to A. A good very first piece: the hand never has to move.",
        "tips": ["Bar 1 starts on G with a dotted rhythm: long G, short A, then G, F.", "Bars 3 and 4 are the two echoes, “falling down, falling down”: D-E-F, then E-F-G.", "The last two bars, “my fair lady”, are four slow notes: D, G, E, C."],
    },
    "yankee-doodle": {
        "title": "Yankee Doodle", "composer": "Traditional (American)", "year": 1755, "year_text": "18th century", "key": "C major", "time": "2/4", "bpm": 116,
        "intro": "Verse and chorus in C major, 2/4 time, all white keys. The verse sits on C, D, E, F; the chorus (“Yankee Doodle keep it up”) drops to the A below and swings between A and C.",
        "tips": ["2/4 time: two beats per bar, mostly in pairs of eighth notes — count “1 and 2 and”.", "Bar 7 dips to the low G and climbs back through A, B to C.", "The chorus starts on A (bar 9): the first note that is not part of the C–F run of the verse."],
    },
    "itsy-bitsy-spider": {
        "title": "Itsy Bitsy Spider", "composer": "Traditional (American)", "year": 1910, "year_text": "early 20th century", "key": "C major", "time": "6/8", "bpm": 100,
        "intro": "The children's song in C major and 6/8 time, from “The itsy bitsy spider climbed up the water spout” through “climbed up the spout again”. All white keys, from the G below middle C to the G above it.",
        "tips": ["6/8 has two big beats per bar with three eighth notes in each — a gentle swing, not a march.", "“Down came the rain” (bars 4–5) rises E, F, G: the highest point of the song.", "Bars 11–14 are bars 1–4 again — the ending is the beginning."],
    },
    "scarborough-fair": {
        "title": "Scarborough Fair", "composer": "Traditional (English)", "year": 1670, "year_text": "17th century", "key": "A minor (Dorian)", "time": "3/4", "bpm": 96,
        "intro": "The English folk ballad in A minor, 3/4 time — the old modal tune with its raised F♯ (the Dorian sixth) in bar 5. Fourteen bars: the question, “parsley, sage, rosemary and thyme”, and the answer.",
        "tips": ["The F♯ in bar 5 is what makes the tune sound ancient; play it as written, not F.", "“Parsley, sage” (bar 4) leaps up to the high A — the peak of the melody.", "The last line, “she once was a true love of mine”, ends back on the A you started from."],
    },
    "blue-danube": {
        "title": "The Blue Danube (waltz theme)", "composer": "Johann Strauss II", "year": 1866, "key": "D major", "time": "3/4", "bpm": 150,
        "intro": "The first waltz theme of An der schönen blauen Donau in D major, two sharps. The rising D–F♯–A, the held A, and the two high answering notes that everyone knows. Twelve bars, one chord per bar.",
        "tips": ["Waltz time: a strong first beat, two light ones. Count “ONE two three”.", "The high pairs in bars 3–4 and 7–8 jump up an octave and more — keep the wrist loose and aim for the A and F♯ above the staff.", "F♯ and C♯ are the two black keys; C♯ only appears in the left hand's A major chords."],
    },
    "beethoven-5th-symphony": {
        "title": "Symphony No. 5 (opening motif)", "composer": "Ludwig van Beethoven", "year": 1808, "key": "A minor", "time": "2/4", "bpm": 108,
        "intro": "The most famous four notes in music, moved from C minor to A minor: three short E's and a long C, three short D's and a long B, then the motif climbing through the sequence Beethoven uses to build the first theme.",
        "tips": ["The three pickup notes come before the bar line — count “1 and” and start on “and”.", "Every group is three quick notes and one long one: short-short-short-LONG.", "The G♯ appears only in the left-hand E major chords; the melody is all white keys."],
    },
    "prelude-in-c": {
        "title": "Prelude in C major, BWV 846", "composer": "Johann Sebastian Bach", "year": 1722, "key": "C major", "time": "4/4", "bpm": 66,
        "intro": "The first eight bars of the prelude that opens The Well-Tempered Clavier, written as one broken chord per bar. Each bar is eight eighth notes: the two lowest notes, then the top three played twice. All white keys except the F♯ in bar 6.",
        "tips": ["Every bar is one chord, spread out — read the chord symbol first, then the letters fall into place.", "The first two notes of each bar are the left hand's notes in Bach's original; we give them to the right hand so you can hear the whole pattern.", "Keep the eighth notes perfectly even; nothing should be accented."],
    },
    "morning-mood": {
        "title": "Morning Mood (Peer Gynt)", "composer": "Edvard Grieg", "year": 1875, "key": "C major", "time": "6/8", "bpm": 60,
        "intro": "The sunrise theme from Peer Gynt, moved from E major to C major so it is all white keys. Eight bars of the pentatonic motif — G, E, D, C, D, E — and its answer that rises to A.",
        "tips": ["The five notes C, D, E, G, A are the whole piece: it is a pentatonic tune, the same scale as the black keys.", "6/8 time, slow: each bar is two gentle beats of three notes.", "Bars 3, 6 and 7 are the answering shape that lifts to A — let it swell a little and then settle back."],
    },
}

# 곡별 해설·연주법 (애드센스 "가치 없는 콘텐츠" 판정 대응: 곡 페이지마다 글자표 말고 실제 읽을 글이 있어야 함). 마디 번호는 static/songs/<slug>.json의 bars 기준.
TEXT = {
    "jingle-bells": {
        "about": "James Lord Pierpont published this in 1857 under the title 'One Horse Open Sleigh', and it was not a Christmas song at all: it is about sleigh racing, and the original verses are closer to a drinking song than a carol. Both Medford, Massachusetts and Savannah, Georgia claim it was written there. The chorus became the part everyone knows, and in 1965 it was the first song ever broadcast from space, when the Gemini 6 crew played it on a smuggled harmonica and sleigh bells.",
        "play": "Bars 1–8 are the chorus. 'Jin-gle bells' is the same note three times (B B B), twice; 'jin-gle all the way' climbs B–D–G–A and lands back on B. 'Oh what fun' is four repeated C's, then 'it is to ride' steps down C–B–B–B–B. The line ends on 'in a one-horse open sleigh' (B A A B, then A up to D), and the second time through (bars 9–16) the ending changes to D D C A, resolving home to G. Bars 17–32 are the verse, 'Dashing through the snow': D B A G, three D's, D B A G again, then the phrase ends on E. Practice the chorus until the three repeated B's are perfectly even — that rhythm is the whole character of the song.",
    },
    "silent-night": {
        "about": "Franz Xaver Gruber wrote the melody on Christmas Eve 1818 for words by the priest Joseph Mohr, and the two of them sang it that night at St. Nicholas church in Oberndorf, Austria, with a guitar because (so the story goes) the organ was broken. It spread across Europe through travelling folk singers and is now sung in more than 300 languages. In 2011 UNESCO listed it as Austrian intangible cultural heritage. The 6/8 time gives it the slow rocking feel of a lullaby.",
        "play": "The opening 'Si-lent night' is G–A–G then a long E, and bar 2 repeats it exactly. 'All is calm' is D D B, 'all is bright' is C C G. Bars 5–8 ('round yon virgin, mother and child') are one phrase sung twice: A A C B A, then G A G E each time. The climb in bar 9, 'sleep in heavenly peace' (D D F D B), is the highest point; bar 10 answers with C and E, and bars 11–12 drift down C G E G F D to end on C. Count in two big beats per bar, not six small ones, and let every long note ring.",
    },
    "we-wish-you-a-merry-christmas": {
        "about": "An English carol from the West Country, probably 16th century, sung by carolers who expected something to eat or drink in return — hence the verse demanding 'figgy pudding'. Arthur Warrell's 1935 arrangement for the University of Bristol made it a concert standard. In 3/4 it swings like a waltz, and the melody is built on one four-bar idea that moves up a step each time it comes back.",
        "play": "Start on the pick-up D in bar 1. 'We wish you a merry Christmas' is G G A G F♯, then E E E; the same phrase repeats a step higher (A A B A G, then F♯ D D) and higher again (B B C B A, then G E D D). Bar 8 is the turn, E A F♯, resolving to G. 'Good tidings we bring' (bars 9–12) sits on long G's and F♯'s — the only place the tune stays still. The last line, 'we wish you a merry Christmas, and a happy new year', is the opening idea one more time, ending on the four D's and the E A F♯ turn.",
    },
    "deck-the-halls": {
        "about": "The tune is the Welsh 'Nos Galan' (New Year's Eve), a 16th-century melody for harp and voice; Mozart is said to have used it in a violin duet. The English 'Deck the halls' words were written by the Scottish musician Thomas Oliphant in 1862, and the 'fa-la-la' refrains are a leftover from the Welsh tradition of singing nonsense syllables while a harpist filled in the tune.",
        "play": "The first phrase is a plain scale down: G F E D C ('deck the halls with boughs of holly'), and every 'fa la la la la' is D E F D. Bars 1–4 and 5–8 are identical, so learn one line and you have half the piece. Line 3 (bars 9–12) is the new part: it starts the same way but rises D E F G A, then the only accidental — F♯ in bar 11 — appears on 'follow me in merry measure'. Line 4 (bars 13–16) is the first line again. Keep the scale even; beginners tend to rush the descending notes.",
    },
    "happy-birthday": {
        "about": "The melody is 'Good Morning to All', written by the Kentucky sisters Patty and Mildred Hill in 1893 for kindergarten classes. Nobody knows who first sang 'Happy birthday to you' to it, but by the 1910s it was everywhere. A publisher claimed copyright on the birthday words for decades, until a 2016 US court settlement put the song firmly in the public domain — it is, by many estimates, the most-sung song in English.",
        "play": "The two pick-up C's in bar 1 are 'Hap-py'. 'Birth-day to you' is D C F E. The second line starts the same but goes higher: D C G F. The third line, 'happy birthday dear …', jumps to the high C (bar 6) and then falls A F E D — that jump is the one difficult moment. The last line, 'happy birthday to you', is B♭ B♭ A F G F. B♭ is in the key signature (F major), so every B in the piece is a black key. Sing it while you play: the words carry the rhythm.",
    },
    "fur-elise": {
        "about": "Beethoven wrote this bagatelle in A minor around 1810, and it was only published in 1867, forty years after his death, by the scholar Ludwig Nohl, who claimed the manuscript was dedicated 'Für Elise'. Who Elise was is still argued about — the strongest candidate is Therese Malfatti, whom Beethoven proposed to. The opening E–D♯ trill figure is one of the most recognizable phrases in piano music.",
        "play": "The whole opening is built on the E–D♯ rocking figure. Bars 1–2: E D♯ E D♯ E B D C, then the left hand answers. Bar 3 is A C E A (an A minor arpeggio), bar 4 is B E G♯ B (E major, with the black-key G♯), bar 5 climbs C E E D♯ and the trill returns in bar 6. Bars 7–8 repeat bars 3–4 with a different ending (B E C B) and the piece lands on A. Play the E–D♯ pairs lightly and evenly — they should sound like a shimmer, not a hammer. Where Beethoven wrote a rest at the start of a bar, this beginner version holds the note so the letters line up with the beat.",
    },
    "twinkle-twinkle-little-star": {
        "about": "The tune is the French song 'Ah! vous dirai-je, maman', printed in 1761; Mozart wrote twelve variations on it (K. 265) around 1781. The words are Jane Taylor's poem 'The Star' from 1806. The same melody carries the alphabet song and 'Baa, Baa, Black Sheep', which is why it is usually the first thing a child learns on any instrument.",
        "play": "Bars 1–4: C C G G, A A G, F F E E, D D C — the first line, and also the last (bars 9–12). Bars 5–8 are the middle, 'up above the world so high': G G F F, E E D, sung twice. There are only six different notes, all white keys, and the right hand never needs to move its position. Play each pair of repeated notes with a small bounce and make the last note of every line ('star', 'are', 'high', 'sky') a little longer.",
    },
    "canon-in-d": {
        "about": "Johann Pachelbel wrote his Canon and Gigue for three violins and continuo in Germany around 1680–1700, and then the piece was forgotten for two centuries. A 1968 recording by Jean-François Paillard made it famous, and it has been at weddings ever since. The bass plays the same eight-chord pattern (D A Bm F♯m G D G A) fifty-four times while the violins enter one after another with the same melody — that is what 'canon' means.",
        "play": "This is the first violin's first entry over the famous bass. Bar 1 steps down F♯ E D C♯, bar 2 B A B C♯, bars 3–4 continue down D C♯ B A, G F♯ G E — a long descending scale broken into pairs. Bars 5–8 are the second phrase, mostly in thirds: D F♯ A G, F♯ D F♯ E, D B D A, G B A G, ending on F♯. The key is D major, so every F and C is sharp. Play it slowly and evenly; the piece is all about calm.",
    },
    "ode-to-joy": {
        "about": "The finale of Beethoven's Ninth Symphony (1824) sets Friedrich Schiller's 1785 poem 'An die Freude' for chorus and orchestra — the first time a major symphony used voices. The tune is deliberately simple, almost a hymn, so that a whole crowd could sing it. Since 1985 it has been the anthem of the European Union, and it was played when the Berlin Wall came down.",
        "play": "The melody uses only five notes, C to G, and moves almost entirely by step. Bars 1–4: E E F G, G F E D, C C D E, then E D D. Bars 5–8 are the same with the ending D C C. The middle (bars 9–12) is the only new material — D D E C, D E F E C, D E F E D, C D G — and bars 13–16 bring the first line back. If you can play a C major scale you can play this; the work is in keeping the rhythm perfectly steady.",
    },
    "amazing-grace": {
        "about": "John Newton, a former slave-ship captain turned clergyman, wrote the words in 1772 for a sermon in Olney, England. The tune we sing, 'New Britain', was joined to the words in William Walker's 1835 shape-note collection 'Southern Harmony'. The melody is pentatonic — five notes, no half steps — which is why it sounds right on bagpipes, and why it is so easy to play on the black keys alone.",
        "play": "Start on the pick-up D. 'A-ma-zing grace' is G B G, then B A; 'how sweet the sound' is G E, D D. Bars 6–8 repeat the opening and rise to the high D on 'me'. Bar 9 is the top of the tune, B D B, and bars 10–16 come back down: D B G, B A, G E, D D, G B G, B A, ending on G. Only five different notes appear (D E G A B). Play it slowly — it is a 3/4 hymn, one strong beat per bar.",
    },
    "moonlight-sonata": {
        "about": "Beethoven's Piano Sonata No. 14 in C♯ minor (1801) was published as 'Sonata quasi una fantasia'. The 'Moonlight' name came from the critic Ludwig Rellstab, who in 1832 compared the first movement to moonlight on Lake Lucerne. Beethoven marked the movement to be played with the damper pedal down throughout, and the steady triplets never stop from the first bar to the last.",
        "play": "This is the opening eight bars, moved to A minor so there are far fewer sharps, and written in 12/8 so the triplets are plain eighth notes. Every bar is the same three-note shape (low, middle, high) four times: bar 1 is E A C over and over, bar 3 changes to C F A (F major), bar 4 to B E G♯ (E major, with the black-key G♯). Bars 5–6 repeat bars 1–2, bar 7 mixes both chords, and the piece settles on A. Keep the left hand very quiet and let the pattern flow; the notes should sound like one long ripple.",
    },
    "minuet-in-g": {
        "about": "For two hundred years this minuet was credited to J. S. Bach, because it appears in the 1725 Notebook for Anna Magdalena Bach. In 1970 it was identified as the work of Christian Petzold, a Dresden organist. It is still the most-taught minuet in the world, and its melody became the 1965 pop hit 'A Lover's Concerto'. A minuet is a stately dance in three, so count 1-2-3 out loud.",
        "play": "Bar 1 leaps up from D to G and climbs A B C; bar 2 falls back to G. Bar 3 does the same from E (E C D E F♯) and bar 4 lands on three G's. Bars 5–8 are a longer descending line — C D C B A, B C B A G, then F♯ G A B G resolving to A. The second half (bars 9–16) is the first half again with a new ending (A B A G F♯ then G). The one sharp, F♯, comes from the key signature. Keep the quarter-then-eighths rhythm crisp; that is the dance.",
    },
    "greensleeves": {
        "about": "'Greensleeves' was registered in London in 1580 and Shakespeare mentions it twice in The Merry Wives of Windsor. The legend that Henry VIII wrote it for Anne Boleyn is almost certainly false — the style is Italian and later than his reign. The same tune carries the carol 'What Child Is This' (words by William Chatterton Dix, 1865). It is in A minor with a raised G♯ and F♯ in the old melodic-minor manner.",
        "play": "Pick-up A, then the verse: C D E F, E D B G, A B C A, A G♯ A B, G♯ E E A — the G♯ and F♯ are written where they happen. Bars 7–10 repeat that with a different ending (A G♯ F♯ G♯). The chorus (bars 11–21) starts high on 'Greensleeves was all my joy' — A A G, G G F, E D B G — and shares its second half with the verse. Count 6/8 as two swinging beats per bar. The G♯ is always a black key; everything else is white.",
    },
    "mary-had-a-little-lamb": {
        "about": "The poem was published by Sarah Josepha Hale in 1830 and, according to Hale's own account, is based on a real girl in Massachusetts whose lamb followed her to school. The tune is the one Lowell Mason fitted to it a few years later. In 1877 Thomas Edison recited the first verse into his new phonograph, making it the first words ever recorded and played back.",
        "play": "The first phrase is E D C D, E E E — the tune goes down two steps, back up, and repeats the E. 'Little lamb' is D D D, then E G G. Bars 5–8 are the same opening followed by E E E E, D D E D and a long C. The right hand never leaves the five notes C D E F G, so keep your thumb on C and one finger per note. This is a good first piece for reading letters: play each bar, say the letters out loud, then join them.",
    },
    "old-macdonald-had-a-farm": {
        "about": "An American cumulative song — each verse adds another animal and its sound — first printed in 1917 in 'Tommy's Tunes', a collection of songs sung by British soldiers, though older versions were sung in the United States long before. The 'E-I-E-I-O' refrain is what everyone remembers, and it is the part written out here.",
        "play": "'Old Mac-Don-ald had a farm' is C C C G, A A G — three repeated C's, a jump down to G, then A A G. 'E-I-E-I-O' is E E D D and a long C. Bars 5–8 repeat the whole phrase. The jump from C down to G in bar 1 is the only awkward moment; keep your hand still and reach down with the thumb. Once this phrase is easy, sing the animal verses over the same notes.",
    },
    "chopsticks": {
        "about": "Published in 1877 as 'The Celebrated Chop Waltz' by 'Arthur de Lulli' — actually the sixteen-year-old British girl Euphemia Allen. The name comes from her instruction to play it with the hands held sideways, chopping at the keys. Almost everyone learns it by ear from another child; this is the tune written down so you can see what your fingers were doing.",
        "play": "Only four notes: F F E E, D D C, over and over. Each two-bar unit is the same, so learn bars 1–2 and you have the piece. Bar 6 has an extra C (D D C C) and the last bar ends on a held C. The left hand alternates a C chord and a G chord — if you have a friend, let them play those while you play the tune, which is how the piece was meant to go. Speed is the only challenge; start slowly and add tempo once the rhythm never wobbles.",
    },
    "joy-to-the-world": {
        "about": "Isaac Watts wrote the words in 1719 as a paraphrase of Psalm 98, not as a Christmas song. The tune, 'Antioch', was arranged by Lowell Mason in 1848 and is usually said to borrow from Handel's Messiah, though only a few notes really match. The opening line is a complete major scale sung downwards, one note per syllable, which makes it one of the easiest carols to pick out on a piano.",
        "play": "Bars 1–2: 'Joy to the world, the Lord is come' is C B A G, F E D — the C major scale downwards. Bars 3–4 answer by going back up: C D E F, then a long G. Bars 5–6 sit on E E E E, E D C, and bars 7–8 are the opening scale again, this time finishing on the low C. There are no black keys. Practice the descending scale with the fingering 5-4-3-2-1 so the thumb lands on F.",
    },
    "the-first-noel": {
        "about": "An English carol from Cornwall, first printed in 1823 and again in William Sandys' 'Christmas Carols Ancient and Modern' in 1833. 'Noel' is the French word for Christmas, from the Latin 'natalis' (birth). The melody is unusual in that the verse and the refrain are built from the same short rising phrase, repeated at different heights.",
        "play": "The verse starts low and climbs: E D C D, E F G — then A B C, B A G. Bar 5 ('was to certain poor') is A B C B, and bar 6 rests on a long A. The refrain, 'Noel, Noel', is C B A G, A B C, and the last line, 'Born is the King of Israel', comes down G F E to finish. The whole piece is white keys in C major and moves by step, so the challenge is the range — it spans a full octave from C to C.",
    },
    "auld-lang-syne": {
        "about": "Robert Burns sent the words to the Scots Musical Museum in 1788, saying he had taken them down from an old man's singing; the title means 'old long since' — times gone by. The tune we use today was attached in 1799. It is sung at midnight on New Year's Eve across the English-speaking world, and in Japan the same melody ('Hotaru no Hikari') is played to tell customers a shop is closing.",
        "play": "In D major (F♯ and C♯). Bars 1–2: 'Should auld acquaintance be forgot' is D G G G, B A G A. Bars 3–4 rise to the high D and E on 'brought to mind'. Bars 5–8 come back down: E D B B, G A G A, B A G, then E E D G. The second half (bars 9–16) is the chorus, 'For auld lang syne, my dear', which is the same shape starting from the high E, with the top note G in bar 13. The tune is pentatonic (D E G A B), so there are no awkward half steps.",
    },
    "o-holy-night": {
        "about": "Adolphe Adam, a French opera composer, wrote 'Minuit, chrétiens' in 1847 to a poem by the wine merchant Placide Cappeau; John Sullivan Dwight's English version followed in 1855. It is often said to be the first piece of music broadcast by radio, played on the violin by Reginald Fessenden on Christmas Eve 1906. The full song climbs to a famous high note on 'O night divine'; this page gives the gentler opening verse.",
        "play": "'O holy night' is E E E G. 'The stars are brightly shining' is G A A F, then A up to C and back to G — the high C in bar 3 is the top of this phrase. 'It is the night' walks down G E D C. 'Of our dear Savior's birth' is E F A F, D and a long C. Everything is on white keys and within one octave. Play it slowly and legato, with a little swell towards the high C and a soft landing on the last C.",
    },
    "twelve-days-of-christmas": {
        "about": "The words were first printed in London around 1780 as a children's memory game, and the melody most people sing today was set down by the English composer Frederic Austin in 1909 — including the drawn-out “five gold rings”, which was his addition. The cumulative structure, each verse adding a gift and repeating all the earlier ones, is why the full song runs to twelve verses and several minutes. Our page gives only the first two verses, which contain every phrase the melody has.",
        "play": "“On the first day of Christmas” is C C, then F F F F E — a pickup of two C's and five notes on F with a small drop to E. “My true love gave to me” climbs F G A up to B♭ and comes back G A. “A partridge in a pear tree” is B♭ C D, the high point, then B♭ A F G F home to the key note. Verse two adds “two turtle doves” — C G A B♭ — before the same “and a partridge” tail. Play the left hand as one whole-bar chord under each phrase: F, C, B♭ and F.",
    },
    "ave-maria": {
        "about": "Schubert wrote this in 1825 as “Ellens dritter Gesang”, the third of Ellen's songs from Walter Scott's The Lady of the Lake, in a German translation; the Latin prayer text that is usually sung to it today was fitted on later. Its opening — a single long note followed by a gentle turn — has made it a fixture of weddings and funerals for two centuries. The original is in B♭ major with a flowing six-note accompaniment; we have moved it to C major and kept only the melody with one plain chord per bar.",
        "play": "Bar 1 is a G held for three full beats and then the turn A G. Bar 2 continues F E D E and rests on F, with G as the pickup into bar 3, which repeats the turn a step higher: A G F E D, then A B. Bar 4 is a long A. Bar 5 is the chromatic bar: G♯ E G F E G A B♭ — every note a step from the last. Bars 6 to 8 come home: G E F A, G G D, then B D and a long C. Keep the left hand very soft and let every right-hand note connect to the next.",
    },
    "eine-kleine-nachtmusik": {
        "about": "Mozart entered this serenade for strings into his own catalogue in August 1787, while he was writing Don Giovanni; the title just means “a little night music”. It was not published until 1827, after his death, and one of its original five movements is lost. The first movement's opening — a bold rising arpeggio in G, answered by the same shape in D — is probably the best known eight bars of classical music after Beethoven's Fifth.",
        "play": "Bar 1 alternates G and D, low and high: G D G D. Bar 2 runs up the G chord, G D G B, and lands on a long D. Bars 3 and 4 do the same on the D chord: C A C A, then C A F♯ A and a long D. Bar 5 starts the second idea: a long G, then G with a quick F♯–G under it; bar 6 does that on B, bar 7 on D with a C♯ turn. Bar 8 is a G major scale from the high G straight down to the G you started on. Play bars 1–4 short and crisp, 5–8 smooth.",
    },
    "god-rest-ye-merry-gentlemen": {
        "about": "One of the oldest carols still sung, printed in England by the 1760s and probably older; Dickens quotes its first line in A Christmas Carol when Scrooge chases a singer away with a ruler. The tune is in the minor, which is unusual for a carol and gives it a serious, marching character. The comma belongs after “merry”: the words mean “God keep you merry”, not “merry gentlemen”.",
        "play": "Verse: E then E B B A, G F♯ E, D E F♯ G, A B — up the scale and back down. The second line is the same. Refrain: “To save us all from Satan's power” is B C A B C D E, then B A; “when we were gone astray” is A G E F♯ G. “O tidings of comfort and joy” is G A B C B B A G F♯ E; the last “O tidings” rises G A B C D E and falls B A G F♯ E to finish on the key note. Left hand: E minor most of the way, G and B major chords where the melody leans on D and B.",
    },
    "in-the-hall-of-the-mountain-king": {
        "about": "Grieg wrote this in 1875 as incidental music for Ibsen's play Peer Gynt, for the scene in which Peer is chased by trolls in the hall of their king. Grieg disliked the piece and called it something that “reeks of cow dung”, but its slow creeping start and relentless acceleration have made it one of the most used pieces of music in film and television. The original is in B minor and begins in the lowest strings.",
        "play": "Bar 1 is the A minor scale climbing A B C D E, then C E. Bar 2 answers with D♯ B D♯ — the D♯ is the one black key. Bar 3 is the same shape on a plain D: D B D. Bar 4 repeats bar 1. Bar 5 is the tune an octave up on the chord: A E C E and a long A; bar 6 is G E G; bar 7 repeats bar 5; bar 8 closes with G♯ E and a held A. Start slow and soft, then, once the notes are secure, play it again a little faster and louder — that is what the orchestra does.",
    },
    "nocturne-op9-no2": {
        "about": "Chopin published the three Nocturnes Op. 9 in 1832, when he was 22 and newly arrived in Paris, and dedicated them to the pianist Marie Pleyel. The second, in E♭ major, became the most played of all his nocturnes: a slow song-like melody over a rocking left hand, decorated more each time it returns. The original is in E♭ with three flats and runs to 34 bars; our page gives the first melody only, moved to C major.",
        "play": "The pickup G leads to the high E in bar 1: E, then D E D, C held, then G. Bar 2 is C, then D C B, C held, G again. Bar 3 is A, B A G♯, A held, C — the G♯ is the only black key. Bar 4 falls B, A G F, E, G. Bars 5 to 8 repeat the shape with a different ending: bar 6 rises to E, bar 7 D, E D C, B then D, and bar 8 is a single long C for the whole bar. Play at about 50 beats a minute, one soft chord per bar in the left hand.",
    },
    "o-christmas-tree": {
        "about": "The melody is a German folk tune from the 16th century; the words “O Tannenbaum” were written by Ernst Anschütz, a Leipzig organist, in 1824, and turned an older love song about a fir tree into a Christmas carol. The same tune carries the state songs of Maryland, Iowa and Michigan and the socialist anthem “The Red Flag”. In 3/4 time, it is a gentle waltz rather than a march.",
        "play": "The pickup C leads to “O Christmas Tree”: F F F, G, then A A A, A, with the dotted rhythm on “Christ-mas”. “Thy leaves are so unchanging” is A G A B♭, E, G, F. The middle section starts on the high C: C, A D C, C C B♭, a long B♭, then B♭ G C, B♭ B♭ A and a long A. The pickup C brings back the opening phrase, and the last bar settles on F. Left hand: F and C chords throughout, one B♭ chord in bar 7.",
    },
    "star-spangled-banner": {
        "about": "The tune began as “To Anacreon in Heaven”, a London gentlemen's club song written by John Stafford Smith around 1773. Francis Scott Key set his poem about the bombardment of Fort McHenry to it in 1814, and it became the official United States national anthem in 1931. It spans an octave and a fifth, which is why it is so often sung badly; on the piano that range is no trouble at all.",
        "play": "“O say can you see” is the pickup G E, then C E G and the high C. “By the dawn's early light” is E D C, E F♯ G. “What so proudly we hailed” is G G, E D C, B. “At the twilight's last gleaming” is A B C C, G E and a long low C. Watch the two long notes: the high C in bar 2 and the G in bar 4 are each held two beats. The left hand plays C, D, G and C chords — the D chord under bar 3 is what gives the F♯ its lift.",
    },
    "spring-vivaldi": {
        "about": "Vivaldi published The Four Seasons in 1725 in Amsterdam as the first four of his twelve concertos Op. 8, each with a sonnet describing the scenes the music paints — birds, a thunderstorm, a sleeping goatherd. Spring's opening theme returns again and again between the solo episodes, which is what a ritornello is. The original is for solo violin and strings in E major with four sharps; we have moved it to C.",
        "play": "Bar 1 is C E E E, a quick D C, then G held and a short G. Bar 2 answers G F E, a quick F E, and a long D. Bars 3 and 4 are the same, ending on C instead. Bars 5 to 8 repeat all four bars, with the final bar simply G F E D and a long C. Keep the eighth notes short and springy — Vivaldi marks the theme Allegro and the strings play it detached — and let the left hand C and G chords bounce with it.",
    },
    "wedding-march": {
        "about": "Mendelssohn wrote the Wedding March in 1842 as part of his incidental music for Shakespeare's A Midsummer Night's Dream, seventeen years after his famous overture to the same play. It became the standard recessional at weddings after Queen Victoria's daughter chose it for her marriage to the Crown Prince of Prussia in 1858. The original is for full orchestra with trumpet fanfares in C major; this page gives its main tune.",
        "play": "Bar 1 is C, C C, and a long E; bar 2 is E, E E, and a long G; bar 3 is G, G G, and a long B — three steps up the chord with the same rhythm each time. Bar 4 leaps to E, then A G F down to D. Bars 5 to 7 repeat bars 1 to 3, and bar 8 lands on a whole-note high C. Play it strongly with a firm left hand: C chords under the C and E bars, G chords under the G and B bars.",
    },
    "hark-the-herald-angels-sing": {
        "about": "Charles Wesley wrote the words in 1739; the tune came a century later from a cantata Mendelssohn composed in 1840 to celebrate the 400th anniversary of Gutenberg's printing press. The English organist William Cummings joined the two in 1855, against Mendelssohn's stated wish that the music never be used for sacred words. It is now one of the three or four most sung carols in the English-speaking world.",
        "play": "“Hark the herald angels sing” is D, G G F♯ G, B B A — a pickup D, a dotted G–F♯, and the climb to B. “Glory to the newborn King” starts on the high D: D D D C, then B A and a long B. “Peace on earth and mercy mild” repeats the first line exactly. “God and sinners reconciled” is D A A G, then F♯ E and a long D home. The left hand is G and D chords; every F is sharp.",
    },
    "london-bridge": {
        "about": "The rhyme about the bridge that keeps falling down was printed in London in 1744 and is probably much older; the tune we sing was published in the 1870s. The bridge itself was rebuilt many times between the Roman period and the 1970s, when the 1831 stone bridge was sold to an American developer and re-erected in Arizona. The song is in nearly every beginner piano book because it needs only five notes.",
        "play": "“London Bridge is falling down” is G A G F, E F G — a long G, a short A, then down and back. “Falling down, falling down” is D E F, then E F G. The first line repeats. “My fair lady” is four slow notes: D, G, E and C. Play with the right thumb on C and one finger per note; the hand never moves. Left hand: C chords, with a G chord under each “falling down”.",
    },
    "yankee-doodle": {
        "about": "The tune was known in England in the 1750s and was first sung by British soldiers to mock the colonial troops during the French and Indian War; the Americans adopted it as their own and played it at the British surrender at Yorktown in 1781. The “macaroni” of the lyric was a slang word for a fashionable young man. It is the state song of Connecticut and one of the first tunes American children learn.",
        "play": "“Yankee Doodle went to town” is C C D E, C E D. “Riding on a pony” is C C D E, C B. “He stuck a feather in his cap” is G C C D E, F E D. “And called it macaroni” is C B G A, B C C. The chorus drops to A: “Yankee Doodle keep it up” is A B A G, A B C; “Yankee Doodle dandy” is G A G F, E G. “Mind the music and the step” repeats the A B A G phrase, and “with the girls be handy” is A G C B, D C C. Two beats a bar, brisk and cheerful.",
    },
    "itsy-bitsy-spider": {
        "about": "The spider that climbs the water spout, is washed out by the rain and climbs back up when the sun comes out first appeared in American print in 1910, as “Spider Song”, and was recorded as a children's song by 1920. It is usually sung with finger movements — thumb to index finger for the climbing spider, wiggling fingers for the rain — and it is sung in the same 6/8 lilt everywhere from Australia (as “Incy Wincy Spider”) to the United States.",
        "play": "The pickup G starts “The itsy bitsy spider”: C C C D, E E E. “Climbed up the water spout” is D C D E, C. “Down came the rain” is E F G; “and washed the spider out” is G F E F G E. “Out came the sun” is C C D E; “and dried up all the rain” is E D C D E C. Then G G lead back into “the itsy bitsy spider” and the last line, “climbed up the spout again”, D C D E C. Two gentle beats per bar; the left hand is C and G chords.",
    },
    "scarborough-fair": {
        "about": "A ballad about a lover who sets impossible tasks — a shirt with no seams, an acre of land between the sea and the shore — sung in Yorkshire since at least the 17th century; Scarborough's fair itself ran for 45 days every summer from 1253. The tune is in the Dorian mode, a minor scale with a raised sixth, which is why it sounds older than most folk songs. Simon & Garfunkel's 1966 recording is a copyrighted arrangement; the traditional melody on this page is public domain.",
        "play": "“Are you going to Scarborough Fair” is A A E, E B C B, A. “Parsley, sage” leaps up E G A; “rosemary and thyme” is G E F♯, D — the F♯ is the Dorian note that gives the tune its colour. “Remember me to one who lives there” is A A G, E E, D C B, A. “She once was a true love of mine” is A D C, B A G, E and a long A. One chord per bar in the left hand: mostly A minor, with C, G and D chords where the melody rests on those notes.",
    },
    "blue-danube": {
        "about": "Strauss wrote the waltz in 1866 for the Vienna Men's Choral Society, with a comic text, and it was a lukewarm success until it was played as an orchestral piece at the Paris World's Fair the next year. It has since become Austria's unofficial anthem, the traditional New Year's Day encore of the Vienna Philharmonic, and — thanks to Stanley Kubrick's 2001: A Space Odyssey — the sound of a space station turning. The full waltz is a chain of five waltzes; this is the first.",
        "play": "Bar 1 rises D F♯ A, and bar 2 holds the A. Bar 3 answers with two high A's, bar 4 with two high F♯'s. Bars 5 and 6 repeat the rise and the held A; this time the answer is two high A's and then two high G's, over the left hand's A major chord. Bars 9 to 12 rise once more and settle on a long D. Play the three-note rise smoothly, hold the long notes for their full value, and drop the two high notes in lightly, like the echo they are.",
    },
    "beethoven-5th-symphony": {
        "about": "Beethoven worked on his Fifth Symphony between 1804 and 1808 and conducted its premiere in Vienna in December 1808 at a four-hour concert in an unheated hall. The opening four-note motif — “fate knocking at the door”, according to his secretary, though Beethoven never said so — is built into almost every bar of the first movement. During the Second World War the BBC used it as a signature because its rhythm, short-short-short-long, is the letter V in Morse code.",
        "play": "Three quick E's lead to a long C. Three quick D's lead to a long B, held two bars. Then the motif climbs: E E E to C, F F F to D, G G G to E. Each group is exactly the same rhythm — three eighth notes and a held note — so once bar 1 is right the rest is copying. Keep the eighths short and identical; the whole point is that they never vary. The left hand plays A minor and E major chords, then D minor and C as the motif rises.",
    },
    "prelude-in-c": {
        "about": "Bach finished the first book of The Well-Tempered Clavier in 1722, a set of preludes and fugues in all 24 keys to show that a keyboard tuned in the new “well-tempered” way could play in any of them. The Prelude in C that opens it has no melody at all: it is a chain of broken chords, one per bar, whose slowly shifting harmonies do all the work. Gounod later wrote his own Ave Maria as a tune to sit on top of it.",
        "play": "Each bar is one chord spread from bottom to top: the two lowest notes once, then the top three notes twice. Bar 1 is C E G C E. Bar 2 is C D A D F — the same C, then D minor above it. Bar 3 is B D G D F, a G seventh. Bar 4 returns to C. Bar 5 is C E A E A, bar 6 C D F♯ A D — the only black key — bar 7 B D G D G, and bar 8 B C E G C. Play every note evenly and softly, and let the chord symbols above the staff tell you where the harmony is going.",
    },
    "morning-mood": {
        "about": "The sunrise music from Peer Gynt, written by Grieg in 1875 for Ibsen's play — where, despite its Norwegian sound, it accompanies a dawn in the Moroccan desert. Grieg later extracted it as the first movement of his Peer Gynt Suite No. 1, and it has been used for every kind of sunrise since. The theme is pentatonic (five notes only) and passes between flute and oboe in the original; the key there is E major.",
        "play": "The motif is G E D C D E: down the scale from G to C and back up two notes. Bars 1 and 2 play it twice. Bar 3 lifts the answer: G E G A E A. Bar 4 returns to the motif, bar 5 repeats it, and bars 6 and 7 give the lifted answer twice. Bar 8 starts the motif once more and settles on a long C. Play it as slowly as you can bear, with the left-hand chords (C and F) sounding for the whole bar, and a small swell each time the line rises to A.",
    },
}
for _k, _v in TEXT.items():
    SONGS[_k].update(_v)
