[Go back to the main page](https://github.com/world-class/REPL)

# Table of contents
<!-- vim-markdown-toc GFM -->

* [Introduction to programming I - Reported problems](#introduction-to-programming-i---reported-problems)
    * [Sleuth cases](#sleuth-cases)
        * [Rookie](#rookie)
            * [101, stage 3](#101-stage-3)
            * [201, stage 4](#201-stage-4)
            * [Other glitches](#other-glitches)
                * [Sleuth cases with spotlight effect](#sleuth-cases-with-spotlight-effect)
                * [Variable assignment](#variable-assignment)
        * [Pro](#pro)
            * [601, All stages](#601-all-stages)
            * [601, stage 4](#601-stage-4)
            * [701, All stages](#701-all-stages)
            * [701, stage 4](#701-stage-4)
            * [702, All stages](#702-all-stages)
            * [702, stage 1](#702-stage-1)
            * [702, stage 2](#702-stage-2)
            * [702, stage 4](#702-stage-4)
            * [802, stage 2](#802-stage-2)
                * [Random function](#random-function)
        * [Global Sleuth glitches](#global-sleuth-glitches)
            * [`console.log()` statements](#consolelog-statements)
            * [Function parentheses](#function-parentheses)
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

---

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
- You should only use `beginShape()`, `vertex(x1, y1)` and `endShape(CLOSE)` in your code.

#### Other glitches
##### Sleuth cases with spotlight effect
Be aware that those Sleuth cases involving a spotlight effect will not work on Firefox out of the box (they work in any webkit based browser like Google Chrome and Safari). There are possible workarounds such as commenting out the line at the bottom that says `blendMode(DARKEST)` and uncommenting it again before submitting the case. Changing it to `blendMode(LIGHTEST)` should work at least to be able to see where the spotlight is.

##### Variable assignment
- Some cases ask to set the value of a variable to `mouseX` for instance and then make sure it doesn't go above or below a certain value with `min()` and `max()` functions. Answers can wrongly be accepted if you first set

      variable = mouseX

  and then reassign it by applying a function that is missing a parameter:

      variable = max(X)

  where `X` is an integer. The variable should be assign in one statement as follow instead:

      variable = max(mouseX, X)

---

### Pro
#### 601, All stages
When required to draw at the various locations of crimes and sightings, take note of the following:

- When asked to draw vertices, at least one vertex must be drawn on the exact co-ordinate. Any number of vertices > 1 can be drawn to get the grader to accept the submission.

- Other shapes like rectangles and triangles can be drawn around the exact co-ordinate (i.e. no edges passing through it or ending on it) provided that they are smaller than approx 10-15 px in diameter.

- The names of array that need plotting may not always match up with the type of crime that is specified, for example, the instructions may refer to thefts, but the array might be called MurderSceneRecord.

- When asked to use `stroke(r,g,b)`, also use `noFill()` and when asked to use `fill(r,g,b)` also use `noStroke()`. Even though these functions are not allowed according to the instructions, the grader appears to need them to correctly assess the stroke and fill properties.

- When asked to draw rects around a point, do not use `rectMode(CENTER)` as it may confuse the grader. Simply use `rect(x-5, y-5, 10, 10)` or similar.

#### 601, stage 4
Where possible matches need to be pushed into a separate array after comparing dates and distances, take note that some conditions could be too strict resulting in zero matches, which could at first seem like an error in your code. In such cases, if you submit, the grader will accept the empty array as long as the logic was implemented correctly.

#### 701, All stages
Witnesses sometimes give details relating to features or characteristics for which no properties are defined in the object arrays. It is usually not required to check for these. If problematic, get suspended to get a new case.

#### 701, stage 4
Some versions of this stage have misspelled words which prevent the student from solving the case. If you encounter the words `plasic` or `nerveous`, you need to make sure that your solution searches for `plastic` or `nervous` instead. Some other variations along those lines with other misspelled words may exist but haven't been reported yet.

#### 702, All stages
Probably the trickiest of all the Sleuth cases. Instructions are not always explicitly clear and require insight into objects and functions.

#### 702, stage 1
There is a bug in the instructions, stating that you need to:
`Get your car on the road by completing the </DRIVE_NAME/> function below.`

The function that requires editing is called `Move_Car()` (or similar).

#### 702, stage 2
Hardest part is to implement the function to check/search a vehicle ahead by comparing the passed variable's (detective car object) distance/km/miles property against the ones in the array. There are several ways to do this, but the grader may not always like what you're doing. Some guidance here:

You need to check each object in the array to confirm using if-statement(s) that:
- They are in the same lane (easy, as per the instructions)
- That the difference between the distance/km/miles-properties of the car ahead and the detective vehicle less than 200
- That the car in the array is in front of (and not behind) the detective car

Note that the `distance`/`km`/`miles_travelled` property is increasing towards the top of the screen, opposite to the regular y-coordinate. Since debugging the array might be tricky, consider adding a text readout to each car using a variation of:
`text(Vehicles[i].Distance, Vehicles[i].X, Vehicles[i].Y); //debug`

Once implemented correctly, remember the logic, as you will likely need to create similar functions things in the stages ahead.

#### 702, stage 4
_"My suspect's car didn't have enough space to pull out in front of me before speeding off, so the chase wouldn't work as expected. I deliberately got myself suspended so I could grab another case, and it worked fine."_ (reported by [@dannycallaghan](https://github.com/dannycallaghan))

#### 802, stage 2
##### Random function
_"They ask you to create an array of random integers between two values. The `random()` function in `p5.js` includes the lower number, but excludes the upper number. So if you do `random(5,9)`, it might well generate a **5**, but never a **9**._

_Naturally I incremented the upper value by one so it'd actually generate values between the two numbers requested, but the puzzle actually expects you to just naively slot the two values into random and not fix the bug."_ (reported by *Pehoulihan*)

---

### Global Sleuth glitches
#### `console.log()` statements
If you get this message when submitting a case:

    There is an error in your code ... Error in compile SyntaxError: Unexpected token )

Be sure that you have removed all of your debugging statements that are using `console.log()`. This is one of those unexpected situations where your statements should have no effect, but they do somehow.

#### Function parentheses
If you get this message when submitting a case:

    TypeError: studentFunctionCodeString.search is not a function

You need to ensure that any function being declared does not have a space between the function name and the argument. So for example:

    function myFunc() // Grader should accept this
    function myFunc () // Grader might not accept this


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
- The bomb exercise template is missing.

### Lesson 4.2
#### Practice quiz: Introducing types: String, Number, Boolean
- Question 5: The question asks for **two** ways to reuse the variable `numWays` but expects **three** selected answers.

#### Practice quiz: Conditionals with types
- Question 3: The question says the answer _"No, because  answer is neither a number, nor is it equal to the number 42"_ is correct. However the correct answer is _"Yes, because answer is equal to 42"_.
- Question 5: The question says the answer `parseInt(a+b)*c` is correct and the others are all wrong: however `(a+b)*c` is also correct. They both produce the same result.
