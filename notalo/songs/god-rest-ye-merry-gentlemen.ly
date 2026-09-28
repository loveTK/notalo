\version "2.22.0"
\include "_common.ily"
\score { \new PianoStaff <<
  \new Staff { \clef treble \key e \minor \time 4/4
    \partial 4 e'4 |
    e'4 b' b' a' | g'2 fis'4 e' | d'4 e' fis' g' | a'2 b'4 e' |
    e'4 b' b' a' | g'2 fis'4 e' | d'4 e' fis' g' | a'2 b'4 b' |
    c''4 a' b' c'' | d''2 e''4 b' | a'4 g' e' fis' | g'2 g'4 a' |
    b'4 c'' b' b' | a'4 g' fis' e' | g'4 fis' e'2 | g'4 a' b' c'' | d''4 e'' b' a' | g'4 fis' e'2 \bar "|." }
  \new Staff { \clef bass \key e \minor \time 4/4
    \partial 4 r4 |
    <e, g, b,>1 | <e, g, b,> | <g, b, d> | <b, dis fis> |
    <e, g, b,> | <e, g, b,> | <g, b, d> | <b, dis fis> |
    <a, c e> | <g, b, d> | <e, g, b,> | <e, g, b,> |
    <g, b, d> | <e, g, b,> | <e, g, b,> | <c e g> | <b, dis fis> | <e, g, b,> \bar "|." } >> \layout { } }
