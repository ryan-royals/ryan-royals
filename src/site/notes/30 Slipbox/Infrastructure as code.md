---
{"created":"2023-10-15","tags":["notes"],"topics":null,"references":["https://learn.microsoft.com/en-us/devops/deliver/what-is-infrastructure-as-code"],"aliases":["IaC"],"dg-publish":true,"dg-path":"Infrastructure as code.md","permalink":"/infrastructure-as-code/","dgPassFrontmatter":true}
---


Infrastructure as Code is a DevOps methodology in which the infrastructure resources for supporting applications is deployed and configured with automation in a repeatable fashion with minimal to no human interaction (Click-Ops).

IaC comes in two major flavours: **Declarative** and **Imperative**.

**Declarative** IaC takes the approach of declaring the desired outcome, and using the IaC language to fill in the gaps and deploy what is required. An example in [[30 Slipbox/Azure\|Azure]] is when deploying a virtual machine into a RG with a Virtual Network, you declare the required resources to a tool like [[30 Slipbox/Terraform\|Terraform]], and then Terraform will create a **Dependency Graph**, and co ordinate the deployment of the RG > VNET > NIC > VM, saving the developer from needing to understand the individual steps. This also creates a *idempotent* process that can be repeated easily, added to, or used to assess configuration drift as Terraform checks the current State of the environment, and creates steps to make the Environment look like the code.

**Imperative** IaC is more familiar to a scripting language, where the operations are conducted top to bottom, in the exact step as defined. Executing a deployment with [[30 Slipbox/Powershell\|Powershell]] is a example of creating a Imperative workflow to deploy infrastructure. Imperative deployments are weak to config drift as they do not check for this, but are better at doing a fresh deployment of a bespoke element.

Both Declarative and Imperative tooling have their own use cases, but typically when speaking about IaC in a broader sense, the industry standard is leaning towards IaC tooling being Declarative.
