\version "2.22.0"
\include "_common.ily"
% 12/8 박자표 숫자를 검출기가 음표로 오인 → 숨김
\layout { \context { \Staff \override TimeSignature.stencil = ##f } }
\score { \new PianoStaff <<
  \new Staff { \clef treble \key c \major \time 12/8
    \partial 8 g'8 |
    e''4. d''8 e'' d'' c''4. g'4. | c''4. d''8 c'' b' c''4. g'4. | a'4. b'8 a' gis' a'4. c''4. | b'4. a'8 g' f' e'4. g'4. |
    e''4. d''8 e'' d'' c''4. g'4. | c''4. d''8 c'' b' c''4. e''4. | d''4. e''8 d'' c'' b'4. d''4. | c''1. \bar "|." }
  \new Staff { \clef bass \key c \major \time 12/8
    \partial 8 r8 |
    <c e g>1. | <c e g> | <f, a, c> | <g, b, d> |
    <c e g> | <c e g> | <g, b, d> | <c e g> \bar "|." } >> \layout { } }
