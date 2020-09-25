# How to contribute to the REPL

REPL is a volunteer effort and we warmly welcome first time Git/GitHub users! We encourage you to pitch in and join the `#repl` channel in the :lock: [UoL Slack workspace](http://londoncs.slack.com/)!

**For a primer on how to use Git & GitHub**, please see the section [How to use Git/GitHub](#how-to-use-gitgithub) below.

Thanks! :heart: :heart: :heart:

The REPL Team

---

## Table of contents

- [How to contribute to the REPL](#how-to-contribute-to-the-repl)
  - [Table of contents](#table-of-contents)
  - [Before getting started](#before-getting-started)
    - [How to use Git/GitHub](#how-to-use-gitgithub)
    - [Cloning faster](#cloning-faster)
      - [A tiny bit of background on the structure of this repo](#a-tiny-bit-of-background-on-the-structure-of-this-repo)
      - [How to actually clone faster](#how-to-actually-clone-faster)
        - [Preferred way](#preferred-way)
        - [Other option](#other-option)
    - [A few words](#a-few-words)
  - [Code of Conduct](#code-of-conduct)
  - [I don't want to read this whole thing I just have a question!!!](#i-dont-want-to-read-this-whole-thing-i-just-have-a-question)
  - [How Can I Contribute](#how-can-i-contribute)
    - [Reporting Issues](#reporting-issues)
      - [Before Submitting An Issue](#before-submitting-an-issue)
      - [How Do I Submit A (Good) Issue](#how-do-i-submit-a-good-issue)
    - [Suggesting Enhancements](#suggesting-enhancements)
      - [Before Submitting An Enhancement Suggestion](#before-submitting-an-enhancement-suggestion)
      - [How Do I Submit A (Good) Enhancement Suggestion?](#how-do-i-submit-a-good-enhancement-suggestion)
    - [Your First Contribution](#your-first-contribution)
    - [Pull Requests](#pull-requests)
  - [Style Guides](#style-guides)
    - [Git Commit Messages](#git-commit-messages)
    - [Documentation Style Guide](#documentation-style-guide)

## Before getting started

### How to use Git/GitHub

Here are a couple of places where you will find useful resources:

- [Step-by-step guide to contributing on GitHub](https://www.dataschool.io/how-to-contribute-on-github/)
- https://github.com/world-class/REPL/blob/master/websites/README.md#git--github
- https://github.com/world-class/REPL/blob/master/youtube/README.md#git--github
- https://github.com/world-class/REPL/tree/master/online_courses/free#git--github

### Cloning faster

#### A tiny bit of background on the structure of this repo

At the time of this writing, cloning this repository means having to download less than ~200 MB of data. This is getting _a bit_ heavy, but this should still be very much acceptable for most users given the following constraints:

- Those who end up contributing probably want most of the files anyways. What's heavy are a bunch of students notes and UoL PDFs. Adding to this, all modules are compulsory up to level 6 (therefore they are eventually useful to all students who wish to complete this degree), so we'll have figured something out by then. Modules at level 6 do not even exist right now :wink:.
- We are trying to keep things simple so that students who are new to Git and GitHub can get some practice with forking, cloning, creating branches, submitting pull requests, etc. There are better ways to deal with large binary files, but still internet connections are fast enough these days to watch HD videos which will consume much more bandwidth than this repo, which is basically a one-time thing only.
- By storing everything in one single repo for now, students are able to `pull` changes on their machine very easily without having to worry about missing something. From time to time, a script is executed to compress PDF files (which are the main culprits for the growing size of the repo), so that helps in a reasonable way too.

#### How to actually clone faster

If you already know [how to clone from the command line](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository), you'll be somewhat familiar with the following alternative (if not, you are highly encouraged to learn how to proceed as knowing Git will prove very useful to any computer science student). Without going into much details, here's what you can do to reduce the size of your clone by keeping revisions to the latest version of each file only. Your best bet should be to use `git clone --depth 1` for now.

##### Preferred way

If you use HTTPS (simpler way):

    git clone -–depth 1 "https://github.com/world-class/REPL.git"

If you use SSH (needs to be configured on GitHub):

    git clone -–depth 1 "git@github.com:world-class/REPL.git"

##### Other option

You can also make sure to keep references only to the `master` branch to save some additional space if more branches get created. Again, use either HTTPS or SSH depending on your setup.

> **Note:** Because this repo usually contains only the `master` branch, this method won't get you far in this particular instance.

With HTTPS:

    git clone https://github.com/world-class/REPL.git --branch master --single-branch REPL

With SSH:

    git clone git@github.com:world-class/REPL.git --branch master --single-branch REPL

### A few words

:+1::tada: First off, thanks for taking the time to contribute! :tada::+1:

The following is a set of guidelines for contributing to REPL, which is hosted in the [World Class
Organization](https://github.com/world-class) on GitHub. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## Code of Conduct

This project and everyone participating in it is governed by the [REPL Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project team in the `#repl` channel in the :lock: [UoL Slack workspace](http://londoncs.slack.com/).

## I don't want to read this whole thing I just have a question!!!

> **Note:** Please don't file an issue to ask a question. You'll get faster results by using the resources below.

We have [an official FAQ](./FAQ/) with helpful advice if you have questions.

If chat is more your speed, you can join the REPL Slack team:

- Join the `#repl` channel in the :lock: [UoL Slack workspace](http://londoncs.slack.com/).
- Even though Slack is a chat service, sometimes it takes several hours for community members to respond &mdash; please be patient!
- Use the `#repl` channel for general questions or discussion about REPL.

## How Can I Contribute

### Reporting Issues

This section guides you through submitting a bug/problem report for REPL. Following these guidelines helps maintainers and the community understand your report :pencil:, reproduce the behavior :computer: :computer:, and find related reports :mag_right:.

Before creating bug reports, please check [this list](#before-submitting-an-issue) as you might find out that you don't need to create one. When you are creating a bug report, please [include as many details as possible](#how-do-i-submit-a-good-issue).

> **Note:** If you find a **Closed** issue that seems like it is the same thing that you're experiencing, open a new issue and include a link to the original issue in the body of your new one.

#### Before Submitting An Issue

- **Perform a [search](https://github.com/search?q=+is%3Aissue+user%3AREPL)** to see if the problem has already been reported. If it has **and the issue is still open**, add a comment to the existing issue instead of opening a new one.

#### How Do I Submit A (Good) Issue

Bugs are tracked as [GitHub issues](https://guides.github.com/features/issues/). Create an issue and provide the following information.

Explain the problem and include additional details to help maintainers reproduce the problem:

- **Use a clear and descriptive title** for the issue to identify the problem.
- **Describe the exact steps which reproduce the problem** in as many details as possible. When listing steps, **don't just say what you did, but explain how you did it**. For example, if you moved the cursor to the end of a line, explain if you used the mouse, or a keyboard shortcut and if so which one?
- **Provide specific examples to demonstrate the steps**. Include links to files or GitHub projects, or copy/pasteable snippets, which you use in those examples (_if applicable_). If you're providing snippets in the issue, use [Markdown code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines).
- **Describe the behavior you observed after following the steps** and point out what exactly is the problem with that behavior.
- **Explain which behavior you expected to see instead and why.**
- **Include screenshots and animated GIFs** which show you following the described steps and clearly demonstrate the problem. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux.

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for REPL, including completely new features and minor improvements to existing functionality. Following these guidelines helps maintainers and the community understand your suggestion :pencil: and find related suggestions :mag_right:.

#### Before Submitting An Enhancement Suggestion

- **Perform a [search](https://github.com/world-class/REPL/issues?q=is%3Aissue)** to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.

#### How Do I Submit A (Good) Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](https://guides.github.com/features/issues/). Create an issue and provide the following information:

- **Use a clear and descriptive title** for the issue to identify the suggestion.
- **Provide a step-by-step description of the suggested enhancement** in as many details as possible.
- **Provide specific examples to demonstrate the steps**. Include copy/pasteable snippets (_if applicable_) which you use in those examples, as [Markdown code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines).
- **Describe the current behavior** and **explain which behavior you expected to see instead** and why.
- **Include screenshots and animated GIFs** (_if applicable_) which help you demonstrate the steps or point out the part of REPL which the suggestion is related to. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux.
- **Explain why this enhancement would be useful** to most REPL users.
- **List some other sources where this enhancement exists** if it helps.

### Your First Contribution

Unsure where to begin contributing to REPL? You can start by looking through the issues with the label `good first issue`.

### Pull Requests

The process described here has several goals:

- Maintain REPL's quality
- Fix problems that are important to users
- Engage the community in working toward the best possible REPL
- Enable a sustainable system for REPL's maintainers to review contributions

Please follow these steps to have your contribution considered by the maintainers:

1. Follow all instructions in [the template](PULL_REQUEST_TEMPLATE.md)
2. Follow the [style guides](#style-guides)

While the prerequisites above must be satisfied prior to having your pull request reviewed, the reviewer(s) may ask you to complete additional design work, tests, or other changes before your pull request can be ultimately accepted.

## Style Guides

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

### Documentation Style Guide

- Use [Markdown](https://daringfireball.net/projects/markdown) and update table of contents when links are changed (if you remember and assuming you've read this far :wink:).

---

_Those guidelines are adapted from [Ruby on Rails](https://github.com/rails/rails/blob/master/CONTRIBUTING.md) and [Atom](https://github.com/atom/atom/blob/master/CONTRIBUTING.md) projects._
