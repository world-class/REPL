[Go back to the main page](https://github.com/world-class/REPL)

# Slack
# Table of contents
<!-- vim-markdown-toc GFM -->

* [Slack app integrations](#slack-app-integrations)
    * [Calendar Linker Bot](#calendar-linker-bot)
    * [Deadline Manager Bot](#deadline-manager-bot)
    * [GreetBot](#greetbot)
    * [Resource Locator Bot](#resource-locator-bot)

<!-- vim-markdown-toc -->

## Slack app integrations
### Calendar Linker Bot
Access it on Slack by typing `/cal`. This app currently displays the following information:
```
Hey {{username}}, here's a UoL calendar for you :simple_smile:.

• Not logged in with a Google account? → <https://calendar.google.com/calendar/embed?src=pmaaof55arb3aku90d2n5bhasg%40group.calendar.google.com|View calendar here>

• Logged in with a Google account? → <https://calendar.google.com/calendar/r?cid=cG1hYW9mNTVhcmIzYWt1OTBkMm41Ymhhc2dAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ|View calendar here>
```

### Deadline Manager Bot
This bot will automatically post events from the same calendar used by **Calendar Linker Bot** on the day and time they occur to the `#general` channel. The current formatting is as follow:
```
:newspaper: *{{summary}}*
:timer_clock: `{{start_dateTime_pretty}}`
:speech_balloon: *Additional details*
>>> {{description}}
```

### GreetBot
[GreetBot](https://greet.bot/) welcomes new students joining the workspace to guide them on their journey from the very beginning by pointing them to this repository and other useful resources. Right now, the custom message sent by the bot is as follow:
```
Hey @new_user_name! Welcome aboard. Here are the key points you will want to know to get started:

- *Reply using threads* to keep things neat instead of posting to the channel. :thumbsup:
- Make sure to read the *Programme Regulations* and the *Guidelines for Examinations*: https://london.ac.uk/sites/default/files/regulations/progregs-computer-science-2019-2020.pdf and https://london.ac.uk/sites/default/files/examiners/guidelines-for-examinations-2018-19.pdf
- *Post in the relevant channels*. For example, discrete maths questions should go in #cm1020-discrete-math. Use #april2019batch or #october2019batch for cohort specific discussion instead of #general.
- *Make sure a channel doesn't already exist* before creating another one with the same purpose. If you are going to invite only a limited number of students on a topic that doesn't concern necessarily everyone or if you need to collaborate in a *private group work*, you can do so by creating a *private channel* instead of a public one.
- Find a curated list of course related resources here: https://github.com/world-class/REPL
- Remember to check the *pinned messages* in each channel: you'll find relevant information. More on how "pins" work here: https://slack.com/help/articles/205239997
- Send yourself a direct message by typing `/resources` to display a *ton of useful resources*.
- Send yourself a direct message by typing `/cal` to display links to a Google Calendar to see *events related to this degree*.
- Please do your own research (Slack, search engine, etc.) *before asking a question* that has been answered many times. For a start, make sure you have read all the documents you will find on that page: https://github.com/world-class/REPL#documents-and-resources-provided-publicly-by-the-university-of-london
- Don't forget the *_Search_ feature* available on Slack: You can search for specific keywords, for messages from a specific user (*from:@username*), in different channels, by files, within certain dates, etc. More details are available here: https://slack.com/help/articles/202528808-search-in-slack

We hope you'll have a great time here, but please take some time to familiarize yourself with all the basic stuff before asking what has been asked over and over again: you can search on Slack and visit the above resources whenever you want. Succeeding as a CS student has a lot to do with being able to find answers on your own :bulb:.

On that note, be well and again, welcome home :slightly_smiling_face:!
```

### Resource Locator Bot
Access it on Slack by typing `/resources`. This app currently displays the following information:

```
Dear {{username}}, you might be interested in checking out the following *resources* to help you with your studies :simple_smile:.

• <https://github.com/world-class/REPL/blob/master/kinks/README.md|Lists of bugs for the different modules>
• <https://github.com/world-class/REPL/tree/master/modules|Info specific for each module>
• Don't forget to check out the right *channels on Slack* that will be best suited to help you!
→ *Modules Level 4*: #cm1005-intro-prog-i, #cm1010-intro-prog-ii, #cm1015-numerical-math, #cm1015-sample-paper, #cm1020-discrete-math, #cm1025-fundamental-cs, #cm1030-hcw, #cm1035-algos-data-i, #cm1040-web-dev
• Other _main_ Slack channels to find *help* and *resources*: #bookworm, #bugs, #channel-discovery, #cs-professionals, #free-stuff, #general, #linux, #live-sessions, #maths, #newbies, #notes, #open_source_collaborations, #random, #resources, #reviewexchange, #studytips_and_tools, #vent
• *UoL calendar* with *week number*, *deadlines*, etc. (*without* <https://calendar.google.com/calendar/embed?src=pmaaof55arb3aku90d2n5bhasg%40group.calendar.google.com|Google account logged in>, *with* <https://calendar.google.com/calendar/r?cid=cG1hYW9mNTVhcmIzYWt1OTBkMm41Ymhhc2dAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ|Google account logged in>)
• *Online courses* (<https://github.com/world-class/REPL/blob/master/online_courses/free/README.md|free> and <https://github.com/world-class/REPL/blob/master/online_courses/paid/README.md|paid>) to supplement your learning
• <https://github.com/world-class/REPL/blob/master/books/README.md|Recommended books>, <https://github.com/world-class/REPL/blob/master/podcasts/README.md|Podcasts>, <https://github.com/world-class/REPL/blob/master/software/README.md|software>, <https://github.com/world-class/REPL/blob/master/websites/README.md|websites>, <https://github.com/world-class/REPL/blob/master/youtube/README.md|YouTube videos>
• <https://github.com/world-class/REPL/blob/master/after_uol/README.md|Next steps after this BSc>
• *New to Slack*? See <https://get.slack.help/hc/en-us/articles/201374536-Slack-keyboard-shortcuts|available shortcuts>, <https://get.slack.help/hc/en-us/articles/202288908-Format-your-messages|how to format your messages>, <https://slack.com/slack-tips/share-code-snippets|how to share snippets of code> (JavaScript, HTML, CSS, Python, C++, etc.) and the <https://get.slack.help/hc/en-us|Slack Help Center> for anything else

• *Want to make this message better and know (or want to know) something about GitHub*? You can <https://github.com/world-class/REPL/blob/master/slack/README.md|update this message here> by sending a _pull request_ and even <https://github.com/world-class/REPL|contribute to the main project here>!
Thank you, good luck and may this degree be as easy as Pi. :wink:
```
