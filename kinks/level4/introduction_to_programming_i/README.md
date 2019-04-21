[Go back to the main page](https://world-class.github.io/REPL/)

# Table of contents
<!-- vim-markdown-toc GFM -->

* [Introduction to programming I - Reported problems](#introduction-to-programming-i---reported-problems)
    * [Sleuth cases](#sleuth-cases)
        * [101, stage 3](#101-stage-3)
        * [201, stage 4](#201-stage-4)
    * [Week 1](#week-1)
        * [Lesson 1.1](#lesson-11)
            * [Video: 2D coordinate system](#video-2d-coordinate-system)
    * [Week 3](#week-3)
        * [Lesson 2.1](#lesson-21)
            * [Video: RGB colours](#video-rgb-colours)
        * [Lesson 2.2](#lesson-22)
            * [Practice quiz: Using the console and debugging syntax errors](#practice-quiz-using-the-console-and-debugging-syntax-errors)

<!-- vim-markdown-toc -->


# Introduction to programming I - Reported problems
This page is about the [Introduction to programming I module](../../../modules/level_4/introduction_to_programming_i/).

## Sleuth cases
### 101, stage 3
- Use only `fill()` and `rect()` commands. You can adjust opacity with `fill()` by adding a fourth value like so:

    fill(R, G, B, A);

  where `R`, `G` and `B` stand for **red**, **green**, **blue** and can have values from 0 to 255 and `A` stands for **alpha** and is optional. In this case, a value of about `100` is fine so you can see through the shape being drawn.

### 201, stage 4
- Some students were given cases where body parts of the judge are missing (i.e., legs appear outside the canvas, for instance). In those cases, you may be better off just failing all your attempts and wait for a new randomized case to be given to you as you probably won't be able to get 100%.
- If your answer isn't accepted, try increasing the number of times you have `vertex()` in your code. Answers including at least 40 to 50 vertices have been reported to work better.
- You should only use `beginShape();`, `vertex(x1, y1);` and `endShape(CLOSE);` in your code.

## Week 1
### Lesson 1.1
#### Video: 2D coordinate system
- At 3:56, the top left corner should have coordinates `(4, 3)` instead of `(5, 3)`.
- At 3:56, the width of the rectangle is `12`, not `11`.


## Week 3
### Lesson 2.1
#### Video: RGB colours
- At 7:20, the instructor says "sum", but the operation being done is a multiplication.

### Lesson 2.2
#### Practice quiz: Using the console and debugging syntax errors
- Question 3: "triangle" is misspelled → `trinagle`, adding an additional error which is not an argument error. However, the spelling mistake shouldn't be taken into account.
