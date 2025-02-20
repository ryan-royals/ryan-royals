---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/create-change-or-delete-an-azure-public-ip-address-prefix/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)

#### In this article

1. [Create a public IP address prefix](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/manage-public-ip-address-prefix#create-a-public-ip-address-prefix)
2. [Create a static public IP address from a prefix](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/manage-public-ip-address-prefix#create-a-static-public-ip-address-from-a-prefix)
3. [View or delete a prefix](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/manage-public-ip-address-prefix#view-or-delete-a-prefix)
4. [Permissions](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/manage-public-ip-address-prefix#permissions)
5. [Next steps](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/manage-public-ip-address-prefix#next-steps)

A public IP address prefix is a contiguous range of standard SKU public IP addresses. When you create a public IP address resource, you can assign a static public IP from the prefix and associate the address to Azure resources. For more information, see [Public IP address prefix overview](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-address-prefix). This article explains how to create, modify, or delete public IP address prefixes, and create public IPs from an existing prefix.

#### Create a public IP address prefix

The following section details the parameters when creating a public IP prefix.

| Setting | Required? | Details |
| --- | --- | --- |
| Subscription | Yes | Must exist in the same [subscription](https://learn.microsoft.com/en-us/azure/azure-glossary-cloud-terminology?toc=/azure/virtual-network/toc.json#subscription) as the resource you want to associate the public IP address prefix to. |
| Resource group | Yes | Can exist in the same, or different, [resource group](https://learn.microsoft.com/en-us/azure/azure-glossary-cloud-terminology?toc=/azure/virtual-network/toc.json#resource-group) as the resource you want to associate the public IP address prefix to. |
| Name | Yes | The name must be unique within the resource group you select. |
| Region | Yes | Must exist in the same [region](https://azure.microsoft.com/regions)as the public IP addresses assigned from the range. |
| IP version | Yes | IP version of the prefix (v4 or v6). |
| Prefix ownership | Yes | Specify if the IP ranges will be owned by Microsoft or you, see [Custom IP Prefix](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/custom-ip-address-prefix) for more information on the latter case. |
| Prefix size | Yes | The size of the prefix you need. A range with 16 IP addresses (/28 for v4 or /124 for v6) is the default limit for Microsoft owned ranges. |

Alternatively, you may use the following CLI and PowerShell commands to create a public IP address prefix.

**Commands**

| Tool | Command |
| --- | --- |
| CLI | [az network public-ip prefix create](https://learn.microsoft.com/en-us/cli/azure/network/public-ip/prefix#az-network-public-ip-prefix-create) |
| PowerShell | [New-AzPublicIpPrefix](https://learn.microsoft.com/en-us/powershell/module/az.network/new-azpublicipprefix) |

Note

In regions with availability zones, you can use PowerShell or CLI commands to create a public IP address prefix as either: non-zonal, associated with a specific zone, or to use zone-redundancy. For API version 2020-08-01 or later, if a zone parameter is not provided, a non-zonal public IP address prefix is created. For versions of the API older than 2020-08-01, a zone-redundant public IP address prefix is created.

Note

For more information about deriving a Public IP Prefix from an onboarded Custom IP Prefix (BYOIP range), please refer to [Manage Custom IP Address Prefix](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/manage-custom-ip-address-prefix#create-a-public-ip-prefix-from-a-custom-ip-prefix).

#### Create a static public IP address from a prefix

The following section details the parameters required when creating a static public IP address from a prefix.

| Setting | Required? | Details |
| --- | --- | --- |
| Name | Yes | The name of the public IP address must be unique within the resource group you select. |
| Idle timeout (minutes) | No | How many minutes to keep a TCP or HTTP connection open without relying on clients to send keep-alive messages. |
| DNS name label | No | Must be unique within the Azure region you create the name in (across all subscriptions and all customers).  Azure automatically registers the name and IP address in its DNS so you can connect to a resource with the name.  Azure appends a default subnet *location.cloudapp.azure.com* to the name you provide to create the fully qualified DNS name.  For more information, see [Use Azure DNS with an Azure public IP address](https://learn.microsoft.com/en-us/azure/dns/dns-custom-domain?toc=/azure/virtual-network/toc.json#public-ip-address). |

Alternatively, you may use the following CLI and PowerShell commands with the **`--public-ip-prefix`** **(CLI)** and **`-PublicIpPrefix`** **(PowerShell)** parameters, to create a public IP address resource from a prefix.

| Tool | Command |
| --- | --- |
| CLI | [az network public-ip create](https://learn.microsoft.com/en-us/cli/azure/network/public-ip#az-network-public-ip-create) |
| PowerShell | [New-AzPublicIpAddress](https://learn.microsoft.com/en-us/powershell/module/az.network/new-azpublicipaddress) |

Note

When requesting a Public IP address from a Public IP Prefix, the allocation is not deterministic or sequential. If a specific Public IP address from a Public IP Prefix is required, the PowerShell or CLI commands allow for this. For PowerShell, the `IpAddress` parameter (followed by the desired IP) should be used; for CLI, the `ip-address` parameter (followed by the desired IP) should be used.

Note

Only static public IP addresses created with the Standard SKU can be assigned from the prefix's range. To learn more about public IP address SKUs, see [public IP address](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses#public-ip-addresses).

#### View or delete a prefix

To view or delete a prefix, the following commands can be used in Azure CLI and Azure PowerShell.

**Commands**

| Tool | Command |
| --- | --- |
| CLI | [az network public-ip prefix list](https://learn.microsoft.com/en-us/cli/azure/network/public-ip/prefix#az-network-public-ip-prefix-list) to list public IP addresses.  [az network public-ip prefix show](https://learn.microsoft.com/en-us/cli/azure/network/public-ip/prefix#az-network-public-ip-prefix-show) to show settings.  [az network public-ip prefix update](https://learn.microsoft.com/en-us/cli/azure/network/public-ip/prefix#az-network-public-ip-prefix-update) to update.  [az network public-ip prefix delete](https://learn.microsoft.com/en-us/cli/azure/network/public-ip/prefix#az-network-public-ip-prefix-delete) to delete. |
| PowerShell | [Get-AzPublicIpPrefix](https://learn.microsoft.com/en-us/powershell/module/az.network/get-azpublicipprefix) to retrieve a public IP address object and view its settings.  [Set-AzPublicIpPrefix](https://learn.microsoft.com/en-us/powershell/module/az.network/set-azpublicipprefix) to update settings.  [Remove-AzPublicIpPrefix](https://learn.microsoft.com/en-us/powershell/module/az.network/remove-azpublicipprefix) to delete. |

#### Permissions

For permissions to manage public IP address prefixes, your account must be assigned to the [network contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles?toc=/azure/virtual-network/toc.json#network-contributor) role or to a [custom](https://learn.microsoft.com/en-us/azure/role-based-access-control/custom-roles?toc=/azure/virtual-network/toc.json) role.

| Action | Name |
| --- | --- |
| Microsoft.Network/publicIPPrefixes/read | Read a public IP address prefix |
| Microsoft.Network/publicIPPrefixes/write | Create or update a public IP address prefix |
| Microsoft.Network/publicIPPrefixes/delete | Delete a public IP address prefix |
| Microsoft.Network/publicIPPrefixes/join/action | Create a public IP address from a prefix |

#### Next steps

* Learn about scenarios and benefits of using a [public IP prefix](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-address-prefix)
