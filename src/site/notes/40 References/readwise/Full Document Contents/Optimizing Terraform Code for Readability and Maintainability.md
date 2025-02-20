---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/optimizing-terraform-code-for-readability-and-maintainability/","tags":["rw/articles"]}
---

![rw-book-cover](https://cdn-images-1.medium.com/proxy/1*TGH72Nnw24QL3iV9IOm4VA.png)

Welcome back to the Azure Terraformer! Today, we’re diving into a critical aspect of infrastructure-as-code (IaC): writing Terraform code that prioritizes readability and maintainability over technical elegance. Unlike traditional application development, where clever code can be a badge of honor, IaC demands simplicity and clarity. Let’s explore this concept through a recent code review I conducted for one of our code ninjas.

Some content could not be imported from the original document. [View content ↗](https://cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2FdwQRv9Vh6Kk%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DdwQRv9Vh6Kk&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2FdwQRv9Vh6Kk%2Fhqdefault.jpg&key=a19fcc184b9711e1b4764040d3dc5c07&type=text%2Fhtml&schema=youtube) 

### The Importance of Readability in IaC

In the world of IaC, the primary goal is to manage and provision infrastructure efficiently. This means the code should be easy to read, understand, and modify by anyone on the team. Overly complex or “elegant” solutions can hinder collaboration and increase the risk of errors.

### Avoiding Unnecessary Complexity

His code presented a scenario where he was dealing with a many-to-many relationship between scopes, identities, and roles in Azure. He attempted to use advanced iteration techniques in Terraform to handle this complexity. While his intentions were good, the result was code that was hard to read and maintain.
