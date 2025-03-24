---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/how-i-track-my-tasks-in-obsidian/","tags":["rw/articles"]}
---

![rw-book-cover](https://miro.medium.com/1*m-R_BkNf1Qjr1YbyOIJY2w.png)

#### Two extensions that turn Obsidian into a task management powerhouse

![](https://miro.medium.com/v2/resize:fit:700/1*JnH8icF6dkXMjxrUom5O-g.png)My Obsidian App with the Tasks Dashboard in the lower right 
I’ve been using [Obsidian](https://obsidian.md/) to take all sorts of notes for work daily. I’ve been using it for a few months now. In creating a solid system for myself, I’ve created an excellent process for handling all my tasks for work.

### First, What is Obsidian?

[Obsidian](https://obsidian.md/) is a lightweight note-taking app that markets itself as “Your Second Brain.” And it lives up to the hype. It’s built using [Electron](https://www.electronjs.org/), a lightweight app framework that combines Chromium and NodeJs, resulting in a lightning-fast, cross-platform app. What makes the app appealing to many, besides its speed and features, is that you can keep the notes you create on your drive in the markdown file format. So unlike many other note-taking options, you can keep your data safe and local, and if the app were to disappear tomorrow, you still have your data. For developers reading this, it reminds me of early VSCode.

### My Task System

Like many others, I just started using Obsidian out of the gate with no real plan. Over time, I added daily notes and noticed what worked and what didn’t. I knew tasks had a place in this system, and this is the task system that has been working for me. The beauty of this system is that I do not have to worry about organizing my tasks in any particular note. Instead, I can add a task to any note. I can also add a hashtag and due date if I want to track them with some detail.

I have a simple *Tasks Dashboard* I keep pinned on the right of my app that keeps me up to date with everything I need to do, whether it’s due today or in the future.

I covered this slightly in my Daily Note article, but after refining it for a few weeks and sticking with it, I feel I can now safely recommend this approach.

[#### My Obsidian Daily Note Template

##### How I use Obsidian to track my day-to-day.

benenewton.medium.com](https://benenewton.medium.com/my-obsidian-daily-note-template-a4bdab53dc62)

#### My Task Types

I generally have two types of tasks, important tasks, and other tasks. Simply put, important tasks have a due date. Other tasks do not.

If I have a task due for work, which I have to complete by Friday, that’s an *important task*. Therefore, I want to track it based on that date. However, If I want to check my email before I log off for the day, that’s a regular task or classified as *other tasks*.

#### My Important Tasks

I use the extension, [Obsidian-tasks](https://github.com/schemar/obsidian-tasks) for tracking my important tasks. This extension allows me to add due dates as well as completion dates. I can use the GUI to add a task and use a keyboard shortcut to trigger it. I use **cmd-t** to create the task. The GUI allows me to add a due date using natural language, such as “Friday” or “Tomorrow.”

![](https://miro.medium.com/v2/resize:fit:700/1*f-5vgsRw3U38KtT5JLE3DQ.png)Add task modal using Obsidian-tasks. 
The extension creates a task in markdown with a due date prefixed with a calendar emoji. In addition, it adds the `#task` hashtag. This hashtag is how it finds tasks using the query tool. This hashtag’s value is configurable in the settings.

```
- [ ] #task Add new section Code Standards 📅 2021–06–25
```

When I mark it complete (**alt-enter**), the **x** is added, and the extension adds the completion date prefixed by a green check emoji.

```
- [x] #task Add new section to Code Standards 📅 2021–06–25 ✅ 2021–09–07
```

#### My Other Tasks

I add my other tasks that typically do not need a due date using plain markdown. There is no hashtag `#task` in the task, so they are not pulled into my *due today* or *past due* lists on the dashboard. They do, however, show up under my *Other Tasks* list.

```
- [ ] Check email before logging off
```

On my *Other Tasks* list, I can quickly look for anything that is not complete. In addition, I use templates to create my daily note, which contains “other tasks” for my “*start of the day”* and “*end of the day”* cleanup tasks. Having these available in my dashboard allows me to assess where I’m at in my day quickly. I usually start my day and finish my day here.

### Task Dashboard

![](https://miro.medium.com/v2/resize:fit:483/1*-3XKCDX--Vh21ejl3ChH2g.png)My Tasks Dashboard 
I aggregate all of these tasks in a note I keep pinned in preview mode on the bottom right of my Obsidian window. This note allows me to view what is due today, due this week quickly, past due, or has no due date. It also lists the *other tasks* at the bottom.

![](https://miro.medium.com/v2/resize:fit:700/1*p6-kxqt_Iw5kja6BDqwmsA.png)Placement of my Tasks Dashboard in the lower right of my Obsidian window 
I can mark the tasks complete from here, and they will disappear from the list. If it is an important task with the `#task` hashtag, it appends a completion date. Notice the hashtag `#task` does not show in preview mode.

They include a link so I can navigate directly to the note for any of the important tasks. I can hover over the link for a preview, and I can also edit the task right from the dashboard by clicking the pencil icon.

The tasks listed by due dates all use the query functions available from the obsidian-task extension. Here’s an example query of the important tasks using obsidian-tasks.

```
##### Due Today  
```tasks  
not done  
due today  
```
```

The other tasks query uses the [DataView](https://blacksmithgu.github.io/obsidian-dataview/) extension. This extension allows me to query only the tasks I want to see and excluded tasks included in certain notes and folders, like my templates folder. Again, the ability to fine-tune the query allows for a clean, proper list of tasks. Here’s an example of the other tasks query.

```
#### Other Tasks<pre class="dataview dataview-error">Evaluation Error: SyntaxError: Invalid or unexpected token
    at DataviewInlineApi.eval (plugin:dataview:18885:21)
    at evalInContext (plugin:dataview:18886:7)
    at asyncEvalInContext (plugin:dataview:18896:32)
    at DataviewJSRenderer.render (plugin:dataview:18922:19)
    at DataviewJSRenderer.onload (plugin:dataview:18464:14)
    at DataviewJSRenderer.load (app://obsidian.md/app.js:1:1214099)
    at DataviewApi.executeJs (plugin:dataview:19465:18)
    at DataviewCompiler.eval (plugin:digitalgarden:10760:23)
    at Generator.next (&lt;anonymous&gt;)
    at eval (plugin:digitalgarden:90:61)</pre>
```

Here is a gist of the source of my Tasks Note. Click view raw to copy and paste.

Some content could not be imported from the original document. [View content ↗](https://medium.com/geekculture/how-i-track-my-tasks-in-obsidian-47fd7ad80364) 

*One caveat to keep in mind - When using these queries containing “today,” it refers to the day you opened the App. If you leave your computer on overnight, it’s a good idea to close Obsidian and reopen it in the morning. I am going to set up a keyboard maestro macro to automate that.*

I’ve played with the idea of including these queries in my daily notes. My original [Daily Note article](https://benenewton.medium.com/my-obsidian-daily-note-template-a4bdab53dc62) included some of these queries, but I have found that this one pinned note off to the side is all I need to track my tasks. Everywhere else is just extra noise.

There is a multitude of options and queries I could build. However, I’ve settled on these over time. I have no real need to view tasks once they are complete, but you could base queries on the date completed if you need to keep track of that info. I find myself tweaking this regularly. I will follow up with where I’m at tracking these tasks in the future. I am sure there will be more extensions and more features to work with soon.

How are you tracking tasks with Obsidian? Or any other App? Let me know in the comments.

Some content could not be imported from the original document. [View content ↗](https://medium.com/geekculture/how-i-track-my-tasks-in-obsidian-47fd7ad80364)
