\version "2.22.0"
\include "_common.ily"
\score { \new PianoStaff <<
  \new Staff { \clef treble \key c \major \time 4/4
    e'4 e' e' g' | g' a' a' f' | a' c''4 g'2 |
    g'4 e' d' c' | e'4 f' a' f' | d'2 c'2 \bar "|." }
  \new Staff { \clef bass \key c \major \time 4/4
    <c e g>1 | <c e g> | <g, b, d>1 |
    <c e g> | <c e g> | <g, b, d>2 <c e g>2 \bar "|." } >> \layout { } }
