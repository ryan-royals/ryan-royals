---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem/","tags":["rw/articles"]}
---

![rw-book-cover](https://storage.googleapis.com/production-eng/1/2020/08/8d67f977-golden-paths_01b.png)

[![](https://storage.googleapis.com/production-eng/1/2020/08/8d67f977-golden-paths_01b.png)](https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem/)
“His spice-induced visions show him a myriad of possible futures where humanity has become extinct and only one where humanity survives. He names this future ‘The Golden Path’ and resolves to bring it to fruition.”

The above is a snippet taken from a [Fandom summary of Frank Herbert’s 1976 science fiction novel, *Children of Dune*](https://dune.fandom.com/wiki/Children_of_Dune_(novel)). The quote is so apt that I am convinced that at least one member of the team who introduced the concept of the Golden Path at Spotify was reading this book, number three in the Dune series of science fiction novels.

Okay, back down to earth.

Rolling back six or so years, Spotify was (and still is) committed to an agile engineering culture with autonomous teams. With all the advantages that brings, it also brought forth complexities, including a fragmented ecosystem of developer tooling where the only way to find out how to do something was to ask your colleague. ‘Rumour-driven development’, we endearingly called it.

This might work in a startup, even a large startup. But as Spotify grew…and grew, it became clear that this kind of software development was slowing us down. We found that rumour-driven development simply wasn’t scalable.

It was obvious that we, in the infrastructure part of the organization (I’ll call us Platform from now on), needed to promote more alignment in developer tooling. But we needed to go further than that. The blessed or recommended tooling should be easily discoverable. The journey through that tooling should be clear. There should be quality user instructions along the way. And, if users get stuck, where to get support should be obvious.

#### Hello Golden Path

The first Golden Path and Golden Path tutorial was developed six years ago for backend engineering. And like many innovations at Spotify, the embryonic Backend Engineering Golden Path tutorial was created as a Hack Week project. Here are a couple of quotes from the Platform team’s write-up, an internal blog post:

> [We aim] to create great ways for a developer to work and build stuff at Spotify. One of our hard challenges is to unify all the different ways to use our infrastructure and provide tools that make sense to our many squads with very different needs.
> 
> 

> [During Hack Week] eight top engineers gathered their forces and created a tutorial on the recommended way of using our services; it was named “The Golden Path”. This is the way we support an easy and streamlined way of working. If you are an adventurer you can of course leave the Golden Path and do your own thing, but then you will not have the same support. It should be easy to work at Spotify and this tutorial made that happen and brought gold to the people.
> 
> 

It is fascinating to me as a product manager — within the team solving technical documentation and discoverability at Spotify — how the Golden Path concept and the problems that it is solving hold up over time. Most of the above could have been written yesterday.

#### The Golden Path today

There was a time when engineers at Spotify couldn’t imagine life with Golden Paths; now we can’t imagine life without them.

Over the years, the Backend Engineering Golden Path tutorial has grown and we have added Golden Paths for: client development, data engineering, data science, machine learning, and web. Actually, there is a recent addition to the family: audio processing.

The Golden Path — as we define it today — is the ‘opinionated and supported’ path to ‘build something’ (for example, build a backend service, put up a website, create a data pipeline). The Golden Path tutorial is a step-by-step tutorial that walks you through this opinionated and supported path.

The ‘blessed’ tools — those on the Golden Path — are visualized in the Explore section of our internal developer portal, [Backstage](https://backstage.io/). Filtering is available per discipline.

![](https://storage.googleapis.com/production-eng/1/2020/08/7c939580-golden-paths_infrastructure-and-tooling.png)
And the path through the tools is expressed in the Golden Path tutorial — created using TechDocs (Spotify’s docs-like-code tool for technical documentation) and consumed in the above-mentioned Backstage.

![](https://storage.googleapis.com/production-eng/1/2020/08/b829ba5b-golden-path_backend-golden-path.png)
The idea behind having Golden Paths is not to limit or stifle engineers, or set standards for the sake of it. With Golden Paths in place, teams don’t have to reinvent the wheel, have fewer decisions to make, and can use their productivity and creativity for higher objectives. They can get back to moving fast.

Amusingly, the concept of the Golden Path has become so popular and ingrained in our way of working that it has given rise to spin-off concepts such as the Paved Road and Silver Path. We try to steer everybody towards the Golden Path.

#### Success factors of the Golden Path tutorials

As mentioned above, the primary job of the Golden Path tutorials is to walk onboarding engineers through the Golden Path (for their particular engineering discipline). And by most accounts, the tutorials have — over the years — had great success in doing this. The Golden Path tutorials have grown to be seen as Spotify’s most important documentation. Here are the key factors behind the success of the Golden Path tutorials.

##### Clearly defined audience

We write the tutorials with a clear target audience in mind: new engineers at Spotify. This lets us assume a certain knowledge level and informs how we explain things. Other, more experienced engineers read these tutorials, as well — say, an engineer working in a new discipline or someone who wants to see the best way to do something now (versus how they did it five years ago). But primarily, we write with new engineers in mind, which ensures the instructions are clear for everyone.

##### One main purpose

It is really important to know and communicate the purpose of the tutorials. One of the mistakes that we made was losing sight of this purpose. Engineers (and me and my team for that matter) started to ask: What are they? Are they a how-to guide? Are they to show best practice? Are they for education? Are they a reference? Are they all of the above?

I was really struggling with this question. Initially, I settled on: “They are for new hires. And they show how we do things at Spotify.” This was my go-to description, but for some reason, it didn’t sit right. And others didn’t seem to be picking it up. Then, just recently, I spotted how another product manager at Spotify had described the Golden Path and tutorial. It went something like: “The Golden Path is the opinionated and supported path to build your system and the Golden Path tutorial walks you through this path.” Bingo, that was it. I shared it with some others, and got a bunch of thumbs up. This is exactly what we needed. We have our main purpose.

##### Step-by-step-by-step

The tutorial is a step-by-step guide. We are careful to include every step — click here, press enter, and so on — even if doing so can be tedious for the writer and appear cumbersome for the reader. The alternative would be to miss steps and, if you think about it, that’s much more likely to cause confusion. Also, step-by-step is a good way to get clear sight on how long your actual Golden Path is.

##### Be true to the Golden Path

A complaint that we often get is that the tutorials are too long. I am not the combative type, but my response is always the same: The tutorials just reflect the actual Golden Path. That’s what we need to shorten. In other words, as a Platform organization, we need to make the actual Golden Path easier to follow and with fewer steps. And then the tutorials naturally become shorter. But to the point of this success factor, it is important that the Golden Path tutorial reflects the actual Golden Path. When one tool gets swapped out and another swapped in — for example, when we adopted [Kubernetes](https://kubernetes.io/docs/home/) — the Golden Path tutorial should be updated at the same time.

##### One per discipline

As mentioned above, we have one Golden Path tutorial per engineering discipline.

![](https://storage.googleapis.com/production-eng/1/2020/08/eef8c0dd-golden-path_getting-started.png)
It doesn’t have to be done this way, for example, I could imagine a more modular approach — with one Golden Path tutorial per engineering job to be done. Or, slicing it another way, such as one tutorial on testing, one on coding, and so on. We have thought about this a lot — and the per-discipline approach is the one we have stuck to. Even if there is a trend towards more [T-shaped engineers](https://medium.com/@jchyip/why-t-shaped-people-e8706198e437).

##### It’s about education

So what if we do a lot of clever engineering and simplify a Golden Path so much that it takes, say, three clicks to put up a website. Would the Golden Path tutorial be three paragraphs? Or just not be needed? This is an interesting question and one I have debated a lot (admittedly, mainly with myself). Our goal is to help Spotify move faster. So it makes sense for us in the Platform organization to simplify and shorten the Golden Path to help individual contributors move faster. But then we are hiding a lot under the surface. There are a lot of black boxes. And the Golden Path tutorials are also about education. So, yes, we need to make it easier for engineers to build stuff — but it’s important to keep in mind that the tutorials are there to educate (in particular, new hires).

##### Special status

The Golden Path tutorials are an integral and key part of the onboarding process for new engineers. They are highly appreciated as a first task and have proven to be a highly effective way to get engineers up to speed. Going by the data, the Golden Path tutorials are Spotify’s most read and most used technical documentation.

So, in my eyes, they have special status. And we try to get this message across to the teams that write and maintain them. We say to those teams, if you own part of a Golden Path tutorial, and you only have a limited time for working on documentation — work on that.

##### Feedback and testing

As mentioned, the Golden Path tutorials are an integral part of our onboarding process. New engineers are encouraged to do the tutorial corresponding to their primary discipline during their first two weeks. Following that they will attend what we call an Engineering Bootcamp where, together with others over the course of a week, they will use the set of tutorials as the basis for building an end-to-end product. So pretty much every engineer that joins Spotify is exposed to the Golden Path tutorials. This is a key factor in the tutorials’ success. Lots of eyes on the material. Lots of testing of the material. Lots of feedback. And, of course, it’s not just feedback on the tutorial — it’s feedback on the Golden Path itself (which are gold nuggets for the Platform organisation).

#### Future developments

I love our Golden Path concept and our Golden Path tutorials and I am proud of how far we have come. But I also see many areas for innovation and improvement. Here are three; the first two we are actively working on, the third is further away.

##### Improved ownership model

We used to have one technical writer per tutorial. But this didn’t really scale and it turned out that we were neglecting other technical documentation problems that were more Spotify-wide. So we ditched the technical writer model and went for a more centralized model to solve some of these larger issues. And, of course, what happens? We created a second-order problem. Because each tutorial covers the Golden Path for a particular engineering discipline, we needed to distribute content ownership across a wide number of teams. This is okay, in itself, but then we miss coordination at the level of the tutorial (something that the technical writer used to cover) and coordination at the level of the set of tutorials (something that the technical writers together used to cover). We are not about to go back to the old model, but we are looking at ways to address these coordination issues.

##### Golden State

Recently we have been exploring around the concept of what we call a Golden State. A Golden State is a list of checks that engineers can use to know if their systems are following the Golden Path. The ambitious end goal of Golden State is to get most of our engineering organisation to be on the Golden Path. In this way, we reduce the amount of fragmentation in our tech ecosystem – which helps teams lower their maintenance costs. Also, more people using the same thing equates to a higher likelihood that we can automatically upgrade them. And teams definitely want that.

##### End-to-end product Golden Path tutorial

The way that the tutorials are set up currently is to serve individual contributors. But individual contributors are in teams and teams build products (features, run experiments, company bets) and are multi-disciplinary. It is a challenging task, but we are definitely excited by the idea of creating a series of Golden Path tutorials for teams that provide blueprints for building various types of products.

This one is perhaps a long way off — but hey…

“His spice-induced visions show him a myriad of possible futures where humanity has become extinct and only one where humanity survives. He names this future ‘The Golden Path’ and resolves to bring it to fruition.”

Tags: [engineering leadership](https://engineering.atspotify.com/tag/engineering-leadership/)
