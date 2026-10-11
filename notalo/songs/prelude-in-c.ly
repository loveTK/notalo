\version "2.22.0"
\include "_common.ily"
\score { \new PianoStaff <<
  \new Staff { \clef treble \key c \major \time 4/4
    c'8 e' g' c'' e'' g' c'' e'' | c'8 d' a' d'' f'' a' d'' f'' | b8 d' g' d'' f'' g' d'' f'' | c'8 e' g' c'' e'' g' c'' e'' |
    c'8 e' a' e'' a'' a' e'' a'' | c'8 d' fis' a' d'' fis' a' d'' | b8 d' g' d'' g'' g' d'' g'' | b8 c' e' g' c'' e' g' c'' \bar "|." }
  \new Staff { \clef bass \key c \major \time 4/4
    <c e>1 | c2 d | <b, d>1 | <c e> |
    <c e> | c2 d | <b, d>1 | b,1 \bar "|." } >> \layout { } }
