\version "2.22.0"
\include "_common.ily"
\score { \new PianoStaff <<
  \new Staff { \clef treble \key c \major \time 6/8
    \partial 8 g'8 |
    c''4 c''8 c''4 d''8 | e''4. e''4 e''8 | d''4 c''8 d''4 e''8 | c''4. c''4 e''8 |
    e''4 f''8 g''4. | g''4 f''8 e''4 f''8 | g''4 e''8 c''4 c''8 | d''4. e''4. |
    e''4 d''8 c''4 d''8 | e''8 c''4 g'4 g'8 | c''4 c''8 c''4 d''8 | e''4. e''4 e''8 | d''4 c''8 d''4 e''8 | c''2. \bar "|." }
  \new Staff { \clef bass \key c \major \time 6/8
    \partial 8 r8 |
    <c e g>2. | <c e g> | <g, b, d> | <c e g> |
    <c e g> | <g, b, d> | <c e g> | <g, b, d> |
    <c e g> | <c e g> | <c e g> | <c e g> | <g, b, d> | <c e g> \bar "|." } >> \layout { } }
