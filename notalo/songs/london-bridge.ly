\version "2.22.0"
\include "_common.ily"
\score { \new PianoStaff <<
  \new Staff { \clef treble \key c \major \time 4/4
    g'4. a'8 g'4 f' | e'4 f' g'2 | d'4 e' f'2 | e'4 f' g'2 |
    g'4. a'8 g'4 f' | e'4 f' g'2 | d'2 g'2 | e'2 c'2 \bar "|." }
  \new Staff { \clef bass \key c \major \time 4/4
    <c e g>1 | <c e g> | <g, b, d> | <c e g>2 <c e g> |  % 마디4 온음표 화음이 검출기에서 F가 하나 더 잡혀 2분음표 둘로
    <c e g>1 | <c e g> | <g, b, d> | <c e g> \bar "|." } >> \layout { } }
