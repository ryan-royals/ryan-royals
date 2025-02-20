---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/advanced-terraform-techniques/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.datocms-assets.com/2885/1677617902-john-mcdonough.png)

This session covers advanced topics related to Terraform coding and code management that will help you and your organization create, utilize, maintain, manage, and optimize your Terraform codebase.

Some content could not be imported from the original document. [View content ↗](https://www.youtube.com/embed/OnsG-P7LyQU?autoplay=0&mute=0&controls=1&origin=https%3A%2F%2Fwww.hashicorp.com&playsinline=1&showinfo=0&rel=0&iv_load_policy=3&modestbranding=1&enablejsapi=1&widgetid=1) 

Learn how to utilize DRY programming concepts in your Terraform code. Through a combination of Terraform HCL constructs and GitHub techniques, your Terraform code can be modularized to support multiple deployments without duplicating code in each project. For the best results though, you should look to the [private module registry](https://developer.hashicorp.com/terraform/cloud-docs/registry).

Next, we will look at `for_each` and dynamic block constructs and how to define and dynamically create the data used in these constructs. By creating data-driven code, you will rarely change the foundational blocks of code and focus more on the data that is used by the code.

By utilizing Maps and converting your lists to Maps you can say goodbye the count parameter and benefit by being able to specifically reference an object by its key. Dynamically generating data by combining sets of data enables extreme flexibility in the way modules will consume the data to create and manage objects.

Wrapping up the session will be a focus on how to implement implicit dependencies and eliminate the need for explicit dependencies. “Implicit dependencies” here aligns to the [dependency inversion](https://developer.hashicorp.com/terraform/language/modules/develop/composition#dependency-inversion) explained on developer.hashicorp.com.

These are techniques I use regularly in my Terraform code to generate hundreds of Azure lab and training environments monthly.
