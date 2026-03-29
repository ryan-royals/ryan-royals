---
{"dg-publish":true,"dg-path":"Slipbox Notes/Cloud Center of Excellence.md","permalink":"/slipbox-notes/cloud-center-of-excellence/","tags":["notes"],"created":"2023-04-19","updated":"2025-11-28"}
---


A Cloud Centre of Excellence is a conceptual body that is used to reduce drag on Cloud Migration and operation tasks, by utilising a top down and bottom up approach to management of the platform, and letting the users use the platform.

A typical suite of technical controls is items like Azure Policy to control the platform and set up the bumper rails, whilst using things like Azure Firewall, Azure User Defined Route and Azure Virtual Network to control the ingress and egress traffic.

The true magic to this approach is it allows for other teams to consume the platform without unrequired lead time for the Infrastructure and Ops team to audit the application, scope the network connectivity, plan a migration etc.

It is important to note that this is not a single implementation, but is a change to business approach and can take a long time to view results, and requires constant attention to keep working correctly.

Reference: [Cloud center of excellence (CCoE) functions - Cloud Adoption Framework](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/organize/cloud-center-of-excellence), [A Cloud Center of Excellence Is the Best-Practice Approach to Drive Cloud-Enabled Transformation.](https://www.gartner.com/en/conferences/hub/cloud-conferences/insights/how-to-build-a-cloud-center-of-excellence)
