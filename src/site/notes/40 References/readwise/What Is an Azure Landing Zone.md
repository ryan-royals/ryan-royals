---
{"dg-publish":true,"permalink":"/40-references/readwise/what-is-an-azure-landing-zone/","tags":["rw/articles"]}
---

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_921743/open-graph-image_2cWYLoJ.png)
  
URL: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/
Author: martinekuan

## Summary

Learn how a landing zone provides the basic building block of any cloud adoption environment.

## Highlights added August 30, 2024 at 2:23 PM
>Azure landing zone conceptual architecture below represents the destination in their cloud adoption journey. ([View Highlight] (https://read.readwise.io/read/01gz4yagt5zmw6wykdhhag4355))


>An Azure landing zone is the output of a multi-subscription Azure environment that accounts for scale, security governance, networking, and identity. ([View Highlight] (https://read.readwise.io/read/01gye5wxm46gd6q2219je7mwmp))


>However, a few Azure landing zone implementation options can help you meet the deployment and operations needs of your growing cloud portfolio. ([View Highlight] (https://read.readwise.io/read/01gye5x6db7kgpxhmap4rhwvej))


>**Scalable:** All Azure landing zones support cloud adoption at scale by providing repeatable environments, with consistent configuration and controls, regardless of the workloads or Azure resources deployed to each landing zone instance. ([View Highlight] (https://read.readwise.io/read/01gye5xa49x0g45fr520km8tex))


>**Modular:** All Azure landing zones provide an extensible approach to building out your environment, based on a common set of design areas. The extensibility of an Azure landing zone enables an organization to easily scale specific elements of the environment, as requirements evolve. ([View Highlight] (https://read.readwise.io/read/01gye5xcgreqkydkcbh6e2y11t))


>There are two types of landing zones:
>• **Platform landing zones:** Subscriptions deployed to provide centralized services, often operated by a central team, or a number of central teams split by function (e.g. networking, identity), which will be used by various workloads and applications. Platform landing zones represent key services that often benefit from being consolidated for efficiency and ease of operations. Examples include networking, identity, and management services.
>• **Application landing zones:** One or more subscriptions deployed as an environment for an application or workload. Application landing zones are placed in management groups like 'corp' or 'online' beneath the 'landing zones' management group to ensure policy controls are correctly applied. Application landing zones can be subcategorized as follows:
>• **Centrally managed**: A central IT team fully operates the landing zone. The team applies controls and platform tools to both the platform and application landing zones.
>• **Technology platforms**: With technology platforms such as AKS or AVS, the underlying service is often centrally managed. The applications running on top of the service have delegated responsibilities to application teams. This results in modified controls or access permissions compared to centrally managed landing zones.
>• **Workload**: A platform administration team delegates the entire landing zone to a workload team to fully manage and support the environment; whilst still being controlled by the policies applied from the Management Groups above that the platform team control. This might include adding additional policies at the subscription scope and using alternative tooling for deploying, securing or monitoring workloads that is fully controlled and operated by the workload team. ([View Highlight] (https://read.readwise.io/read/01gye5xn1h8ex2jn3ka9wdqx3e))


>[![A conceptual architecture diagram of an Azure landing zone.](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/../enterprise-scale/media/ns-arch-cust-expanded.svg)](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/../enterprise-scale/media/ns-arch-cust-expanded.svg#lightbox) ([View Highlight] (https://read.readwise.io/read/01gye5y6va4za4h2g6vfs8kthe))


