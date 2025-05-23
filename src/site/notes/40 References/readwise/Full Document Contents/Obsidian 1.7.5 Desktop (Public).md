---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/obsidian-1-7-5-desktop-public/","tags":["rw/articles"]}
---

![rw-book-cover](https://obsidian.md/images/banner.png)

#### No longer broken

* Updated the behavior of the "Add internal link" command so the cursor is placed at the end of the link text, and the link suggestion pop-up appears.
* Fixed issues where Sync Sidebar timestamps would not reflect changes made locally.
* Improved render performance of Canvas when there are many nodes on the screen.
* Fixed issues where the attachment folder would be displayed incorrectly in settings.
* Fixed regression where the "Add tag" command was not causing the tag suggestions to appear.
* Fixed bug where Sandbox vault would fail to load if the "Start here" file was missing.
* File Explorer: "Reveal in file navigation" now waits for the view to load.
* Fixed bug where tree components (such as the Outline view) would be slow to refresh on Android.
* Fixed bug where switching between Obsidian and other apps would cause the navigation bar and the toolbar to both be active.
* Fixed "Installing theme" notice not disappearing when installing a legacy theme.
* Fixed middle-click not closing tabs.
* Fixed bug where Graph view options would sometimes get overridden when opening a new graph view.

#### Developers

* The installer has been updated to use Electron v32 (requires downloading [the latest installer](https://obsidian.md)).
* Fixed vim `langmap` failing to load properly.
* Added a new debug mode for developers. To enable, run `app.debugMode(true);` in developer tools. When active, inline source maps will not be stripped from loaded plugins.
* Fixed MarkdownCodeBlockProcessor adding an extra newline when in reading mode.
