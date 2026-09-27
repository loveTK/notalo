\version "2.22.0"
\include "_common.ily"
\score { \new PianoStaff <<
  \new Staff { \clef treble \key c \major \time 4/4
    c'4 c' c' g | a a g2 | e'4 e' d d | c'1 |
    c'4 c' c' g | a a g2 | e'4 e' d d | c'1 \bar "|." }
  \new Staff { \clef bass \key c \major \time 4/4
    <c e g>1 | <f, a, c> | <c e g> | <c e g> |
    <c e g> | <f, a, c> | <c e g> | <c e g> \bar "|." } >> \layout { } }
