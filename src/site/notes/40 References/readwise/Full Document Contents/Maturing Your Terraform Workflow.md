---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/maturing-your-terraform-workflow/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.hashicorp.com/favicon.svg)

[Platform teams are now widespread](https://www.hashicorp.com/state-of-the-cloud#92percent-of-organizations-are-adopting,-standardizing,-or-scaling-platform-teams), standardizing organizational approaches to the cloud. But as platforms expand, they often struggle to reach the desired levels of scale. Adoption slows as subject matter experts (SMEs) get burdened with support requests. Governance teams become a bottleneck on the path to production, slowing the release cycle.

Highly cloud mature organizations don’t suffer like this. They recognize that different concerns are at play when operating at scale and adapt their processes to deliver at a faster pace. The role that [HashiCorp Terraform](https://www.terraform.io/) plays in this should not be underestimated. By codifying and standardizing an organization’s infrastructure and compliance rules, developers can be free to do what they want to: add business value by writing code. 

What does that mean in practice? How can an organization mature quickly, become a high performer, and scale its platform? This blog post looks at some of the patterns and techniques that we see in high-maturity organizations and provides ideas on how enterprises can make the best use of Terraform.

#### Guiding principles

Left to grow organically, cloud platforms can end up wild and hard to use. But rigidly enforcing standards can lead to a platform that doesn’t meet customer needs, ultimately encouraging [shadow IT](https://en.wikipedia.org/wiki/Shadow_IT). Instead, platform teams in organizations with high cloud maturity typically adopt a set of guiding principles — like the ones laid out below — that strike a balance between the two extremes. Principles like these help to shape the culture of a cloud platform, influencing its developers to help it meet the needs of both the organization and its customers (application teams).

##### Standardization

Two anti-patterns often arise as organizations increase the use of their platform and start to scale: first module proliferation, then mega-modules.

Module proliferation happens when developers discover [the benefits of Terraform modules](https://developer.hashicorp.com/terraform/tutorials/modules/module#what-are-modules-for) and start creating them. Without centralized coordination, the path of least resistance is often to create a new module instead of trying to reuse one that doesn’t quite fit requirements. The sprawl of similar-looking modules can become difficult to use and a maintenance headache. 

In an attempt to fix this sprawl, mega-modules arise as platform teams consolidate overlapping modules hoping to reduce proliferation and encourage code reuse. These bloated mega-modules aim to cover every possible use case but often become overly brittle and complex.

To address these problems, cloud mature organizations apply the [Pareto Principle](https://en.wikipedia.org/wiki/Pareto_principle) to module design. Use case analysis shows that the vast majority of modules need just a handful of inputs to meet most customer requirements. Focusing on this “easy 80%” of use cases results in neat, concise modules that are simple to understand and use. It also causes modules to become more opinionated, which guides developers into a standard pattern, bringing consistency around how infrastructure is used in the organization. 

Gradually, more than just code can be shared. Best practices start to emerge. Runbooks and documentation are made consistent. Golden paths are created.

##### Golden paths

Famously, Spotify addressed its scale problems with [golden paths](https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem/). Cloud mature organizations find they can do the same with their Terraform modules to scale out and increase delivery velocity. Following the golden path model, Terraform modules should be easily discoverable (typically via an [internal module registry](https://developer.hashicorp.com/terraform/registry/private)), with a clear journey through the module, high-quality user instructions, and an obvious way to find support.

Modules like these provide an easy route for developers wanting to use them and encourage developers to reuse code rather than reinvent the wheel. As always, some edge cases won’t be able to use a module without making the interface too complex. But that’s OK. Developers should be free to leave the golden path and follow their own route when necessary. It’s worth checking back every so often, though, to make sure the golden path modules still cater to the majority of use cases.

##### Developer experience

Application teams inside an organization are a captive audience, but that is no excuse to ignore the developer experience. Modules that are easy to understand help to lower the learning curve for new users. They help developers to help themselves, easing the support burden on SMEs. They bring more joy, satisfaction, and engagement both for those using a module, and those maintaining it.

[The Technology Acceptance Model (TAM)](https://open.ncl.ac.uk/theories/1/technology-acceptance-model/) suggests that adoption is predicted on how much people see something as being useful and easy to use. Standardization and golden paths address both these factors and make adoption of a module more likely. But there is much more that can be done to make modules easy to use. For example: 

* The API of a Terraform module should help developers use it correctly, through variable validation and sensible default values for variables.
* Terraform repositories should have a consistent folder and file structure.
* Terraform code comments [should clearly explain](https://blog.codinghorror.com/code-tells-you-how-comments-tell-you-why/) *why* a decision has been taken, when the code itself is unclear.
* Proper [bounds checking and error checking](https://developer.hashicorp.com/terraform/language/expressions/custom-conditions) will help catch common input mistakes.
* Storing user-facing documentation and code samples in the module repository makes it easier to remember to update them.

A relentless focus is needed to maintain good experience and make sure that every change to a module considers how its users will be affected.

##### Product management

Standardization, golden paths, and a great developer experience won’t just happen overnight. Constant planning, coordination, and oversight are needed to reach true scale. In other words, each Terraform module needs to be a component of a comprehensive [infrastructure product](https://www.thoughtworks.com/insights/articles/infrastructure-as-product), with an assigned product owner. This person takes accountability for a module’s interface, its roadmap, and its maintenance. To form a cohesive product offering, cloud mature organizations also place [policy as code](https://docs.hashicorp.com/sentinel/concepts/policy-as-code), documentation, examples, and developer advocacy under the accountability of the product owner.

#### Common advanced patterns

Everything described so far will help an organization through its crawl, walk, run journey with a cloud platform. But for some organizations, that isn’t enough. They want to fly. These advanced patterns use Terraform modules to scale by removing even more toil and manual process from a delivery pipeline. They enable application teams to quickly deploy infrastructure that complies with organizational policies, follows best practices, and doesn’t require a steep learning curve or specialist knowledge.

##### Cohesive modules

Cohesion means that related parts of a code base are kept in a single place. When thinking about infrastructure as a product, this means that all concerns making a ‘unit’ of infrastructure should live in the same Terraform module. For example, say you have a Terraform module that creates [Azure Cosmos PostgreSQL](https://learn.microsoft.com/en-us/azure/cosmos-db/postgresql/introduction) databases. You could use the [DataDog Terraform provider](https://registry.terraform.io/providers/DataDog/datadog/latest) to ensure the [key health metrics](https://www.datadoghq.com/blog/azure-cosmos-db-postgresql/) of every database are monitored by default. You could also use the [HashiCorp Vault Terraform provider](https://registry.terraform.io/providers/hashicorp/vault/latest) to [manage the root credentials](https://developer.hashicorp.com/vault/api-docs/secret/databases#rotate-root-credentials) and issue [on-the-fly dynamic credentials](https://developer.hashicorp.com/vault/docs/secrets/databases/postgresql) for users, bringing security best practices right out of the box. With [thousands of providers](https://registry.terraform.io/browse/providers) in the Terraform ecosystem, almost any technology can be configured in code. Introducing standard patterns like these into a module can reduce the toil of common scenarios and help developers follow best practices by default.

##### Compliant modules

Shifting left doesn’t just apply to security or application testing. Mature organizations accelerate application delivery by shifting compliance left in this manner as well. Lengthy governance processes can be simplified by writing compliance policies as code, instead of repeating them manually for every deployment. Slow release cycles can be accelerated — even in highly regulated industries — if compliance can be guaranteed during the development phase.

##### Architecture blueprints

Some highly cloud mature organizations go further still. If Terraform modules serve as the LEGO blocks that build applications, then architecture blueprints are the instruction manual that defines how to link them together. As common architectural patterns emerge, they can be codified into a standalone infrastructure product that binds multiple blocks together into a complete solution. A module of modules.

So long as these patterns remain standardized across the organization, they can supercharge application delivery. A product owner can ensure the pattern meets the organization’s governance, risk, and compliance requirements, and application teams can simply consume the pattern and fast-track into production.

#### Common blockers

While these advanced patterns may sound idealistic and aspirational, they really do work in practice and many organizations are already benefiting. In cases where those benefits are slow to appear, technology is rarely the barrier — process is. Here are some frequently raised reasons organizations fail to mature their processes using these approaches, and ways to overcome the blocker:

##### The platform team is too busy

Platform teams are often small and have many competing priorities. They can be so busy that there is no time to mature their use of modules. But, like [sharpening the axe](https://www.clairenewton.co.za/my-articles/the-wood-cutter-stories.html#h4-have-you-sharpened-your-axe), taking time out to improve the platform can pay dividends later on. It’s hard to improve a platform when the team is always in fire-fighting mode. Technical debt has to be paid down.

##### No one wants to use our common modules

The Roman poet Juvenal said: “[Give them bread and circuses and they will never revolt.](https://en.wikipedia.org/wiki/Bread_and_circuses)” A good product owner is essential to make sure that a common Terraform module is both useful and easy to use. Give developers what they want, make it easy for them to use, and they will have no reason to resort to shadow IT.

##### There is too much maintenance

Keeping modules evergreen, useful, and easy to use is not effortless. But maintaining one module is much easier than maintaining several. Cloud mature organizations recognize that Terraform code is being maintained in many different places, and that centralizing the effort makes more sense.

Good product owners encourage contributions from their community, using the [inner source model](https://en.wikipedia.org/wiki/Inner_source) to distribute the burden of maintenance. Automation tools like [Dependabot](https://github.com/dependabot) help take the burden out of finding and applying version updates.

##### Developers can’t be trusted

Low-maturity organizations struggle when application teams are not trusted to make changes directly in production without oversight and a separate team is needed to approve and deploy the changes.

Automation helps drive organizations toward high maturity. Since infrastructure is written in Terraform, the subject matter experts and governance teams codify their rules and inject them into the deployment pipeline. If a block of Terraform doesn’t meet compliance requirements, it won’t get deployed. Developers are trusted to make changes because automated checks prove that the changes are OK: [Trust, but verify](https://en.wikipedia.org/wiki/Trust,_but_verify).

#### How to get started

The end goal is attractive: developer self-service, at scale, in a safe, compliant environment. But getting there takes time and resources. Careful planning can help you deliver business value more quickly.

To prioritize, it’s important to understand how the platform will be used. Should a developer (with sufficient guardrails) be able to deploy straight into production? Or should some kind of manual quality gate always exist? Are governance teams able and willing to work with the platform team to codify compliance checks?

[Terraform training](https://www.hashicorp.com/customer-success/enterprise-academy) for SMEs and governance teams can yield great benefits. By shifting left and codifying their work, the governance bottleneck can be reduced or removed. Traditionally, infrastructure as code is the domain of a small group of DevOps engineers in platform and application teams. Cloud mature organizations understand the business value that codification brings and work to remove delivery constraints. Empowering specialists to write their own Terraform code with the platform team can help to deliver more value at a higher velocity.

[Value-stream mapping](https://en.wikipedia.org/wiki/Value-stream_mapping) is a useful practice to highlight the worst bottlenecks and gates in the software development lifecycle. Targeting and automating away the biggest time wasters can yield quick and impactful results. Delivering business value in this way showcases the benefits of this approach, which results in more buy-in and commitment from stakeholders.

[HashiCorp Professional Services](https://www.hashicorp.com/customer-success/professional-services) can guide you towards Terraform maturity and best practices by using our industry experience and understanding of how customers use our products. We have real-world experience of these techniques and look forward to helping steer you on the right path.
