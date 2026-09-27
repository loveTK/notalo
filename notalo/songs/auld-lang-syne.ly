\version "2.22.0"
\include "_common.ily"
\score { \new PianoStaff <<
  \new Staff { \clef treble \key d \major \time 4/4
    d'4 g' g' g' | b' a' g' a' |
    b'4 g' g' b' | d''2 e''2 |
    e''4 d'' b' b' | g' a' g' a' |
    b'4 a' g'2 | e'4 e' d' g' |
    e''4 d'' b' b' | g' a' g' a' |
    e''4 d'' b' b' | d''2 e''2 |
    g''4 d'' b' b' | g' a' g' a' |
    b'4 a' g'2 | e'4 e' d'2 \bar "|." }
  \new Staff { \clef bass \key d \major \time 4/4
    <d g b>1 | <g, b, d> |
    <g, b, d> | <g, b, d> |
    <g, b, d> | <d g b> |
    <a, cis e> | <d g b> |
    <g, b, d> | <d g b> |
    <g, b, d> | <g, b, d> |
    <g, b, d> | <d g b> |
    <a, cis e> | <d g b> \bar "|." } >> \layout { } }
