\version "2.22.0"
\include "_common.ily"
\score { \new PianoStaff <<
  \new Staff { \clef treble \key d \major \time 3/4
    d'4 fis' a' | a'2. | a''2 a''4 | fis''2 fis''4 | d'4 fis' a' | a'2. | a''2 a''4 | g''2 g''4 |
    d'4 fis' a' | a'2. | a''2 a''4 | d''2. \bar "|." }
  \new Staff { \clef bass \key d \major \time 3/4
    <d fis a>2. | <d fis a> | <d fis a> | <d fis a> | <d fis a> | <d fis a> | <a, cis e> | <a, cis e> |
    <d fis a> | <d fis a> | <d fis a> | <d fis a> \bar "|." } >> \layout { } }
