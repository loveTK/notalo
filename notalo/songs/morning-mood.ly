\version "2.22.0"
\include "_common.ily"
\score { \new PianoStaff <<
  \new Staff { \clef treble \key c \major \time 6/8
    g'8 e' d' c' d' e' | g'8 e' d' c' d' e' | g'8 e' g' a' e' a' | g'8 e' d' c' d' e' |
    g'8 e' d' c' d' e' | g'8 e' g' a' e' a' | g'8 e' g' a' e' a' | g'8 e' d' c'4. \bar "|." }
  \new Staff { \clef bass \key c \major \time 6/8
    <c e g>2. | <c e g> | <f, a, c> | <c e g> |
    <c e g> | <f, a, c> | <f, a, c> | <c e g> \bar "|." } >> \layout { } }
