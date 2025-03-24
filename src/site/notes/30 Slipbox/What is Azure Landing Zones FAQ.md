---
{"dg-publish":true,"dg-path":"What is Azure Landing Zones FAQ.md","permalink":"/what-is-azure-landing-zones-faq/","tags":["notes"]}
---


## What is a Azure Landing Zone?

Azure Landing Zones are a architecture pattern designed to have an opinionated way to onboard and deploy to a Cloud platform with confidence that the environment is reliable, scalable, and built to last without fear of outgrowing what has been deployed.

## What Type of Landing Zones Are There?

There are two types of Landing Zones: **Platform** Landing Zones, and **Application** Landing Zones.

## What is a Platform Landing Zone

**Platform** Landing Zones are the central zones where shared Azure resources are deployed. **Platform** zones are not for shared workloads (like a CRM system), but are specifically for the Azure building blocks that **Application** Landing Zones plug into.

## What Kind of Platform Landing Zones Are There?

There are lots of different **Platform** Landing zones, but the three primary ones are:  
**Management** - This handles the creating of *Management Groups* (Like OU's in Active Directory, but for Azure Subscriptions), and *Azure Policies* (Like Group Policy, but for Management Groups and Subscriptions).  
**Connectivity** - This is the central location that all Virtual Networks connect into, having a Virtual Network of its own that typically gets referred to as the Hub. This Hub network is typically also associated to a Azure Firewall, and on premises connectivity either by VPN or ExpressRoute.  
**Identity** - This is the central location for Identity services if being used, such as *Entra Domain Services* or a self hosted *Active Directory*.

## What Is a Application Landing Zone

**Application** Landing Zones are where Applications and Workloads are deployed. These inherit Azure Policies deployed by the **Platform**, which act as bumper rails to make sure the Application does not break company policies by doing things such as deploying to unsanctioned Azure regions, or exposing public endpoints to bypass the central Firewall.  
**Application** Landing Zones can be subdivided into 3 general approaches:  
**Central Team Management** - Typically managed by the Azure Platform Administration team, this zone is used to add controls and tools to be used by this team.  
**Application Team Management** - Managed by Application Teams, this zone is for hosting internal and external applications.  
**Shared Management** - Hybrid responsibility Landing Zones where more complex infrastructure is required to host a application, such as Azure Kubernetes Services.
