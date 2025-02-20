---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/new-and-upcoming-capabilities-with-elastic-cloud-elasticsearch-an-azure-native-isv-service/","tags":["rw/articles"]}
---

![rw-book-cover](https://c.s-microsoft.com/favicon.ico?v2)

Microsoft and Elastic partnered together in 2020 to build an [Elastic Cloud (Elasticsearch)—An Azure Native ISV Service](https://aka.ms/azurenativeelasticcloud) to create cloud native deeply integrated experiences for all Azure and Elastic customers to power their digital transformation. Since [general availability](https://azure.microsoft.com/blog/search-made-simple-native-elastic-integration-with-azure-now-in-preview/), thanks to you, this service is growing rapidly while improving efficiency for all its customers.

Case in point is that Mr. Turing’s cognitive intelligence software as a service (SaaS) product “Alan”, greatly benefited from the native Elasticsearch offering on Azure and deep integration between products like Azure, GitHub, and Visual Studio Code, as elaborated in [their story here](https://customers.microsoft.com/story/1557429616211490364-mister-turing-professional-services-azure):

“*On Microsoft Azure, Alan is twice as fast and less costly to operate compared to when he was running on our previous cloud provider. In addition, because of the strong integration between Azure, GitHub, and Visual Studio Code, we can deliver new features faster than we could before*.”—Marcelo Noronha, Chief Executive Officer of Mr. Turing (October ’2022).

Microsoft and Elastic are continuously striving to bring more delightful experiences to our customers and enable newer capabilities to usher an era of superfast speed, massive scale, and trustworthy reliability.

#### Better together with Azure and Elastic Cloud

The core setup of Elastic Cloud (Elasticsearch)—An Azure Native ISV Service makes it simpler for developers and IT administrators to manage their Elastic deployments right from Azure. Users no longer must go through multiple manual steps to integrate Azure with Elastic or manage their own infrastructure.

While this is immensely beneficial, the true power relies on when we can continue to bring Elastic’s newer capabilities natively for Azure customers.

Here are a few of the newest capabilities added since announcing general availability:

##### Elastic 8.X version support

The [Elastic 8.X versions](https://www.elastic.co/blog/whats-new-elastic-8-0-0) bring enhancements to Elasticsearch’s vector search capabilities, native support for natural language processing models, increasingly simplified data onboarding, and a streamlined security experience. This helps people and teams connect quickly and search enterprise content to find relevant information and insights, enable observability to keep mission critical applications and infrastructure running, and protect entire digital ecosystems from increasingly sophisticated cyber threats. New Elastic deployments created using the Azure native service are automatically set up with the latest Elastic version, so that customers can leverage these enhanced capabilities easily out of the box.

##### Cluster and user management

Setting up Elastic clusters using the Azure native service ensures provisioning of the right configuration as part of deployment itself. Apart from automated cluster provisioning, we have also enabled user management capabilities where the primary owner or creator of the initial cluster can now add multiple users from the organization to manage the deployments. This helps ensure easy management of production workloads, even when the primary owner changes roles or moves out of the organization.

##### Private link

For customers who are interested in sending Azure resource and subscription logs to Elastic clusters setup at private link endpoint inside an Azure VNet, we have enabled easy configuration to set this up from right within the native experience. Users have the ability to set [traffic filters](https://www.elastic.co/guide/en/cloud/current/ec-traffic-filtering-vnet.html) for Azure private links, to manage how Elastic deployments can be accessed.

##### Observability resource types

We are constantly working to support all [resource categories on Azure Monitor](https://learn.microsoft.com/azure/azure-monitor/essentials/resource-logs-categories) to ship logs to Elastic. For customers who have setup monitoring tag rules in an Azure subscription, new resource types and categories get automatically enrolled for logs shipping, without the need for customers to manually do any changes to enable new resource types. As of now, the Azure native service supports logs shipping from 126 resource types to flow to Elastic.

##### Region expansion

Azure and Elastic teams have been continuously partnering to add additional regions support, to be available closer to where customers need the native offering and data residency. As of now, we support 16 Azure regions (including [four new regions](https://www.elastic.co/blog/elastic-cloud-is-now-available-on-microsoft-azure-in-4-new-regions)—South Africa North, Central India, Brazil South and Canada Central) for the Elastic Cloud (Elasticsearch)—An Azure Native ISV Service, and we are on the path to grow to additional regions.

#### Looking at the future

Here are some of the key capabilities that Microsoft and Elastic teams are working together to bring to you in the next six months:

##### Elastic version selection

Currently, the Elastic Cloud (Elasticsearch)—An Azure Native ISV Service automatically takes care of setting up Elastic with the right configuration and the latest cluster version. We heard from customers that there might be situations where the user consciously wants to create new resources leveraging an older Elastic version to support compatibility with their overall technology architecture. We are planning to address that by offering the flexibility to customers to select the Elastic version from right within the Azure portal experience.

##### Billing visibility enhancements

Given that today we support Elastic deployments to be set up across multiple Azure subscriptions—while still retaining the ability for customers to receive a unified bill—we are planning multiple enhancements on the native offering experience to bring visibility and transparency to billing resource and deployments that the usage and billing correspond to, so that customers can correlate better, optimize costs, or raise requests for support in case something is out of place.

##### Native experience for Elastic customers on standard Azure marketplace listing

Customers who started using Elastic on Azure by subscribing to the standard marketplace offer before the native offering went live, are missing out on the deep integration capabilities that the native Elastic Cloud (Elasticsearch service) brings to the table. Microsoft and Elastic teams are working together to migrate these customers to the Azure native service seamlessly, so that customers can get the added integration benefits.

There are many more exciting capabilities being planned for customers beyond the next six months, stay up to date with the latest news on [the Microsoft Azure blog](https://azure.microsoft.com/blog/).

#### Next steps

* Subscribe to the [Elastic Cloud (Elasticsearch)—An Azure Native ISV Service](https://aka.ms/azurenativeelasticcloud) from Azure marketplace.
* To learn more about the Elastic Cloud (Elasticsearch)—An Azure Native ISV Service, check out our documentation on the [Elastic integration with Azure](https://aka.ms/azurenativeelasticclouddocs).
* Watch the Microsoft Ignite session [The Elastic on Microsoft Azure Native Integration Story: Helping Customers Turn Challenges to Advantages](https://aka.ms/azurenativeelasticcloudignitesession) presented by Elastic.
* Share additional information about how you use resource and subscription logs to monitor and manage your cloud infrastructure and applications by [responding to this survey](https://aka.ms/ObservabilityScenariosSurvey).
