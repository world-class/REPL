[Go back to the main page](https://github.com/world-class/REPL)

# Table of contents
<!-- vim-markdown-toc GFM -->

* [Introduction to programming I - Reported problems](#introduction-to-programming-i---reported-problems)
    * [Sleuth cases](#sleuth-cases)
        * [Rookie](#rookie)
            * [101, stage 3](#101-stage-3)
            * [201, stage 4](#201-stage-4)
            * [Other glitches](#other-glitches)
        * [Pro](#pro)
            * [702, stage 4](#702-stage-4)
            * [802, stage 2](#802-stage-2)
                * [Random function](#random-function)
                * [Apparently fixed](#apparently-fixed)
        * [Global Sleuth glitches](#global-sleuth-glitches)
    * [Week 1](#week-1)
        * [Lesson 1.1](#lesson-11)
            * [Video: 2D coordinate system](#video-2d-coordinate-system)
    * [Week 3](#week-3)
        * [Lesson 2.2](#lesson-22)
            * [Practice quiz: Using the console and debugging syntax errors](#practice-quiz-using-the-console-and-debugging-syntax-errors)
    * [Week 7](#week-7)
        * [Lesson 4.1](#lesson-41)
            * [Video: Conditional statements using ==](#video-conditional-statements-using-)
        * [Lesson 4.2](#lesson-42)
            * [Practice quiz: Introducing types: String, Number, Boolean](#practice-quiz-introducing-types-string-number-boolean)
            * [Practice quiz: Conditionals with types](#practice-quiz-conditionals-with-types)

<!-- vim-markdown-toc -->

# Introduction to programming I - Reported problems
This page is about the [Introduction to programming I module](../../../modules/level_4/introduction_to_programming_i/).

## Sleuth cases
### Rookie
#### 101, stage 3
- Use only `fill()` and `rect()` commands. You can adjust opacity with `fill()` by adding a fourth value like so:

    fill(R, G, B, A);

  where `R`, `G` and `B` stand for **red**, **green**, **blue** and can have values from 0 to 255 and `A` stands for **alpha** and is optional. In this case, a value of about `100` is fine so you can see through the shape being drawn.

#### 201, stage 4
- Some students were given cases where body parts of the judge are missing (i.e., legs appear outside the canvas, for instance). In those cases, you may be better off just failing all your attempts and wait for a new randomized case to be given to you as you probably won't be able to get 100%.
- If your answer isn't accepted, try increasing the number of times you have `vertex()` in your code. Answers including at least 40 to 50 vertices have been reported to work better.
- You should only use `beginShape();`, `vertex(x1, y1);` and `endShape(CLOSE);` in your code.

#### Other glitches
- Some cases ask to set the value of a variable to `mouseX` for instance and then make sure it doesn't go above or below a certain value with `min()` and `max()` functions. Answers can wrongly be accepted if you first set

      variable = mouseX

  and then reassign it by applying a function that is missing a parameter:

      variable = max(X)

  where `X` is an integer. The variable should be assign in one statement as follow instead:

      variable = max(mouseX, X)


### Pro
#### 702, stage 4
_"My suspect's car didn't have enough space to pull out in front of me before speeding off, so the chase wouldn't work as expected. I deliberately got myself suspended so I could grab another case, and it worked fine."_ (reported by [@dannycallaghan](https://github.com/dannycallaghan))

#### 802, stage 2
##### Random function
_"They ask you to create an array of random integers between two values. The `random()` function in `p5.js` includes the lower number, but excludes the upper number. So if you do `random(5,9)`, it might well generate a **5**, but never a **9**._

_Naturally I incremented the upper value by one so it'd actually generate values between the two numbers requested, but the puzzle actually expects you to just naively slot the two values into random and not fix the bug."_ (reported by *Pehoulihan*)

##### Apparently fixed
_"It asks you to fill an array with values, but the grader is clearly broken as I’ve used four different ways of adding values to an array (concat, push, by index, etc.) and I get this error every time (which makes no sense in terms of the sketch file, so must be the graded). Secondly, I  can’t get a new case as it won’t recognise that I’ve uploaded this maybe 20 times. It won’t stop me trying again. Thirdly, I’ve grabbed the cases for Parts 3 and 4, and they ask you to reuse the same function, and again it fails when grading that bit, so you can’t finish Case 802."_ (reported by [@dannycallaghan](https://github.com/dannycallaghan))

### Global Sleuth glitches
If you get this message when submitting a case:

    There is an error in your code ... Error in compile SyntaxError: Unexpected token )

Be sure that you have removed all of your debugging statements that are using `console.log();`. This is one of those unexpected situations where your statements should have no effect, but they do somehow.


## Week 1
### Lesson 1.1
#### Video: 2D coordinate system
- At 3:56, the top left corner should have coordinates `(4, 3)` instead of `(5, 3)`.
- At 3:56, the width of the rectangle is `12`, not `11`.


## Week 3
### Lesson 2.2
#### Practice quiz: Using the console and debugging syntax errors
- Question 3: "triangle" is misspelled → `trinagle`, adding an additional error which is not an argument error. However, the spelling mistake shouldn't be taken into account.

## Week 7
### Lesson 4.1
#### Video: Conditional statements using ==
- The bomb exercise template is missing. You can [download it here](https://www.dropbox.com/s/wudoo14bsg1l7am/Bomb%20Template.zip?dl=1).

### Lesson 4.2
#### Practice quiz: Introducing types: String, Number, Boolean
- Question 5: The question asks for **two** ways to reuse the variable `numWays` but expects **three** selected answers.

#### Practice quiz: Conditionals with types
- Question 3: The question says the answer _"No, because  answer is neither a number, nor is it equal to the number 42"_ is correct. However the correct answer is _"Yes, because answer is equal to 42"_.
- Question 5: The question says the answer `parseInt(a+b)*c` is correct and the others are all wrong: however `(a+b)*c` is also correct. They both produce the same result. 
