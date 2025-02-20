---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/using-readwise-s-highlight-id-as-a-single-source-of-truth-in-obsidian/","tags":["rw/articles"]}
---

![rw-book-cover](https://miro.medium.com/v2/resize:fit:800/0*HBhv7hIzbYVZv4z-.png)

The [Readwise](https://readwise.io/) service allows you to export your highlights to various tools like Obsidian, Roam, Notion, and more. The export can be configured to export these highlights in a format that works best for you.

One possible issue though as you work across various media sources with these exported highlights is that you can lose context of where they come from.

To illustrate the problem I want to solve: Imagine I have a highlight from an article exported to Obsidian and also exported to Roam, how can I know where that highlight came from? This is where Readwise’s **highlight\_id** field comes into play. I can use this field to identify the highlight origin, no matter in which tool I use that highlight.

In effect, Readwise becomes a single source of truth for all our ebook and article highlights. You don’t have to deal with the complexity of multiple data sources, rather you let Readwise be your central store, your single source of truth for all your highlights.

For this article, I am going to focus on Obsidian to illustrate how to use highlight\_id to solve this problem.

**What is highlight\_id?**

Readwise allows you to configure the way your highlights are exported to Obsidian. The export allows you to choose what data elements from your highlights are exported and also define the layout of the exported data.

One field that can be used in the export configuration is **highlight\_id**.

The **highlight\_id** field is very interesting. It is Readwise’s internal identifier for that highlight. Readwise assigns a unique number to every highlight you create. This identifier is globally unique to the Readwise system. Once a highlight is created and assigned its highlight\_id, that identifier never changes.

Using this identifier in our export gives us two advantages:

* A unique identifier to be used in our export that is always the same no matter where you that highlight
* I can run the export command as many times as I want in my Obsidian vault and the highlight will always have the same ID.

Why are these two things important? It has to do with how many Tools for Thought work internally. These tools promote the idea of block referencing or creating a link in one note to another note. For example, you have a highlight from an article you read, and that highlight is stored in a file in Obsidian. You want to make notes to that highlight. Since the highlight is located in a different file, you can create a reference to that highlight without having to copy it out.

This is very important when you start to block reference highlights in other places in your vault so that the link between the highlight and your note doesn’t break, since the ID is always the same.

In effect, the Readwise highlight\_id becomes a [single source of truth](https://en.wikipedia.org/wiki/Single_source_of_truth) for your highlights. This allows us to repurpose those highlights in other programs, but with a link back to Readwise.

**How to use highlight\_id?**

For this article, I demonstrate the configuration for exporting to Obsidian, but the concept equally applies to any other tool Readwise supports.

Each user has their own export configuration. This configuration defines what data is exported, and how it is laid out.

The configuration for Obsidian can be found at this URL: <https://readwise.io/export/obsidian/preferences> (there is a link to this page as well in the [Readwise plugin for Obsidian](https://github.com/readwiseio/obsidian-readwise)).

This is my configuration for the highlight section on the configuration page:

![](https://miro.medium.com/v2/resize:fit:700/0*HBhv7hIzbYVZv4z-.png)
Readwise configuration for export to Obsidian

This configuration for highlights will render as follows in ObsidIan:

![](https://miro.medium.com/v2/resize:fit:700/0*4hVipgSXBE55VUiO.png)
Example of Readwise exported highlights in Obsidian

Notice under the heading # Highlights, that each highlight is exported to its own line. It has a dash at the beginning, which means treat that highlight as a part of a list. Then it’s followed by the text of the highlight, the link back to Readwise for that highlight, and then finally a weird number formatted as **^rw75317236**.

What is this number? It is what Obsidian calls a block reference identifier. It is a fancy way of saying that this paragraph of text has a unique identifier and the identifier is
{ #rw75317236}
. Every paragraph can have its own unique identifier.

Obsidian uses the block identifier as a way of linking to this paragraph from other notes. Obsidian allows the user to assign a unique identifier, or Obsidian can generate one for you.

Our goal is to use Readwise as a single source of truth for our highlights. With this goal in mind, we want to use the same identifier Readwise created for the highlight as the block identifier in Obsidian.

This is where the concept becomes powerful. We can use the same identifier for a highlight in multiple locations, but it all ties back to one central source, Readwise.

Let us look at the configuration for the highlight a bit closer:

```
- {{ highlight_text }}{% if highlight_location and highlight_location_url %} ([{{highlight_location}}]({{highlight_location_url}})){% elif highlight_location %} ({{highlight_location}}){% endif %} ^rw{{highlight_id}}{% if highlight_tags %}  
  - Tags: {% for tag in highlight_tags %}[[{{tag}}]] {% endfor %}{% endif %}{% if highlight_note %}  
  - Note: {{ highlight_note }}{% endif %}
```

![](https://storage.googleapis.com/pieces-web-extensions-cdn/pieces.png)
![](https://storage.googleapis.com/pieces-web-extensions-cdn/link.png)
First the highlights export as a list using the dash. It’s a standard Markdown list.

It is hard to see in all the goo and spaghetti of the code the configuration, but notice **^rw{{highlight\_id}}**. This is the Obsidian block reference. The format is as follows:

* Obsidian requires that a block (a paragraph or highlight) ends with a space and then the **^** character. This tells Obsidian that this is a block that can be referenced elsewhere in the vault.
* The next 2 characters are **rw**. I choose to export the **rw** as a prefix for the identifier as a way of telling myself that this block reference originates with Readwise, but it is not necessary, you don’t have to include it if you don’t want it.
* Then the highlight\_id field from readwise
{ #rw}
**{{highlight\_id}}**.

This will append the Readwise ID to the end of the highlight. So an exported highlight looks like this:

```
- The checklist cannot be lengthy. A rule of thumb some use is to keep it to between five and nine items, which is the limit of working memory. Boorman didn’t think one had to be religious on this point. [Loc 1831](https://readwise.io/open/75317236) ^rw75317236
```

![](https://storage.googleapis.com/pieces-web-extensions-cdn/pieces.png)
![](https://storage.googleapis.com/pieces-web-extensions-cdn/link.png)
This highlight now has a global identifier,
{ #rw75317236}
 that always ties that highlight back to Readwise.

Interestingly, you can also use this ID directly to link back to Readwise’s site:

* <https://readwise.io/open/{{highlight_id}}>

Just replace {{highlight\_Id}} with the id number, for example:

* <https://readwise.io/open/75317236>

When working with the Readwise identifier in Obsidian, or any other Tool for thought, keep in mind these two technical details:

* The Readwise ID is guaranteed to be unique
* The Readwise ID does not follow a sequential order nor is it guaranteed to follow some pattern.

**Summary**

This article contains a lot of nerdy details. However, if you are serious about leveraging your highlights in your Tool for Thought, you will want to invest the time into deeply understanding the export features of Readwise, since the connection between your highlights and notes are of great personal value and you want them to remain useful for years to come.

If you need help with this, feel free to leave comments here or contact me on [Twitter](https://twitter.com/tfthacker).

If you like my writing and would like to help support it, please consider signing up for a Medium membership using my referral link: <https://bit.ly/o42-medium> or buy me a coffee at: <https://bit.ly/o42-kofi>.
