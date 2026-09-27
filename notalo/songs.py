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
    "rhapsody-in-blue": {
        "title": "Rhapsody in Blue (opening, simplified)", "composer": "George Gershwin", "year": 1924, "key": "B\u266d major", "time": "4/4", "bpm": 100,
        "intro": "Gershwin's famous 1924 concert work opens with a clarinet gliding up through a scale into a jazzy blue-note riff. This is not a note-for-note transcription of that orchestral opening (it's written for a full orchestra, not solo piano) \u2014 it's a simplified, easy-piano piece inspired by that gesture: a rising-then-falling scale for the glide, then a short syncopated blues motif in the same key, B\u266d major.",
        "tips": ["Bars 1\u20132 are just the B\u266d major scale going up an octave, then straight back down \u2014 no new notes to learn.", "E is always E\u266d and B is always B\u266d here (the key signature) \u2014 both are black keys.", "Bars 3 and 5 are the exact same four notes \u2014 learn the motif once, play it twice."],
    },
}
