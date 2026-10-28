\version "2.22.0"
\include "_common.ily"
\score { \new PianoStaff <<
  \new Staff { \clef treble \key c \major \time 4/4
    g'2. a'8 g' | f'8 e' d' e' f'2 | g'4 a'8 g' f' e' d'4 | a'8 b' a'2. |
    gis'8 e' g' f' e' g' a' bes' | g'4 e' f' a' | g'2 g'4 d'' | b'8 d'' c''2. \bar "|." }
  \new Staff { \clef bass \key c \major \time 4/4
    <c e g>1 | <g, b, d> | <c e g> | <f, a, c> |
    <c e g> | <f, a, c> | <g, b, d> | <c e g> \bar "|." } >> \layout { } }
