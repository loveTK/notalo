\version "2.22.0"
\include "_common.ily"
\score { \new PianoStaff <<
  \new Staff { \clef treble \key g \major \time 4/4
    d'4 g' g'4. fis'8 | g'4 b' b' a' | d''4 d'' d''4. c''8 | b'4 a' b'2 |
    d'4 g' g'4. fis'8 | g'4 b' b' a' | d''4 a' a'4. g'8 | fis'4 e' d'2 \bar "|." }
  \new Staff { \clef bass \key g \major \time 4/4
    <g, b, d>1 | <g, b, d> | <d fis a> | <g, b, d> |
    <g, b, d> | <g, b, d> | <d fis a> | <g, b, d> \bar "|." } >> \layout { } }
