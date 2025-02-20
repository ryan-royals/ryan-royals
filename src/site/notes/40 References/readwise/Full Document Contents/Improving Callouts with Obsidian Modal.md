---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/improving-callouts-with-obsidian-modal/","tags":["rw/articles"]}
---

![rw-book-cover](https://obsidian.rocks/wp-content/uploads/2024/07/mitchell-luo-NROHA1B-NYk-unsplash-1.jpg)

It’s no secret that [I love callouts in Obsidian](https://obsidian.rocks/using-callouts-in-obsidian/).

Whenever a note starts to feel overwhelming, I try to do two things: break the note into multiple [atomic notes](https://obsidian.rocks/five-title-ideas-for-notes/#Idea-1-Each-Note-Should-Contain-One-Idea), and pretty the note up with headings and callouts.

But I have a problem with callouts: the format is hard to remember. Nearly every time I want to use a callout, I need to struggle to remember how (or look it up). Even if I am able to remember the format, I forget the *types* of callouts. “note” is an easy one, but what are the green ones called? Is it todo, succeed, or just green?

I’ve struggled with this for years, and I find myself in a chicken and egg situation. If I used them *more*, maybe I would remember them better. But I *don’t* use them more because I forget how.

I did discover, eventually, that you can create callouts with the [Command Palette](https://obsidian.rocks/for-beginners-and-pros-alike-the-command-palette-in-obsidian/). This is an improvement, but it still doesn’t help me with collapsible callouts or with the different *types* of callouts. There has to be a better way.

Turns out there *is* a better way, and after several years of looking, I finally found it!

#### The Obsidian Modal Form Plugin

Have you heard of the Modal Form plugin for Obsidian?

Me neither, until a couple of weeks ago.

It is a fascinating plugin that allows you to create popups that accept inputs. If you’ve ever used the QuickAdd plugin, you’ll be familiar with the concept, but the Modal Form plugin takes it up a level.

This plugin is complex and a bit overwhelming at first, so rather than telling you everything it can do, I’m going to show you what we’re going to build with it today. Take a look:

This workflow allows you to create your own user interface for Obsidian! In the example above, we’re able to use QuickAdd to trigger an overlay that gives us an easy visual interface for callouts in Obsidian.

This isn’t the only thing you can do with this plugin, and probably not even the most useful thing we can do with it. But it’s where I started, and I think it’s a good way to learn how to use this complicated plugin. So let’s jump in!

#### Prerequisites

In order to use this workflow, you need two plugins:

* [QuickAdd](https://obsidian.md/plugins?id=quickadd)
* [Modal Forms](https://obsidian.md/plugins?id=modalforms)

Click on the above links to open in Obsidian. Then install and activate them, and then we can move on to setup.

#### Setting up Modal Forms

The Modal Forms plugin is a bit unusual when it comes to plugins. It doesn’t have much in the way of *settings*, instead it gives you a bunch of custom views. By default these views shows up in your right sidebar, but you can configure it to appear in either sidebar or in your main view. I find it easier to use in the main view, so I have configured it that way for this tutorial.

Once installed and enabled, open the [command palette](https://obsidian.rocks/for-beginners-and-pros-alike-the-command-palette-in-obsidian/) and search for “modal forms”, and you will see a bunch of options. Select “new form”, and we’ll get started on our Callout form.

That command will open the New Form view, which allows you to create a new form. It asks for a title and a name. For this form, I gave it the title “new\_callout” and the name “New Callout”. That should look something like this:

![A screenshot of the form creation screen for the Obsidian Modal Forms plugin.](https://i0.wp.com/obsidian.rocks/wp-content/uploads/2024/07/image.png?resize=1024%2C720&ssl=1)
Once you’ve given it a title and name, then comes the fun part. Next we get to configure the form itself. Click the button that says “add more fields”, and you should see something like this:

![A screenshot of adding fields in the Obsidian Modal Forms plugin.](https://i0.wp.com/obsidian.rocks/wp-content/uploads/2024/07/image-1.png?resize=1024%2C793&ssl=1)
Don’t be scared by the warning at the top! This happens anytime you add a new field, because the field won’t be valid until you give it a name.

So let’s do that! First we’ll create a “type” field to store the different types of callouts we use. Add “Type” as the name of this field, and change the type to “Select”. Then we can add all the different types of callouts that we use.

[Check out my article](https://obsidian.rocks/using-callouts-in-obsidian/) to see all the different types of callouts available, or just add the ones you use. Once you’re done, it should look something like this:

![A screenshot of configuring an Obsidian Modal with different types of callouts.](https://i0.wp.com/obsidian.rocks/wp-content/uploads/2024/07/image-2.png?resize=1024%2C915&ssl=1)
The “label” can be whatever you want, name them whatever makes sense to you. If you want to name them colors instead of the official terms, then feel free! But make sure you use the official terms (such as “note”, “success”, “info”, etc) in the “value” field, otherwise this won’t work.

Once you have your types set up, the rest are easy. Here are the other fields that I like to have:

* Add a field called “Title”, as a default text field
* Add a field called “Contents” as a default text field
* Add a field called “Collapsible” and change it to a “toggle” field

> 
> Note: You will notice that every field has both a name and a label, but technically only one is required. If you only include a name, like I suggest above, then the label becomes the same as the title.
> 
> 
> 

Once you have all of those configured properly, click the big shiny button that says “Save and close”. If you’re not sure that you have everything configured properly, you can also click the “Preview” button to test your field types out.

And that’s it for the Modal Forms plugin! You now have your very own modal form, and all we have to do is connect it to QuickAdd.

#### Setting up QuickAdd

QuickAdd is a super useful plugin that you can use for all sorts of things. For example, see my article on [Quick Capture in Obsidian](https://obsidian.rocks/obsidian-quick-capture/#The-QuickAdd-Solution).

QuickAdd allows you to automate things that you do often in your vault. For example, you can quickly capture a new note, a new todo, or a new article you want to read.

In our case, we want to automate the creation of callouts. We already have a form set up, but Obsidian doesn’t know what to do after you submit that form: that is where QuickAdd comes in.

We will use QuickAdd both to *trigger* the callout modal, and also to *process* the results of the modal.

First we need to set up a QuickAdd action. To do that, open the settings for your vault, and select “QuickAdd”. You should see the settings page for QuickAdd, with a input box at the top of the overlay. Type “New Callout” into the input and change the select menu to “capture”, then click “Add Choice”.

![A screenshot of adding a new QuickAdd action in Obsidian called ](https://i0.wp.com/obsidian.rocks/wp-content/uploads/2024/07/image-3.png?resize=1024%2C107&ssl=1)
That will create a new action called New Callout. Then click the gear icon to the right of that action, and we can configure this new action.

Configuring this action is fairly straightforward. Turn on the option that says “capture to active file”, then scroll down and turn on “capture format”. Then paste this code, which tells QuickAdd how to format the callout based on the response from Modal Forms:

```
```js quickadd
    const modalForm = app.plugins.plugins.modalforms.api;
    const result = await modalForm.openForm('new_callout');
    const collapsible = result.get('Collapsible');
    const col = (collapsible) ? '-' : '';
    return result.asString(`> [!{{Type}}]${col} {{Title}}\n> {{Contents}}\n\n`);
```
```

This code contains a bunch of variables that come from the Modal Forms plugin, so make sure the names match the names you gave your inputs. “Type” in this script has to match the label for your “Type” in the overlay and so on, even capitalization matters. If you’ve followed the instructions above precisely then you shouldn’t have a problem, but if you run into issues, that may be why.

And with that, you’re done! You can now test your new overlay by following these steps:

* Press ctrl/cmd+P to open the Command Palette.
* Type “quick” and select “Run QuickAdd”.
* Select “New Callout”
* Configure your callout, and press submit. A new callout should appear where your text cursor was, with all the options you selected.

#### Conclusion

QuickAdd and Modal Forms are two of the most powerful plugins available for Obsidian. But figuring out how to use them can be tricky. I hope this article has given you an idea of how useful these plugins can be, and an idea of how to build your own features using these two incredible plugins.

If you have any problems with the above instructions, feel free to contact me or let me know in the comments below!

The post [Improving Callouts with Obsidian Modal](https://obsidian.rocks/improving-callouts-with-obsidian-modal/) appeared first on [Obsidian Rocks](https://obsidian.rocks).
