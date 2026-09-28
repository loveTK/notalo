\version "2.22.0"
\include "_common.ily"
\score { \new PianoStaff <<
  \new Staff { \clef treble \key g \major \time 4/4
    g'4. d'8 g'4. d'8 | g'8 d' g' b' d''2 | c''4. a'8 c''4. a'8 | c''8 a' fis' a' d'2 |
    g'2 g'4. fis'16 g' | b'2 b'4. a'16 b' | d''2 d''4. cis''16 d'' | g''8 fis'' e'' d'' c'' b' a' g' \bar "|." }
  \new Staff { \clef bass \key g \major \time 4/4
    <g, b, d>1 | <g, b, d> | <d fis a> | <d fis a> |
    <g, b, d> | <g, b, d> | <d fis a> | <g, b, d> \bar "|." } >> \layout { } }
