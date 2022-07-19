
# Table of contents

- [Table of contents](#table-of-contents)
- [Object Oriented Programming - Reported Problems](#object-oriented-programming---reported-problems)
  - [Week 18](#week-18)
    - [9.2 Adding a moveable playhead](#92-adding-a-moveable-playhead)
      - [9.207 - Implement A Timer](#9207-Implement-a-timer)
  - [Week 19](#week-19)
    - [Vector Subscript Out of Range](#vector-subscript-out-of-range)

# Object Oriented Programming - Reported Problems

This page is about the [Object Oriented Programming module](../../../modules/level-5/cm-2005-object-oriented-programming/).

## Week 18

### 9.2 Adding a moveable playhead

#### 9.207 Implement a timer

_"There's a nasty bug in week 18 video 9.207. When you load a file the application will crash. After a bit of detective work it turns out that as the timer is being called before a file is loaded, the position is NaN (not a number). I found a simple fix for this: "_ - Jamie Jackson

![Solution](https://github.com/world-class/binary-assets/blob/master/modules/cm2005-oop/bugs/bug_9.207.png?raw=true)

## Week 19

### 10.1 Starter Table Component

#### "Vector Subscript Out of Range"

"_If you try maximising the window you'll get a crash. Inspecting the error message it says vector subscript out of range. So I looked up the paintCell function in the juce API, it says in the description:_
> Note that the rowNumber value may be greater than the number of rows in your list, so be careful that you don't assume it's less than getNumRows().

_So a solution I came up with for the problem is to use getNumRows() and check if rowNum is less than it like in the image below._" - Jamie Jackson

![Solution](https://github.com/world-class/binary-assets/blob/master/modules/cm2005-oop/bugs/bug_10.107.png?raw=true)
