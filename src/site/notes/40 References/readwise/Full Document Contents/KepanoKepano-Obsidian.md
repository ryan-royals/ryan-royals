---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/kepano-kepano-obsidian/","tags":["rw/articles"]}
---

![rw-book-cover](https://opengraph.githubassets.com/b1747c987bedd6ab4303b6bcddb52ddedd1de51e0bb360dee02689df0c203b26/kepano/kepano-obsidian)

My personal [Obsidian](https://obsidian.md/) vault template. A bottom-up approach to note-taking and organizing things I am interested in. This is not dogma, just my personal approach. Hopefully it can serve as inspiration, but do what works for you!

To learn more about how I use Obsidian, visit my website [stephango.com](https://stephango.com/topics/obsidian/).

#### [Get started](https://github.com/kepano/kepano-obsidian#get-started)

1. [Download this vault](https://github.com/kepano/kepano-obsidian/archive/refs/heads/main.zip)
2. Unzip the .zip file to a folder of your choosing
3. Open Obsidian and create a new vault pointing to that folder

#### [Vault structure](https://github.com/kepano/kepano-obsidian#vault-structure)

##### [Theme and related tools](https://github.com/kepano/kepano-obsidian#theme-and-related-tools)

* My theme: [Minimal](https://github.com/kepano/obsidian-minimal), more at [minimal.guide](https://minimal.guide)
* My [web clipper](https://stephango.com/obsidian-web-clipper) for saving articles and pages on the web

##### [Plugins](https://github.com/kepano/kepano-obsidian#plugins)

Some of my templates depend on plugins I use:

* [Dataview](https://github.com/blacksmithgu/obsidian-dataview) for overviews
* [Leaflet](https://github.com/javalent/obsidian-leaflet) for maps

##### [Folders](https://github.com/kepano/kepano-obsidian#folders)

I use very few folders. I avoid folders because many of my entries belong to more than one area of thought. My system is oriented towards speed and laziness. I don't want the overhead of having to consider where something should go.

My personal notes are in the root of my vault. These are my [journal](https://github.com/kepano/kepano-obsidian/blob/main/Categories/Journal.md) entries, [evergreen](https://github.com/kepano/kepano-obsidian/blob/main/Categories/Evergreen.md) notes, and personal ideas. If a note is in the root I know it's something I came up with. I do not use the file explorer much for navigation, instead I navigate mostly using the quick switcher or clicking links.

If you want to use this vault as a starting point the **Categories** and **Templates** folders contain everything you need.

The folders I use:

* **Attachments** for images, audio, videos, PDFs, etc.
* **Clippings** for articles and web pages captured with my [web clipper](https://stephango.com/obsidian-web-clipper) written by other people.
* **Daily** for my daily notes, all named `YYYY-MM-DD.md`.
* **References** for anything that refers to something that exists outside of my vault, e.g. books, movies, places, people, podcasts, etc.
* **Templates** for templates. In my real personal vault the "Templates" folder is nested under "Meta" which also contains my personal style guide and other random notes about the vault.

The folders I don't use, but have created here for the sake of clarity. The notes in these folders would be in the root of my personal vault:

* **Categories** contains top-level overviews of notes per category (e.g. books, movies, podcasts, etc).
* **Notes** contains example notes.

#### [Style guide](https://github.com/kepano/kepano-obsidian#style-guide)

##### [Templates and metadata](https://github.com/kepano/kepano-obsidian#templates-and-metadata)

I use templates very heavily, because they allow me to lazily insert most of the metadata I need about any kind of note.

The `.obsidian/types.json` file shows which properties are assigned to which types.

* Most of my properties attempt to be reusable across categories
* Many properties have short names e.g. `start` instead of `startdate`
* I use the `list` type more than the `text` type for many properties, because I find it useful to be able to enter multiple links

##### [Categories and tagging](https://github.com/kepano/kepano-obsidian#categories-and-tagging)

My notes are primarily organized using the category property, e.g. `category: "[[Movies]]"`. These also function as links that help me navigate to the overview note for that category. Some rules I follow:

* Always pluralize categories and tags
* Use `YYYY-MM-DD` everywhere
* Use a single vault for everything
* Avoid folders for organization
* Avoid non-standard Markdown

Having a [consistent style](https://stephango.com/style) collapses hundreds of future decisions into one, and gives me focus. I always pluralize tags so I never have to wonder what to name new tags. Choose the rules that feel comfortable to you.

##### [Rating system](https://github.com/kepano/kepano-obsidian#rating-system)

Anything with a `rating` uses an integer from 1 to 7

* 7 — **Perfect**, must try, life-changing, go out of your way to seek this out
* 6 — **Excellent**, worth repeating
* 5 — **Good**, don't go out of your way, but enjoyable
* 4 — **Passable**, works in a pinch
* 3 — **Bad**, don't do this if you can
* 2 — **Atrocious**, actively avoid, repulsive
* 1 — **Evil**, life-changing in a bad way

Why this scale? I like rating out of 7 better than 4 or 5 because I need more granularity at the top, for the good experiences, and 10 is too granular.
