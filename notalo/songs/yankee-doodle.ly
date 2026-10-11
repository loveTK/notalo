\version "2.22.0"
\include "_common.ily"
\score { \new PianoStaff <<
  \new Staff { \clef treble \key c \major \time 2/4
    c''8 c'' d'' e'' | c''8 e'' d''4 | c''8 c'' d'' e'' | c''4 b'8 g' | c''8 c'' d'' e'' | f''8 e'' d''4 | c''8 b' g' a' | b'8 c'' c''4 |
    a'8 b' a' g' | a'8 b' c''4 | g'8 a' g' f' | e'4 g'4 | a'8 b' a' g' | a'8 b' c''4 | a'8 g' c'' b' | d''8 c'' c''4 \bar "|." }
  \new Staff { \clef bass \key c \major \time 2/4
    <c e g>2 | <g, b, d> | <c e g> | <g, b, d> | <c e g> | <f, a, c> | <g, b, d> | <c e g> |
    <f, a, c> | <c e g> | <g, b, d> | <c e g> | <f, a, c> | <c e g> | <g, b, d> | <c e g> \bar "|." } >> \layout { } }
