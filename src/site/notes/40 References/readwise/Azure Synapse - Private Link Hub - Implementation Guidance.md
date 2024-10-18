---
{"dg-publish":true,"permalink":"/40-references/readwise/azure-synapse-private-link-hub-implementation-guidance/","tags":["rw/articles"]}
---

![40 References/attachments/5e41027b70a856f01dfaa00a5bf30b56_MD5.jpg](/img/user/40%20References/attachments/5e41027b70a856f01dfaa00a5bf30b56_MD5.jpg)
  
Author: Ryan Royals

## Summary

We recently did a bit of a deep dive on Azure Synapse Private Link Hub for private connectivity to Azure Synapse. Particularly with regard to customers with multiple workspaces.

## Highlights added August 30, 2024 at 2:23 PM
>We recently did a bit of a deep dive on Azure Synapse Private Link Hub for private connectivity to Azure Synapse. Particularly with regard to customers with multiple workspaces. The key take aways are:
>• Azure Synapse Private Link Hub is not at all tied to a Workspace
>• When you create a private link from the hub, it gives you a private IP address and private DNS record for **web.azuresynapse.net** portal.
>• Because you can only have a single DNS record for web.azuresynapse.net you can't create two hubs in a connected environment and have them be resolvable to all virtual networks.
>• In a customer like HSS. If you put the Synapse Private Link Hub in a customer's spoke virtual network. Firewall restrictions will prevent other customers from accessing the Synapse Portal because they can't access things in other customers networks.
>Therefore, you should
>• Only deploy one private link hub in a shared / hub virtual network.
>• This virtual network should be accessible (firewall rules) to all users / customers that require access to Synapse.
>• You only need to create a single private link connection within the hub and link it to the shared / hub virtual network
>• You should use DNS zones managed within the hub virtual network so that all users can resolve the name of **web.azuresynapse.net**
>There are plenty of docs on it, none of which are overly clear:
>• [azure-docs/articles/synapse-analytics/security/how-to-connect-to-workspace-from-restricted-network.md at main · MicrosoftDocs/azure-docs (github.com)](https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/synapse-analytics/security/how-to-connect-to-workspace-from-restricted-network.md)
>• [Azure Synapse Private Link hub. What is a Synapse Private Link Hub? | by Vijay K J | Medium](https://medium.com/@viju.coorg/azure-synapse-private-link-hub-4eb758df9e40)
>• [Synapse Connectivity Series Part #2 – Inbound Synapse Private Endpoints – Azure Aggregator (wordpress.com)](https://azureaggregator.wordpress.com/2023/01/27/synapse-connectivity-series-part-2-inbound-synapse-private-endpoints-2/) ([View Highlight] (https://read.readwise.io/read/01he21rrrbybwn5xmgh0zjsqa6))


