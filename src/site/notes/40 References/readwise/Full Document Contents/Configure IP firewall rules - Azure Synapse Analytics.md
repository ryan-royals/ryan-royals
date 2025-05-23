---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/configure-ip-firewall-rules-azure-synapse-analytics/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png)

#### In this article

1. [IP firewall rules](https://learn.microsoft.com/en-us/azure/synapse-analytics/security/synapse-workspace-ip-firewall#ip-firewall-rules)
2. [Create and manage IP firewall rules](https://learn.microsoft.com/en-us/azure/synapse-analytics/security/synapse-workspace-ip-firewall#create-and-manage-ip-firewall-rules)
3. [Connect to Azure Synapse from your own network](https://learn.microsoft.com/en-us/azure/synapse-analytics/security/synapse-workspace-ip-firewall#connect-to-azure-synapse-from-your-own-network)
4. [Manage the Azure Synapse workspace firewall](https://learn.microsoft.com/en-us/azure/synapse-analytics/security/synapse-workspace-ip-firewall#manage-the-azure-synapse-workspace-firewall)
5. [Next steps](https://learn.microsoft.com/en-us/azure/synapse-analytics/security/synapse-workspace-ip-firewall#next-steps)

This article will explain IP firewall rules and teach you how to configure them in Azure Synapse Analytics.

#### IP firewall rules

IP firewall rules grant or deny access to your Azure Synapse workspace based on the originating IP address of each request. You can configure IP firewall rules for your workspace. IP firewall rules configured at the workspace level apply to all public endpoints of the workspace (dedicated SQL pools, serverless SQL pool, and development).

#### Create and manage IP firewall rules

There are two ways IP firewall rules are added to an Azure Synapse workspace. To add an IP firewall to your workspace, select **Networking** and check **Allow connections from all IP addresses** during workspace creation.

Important

This feature is only available to Azure Synapse workspaces not associated with a Managed VNet.

[![Screenshot that highlights the Security tab, and the 'Allow connections from all IP addresses' checkbox.](https://learn.microsoft.com/en-us/azure/synapse-analytics/security/media/synpase-workspace-ip-firewall/azure-synapse-workspace-networking-connections-all-ip-addresses.png)](https://learn.microsoft.com/en-us/azure/synapse-analytics/security/media/synpase-workspace-ip-firewall/azure-synapse-workspace-networking-connections-all-ip-addresses.png#lightbox)
You can also add IP firewall rules to a Synapse workspace after the workspace is created. Select **Firewalls** under **Security** from Azure portal. To add a new IP firewall rule, give it a name, Start IP, and End IP. Select **Save** when done.

Note

The Public network access feature is only available to Azure Synapse workspaces associated with Azure Synapse Analytics Managed Virtual Network. However, you can still open your Azure Synapse workspaces to the public network regardless of its association with managed VNet. For more information, see [Public network access](https://learn.microsoft.com/en-us/azure/synapse-analytics/security/connectivity-settings#public-network-access).

[![Screenshot of the Networking page of a Synapse Workspace, highlighting the Add client IP button and rules fields.](https://learn.microsoft.com/en-us/azure/synapse-analytics/security/media/synpase-workspace-ip-firewall/azure-synapse-workspace-networking-firewalls-add-client-ip.png)](https://learn.microsoft.com/en-us/azure/synapse-analytics/security/media/synpase-workspace-ip-firewall/azure-synapse-workspace-networking-firewalls-add-client-ip.png#lightbox)
#### Connect to Azure Synapse from your own network

You can connect to your Synapse workspace using Synapse Studio. You can also use SQL Server Management Studio (SSMS) to connect to the SQL resources (dedicated SQL pools and serverless SQL pool) in your workspace.

Make sure that the firewall on your network and local computer allows outgoing communication on TCP ports 80, 443 and 1443. These ports are used by Synapse Studio.

To connect using tools such as SSMS and Power BI, you must allow outgoing communication on TCP port 1433. The 1433 port used by SSMS (Desktop Application).

#### Manage the Azure Synapse workspace firewall

For more information on managing the firewall, see [the Azure SQL documentation to manage server-level firewalls](https://learn.microsoft.com/en-us/azure/azure-sql/database/firewall-configure#create-and-manage-ip-firewall-rules). Azure Synapse only supports server-level IP firewall rules. It doesn't support database-level IP firewall rules.

For more information on the methods to manage the firewall programmatically, see:

* [API](https://learn.microsoft.com/en-us/rest/api/synapse/ip-firewall-rules)
* [PowerShell](https://learn.microsoft.com/en-us/powershell/module/az.synapse/new-azsynapsefirewallrule)
* [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/sql/server/firewall-rule)

#### Next steps

* Create an [Azure Synapse Workspace](https://learn.microsoft.com/en-us/azure/synapse-analytics/quickstart-create-workspace)
* Create an Azure Synapse workspace with a [Managed workspace Virtual Network](https://learn.microsoft.com/en-us/azure/synapse-analytics/security/synapse-workspace-managed-vnet)
* [Troubleshoot Azure Private Link connectivity problems](https://learn.microsoft.com/en-us/azure/private-link/troubleshoot-private-link-connectivity)
* [Troubleshoot Azure Private Endpoint connectivity problems](https://learn.microsoft.com/en-us/azure/private-link/troubleshoot-private-endpoint-connectivity)
