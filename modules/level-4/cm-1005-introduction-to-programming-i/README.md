[Go back to the main page](../../../README.md)

### Table of contents

- [Introduction to Programming I](#introduction-to-programming-i)
  - [Professor(s)](#professors)
  - [Topics covered](#topics-covered)
  - [Assessment](#assessment)
  - [Module specification](#module-specification)
  - [Recognition of Prior Learning](#recognition-of-prior-learning)
  - [Syllabus](#syllabus)
  - [Resources](#resources)
    - [Essential reading](#essential-reading)
    - [JavaScript](#javascript)
      - [p5.js - JavaScript library](#p5js---javascript-library)
      - [W3 Schools](#w3-schools)
    - [Kinks to be aware of](#kinks-to-be-aware-of)
    - [:heart: Notes](#heart-notes)
    - [On REPL (see relevant sections)](#on-repl-see-relevant-sections)
    - [Sleuth assignments](#sleuth-assignments)
      - [Tips & Tricks](#tips--tricks)
      - [Utils and aids (student created)](#utils-and-aids-student-created)
    - [The game project](#the-game-project)
    - [Text editor](#text-editor)
      - [Configuring VS Code (optional)](#configuring-vs-code-optional)
        - [Extensions](#extensions)
        - [p5.js autocompletion](#p5js-autocompletion)
        - [Conclusion](#conclusion)

---

## Introduction to Programming I

This module focuses on basic programming techniques. You'll learn
how to use the fundamental elements of computer programming such as
variables, conditionals, functions and loops. You'll learn how to
create interactive, graphical computer programs. You will also be
introduced to basic object-oriented programming techniques.

### Professor(s)

- Dr. Edward Anstead
- Dr. Simon Katan

### Topics covered

- Your development environment
- Drawing in 2D
- Variables, Objects and Interaction
- Conditional Statements
- Basic loops and arrays
- Traversing with for loops
- Functions
- Advanced loops and arrays
- Extending Objects
- Constructor functions

### Assessment

Coursework only (Type II)

### Module specification

- [Module specification (September 2020)](https://github.com/world-class/binary-assets/blob/master/modules/module-specification/CM1005_ITP1-Module-Spec.pdf)

### Recognition of Prior Learning

- At the time of this writing, you can apply for [automatic RPL](https://london.ac.uk/applications/how-apply/recognition-prior-learning/recognition-and-accreditation-prior-learning-3) for this module if you obtain the [IBM Applied AI Professional Certificate](https://www.coursera.org/professional-certificates/applied-artifical-intelligence-ibm-watson-ai). **Note:** If you don't have prior programming experience, the course offered by UoL is probably easier and the recommended way to go.

### Syllabus

- [Syllabus PDF (September 2020)](https://github.com/world-class/binary-assets/blob/master/modules/syllabi/Syllabus_CM1005_ITP1.pdf)

### Resources

#### Essential reading

_"There is no required textbook for this module. The module draws on number of different, largely web-based, public resources as well as the resources produced as bespoke material for this module. The programming language is Javascript, with the p5js library used for graphical and interactive programming functionality. The main external resource is the set of online tutorials available from: [https://p5js.org/learn/](https://p5js.org/learn/)."_

_"Specific readings for each topic are listed with direct links to free online resources that provide additional material on the topics of this course."_

#### JavaScript

##### p5.js - JavaScript library

- [p5.js](https://p5js.org/) - Official website to find [the reference guide](https://p5js.org/reference) and an [online editor](https://editor.p5js.org/) to practice. Next step: [p5.js libraries](https://p5js.org/libraries/).
  - [Examples](https://p5js.org/examples/) are also available to get started.
- [The Coding Train](https://www.youtube.com/user/shiffman/playlists) (playlists) - Channel from Daniel Shiffman, a board member of `p5.js`.

##### W3 Schools

- [JavaScript Array Iteration Methods](https://www.w3schools.com/js/js_array_iteration.asp) - Will help in making your code more concise and readable.

#### Kinks to be aware of

- [List of reported errors and bugs with the module](../../../kinks/level-4/cm-1005-introduction-to-programming-i/).

#### :heart: Notes

- Visit [this page of world-class/notes](https://github.com/world-class/notes/tree/master/level-4/introduction-to-programming-i).

#### On REPL (see relevant sections)

- [Podcasts](../../../podcasts/)
- [Websites](../../../websites/)
- [YouTube](../../../youtube/)

#### Sleuth assignments

##### Tips & Tricks

- Each case in Sleuth has four stages. You have a maximum of **FIVE** attempts for each 'stage'. Attempt a 'stage' when you are confident. If you make a mistake, you will get a pop-up explaining what requirement you hadn't met. But if you exhaust your five attempts, fret not because, after some downtime (about 24 hours), you will be able to solve a variation of the same stage again. This will not affect your grade, and only the highest grade is counted.
- Get familiar with finding precise coordinates in an image. If you are using VS Code, you can use the [Luna Paint](https://marketplace.visualstudio.com/items?itemName=Tyriar.luna-paint) extension to view image coordinates or use an image editor like [GIMP](https://www.gimp.org/).
- Practice all basic drawing functions with `p5.js` in the [online editor](https://editor.p5js.org/) before attempting to solve crimes.

##### Utils and aids (student created)

- JavaScript library with visual aids for solving case 202 stage 4 [utils4sleuth.js](https://gist.github.com/amilos/beb1eee1cbd334f1e9abca8c9772c725).
- Python program to create directories for Sleuth cases [Make-Sleuth-Folders.py](https://github.com/BlairCurrey/Make-Sleuth-Folders)

#### The Game Project

- Visit [this link](https://doc.gold.ac.uk/www/118/) to see some of the games created by previous students.

#### Text editor

- The recommended text editor for this module is **no longer** [Brackets](http://brackets.io/). More options available on the [free software page](../../../software/).
- **Note**: support for Brackets is ending on September 1, 2021. [VS Code](https://code.visualstudio.com/) is a good alternative.

##### Configuring VS Code (optional)

This section is optional but recommended for your sanity in the long run as `p5.js` will be used in a few modules across this degree. You can certainly use VS Code as is without the need to install further extensions, but the following may make your life easier.

###### Extensions

VS Code supports JavaScript and its ecosystem by default, but you may want to enable more functionality by installing the following extensions:

- [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) - starts a development server straight from Code, allowing you to preview your work in the browser as if it was hosted on a remote server. For installation instructions, see [this video](https://www.youtube.com/watch?v=y4qqQeUDCBQ)
- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
- [Path Intellisense](https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense) - auto-completes filesystem paths, for example when loading assets with p5.js

Once you've gained some experience and confidence, you may want to try these as well:

- [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner) - allows you to run snippets of JS and other languages straight from Code, provided that a suitable runtime is installed (eg. Node.js). This is useful for experimentation and for small projects
- [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) - checks for "[code lint](https://en.wikipedia.org/wiki/Lint_(software))" in JS. Requires [ESLint](https://eslint.org/) to be installed, and may require some configuration to conform with the style used in the course (for more information on using ESLint, see the [ESLint user guide](https://eslint.org/docs/user-guide/configuring/); for a sample configuration that's compatible with ITP1, see [here](https://gist.githubusercontent.com/morags/2d762fd51c5ea4d733756baaf20cc6cc/raw/4093a82e966b38a75ba32bc0f623d61412ee047c/.eslintrc.json))
- [Project Manager](https://marketplace.visualstudio.com/items?itemName=alefragnani.project-manager) - useful when you start working on several projects at a time

###### p5.js autocompletion

To enable autocompletion for p5.js in a beginner-friendly way, you can install the extension [p5.vscode](https://marketplace.visualstudio.com/items?itemName=samplavigne.p5-vscode). If you feel more adventurous and are looking for a challenge and some extra flexibility in your setup, please keep reading!

First install [Node.js](https://nodejs.org/en/). Node is a JS [runtime](https://en.wikipedia.org/wiki/Runtime_system) - a program that runs JS code. It's not entirely unlike your browser's JS engine - in fact, it is based on Chrome's [V8 engine](https://en.wikipedia.org/wiki/V8_(JavaScript_engine)) - but it's intended for servers and commandline programs rather than web pages. Its package manager, [npm](https://www.npmjs.com/), is useful for setting up JS projects of any scale, so it's a good tool to have if you're going to work with JS. When you install Node, make sure to choose the option "add to PATH", so you have Node and npm available throughout your system. Once Node and npm are installed, open Code and a commandline interface (`cmd.exe` or `powershell.exe` in Windows, `Terminal` in macOS), navigate to your project folder (eg. `Documents/Goldsmiths/ITP1/Game_project`) and follow these steps:

1. Type the following command into your commandline: `npm i --save-dev @types/p5` . This will tell npm to download type definitions for p5.js. You will notice that npm has created a `node_modules` folder and a couple of files, which it uses to track and manage downloaded packages; you needn't worry about those at the moment (for more information on npm, see the [npm Docs](https://docs.npmjs.com/cli/v7/commands/npm)).
2. In Code, create a new file with the following text, and save it to the project folder as `jsconfig.json`:

```json
{
  "compilerOptions": {},
  "exclude": ["node_modules"],
}
```

This will let Code know that you're working on a JS project and that it should expect some other configuration files like `globals.d.ts` to be present (for more configuration options, see the [jsconfig.json reference](https://code.visualstudio.com/docs/languages/jsconfig)).

3. Create another file with this text, and save it to the project folder as `globals.d.ts`:

```ts
import {  } from "./node_modules/@types/p5/global";
```

This will import the type definitions you just downloaded into the global scope, allowing Code to autocomplete all of p5's identifiers from anywhere in your code (for more information on `global.d.ts`, see the [TypeScript documentation](https://www.typescriptlang.org/docs/handbook/declaration-files/templates/global-d-ts.html); for more information on p5.js's modes, see [p5.js's Github wiki](https://github.com/processing/p5.js/wiki/p5.js-overview#user-content-instantiation--namespace)).

###### Conclusion

Congratulations! Now VS Code is all set up. Keep a copy of Code's [keyboard shortcut reference](https://code.visualstudio.com/docs/getstarted/keybindings#_keyboard-shortcuts-reference) handy, and you'll be a Code master in no time!
