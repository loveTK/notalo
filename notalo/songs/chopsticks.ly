\version "2.22.0"
\include "_common.ily"
\score { \new PianoStaff <<
  \new Staff { \clef treble \key c \major \time 4/4
    f'4 f' e' e' | d' d' c'2 | f'4 f' e' e' | d' d' c'2 |
    f'4 f' e' e' | d' d' c' c' | f' f' e' e' | d' d' c'2 \bar "|." }
  \new Staff { \clef bass \key c \major \time 4/4
    <c e g>1 | <g, b, d> | <c e g> | <g, b, d> |
    <c e g> | <g, b, d> | <c e g> | <c e g> \bar "|." } >> \layout { } }
