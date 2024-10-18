---
{"dg-publish":true,"permalink":"/40-references/readwise/maturing-your-terraform-workflow/","tags":["rw/articles"]}
---

<svg width="36" height="39" viewBox="0 0 36 39" xmlns="http://www.w3.org/2000/svg"><style>path{fill:black}@media (prefers-color-scheme:dark){path{fill:white}}</style><path d="M0 9.335L14.663.875v6.356l-9.154 5.284v20.318L0 29.653V9.334z"/><path d="M20.516.876v16.181h-5.853v-6.039l-5.509 3.18V34.93l5.509 3.188V21.983h5.853v6l5.51-3.182V4.057L20.515.876z"/><path d="M35.18 29.665l-14.664 8.46v-6.356l9.154-5.285V6.167l5.51 3.18v20.318z"/></svg>
  
URL: https://www.hashicorp.com/blog/maturing-your-terraform-workflow
Author: Morgan Peat

## Summary

These guidelines can help organizations mature their use of HashiCorp Terraform modules for scale and a faster release cadence.

## Highlights added August 30, 2024 at 2:23 PM
>Two anti-patterns often arise as organizations increase the use of their platform and start to scale: first module proliferation, then mega-modules. ([View Highlight] (https://read.readwise.io/read/01h717a5dcxqgncrd74hz1drcj))


>Module proliferation happens when developers discover [the benefits of Terraform modules](https://developer.hashicorp.com/terraform/tutorials/modules/module#what-are-modules-for) and start creating them. Without centralized coordination, the path of least resistance is often to create a new module instead of trying to reuse one that doesn’t quite fit requirement ([View Highlight] (https://read.readwise.io/read/01h717b6t2yrdegarmjwv8stqk))


>In an attempt to fix this sprawl, mega-modules arise as platform teams consolidate overlapping modules hoping to reduce proliferation and encourage code reuse. These bloated mega-modules aim to cover every possible use case but often become overly brittle and complex. ([View Highlight] (https://read.readwise.io/read/01h717bs8vnr5v5an2z0jdxsxb))


>To address these problems, cloud mature organizations apply the [Pareto Principle](https://en.wikipedia.org/wiki/Pareto_principle) to module design. Use case analysis shows that the vast majority of modules need just a handful of inputs to meet most customer requirements. Focusing on this “easy 80%” of use cases results in neat, concise modules that are simple to understand and use. It also causes modules to become more opinionated, which guides developers into a standard pattern, bringing consistency around how infrastructure is used in the organization. ([View Highlight] (https://read.readwise.io/read/01h717ehhqwdx0rvnmq29vkkry))


>• The API of a Terraform module should help developers use it correctly, through variable validation and sensible default values for variables.
>• Terraform repositories should have a consistent folder and file structure.
>• Terraform code comments [should clearly explain](https://blog.codinghorror.com/code-tells-you-how-comments-tell-you-why/) *why* a decision has been taken, when the code itself is unclear.
>• Proper [bounds checking and error checking](https://developer.hashicorp.com/terraform/language/expressions/custom-conditions) will help catch common input mistakes.
>• Storing user-facing documentation and code samples in the module repository makes it easier to remember to ([View Highlight] (https://read.readwise.io/read/01h717myt98eshh8agshtw48ma))


>Cohesion means that related parts of a code base are kept in a single place. When thinking about infrastructure as a product, this means that all concerns making a ‘unit’ of infrastructure should live in the same Terraform module. For example, say you have a Terraform module that creates [Azure Cosmos PostgreSQL](https://learn.microsoft.com/en-us/azure/cosmos-db/postgresql/introduction) databases. You could use the [DataDog Terraform provider](https://registry.terraform.io/providers/DataDog/datadog/latest) to ensure the [key health metrics](https://www.datadoghq.com/blog/azure-cosmos-db-postgresql/) of every database are monitored by default. ([View Highlight] (https://read.readwise.io/read/01h717q8rqjw9msessdxxmy8zh))


