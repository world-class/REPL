[Go back to the main page](../README.md)

# How to contribute to the REPL

REPL is a volunteer effort and we warmly welcome first time Git/GitHub users! We encourage you to pitch in and join the `#repl` channel in the :lock: [UoL Slack workspace](http://londoncs.slack.com/)!

**For a primer on how to use Git & GitHub**, please see the section [How to use Git/GitHub](#how-to-use-gitgithub) below.

Thanks! :heart: :heart: :heart:

The REPL Team

---

**Table of contents:**

- [How to contribute to the REPL](#how-to-contribute-to-the-repl)
  - [Essential reading](#essential-reading)
    - [What contributions are accepted](#what-contributions-are-accepted)
  - [Optional but still recommended reading](#optional-but-still-recommended-reading)
    - [How to use Git/GitHub](#how-to-use-gitgithub)
    - [Code of Conduct](#code-of-conduct)
    - [How Can I Contribute](#how-can-i-contribute)
      - [Reporting Issues](#reporting-issues)
        - [Before Submitting An Issue](#before-submitting-an-issue)
        - [How Do I Submit A (Good) Issue](#how-do-i-submit-a-good-issue)
      - [Suggesting Enhancements](#suggesting-enhancements)
        - [Before Submitting An Enhancement Suggestion](#before-submitting-an-enhancement-suggestion)
        - [How Do I Submit A (Good) Enhancement Suggestion](#how-do-i-submit-a-good-enhancement-suggestion)
      - [Your First Contribution](#your-first-contribution)
      - [Pull Requests](#pull-requests)
    - [Style Guides](#style-guides)
      - [Git Commit Messages](#git-commit-messages)
      - [Documentation Style Guide](#documentation-style-guide)

## Essential reading

**Have questions?**

- We have [an official FAQ](../faq/README.md) with helpful advice.
- Join the `#repl` channel in the :lock: [UoL Slack workspace](http://londoncs.slack.com/).

### What contributions are accepted

- **No binary files** (PDFs, images, etc.) or generally **anything above 100 KB** in size should be committed directly to this repository. If you would like to reference a large file in your contribution, please send an additional contribution to either the **[notes](https://github.com/world-class/notes)** or **[binary-assets](https://github.com/world-class/binary-assets)** repositories so we can keep this one as light as a feather.
- **Improvements to any existing page** are welcome. For something more substantial than a few additions or fixing a typo (such as creating a new section or something above, say, 500 words), please [open a new issue](https://github.com/world-class/REPL/issues/new/choose) to discuss it or reach out on Slack in the `#repl` channel so we can be more efficient and respectful of everyone's time. This could include:
  - **Updating links** (broken, outdated documents, etc.).
  - **Adding missing files to [binary-assets](https://github.com/world-class/binary-assets)** (such as past exams, syllabi, module specifications, etc.).
  - **Answering new questions in the [FAQ](../faq/README.md).**
  - **Fixing formatting errors/issues and typos**.
  - Sharing something that was useful to you during your journey in this degree, such as **[books](../books/README.md)**, **[podcasts](../podcasts/README.md)**, **[websites](../websites/README.md)**, **[software](../software/README.md)** and so on.
- Besides the above points, anything you think would be useful to at least a handful students in this programme will be a strong candidate for being merged into the REPL _as long as it doesn't break any rules set by the university in any of their publicly available documents and isn't ethically dubious_ :wink:.

## Optional but still recommended reading

**A few initial words...**

:+1::tada: First off, thanks for taking the time to contribute! :tada::+1:

The following is a set of guidelines for contributing to REPL, which is hosted in the [World Class Organization](https://github.com/world-class) on GitHub. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

### How to use Git/GitHub

Here are a couple of places where you will find useful resources:

- [Step-by-step guide to contributing on GitHub](https://www.dataschool.io/how-to-contribute-on-github/)
- https://github.com/world-class/REPL/blob/master/websites/README.md#git--github
- https://github.com/world-class/REPL/blob/master/youtube/README.md#git--github
- https://github.com/world-class/REPL/tree/master/online_courses/free#git--github

### Code of Conduct

This project and everyone participating in it is governed by the [REPL Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project team in the `#repl` channel in the :lock: [UoL Slack workspace](http://londoncs.slack.com/).

### How Can I Contribute

#### Reporting Issues

This section guides you through submitting a bug/problem report for REPL. Following these guidelines helps maintainers and the community understand your report :pencil:, reproduce the behavior :computer: :computer:, and find related reports :mag_right:.

Before creating bug reports, please check [this list](#before-submitting-an-issue) as you might find out that you don't need to create one. When you are creating a bug report, please [include as many details as possible](#how-do-i-submit-a-good-issue).

> **Note:** If you find a **Closed** issue that seems like it is the same thing that you're experiencing, open a new issue and include a link to the original issue in the body of your new one.

##### Before Submitting An Issue

- **Perform a [search](https://github.com/search?q=+is%3Aissue+user%3AREPL)** to see if the problem has already been reported. If it has **and the issue is still open**, add a comment to the existing issue instead of opening a new one.

##### How Do I Submit A (Good) Issue

Bugs are tracked as [GitHub issues](https://guides.github.com/features/issues/). Create an issue and provide the following information.

Explain the problem and include additional details to help maintainers reproduce the problem:

- **Use a clear and descriptive title** for the issue to identify the problem.
- **Describe the exact steps which reproduce the problem** in as many details as possible. When listing steps, **don't just say what you did, but explain how you did it**. For example, if you moved the cursor to the end of a line, explain if you used the mouse, or a keyboard shortcut and if so which one?
- **Provide specific examples to demonstrate the steps**. Include links to files or GitHub projects, or copy/pasteable snippets, which you use in those examples (_if applicable_). If you're providing snippets in the issue, use [Markdown code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines).
- **Describe the behavior you observed after following the steps** and point out what exactly is the problem with that behavior.
- **Explain which behavior you expected to see instead and why.**
- **Include screenshots and animated GIFs** which show you following the described steps and clearly demonstrate the problem. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux.

#### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for REPL, including completely new features and minor improvements to existing functionality. Following these guidelines helps maintainers and the community understand your suggestion :pencil: and find related suggestions :mag_right:.

##### Before Submitting An Enhancement Suggestion

- **Perform a [search](https://github.com/world-class/REPL/issues?q=is%3Aissue)** to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.

##### How Do I Submit A (Good) Enhancement Suggestion

Enhancement suggestions are tracked as [GitHub issues](https://guides.github.com/features/issues/). Create an issue and provide the following information:

- **Use a clear and descriptive title** for the issue to identify the suggestion.
- **Provide a step-by-step description of the suggested enhancement** in as many details as possible.
- **Provide specific examples to demonstrate the steps**. Include copy/pasteable snippets (_if applicable_) which you use in those examples, as [Markdown code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines).
- **Describe the current behavior** and **explain which behavior you expected to see instead** and why.
- **Include screenshots and animated GIFs** (_if applicable_) which help you demonstrate the steps or point out the part of REPL which the suggestion is related to. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux.
- **Explain why this enhancement would be useful** to most REPL users.
- **List some other sources where this enhancement exists** if it helps.

#### Your First Contribution

Unsure where to begin contributing to REPL? You can start by looking through the issues with the label `good first issue`.

#### Pull Requests

The process described here has several goals:

- Maintain REPL's quality
- Fix problems that are important to users
- Engage the community in working toward the best possible REPL
- Enable a sustainable system for REPL's maintainers to review contributions

Please follow these steps to have your contribution considered by the maintainers:

1. Follow all instructions in [the template](PULL_REQUEST_TEMPLATE.md)
2. Follow the [style guides](#style-guides)

While the prerequisites above must be satisfied prior to having your pull request reviewed, the reviewer(s) may ask you to complete additional design work, tests, or other changes before your pull request can be ultimately accepted.

### Style Guides

#### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

#### Documentation Style Guide

- Use [Markdown](https://daringfireball.net/projects/markdown) and update table of contents when links are changed (if you remember and assuming you've read this far :wink:).

---

_Those guidelines are adapted from the [Ruby on Rails](https://github.com/rails/rails/blob/master/CONTRIBUTING.md) and [Atom](https://github.com/atom/atom/blob/master/CONTRIBUTING.md) projects._
