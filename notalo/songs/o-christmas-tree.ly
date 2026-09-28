\version "2.22.0"
\include "_common.ily"
\score { \new PianoStaff <<
  \new Staff { \clef treble \key f \major \time 3/4
    \partial 4 c'4 |
    f'8. f'16 f'4 g' | a'8. a'16 a'4 a' | a'8 g' a' bes' e'4 | g'4 f' c'' |
    c''4. a'8 d''4 | c''4 c'' bes' | bes'2 bes'4 | bes'4. g'8 c''4 | bes'4 bes' a' | a'2 c'4 |
    f'8. f'16 f'4 g' | a'8. a'16 a'4 a' | a'8 g' a' bes' e'4 | g'4 f'2 \bar "|." }
  \new Staff { \clef bass \key f \major \time 3/4
    \partial 4 r4 |
    <f, a, c>2. | <f, a, c> | <c e g> | <f, a, c> |
    <f, a, c> | <c e g> | <bes, d f> | <c e g> | <f, a, c> | <f, a, c> |
    <f, a, c> | <f, a, c> | <c e g> | <f, a, c> \bar "|." } >> \layout { } }
