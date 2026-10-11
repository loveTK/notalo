\version "2.22.0"
\include "_common.ily"
\score { \new PianoStaff <<
  \new Staff { \clef treble \key c \major \time 3/4
    \partial 4 g'8. e'16 |
    c'4 e' g' | c''2 e''8 d'' | c''4 e' fis' | g'2 g'8 g' |
    e''4. d''8 c''4 | b'2 a'8 b' | c''4 c'' g' | e'4 c'2 \bar "|." }
  \new Staff { \clef bass \key c \major \time 3/4
    \partial 4 r4 |
    <c e g>2. | <c e g> | <d fis a> | <g, b, d> |
    <c e g> | <g, b, d> | <c e g> | <c e g> \bar "|." } >> \layout { } }
