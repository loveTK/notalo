\version "2.22.0"
\include "_common.ily"
\score { \new PianoStaff <<
  \new Staff { \clef treble \key bes \major \time 4/4
    c'8 d' ees' f' g' a' bes' c'' | bes'8 a' g' f' ees' d' c' bes |
    c'4 ees' d' c' | bes2 c'2 |
    c'4 ees' d' c' | f'2 ees'2 |
    d'4 c' bes a | bes1 \bar "|." }
  \new Staff { \clef bass \key bes \major \time 4/4
    <bes, d f>1 | <bes, d f> |
    <ees, g bes> | <bes, d f> |
    <ees, g bes> | <f, a c> |
    <f, a c> | <bes, d f> \bar "|." } >> \layout { } }
