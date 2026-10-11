\version "2.22.0"
\include "_common.ily"
\score { \new PianoStaff <<
  \new Staff { \clef treble \key c \major \time 4/4
    c''8 e'' e'' e'' d''16 c'' g''4 g''8 | g''8 f'' e'' f''16 e'' d''2 | c''8 e'' e'' e'' d''16 c'' g''4 g''8 | g''8 f'' e'' f''16 e'' d''4 c''4 |
    c''8 e'' e'' e'' d''16 c'' g''4 g''8 | g''8 f'' e'' f''16 e'' d''2 | c''8 e'' e'' e'' d''16 c'' g''4 g''8 | g''8 f'' e'' d'' c''2 \bar "|." }
  \new Staff { \clef bass \key c \major \time 4/4
    <c e g>1 | <g, b, d> | <c e g> | <c e g> |
    <c e g> | <g, b, d> | <c e g> | <c e g> \bar "|." } >> \layout { } }
