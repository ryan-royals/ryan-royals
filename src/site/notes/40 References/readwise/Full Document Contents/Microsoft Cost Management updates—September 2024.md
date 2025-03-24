---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/microsoft-cost-management-updates-september-2024/","tags":["rw/articles"]}
---

![rw-book-cover](https://azure.microsoft.com/en-us/blog/wp-content/uploads/2024/10/Azure_383201_Blog_241023.png)

Whether you’re a new student, a thriving startup, or the largest enterprise, you have financial constraints, and you need to know what you’re spending, where it’s being spent, and how to plan for the future. Nobody wants a surprise when it comes to the bill, and this is where [Microsoft Cost Management](https://azure.microsoft.com/services/cost-management/) comes in.

We’re always looking for ways to learn more about your challenges and how Microsoft Cost Management can help you better understand where you’re accruing costs in the cloud, identify and prevent bad spending patterns, and optimize costs to empower you to do more with less. Here are few updates that you may find useful:

* [Azure OpenAI Service costs](#_Azure_OpenAI_Costs)
* [New ways to save money with Microsoft Cloud](#_New_ways_to)
* [Documentation updates](#_Documentation_updates)
* [What’s next](#_What's_next?)

#### Azure OpenAI Service costs

As AI adoption accelerates across industries, organizations are increasingly integrating these technologies into their core operations. With the growing reliance on AI, it has become essential for our customers to manage their AI spend. (FinOps for AI). In [our last blog](https://azure.microsoft.com/en-us/blog/microsoft-cost-management-updates-august-2024/), I wrote about the hourly pricing for Azure OpenAI provisioned throughput units (PTUs) and the introduction of 1-month and 1-year Azure OpenAI provisioned reservations**.** Here, I will cover the tools we offer in [Cost Management](https://azure.microsoft.com/en-us/products/cost-management/) for you to analyze, monitor, and optimize your Azure OpenAI costs. Please note that the tools mentioned below are also applicable for other Azure services.

##### Analyze costs

We know [Cost analysis](https://aka.ms/costanalysis) is your go-to tool for getting insights into your costs Customizable views within Cost analysis enable you to group and filter by multiple cost attributes. You can view costs grouped by Tags, resource groups, locations, and more and use filters to focus on the desired attribute. The below screenshot shows the customizable views in Cost analysis.

![](https://azure.microsoft.com/en-us/blog/wp-content/uploads/2024/10/Picture1-6-1024x788.webp)
The good news is that you can use these existing views that most of you are already familiar with to analyze your Azure OpenAI costs as well by using the filters below:

Service name = Cognitive Services.

Service Tier/Meter subcategory = “Azure Open AI” or “Azure Open AI Reservation”

You could also use the “Resource Type = OpenAI” filter but the view wouldn’t include reservation purchases. The screenshot below shows the “Accumulated costs” view in Cost analysis using the filters mentioned above and grouped by meter. Grouping by meter allows you to see input/output costs for your different models for token-based deployments and PTU costs for PTU-based deployments for the selected scope.

![chart](https://azure.microsoft.com/en-us/blog/wp-content/uploads/2024/10/Picture2-4-1024x382.webp)
##### Monitor costs:

There are multiple ways to monitor [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service/) costs to ensure that they do not get out of control and stay within allotted budgets. Here I will cover two approaches available in cost management.

**Scheduled emails**:

Getting email updates for your costs is a great way to stay on top of them and analyze trends and anomalies. You can subscribe to automated emails for your private or shared views in Cost analysis using the “Subscribe” button on top of your desired view (as seen in the screenshot above) or through the [Scheduled Actions API](https://learn.microsoft.com/en-us/rest/api/cost-management/scheduled-actions?view=rest-cost-management-2023-11-01). You can also add members of your team to receive these emails on a daily, weekly, or monthly basis.

**Budgets**:

If you do not want to be surprised by your costs and keep your teams accountable for their spend, you must create budgets. With budgets you get alerts when the actual or forecasted costs exceed the threshold you have defined. You could create a budget for your Azure OpenAI costs using the filters mentioned above. Budgets also support calling [action groups](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups#create-an-action-group-in-the-azure-portal) when the threshold is met, which allows you to take automated actions like calling webhooks, creating tickets, and sending push notifications to the Azure mobile app so that you never miss an alert! Setting up budgets is really easy and can save you a lot of hassle explaining cost overruns. You can read more about budget creation [in our documentation](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets?tabs=psbudget), which covers both the Cost analysis and API experiences.

If you prefer a video tutorial, discover [how to create Azure Budgets](https://www.youtube.com/watch?v=MRWR_9JMsF4&t=5s). 

##### Optimize costs

Your cost optimization journey starts with identifying the correct [pricing](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/) model for your Azure OpenAI deployments. You have two models to choose from, provisioned throughput units (PTUs) and standard token-based deployments. You can use the [pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/) to estimate costs for these models based on your predicted usage. For PTU deployments, Azure Open AI Service provisioned reservations can help you save significant costs. You have the flexibility to go with a 1-month or a 1-year commitment. While purchasing reservations to optimize your costs is the first step in the right direction, it is equally important for you to monitor the utilization of these reservations to avoid any wastage. In Cost management, you can use the “Reservations + Hybrid benefit” blade to monitor the utilization of all your reservations. As seen in the screenshot below, it can be found under Optimization on the left-hand side menu in Cost management.

![graphical user interface, text, application](https://azure.microsoft.com/en-us/blog/wp-content/uploads/2024/10/Picture3-1.webp)
You can also create [reservation utilization alerts](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/reservation-utilization-alerts) to be proactively alerted when the utilization is below your configured threshold to maximize your benefits.

We hope you can leverage all these tools to manage your spending on Azure OpenAI Service, and as I mentioned above, these are applicable for all Azure services.

#### New ways to save money in the Microsoft Cloud

Here are some of the new and updated offers you might be interested in:

* [Generally Available: Azure Cosmos DB dynamic scaling—per region and per partition autoscale](https://azure.microsoft.com/en-us/updates/v2/Azure-Cosmos-DB-dynamic-scaling)
* [Generally Available: V5 reservations for Azure Database for PostgreSQL – Flexible Server](https://azure.microsoft.com/en-us/updates/v2/V5-reservations-for-Azure-Database)
* [Generally Available: Smaller Enterprise tier cache instance for Azure Cache for Redis](https://azure.microsoft.com/en-us/updates/v2/Smaller-Enterprise-tier-cache-instance-for-Azure-Cache-for-Redis)
* [Generally Available: Azure NetApp Files Reserved Capacity](https://azure.microsoft.com/en-us/updates/v2/ANF-Reserved-Capacity)
* [Generally Available: Azure Public IPs are zone redundant by default](https://azure.microsoft.com/en-us/updates/v2/Azure-Public-Ips-are-zone-redundant-by-default)
* [Public Preview: Live Resize for Azure Premium SSD v2 and Ultra Disks](https://azure.microsoft.com/en-us/updates/v2/Live-Resize-for-Azure-Premium-SSD-v2-and-Ultra-Disks)
* [Public Preview: Virtual machines node pools support in AKS](https://azure.microsoft.com/en-us/updates/v2/Virtual-machines-node-pools-support-in-AKS)

#### Documentation updates

Here are a few documentation updates you might be interested in this month:

New: [Save on select Linux VMs for a limited time](https://learn.microsoft.com/azure/cost-management-billing/reservations/limited-time-linux)

New: [Discover your Microsoft cloud footprint FAQ](https://learn.microsoft.com/azure/cost-management-billing/manage/discover-cloud-footprint)

New: [Manage a Microsoft Azure Consumption Commitment resource under a subscription](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/manage-consumption-commitment)

Update: [Save costs with Microsoft Azure OpenAI Service Provisioned Reservations](https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/azure-openai)

Update: [Azure product transfer hub](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/subscription-transfer)

Update: [Change contact information for an Azure billing account](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/change-azure-account-profile)

Update: [Permissions to buy an Azure savings plan](https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/permission-buy-savings-plan)

Want to keep an eye on all documentation updates? Check out the [Cost Management and Billing documentation change history](https://github.com/MicrosoftDocs/azure-docs/commits/main/articles/cost-management-billing) in the **azure-docs** repository on GitHub. If you see something missing, select **Edit** at the top of the document and submit a quick pull request. You can also submit a GitHub issue. We welcome and appreciate all contributions!

#### What’s next?

These are just a few of the big updates from last month. Don’t forget to check out the [previous Microsoft Cost Management updates](https://aka.ms/costmgmt/blog). We’re always listening and making constant improvements based on your feedback, so please keep the feedback coming.

Follow [@MSCostMgmt](https://twitter.com/mscostmgmt) on Twitter and subscribe to the [YouTube channel](https://aka.ms/costmgmt/videos) for updates, tips, and tricks. You can also share ideas and vote up others in the [Cost Management feedback forum](https://aka.ms/costmgmt/feedback) or [join the research panel](https://aka.ms/costmgmt/joinresearch) to participate in a future study and help shape the future of Microsoft Cost Management.

Want to learn more about Azure OpenAI Service for building generative AI applications? Visit the [product page](https://azure.microsoft.com/en-us/products/ai-services/openai-service) and [documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/) or try it out in [Azure AI Studio](https://ai.azure.com/).

The post [Microsoft Cost Management updates—September 2024](https://azure.microsoft.com/en-us/blog/microsoft-cost-management-updates-september-2024/) appeared first on [Microsoft Azure Blog](https://azure.microsoft.com/en-us/blog).
