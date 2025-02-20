---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/the-next-chapter-of-reader-public-beta/","tags":["rw/articles"]}
---

![rw-book-cover](https://s3.amazonaws.com/readwiseio/2022/12/OG-Reader-1.png)

**Today, we're excited to announce the public beta of our own, fully-integrated reading app (known as "Reader"). Get started for free at [readwise.io/read](https://readwise.io/read).**

![OG-Reader-3](https://s3.amazonaws.com/readwiseio/2022/12/OG-Reader-3.png)

What is Reader? In case you missed [our original manifesto](https://blog.readwise.io/readwise-reading-app/), Reader is a more powerful, more flexible version of the classic read-it-later app. If you've used Instapaper or Pocket, it's like those except built for 2023 and beyond. This means:

* **Read anything** — Reader handles not only web articles saved for later, but also email newsletters, RSS feeds, Twitter threads, Twitter lists, PDFs, and EPUBs. You can even highlight the open web using the Reader browser extensions and highlight Youtube videos in the Reader interface.
* **Highlight like a pro** — Reader is intended for power users with productivity-oriented innovations such as first-class highlighting & annotating, keyboard-based reading, text-to-speech, GPT-3 (aka Ghostreader), and much more.
* **Customize your experience** — Reader is designed with the flexibility to accommodate a variety of consumer, professional, and academic use cases. All-in-one does not mean one-size-fits-all so Reader can adapt to your unique needs.
* **Read anywhere** — Reader is built with a local-first, cross-platform architecture enabling full-text search and offline reading with data constantly synced across web and mobile devices.
* **Watch it evolve** — Reader is being actively developed with responsive customer support and rapid feedback loops informed by beta testers who are already reading in the app for hours a day.

Admittedly, getting from a next-generation read-it-later app (where we were last year) to an all-in-one reading app (where we are now) turned out to be harder than we thought. For example, unifying the user experience of an RSS feed reader – which automatically pushes low signal-to-noise content to you all day – with a read-it-later app proved to be quite the product challenge.

The good news is that we're through the woods and the cumulative effect of bringing all these different content types together under one roof is as magical as we thought it would be. We hope you love Reader, even in its public beta state, as much as our testers have!

Here's some of their feedback:

[![Reader testimonials](https://s3.amazonaws.com/readwiseio/2022/12/image-14-1.png)](https://twitter.com/michaelfransen/status/1601737652814110720)

[![Reader testimonials](https://s3.amazonaws.com/readwiseio/2022/12/image-13-1.png)](https://twitter.com/Mridgyy/status/1599738223923646464)

[![Reader testimonials](https://s3.amazonaws.com/readwiseio/2022/12/image-15-1.png)](https://twitter.com/rahulrajeeev/status/1574642790629511168)

[![Reader testimonials](https://s3.amazonaws.com/readwiseio/2022/12/image-16-1.png)](https://twitter.com/atannerhodges/status/1601210866224967680)

[![Reader testimonials](https://s3.amazonaws.com/readwiseio/2022/12/image-18-1.png)](https://twitter.com/entrpswn/status/1602696075512610819)

[![Reader testimonials](https://s3.amazonaws.com/readwiseio/2022/12/image-19-1.png)](https://twitter.com/AleenaCodes/status/1602584588236345345?s=20&t=NaKdiug57sPgnM_nzUb0yw)

We're still calling this release a "public beta" because the surface area of the Reader product is rather vast. We basically had to build five different kinds of reading apps at the same time without accidentally developing the software equivalent of a spork. Meanwhile, we had to make sure the app works well on Chrome, Firefox, and Safari as well as iOS and Android.

That said, we're ready to release Reader into the wild because thousands of beta testers have battle-tested the product and, even though you might run into something here or there, the core experience is solid. We're just hoping the "public beta" label buys us a little leeway for the next few months while we continue to smooth out rough edges. It's also an opportunity for you to help shape the future of digital reading 🙂

→ **If you haven't already, join the beta of Reader for free here: [readwise.io/read](https://readwise.io/read)**.

The rest of this post gets into the Reader product including its first value proposition of "all your reading in one place" as well as our favorite innovations to date. We conclude with a brief discussion of our bootstrapped business model and what we look forward to building next year.

#### All your reading in one place

There are many problems with digital reading we hope to solve with Reader (see: [our quasi-manifesto](https://blog.readwise.io/readwise-reading-app/)), but the first we've chosen to focus on is what we call "unbundling". What we mean by this is that digital reading is terribly fragmented. You read articles in a web browser. Newsletters in an email client. RSS feeds in a feed reader. Tweetstorms in the Twitter app. PDFs in Acrobat. Ebooks on a proprietary device. And so on.

Meanwhile, the lines separating media types have blurred. Is a sequential series of longform email newsletters really that different from an ebook? Is a thread of tweets really that different from a blog post? As everything blends together, what's the purpose of all these different containers?

Our users certainly don't see the point. They just want everything in one place. You can see this in the many tutorials all over the internet teaching you how to cobble together half a dozen reading apps resulting in diagrams like below:

![fragmented-reading-solutions](https://s3.amazonaws.com/readwiseio/2022/12/pkm-setups.png)

Sources: [Eva Keiffenheim](https://betterhumans.pub/the-complete-guide-for-building-a-zettelkasten-with-roamresearch-8b9b76598df0) & [Ravi Kurani](https://ravi-kurani.medium.com/how-i-read-20-articles-a-day-using-instapaper-readwise-amazon-kindle-and-roam-research-7aca037a5fc4) & [Nicole van der Hoeven](https://nicolevanderhoeven.com/blog/20210206-readwise-to-obsidian/) & [Kyle Stratis](https://www.kylestratis.com/post/my-information-operating-system-part-2-collecting)

The problem with these systems it that they're a lot of work. You need to juggle multiple apps and, often, subscriptions. You need to learn the ins & outs of each application. You need to maintain a bunch of fragile integrations. And all the while you're losing scarce focus context switching from one app to another. In the end, many folks spend more time working on their capture systems than working in them.

The unbundling gets in our way as developers too. With everything scattered all over the place, we can't seriously pursue our mission of improving the digital reading experience by an order of magnitude using software. Even if we achieved a 10x improvement in a single silo, such as ebooks, that might only comprise 10% or 20% of your digital reading.

For all these reasons, getting all your content in one place was the first value proposition we focused on with Reader.

Admittedly, this means we had to spend the past year schlepping a lot of inglorious one-to-ten work (creating more of something that already exists) versus the zero-to-one inventive work that gets us out of bed in the morning. We persisted, however, because we hoped the sum of the parts would be greater than the whole. Fortunately, we think we can now see that bet paying off.

All-in-one is just the beginning.

#### Our favorite innovations so far

Even though we spent most of last year rebuilding functionality that individually exists elsewhere, we couldn't help but go off on some side quests. We know, we know: sell benefits, not features. But this is a launch post and what's a launch post without a review of cool new features? Below are some of our favorites.

##### First-class highlighting & annotating

It's no secret that Readwise was built on a foundation of highlights. We therefore embedded highlighting and annotating features into Reader from day one rather than bolting them on after the fact, as has been typical with other reading apps. This was our opportunity to raise the table stakes of highlighting going forward.

###### Images and rich-text formatting

In Reader, you can highlight not only plain text but also images and rich-text. These then carry over into Readwise and your note-taking app of choice. As far as we know, Reader is the first and only reading app to preserve these details which, candidly, makes no sense to us. We expect this to be the new standard going forward because once you've highlighted images, you'll never settle for anything less.

![Highlighting_Image](https://s3.amazonaws.com/readwiseio/2022/12/Highlighting_Image.gif)

###### Margin notes

In other reading apps, marginalia are stuffed into little icons or misaligned sidebars making it difficult to connect your notes to the author's prose. Inspired by [Tufte sidenotes](https://edwardtufte.github.io/tufte-css/) and commenting in Google Docs and Notion, we designed annotations that will appear in the right margin, just like traditional marginalia, provided your screen has enough width.

![Marginalia](https://s3.amazonaws.com/readwiseio/2022/12/Marginalia.gif)

###### First-class tagging

In addition to highlighting and annotating, we incorporated first-class tagging into Reader from the very beginning. These aren't special notes like dot `.tag`, hashtag `#tag`, or double brackets `[[tag]]`, but an actual tagging primitive. You can apply tags at both the document- and highlight-level and use these to organize your library as well as orchestrate workflows.

![Tagging](https://s3.amazonaws.com/readwiseio/2022/12/Tagging.gif)

###### Double-tap to highlight

One of our favorite mobile gestures is the double-tap to highlight a paragraph. Sometimes you'll want highlights to be shorter or longer than a whole paragraph, but we've handled enough highlights at this point (nearly a billion) to know that the paragraph represents the 80/20 of highlights. At least, if you're highlighting to capture an idea rather than just markup the page.

![Tap_Highlight](https://s3.amazonaws.com/readwiseio/2022/12/Tap_Highlight.gif)

##### Twitter list digests

In Reader, there are two broad sections for your content: Library and Feed. Library is where high signal documents that you manually curate for yourself go such as clipped web articles, saved Twitter threads, and uploaded PDFS. Feed is where low signal documents that are automatically pushed to you go such as RSS feeds, email newsletters, and other digests.

![Twitter-Digest](https://s3.amazonaws.com/readwiseio/2022/12/Twitter-Digest.gif)

RSS and email newsletters in the Feed are of course great, but one of Reader's special content types is the Twitter list digest. You create a public list in Twitter and then subscribe to it in Reader. You'll then start receiving two digests per day (AM and PM) containing all the new tweets in that list since the last edition. We've found this to be a great way to batch your Twitter screen time without fear of missing out.

##### Tiktok-like Feed UI

Another novelty of the Reader Feed is a specialized, TikTok-inspired user interface enabling you to cruise through new items like a warm knife cutting through butter. You swipe up to advance, swipe down to reverse, save for later, and of course tap to just start reading. Advancing marks a document as seen, so this UI is a great way to clear your Feed. You can get through 100 to 200 items per day without breaking sweat.

![TikTok-UI](https://s3.amazonaws.com/readwiseio/2022/12/TikTok-UI.gif)

##### Daily Digest

To this day, our favorite feature of Readwise is the Daily Review. It's a delightful yet healthy habit so of course we wanted to build an analog for Reader. Where we landed is the Daily Digest, which serves up an appetizer of *new* items followed by a main course of *previously saved* items each morning.

![Daily-Digest](https://s3.amazonaws.com/readwiseio/2022/12/Daily-Digest.gif)

Functionally, the Daily Digest helps you maintain a routine of staying on top of your Feed, whittling down your backlog, and (hopefully) reading everyday. Psychologically, the novelty of the new items at the beginning eases you into the more challenging but fulfilling backlog at the end. Modern problems (monkey brain) require modern solutions (cunning software).

##### Powerful highlighter extension

The Reader browser extension not only saves web articles for later, but also enables you to highlight the open web. There are a few good reasons you might want to do this rather than highlight the parsed document in Reader:

First, although we generally prefer the clean, consistent, distraction-free reading experience, there are some exceptions where the original site is better. In these cases, you can honor the OP and read their work as they intended while still making notes and highlights.

Second, although our parsing already exceeds existing read-it-later apps in our benchmark tests, we'll never be able to parse 100% of the internet, 100% error-free. HTML, CSS, and JS are just too flexible. The web highlighter is our exception handler.

Third, sometimes you'll find yourself reading an article and want to take a highlight but not break your flow. Just activate the highlighter, make your highlight, and keep reading.

![Web-Extension](https://s3.amazonaws.com/readwiseio/2022/12/Web-Extension.gif)

What makes the Reader browser extension so unique is that highlights bidirectionally sync with the Reader app. This means if you highlight the open web using the extension, the highlights will appear overlaid on the parsed document in Reader, and if you highlight the parsed document in Reader, the highlights will appear overlaid on the original website.

##### Annotated sharing

On the topic of overlaid highlights, you can generate public versions of your annotated documents for sharing with friends, family, and colleagues. Here's an example of [an article about QA testing I annotated](https://readwise.io/reader/shared/01gcj7td8p308nvea7cgknktwa) for my cofounder Tristan. It came at a time when we were both pondering whether we should hire a quality assurance tester as part of our software development process.

![Annotated-Share](https://s3.amazonaws.com/readwiseio/2022/12/Annotated-Share.gif)

We're generally antisocial when it comes to our digital reading product philosophy, but we do believe that there is a lot of utility in sharing annotated documents among small groups with "shared context". A perfect example is the shared link above, from one colleague to another about a project they're constantly thinking about and working on together, but it also occurs among friends, family, spouses, and other small social settings.

##### Keyboard-based reading (and shortcuts)

Whereas most modern reading apps are developed mobile-only, or mobile-first with a web app reluctantly added later on, Reader has been cross-platform since inception. There is no question that reading on a mobile device is more convenient (and often more comfortable) than a typical computer screen; however, we hold a contrarian position that some kinds of annotation-heavy "reading for betterment" want to take place on a monitor with a keyboard. For this reason, we've crafted a keyboard-based reading experience enabling you to read, highlight, and annotate without ever using the mouse.

![Keyboard-Shortcuts](https://s3.amazonaws.com/readwiseio/2022/12/Keyboard-Shortcuts.gif)

We took a risk when building keyboard-based reading because it's not exactly the kind of "faster horse" that users think to ask for in conversations. But fortunately the gamble paid off and keyboard navigation is now one of Reader's most beloved features. Like highlighting images and rich text, we wouldn't be surprised if this becomes a UX pattern in reading apps going forward.

##### Filtered Views

We love flexible software like Notion, Airtable, and Obsidian with low bars for novices and high ceilings for experts. Inspired by those apps, you can think of your Reader account as one giant database with each row representing a document. Each document contains the content itself, but also all kinds of structured metadata ranging from inherent properties such as title, author, and published date to user-specific properties such as tags, highlights, and reading progress. The core organizational primitive of Reader — called a *filtered view* — enables you to easily subset documents based on these properties, and then save those as views for future reference.

In its simplest form, you might create a filtered view based on a single tag to simulate a folder, a single media type to separate, say, all your PDFs, or a set of RSS feeds to create a group of related news sources. In more advanced permutations, you might create a filtered view to facilitate various workflows such as "show me all documents with at least 2 highlights that I read in the past week" for composing your weekly newsletter. The possibilities are virtually limitless.

![Homepage-Customization](https://s3.amazonaws.com/readwiseio/2022/12/Homepage-Customization.gif)

Once you save a filtered view, you can use it throughout the user interface including the left sidebar, the Home screen, the quick switcher, and the dedicated views page enabling you to customize the experience to your unique situation.

##### YouTube highlighting

It might seem odd to mention a YouTube feature in the context of an application named "Reader", but we're ultimately about betterment and YouTube has evolved into perhaps the best learning content platform in existence. Yet until now, there weren't many digital solutions to capture ideas and take notes while you watch.

![Youtube-Highlighting](https://s3.amazonaws.com/readwiseio/2022/12/Youtube-Highlighting.gif)

In Reader, you can watch a YouTube video alongside its time-synced transcript, and take notes and highlights as it plays. You can also precisely navigate the video by clicking any fragment, clicking a highlight in the right sidebar, or using special keyboard controls.

##### Ghostreader (aka GPT-3)

Last but not least, if you're building product in late 2022 without incorporating AI, are you even trying? There are lots of GPT-3 based copilots for writing, but Reader incorporates the first copilot of reading. We call it Ghostreader.

![24-stroke-ghost--1-](https://s3.amazonaws.com/readwiseio/2022/12/24-stroke-ghost--1-.gif)

There are so many fun things you can do with Ghostreader, but let us show you some of our favorites:

You can lookup definitions in context:  

![readwise-reader-gpt-define-small](https://s3.amazonaws.com/readwiseio/2022/12/readwise-reader-gpt-define-small.gif)

You can perform encyclopedia lookups:  

![readwise-reader-gpt-lookup-small](https://s3.amazonaws.com/readwiseio/2022/12/readwise-reader-gpt-lookup-small.gif)

You can translate to other languages:  

![readwise-reader-gpt-translate-small](https://s3.amazonaws.com/readwiseio/2022/12/readwise-reader-gpt-translate-small.gif)

You can "come to terms" with the author:  

![readwise-reader-gpt-come-to-terms-small](https://s3.amazonaws.com/readwiseio/2022/12/readwise-reader-gpt-come-to-terms-small.gif)

You can simplify complex language (think contracts and research papers):  

![readwise-reader-gpt-simplify-small](https://s3.amazonaws.com/readwiseio/2022/12/readwise-reader-gpt-simplify-small.gif)

You can create question & answer pairs:  

![readwise-reader-gpt-flashcard-small](https://s3.amazonaws.com/readwiseio/2022/12/readwise-reader-gpt-flashcard-small.gif)

You can summarize whole documents or just sections:  

![readwise-reader-gpt-summarize-doc-small](https://s3.amazonaws.com/readwiseio/2022/12/readwise-reader-gpt-summarize-doc-small.gif)

You can even write your own prompts using Reader's powerful templating language for accessing document content and metadata! The only limit is your imagination.

##### Honorable mentions

For brevity, we didn't even bother mentioning table stakes features such as:

* Lifelike text-to-speech (listen to documents)
* Personal Reader email addresses
* Offline support
* Cross-platform syncing
* Public APIs
* Adjustable typography
* Light & dark modes
* Customizable workflows
* Navigable tables of contents
* Editable metadata
* Document-level notes
* Exporting to note-taking apps such as Notion, Obsidian, Roam Research, Logseq, Evernote, and Markdown.

All these features (and more) are included in this public beta.

#### Bootstrapped business model

As we wind down this launch post, we want to take a moment to explain our business model because we've noticed a recent phenomenon of consumers taking an interest in the sustainability of their favorite productivity apps.

![business-model](https://s3.amazonaws.com/readwiseio/2022/12/business-model.png)

We don't know what exactly caused this trend, but we do know it’s really annoying to invest time and energy into a tool like Reader only for it to stop improving or, worse, shutdown completely. And lord knows this fear isn't mere paranoia. We've all had a favorite reading app come and go, from beloved Google Reader vanishing a decade ago to Instapaper and Pocket gradually entering maintenance mode over the past few years. Let us also not forget others who came before us like Readability, Findings, Readmill, Highly, Diigo, Oyster, Glose, Hardbound, and Scroll.

Reading software, as a business, is brutal. RIP.

The good news is we aren't going anywhere. Readwise the company has been around for five years (that's Lindy in our industry), and the business is sustainable on a team of 13 mission-oriented all-stars and growing.

![team-photo-1](https://s3.amazonaws.com/readwiseio/2022/12/team-photo-1.png)

This is only possible because of two difficult choices early on:

First, we made the hard decision back in 2018 to **not** raise venture capital (see: [Why We're Bootstrapping Readwise](https://blog.readwise.io/why-were-bootstrapping-readwise/)). This wasn't because we're ideologically opposed to VC like DHH and Jason Fried. We just studied our industry and realized the market is not large enough to support VC valuations. Had we pursued external funding, we probably would have been pushed into trying, say, social reading features, which are orthogonal to our stated mission.

Second, we made the unusual decision to start charging for our software. Even today consumer/B2C saas is uncommon, but back then the notion that an individual (as opposed to a company) would pay for niche productivity software was unheard of. And for good reason. [As we've written](https://twitter.com/deadly_onion/status/1578831165561049089), it's mathemetically impossible to build a huge business in consumer saas. Fortunately, we don't have to because we aren't venture-backed.

This brings us to the question of how we'll price Reader. Once Reader officially exits beta sometime in 2023, we intend to reprice Readwise/Reader for new subscribers thereafter. Pricing is really hard and complex so we candidly haven't figured out the exact plans yet, but we hope to justify a slightly higher price point than Readwise could before Reader. Regardless, we don't intend to increase pricing on existing full subscribers at that time. This means that if you subscribe while Reader is in beta, you'll get lifetime access for $7.99/month (billed annually) as part of our current Readwise Full plan.

Before concluding this section, we do want to express our gratitude to our existing customers and our intrepid beta testers. Because we've never relied on external funding to build Readwise, we literally would not be here without you. We thank you.

#### Road ahead

Although public beta is a significant milestone, we want to be clear that we by no means think Reader finished. We'll be the first ones to admit that we still have so much to build. Nor does public beta mean we'll be slowing down our shipping velocity. If anything, we hope to ship faster because we'll be more focused on deepening existing functionality over exposing new surface area.

Looking back, we started with the foundation of a next-generation read-it-later app with first-class highlighting & annotating. We then gradually folded in v1s of email newsletters, Twitter threads, Twitter lists, RSS, PDFs, EPUBs, and YouTube. Roadmaps are always fluid, but going forward I suspect we'll spend the next few months going deeper on each of these use cases while optimizing performance and fixing edge cases.

Longer term, we remain hopeful that Reader will pioneer a whole new category of software: tools for thought built not for writing, but for reading.

As always, we thank you for joining us on this journey 🙏
