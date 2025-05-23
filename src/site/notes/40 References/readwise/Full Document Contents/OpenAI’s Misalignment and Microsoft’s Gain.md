---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/open-ai-s-misalignment-and-microsoft-s-gain/","tags":["rw/articles"]}
---

![rw-book-cover](https://149384716.v2.pressablecdn.com/wp-content/uploads/2023/11/openai-1.png)

I have, as you might expect, authored several versions of this Article, both in my head and on the page, as [the most extraordinary weekend of my career](https://twitter.com/benthompson/status/1726514608234746003) has unfolded. To briefly summarize:

* On Friday, then-CEO Sam Altman was fired from OpenAI by the board that governs the non-profit; then-President Greg Brockman was removed from the board and subsequently resigned.
* Over the weekend rumors surged that Altman was negotiating his return, only for OpenAI to hire former Twitch CEO Emmett Shear as CEO.
* Finally, late Sunday night, [Satya Nadella announced via tweet](https://twitter.com/satyanadella/status/1726509045803336122) that Altman and Brockman, “together with colleagues”, would be joining Microsoft.

This is, quite obviously, a phenomenal outcome for Microsoft. The company already has [a perpetual license to all OpenAI IP](https://www.wsj.com/articles/microsoft-and-openai-forge-awkward-partnership-as-techs-new-power-couple-3092de51) ([short of artificial general intelligence](https://openai.com/our-structure#:~:text=the%20board%20determines%20when%20we%27ve%20attained%20AGI.%20Again%2C%20by%20AGI%20we%20mean%20a%20highly%20autonomous%20system%20that%20outperforms%20humans%20at%20most%20economically%20valuable%20work.%20Such%20a%20system%20is%20excluded%20from%20IP%20licenses%20and%20other%20commercial%20terms%20with%20Microsoft%2C%20which%20only%20apply%20to%20pre%2DAGI%20technology.)), including source code and model weights; the question was whether it would have the talent to exploit that IP if OpenAI suffered the sort of talent drain that was threatened upon Altman and Brockman’s removal. Indeed they will, as a good portion of that talent seems likely to flow to Microsoft; you can make the case that Microsoft just acquired OpenAI for $0 and zero risk of an antitrust lawsuit.[1](#fn1-11944 "Microsoft’s original agreement with OpenAI also barred Microsoft from pursuing AGI based on OpenAI tech on its own; my understanding is that this clause was removed in the most recent agreement")

Microsoft’s gain, meanwhile, is OpenAI’s loss, which is dependent on the Redmond-based company for both money and compute: the work its employees will do on AI will either be Microsoft’s by virtue of that perpetual license, or Microsoft’s directly because said employees joined Altman’s team. OpenAI’s trump card is ChatGPT, which is well on its way to achieving the holy grail of tech — an at-scale consumer platform — but if the reporting this weekend is to be believed, OpenAI’s board may have already had second thoughts about the incentives ChapGPT placed on the company (more on this below).

The biggest loss of all, though, is a necessary one: the myth that anything but a for-profit corporation is the right way to organize a company.

##### OpenAI’s Non-Profit Model

OpenAI was founded in 2015 as a “non-profit intelligence research company.” From the [initial blog post](https://openai.com/blog/introducing-openai):

> 
>  OpenAI is a non-profit artificial intelligence research company. Our goal is to advance digital intelligence in the way that is most likely to benefit humanity as a whole, unconstrained by a need to generate financial return. Since our research is free from financial obligations, we can better focus on a positive human impact. We believe AI should be an extension of individual human wills and, in the spirit of liberty, as broadly and evenly distributed as possible. The outcome of this venture is uncertain and the work is difficult, but we believe the goal and the structure are right. We hope this is what matters most to the best in the field.
> 
> 
> 

I was pretty cynical about the motivations of OpenAI’s founders, at least Altman and Elon Musk; I wrote in a [Daily Update](https://stratechery.com/2015/openai-artificial-intelligence-and-data-data-and-recruiting/):

> 
>  Elon Musk and Sam Altman, who head organizations (Tesla and YCombinator, respectively) that look a lot like the two examples I just described of companies threatened by Google and Facebook’s data advantage, have done exactly that with OpenAI, with the added incentive of making the entire thing a non-profit; I say “incentive” because being a non-profit is almost certainly a lot less about being altruistic and a lot more about the line I highlighted at the beginning: “We hope this is what matters most to the best in the field.” In other words, OpenAI may not have the best data, but at least it has a mission structure that may help idealist researchers sleep better at night. That OpenAI may help balance the playing field for Tesla and YCombinator is, I guess we’re supposed to believe, a happy coincidence.
> 
> 
> 

Whatever Altman and Musk’s motivations, the decision to make OpenAI a non-profit wasn’t just talk: the company is a 501(c)3; you can view their annual IRS filings [here](https://projects.propublica.org/nonprofits/organizations/810861541). The first question on Form 990 asks the organization to “Briefly describe the organization’s mission or most significant activities”; [the first filing in 2016](https://projects.propublica.org/nonprofits/organizations/810861541/201703459349300445/full) stated:

> 
>  OpenAIs goal is to advance digital intelligence in the way that is most likely to benefit humanity as a whole, unconstrained by a need to generate financial return. We think that artificial intelligence technology will help shape the 21st century, and we want to help the world build safe AI technology and ensure that AI’s benefits are as widely and evenly distributed as possible. Were trying to build AI as part of a larger community, and we want to openly share our plans and capabilities along the way.
> 
> 
> 

Two years later, and the commitment to “openly share our plans and capabilities along the way” was gone; three years after that and the goal of “advanc[ing] digital intelligence” was replaced by “build[ing] general-purpose artificial intelligence”.

In 2018 Musk, [according to a Semafor report earlier this year](https://www.semafor.com/article/03/24/2023/the-secret-history-of-elon-musk-sam-altman-and-openai), attempted to take over the company, but was rebuffed; he left the board and, more critically, stopped paying for OpenAI’s operations. That led to the second critical piece of background: faced with the need to pay for massive amounts of compute power, Altman, now firmly in charge of OpenAI, created OpenAI Global, LLC, a capped profit company with Microsoft as minority owner. This image of OpenAI’s current structure is [from their website](https://openai.com/our-structure):

[![OpenAI's corporate structure](https://i0.wp.com/stratechery.com/wp-content/uploads/2023/11/openai-2.png?resize=640%2C464&ssl=1)](https://openai.com/our-structure)

OpenAI Global could raise money and, critically to its investors, make it, but it still operated under the auspices of the non-profit and its mission; OpenAI Global’s operating agreement states:

> 
>  The Company exists to advance OpenAI, Inc.’s mission of ensuring that safe artificial general intelligence is developed and benefits all of humanity. The Company’s duty to this mission and the principles advanced in the OpenAI, Inc. Charter take precedence over any obligation to generate a profit. The Company may never make a profit, and the Company is under no obligation to do so. The Company is free to re-invest any or all of the Company’s cash flow into research and development activities and/or related expenses without any obligation to the Members.
> 
> 
> 

Microsoft, despite this constraint on OpenAI Global, was not only an investor, but also a customer, incorporating OpenAI into all of its products.

##### ChatGPT Tribes

The third critical piece of background is the most well-known, and what has driven those ambitions to new heights: ChatGPT was released at the end of November 2022, and it has taken the world by storm. Today ChatGPT has over 100 million weekly users and over $1 billion in revenue; it has also fundamentally altered the conversation about AI for nearly every major company and government.

What was most compelling to me, though, was the possibility I noted above, in which ChatGPT becomes the foundation of a new major consumer tech company, the most valuable and most difficult kind of company to build. I wrote earlier this year in [The Accidental Consumer Tech Company](https://stratechery.com/2023/the-accidental-consumer-tech-company-chatgpt-meta-and-product-market-fit-aggregation-and-apis/):

> 
>  When it comes to meaningful consumer tech companies, the product is actually the most important. The key to consumer products is efficient customer acquisition, which means word-of-mouth and/or network effects; ChatGPT doesn’t really have the latter (yes, it gets feedback), but it has an astronomical amount of the former. Indeed, the product that ChatGPT’s emergence most reminds me of is Google: it simply was better than anything else on the market, which meant it didn’t matter that it came from a couple of university students (the origin stories are not dissimilar!). Moreover, just like Google — and in opposition to Zuckerberg’s obsession with hardware — ChatGPT is so good people find a way to use it. There isn’t even an app! And yet there is now, a mere four months in, a platform.
> 
> 
> 

The platform I was referring to was [ChatGPT plugins](https://stratechery.com/2023/chatgpt-learns-computing/); it’s a compelling concept with a UI that didn’t quite work, and it was only eight months later at [OpenAI’s first developer day](https://stratechery.com/2023/the-openai-keynote/) that the company announced GPTs, their second take at being a platform. Meanwhile, Altman was reportedly exploring new companies outside of the OpenAI purview to build chips and hardware, apparently without the board’s knowledge. Some combination of these factors, or perhaps something else not yet reported, were the final straw for the board, which, led by Chief Scientist Ilya Sutskever, deposed Altman over the weekend. [The Atlantic reported](https://www.theatlantic.com/technology/archive/2023/11/sam-altman-open-ai-chatgpt-chaos/676050/):

> 
>  Altman’s dismissal by OpenAI’s board on Friday was the culmination of a power struggle between the company’s two ideological extremes—one group born from Silicon Valley techno optimism, energized by rapid commercialization; the other steeped in fears that AI represents an existential risk to humanity and must be controlled with extreme caution. For years, the two sides managed to coexist, with some bumps along the way.
> 
> 
>  This tenuous equilibrium broke one year ago almost to the day, according to current and former employees, thanks to the release of the very thing that brought OpenAI to global prominence: ChatGPT. From the outside, ChatGPT looked like one of the most successful product launches of all time. It grew faster than any other consumer app in history, and it seemed to single-handedly redefine how millions of people understood the threat — and promise — of automation. But it sent OpenAI in polar-opposite directions, widening and worsening the already present ideological rifts. ChatGPT supercharged the race to create products for profit as it simultaneously heaped unprecedented pressure on the company’s infrastructure and on the employees focused on assessing and mitigating the technology’s risks. This strained the already tense relationship between OpenAI’s factions — which Altman referred to, in a 2019 staff email, as “tribes.”
> 
> 
> 

Altman’s tribe — the one that was making OpenAI into much more of a traditional tech company — is certainly the one that is more familiar to people in tech, including myself. I even had a paragraph in my Article about the developer day keynote that remarked on OpenAI’s transition, that I unfortunately edited out. Here is what I wrote:

> 
>  It was around this time that I started to, once again, bemoan [OpenAI’s bizarre corporate structure](https://stratechery.com/2022/dall-e-open-to-all-openai-and-openness-openai-opportunities-and-threats/). As a long-time Silicon Valley observer it is enjoyable watching OpenAI follow the traditional startup path: the company is clearly in the rapid expansion stage where product managers are suddenly considered useful, as they occupy that sweet spot of finding and delivering low-hanging fruit for an entity that doesn’t yet have the time or moat to tolerate kingdom building and feature creep.
> 
> 
>  What gives me pause is that the goal is not an IPO, retiring to a yacht, and giving money to causes that do a better job of soothing the guilt of being fabulously rich than actually making the world a better place. There is something about making money and answering to shareholders that holds the more messianic impulses in check; when I hear that Altman doesn’t own any equity in OpenAI that makes me more nervous than relieved. Or maybe I’m just biased because I won’t have S-1s or 10-Ks to analyze.
> 
> 
> 

Obviously I regret the edit, but then again, I didn’t realize how prescient my underlying nervousness about OpenAI’s structure would prove to be, largely because I clearly wasn’t worried enough.

##### Microsoft vs. the Board

Much of the discussion on tech Twitter over the weekend has been shock that a board would incinerate so much value. First off, Altman is one of the Valley’s most-connected executives, and a prolific fund-raiser and dealmaker; second is the fact that several OpenAI employees already resigned, and more are expected to follow in the coming days. OpenAI may have had two tribes previously; it’s reasonable to assume that going forward it will only have one, led by a new CEO in Shear who puts the probability of AI doom at [between 5 and 50 percent](https://twitter.com/rowancheung/status/1726473420299534491) and has advocated [a significant slowdown in development](https://twitter.com/eshear/status/1703178063306203397).

Here’s the reality of the matter, though: whether or not you agree with the Sutskever/Shear tribe, the board’s charter and responsibility is not to make money. This is not a for-profit corporation with a fiduciary duty to its shareholders; indeed, as I laid out above, OpenAI’s charter specifically states that it is “unconstrained by a need to generate financial return”. From that perspective the board is in fact doing its job, as counterintuitive as that may seem: to the extent the board believes that Altman and his tribe were not “build[ing] general-purpose artificial intelligence that benefits humanity” it is empowered to fire him; they do, and so they did.

This gets at the irony in my concern about the company’s non-profit status: I was worried about Altman being unconstrained by the need to make money or the danger of having someone in charge without a financial stake in the outcome, when in fact it was those same factors that cost him his job. More broadly, my criticism was insufficiently expansive because philosophical concerns about unconstrained power pale — at least in the case of business analysis, Stratechery’s core competency — in the face of how much this structure made OpenAI a fundamentally unstable entity to make deals with. This refers, of course, to Microsoft, and as someone who has been a proponent of Satya Nadella’s leadership, I have to admit that my analysis of the company’s partnership with OpenAI was lacking.

Microsoft had, to its tremendous short-term benefit, bet a substantial portion of its future on its OpenAI partnership. This goes beyond money, which Microsoft has plenty of, and much of which it hasn’t yet paid out (or granted in terms of Azure credits); OpenAI’s technology is built into a whole host of Microsoft’s products, from Windows to Office to ones most people have never heard of (I see you Dynamics CRM nerds!). Microsoft is also investing massively in infrastructure that is custom-built for OpenAI — Nadella has been [touting the financial advantages of specialization](https://stratechery.com/2023/google-earnings-microsoft-earnings-ai-leverage/) — and has [just released a custom chip that was tuned for running OpenAI models](https://www.bloomberg.com/news/articles/2023-11-15/microsoft-unveils-its-first-custom-designed-ai-cloud-chips). That this level of commitment was made to an entity *not* motivated by profit, and thus un-beholden to Microsoft’s status as an investor and revenue driver, now seems absurd.

Or, rather, it did, until Nadella tweeted the following at 11:53pm Pacific:

The counter to the argument I just put forth about Microsoft’s poor decision to partner with a non-profit is the reality of AI development, specifically the need for massive amounts of compute. It was the need for this compute that led OpenAI, which had barred itself from making a traditional venture capital deal, to surrender their IP to Microsoft in exchange for Azure credits. In other words, while the board may have had the charter of a non-profit, and an admirable willingness to act on and stick to their convictions, they ultimately had no leverage because they weren’t a for-profit company with the capital to be truly independent.

The end result is that an entity committed by charter to the safe development of AI has basically handed off all of its work and, probably soon enough, a sizable portion of its talent, to one of the largest for-profit entities on earth. Or, in an AI-relevant framing, the structure of OpenAI was ultimately misaligned with fulfilling its stated mission. Trying to organize incentives by fiat simply doesn’t account for all of the possible scenarios and variable at play in a dynamic situation; harvesting self-interest has, for good reason, long been the best way to align individuals and companies.

##### Altman Questions

There is one other angle of the board’s actions that ought to be acknowledged: it very well could have been for cause. I endorse [Eric Newcomer’s thoughtful column on his eponymous Substack](https://www.newcomer.co/p/give-openais-board-some-time-the):

> 
>  In its [statement](https://openai.com/blog/openai-announces-leadership-transition), the board said it had concluded Altman, “was not consistently candid in his communications with the board.” We shouldn’t let poor public messaging blind us from the fact that Altman has lost confidence of the board that was supposed to legitimize OpenAI’s integrity…
> 
> 
>  My understanding is that some members of the board genuinely felt Altman was dishonest and unreliable in his communications with them, sources tell me. Some members of the board believe that they couldn’t oversee the company because they couldn’t believe what Altman was saying. And yet, the existence of a nonprofit board was a key justification for OpenAI’s [supposed trustworthiness](https://x.com/martin_casado/status/1723112508234539270?s=20).
> 
> 
>  I don’t think any of us really knows enough right now to urge the board to make a hasty decision. I want you to consider a couple things here:
> 
> 
> 

Newcomer notes the board’s charter that I referenced above, the fact that Anthropic’s founders felt it necessary to leave OpenAI in the first place, Musk’s antipathy towards Altman, and Altman’s still [somewhat murky and unexplained exit from YCombinator](https://www.newcomer.co/p/odds-and-ends?nthPub=1251). Newcomer concludes:

> 
>  I’m sure that writing this cautionary letter will not make me popular in many corners of Silicon Valley. But I think we should just slow down and get more facts. If OpenAI leads us to artificial general intelligence or anywhere close, we will want to have taken the time to think for more than a weekend about who we want to take us there…
> 
> 
>  Altman had been given a lot of power, the cloak of a nonprofit, and a glowing public profile that exceeds his more mixed private reputation. He lost the trust of his board. We should take that seriously.
> 
> 
> 

Perhaps I am feeling a bit humbled by the aforementioned miss in my Microsoft analysis — much less my shock at the late night reversal in fortunes — but I will note that [I have staked my claim](https://stratechery.com/2023/attenuating-innovation-ai/) in opposition to AI doomers and the call for regulation; to that end, I am wary of a narrative that confirms my priors about what drove the events of this weekend. And, I would note, I remain concerned about the philosophical question of executives who seek to control incredible capabilities without skin in the game.

To that end, a startup ecosystem fixture like Altman going to work for Microsoft is certainly surprising: that Microsoft is the one place that retains access to OpenAI’s IP, and can combine that with effectively unlimited funding and GPU access, certainly adds credence to the narrative that power over AI is Altman’s primary motivation.

##### The Altered Landscape

What is clear is that Altman and Microsoft are in the driver seat of AI. Microsoft has the IP and will soon have the team to combine with its cash and infrastructure, while shedding coordination problems inherent in their partnership with OpenAI previously (and, of course, they are still partners with OpenAI!).

I’ve also argued for a while that it made more sense for external companies to build on Azure’s API rather than OpenAI’s; Microsoft is a development platform by nature, whereas OpenAI is fun and exciting but likely to clone your functionality or deprecate old APIs. Now the choice is even more obvious. And, from the Microsoft side, this removes a major reason for enterprise customers, already accustomed to evaluating long-term risks, to avoid Azure because of the OpenAI dependency; Microsoft now owns the full stack.

Google, meanwhile, might need to make some significant changes; the company’s latest model, Gemini, has been delayed, and its Cloud business has been slowing as spending shifts to AI, the exact opposite outcome the company had hoped for. How long will the company’s founders and shareholders tolerate the perception that the company is moving too slow, particularly in comparison to the nimbleness and willingness to take risks demonstrated by Microsoft?

That leaves Anthropic, which looked like a big winner 12 hours ago, and now feels increasingly tenuous as a standalone entity. The company has struck partnership deals with both Google and Amazon, but it is now facing a competitor in Microsoft with effectively unlimited funds and GPU access; it’s hard not to escape the sense that it makes sense as a part of AWS (and yes, B corps can be acquired, with considerably more ease than a non-profit).

Ultimately, though, one could make the argument that not much has changed at all: it has been apparent [for a while](https://stratechery.com/2023/ai-and-the-big-five/) that AI was, at least in the short to medium-term, a sustaining innovation, not a disruptive one, which is to say it would primarily benefit and be deployed by the biggest companies. The costs are so high that it’s hard for anyone else to get the money, and that’s even before you consider questions around channel and customer acquisition. If there were a company poised to join the ranks of the Big Five it was OpenAI, thanks to ChatGPT, but that seems less likely now (but not impossible). This, in the end, was Nadella’s insight: the key to winning if you are big is not to invent like a startup, but to leverage your size to acquire or fast-follow them; all the better if you can do it for the low price of $0.

##### *Related*
