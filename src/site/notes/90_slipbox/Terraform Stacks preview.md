---
{"dg-publish":true,"permalink":"/90-slipbox/terraform-stacks-preview/","tags":["notes"],"created":"2025-06-11T10:28:48.686+09:30","updated":"2026-03-03T09:55:32.088+10:30","dg-note-properties":{"created":"2023-11-29","tags":"notes","related":["[[Terraform]]"],"references":["https://www.hashicorp.com/blog/terraform-stacks-explained"],"modified":"2026-03-03"}}
---


Terraform Stacks looks to be a answer to [[90_slipbox/Terragrunt\|Terragrunt]], and the ability to turn your one terraform project into bite sized chunks that are easier to maintain from a blast radius perspective.

Instead of a `terragrunt.hcl`, it uses a `.tfstack.hcl` to define components there are in the stack, and then uses a `.tfdeploy.hcl` to define the inputs for each Deployments.

In the supplied example, Kubernetes itself is a Component, and then the namespaces inside are each a component. This creates a imperative chain of actions, as the Namespace need the Kubernetes to exist first.  
The Deployments are used to deploy the stack to different regions.
