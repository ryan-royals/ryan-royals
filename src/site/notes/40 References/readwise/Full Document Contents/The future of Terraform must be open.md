---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/the-future-of-terraform-must-be-open/","tags":["rw/articles"]}
---

![rw-book-cover](https://miro.medium.com/v2/resize:fit:1200/1*-IYy8o8grCs4cJYzVYbNcA.jpeg)

#### Our plan and pledge to keep Terraform open source

![](https://miro.medium.com/v2/resize:fit:700/1*-IYy8o8grCs4cJYzVYbNcA.jpeg)
On August 10, 2023, HashiCorp announced that after ~9 years of Terraform being open source under the MPL v2 license, they were suddenly switching it to a non open source BSL v1.1 license. We believe the BSL license is a poison pill for Terraform which threatens the entire community and ecosystem, and in this blog post, we’ll introduce [OpenTF](https://opentf.org/), our plan for keeping Terraform open source—forever.

### Why the BSL license is a poison pill for Terraform

#### The virtuous cycle of open source

Terraform was originally released under the [Mozilla Public License](https://www.mozilla.org/en-US/MPL/2.0/FAQ/) (MPL) v2.0, which is a well-known, trusted, and permissive open source license: MPL allows you to use Terraform for just about any purpose and incorporate it into any product, including copying, modifying, and redistributing the code. The only limitation is that if you modify the source code of Terraform itself, you have to release those modifications under the same MPL license.

The permissive terms of this license were a key factor in why the community adopted Terraform:

* Companies were comfortable in adopting Terraform, as the license ensured there would be no unexpected fees or IP problems.
* Developers were comfortable in contributing to [Terraform core](https://github.com/hashicorp/terraform/) (which had 1,700+ contributors as of this writing) and the hundreds of Terraform providers (the [AWS provider](https://github.com/hashicorp/terraform-provider-aws) had 2,800+ contributors and the [Azure provider](https://github.com/hashicorp/terraform-provider-azurerm) had 1,300+ contributors as of this writing), as the license ensured they’d be able to use their work in both their current jobs and any future ones.
* Vendors created tools, modules, and extensions for Terraform (e.g., at Gruntwork, we created [Terragrunt](https://terragrunt.gruntwork.io/), [Terratest](https://terratest.gruntwork.io/), and the [IaC Library](https://gruntwork.io/infrastructure-as-code-library/)), as the license ensured you’d be able to use this work, whether for fun (e.g., as part of a side project) or profit (e.g., as part of a proprietary project).

This led to a virtuous cycle: as more companies adopt Terraform, more developers start using it; those developers contribute to Terraform, fixing bugs, improving security, adding new features, creating new tools and extensions, etc.; that makes Terraform even more compelling, so even more companies adopt it, and the cycle continues. As a result, Terraform has become one of the most popular infrastructure as code (IaC) tools on the market.

**But none of this would have happened if Terraform hadn’t been released under a truly open source license**. Those companies wouldn’t have adopted it; those developers wouldn’t have contributed to it; I can say for certain we would’ve never built Terragrunt, Terratest, and the IaC Library, or even written [*Terraform: Up & Running*](https://www.terraformupandrunning.com/), if Terraform hadn’t been open source.

#### The move to BSL

After ~9 years of seeing the virtuous cycle of open source in action, we were shocked to hear HashiCorp’s [announcement](https://www.hashicorp.com/blog/hashicorp-adopts-business-source-license) that they were suddenly switching Terraform to the [Business Source License](https://www.hashicorp.com/bsl) (BSL) v1.1, which is *not* an open source license ([HashiCorp’s own FAQ](https://www.hashicorp.com/license-faq#details-on-nomenclature) even says the BSL doesn’t meet the definition of open source). In fact, not only Terraform, but all other core HashiCorp products are moving to BSL too: e.g., Vault, Consul, Nomad, etc.

To some extent, we understand what led HashiCorp in this direction. They are trying to maintain a delicate balance: on the one hand, they are creating amazing value by providing high quality, free, open source software to a community of thousands of developers; on the other hand, they are trying to run a sustainable business, so they need to capture and monetize some of the value they create.

The tricky part is deciding what to make open source and what to commercialize. If you make too much open source, then you don’t have enough to sell, so you can’t make enough money to pay the very employees who are creating and maintaining these amazing open source projects, so everyone loses; but if you make too little open source, then you never build up a community, and without that community, you can’t sell enough, can’t pay employees, and again, everyone loses. It’s only when you get this balance just right that everyone wins.

Up until last Friday, it seemed like HashiCorp had this balance just right. They did so by making most functionality open source, but reserving some functionality solely for their commercial products, such as Terraform Cloud and Terraform Enterprise. With this approach, the Terraform community grew, companies that used Terraform grew, and, of course, HashiCorp grew into a public, multi-billion dollar company. Everyone wins!

That’s why we’re so stumped about the sudden move away from an open source license to a non open source BSL license. We believe that this move away from open source will upset the delicate balance and will lead to a scenario where everyone loses: the community will lose, companies that use Terraform will lose, and ultimately, even HashiCorp will lose. Let’s discuss why.

#### The problems with BSL

The BSL license, along with the additional use grants HashiCorp wrote for it, is generally fairly permissive, allowing you to copy, modify, and redistribute the code. However, there is an exception. The license does *not* allow you to use Terraform if you meet both of the following conditions:

1. You are building a product that is competitive with HashiCorp.
2. You embed or host Terraform in your product.

**The first problem is that the terms of the BSL and the use grants are vague.** What does “competitive with HashiCorp” mean and who decides that? And what does “embed or host” mean? If you’re a lawyer and you see this, you start to sweat. The number of questions is infinite. For example, if you’re an independent software vendor (ISV) or managed service provider (MSP) in the DevOps space, and you use Terraform with your customers (but not necessarily Terraform Cloud/Enterprise), are you a competitor? If your company creates a CI / CD product, is that competitive with Terraform Cloud or Waypoint? If your CI / CD product natively supports running Terraform as part of your CI / CD builds, is that embedding or hosting? If you built a wrapper for Terraform, is that a competitor? Is it embedding only if you include the source code or does using the Terraform CLI count as embedding? What if the CLI is installed by the customer? Is it hosting if the customer runs your product on their own servers?

It’s not an accident that these terms are vague. This is a common practice used by many legal teams to implicitly force you to ask the company for permission, so they can decide on a case-by-case basis: [HashiCorp’s FAQ](https://www.hashicorp.com/license-faq#details-on-nomenclature) even says that to get clarification on whether what you’re doing is competitive or embedding or hosting, you need to reach out to [licensing@hashicorp.com](mailto:licensing@hashicorp.com).

**And that leads to the second problem with the BSL: whether your usage complies with the license isn’t determined by the legal terms, but instead is entirely at the whim of HashiCorp.** If HashiCorp doesn’t think you’re a competitor, you’re in the clear. But if they feel threatened by your company: no Terraform for you. If they want to define your usage as embedding or hosting: no Terraform for you. Or perhaps they grant you a license to use Terraform, but only at a fee, and if you can’t pay that fee: no Terraform for you.

**And that brings us to the third, and worst problem with the BSL: HashiCorp can change its decisions at any time.** Perhaps HashiCorp told you your usage was safe before, but a year later, you launched a new product and now they think you’re a competitor, so suddenly, your usage no longer complies with the license. Or perhaps you didn’t change anything on your end, but it’s HashiCorp that launched a new product, which just so happens to be in your market, so now you’re a competitor, and your usage is no longer allowed. Or maybe HashiCorp decides that all the usages that were OK before will now cost money. Or maybe you’ve already been paying them for a license, but suddenly, they decide to raise prices. And no matter what else happens, or what previous decisions or agreements you’ve reached, remember, HashiCorp can just change the license again at any time!

**As a result of the change to BSL, there is now no certainty with using Terraform:**

* If you’re a CTO, and you’re picking an IaC tool to use at your company, if you see that Terraform is BSL licensed, why take the risk? You’re now much more likely to go with alternative tools that are truly open source and have no licensing headaches.
* If you’re on the legal team at a company and reviewing the licenses your dev team wants to use, and you see BSL, why take the risk? You’re now much more likely to push back and put BSL on the banned license list.
* If you’re a developer and considering contributing to open source, why contribute to a BSL project with no guarantee you’d be able to use your own work in the future? You’re now much more likely to contribute to something else.
* If you’re a vendor and considering building a product or tooling in the DevOps space, why build it around Terraform, and take the risk that HashiCorp will, now or in the future, consider you competitive? That’s just too shaky of a foundation to build on, so you’re now much more likely to build around something else.

**In short, BSL breaks the virtuous open source cycle that got Terraform to where it is today.** And once you break that virtuous cycle, everyone loses: adoption will slow, contributions will decrease, and the community and ecosystem will dwindle and wither.

### OpenTF: keeping Terraform open source

We believe that the essential building blocks of the modern Internet—tools such as Linux, Kubernetes, and Terraform—must be truly open source. That is the only way to ensure that we are building our industry on top of solid and predictable underpinnings.

Therefore, we have joined forces with a number of other companies to create the [OpenTF manifesto](https://opentf.org/). **The goal of the manifesto is to ensure Terraform remains truly open source — always.**

To this end, the manifesto lays out the following two-step plan:

1. **Ask HashiCorp to switch Terraform back to open source.** The manifesto is a public request—a petition with signatures—for HashiCorp to do the right thing here and switch Terraform back to a truly open source license (e.g., go back to MPL). Moreover, we want to be sure that it stays that way, so we are asking HashiCorp to commit to keeping Terraform under an open source license forever in the future.
2. **If they refuse, we will fork Terraform into an open source foundation.** If HashiCorp decides to keep Terraform under the BSL license, then we will fork the MPL-licensed Terraform (Terraform version 1.5.5 and all versions before that are still MPL licensed), and put it into an open source foundation maintained by the community. We are one of many companies who have pledged resources to maintaining this fork, if it comes to it.

**Either way, the future of Terraform is open source**. If you also believe that Terraform should remain open source, please lend us your support, and let HashiCorp know how you feel by signing the OpenTF manifesto at <https://opentf.org/>!

### What this means for Gruntwork customers

**As long as you use Terraform 1.5.5 or older, you can keep using all our commercial and open source products with no changes**. Terraform 1.5.5 and all older versions are still MPL licensed, so you can keep using that version of Terraform with Terragrunt, Terratest, the IaC Library, the Reference Architecture, Gruntwork Pipelines, etc., with no changes of any kind.

**For future versions of Terraform, Gruntwork will use open source Terraform**. For versions of Terraform that come out after 1.5.5, we will switch all our commercial and open source products to work only with open source Terraform: that is, if HashiCorp chooses to switch Terraform back to an open source license, we will use that, and if they don’t, then we will use our open source fork. We are currently waiting to see how HashiCorp responds to OpenTF, and we will share more details once we have them.

**But rest assured: no matter what happens, we are committed to keeping Terraform open source and ensuring all our products will continue to work with it.**

For more information, and to join the OpenTF movement, please see <https://opentf.org/>!
