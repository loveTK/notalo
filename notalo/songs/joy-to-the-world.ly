\version "2.22.0"
\include "_common.ily"
\score { \new PianoStaff <<
  \new Staff { \clef treble \key c \major \time 4/4
    c'4 b a g | f e d2 | c'4 d e f | g1 |
    e4 e e e | e d c2 | c'4 b a g | f e d c \bar "|." }
  \new Staff { \clef bass \key c \major \time 4/4
    <c e g>1 | <c e g> | <f, a, c> | <c e g> |
    <c e g> | <g, b, d> | <c e g> | <g, b, d> \bar "|." } >> \layout { } }
