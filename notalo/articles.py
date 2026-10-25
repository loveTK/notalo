"""/learn/<slug> 글. 애드센스 'low value content' 대응: 도구 사이트가 아니라 '글이 있는 사이트'로 보이게, 우리 경험(측정치·파이프라인·편곡 작업)에서만 나올 수 있는 내용으로.
각 글: title, desc(meta), date, image(og), body(html). 바이라인·구조화 데이터는 app.py가 붙임. 새 글은 몇 주 간격으로 추가(한 번에 10배로 늘리면 '승인용 사이트'로 봄)."""

ARTICLES = {
 "how-to-photograph-sheet-music": {
  "title": "How to photograph sheet music so a scanner can read it",
  "desc": "Seven things that decide whether a phone photo of sheet music converts cleanly: light, angle, distance, shadows, page curl, resolution and file type. From the failures we see every day.",
  "date": "2026-10-10", "image": "/hero/sample_en.webp",
  "body": """
<p class="lead">Most conversions that go wrong on Notalo go wrong before the upload. The page was photographed at an angle, half of it in shadow, or so far away that a quarter note is eleven pixels tall. This is what we have learned from the pages people send us when a result looks bad, and what to do instead.</p>

<h2>1. Shoot straight down, not from a chair</h2>
<p>A page photographed from where you sit is a trapezoid: the top edge is shorter than the bottom, and the five staff lines, which should be parallel, converge. Our first processing step straightens the page by measuring the dominant line angle, but it corrects rotation, not perspective. A tilt of a few degrees is fine. A photo taken from 30 cm above the music stand, looking down at 45°, is not: the staff spacing changes from one side of the page to the other and the note detector, which expects every staff on the page to have roughly the same spacing, starts missing noteheads on the far side.</p>
<p>Put the page flat on a table, hold the phone directly above it, and look at the edges of the paper on screen. If they are parallel to the edges of the screen, you are done.</p>

<h2>2. One light source, from the side, no flash</h2>
<p>The flash on a phone is a point light right next to the lens. On glossy paper it makes a bright oval in the middle of the page where the ink disappears, and on matte paper it leaves the corners dark. Both are a problem because the second processing step turns the photo into pure black and white, and it has to pick a threshold that works across the whole page. A bright patch becomes white (notes vanish); a dark corner becomes black (staff lines merge).</p>
<p>Daylight from a window to one side is ideal. A desk lamp off to the side is nearly as good. Overhead room light is acceptable if you keep your own shadow off the page, which usually means standing so the light is in front of you, not behind.</p>

<h2>3. Fill the frame with the page</h2>
<p>Resolution is the quiet killer. A phone takes a 12-megapixel photo, but if the page is a third of the frame, the music is 4 megapixels, and a staff that is 8 mm tall on paper ends up about 60 pixels tall in the image. The detector was trained on scores where the space between staff lines is 12 to 20 pixels, and it degrades below about 10. In our test set, the same page photographed close (staff spacing 18 px) reads 99% of the pitches; photographed from twice the distance (9 px) it reads 86%, and the note lengths get worse faster than the pitches, because a dot after a note is only two or three pixels across.</p>
<p>Get close enough that the page fills the screen with a small margin. If a page has very small print, photograph the top half and the bottom half separately and upload them as two images.</p>

<h2>4. Flatten the page</h2>
<p>A book that will not stay open produces a curved page, and a curved page gives curved staff lines. We handle gentle curvature, but a strong curl near the spine does two things: the lines bend out of the horizontal window the staff finder looks in, and the noteheads near the spine are compressed sideways and look like something else. Hold the book down with a hand on each side outside the music, or photocopy the page first; a copy lies flat.</p>

<h2>5. Avoid shadows from your hand or phone</h2>
<p>The most common artifact we see is a soft dark band across the page from the phone's own shadow. It is wide enough to shift the black-and-white threshold inside it, which turns thin staff lines into thick ones. Stand so the light comes over your shoulder from the opposite side of the phone, or simply photograph in brighter light so the shadow is faint.</p>

<h2>6. PDF beats photo, and a scan beats both</h2>
<p>If the music came from a PDF, upload the PDF, not a screenshot of it. A PDF exported from notation software is rendered by us at 200 dots per inch into a perfectly aligned, perfectly lit image, and on those pages our detector finds every pitch on our test set. A scan from a flatbed scanner at 300 dpi is nearly as good. A photo is always a step down, which is fine for a clean page under good light, and a struggle for a dim, tilted one.</p>
<p>If the PDF is itself a scan of a printed book, it will behave like a scan, not like a rendered file. That is usually still good; the one thing that catches us is a scan that was made slightly rotated, which we straighten automatically.</p>

<h2>7. Crop the page, not the music</h2>
<p>Cropping away the table, the music stand and the neighbouring page helps, because anything with long horizontal lines (a table edge, a ruled notebook) can be mistaken for a staff. Cropping into the music hurts: a staff that is cut off at the left edge loses its clef, and without a clef we assume treble, which gives the left hand the wrong letters by a sixth. Leave a finger's width of white around the music.</p>

<h2>What we do with the photo</h2>
<p>For the curious: the image is converted to greyscale, the skew angle is measured from the staff lines and corrected, uneven lighting is removed by subtracting a blurred copy of the page from itself, and the result is thresholded to black and white. The staff lines are found from runs of black pixels of consistent length and spacing. Then a neural network looks at the page and marks noteheads, clefs, sharps, flats and naturals. The rest is bookkeeping: which staff each notehead is on, how far from the bottom line, which clef and key signature apply, and whether an accidental earlier in the bar changes it.</p>
<p>Every step before the neural network is there to make a photo look as much like a rendered PDF as possible. The better the photo already looks, the less those steps have to do, and the fewer mistakes they make. That is the whole reason for this list.</p>

<h2>A quick checklist</h2>
<ul>
  <li>Page flat, phone directly above, paper edges parallel to the screen.</li>
  <li>Light from a window or lamp to the side; flash off; no shadow across the page.</li>
  <li>Page fills the frame. Small print: two photos, top and bottom.</li>
  <li>Book held open or photocopied; no curl at the spine.</li>
  <li>Leave white margin around the music; crop away everything else.</li>
  <li>If you have the PDF, send the PDF.</li>
</ul>
"""},

 "how-optical-music-recognition-works": {
  "title": "How optical music recognition works, and why photos are harder than PDFs",
  "desc": "What happens between uploading a page of sheet music and getting the notes back: staff finding, symbol detection, pitch rules, and where the classic engines like Audiveris and newer neural models differ.",
  "date": "2026-10-10", "image": "/guide/treble.png",
  "body": """
<p class="lead">Optical music recognition, OMR, is to sheet music what OCR is to text: software that looks at a picture of a page and works out what is written on it. It has existed since the 1960s and it is still not solved, for reasons that become obvious once you try to build one. This is how Notalo's works, how the established tools work, and where each of them fails.</p>

<h2>Why it is harder than reading text</h2>
<p>Printed text is a line of separate symbols, each of which means one thing. Music is two-dimensional: a notehead's meaning depends on its vertical position, on a clef that may be several centimetres to the left, on a key signature at the start of the line, on an accidental earlier in the same bar, and on a stem, flag, beam and dot that may each be attached to it or to a neighbour. And everything sits on top of five lines that cut through every symbol. An OCR engine can assume the letters are separated by white space. An OMR engine cannot assume anything is separated from anything.</p>

<h2>The classic pipeline</h2>
<p>Almost every OMR system, from the 1990s commercial scanners to the open-source Audiveris engine that MuseScore's PDF import is built on, does the same five things in order.</p>
<ol>
  <li><strong>Binarize.</strong> Turn the image into pure black and white. On a rendered PDF this is trivial. On a photo it means first correcting the lighting, because a single global threshold will lose the notes in a bright patch and merge the lines in a dark one.</li>
  <li><strong>Find and remove the staff lines.</strong> Staff lines are long, thin, horizontal, evenly spaced, and in groups of five. Finding them is a matter of looking for rows with many black pixels in a row at a regular vertical interval. Removing them is harder: a line passes through every notehead, and taking it out must not cut the notehead in half. Audiveris removes the lines and then repairs the symbols; Notalo leaves the lines in and lets the detector learn to see through them.</li>
  <li><strong>Segment and classify symbols.</strong> With the lines gone, what remains is blobs of ink. Each blob, or group of blobs, is classified: notehead, clef, sharp, rest, and so on. Audiveris uses a small neural network trained on glyph shapes for this; older systems used template matching. Notalo skips the segmentation step and uses an object detector (YOLO) that proposes boxes and classes directly on the page image, trained on DeepScoresV2, a public dataset of about 250,000 annotated symbols on engraved scores.</li>
  <li><strong>Assemble and interpret.</strong> Noteheads are attached to stems, stems to beams and flags, dots to the note on their left. Then the music rules apply: a notehead's distance from the bottom staff line plus the clef gives a letter; the key signature and any accidental earlier in the bar adjust it. Audiveris does this with a graph of candidate interpretations and prunes the ones that contradict each other, so a bar that adds up to five beats in 4/4 time loses its least confident note. Notalo's rules are simpler and never delete a detection, which is why it occasionally shows a note that is not there, but never silently drops one.</li>
  <li><strong>Output.</strong> Audiveris writes MusicXML, which notation programs can open and edit. Notalo writes the letters back onto the original image and makes a MIDI file from the same notes.</li>
</ol>

<h2>Where the two approaches differ</h2>
<p>The classic pipeline is excellent on clean engraved music and terrible on everything else, because every stage assumes the previous stage was perfect. A staff-removal step that leaves fragments of line through a notehead sends a mangled blob to the classifier, which calls it a rest, which breaks the bar count. On a photo with uneven lighting, the fragments are everywhere.</p>
<p>A learned detector is more forgiving. It has seen thousands of noteheads with lines through them and classifies them anyway, and it does not care much about a mild blur. Its weakness is the opposite one: it has no model of music. It will happily find a notehead where a dot of dirt is, because nothing tells it that a bar cannot have nine beats. The sensible design, which both camps are moving towards, is a learned front end with a rule-based back end that checks the result. Notalo's back end is still thin: it reads pitches, note heads, flags, beams and dots, and it does not yet read rests, ties or tuplets. That is why the letters are almost always right and the MIDI timing sometimes is not.</p>

<h2>The numbers</h2>
<p>We keep a test set of our own rendered scores, with every notehead's true pitch and length recorded, and run the detector on them in three versions: the clean rendering, a copy rotated by a few degrees, and a copy degraded to look like a phone photo (blur, noise, uneven light). On the clean pages the pitches are all correct and the note lengths are right 97% of the time. On the skewed pages the same, once the page is straightened. On the photo-like pages the pitches are still 95 to 99% right, but the note lengths drop to about 60%, almost entirely because the augmentation dot after a dotted note merges with a staff line and is lost. That one failure is the next thing we are fixing, and it is a good example of how OMR fails: not on the big symbols but on a three-pixel dot that changes a note's length by half.</p>

<h2>What is hard for everyone</h2>
<ul>
  <li><strong>Handwritten music.</strong> No two people draw a quarter note the same way. Engines trained on engraved music fall to 50 to 70% on handwriting. There are handwritten datasets (MUSCIMA++ is the best known) but far less data than for print.</li>
  <li><strong>Dense piano music.</strong> Chords of four notes a second apart, cross-staff beams, three voices on one staff. The symbols touch and overlap, and the assembly step has to guess.</li>
  <li><strong>Lyrics and text.</strong> Letters under the staff look like nothing in the symbol set and can confuse a detector that was not trained on them. Notalo masks the region below each staff before detecting, which is why lyrics do not become noteheads, and also why we cannot read them.</li>
  <li><strong>Old editions.</strong> Nineteenth-century engraving has different notehead shapes, different clef designs and ink bleed. Everything degrades a little.</li>
</ul>

<h2>Which tool for which job</h2>
<p>If you want an editable score from a clean PDF, Audiveris (free, open source) followed by a notation editor is the right tool, and the commercial scanners (PhotoScore, PlayScore, ScanScore) do the same with less fiddling. If you want to play the page today and the page is a photo, a learned detector that labels the image is more useful than a MusicXML file with errors you have to find in an editor. That is the gap Notalo is built for, and it is why we output letters on the picture rather than a file.</p>
"""},

 "sheet-music-to-midi-what-to-expect": {
  "title": "Sheet music to MIDI: what the file can tell you and what it cannot",
  "desc": "A MIDI file made from a page of sheet music carries pitches and lengths, not tempo, dynamics or feel. How to read one, what breaks in conversion, and how to use it to practise.",
  "date": "2026-10-10", "image": "/songs/fur-elise.png",
  "body": """
<p class="lead">Every demo song on this site, and every page you convert, comes with a MIDI file. People expect it to sound like a recording and are surprised when it sounds like a music box. That is what MIDI is. Here is what is actually in the file, what gets lost on the way from paper to file, and the three ways it is genuinely useful for learning a piece.</p>

<h2>What a MIDI file is</h2>
<p>A MIDI file is not audio. It is a list of instructions: at time 0, press key 60 (middle C) at this loudness; at time 480, release it; at time 480, press key 62. A player program reads the list and makes the sounds with whatever instrument it has, which is why the same file sounds like a grand piano in one app and a toy in another. The file is tiny, a few kilobytes for a whole piece, and it can be slowed down without changing the pitch, which is the property that makes it useful for practice.</p>

<h2>What gets into the file from the page</h2>
<p>When Notalo converts a page, each detected notehead becomes one note in the file. Its pitch comes from the staff position, the clef and the key signature. Its start time comes from its horizontal position in the bar: notes are sorted left to right, and each starts when the previous one in the same hand ends. Its length comes from the notehead shape (hollow or filled), the flags or beams on its stem, and a dot if there is one. The right hand goes on one track, the left on another, so you can mute either in most players.</p>
<p>Tempo is whatever you ask for; the page does not say. The demo songs are set to a sensible speed for each piece and your conversions default to 90 beats per minute. Loudness is the same for every note. There is no pedal, no accent, no ritardando at the end of the phrase.</p>

<h2>What gets lost</h2>
<ul>
  <li><strong>Rests.</strong> We do not yet detect rests, so a rest is filled by the previous note being held longer. The timing of everything after it stays right, because note lengths are measured from the page positions; only the silence is missing.</li>
  <li><strong>Ties.</strong> A tie joins two notes into one longer note. We play them as two notes, re-struck. On a piano this is audible; on a sustained instrument it is the difference between a held note and a repeated one.</li>
  <li><strong>Triplets and other tuplets.</strong> Three notes in the time of two are written with a small 3 over the beam. We do not read the 3 and play them as ordinary eighths, so a triplet bar runs long. Classical pieces with triplet accompaniments (the Moonlight Sonata is the famous case) are the ones where this matters; our easy version of it is written in 12/8 precisely to avoid it.</li>
  <li><strong>Dots on photos.</strong> On a clean PDF we read the dot after a dotted note almost every time. On a phone photo the dot often merges with a staff line and the note plays at two-thirds of its length. Pitches are unaffected.</li>
  <li><strong>Grace notes, trills, ornaments.</strong> Not read. A trill plays as its main note.</li>
  <li><strong>Repeat signs, first and second endings, D.C. al Fine.</strong> Not read. The file plays the page once, top to bottom.</li>
</ul>
<p>So a converted MIDI file is a reliable record of which notes are on the page in which order, a good record of their relative lengths on clean input, and a poor record of silence, articulation and form. That is a lot more useful than it sounds, as long as you know which parts to trust.</p>

<h2>How to use it to learn a piece</h2>
<h3>1. Hear the tune before you can play it</h3>
<p>Most beginners' mistakes are not wrong notes but wrong rhythms: holding a half note for one beat, rushing through a dotted figure. Hearing the file once, even at music-box quality, fixes the rhythm in your ear before your hands get a vote. Play it at the written tempo once, then at half speed while you follow the letters on the image.</p>
<h3>2. Loop the bar you cannot play</h3>
<p>Every decent MIDI player can loop a region. Loop the two hard bars at 60% speed and play along until you can do it three times running, then move the loop forward a bar. This is what a teacher does with a metronome and it works better with a sounding reference than with clicks.</p>
<h3>3. Mute one hand</h3>
<p>Because the two hands are on separate tracks, you can mute the right hand and play it yourself against the file's left hand, which is the hardest part of piano music to self-supervise: you can hear immediately when your hand falls behind the accompaniment. Then swap.</p>

<h2>Players that do this</h2>
<p>On a phone, any free MIDI player with a tempo slider will do; on a computer, MuseScore opens a MIDI file as a score (expect it to guess the note lengths and sometimes guess wrong), and most digital audio workstations open it as a piano roll. If the player shows a piano roll, you get a bonus: the notes are drawn as bars on a keyboard, which is a third way of seeing the same music next to the staff and the letters.</p>

<h2>A note on the demo songs</h2>
<p>The MIDI files for the demo songs are made the same way as your conversions: we render the score, run the detector on it and build the file from what it found, not from the score's own data. We do that on purpose, so that the files are an honest sample of what the converter produces on clean input. Where a demo file has a wrong length, that is a detector error, and the test set that catches it is public in the repository.</p>
"""},

 "learning-with-letter-notes-four-week-plan": {
  "title": "A four-week plan for learning piano with letter notes, and then taking the letters away",
  "desc": "Letter notes get you playing on day one; the risk is never moving past them. A week-by-week plan using the free demo songs on this site, with the letters fading out as the staff becomes familiar.",
  "date": "2026-10-10", "image": "/songs/twinkle-twinkle-little-star.png",
  "body": """
<p class="lead">Teachers are divided on letter notes. The case against is real: a student who reads letters never reads the staff. The case for is also real: a student who cannot play anything for a month quits. The way through is to use the letters as scaffolding and remove them on a schedule. This is the schedule we suggest, using songs that are on this site and free.</p>

<h2>Before you start</h2>
<p>Find middle C on your keyboard: the C nearest the middle, just left of the pair of black keys closest to the centre. Everything in weeks one and two sits within an octave of it. Put the right thumb on middle C and let the fingers fall on D, E, F, G. That five-finger position is the whole hand for the first week. Sit so your forearms are level with the keys; a chair that is too low makes everything harder.</p>

<h2>Week 1: five fingers, letters on</h2>
<p>Pieces: <a href="/letter-notes/mary-had-a-little-lamb">Mary Had a Little Lamb</a>, <a href="/letter-notes/london-bridge">London Bridge</a>, <a href="/letter-notes/twinkle-twinkle-little-star">Twinkle Twinkle Little Star</a>. All three stay inside C to G or C to A in the right hand and have one chord per bar in the left.</p>
<p>Right hand only for the first three days, reading the red letters. Say the letter out loud as you press the key; it feels silly and it is the single most effective thing in this plan, because it links the sound, the symbol and the name in one moment. Ten minutes a day, each song until you can play it twice without stopping. On day four add the left hand chords, held for the whole bar, reading the blue letters from the bottom up. By day seven you should have one song with both hands at a slow, steady speed.</p>
<p>What you are learning without noticing: that the notes on the staff go up when the letters go up, that a filled notehead is shorter than a hollow one, and where C, D, E, F and G sit on the treble staff.</p>

<h2>Week 2: a wider hand, first black key</h2>
<p>Pieces: <a href="/letter-notes/ode-to-joy">Ode to Joy</a>, <a href="/letter-notes/jingle-bells">Jingle Bells</a>, <a href="/letter-notes/happy-birthday">Happy Birthday</a>.</p>
<p>Ode to Joy adds nothing new but speed and length. Jingle Bells is in G major: the key signature has one sharp and every F is F♯, a black key. Notice how the letters show it, F♯, and find it on the keyboard: the black key just right of F. Happy Birthday has a wide leap in the third phrase; that leap is the first time your hand has to move out of its position and come back.</p>
<p>This week, start the fade: for the one song you know best from week one, cover the red letters with a strip of paper and play from the staff. You will be slower. When you get stuck, lift the paper, look, cover it again. Do this for two minutes at the end of each practice.</p>

<h2>Week 3: both clefs for real</h2>
<p>Pieces: <a href="/letter-notes/amazing-grace">Amazing Grace</a>, <a href="/letter-notes/minuet-in-g">Minuet in G</a>, <a href="/letter-notes/silent-night">Silent Night</a>.</p>
<p>The Minuet is the first piece where the left hand does more than hold a chord. Read the bass clef notes from the <a href="/bass-clef-notes">bass clef chart</a>: the lines are G B D F A, and the shortcut from treble is that every position is two letters lower. Silent Night and Amazing Grace are in 6/8 and 3/4 respectively: count them out loud, "one two three", because the counting is the piece.</p>
<p>Fade: now cover the letters on everything from weeks one and two. Keep them on the new pieces. Play one old piece from the plain staff every day, before learning anything new. This is the week most people feel the staff "click": the letters are still there in your head when you look at the note.</p>

<h2>Week 4: pieces that sound like music</h2>
<p>Pieces: <a href="/letter-notes/fur-elise">Für Elise</a> (opening), <a href="/letter-notes/canon-in-d">Canon in D</a>, <a href="/letter-notes/greensleeves">Greensleeves</a>, or any carol from the <a href="/christmas-piano-songs-with-letters">Christmas page</a> if the season is right.</p>
<p>These are the pieces people actually want to play, simplified to a level that week-three hands can manage. Für Elise is in 3/8 with sixteenth notes: it will feel fast; it is not, if you count in three. Canon in D has two sharps. Greensleeves has accidentals written in the bars where they happen, which is the last reading skill in this plan.</p>
<p>Fade: learn one of these with the letters covered from the start, uncovering only to check. If that works, you no longer need the letters for pieces at this level. Keep using them for harder music, which is what they are for: a piece beyond your reading level that you want to play anyway. That is also what the converter on the front page is for.</p>

<h2>Three rules that make the plan work</h2>
<ul>
  <li><strong>Slow and correct beats fast and wrong.</strong> Set the MIDI file to 60% and play with it. Speed arrives on its own once the notes are secure; mistakes practised fast become permanent.</li>
  <li><strong>Ten minutes every day beats an hour on Sunday.</strong> Reading is a recognition skill, like faces. It is built by frequent short exposure.</li>
  <li><strong>Say the letters.</strong> Out loud, every time, until week three. Then say them silently. Then stop. The order matters.</li>
</ul>

<h2>After week four</h2>
<p>You can read both staves slowly, you know what sharps and flats do, and you have eight or ten short pieces. The next step is a method book or a teacher, and the one thing to carry over from this plan is the fade: whatever you learn with help, learn again without it. The letters were never the point. Playing was.</p>
"""},

 "key-signatures-by-example": {
  "title": "Key signatures explained with real songs: one sharp, one flat, two sharps",
  "desc": "What the sharps and flats after the clef mean, how to read them in seconds, and which demo songs on this site are in which key, so you can hear the difference instead of memorizing a table.",
  "date": "2026-10-10", "image": "/songs/jingle-bells.png",
  "body": """
<p class="lead">The cluster of sharps or flats between the clef and the time signature is the key signature. It says: every note with this letter name is sharp (or flat) for the whole piece, in every octave, unless a natural sign says otherwise in a particular bar. Beginners learn it as a table. It is easier to learn it from songs you already know, so here it is by example, using the arrangements on this site.</p>

<h2>No sharps or flats: C major and A minor</h2>
<p>Nothing after the clef means all white keys. Most of the first songs anyone learns are written here on purpose: <a href="/letter-notes/mary-had-a-little-lamb">Mary Had a Little Lamb</a>, <a href="/letter-notes/twinkle-twinkle-little-star">Twinkle Twinkle</a>, <a href="/letter-notes/ode-to-joy">Ode to Joy</a>, <a href="/letter-notes/london-bridge">London Bridge</a>, <a href="/letter-notes/yankee-doodle">Yankee Doodle</a>, <a href="/letter-notes/joy-to-the-world">Joy to the World</a>, and Bach's <a href="/letter-notes/prelude-in-c">Prelude in C</a>, which is a tour of every chord you can build on white keys.</p>
<p>The same empty signature also means A minor, the "relative minor" of C: the same seven notes, with A treated as home instead of C. <a href="/letter-notes/greensleeves">Greensleeves</a>, <a href="/letter-notes/scarborough-fair">Scarborough Fair</a> and our easy <a href="/letter-notes/in-the-hall-of-the-mountain-king">Mountain King</a> are in A minor. You can tell a minor piece from a major one with the same signature by where it ends: on A, not on C, and by the G♯ that minor pieces write into the bars as an accidental, because the leading note in A minor is G♯ and the key signature cannot show it. Count the G♯ signs in Greensleeves; that is A minor announcing itself.</p>

<h2>One sharp: G major and E minor</h2>
<p>One sharp sits on the top line of the treble staff, the F line. It means every F is F♯. <a href="/letter-notes/jingle-bells">Jingle Bells</a>, the <a href="/letter-notes/minuet-in-g">Minuet in G</a>, <a href="/letter-notes/hark-the-herald-angels-sing">Hark! The Herald Angels Sing</a> and <a href="/letter-notes/eine-kleine-nachtmusik">Eine kleine Nachtmusik</a> are all in G major. On the keyboard: the black key just to the right of every F. In our labeled scores the letter under the note says F♯, so you cannot forget it, but notice that the sharp sign itself is not printed next to the note. The key signature already said it.</p>
<p>One sharp is also E minor. <a href="/letter-notes/god-rest-ye-merry-gentlemen">God Rest Ye Merry, Gentlemen</a> is the example: it starts and ends on E, and the left hand's B major chords contain a D♯ that the signature does not show, written in as an accidental, the same trick as the G♯ in A minor.</p>

<h2>Two sharps: D major</h2>
<p>F♯ and C♯. <a href="/letter-notes/canon-in-d">Canon in D</a> and the <a href="/letter-notes/blue-danube">Blue Danube</a> are in D major. Sharps are always added in the same order, F C G D A E B, so a two-sharp signature is always F and C, never any other pair. If you remember one thing from this page, remember that order: the last sharp in the signature is one letter below the key. Last sharp C♯, key is D. Last sharp F♯, key is G.</p>

<h2>One flat: F major</h2>
<p>A single flat on the middle line of the treble staff, the B line. Every B is B♭, the black key to the left of B. <a href="/letter-notes/twelve-days-of-christmas">The Twelve Days of Christmas</a> and <a href="/letter-notes/o-christmas-tree">O Christmas Tree</a> are in F major. Flats are added in the order B E A D G C F, the reverse of the sharps, and the rule for naming the key is different: the key is the second-to-last flat. With only one flat there is no second-to-last, so you memorize this one: one flat is F major.</p>

<h2>Why composers bother</h2>
<p>A piece could be written in C with sharps and flats scattered through every bar, and some are. Keys exist because instruments and voices have ranges: Jingle Bells in G sits comfortably for most singers; in C it is either too low or too high. And keys have colour. Two pieces on this site are moved from their original keys to make them easier: our <a href="/letter-notes/moonlight-sonata">Moonlight Sonata</a> is in A minor instead of C♯ minor (four sharps) and <a href="/letter-notes/nocturne-op9-no2">Chopin's Nocturne</a> is in C instead of E♭ (three flats). They are the same tune. Pianists will tell you they are not the same piece, and they are right: the black keys change the hand shape and the sound. For learning the notes, though, fewer sharps is simply fewer things to go wrong.</p>

<h2>Reading a key signature in three seconds</h2>
<ol>
  <li>Count the sharps or flats after the clef.</li>
  <li>Sharps: the key is one letter above the last sharp. Flats: the key is the second-to-last flat (one flat: F).</li>
  <li>Look at the last note of the piece. If it is that letter, major. If it is three letters below it (G major ends on E, C major ends on A), minor.</li>
</ol>
<p>Then play, and every time the letter under a note carries a ♯ or ♭, that is the key signature at work.</p>
"""},

 "is-this-song-public-domain": {
  "title": "Is this song public domain? How we decide what to publish",
  "desc": "The rules of thumb we use before putting a song on this site: composer death dates, publication before 1930, the separate copyright on arrangements and lyrics, and the famous traps like Happy Birthday and Carol of the Bells.",
  "date": "2026-10-10", "image": "/songs/happy-birthday.png",
  "body": """
<p class="lead">Every one of the demo songs on this site is a melody nobody owns. Deciding that is not always as simple as "it is old". These are the questions we ask before a song goes up, with examples of the ones that nearly caught us. None of this is legal advice; it is the checklist of a small publisher that would rather leave a song out than guess.</p>

<h2>1. When did the composer die?</h2>
<p>In most of the world, including the European Union, the United Kingdom, South Korea and Japan, a musical work enters the public domain 70 years after the end of the year its composer died. Beethoven (1827), Chopin (1849), Mozart (1791), Bach (1750), Grieg (1907), Tchaikovsky (1893): all comfortably past. Rachmaninoff died in 1943, so his music became free in 2014. Ravel died in 1937; free since 2008. Gershwin died in 1937, which is why we briefly considered Rhapsody in Blue and then took it down: see question four.</p>
<p>For a song with a lyricist as well as a composer, the clock runs from the later death. For traditional songs with no known composer, the melody is public domain by definition, but the particular version you found in a book may not be.</p>

<h2>2. When was it published?</h2>
<p>The United States uses a different rule for older works: anything published before 1930 is public domain in the US regardless of when the author died, and works from 1930 onward are protected for 95 years from publication. Because our visitors are mostly in the US and Europe, we require both tests to pass: composer dead 70 years, and published before 1930. "The Twelve Days of Christmas" is an 18th-century text, but the tune everyone sings was arranged by Frederic Austin in 1909. He died in 1952. Published 1909 makes it free in the US; died 1952 made it free in Europe from 2023. It went up this year.</p>

<h2>3. Is the melody free but the words not?</h2>
<p>Words and music are separate works. "Happy Birthday to You" is the famous case: the melody is from "Good Morning to All" (1893), but the birthday lyrics were claimed under copyright until a court threw the claim out in 2016. We publish no lyrics at all, on any song, which removes the question. It also removes the second most common trap: a translation. The German "O Tannenbaum" is old; a particular English translation may have been written last decade by someone who is very much alive.</p>

<h2>4. Is it the melody, or somebody's arrangement?</h2>
<p>This is the one that catches careful people. A public-domain melody can be arranged, and the arrangement is a new work with its own copyright. The easy-piano version in a 2015 method book, the choral setting, the film orchestration, the chord chart on a lyrics website: all of these can be protected even though the tune is not. Rhapsody in Blue is a sharp example: Gershwin's own piano version is public domain, but the famous orchestral sound is Ferde Grofé's orchestration, and Grofé died in 1972. We decided we could not publish a simplified version without someone reasonably thinking it was derived from the orchestration, and removed it.</p>
<p>So we never copy an arrangement. Every score here was written by us from the melody: our left hand, our voicings, our simplifications. The melodies we check against public sources; the arrangement is ours. Carol of the Bells is the clearest case of why this matters: Leontovych's melody (1914, died 1921) is free, but the English words and the arrangement that everyone knows are Peter Wilhousky's from 1936, and his estate enforces them. A new arrangement of the bare melody without the words would be legal; we have not published one, because the line between "the melody" and "the arrangement everyone knows" is thin for that piece and we would rather not test it.</p>

<h2>5. Is the recording or the edition free?</h2>
<p>A public-domain piece in a modern printed edition is still public domain, but the engraving, the fingering, the editorial markings and the page layout belong to the publisher. Scanning a page of a 2010 Henle edition and posting it is copying the edition. Typing the notes into notation software and rendering your own page is not. That distinction is why we render everything ourselves from LilyPond source files, and why the converter on the front page deletes your uploads after processing: we do not want to hold copies of anyone's editions, including yours.</p>
<p>Recordings are a separate layer again. A recording of a Bach prelude made in 1995 is protected for decades regardless of Bach. The MIDI files here are generated by us from our own scores and carry no recording rights.</p>

<h2>The songs we turned down</h2>
<p>For the record, and because people ask: Wheels on the Bus (1939), You Are My Sunshine (1939), Heart and Soul (1938), Rudolph the Red-Nosed Reindeer (1949), Santa Claus Is Coming to Town (1934), Jingle Bell Rock (1957), Feliz Navidad (1970), Kookaburra (1932), and every film, game and pop theme. All of these are requested often and all are still in copyright. Many lyrics sites and YouTube tutorials publish them anyway; their risk tolerance is not ours.</p>

<h2>If you want to check a song yourself</h2>
<ol>
  <li>Find the composer and the lyricist, not the performer. Wikipedia usually has both.</li>
  <li>Both dead more than 70 full years ago, and the work published before 1930? Melody is free almost everywhere.</li>
  <li>Make your own arrangement. Do not copy a published one, however simple it looks.</li>
  <li>Leave out the words unless you have checked the words separately.</li>
  <li>If you are not sure, leave it out. There are more public-domain tunes than anyone can arrange in a lifetime.</li>
</ol>
"""},

 "chord-symbols-for-beginners": {
  "title": "Chord symbols for beginners: what C, G7 and Am mean above the bar",
  "desc": "The green letters above each bar on our scores are chord symbols. What they mean, how to play a left hand from them, how Notalo works them out from the notes, and why it sometimes writes Cmaj7 where you expected C.",
  "date": "2026-10-10", "image": "/songs/canon-in-d.png",
  "body": """
<p class="lead">Every score on this site has green letters above the bars: C, G7, Am, Dm7. They are chord symbols, the shorthand guitarists and jazz pianists have used for a century, and they let you play a left hand without reading a single bass note. Here is how to read them, how to play from them, and how the converter decides which one to write.</p>

<h2>What a chord symbol says</h2>
<p>A chord symbol names a chord by its root and its type. <strong>C</strong> means a C major chord: C, E and G. <strong>G</strong> means G, B and D. The capital letter alone always means major. A lower-case <strong>m</strong> means minor: <strong>Am</strong> is A, C and E, with the middle note a semitone lower than in A major. A <strong>7</strong> adds the seventh note above the root, flattened: <strong>G7</strong> is G, B, D and F. <strong>maj7</strong> adds it unflattened: <strong>Cmaj7</strong> is C, E, G and B. That covers almost every symbol on this site. The rest are rare: <strong>dim</strong> (diminished), <strong>sus4</strong> (the third replaced by the fourth), a slash like <strong>C/E</strong> meaning a C chord with E as the lowest note.</p>

<h2>Building any major or minor chord</h2>
<p>You do not need to memorize them. Start on the root and count up the white and black keys together. A major chord is root, then four keys up, then three more. C: C, up four to E, up three to G. A minor chord is root, three up, four up. A: A, up three to C, up four to E. Every chord symbol with a plain letter or an m can be built this way in a few seconds, and after a week of doing it you will stop counting.</p>

<h2>Playing a left hand from the symbols</h2>
<p>The simplest left hand is the one our scores use: play the chord as a block, all notes at once, on the first beat of the bar, and hold it until the next symbol. That is what the blue letters under the bass staff are. Once that is comfortable, there are two upgrades that make any song sound more finished:</p>
<ul>
  <li><strong>Root then chord.</strong> On beat one play just the root with the fifth finger; on beat two (or three, in 3/4 time) play the other two notes above it with the thumb and index finger. This is the "oom-pah" pattern and it fits every song in 3/4 and 4/4 on this site. Try it on <a href="/letter-notes/blue-danube">The Blue Danube</a>, which is written for it.</li>
  <li><strong>Broken chord.</strong> Play the three notes one after another, low to high, as even eighths. Bach's <a href="/letter-notes/prelude-in-c">Prelude in C</a> is nothing but this pattern, with the chord symbols changing every bar; it is the best possible exercise for it.</li>
</ul>
<p>Guitarists read the same symbols and strum them, which is why a page from this site works as a lead sheet for a singalong with a guitar.</p>

<h2>How Notalo decides which symbol to write</h2>
<p>The converter does not know what chord you meant. It looks at every notehead that falls inside a bar, in both hands, collects their letter names, and finds the chord that explains the most of them. If a bar contains C, E and G in the left hand and the melody wanders through C, D, E and G, the best match is C. If the melody also lands on a B, the best match becomes Cmaj7, because B is the major seventh of C, and that is what you will see written. If a bar has G, B, D and the melody adds an F, you get G7.</p>
<p>This is why the symbols are occasionally more complicated than a human arranger would write. In the <a href="/letter-notes/london-bridge">London Bridge</a> score, bar one is labeled Am7: the left hand holds a C chord and the melody passes through A, and C, E, G, A is literally an A minor seventh. An arranger would write C and call the A a passing note. The converter has no concept of a passing note, so it reports what is there. Read the symbol as "the notes in this bar add up to this", and simplify it yourself if the fancier chord sounds wrong: Am7 can always be played as C, Cmaj7 as C, G7 as G.</p>
<p>Two things to know about the guessing. First, it is per bar, so a bar that changes chord halfway (common in hymns and carols) gets one symbol for the whole bar, usually the first chord; on our own scores we split such bars into two chords, and the converter then writes two symbols. Second, a bar with only a melody and no left hand gets a guess from the melody alone, which is unreliable; the symbols are best on music with a written left hand.</p>

<h2>The five chords that cover most songs</h2>
<p>In any major key, three chords cover the majority of folk songs and carols: the ones built on the first, fourth and fifth notes of the scale. In C major that is C, F and G (or G7). In G major it is G, C and D. In F major, F, B♭ and C. Add the two minor chords built on the sixth and second notes (Am and Dm in C) and you can accompany nearly everything on this site. Look at the symbols on <a href="/letter-notes/jingle-bells">Jingle Bells</a>, <a href="/letter-notes/twelve-days-of-christmas">The Twelve Days of Christmas</a> and <a href="/letter-notes/amazing-grace">Amazing Grace</a> in turn, and you will see the same three-chord pattern in three different keys. Once you see it, you can play the left hand of a song you have never heard from its symbols alone, which is the point of the whole system.</p>
"""},
 "piano-keyboard-notes-chart": {
  "title": "Piano keyboard notes chart: every key named, and how to find middle C",
  "desc": "A labeled chart of the piano keys from C3 to B5 with every white and black key named, octave numbers, and the two-and-three black-key pattern that lets you find any note in seconds on any piano or keyboard.",
  "date": "2026-10-25", "image": "/guide/keyboard.png",
  "body": """
<p class="lead">A piano keyboard looks like 88 identical keys. It is really one pattern of twelve keys, seven white and five black, repeated from the bottom of the instrument to the top. Learn the pattern once and you can name any key on any piano, keyboard or app, without counting from the end.</p>

<figure><img src="/guide/keyboard.png" alt="Piano keyboard chart from C3 to B5 with every white key labeled C D E F G A B with its octave number, every black key labeled with its sharp and flat name, and middle C (C4) highlighted" width="1152" height="440"><figcaption>Three octaves, C3 to B5. White keys in red, octave numbers below, sharp and flat names on the black keys. Middle C is highlighted.</figcaption></figure>

<h2>The pattern: twos and threes</h2>
<p>Look only at the black keys. They come in groups: two, then three, then two, then three, all the way along. That alternation is the whole map. Two landmarks are enough to read it:</p>
<ul>
  <li><strong>C</strong> is the white key just to the left of every group of <strong>two</strong> black keys.</li>
  <li><strong>F</strong> is the white key just to the left of every group of <strong>three</strong> black keys.</li>
</ul>
<p>From C, the white keys go up through the alphabet: C, D, E, F, G, A, B, and then C again. Music uses only those seven letters. After G comes A, not H, which is the one place the alphabet trips people up. Between E and F, and between B and C, there is no black key, which is why the groups split where they do.</p>

<h2>The black keys: sharps and flats</h2>
<p>Every black key has two names. The black key just above C is <strong>C♯</strong> (C sharp), because it is one step higher than C. It is also <strong>D♭</strong> (D flat), because it is one step lower than D. Both names are correct; which one a piece of music uses depends on its key. A piece in G major writes F♯, never G♭, for the same key. The <a href="/learn/key-signatures-by-example">key signatures article</a> explains which name to expect when.</p>
<p>The step from any key to the very next key, white or black, is a <strong>half step</strong> (or semitone). Two half steps make a <strong>whole step</strong>. C to D is a whole step with a black key in between; E to F is a half step with nothing in between. Every scale and chord is built from these two distances, so it is worth seeing them on the keyboard early.</p>

<h2>Octave numbers, and which C is middle C</h2>
<p>Because the letters repeat, musicians number each octave. The numbering changes at every C: the C and all the keys above it up to the next B share a number. <strong>Middle C is C4.</strong> The keys above it are D4, E4 and so on up to B4; the next C is C5. Going down from middle C, the B just below it is B3.</p>
<p>On a full 88-key piano the lowest key is A0 and the highest is C8, and middle C is the fourth C from the left. On a 61-key keyboard, which usually runs from C2 to C7, middle C is the third C from the left. On smaller keyboards the safest rule is to find the C closest to the middle of the instrument; on most pianos it is right below the brand name.</p>
<p>One warning that catches people moving between apps: some manufacturers and music programs call middle C <strong>C3</strong> instead of C4. The key is the same; only the label is shifted by one. If a MIDI file or app says a note is C5 and it sounds an octave lower than you expected, this is almost always the reason. Notalo and the charts on this site use the more common convention, middle C = C4, which is also MIDI note number 60.</p>

<h2>How the keys line up with the staff</h2>
<p>Middle C is the meeting point of the two staves in piano music. It sits on a short ledger line just <em>below</em> the treble staff and just <em>above</em> the bass staff, and both mean the same key. Everything on the treble staff is middle C and above, mostly played by the right hand; everything on the bass staff is middle C and below, mostly the left. The staff lines map onto the keys like this:</p>
<table>
  <tr><th>Staff</th><th>Bottom line</th><th>Middle line</th><th>Top line</th></tr>
  <tr><td>Treble clef</td><td>E4</td><td>B4</td><td>F5</td></tr>
  <tr><td>Bass clef</td><td>G2</td><td>D3</td><td>A3</td></tr>
</table>
<p>The full charts are in <a href="/treble-clef-notes">treble clef notes</a> and <a href="/bass-clef-notes">bass clef notes</a>. The two charts plus this one are all you need to go from a dot on the page to a key under your finger.</p>

<h2>A ten-minute drill to learn the keys</h2>
<ol>
  <li><strong>All the Cs.</strong> Starting from the bottom, play every C on the keyboard, saying "C" each time. Then every F. These two are your anchors; everything else is a step or two from one of them.</li>
  <li><strong>Up and down from C.</strong> Put your right thumb on middle C and play C D E F G with one finger per key, saying the names. This is the "C position" that the first songs on this site use.</li>
  <li><strong>Random keys.</strong> Close your eyes, put a finger anywhere, open your eyes and name the key from the nearest group of black keys. Ten keys a day for a week is enough to make it automatic.</li>
  <li><strong>Black keys both ways.</strong> Pick any black key and say both its names: "F sharp, G flat". It feels redundant until the first piece that uses flats.</li>
</ol>
<p>Then play something. <a href="/letter-notes/mary-had-a-little-lamb">Mary Had a Little Lamb</a> and <a href="/letter-notes/ode-to-joy">Ode to Joy</a> use only the five keys from C to G in the right hand, and every note on those pages has its letter written under it, so the chart above is all you need to play them.</p>

<h2>Should you put stickers on the keys?</h2>
<p>Note stickers are fine for the first week or two, while the twos-and-threes pattern is still new. Their cost is that your eyes learn to read the sticker instead of the shape of the keyboard, and the habit is hard to drop later. A gentler aid is a single sticker or a small piece of tape on middle C only: one fixed reference point, with every other key found from the pattern. Once you can find any C and F without looking for long, take the sticker off.</p>

<h2>Common mistakes</h2>
<ul>
  <li><strong>Mixing up C and F.</strong> Both sit to the left of a black-key group. Look at the size of the group: two means C, three means F.</li>
  <li><strong>Counting from the end of the keyboard.</strong> Slow and error-prone. Always find the nearest group of black keys instead.</li>
  <li><strong>Looking for E♯ or B♯ on a black key.</strong> They exist as names (E♯ is the same key as F, B♯ the same as C), but there is no black key between E and F or B and C.</li>
  <li><strong>Losing middle C on a small keyboard.</strong> Count Cs from the middle of the instrument, not from the left edge, or check the octave buttons: many keyboards shift every key by an octave when they are pressed.</li>
</ul>
"""},
}
