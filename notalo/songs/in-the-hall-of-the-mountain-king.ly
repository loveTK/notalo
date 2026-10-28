\version "2.22.0"
\include "_common.ily"
\score { \new PianoStaff <<
  \new Staff { \clef treble \key a \minor \time 4/4 \stemUp
    a'8 b' c'' d'' e'' c'' e''4 | dis''8 b' dis''2. | d''8 b' d''2. | a'8 b' c'' d'' e'' c'' e''4 |
    a''8 e'' c'' e'' a''2 | g''8 e'' g''2. | a''8 e'' c'' e'' a''2 | gis''8 e'' a''2. \bar "|." }
  \new Staff { \clef bass \key a \minor \time 4/4
    <a, c e>1 | <b, dis fis> | <b, d fis> | <a, c e> |
    <a, c e> | <c e g> | <a, c e> | <a, c e> \bar "|." } >> \layout { } }
