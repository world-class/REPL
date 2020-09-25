[Go back to the main page](../../../README.md)

# Table of contents

- [Table of contents](#table-of-contents)
- [ITP1 - Reported problems, tips and additional instructions](#itp1---reported-problems-tips-and-additional-instructions)
  - [Sleuth](#sleuth)
    - [General Sleuth Issues](#general-sleuth-issues)
      - [Spotlight Effect on Firefox](#spotlight-effect-on-firefox)
      - [Syntax error due to `console.log()`](#syntax-error-due-to-consolelog)
      - [Function parentheses](#function-parentheses)
      - [Variable assignment](#variable-assignment)
    - [Rookie](#rookie)
      - [101, Stage 3](#101-stage-3)
      - [201, Stage 4](#201-stage-4)
    - [Pro](#pro)
      - [601, All stages](#601-all-stages)
      - [601, Stage 4](#601-stage-4)
      - [701, All stages](#701-all-stages)
      - [701, Stage 4](#701-stage-4)
      - [702, All stages](#702-all-stages)
      - [702, Stage 1](#702-stage-1)
      - [702, Stage 2](#702-stage-2)
      - [702, Stage 4](#702-stage-4)
      - [801, All stages](#801-all-stages)
      - [801, Stage 3-4](#801-stage-3-4)
      - [801, Stage 4](#801-stage-4)
      - [802, Stage 1](#802-stage-1)
      - [802, Stage 2](#802-stage-2)
        - [Random function](#random-function)
      - [802, Stage 3](#802-stage-3)
      - [802, Stage 4](#802-stage-4)
  - [Game Project](#game-project)
    - [Audio](#audio)
      - [AudioContext not allowed to start](#audiocontext-not-allowed-to-start)
      - [Audio resources not loading](#audio-resources-not-loading)
  - [Coursera Material](#coursera-material)
    - [Week 1](#week-1)
      - [Video: 2D coordinate system](#video-2d-coordinate-system)
    - [Week 3](#week-3)
      - [Practice quiz: Using the console and debugging syntax errors](#practice-quiz-using-the-console-and-debugging-syntax-errors)
    - [Week 7](#week-7)
      - [Lesson 4.1 Video: Conditional statements using ==](#lesson-41-video-conditional-statements-using-)
      - [Lesson 4.2 Practice quiz: Introducing types: String, Number, Boolean](#lesson-42-practice-quiz-introducing-types-string-number-boolean)
      - [Practice quiz: Conditionals with types](#practice-quiz-conditionals-with-types)

---

# ITP1 - Reported problems, tips and additional instructions

This page is about the [Introduction to programming I module](../../../modules/level_4/introduction_to_programming_i/).

## Sleuth

### General Sleuth Issues

#### Spotlight Effect on Firefox

Be aware that Sleuth cases involving a spotlight effect (302 and 801) will not work on Firefox out of the box, like they work in any webkit based browser (like Google Chrome and Safari).

Easiest workaround is commenting out the line at the bottom that says `blendMode(DARKEST)` and uncommenting it again before submitting the case. Changing it to `blendMode(LIGHTEST)` should work at least to be able to see where the spotlight is.

#### Syntax error due to `console.log()`

If you get this message when submitting a case:

    There is an error in your code ...
    Error in compile SyntaxError: Unexpected token )

Remove all of your debugging statements that are using `console.log()`.

#### Function parentheses

If you get this message when submitting a case:

    TypeError: studentFunctionCodeString.search is not a function

You need to ensure that any function being declared does not have a space between the function name and the argument. For example:

    function myFunc() // Grader should accept this
    function myFunc () // Grader might not accept this

#### Variable assignment

- Some cases ask to set the value of a variable to `mouseX` for instance and then make sure it doesn't go above or below a certain value with `min()` and `max()` functions. Answers can wrongly be accepted if you first set

      variable = mouseX;

  and then reassign it by applying a function that is missing a parameter:

      variable = max(X);

  where `X` is an integer. The variable should be assign in one statement as follow instead:

      variable = max(mouseX, X);

### Rookie

#### 101, Stage 3

Use only `fill()` and `rect()` commands. You can adjust opacity with `fill()` by adding a fourth value as follows:

    fill(R, G, B, A);

where `R`, `G` and `B` stand for **red**, **green**, **blue** and can have values from 0 to 255 and `A` is optional **alpha**. In this case, a value of about `100` is fine so you can see through the shape being drawn.

#### 201, Stage 4

- Some students were given cases where body parts of the judge are missing (i.e., legs appear outside the canvas, for instance). In those cases, you may be better off just failing all your attempts and wait for a new randomized case to be given to you as you probably won't be able to get 100%.
- If your answer isn't accepted, try increasing the number of times you have `vertex()` in your code. Answers including at least 40 to 50 vertices have been reported to work better.
- You should only use `beginShape()`, `vertex(x1, y1)` and `endShape()` in your code.
- Note that `endShape()` stops drawing at the last vertex, but with parameter `CLOSE`, it closes the shape by drawing to the first vertex.

---

### Pro

#### 601, All stages

When required to draw at the various locations of crimes and sightings, take note of the following:

- When asked to draw vertices, at least one vertex must be drawn on the exact co-ordinate. Any number of vertices > 1 can be drawn to get the grader to accept the submission.

- Other shapes like rectangles and triangles can be drawn around the exact co-ordinate (i.e. no edges passing through it or ending on it) provided that they are smaller than approx 10-15 px in diameter.

- The names of array that need plotting may not always match up with the type of crime that is specified, for example, the instructions may refer to thefts, but the array might be called MurderSceneRecord.

- When asked to use `stroke(r,g,b)`, also use `noFill()` and when asked to use `fill(r,g,b)` also use `noStroke()`. Even though these functions are not allowed according to the instructions, the grader appears to need them to correctly assess the stroke and fill properties.

- When asked to draw rects around a point, do not use `rectMode(CENTER)` as it may confuse the grader. Simply use `rect(x-5, y-5, 10, 10)` or similar.

#### 601, Stage 4

Where possible matches need to be pushed into a separate array after comparing dates and distances, take note that some conditions could be too strict resulting in zero matches, which could at first seem like an error in your code. In such cases, if you submit, the grader will accept the empty array as long as the logic was implemented correctly.

#### 701, All stages

Witnesses sometimes give details relating to features or characteristics for which no properties are defined in the object arrays. It is usually not required to check for these. If problematic, get suspended to get a new case.

#### 701, Stage 4

Some versions of this stage have misspelled words which prevent the student from solving the case. If you encounter the words `plasic` or `nerveous`, you need to make sure that your solution searches for `plastic` or `nervous` instead. Some other variations along those lines with other misspelled words may exist but haven't been reported yet.

#### 702, All stages

Probably the trickiest of all the Sleuth cases. Instructions are not always explicitly clear and require insight into objects and functions.

#### 702, Stage 1

There is a bug in the instructions, stating that you need to:
`Get your car on the road by completing the </DRIVE_NAME/> function below.`

The function that requires editing is called `Move_Car()` (or similar).

#### 702, Stage 2

Hardest part is to implement the function to check/search a vehicle ahead by comparing the passed variable's (detective car object) distance/km/miles property against the ones in the array. There are several ways to do this, but the grader may not always like what you're doing. Some guidance here:

You need to check each object in the array to confirm using if-statement(s) that:

- They are in the same lane (easy, as per the instructions)
- That the difference between the distance/km/miles-properties of the car ahead and the detective vehicle less than 200
- That the car in the array is in front of (and not behind) the detective car

Note that the `distance`/`km`/`miles_travelled` property is increasing towards the top of the screen, opposite to the regular y-coordinate. Since debugging the array might be tricky, consider adding a text readout to each car using a variation of:

    text(Vehicles[i].Distance, Vehicles[i].X, Vehicles[i].Y); //debug

Once implemented correctly, remember the logic, as you will likely need to create similar functions things in the stages ahead.

#### 702, Stage 4

_"My suspect's car didn't have enough space to pull out in front of me before speeding off, so the chase wouldn't work as expected. I deliberately got myself suspended so I could grab another case, and it worked fine."_ (reported by [@dannycallaghan](https://github.com/dannycallaghan))

#### 801, All stages

More spotlight stages, which may cause Firefox users to not see the spotlights.
To get it to work, refer to [Spotlight effect on Firefox](#spotlight-effect-on-firefox).

**Tips:**

- The 1st seat in the 1st row will be `seats[0][0]`.
- Rows and seats relate to `seats[row][seat]` and not vice versa.
- You don't need to factor in reverse counting of rows such that row numbers increase from front to back, like in a real theatre. For this case the first row is at the back of the theatre (i.e. the top of the screen.)

#### 801, Stage 3-4

Many students waste time here trying to spot patterns in the audience members based on their appearance. The information about the seat numbers of gang/perpetrators is already defined in an array. It appears that any information given about appearance (hats, retro glasses, etc.) is merely to confirm that you have used the array to traverse the seats in the correct manner and not to actually identify gang members.

#### 801, Stage 4

Here the challenge is to traverse a two-dimensional array using a normal (one-dimensional) array. There are different ways to approach this, but these work:

- Create additional variables and use a nested-for with conditionals, or
- convert the 1D array to a 2D array and compare against the 2D array.

It appears that the grader is looking for two simple nested for-loops in the solution, so more elegant ways involving math to convert your 1D iterator into two 2D co-ordinates does not work, even when all gang members are correctly identified. This, for example, was not accepted by the grader:

    for (var i = 0; i < suspect.length; i++)
    operaFolks[floor(i/10)][i%10].recognised = (suspect[i]);

#### 802, Stage 1

**Tip:** You can comment out the line `if (frameCount % 7 == 0)` in order to speed up the deck spread sequence. It might save some time during testing.

#### 802, Stage 2

##### Random function

_"They ask you to create an array of random integers between two values. The `random()` function in `p5.js` includes the lower number, but excludes the upper number. So if you do `random(5,9)`, it might well generate a 5, but never a 9._

_I incremented the upper value by one so it'd actually generate values between the two numbers requested, but the puzzle actually expects you to just naively slot the two values into random and not fix the bug."_ (reported by _Peter Houlihan_)

#### 802, Stage 3

Tip: When comparing cards, you can't simply compare objects against each other as the objects may be structured differently. Rather consider the properties of the different objects in the arrays and compare similar properties against one another.

#### 802, Stage 4

- Take a good look at some form of documentation to understand how the JavaScript `splice()` function works. [MDN `Array.splice()` documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)

- From the instructions and the variable names, it is not always clear which part of the deck the grader wants in the spliced array. Other versions may exist, but it appears that the objective is to splice the part of the deck that would remain on the table (after it was cut) into a new array. In some cases that new array is called `topOfDeck` which is incredibly confusing, because it is actually the bottom part of the deck we are looking for. The top card lying on the remaining part of the deck must be the target card.

- When testing the reverse operation, take note that the console in Firefox Developer Edition and some other browsers may display object data live at the time of viewing it and not at the time of logging. This could create the impression that your array operations are not working. To see the array values at the time of logging them, do not use `console.log(obj)`, but use `console.log(JSON.parse(JSON.stringify(obj)))` instead.

---

## Game Project

### Audio

#### AudioContext not allowed to start

When implementing audio on your project, you could get an error similar to this from the browser:

`The AudioContext was not allowed to start. It must be resumed (or created) after a user gesture on the page.`

This is just a browser feature to prevent websites from playing sounds without user input. Ensure that your user presses a button or clicks the mouse before you attempt to play audio.

Refer to: https://developers.google.com/web/updates/2017/09/autoplay-policy-changes#webaudio

#### Audio resources not loading

Some users have reported CORS-related problems when trying to launch the audio template provided. This could occur on the `file:///` protocol due to [Cross-Origin policy restrictions](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS). Ensure that you launch the `index.html` file from a local web server and not through a file explorer.

Alternatively you can use the live preview functions of Brackets or the [Live Server extension](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) in VSCode.

These functions will automatically create a local server for testing and you can confirm this by checking that the address in your browser address starts with `localhost` or `http://` and not `file:///`

---

## Coursera Material

### Week 1

#### Video: 2D coordinate system

- At 3:56, the top left corner should have coordinates (4, 3) instead of (5, 3).
- At 3:56, the width of the rectangle should be 12, and not 11.

### Week 3

#### Practice quiz: Using the console and debugging syntax errors

- Question 3: "triangle" is misspelled → `trinagle`, adding an additional error which is not an argument error. However, the spelling mistake shouldn't be taken into account.

### Week 7

#### Lesson 4.1 Video: Conditional statements using ==

- The bomb exercise template is missing.

#### Lesson 4.2 Practice quiz: Introducing types: String, Number, Boolean

- Question 5: The question asks for **two** ways to reuse the variable `numWays` but expects **three** selected answers.

#### Practice quiz: Conditionals with types

- Question 3: The question says the answer _"No, because answer is neither a number, nor is it equal to the number 42"_ is correct. However the correct answer is _"Yes, because answer is equal to 42"_.
- Question 5: The question says the answer `parseInt(a+b)*c` is correct and the others are all wrong: however `(a+b)*c` is also correct. They both produce the same result.
