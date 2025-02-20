---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/announcing-the-general-availability-of-change-actor/","tags":["rw/articles"]}
---

![rw-book-cover](https://cdn.techcommunity.microsoft.com/assets/Azure/BlogPreview_default-blue.png)

**Change Analysis**

Identifying who made a change to your Azure resources and how the change was made just became easier! With Change Analysis, you can now see who initiated the change and with which client that change was made, for changes across all your tenants and subscriptions.

**Audit, troubleshoot, and govern at scale** 

Changes should be available in under five minutes and are queryable for fourteen days. In addition, this support includes the ability to craft charts and pin results to Azure dashboards based on specific change queries.

**What’s new: Actor Functionality**

* Who made the change
	+ This can be either ‘AppId’ (client or Azure service) or email-ID of the user
	+ *changedBy: elizabeth@contoso.com*

* With which client the change was made
	+ *clientType: portal*

* What operation was called
	+ [Azure resource provider operations | Microsoft Learn](https://learn.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations)

**Try it out**

You can try it out by querying the “resourcechanges” or “resourcecontainerchanges” tables in [Azure Resource Graph](https://ms.portal.azure.com/#view/HubsExtension/ArgQueryBlade).

**Sample Queries**

Here is documentation on how to query resourcechanges and resourcecontainerchanges in Azure Resource Graph. [Get resource changes - Azure Resource Graph | Microsoft Learn](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fazure%2Fgovernance%2Fresource-graph%2Fhow-to%2Fget-resource-changes%3Ftabs%3Dazure-cli&data=05%7C01%7Ciancarter%40microsoft.com%7C2848c427a96c4268c4f408db94b3aa89%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C638267271743328012%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=0Il95EThZS8AciSyMG5KxbkCUqAIxR85JQwFnJ4XQK8%3D&reserved=0)

The following queries all show changes made within the last 7 days.

*Summarization of who and which client were used to make resource changes in the last 7 days ordered by the number of changes*

resourcechanges

| extend changeTime = todatetime(properties.changeAttributes.timestamp),

targetResourceId = tostring(properties.targetResourceId),

changeType = tostring(properties.changeType), changedBy = tostring(properties.changeAttributes.changedBy),

changedByType = properties.changeAttributes.changedByType,

clientType = tostring(properties.changeAttributes.clientType)

| where changeTime > ago(7d)

| project changeType, changedBy, changedByType, clientType

| summarize count() by changedBy, changeType, clientType

| order by count\_ desc

*Summarization of who and what operations were used to make resource changes ordered by the number of changes*

resourcechanges

| extend changeTime = todatetime(properties.changeAttributes.timestamp),

targetResourceId = tostring(properties.targetResourceId),

operation = tostring(properties.changeAttributes.operation),

changeType = tostring(properties.changeType), changedBy = tostring(properties.changeAttributes.changedBy),

changedByType = properties.changeAttributes.changedByType,

clientType = tostring(properties.changeAttributes.clientType)

| project changeType, changedBy, operation

| summarize count() by changedBy, operation

| order by count\_ desc

*List resource container (resource group, subscription, and management group) changes. who made the change, what client was used, and which operation was called, ordered by the time of the change*

resourcecontainerchanges

| extend changeTime = todatetime(properties.changeAttributes.timestamp),

targetResourceId = tostring(properties.targetResourceId),

operation=tostring(properties.changeAttributes.operation),

changeType = tostring(properties.changeType), changedBy = tostring(properties.changeAttributes.changedBy),

changedByType = properties.changeAttributes.changedByType,

clientType = tostring(properties.changeAttributes.clientType)

| project changeTime, changeType, changedBy, changedByType, clientType, operation, targetResourceId

| order by changeTime desc

**FAQ**

**How do I use Change Analysis?**

Change Analysis can be used by querying the **resourcechanges** or **resourcecontainerchanges** tables in Azure Resource Graph, such as with Azure Resource Graph Explorer in the Azure Portal or through the Azure Resource Graph APIs.

More information can be found here: [Get resource changes - Azure Resource Graph | Microsoft Learn.](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fazure%2Fgovernance%2Fresource-graph%2Fhow-to%2Fget-resource-changes%3Ftabs%3Dazure-cli&data=05%7C01%7Ciancarter%40microsoft.com%7C2848c427a96c4268c4f408db94b3aa89%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C638267271743328012%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=0Il95EThZS8AciSyMG5KxbkCUqAIxR85JQwFnJ4XQK8%3D&reserved=0)

**What does unknown mean?**

**Unknown** is displayed when the change happened on a client that is unrecognized. Clients are recognized based on the user agent and client application id associated with the original change request.

**What does System mean?**

**System** is displayed as a changedBy value when a background change occurred that wasn’t correlated with any direct user action.

**What resources are included?**   

You can try it out by querying the “resourcechanges” or “resourcecontainerchanges” tables in [Azure Resource Graph](https://ms.portal.azure.com/#view/HubsExtension/ArgQueryBlade).

**Questions and Feedback** 

* If you have any other questions or input, you can reach out to the team at [argchange@microsoft.com](mailto:argchange@microsoft.com)
* Share Product feedback and ideas with us at [Azure Governance · Community](https://feedback.azure.com/d365community/forum/675ae472-f324-ec11-b6e6-000d3a4f0da0)
* For more information about Change Analysis [Get resource changes - Azure Resource Graph | Microsoft Learn](https://learn.microsoft.com/en-us/azure/governance/resource-graph/changes/get-resource-changes?tabs=azure-cli)
