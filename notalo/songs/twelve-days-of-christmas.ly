\version "2.22.0"
\include "_common.ily"
\score { \new PianoStaff <<
  \new Staff { \clef treble \key f \major \time 4/4
    \partial 4 c'8 c' |
    f'4 f'8 f' f'4 e' | f'8 g' a'4 bes'8 g' a'4 | bes'8 c'' d''4 bes'8 a' f' g' | f'2. c'8 c' |
    f'4 f'8 f' f'4 e' | f'8 g' a'4 bes'8 g' a'4 | c''4 g'4. a'8 bes'4 | a'8 bes' c''4 d''4 bes'8 a' | f'8 g' f'2. \bar "|." }
  \new Staff { \clef bass \key f \major \time 4/4
    \partial 4 r4 |
    <f, a, c>1 | <c e g> | <bes, d f> | <f, a, c> |
    <f, a, c> | <c e g> | <f, a, c> | <bes, d f> | <f, a, c> \bar "|." } >> \layout { } }
