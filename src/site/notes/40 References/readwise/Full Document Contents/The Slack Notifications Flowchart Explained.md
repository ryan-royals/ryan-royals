---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/the-slack-notifications-flowchart-explained/","tags":["rw/articles"]}
---

![rw-book-cover](https://magicbell.com/api/og-images?url=https://magicbell.ghost.io/content/images/2020/11/C6ROe0mU0AEmpzz--1-.jpeg)

In just a few short years, [Slack](https://slack.com/) has gone on to become an indispensable work tool in our always-on often mobile work life.

A big part of the workflow improvements they offer is the fine-grained control of notifications you receive from them. Not only can you choose to be notified on email, desktop and mobile, but you can also set a notification schedule and adjust intervals between getting the same [Slack notification](https://www.magicbell.com/blog/what-are-slack-notifications) on the desktop and on your mobile.

This is a complex problem to solve engineering-wise. A few years back, [Slack shared the flowchart](https://slack.engineering/reducing-slacks-memory-footprint/) of how they decided to notify you.

Let's dissect that flowchart in this article.

##### Channel Notifications

You can be notified for messages on the channels you are part of, unless you mute a channel.

![](https://magicbell.ghost.io/content/images/2020/11/image-4.png)
That's the first thing Slack checks in its flowchart.

![](https://magicbell.ghost.io/content/images/2020/11/image-2.png) Check if the user has muted the channel
##### Do not disturb (DnD)

The next thing they check is if the user has enabled DnD. Users can enable it at any time or setup a schedule to toggle DnD automatically.

![](https://magicbell.ghost.io/content/images/2020/11/2020-09-07-at-3.06-PM.png) Slack users can mute their notifications
However, Slack also offers the sender an option to override your DnD setting, thereby resulting in the next section of the Flowchart

![](https://magicbell.ghost.io/content/images/2020/11/image-3.png) Check if the user has setup DnD and if the send overrode DnD
If you are not in DnD or if DnD was ignored by the sender, Slack checks if this message is in fact a @channel, @everyone or @here mention and if you have disabled notifications for those (for this channel).

![](https://magicbell.ghost.io/content/images/2020/11/image-1.png) You can stop @channel/@here from being mentions for you
This is checked in the next part of the flowchart

![](https://magicbell.ghost.io/content/images/2020/11/image-5.png) Check what kind of mention this is and if it should create a notification
Notice the part about this message being part of a thread? Slack let's you set a global preference for notifying you of replies to threads

![](https://magicbell.ghost.io/content/images/2020/11/image-6.png) A global preference for replies in threads you are following
However, it's interesting that even if this setting is turned on but you have disabled notifications entirely for the channel, you won't get notified. See this part of the Flowchart (the leftmost branch leads you to the big RED NO).

![](https://magicbell.ghost.io/content/images/2020/11/image-7.png) The channel preference overrides the global thread notification preference
##### Mobile-specific notification preferences

Before we go on any further, let us talk about Slack's ability to set a different preference for mobile notifications. They allow you to do this globally, as well as per channel. It looks something like this:

![](https://magicbell.ghost.io/content/images/2020/11/image-9.png)
Assuming that the *notification candidate* has made it so far (and so have you!), Slack checks for mobile-specific notification preference for this channel. If none has been set up, they check if you have a preference globally.

![](https://magicbell.ghost.io/content/images/2020/11/Screen-Shot-2020-09-07-at-3.22.12-PM.png) Check if a mobile-specific notification preference exists for this channel or globally
If you have chosen not to be notified of anything, it's a straight line to the big RED NO. However, if you have chosen to be notified, based on your preferences, you may lead down to the big GREEN YES. However, you may reach here on the desktop or on the mobile. In the Flowchart, they talk about checking for "past mobile push timing threshold", but I wasn't able to find this as an option in their UI. Perhaps this is something to check for in their backend without it being a user-adjustable property.

As you can see, building a sophisticated notification system is fairly complex. It doesn't have to be. [MagicBell](https://www.magicbell.com/) can take care of all of this for you while you focus on the core functionality of your product.

Here is a quick [Slack integration](https://www.magicbell.com/docs/slack) tutorial in case you'd like to add Slack notifications to your product.

Some content could not be imported from the original document. [View content ↗](https://www.youtube.com/embed/HNj0fMp8DyY?feature=oembed)
