\version "2.22.0"
\include "_common.ily"
\score { \new PianoStaff <<
  \new Staff { \clef treble \key c \major \time 4/4
    e'4 d' c' d' | e' f' g'2 |
    a'4 b' c''2 | b'4 a' g'2 |
    a'4 b' c''4 b' | a'1 |
    c''4 b' a' g' | a' b' c''2 |
    g'4 f' e'2 \bar "|." }
  \new Staff { \clef bass \key c \major \time 4/4
    <c e g>1 | <g, b, d> |
    <f, a, c> | <c e g> |
    <f, a, c> | <c e g> |
    <c e g> | <g, b, d> |
    <c e g> \bar "|." } >> \layout { } }
