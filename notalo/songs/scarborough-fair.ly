\version "2.22.0"
\include "_common.ily"
\score { \new PianoStaff <<
  \new Staff { \clef treble \key a \minor \time 3/4
    a'4 a' e'' | e''4 b'8 c'' b'4 | a'2. | e''4 g'' a'' | g''4 e'' fis'' | d''2. |
    a''4 a'' g'' | e''2 e''4 | d''4 c'' b' | a'2. | a'4 d'' c'' | b'4 a' g' | e'4 a'2 | a'2. \bar "|." }
  \new Staff { \clef bass \key a \minor \time 3/4
    <a, c e>2. | <a, c e> | <a, c e> | <c e g> | <g, b, d> | <d fis a> |
    <a, c e> | <e, g, b,> | <g, b, d> | <a, c e> | <a, c e> | <g, b, d> | <a, c e> | <a, c e> \bar "|." } >> \layout { } }
