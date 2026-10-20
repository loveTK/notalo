\version "2.22.0"
\include "_common.ily"
\score { \new PianoStaff <<
  \new Staff { \clef treble \key c \major \time 4/4
    e'4 d' c' d' | e' e' e'2 | d'4 d' d'2 | e'4 g' g'2 |
    e'4 d' c' d' | e' e' e' e' | d' d' e' d' | c'1 \bar "|." }
  \new Staff { \clef bass \key c \major \time 4/4
    <c e g>1 | <c e g> | <g, b, d> | <c e g> |
    <c e g> | <c e g> | <g, b, d> | <c e g> \bar "|." } >> \layout { } }
