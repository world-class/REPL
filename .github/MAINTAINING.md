# Maintaining the REPL

This document is intended to help maintainers of the REPL.

## What is there to do?

The following are merely suggestions to be built upon. Feel free to [suggest new ideas](https://github.com/world-class/REPL/issues/new/choose)!

### I am a maintainer

- The [contributing guidelines](./CONTRIBUTING.md) list the main areas of maintenance.
- The start date of each new semester is added to [a script](../assets/scripts/update_week.py).
- New contributors are added to the contributors list.
  - [How to add a new contributor](https://allcontributors.org/docs/en/bot/usage).
  - [What type of contribution can be added](https://allcontributors.org/docs/en/emoji-key).
- Pull requests are merged.
- [Companion repositories](https://github.com/world-class) are kept-up-to-date.
- [Projects](https://github.com/orgs/world-class/projects/) are kept up-to-date as needed.
- Communication happens in known channels.
  - The `#repl` channel on Slack.
  - In [issues](https://github.com/world-class/REPL/issues).
- If I am actively willing to help maintain the REPL, I am [listed as a maintainer in the Maintainers team](https://github.com/orgs/world-class/teams/maintainers/members) so others know they can reach out to me.
  - In addition, the :construction: emoji is shown under my name in the contributors list (or removed, as needed).
    - Removing a contributor: Remove `maintenance` from under your name in `all-contributorsrc`, then let all-contributors clean up the README on the next use of the bot or delete the HTML by yourself in the README (careful with start/close tags in that case! You may want to double-check with a tool like https://validator.w3.org/).
    - Adding a contributor: e.g., comment `@all-contributors please add @maintainer for maintenance` in an issue or pull request.

### I am an owner

The same as a maintainer, plus:

- I can make sure that the [Maintainers team](https://github.com/orgs/world-class/teams/maintainers/members) is up-to-date.
- I can [create any team](https://github.com/orgs/world-class/teams) that is needed to split concerns, e.g. to manage a single repository.
- I can give `maintainer` access to other students as I see fit.
- After discussing with the other owners (the `#repl` channel on Slack is a good place to do so transparently), I can add new owners and remove inactive people as well (security!).
- I may enable/disable GitHub features as needed. For example, I may enable GitHub Discussions if the consensus is that it is a good idea.
- I can archive old and unused repositories if there's a need to keep things tidy.
- I can do evil things, but I won't. :wink:
