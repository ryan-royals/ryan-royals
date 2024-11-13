---
{"dg-publish":true,"permalink":"/40-references/readwise/using-readwise-s-highlight-id-as-a-single-source-of-truth-in-obsidian/","tags":["rw/articles"]}
---

![rw-book-cover](https://miro.medium.com/v2/resize:fit:800/0*HBhv7hIzbYVZv4z-.png)

## Summary

The Readwise service allows you to export your highlights to various tools like Obsidian, Roam, Notion, and more. The export can be…

## Highlights

It is hard to see in all the goo and spaghetti of the code the configuration, but notice **^rw{{highlight_id}}**. This is the Obsidian block reference. The format is as follows:
• Obsidian requires that a block (a paragraph or highlight) ends with a space and then the **^** character. This tells Obsidian that this is a block that can be referenced elsewhere in the vault.
• The next 2 characters are **rw**. I choose to export the **rw** as a prefix for the identifier as a way of telling myself that this block reference originates with Readwise, but it is not necessary, you don’t have to include it if you don’t want it.
• Then the highlight_id field from readwise
{ #rw}
**{{highlight_id}}**.
This will append the Readwise ID to the end of the highlight. So an exported highlight looks like this:
- The checklist cannot be lengthy. A rule of thumb some use is to keep it to between five and nine items, which is the limit of ([View Highlight] (https://read.readwise.io/read/01h6jvcha2axdbs1e7fgnvyfs3))


Interestingly, you can also use this ID directly to link back to Readwise’s site:
• [https://readwise.io/open/{{highlight_id}}](https://readwise.io/open/{{highlight_id}}) ([View Highlight] (https://read.readwise.io/read/01h6jvcpre63xd80g2gfpehk6m))


