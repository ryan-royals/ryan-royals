---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/ethical-web-principles/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.w3.org/favicon.ico)

#### Abstract

The web should be a platform that helps people and provides a positive social benefit. As we continue to evolve the web platform, we must therefore consider the consequences of our work. The following document sets out ethical principles that will drive W3C's continuing work in this direction.

#### Status of This Document

*This section describes the status of this document at the time of its publication. A list of current W3C publications and the latest revision of this technical report can be found in the [W3C technical reports index](https://www.w3.org/TR/) at https://www.w3.org/TR/.*

This document is a Technical Architecture Group (TAG) Finding. It does not contain any normative content.

This document reflects the consensus of the TAG at the time of publication. It will continue to evolve and the TAG will issue updates as often as needed.

This document was published by the [Technical Architecture Group](https://www.w3.org/groups/other/tag) as a Statement using the [Note track](https://www.w3.org/policies/process/20231103/#recs-and-notes).

A W3C Statement is a specification that, after extensive consensus-building, is endorsed by W3C and its Members.

The [W3C Patent Policy](https://www.w3.org/policies/patent-policy/) does not carry any licensing requirements or commitments on this document.

This document is governed by the [03 November 2023 W3C Process Document](https://www.w3.org/policies/process/20231103/).

#### 1. Introduction

The web should empower an equitable, informed, and interconnected society. It has been, and should continue to be, designed to enable communication and knowledge-sharing for everyone. In order for the web to continue to be beneficial to society, we need to consider the ethical implications of our work when we build web technologies, applications, and sites.

The web is made up of a number of technologies and technical standards. HTML, CSS, and JavaScript are often thought of as the web's core set of technologies but there are many other technologies, standards, languages and APIs that come together to form the "web platform." We strive to maintain a strong ethical framework as a differentiator for the web platform, for example an emphasis on [internationalization](https://www.w3.org/International/), [accessibility](https://www.w3.org/WAI/), [privacy](https://www.w3.org/Privacy/), and [security](https://www.w3.org/Security/). Web technologies are also released for use under a [royalty-free license](https://www.w3.org/Consortium/Patent-Policy/) to enable open source implementation. We build new web technologies in a collaborative manner according to open processes (for example, the [W3C process](https://www.w3.org/Consortium/Process/)), and in inclusive environments adhering to codes of conduct (such as the W3C [Code of Conduct](https://www.w3.org/policies/code-of-conduct/)).

These are often cited as some of the strengths of the web. Despite this, in the 30 years since the development of the web began, it has become clear that the web platform can often be used in ways that subvert its original mission or even be used to cause harm.

The architecture of the web is designed with the notion of different classes of application that retrieve and process content, and represent the needs of the application's users. This includes web browsers, web-hosted applications such as search engines, and software that acts on web resources. This lends itself well towards empowering people by allowing them to choose the browser, search engine, or other application that best meets their needs (for example, with strong privacy protections).

The web should also support human rights, dignity, and personal agency. We need to put internationally recognized human rights at the core of the web platform [[UDHR](https://www.w3.org/TR/ethical-web-principles/#bib-udhr)]. We can reinforce this approach by promoting ethical thinking across the web industry.

The principles in this document are deliberately unordered, and many are interconnected with each other. They are intended to be read together, rather than each in isolation, and to collectively support a web that is beneficial for society. When the effects of upholding one principle may diminish the efficacy of another principle, the benefits and tradeoffs need to be carefully balanced. It is important to consider the context in which the technology is being applied, the expected audience(s) for the technology, who the technology benefits and who it may disadvantage, and any power dynamics involved (see also the [priority of constituencies](https://www.w3.org/TR/design-principles/#priority-of-constituencies)).

This is a statement of the ethical principles of the W3C community. Spec developers, authors, and reviewers can use it to guide their thinking. In particular, the purpose of this document is to inform wide review of new charters, new specifications, and updates to published recommendations. Others can read this document to understand how we are informing our design process with ethical considerations.

For actionable guidance applicable to spec editors, site authors, and others designing and building parts of the web platform, see the [Web Platform Design Principles](https://www.w3.org/TR/design-principles/), [Self-Review Questionnaire: Security and Privacy](https://www.w3.org/TR/security-privacy-questionnaire/), the [Privacy Principles](https://www.w3.org/TR/privacy-principles/), and [TAG Findings](https://tag.w3.org/findings/).

#### 2. Principles

##### 2.1 There is one web

When we are adding new web technologies and platforms, we will build them to cross regional and national boundaries. People in one location should be able to view web pages from anywhere that is connected to the web.

##### 2.2 The web does not cause harm to society

When we are adding a feature or technology to the web, we will work to prevent or mitigate any harm it might cause society or groups, especially to vulnerable people. We consider a range of threat models that account for abuse scenarios at different scales, from societal to interpersonal. We will prioritize potential benefits for web users over potential benefits to web developers, content providers, user agents, advertisers, or others in the ecosystem, in line with the [priority of constituencies](https://www.w3.org/TR/design-principles/#priority-of-constituencies). We commit to learning about and understanding diverse perspectives, and will strive to reflect a respect for that diversity in the designs we produce, so that our designs properly respect the interests and views of all of the people who might be affected by them.

##### 2.3 The web supports healthy community and debate

We are building technologies and platforms for distributing ideas, for virtual interaction, and for mass collaboration on any topic. While those tools can be used for good, they can also be used for spreading misinformation, revealing private personal information (doxing), harassment, and persecution. We will consider these risks in the work we do, and will build web technologies and platforms that respect individuals' rights and provide features to empower them against dangers like these.

##### 2.4 The web is for all people

People should not need a high level of technical literacy to use the web. Web platform technologies should behave consistently and intuitively. We will build internationalization and localization capabilities into our specifications and websites, including support for different languages. Our specifications and websites are well internationalized, provide support for language and cultural adaptation, and support localization, so that our work is accessible to all users, regardless of language, writing system, or culture. We will accommodate people on low bandwidth networks and with low specification equipment. The web platform and the tools we use to create it must be accessible to people with disabilities, including visual, auditory, physical, speech, cognitive, language, learning, and neurological disabilities. Anyone should be able to meaningfully participate in the creation of specifications, user agents, and content, and the platform should enable a fully accessible end-user experience.

##### 2.5 The web is secure and respects people's privacy

When we add features to the web platform, we are making decisions that impact people's ability to control their personal data. This data includes their conversations, their financial transactions and how they live their lives. We will start by creating web technologies that create as few potential threats to web users as possible, and mitigate the threats that we cannot avoid. We will make sure people understand what risks they are taking when they use the web.

##### 2.6 The web enables freedom of expression

We will create web technologies and platforms that encourage free expression. Our work should not enable state censorship, [surveillance](https://www.rfc-editor.org/rfc/rfc7258#section-1) or other practices that seek to limit this freedom. This principle must be balanced with respect for other human rights and does not imply that individual services on the web must therefore support all speech.

##### 2.7 The web makes it possible to verify information

Society relies on the integrity of public information. We have a responsibility to build web technologies to counter attempts to mislead, deliberate or inadvertent, and to maintain the integrity of information for public good. The public needs verifiable source and context information to recognize trustworthy web publishers and content. The concept of origin and [its relationship with information sources](https://www.w3.org/2001/tag/doc/distributed-content/) are core to the web's security model.

##### 2.8 The web enhances individuals' control and power

We recognize that web technologies can be used to manipulate and deceive people, complicate isolation, and encourage addictive behaviors. We seek to mitigate against these potential abuses and [patterns](https://en.wikipedia.org/wiki/Dark_pattern) when creating new technologies and platforms, and avoid introducing technologies that increase the chance of people being harmed in this way. We aim to reduce centralization in web architecture, minimizing single points of failure and single points of control. We will also build web technologies for individual developers as well as for developers at large companies and organizations. The web should enable do-it-yourself developers.

##### 2.9 The web is an environmentally sustainable platform

Web technologies may have overall positive environmental impacts as well as negative impacts. These can change over time and vary geographically as both web and environmental technologies develop. We will endeavor not to do further harm to the environment when we introduce new technologies to the web and keep in mind that people most affected by the environmental consequences of new technologies may not be those who benefit from the features introduced. This includes, but is not limited to, lowering carbon emissions by minimizing data storage and processing requirements, as well as reducing electronic waste by maximizing the lifespan of physical devices through backwards compatibility.

##### 2.10 The web is transparent

The web was built on a "view source" principle, currently realized through robust developer tools built into many browsers. We will always make sure it is possible to determine how a web application was built and how the code works. Furthermore, we will always make sure it is possible to audit and inspect web applications and underlying software for security, privacy, or other considerations.

##### 2.11 The web is multi-browser, multi-OS, and multi-device

We will not create web technologies that encourage the creation of websites that work only in one browser, or only on particular hardware. We expect that content provided by accessing a URL [should yield a thematically consistent experience](https://www.w3.org/TR/mobile-bp/#tc) when someone is accessing it from different devices. The existence of multiple interoperable implementations enables competition, and thus a variety of choices for web users.

##### 2.12 The web can be consumed in any way that people choose

People must be able to change web pages according to their needs. For example, people should be able to install style sheets, assistive browser extensions, and blockers of unwanted content or scripts. We will build features and write specifications that respect people's agency, and will create user agents to represent those preferences on the web user's behalf.

The TAG would like to thank the following people for their help, input, and feedback during the conceptualization and ongoing development of this document: Tantek Çelik (Mozilla), Oluwatomisin Niyi-Awosusi, Joanna J. Bryson (Professor of Ethics and Technology, Centre for Digital Governance, Hertie School), Wendy Seltzer.

##### B.1 Informative references

[design-principles] [Web Platform Design Principles](https://www.w3.org/TR/design-principles/). Lea Verou. W3C. 18 July 2024. W3C Working Group Note. URL: <https://www.w3.org/TR/design-principles/> [mobile-bp] [Mobile Web Best Practices 1.0](https://www.w3.org/TR/mobile-bp/). Jo Rabin; Charles McCathieNevile. W3C. 29 July 2008. W3C Recommendation. URL: <https://www.w3.org/TR/mobile-bp/> [Privacy-Principles] [Privacy Principles](https://www.w3.org/TR/privacy-principles/). Robin Berjon; Jeffrey Yasskin. W3C. 20 November 2024. W3C Working Group Note. URL: <https://www.w3.org/TR/privacy-principles/> [RFC7258] [Pervasive Monitoring Is an Attack](https://www.rfc-editor.org/rfc/rfc7258). S. Farrell; H. Tschofenig. IETF. May 2014. Best Current Practice. URL: <https://www.rfc-editor.org/rfc/rfc7258> [security-privacy-questionnaire] [Self-Review Questionnaire: Security and Privacy](https://www.w3.org/TR/security-privacy-questionnaire/). Theresa O'Connor; Peter Snyder. W3C. 16 December 2021. W3C Working Group Note. URL: <https://www.w3.org/TR/security-privacy-questionnaire/> [UDHR] [Universal Declaration of Human Rights](https://www.un.org/en/universal-declaration-human-rights/). United Nations. URL: <https://www.un.org/en/universal-declaration-human-rights/>
