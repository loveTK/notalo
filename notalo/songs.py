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
}
for _k, _v in TEXT.items():
    SONGS[_k].update(_v)
