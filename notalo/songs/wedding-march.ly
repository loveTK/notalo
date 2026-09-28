\version "2.22.0"
\include "_common.ily"
\score { \new PianoStaff <<
  \new Staff { \clef treble \key c \major \time 4/4
    c'4 c'8 c' e'2 | e'4 e'8 e' g'2 | g'4 g'8 g' b'2 | e''4 a'8 g' f'4 d' |
    c'4 c'8 c' e'2 | e'4 e'8 e' g'2 | g'4 g'8 g' b'2 | c''1 \bar "|." }
  \new Staff { \clef bass \key c \major \time 4/4
    <c e g>1 | <c e g> | <g, b, d> | <g, b, d> |
    <c e g> | <c e g> | <g, b, d> | <c e g> \bar "|." } >> \layout { } }
