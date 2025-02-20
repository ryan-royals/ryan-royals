---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/configure-ip-firewall-rules-for-azure-service-bus-azure-service-bus/","tags":["rw/articles"]}
---

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_921743/logo-ms-social.png)

#### In this article

1. [IP firewall rules](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-ip-filtering#ip-firewall-rules)
2. [Important points](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-ip-filtering#important-points)
3. [Use Azure portal](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-ip-filtering#use-azure-portal)
4. [Trusted Microsoft services](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-ip-filtering#trusted-microsoft-services)
5. [Use Resource Manager template](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-ip-filtering#use-resource-manager-template)
6. [Use Azure CLI](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-ip-filtering#use-azure-cli)
7. [Use Azure PowerShell](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-ip-filtering#use-azure-powershell)
8. [default action and public network access](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-ip-filtering#default-action-and-public-network-access)
9. [Next steps](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-ip-filtering#next-steps)

By default, Service Bus namespaces are accessible from internet as long as the request comes with valid authentication and authorization. With IP firewall, you can restrict it further to only a set of IPv4 addresses or IPv4 address ranges in [CIDR (Classless Inter-Domain Routing)](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation.

This feature is helpful in scenarios in which Azure Service Bus should be only accessible from certain well-known sites. Firewall rules enable you to configure rules to accept traffic originating from specific IPv4 addresses. For example, if you use Service Bus with [Azure Express Route](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-faqs#supported-services), you can create a **firewall rule** to allow traffic from only your on-premises infrastructure IP addresses or addresses of a corporate NAT gateway.

#### IP firewall rules

The IP firewall rules are applied at the Service Bus namespace level. Therefore, the rules apply to all connections from clients using any **supported protocol** (AMQP (5671) and HTTPS (443)). Any connection attempt from an IP address that doesn't match an allowed IP rule on the Service Bus namespace is rejected as unauthorized. The response doesn't mention the IP rule. IP filter rules are applied in order, and the first rule that matches the IP address determines the accept or reject action.

#### Important points

* Firewalls and Virtual Networks are supported only in the **premium** tier of Service Bus. If upgrading to the **premier** tier isn't an option, we recommend that you keep the Shared Access Signature (SAS) token secure and share with only authorized users. For information about SAS authentication, see [Authentication and authorization](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-authentication-and-authorization#shared-access-signature).
* Specify **at least one IP firewall rule or virtual network rule** for the namespace to allow traffic only from the specified IP addresses or subnet of a virtual network. If there are no IP and virtual network rules, the namespace can be accessed over the public internet (using the access key).
* Implementing firewall rules can prevent other Azure services from interacting with Service Bus. As an exception, you can allow access to Service Bus resources from certain **trusted services** even when IP filtering is enabled. For a list of trusted services, see [Trusted services](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-ip-filtering#trusted-microsoft-services).

 The following Microsoft services are required to be on a virtual network

	+ Azure App Service
	+ Azure Functions

#### Use Azure portal

When creating a namespace, you can either allow public only (from all networks) or private only (only via private endpoints) access to the namespace. Once the namespace is created, you can allow access from specific IP addresses or from specific virtual networks (using network service endpoints).

##### Configure public access when creating a namespace

To enable public access, select **Public access** on the **Networking** page of the namespace creation wizard.

![Screenshot showing the Networking page of the Create namespace wizard with Public access option selected.](https://learn.microsoft.com/en-us/azure/service-bus-messaging/media/service-bus-ip-filtering/create-namespace-public-access.png)
After you create the namespace, select **Networking** on the left menu of the **Service Bus Namespace** page. You see that **All Networks** option is selected. You can select **Selected Networks** option and allow access from specific IP addresses or specific virtual networks. The next section provides you details on configuring IP firewall to specify the IP addresses from which the access is allowed.

##### Configure IP firewall for an existing namespace

This section shows you how to use the Azure portal to create IP firewall rules for a Service Bus namespace.

1. Navigate to your **Service Bus namespace** in the [Azure portal](https://portal.azure.com).
2. On the left menu, select **Networking** option under **Settings**.

  Note

 You see the **Networking** tab only for **premium** namespaces.
3. On the **Networking** page, for **Public network access**, you can set one of the three following options. Choose **Selected networks** option to allow access from only specified IP addresses.

	* **Disabled**. This option disables any public access to the namespace. The namespace is accessible only through [private endpoints](https://learn.microsoft.com/en-us/azure/service-bus-messaging/private-link-service).
	* **Selected networks**. This option enables public access to the namespace using an access key from selected networks.
	
	  Important
	
	 If you choose **Selected networks**, add at least one IP firewall rule or a virtual network that will have access to the namespace. Choose **Disabled** if you want to restrict all traffic to this namespace over [private endpoints](https://learn.microsoft.com/en-us/azure/service-bus-messaging/private-link-service) only.
	* **All networks** (default). This option enables public access from all networks using an access key. If you select the **All networks** option, Service Bus accepts connections from any IP address (using the access key). This setting is equivalent to a rule that accepts the 0.0.0.0/0 IP address range.
4. To allow access from only specified IP address, select the **Selected networks** option if it isn't already selected. In the **Firewall** section, follow these steps:

	1. Select **Add your client IP address** option to give your current client IP the access to the namespace.
	2. For **address range**, enter a specific IPv4 address or a range of IPv4 address in CIDR notation.
	3. Specify whether you want to **allow trusted Microsoft services to bypass this firewall**.
	
	  Warning
	
	 If you select the **Selected networks** option and don't add at least one IP firewall rule or a virtual network on this page, the namespace can be accessed over public internet (using the access key).
	
	   [![Screenshot of the Azure portal Networking page. The option to allow access from Selected networks is selected and the Firewall section is highlighted.](https://learn.microsoft.com/en-us/azure/service-bus-messaging/media/service-bus-ip-filtering/firewall-selected-networks-trusted-access-disabled.png)](https://learn.microsoft.com/en-us/azure/service-bus-messaging/media/service-bus-ip-filtering/firewall-selected-networks-trusted-access-disabled.png#lightbox)
5. Select **Save** on the toolbar to save the settings. Wait for a few minutes for the confirmation to show up on the portal notifications.

  Note

 To restrict access to specific virtual networks, see [Allow access from specific networks](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-service-endpoints).

#### Trusted Microsoft services

When you enable the **Allow trusted Microsoft services to bypass this firewall** setting, the following services are granted access to your Service Bus resources.

| Trusted service | Supported usage scenarios |
| --- | --- |
| Azure Event Grid | Allows Azure Event Grid to send events to queues or topics in your Service Bus namespace. You also need to do the following steps: * Enable system-assigned identity for a topic or a domain
* Add the identity to the Azure Service Bus Data Sender role on the Service Bus namespace
* Then, configure the event subscription that uses a Service Bus queue or topic as an endpoint to use the system-assigned identity.

For more information, see [Event delivery with a managed identity](https://learn.microsoft.com/en-us/azure/event-grid/managed-service-identity) |
| Azure Stream Analytics | Allows an Azure Stream Analytics job to output data to Service Bus [queues](https://learn.microsoft.com/en-us/azure/stream-analytics/service-bus-queues-output) to [topics](https://learn.microsoft.com/en-us/azure/stream-analytics/service-bus-topics-output). **Important**: The Stream Analytics job should be configured to use a **managed identity** to access the Service Bus namespace. Add the identity to the **Azure Service Bus Data Sender** role on the Service Bus namespace.  |
| Azure IoT Hub | Allows an IoT hub to send messages to queues or topics in your Service Bus namespace. You also need to do the following steps: * [Enable system-assigned or user assigned managed identity for your IoT hub](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-managed-identity).
* [Add the identity to the **Azure Service Bus Data Sender** role on the Service Bus namespace](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal).
* [Configure the IoT Hub that uses a Service Bus entity as an endpoint to use the identity-based authentication](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-managed-identity#configure-message-routing-with-managed-identities).
 |
| Azure API Management | The API Management service allows you to send messages to a Service Bus queue/topic in your Service Bus Namespace.* You can trigger custom workflows by sending messages to your Service Bus queue/topic when an API is invoked by using the [send-request policy](https://learn.microsoft.com/en-us/azure/api-management/api-management-sample-send-request).
* You can also treat a Service Bus queue/topic as your backend in an API. For a sample policy, see [Authenticate using a managed identity to access a Service Bus queue or topic](https://github.com/Azure/api-management-policy-snippets/blob/master/examples/Authenticate%20using%20Managed%20Identity%20to%20access%20Service%20Bus.xml). You also need to do the following steps:
	1. Enable system-assigned identity on the API Management instance. For instructions, see [Use managed identities in Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-use-managed-service-identity).
	2. Add the identity to the **Azure Service Bus Data Sender** role on the Service Bus namespace
 |
| Azure IoT Central | Allows IoT Central to export data to Service Bus queues or topics in your Service Bus namespace. You also need to do the following steps:* Enable system-assigned identity for your IoT Central application
* Add the identity to the **Azure Service Bus Data Sender** role on the Service Bus namespace.
* Then, configure the Service Bus [export destination on your IoT Central application](https://learn.microsoft.com/en-us/azure/iot-central/core/howto-export-data) to use identity-based authentication.
 |
| Azure Digital Twins | Allows Azure Digital Twins to egress data to Service Bus topics in your Service Bus namespace. You also need to do the following steps: * Enable system-assigned identity for your Azure Digital Twins instance.
* Add the identity to the **Azure Service Bus Data Sender** role on the Service Bus namespace.
* Then, configure an Azure Digital Twins endpoint or Azure Digital Twins data history connection that uses the system-assigned identity to authenticate. For more information about configuring endpoints and event routes to Service Bus resources from Azure Digital Twins, see [Route Azure Digital Twins events](https://learn.microsoft.com/en-us/azure/digital-twins/concepts-route-events) and [Create endpoints in Azure Digital Twins](https://learn.microsoft.com/en-us/azure/digital-twins/how-to-create-endpoints).
 |

The other trusted services for Azure Service Bus can be found below:

* Azure Synapse
* Azure Data Explorer
* Azure Health Data Services
* Azure Monitor
* Azure Arc

#### Use Resource Manager template

This section has a sample Azure Resource Manager template that adds a virtual network and a firewall rule to an existing Service Bus namespace.

**ipMask** is a single IPv4 address or a block of IP addresses in CIDR notation. For example, in CIDR notation 70.37.104.0/24 represents the 256 IPv4 addresses from 70.37.104.0 to 70.37.104.255, with 24 indicating the number of significant prefix bits for the range.

Note

The default value of the `defaultAction` is `Allow`. When adding virtual network or firewalls rules, make sure you set the `defaultAction` to `Deny`.

JSON 

```
{
    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {
        "namespace_name": {
            "defaultValue": "mypremiumnamespace",
            "type": "String"
        }
    },
    "variables": {},
    "resources": [
        {
            "type": "Microsoft.ServiceBus/namespaces",
            "apiVersion": "2022-10-01-preview",
            "name": "[parameters('namespace_name')]",
            "location": "East US",
            "sku": {
                "name": "Premium",
                "tier": "Premium",
                "capacity": 1
            },
            "properties": {
                "premiumMessagingPartitions": 1,
                "minimumTlsVersion": "1.2",
                "publicNetworkAccess": "Enabled",
                "disableLocalAuth": false,
                "zoneRedundant": true
            }
        },
        {
            "type": "Microsoft.ServiceBus/namespaces/networkRuleSets",
            "apiVersion": "2022-10-01-preview",
            "name": "[concat(parameters('namespace_name'), '/default')]",
            "location": "East US",
            "dependsOn": [
                "[resourceId('Microsoft.ServiceBus/namespaces', parameters('namespace_name'))]"
            ],
            "properties": {
                "publicNetworkAccess": "Enabled",
                "defaultAction": "Deny",
                "virtualNetworkRules": [],
                "ipRules": [
                    {
                        "ipMask": "10.1.1.1",
                        "action": "Allow"
                    },
                    {
                        "ipMask": "11.0.0.0/24",
                        "action": "Allow"
                    }
                ]
            }
        }
    ]
}

```

To deploy the template, follow the instructions for [Azure Resource Manager](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/deploy-powershell).

Important

If there are no IP and virtual network rules, all the traffic flows into the namespace even if you set the `defaultAction` to `deny`. The namespace can be accessed over the public internet (using the access key). Specify at least one IP rule or virtual network rule for the namespace to allow traffic only from the specified IP addresses or subnet of a virtual network.

#### Use Azure CLI

Use [`az servicebus namespace network-rule`](https://learn.microsoft.com/en-us/cli/azure/servicebus/namespace/network-rule) add, list, update, and remove commands to manage IP firewall rules for a Service Bus namespace.

#### Use Azure PowerShell

Use the following Azure PowerShell commands to add, list, remove, update, and delete IP firewall rules.

* [`Add-AzServiceBusIPRule`](https://learn.microsoft.com/en-us/powershell/module/az.servicebus/add-azservicebusiprule) to add an IP firewall rule.
* [`New-AzServiceBusIPRuleConfig`](https://learn.microsoft.com/en-us/powershell/module/az.servicebus/new-azservicebusipruleconfig) and [`Set-AzServiceBusNetworkRuleSet`](https://learn.microsoft.com/en-us/powershell/module/az.servicebus/set-azservicebusnetworkruleset) together to add an IP firewall rule
* [`Remove-AzServiceBusIPRule`](https://learn.microsoft.com/en-us/powershell/module/az.servicebus/remove-azservicebusiprule) to remove an IP firewall rule.

#### default action and public network access

##### REST API

The default value of the `defaultAction` property was `Deny` for API version **2021-01-01-preview and earlier**. However, the deny rule isn't enforced unless you set IP filters or virtual network (VNet) rules. That is, if you didn't have any IP filters or VNet rules, it's treated as `Allow`.

From API version **2021-06-01-preview onwards**, the default value of the `defaultAction` property is `Allow`, to accurately reflect the service-side enforcement. If the default action is set to `Deny`, IP filters and VNet rules are enforced. If the default action is set to `Allow`, IP filters and VNet rules aren't enforced. The service remembers the rules when you turn them off and then back on again.

The API version **2021-06-01-preview onwards** also introduces a new property named `publicNetworkAccess`. If it's set to `Disabled`, operations are restricted to private links only. If it's set to `Enabled`, operations are allowed over the public internet.

For more information about these properties, see [Create or Update Network Rule Set](https://learn.microsoft.com/en-us/rest/api/servicebus/preview/namespaces-network-rule-set/create-or-update-network-rule-set) and [Create or Update Private Endpoint Connections](https://learn.microsoft.com/en-us/rest/api/servicebus/preview/private-endpoint-connections/create-or-update).

Note

None of the above settings bypass validation of claims via SAS or Azure AD authentication. The authentication check always runs after the service validates the network checks that are configured by `defaultAction`, `publicNetworkAccess`, `privateEndpointConnections` settings.

##### Azure portal

Azure portal always uses the latest API version to get and set properties. If you had previously configured your namespace using **2021-01-01-preview and earlier** with `defaultAction` set to `Deny`, and specified zero IP filters and VNet rules, the portal would have previously checked **Selected Networks** on the **Networking** page of your namespace. Now, it checks the **All networks** option.

![Screenshot of the Azure portal Networking page. The option to allow access from All networks is selected on the Firewalls and virtual networks tab.](https://learn.microsoft.com/en-us/azure/service-bus-messaging/media/service-bus-ip-filtering/firewall-all-networks-selected.png)
#### Next steps

For constraining access to Service Bus to Azure virtual networks, see the following link:

* [Virtual Network Service Endpoints for Service Bus](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-service-endpoints)
