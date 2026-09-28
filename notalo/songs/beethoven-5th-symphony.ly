\version "2.22.0"
\include "_common.ily"
\score { \new PianoStaff <<
  \new Staff { \clef treble \key a \minor \time 2/4
    \partial 4. e''8 e'' e'' |
    c''2 | c''4. d''8 | d''8 d'' b'4 | b'2 | b'4. e''8 | e''8 e'' c''4 | c''4. f''8 | f''8 f'' d''4 | d''4. g''8 | g''8 g'' e''4 | e''2 \bar "|." }
  \new Staff { \clef bass \key a \minor \time 2/4
    \partial 4. r4. |
    <a, c e>2 | <a, c e> | <e, gis, b,> | <e, gis, b,> | <e, gis, b,> | <a, c e> | <a, c e> | <d f a> | <d f a> | <c e g> | <a, c e> \bar "|." } >> \layout { } }
