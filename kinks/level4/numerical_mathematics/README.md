[Go back to the main page](https://world-class.github.io/REPL/)

# Table of contents
<!-- vim-markdown-toc GFM -->

* [Numerical Mathematics](#numerical-mathematics)
    * [Week 1](#week-1)
        * [Video: 1.001 Introduction to number bases and modular arithmetic](#video-1001-introduction-to-number-bases-and-modular-arithmetic)
        * [Video: 1.101 Introduction to number bases](#video-1101-introduction-to-number-bases)
        * [Video: 1.107 Place value for fractional numbers: binary](#video-1107-place-value-for-fractional-numbers-binary)
        * [Practice quiz: 1.110 Rational and irrational numbers: decimal and binary](#practice-quiz-1110-rational-and-irrational-numbers-decimal-and-binary)
    * [Week 2](#week-2)
        * [Video: 1.401 Octal and hexadecimal (integer)](#video-1401-octal-and-hexadecimal-integer)
        * [Video: 1.405 Special relationship between binary and hexadecimal, and binary and octal](#video-1405-special-relationship-between-binary-and-hexadecimal-and-binary-and-octal)
        * [Practice quiz: 1.406 Translate between binary and hexadecimal/octal](#practice-quiz-1406-translate-between-binary-and-hexadecimaloctal)
        * [Practice quiz: 1.602 Arithmetic in hexadecimal/octal](#practice-quiz-1602-arithmetic-in-hexadecimaloctal)

<!-- vim-markdown-toc -->

# Numerical Mathematics
This page is about the [numerical mathematics module](../../../modules/level_4/numerical_mathematics/).

## Week 1
### Video: 1.001 Introduction to number bases and modular arithmetic
- At 11:16, `(255, 255, 255)` is **white**, not blue.

### Video: 1.101 Introduction to number bases
- At 11:34: Wrong. Each column is a power of 60, so it should be times `1`, times `60` and times `3600`.


### Video: 1.107 Place value for fractional numbers: binary
- At 0:37: The "fractional point" is called "radix point".

### Practice quiz: 1.110 Rational and irrational numbers: decimal and binary
- Answers should be given without spaces.
- When a repeating fractional part is present, the answer should be written as `i.rr...`, where `i` stands for **integer part**, `r` is the **repeating** fraction and one must include three dots at the end. Example:

    3.12121212121212

  is written as
  
    3.1212...

## Week 2
### Video: 1.401 Octal and hexadecimal (integer)
- In the quiz at 3:41, the place values are supposed to be entered as "1, 16, 256". The answer isn't accepted.
- In the quiz at 4:24, 65536 should be written as 2^(16), but the "6" isn't part of the exponent part.
- At 5:07, second letter in hexadecimal should be "B", not "D".
- At 6:01, the hexadecimal number `11F` should have an expansion starting with `1 × 16^2`, not `1 × 16 (base 2)` as displayed.
- In the quiz at 6:29, the third answer is 256, not 64. The last part is asking in the quiz for multiples in binary while the answer is given for hexadecimal.

### Video: 1.405 Special relationship between binary and hexadecimal, and binary and octal
- At 7:38, this is wrong. `C` (base 16) = 12 (base 10) = 1100 (base 2), not 1101.
- At 11:24, The grouping of digits is wrong.

    1.001.111 1

  in binary should read

    1 001.111 1

  having only one radix point.

- At 11:37, it is said the answer is `11.71` (base 8). Wrong: It's `11.74` (base 8).

### Practice quiz: 1.406 Translate between binary and hexadecimal/octal
- Question 6: `73.06` (base 8) *is* `111011.00011` in binary.

### Practice quiz: 1.602 Arithmetic in hexadecimal/octal
- `6D * 60` in hexadecimal is `28E0`.
