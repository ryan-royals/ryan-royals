---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/public-preview-change-actor/","tags":["rw/articles"]}
---

![rw-book-cover](https://azurecomcdn.azureedge.net/cvt-7c05f9e517923fd679a6e186eecacb1ba4b2a7170271d8a0142c0a3e471be91c/images/shared/social/azure-icon-250x250.png)

With Change Analysis you can now see who initiated the change and with which client that change was made, for changes across all your tenants and subscriptions.

**Audit, troubleshoot, and govern at scale** 

By using Azure Resource Graph to query your resource changes, you can craft charts and pin results to Azure dashboards based on specific change queries.

 **What’s new: Actor Functionality**

* Who made the change
* With which client the change was made
* What operation was called

**Try it out**

You can try it out by querying the “resourcechanges” or “resourcecontainerchanges” tables in Azure Resource Graph.

**Sample Query**

*The following query shows the Summarization of who and which client were used to make resource changes in the last 7 days ordered by the number of changes* 

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

If you're just getting started with changes and want to learn how to query resourcechanges and resourcecontainerchanges in Azure Resource Graph, you can learn about the service here**.**

[Get resource configuration changes - Azure Resource Graph | Microsoft Learn](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fazure%2Fgovernance%2Fresource-graph%2Fhow-to%2Fget-resource-changes%3Ftabs%3Dazure-cli&data=05%7C02%7Ciancarter%40microsoft.com%7Cf09309997dc348653ebe08dc34b10e3f%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C638443182260384197%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=9HlHP4daqEAlqZSmSAl0Ev4of5%2FxzpVit397vXAzdvI%3D&reserved=0)
