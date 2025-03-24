---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/streamline-your-day-enhance-focus-and-productivity-with-rescue-time-and-obsidian/","tags":["rw/articles"]}
---

![rw-book-cover](https://obsidian.rocks/wp-content/uploads/2023/07/markus-winkler-IrRbSND5EUc-unsplash-1.jpg)

If you work for or by yourself, it can be hard to stay productive.

It’s easy to get distracted, and hard to stay on track.

For many years now I have used [RescueTime](https://www.rescuetime.com/rp/ObsRocks) to help keep track of what I’m doing while I’m on the computer (it’s amazing how easy it is to lose track of time if you don’t).

RescueTime is great, but it’s easy to forget that you’re using it. Even if you check the dashboard every day, sometimes it feels a little too *fleeting*, wasting time doesn’t feel *painful* enough to me on the RescueTime dashboard.

So instead of using RescueTime exclusively, I found a way to integrate it into Obsidian.

Let me introduce you to the Obsidian RescueTime graph:

![A graph showing RescueTime productivity pulse over time in Obsidian.](https://i0.wp.com/obsidian.rocks/wp-content/uploads/2023/07/Screenshot-from-2023-07-07-15-11-05.png?resize=1024%2C592&ssl=1)
#### Showcasing your RescueTime progress in Obsidian

You may recognize this graph from my previous article, [Creating Dynamic Graphs in Obsidian](https://obsidian.rocks/creating-dynamic-graphs-in-obsidian/). But that article was meant to act as inspiration, not as instructions.

So today, I’d like to teach you how to build this graph in *your* Obsidian vault.

If that sounds interesting to you, then there are a few things you need to do first:

##### Prerequisites

In order to build the above chart, you need a couple of plugins:

* [Dataview](https://blacksmithgu.github.io/obsidian-dataview/)
* [Obsidian Charts](https://charts.phibr0.de/Meta/Charts/Obsidian+Charts+Documentation)

After installing these plugins, check your Dataview settings and ensure that “Enable JavaScript Queries” is turned ON. We’ll need that later.

You’ll also need to sign up for [RescueTime](https://www.rescuetime.com/rp/ObsRocks) and follow the instructions to install that on your computer.

> 
> Note: the RescueTime link above is an affiliate link, but I wrote this article before I knew they had affiliates! If you use the link it helps support my work. Otherwise feel free to find it on your search engine of choice.
> 
> 
> 

If you haven’t installed plugins before, see [How to use Community Plugins in Obsidian](http://community).

#### Set up

Install and enable the above plugins. In addition to that, you’ll also need to enable the *Daily Notes* core plugin. And you’ll need to create a *template* for your Daily Notes. There are [all sorts of things you can do with your Daily Notes template](https://obsidian.rocks/supercharge-your-daily-notes-in-obsidian/), but for our purposes, you only need one line, and it looks like this:

```
RT::0
```

* Create a file called “Daily Notes Template” and make sure it includes the above line.
* Then, in your Daily Notes settings, set the “Template file location” to your Daily Notes Template.

RT stands for “RescueTime”, and in order to use it you need to:

1. Create a daily note at the end of your work day
2. Check your RescueTime dashboard
3. Copy your Productivity Pulse from RescueTime to your Daily Note

Once you have your productivity pulse, enter it like this:

```
RT::72
```

After a day or two of doing this, then you will have the data required to create a graph.

#### Creating a graph for your Productivity Pulse

Once you have this data set up in your Daily Notes, all we have to do is find a way to use it.

Create another note called “Productivity Pulse”. This is where we will add our graph.

Copy this script into that note:

```
<pre class="dataview dataview-error">Evaluation Error: TypeError: window.renderChart is not a function
    at eval (eval at &lt;anonymous&gt; (plugin:dataview), &lt;anonymous&gt;:35:8)
    at DataviewInlineApi.eval (plugin:dataview:18885:16)
    at evalInContext (plugin:dataview:18886:7)
    at asyncEvalInContext (plugin:dataview:18896:32)
    at DataviewJSRenderer.render (plugin:dataview:18922:19)
    at DataviewJSRenderer.onload (plugin:dataview:18464:14)
    at DataviewJSRenderer.load (app://obsidian.md/app.js:1:1214099)
    at DataviewApi.executeJs (plugin:dataview:19465:18)
    at DataviewCompiler.eval (plugin:digitalgarden:10760:23)
    at Generator.next (&lt;anonymous&gt;)</pre>

Update the first line of code, ‘Path/to/your/daily notes’ with the path to your notes.

And that’s it! If you have everything set up properly, you should see something like this:

![A graph showing RescueTime productivity pulse over time in Obsidian.](https://i0.wp.com/obsidian.rocks/wp-content/uploads/2023/07/Screenshot-from-2023-07-07-15-11-05.png?resize=1024%2C592&ssl=1)
It will likely only have a few data points at first, but the more you use it, the better it gets.

#### Including this chart in other notes

Once you have your Productivity Pulse set up, you can add it to other notes using an embed in Obsidian:

```
![[Productivity Pulse\|Productivity Pulse]]
```

I personally like to include it in my [home note](https://obsidian.rocks/home-notes-in-obsidian-with-examples/)!

![A screenshot of my productivity graph embedded within my home note.](https://i0.wp.com/obsidian.rocks/wp-content/uploads/2023/07/Screenshot-from-2023-07-07-11-25-03.png?resize=1024%2C849&ssl=1)
#### Code explanation

For those who want to understand what the code above is doing, let’s go through it and figure it out. Once you understand the code, you can adapt it to track *anything* included in your Daily Notes, which can be quite useful.

```
const journalPath = '"Path/to/your/daily notes"';
const chartColor = '#de425b';
```

These are *variables*, which tell our code 1) where to look for Daily Notes, and 2) what color our chart should be. I added these as conveniences, because you might have or want to update these from time to time.

```
const dailyNotesPlugin = app.internalPlugins.plugins['daily-notes'];
const dateFormat = dailyNotesPlugin.instance.options.format;
var labels = [];
var rt_data = [];
```

More variables. The `dailyNotesPlugin` variable allows us to pull the Date Format directly from the Daily Notes plugin, which is needed later in the script. The `labels` and `rt_data` variables are created here, and they will hold the data we need for our graph.

```
var sortByName = ((a, b) => moment(a, dateFormat).format('YYYYMMDD') - moment(b, dateFormat).format('YYYYMMDD'));
var latest_journals = dv.pages(journalPath)
    .sort(j => j.file.name, 'asc', sortByName);
```

This is where we fetch all of your latest daily notes, and sort them. `sortByName` is a function that allows us to sort your daily notes by their names, rather than by the created date. This way it doesn’t matter when we *create* our daily notes, they are sorted by their title regardless of when they are created.

```
for (var i=0; i < latest_journals.length; i++) {
    var j = latest_journals[i];
    if (j['rt'] !== undefined) {
        rt_data.push(j['rt']);
        labels.push(j.file.name);
    }
}
```

This is a *for* loop. This allows us to check every one of our daily notes for the “RT” data. If the data exists, then we add it to the “rt\_data” array, and we add the date to the “labels” arrays. Those two arrays are then turned into our graph:

```
const lineChart = {
    type: 'line',
    data: {
    labels: labels,
    datasets: [{
        label: 'RescueTime Score',
        data: rt_data,
        backgroundColor: [chartColor],
        borderColor: [chartColor],
        borderWidth: 1
    }]
   }
}
```

This is how you create a simple line chart in [Chart.js](https://www.chartjs.org/), the library that Obsidian Charts uses. We give our chart the “labels” and “rt\_data” that we created earlier, and we also specify the background and border colors. After creating this data, the only thing we have left to do is render the chart:

```
window.renderChart(lineChart, this.container);
```

And that’s it!

#### In conclusion

I’ve found this chart helps me enormously in my work life, and I hope that it helps you too. If you have any questions or comments, feel free to ask them in the comment box below.

The post [Streamline Your Day: Enhance Focus and Productivity with RescueTime and Obsidian](https://obsidian.rocks/streamline-your-day-enhance-focus-and-productivity-with-rescuetime-and-obsidian/) appeared first on [Obsidian Rocks](https://obsidian.rocks).
