---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/oracle-goes-vegan-dumps-terraform-for-open-tofu/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.thestack.technology/content/images/size/w1200/2024/05/yu-jinyang-m4TUrjoJ0TI-unsplash.jpg)

![](https://www.thestack.technology/content/images/size/w1304/2024/05/yu-jinyang-m4TUrjoJ0TI-unsplash.jpg)
Oracle has swapped Terraform for the open-source fork OpenTofu under the hood of its Oracle E-Business Suite (EBS) Cloud Manager.

It is now telling customers they “must” make the shift to its new OpenTofu-based version of the migration/provisioning tool by June 30, 2024.

Oracle EBS is a suite of business applications including CRM, procurement and supply chain software. “Cloud Manager” is what it describes as the “primary tool” for EBS customers looking to adopt Oracle Cloud.

It can be used for migrating Linux-based environments, provisioning new environments, and performing lifecycle management activities.

(Unless The Stack is sorely mistaken, "Cloud Manager" is a lick of Oracle paint on an underlying open source Terraform engine; or was... )

#### **Oracle’s OpenTofu shift**

In a short [blog](https://blogs.oracle.com/ebsandoraclecloud/post/ebs-cloud-manager-24111-now-available?ref=thestack.technology), an EBS product director at Oracle said that its “latest Oracle E-Business Suite (EBS) Cloud Manager update, 24.1.1.1, is now available,” urging customers to update “at your earliest convenience.”

“In this release, we have switched from Terraform to OpenTofu due to forthcoming Terraform licensing changes,” wrote [Terri Noyes](https://blogs.oracle.com/authors/terri-noyes?ref=thestack.technology).

“ You must therefore upgrade your Cloud Manager to 24.1.1.1 by June 30, 2024 at the latest,” she said, adding that the release updated further components to “maintain security standards and improve supportability.”

The move comes after Hashicorp’s 2023 decision to adopt a more restrictive BSL 1.1. Licence for Terraform and other products, instead of the [MPL 2.0](https://www.mozilla.org/en-US/MPL/2.0/?ref=thestack.technology) that it previously used. That move triggered a swift fork, OpenTofu, adopted by the Linux Foundation. (Version 1.7 [landed in March](https://www.thestack.technology/opentofu-1-7-business-value/) 2024 and was widely considered to be the first enterprise-ready version.)

Oracle’s move seems like a straightforward decision to ensure it is using the most permissive underlying IaC tool without having to worry about downstream licence complications, no more and no less. OpenTofu is essentially a pretty familiar drop-in replacement for Terraform; using it here is ultimately a minor implementation detail for those looking to move complex EBS environments to the cloud, but it does signal that serious enterprises feel the fork is already robust enough to use.

In late April IBM agreed to buy Hashicorp for $6.7 billion.
