---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/obsidian-1-4-0-desktop-catalyst/","tags":["rw/articles"]}
---

![rw-book-cover](https://obsidian.md/images/banner.png)

#### Shiny new things

Introducing **Properties**. A simple and durable way to add tags, aliases, dates, and other metadata to your notes. Your properties can even include links to other notes.

![property-editor](https://github.com/obsidianmd/obsidian-api/assets/693981/aea72173-5663-459d-83de-6ff888f6bdd5)
###### Usage

* New visual editor for properties in Live Preview and Reading mode.
* Property types:
	+ Text — supports internal links
	+ List — supports internal links
	+ Number
	+ Checkbox
	+ Date
	+ Time
* New commands for interacting with properties
	+ Add file property (`Ctrl/Command + ;`)
	+ Clear properties
	+ Edit property
	+ Show all properties
	+ Show file properties
* **All properties** sidebar pane shows a list of all the properties across your vault, and number of uses for each
* **File properties** sidebar pane shows the properties for the active file
* Cut/copy/paste properties

###### Portability

Properties are saved directly to your note as *frontmatter*, a special section at the beginning of your file, encoded in YAML. This makes your note metadata readable in any plain text app, and compatible with many tools that support YAML frontmatter.

#### Improvements

* Tag autocomplete now uses a fuzzy search algorithm.
* PDF: Added “Copy as quote” and “Copy annotation” context menu options
* PDF: Added a button to copy annotations from the annotation popup
* PDF: Added “Copy link to page” to PDF thumbnail context menu

#### No longer broken

* Fixed: PDF Viewer single page view resets to first page.
* Fixed: PDF viewer search settings unclickable when toggling sidebar.
* Fixed bug where closing an pop-out window with an active modal would keep the modal active.
* macOS: In frameless window mode, the top-right buttons no longer shift when creating/closing tab groups.
* File Recovery modal will now show a loading state when loading large vaults.
* Workspace: fix "follow link under cursor" commands in Canvas.
* Canvas: nudging selection should not cause stacked tabs to scroll.
* Outline: Fixed outline not rendering if the view was opened via the "Show outline" command.
* The "New tab" view will now show the current hotkeys.

#### Developers

* Mermaid: Upgrade to v10.2.3.
* Vault: createFolder now return a `TFolder`.
* Metadata: `FrontMatterCache` no longer inherits from `CacheItem`.
* Theming: new CSS variables have been added for Properties that start with `--metadata`

###### About Properties

###### Internal Links

Internal links can be added to frontmatter using the following syntax:

```
---
link: "[[Link]]"
linklist:
  - "[[Link]]"
  - "[[Link2]]"
---

```

###### `tag`/`alias`/`cssclass` vs `tags`/`aliases`/`cssclasses`

As of 1.4.0, we're **deprecating** the "tag", "alias", and "cssClass" frontmatter keys. The new property editor will automatically migrate to `tags`, `aliases`, and `cssclasses` and the values will automatically be converted to lists.

The old keys will still be identified correctly in the app, but the property editor will always prefer `tags` and `aliases`.
