---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/how-to-add-tasks-to-your-daily-notes-in-obsidian/","tags":["rw/articles"]}
---

![rw-book-cover](https://obsidian.rocks/wp-content/uploads/2022/09/glenn-carstens-peters-RLw-UC03Gwc-unsplash.jpg)

![Example of a bullet journal.](https://obsidian.rocks/wp-content/uploads/2022/09/glenn-carstens-peters-RLw-UC03Gwc-unsplash.jpg)

> This article is part of a series of tips on handling tasks in Obsidian. To see the full series, see [How to Manage Tasks in Obsidian](https://obsidian.rocks/how-to-manage-tasks-in-obsidian/).
> 
> 

Do you use Daily Notes in Obsidian? If so, have you ever thought about adding tasks to your Daily Notes?

I’ve kept a daily journal for over a decade now, and I find it tremendously helpful to look back on the progress I’ve made in both life and work.

But a lot gets lost between the lines of my journals. I often write about the progress I’ve made on a project, but as time goes on, I forget the details.

One way to add more context to your journals *without* adding any more work is to keep a log of your daily to-dos *inside* the journal.

#### Creating Tasks in Daily Notes

There are a couple of ways of handling tasks in tandem with Daily Notes. One way is to add tasks *directly* to your daily note. Then at the end of the day, if you have any tasks left, you move them over to the next day. That looks like this:

![A screenshot of a to-do list inside of a Daily Note.](https://obsidian.rocks/wp-content/uploads/2022/09/2022-09-21_09-06.png)
This is a good solution if you only have a few tasks to do every day. But this is not my favorite solution, because I tend to have *too many* tasks to manage them like this.

#### Logging Tasks to your Daily Notes

I prefer to plan my projects in their own “project” notes, and pull tasks into my Daily Note *after* they are completed, creating a “daily log” of my completed tasks.

Here’s what it looks like to include only your *completed* tasks within a Daily Note:

![An example of completed tasks showing up inside a Daily Note.](https://obsidian.rocks/wp-content/uploads/2022/09/2022-09-21_09-07.png)
You can create the tasks anywhere within your vault, and your Daily Note will find them as soon as you complete them. I like this, because it allows me to structure my projects however I like, and requires no extra work on my end. If a task is completed today, it will show up in my daily note.

And thanks to the Tasks plugin, this is super easy to do. Let me show you how.

##### Prerequisites

* **Enable** the Daily Notes plugin (included in Obsidian’s Core Plugins)

##### Using the Tasks Query Language

The tasks plugin includes a [query language](https://obsidian-tasks-group.github.io/obsidian-tasks/queries/) that allows you to pull in tasks based on whatever parameters you wish. You don’t have to be a programmer to do this, the query language is easy to understand, and doesn’t require any complex logic. In our case, we want to pull in *all tasks completed* on a certain day.

That query looks like this:

That’s all well and good, but we don’t want to have to manually type the date every day. That’s where the *Templates* plugin comes in.

The [Obsidian Templates plugin](https://help.obsidian.md/Plugins/Templates) allows you to automatically fill in dates. So we can use that to fill in the date for our task query. Here’s what my Daily Notes template looks like:

```
## Journal Entries
-

## Task Log
```tasks
done on {{date:YYYY-MM-DD}}
```
```

And just like that, every time you create a new Daily Note, it will automatically import all completed tasks for that day. This is the easiest way I’ve found to add tasks to your daily notes.

#### Join the Newsletter

Subscribe for more Obsidian tips and tricks.

We won't send you spam. Unsubscribe at any time.
