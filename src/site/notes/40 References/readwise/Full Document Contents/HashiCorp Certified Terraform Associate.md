---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/hashi-corp-certified-terraform-associate/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.datocms-assets.com/2885/1645553469-hcta0-badge.png?auto=format&fit=max&w=1200)

The HashiCorp Certified: Terraform Associate (003) certification exam is now available. Until May, cloud engineers will be able to use either version of the Terraform Associate certification to verify their basic infrastructure automation skills.

The Terraform Associate 003 is now available. This certification is for Cloud Engineers specializing in operations, IT, or development who know the basic concepts and skills associated with HashiCorp Terraform. This person understands the difference in functionality between Terraform Cloud, Terraform Enterprise, and open source Terraform.

##### Exam availability dates

* **April 5:** Terraform Associate **003** is available to schedule. Both versions are available
* **May 5:** Last day to schedule or reschedule an appointment to take the Terraform Associate **002** exam
	+ Scheduling subject to appointment availability until **May 19**

##### Which exam to take

The [Terraform Associate 002 certification](https://www.hashicorp.com/certification/terraform-associate-002) is still relevant and will be accepted as a validation of Terraform knowledge until each individual badge’s expiration date. Receiving a Terraform Associate 003 certification will not impact any existing Terraform Associate 002 credentials, and a single candidate can hold both at the same time. However, either certification alone can be used to validate Terraform knowledge at the associate level.

* **If you have already passed the Terraform Associate** take the new (003) exam when you are eligible to [recertify](https://www.hashicorp.com/blog/renew-your-existing-hashicorp-certifications).
* **If you have never passed the Terraform Associate exam** the choice is up to you and your timeline.

##### Content differences between exams

We've updated the Terraform Associate 003 exam to account for how Terraform has grown, and to accommodate future growth. The changes are primarily a reorganization and rewording of the 002 exam objectives. More significant changes are listed below.

| # | Objective Description | Status in Terraform Associate 003 |
| --- | --- | --- |
| 3e | Explain when to use and not use provisioners and when to use local-exec or remote-exec | Removed |
| 4 | Use Terraform outside of core workflow | `terraform taint` removed, other topics reorganized |
| 6b | Initialize a Terraform working directory (`terraform init`) | Includes questions about `terraform.lock.hcl` |
| 7 | Implement and maintain state | Cloud integration authentication, and cloud backends added |
| 8a | Demonstrate use of variables and outputs | Covers sensitive variables and outputs' relationship to exposure on the CLI |
| 8g | Configure resource using a `dynamic` block | Use cases for `dynamic` block are still tested in objective 8 |
| 9 | Understand Terraform Cloud capabilities | Restructured to accommodate the current and future state of Terraform Cloud |

##### Prerequisites

* Basic terminal skills
* Basic understanding of on premises and cloud architecture

##### Product version tested

Terraform 1.0 and higher.

##### Preparing for the exam

The Terraform Associate 002 exam has both a [study guide](https://developer.hashicorp.com/terraform/tutorials/certification-003/associate-study-003) and a [review guide](https://developer.hashicorp.com/terraform/tutorials/certification-003/associate-review-003). While much of the information in these two guides are the same, they are presented differently for different uses. Use the [study guide](https://developer.hashicorp.com/terraform/tutorials/certification-003/associate-study-003) if you want to study all the exam objectives. Use the [review guide](https://developer.hashicorp.com/terraform/tutorials/certification-003/associate-review-003) if you already have Terraform experience and/or training and want to pick and choose which objectives to review before taking the exam. There are also [sample questions](https://developer.hashicorp.com/terraform/tutorials/certification-003/associate-questions) available so you can get a feel for what the exam will be like.

##### Exam details

|  |  |
| --- | --- |
| Assessment Type | Multiple choice |
| Price | $70.50 USD  plus locally applicable taxes and fees  Free retake **not included** |

##### Exam objectives

| 1 | Understand infrastructure as code (IaC) concepts |
| --- | --- |

| 2 | Understand the purpose of Terraform (vs other IaC) |
| --- | --- |
| 2a | Explain multi-cloud and provider-agnostic benefits |

| 3 | Understand Terraform basics |
| --- | --- |

| 4 | Use Terraform outside of core workflow |
| --- | --- |
| 4a | Describe when to use `terraform import` to import existing infrastructure into your Terraform state  |
| 4c | Describe when to enable verbose logging and what the outcome/value is |

| 5 | Interact with Terraform modules |
| --- | --- |

| 6 | Use the core Terraform workflow |
| --- | --- |

| 7 | Implement and maintain state |
| --- | --- |

| 8 | Read, generate, and modify configuration |
| --- | --- |
| 8g | Describe built-in dependency management (order of execution based) |

| 9 | Understand Terraform Cloud capabilities |
| --- | --- |
