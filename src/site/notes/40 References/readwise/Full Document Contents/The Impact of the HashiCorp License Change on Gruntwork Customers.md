---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/the-impact-of-the-hashi-corp-license-change-on-gruntwork-customers/","tags":["rw/articles"]}
---

![rw-book-cover](https://miro.medium.com/v2/resize:fit:1024/1*9OIFEnomVZ1dW_kd5kMaww.png)

![](https://miro.medium.com/v2/resize:fit:700/1*9OIFEnomVZ1dW_kd5kMaww.png)
On Thursday, August 10, 2023, HashiCorp [announced](https://www.hashicorp.com/blog/hashicorp-adopts-business-source-license) that it was switching Terraform from the [MPL v2 license](https://www.mozilla.org/en-US/MPL/2.0/FAQ/) to a “Business Source License” (BSL). In this blog post, we’d like to address how this impacts Gruntwork customers.

### What exactly happened?

Terraform was released in 2014 under an MPL v2 license, which allows almost any use of Terraform. The one meaningful requirement is that if you modify the Terraform source code, you need to release those modifications under the same MPL v2 license.

After nearly 9 years, HashiCorp made a surprise decision to change to the BSL license for all future releases of Terraform. Importantly, Terraform v1.5.5 and earlier continue to exist under the MPL v2 license.

The BSL license does not allow you to use Terraform if you both (a) compete with HashiCorp, and (b) host or embed Terraform in your products. Again, this only applies to new versions of Terraform going forward.

### Can I continue to use Gruntwork commercial products?

Yes. Terraform 1.5.5 and earlier continue to maintain the original MPL v2 license, and you are free to continue using all Gruntwork commercial products *as long as you do not upgrade beyond Terraform v1.5.5.* Fortunately, as of the writing of this blog post, Terraform v1.5.5 is the latest release of Terraform.

**As a Gruntwork customer, there is no action item beyond ensuring that your team does not use a Terraform version above v1.5.5.**

### Can I continue to use Gruntwork open source products like Terragrunt and Terratest?

Yes. Terraform 1.5.5 and earlier continue to maintain the original MPL v2 license, and you are free to continue using all Gruntwork open source products *as long as you do not upgrade beyond Terraform v1.5.5.* Fortunately, as of the writing of this blog post, Terraform v1.5.5 is the latest release of Terraform.

**As a Gruntwork open source user, there is no action item beyond ensuring that your team does not use a Terraform version above v1.5.5.**

### What if I want to upgrade Terraform beyond v1.5.5?

We are finalizing our plan for how you can use all Gruntwork products — both commercial and open source — with future Terraform versions in a way that will comply with all applicable licenses, and we’ll be sharing that later this week.

### What if I have questions?

Our sales team has been trained on the details of the license change and is the best resource to answer your questions. You may contact them at [sales@gruntwork.io](mailto:sales@gruntwork.io) with any additional questions.

### Any other thoughts?

Our first responsibility will always be to you, our customer, and setting you up for success with DevOps best practices. In that spirit, we see charting the path forward on the Terraform license change as another opportunity to provide a best practice decision, and we look forward to offering more guidance later this week.
