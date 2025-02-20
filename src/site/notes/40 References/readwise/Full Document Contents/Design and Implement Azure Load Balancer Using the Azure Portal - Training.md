---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/design-and-implement-azure-load-balancer-using-the-azure-portal-training/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)

[Previous](https://learn.microsoft.com/en-us/training/modules/load-balancing-non-https-traffic-azure/2-explore/) 

* #### Load balance non-HTTP(S) traffic in Azure

	+ [Introduction 2 min : Completed](https://learn.microsoft.com/en-us/training/modules/load-balancing-non-https-traffic-azure/1-introduction/)
	+ [Explore load balancing 6 min : Completed](https://learn.microsoft.com/en-us/training/modules/load-balancing-non-https-traffic-azure/2-explore/)
	+ [Design and implement Azure load balancer using the Azure portal 17 min : Completed](https://learn.microsoft.com/en-us/training/modules/load-balancing-non-https-traffic-azure/3-design-implement-azure-load-balancer-using-azure-portal/)
	+ [Exercise: Create and configure an Azure load balancer 15 min : Completed](https://learn.microsoft.com/en-us/training/modules/load-balancing-non-https-traffic-azure/4-exercise-create-configure-azure-load-balancer/)
	+ [Explore Azure Traffic Manager 14 min : Completed](https://learn.microsoft.com/en-us/training/modules/load-balancing-non-https-traffic-azure/5-explore-azure-traffic-manager/)
	+ [Exercise: Create a Traffic Manager profile using the Azure portal 7 min : Completed](https://learn.microsoft.com/en-us/training/modules/load-balancing-non-https-traffic-azure/6-exercise-create-traffic-manager-profile-using-azure-portal/)
	+ [Summary 1 min : Completed](https://learn.microsoft.com/en-us/training/modules/load-balancing-non-https-traffic-azure/7-summary/)

Achievements

 [Next](https://learn.microsoft.com/en-us/training/modules/load-balancing-non-https-traffic-azure/4-exercise-create-configure-azure-load-balancer/)  

 Completed 200 XP

**Azure Load Balancer** operates at layer 4 of the Open Systems Interconnection (OSI) model. It's the single point of contact for clients. Azure Load Balancer distributes inbound flows that arrive at the load balancer's front end to backend pool instances. These flows are according to configured load-balancing rules and health probes. The backend pool instances can be Azure Virtual Machines or instances in a virtual machine scale set.

#### Choosing a load balancer type

Load balancers can be public (also known as external) or internal (also known as private).

A [**public load balancer**](https://learn.microsoft.com/en-us/azure/load-balancer/components) can provide outbound connections for virtual machines (VMs) inside your virtual network. These connections are accomplished by translating their private IP addresses to public IP addresses. External load balancers are used to distribute client traffic from the internet across your VMs. That internet traffic might come from web browsers, module apps, or other sources.

An [**internal load balancer**](https://learn.microsoft.com/en-us/azure/load-balancer/components) is used where private IPs are needed at the frontend only. Internal load balancers are used to load balance traffic from internal Azure resources to other Azure resources inside a virtual network. A load balancer frontend can also be accessed from an on-premises network in a hybrid scenario.

![Diagram illustrating Internal and Public load balancers in Azure](https://learn.microsoft.com/en-us/training/wwl-azure/load-balancing-non-https-traffic-azure/media/load-balancer-3cfca04c.png)
#### Azure load balancer and availability zones

Azure services that support availability zones fall into three categories:

* Zonal services: Resources can be pinned to a specific zone. For example, virtual machines, managed disks, or standard IP addresses can be pinned to a specific zone, which allows for increased resilience by having one or more instances of resources spread across zones.
* Zone-redundant services: Resources are replicated or distributed across zones automatically. Azure replicates the data across three zones so that a zone failure doesn't impact its availability.
* Non-regional services: Services are always available from Azure geographies and are resilient to zone-wide outages and region-wide outages.

Azure Load Balancer supports availability zones scenarios. You can use Standard Load Balancer to increase availability throughout your scenario by aligning resources with, and distribution across zones. Review this document to understand these concepts and fundamental scenario design guidance.

A Load Balancer can either be zone redundant, zonal, or non-zonal. To configure the zone related properties (mentioned above) for your load balancer, select the appropriate type of frontend needed.

##### Zone redundant

![Diagram illustrating Zone redundant load balancers in Azure.](https://learn.microsoft.com/en-us/training/wwl-azure/load-balancing-non-https-traffic-azure/media/zone-redundant-019f3528.png)
In a region with Availability Zones, a Standard Load Balancer can be zone-redundant. This traffic is served by a single IP address.

A single frontend IP address survives zone failure. The frontend IP may be used to reach all (non-impacted) backend pool members no matter the zone. One or more availability zones can fail and the data path survives as long as one zone in the region remains healthy.

The frontend's IP address is served simultaneously by multiple independent infrastructure deployments in multiple availability zones. Any retries or reestablishment succeed in other zones not affected by the zone failure.

##### Zonal

You can choose to have a frontend guaranteed to a single zone, which is known as a zonal. This scenario means any inbound or outbound flow is served by a single zone in a region. Your frontend shares fate with the health of the zone. The data path is unaffected by failures in zones other than where it was guaranteed. You can use zonal frontends to expose an IP address per Availability Zone.

Additionally, the use of zonal frontends directly for load balanced endpoints within each zone is supported. You can use this configuration to expose per zone load-balanced endpoints to individually monitor each zone. For public endpoints, you can integrate them with a DNS load-balancing product like Traffic Manager and use a single DNS name.

![Diagram illustrating Zonal load balancers in Azure.](https://learn.microsoft.com/en-us/training/wwl-azure/load-balancing-non-https-traffic-azure/media/zonal-load-balancer-3933c0be.png)
For a public load balancer frontend, you add a zones parameter to the public IP. This public IP is referenced by the frontend IP configuration used by the respective rule.

For an internal load balancer frontend, add a zones parameter to the internal load balancer frontend IP configuration. A zonal frontend guarantees an IP address in a subnet to a specific zone.

#### Selecting an Azure load balancer SKU

Two SKUs are available when you create a load balancer in Azure: Basic load balancers and Standard load balancers. These SKUs differ in terms of their scenario scope and scale, features, and cost. Any scenario that is possible with the Basic load balancer can also be created with the Standard load balancer.

To compare and understand the differences, review the table below.

***Features***

**Standard Load Balancer**

**Basic Load Balancer**

Backend pool size

Supports up to 1000 instances.

Supports up to 300 instances.

Backend pool endpoints

Any virtual machines or virtual machine scale sets in a single virtual network.

Virtual machines in a single availability set or virtual machine scale set.

Health probes

TCP, HTTP, HTTPS

TCP, HTTP

Health probe down behavior

TCP connections stay alive on an instance probe down and on all probes down.

TCP connections stay alive on an instance probe down. All TCP connections end when all probes are down.

Availability Zones

Zone-redundant and zonal frontends for inbound and outbound traffic.

Not available

Diagnostics

Azure Monitor multi-dimensional metrics

[Azure Monitor logs](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-monitor-log)

HA Ports

Available for Internal Load Balancer

Not available

Secure by default

Closed to inbound flows unless allowed by a network security group. Internal traffic from the virtual network to the internal load balancer is allowed.

Open by default. Network security group optional.

Outbound Rules

Declarative outbound NAT configuration

Not available

TCP Reset on Idle

Available on any rule

Not available

Multiple front ends

Inbound and outbound

Inbound only

Management Operations

Most operations < 30 seconds

60-90+ seconds typical

SLA

[99.99%](https://azure.microsoft.com/support/legal/sla/load-balancer/v1_0/)

Not available

**Microsoft recommends Standard load balancer. Standalone VMs, availability sets, and virtual machine scale sets can be connected to only one SKU, never both. Load balancer and the public IP address SKU must match when you use them with public IP addresses.**

**SKUs aren't mutable; therefore, you cannot change the SKU of an existing resource.**

#### Creating and configuring an Azure load balancer

There are several tasks you need to perform to successfully create and configure an Azure Load Balancer.

##### Create the load balancer

In this example, we're looking at the tasks required to create and configure a **Public** (external) **load balancer** in a **Standard SKU**. The first task is to create the load balancer itself. During the creation process, a frontend IP configuration is created and a public IP address is assigned. You can also add a backend pool, create a health probe, and add load balancing rules during the creation process, but we add these components later in the process.

From the Azure portal home page, navigate to the Global Search bar and search **Load Balancer** then select **Load balancers**.

Choose **+ Create** or **Create load balancer** to start the process.

On the **Create load balancer** page, you must supply the following required information on the **Basics** tab:

| Setting | Value |
| --- | --- |
| **Subscription** | Select the Azure subscription that you want to create your new load balancer resource in. |
| **Resource group** | Here you can select an existing resource group or create a new one. |
| **Name** | Provide a unique name for the instance. |
| **Region** | Select the region where the virtual machines were created. |
| **Type** | This is where you select whether your load balancer is going to be **Internal** (private) or **Public** (external). If you choose **Internal**, you need to specify a virtual network and IP address assignment, but if you choose **Public**, you need to specify several Public IP address details. |
| **SKU** | Here you can select either the **Standard** SKU or the **Basic** SKU (for production workloads you should choose **Standard**, but for testing and evaluation and training purposes, you could choose **Basic**, but you won't get all the possible load balancer features). Depending on which SKU you select here, the remaining configuration options differ slightly. |
| **Tier** | This is where you select whether your load balancer is balancing within a region (**Regional**) or across regions (**Global**) - If you select the **Basic** SKU above, this setting is greyed out. |

![Screenshot of Create load balancer page on Basics tab.](https://learn.microsoft.com/en-us/training/wwl-azure/load-balancing-non-https-traffic-azure/media/create-load-balancer-basics.png)
After you select **Next: Frontend IP configuration**, select **+ Add frontend IP address** to add a public IP address for your public-facing front-end. You add a name for the frontend IP configuration, choose IP version and IP type, then add a Public IP Address. You can create a new public IP address for your public-facing front-end, or use an existing one. When creating a new public IP address, you specify the name and you also specify a name for your public IP address, and whether to use a dynamic or statically assigned IP address. You can optionally also assign an IPv6 address to your load balancer in addition to the default IPv4 one.

![Screenshot of Frontend IP configuration tab and Add frontend IP configuration options.](https://learn.microsoft.com/en-us/training/wwl-azure/load-balancing-non-https-traffic-azure/media/create-load-balancer-frontend-ip-configuration.png)
Once completed with the frontend IP configuration, select **Review + Create**, where the configuration settings for the new load balancer resource will be validated, and then you can select **Create** to deploy the resource.

![Screenshot of the configuration settings for the new load balancer after validation.](https://learn.microsoft.com/en-us/training/wwl-azure/load-balancing-non-https-traffic-azure/media/create-load-balancer-validation.png)
The resource starts to be deployed.

![Screenshot of Create load balancer - deployment complete.](https://learn.microsoft.com/en-us/training/wwl-azure/load-balancing-non-https-traffic-azure/media/create-load-balancer-complete.png)
When it completes, you can select **Go to resource** to view the new load balancer resource in the portal.

![Screenshot of View load balancer resource Overview page in Azure portal.](https://learn.microsoft.com/en-us/training/wwl-azure/load-balancing-non-https-traffic-azure/media/create-load-balancer-overview.png)
##### Add a backend pool

The next task is to create a backend pool in the load balancer and then adds your virtual machines to it.

From the Load balancer Overview page for your load balancer, select **Backend pools** under Settings and select **+ Add**.

![Screenshot of Load Balancer page and Backend pools window.](https://learn.microsoft.com/en-us/training/wwl-azure/load-balancing-non-https-traffic-azure/media/create-backend-pool-add.png)
You need to enter the following information on the **Add backend pool** page:

| Setting | Value |
| --- | --- |
| **Name** | Enter a unique name for the backend pool. |
| **Virtual network** | Select the name of the virtual network where the resources are located that you're adding to the backend pool. |
| **Backend Pool Configuration** | Select whether you want to associate the backend pool using the NIC or IP address of a resource. |

You could add existing virtual machines to the backend pool at this point, or you can create and add them later. You then select **Save** to add the backend pool.

![Screenshot of Add backend pool - Add.](https://learn.microsoft.com/en-us/training/wwl-azure/load-balancing-non-https-traffic-azure/media/create-backend-pool-configuration.png)
##### Add virtual machines to the backend pool

The next task is to add the virtual machines to the existing back-end pool.

On the **Backend pools** page, select the backend pool from the list.

![Screenshot of View backend pool in the load balancer.](https://learn.microsoft.com/en-us/training/wwl-azure/load-balancing-non-https-traffic-azure/media/add-vm-backend-pool-add.png)
You need to enter the following information to add the virtual machines to the backend pool:

| Setting | Value |
| --- | --- |
| **Virtual network** | Specify the name of the virtual network where the resources are located that you're adding to the backend pool. |
| **Backend Pool Configuration** | Select whether you want to associate the backend pool using the NIC or IP address of a resource. |

Then under the **IP configurations** section, select **+ Add**.

![Add VM to backend pool.](https://learn.microsoft.com/en-us/training/wwl-azure/load-balancing-non-https-traffic-azure/media/add-vm-backend-pool-2-eb71b178.png)
Select the virtual machines you want to add to the backend pool and select **Add**.

![View list of VMs added to backend pool.](https://learn.microsoft.com/en-us/training/wwl-azure/load-balancing-non-https-traffic-azure/media/add-vm-backend-pool-3-c6a69d39.png)
Then select **Save** to add them to the backend pool.

![Save backend pool with VMs added.](https://learn.microsoft.com/en-us/training/wwl-azure/load-balancing-non-https-traffic-azure/media/add-vm-backend-pool-4-956bad09.png)
![View list of backend pools running in load balancer.](https://learn.microsoft.com/en-us/training/wwl-azure/load-balancing-non-https-traffic-azure/media/add-vm-backend-pool-5-baabc018.png)
##### Add health probes

The next task is to create a health probe to monitor the virtual machines in the back-end pool.

On the **Backend pools** page of the load balancer, select **Health probes** under **Settings**, and then select **+ Add**. 

![Add health probes.](https://learn.microsoft.com/en-us/training/wwl-azure/load-balancing-non-https-traffic-azure/media/create-health-probe-1-aba00e8f.png)
You need to enter the following information on the **Add health probe** page:

| Setting | Value |
| --- | --- |
| **Name** | Enter a unique name for the health probe. |
| **Protocol** | Select either **TCP**, **HTTP**, or **HTTPS**. |
| **Port** | Specify the destination port number for the health signal. The default is port **80**. |
| **Interval (seconds)** | Specify the interval time in seconds between probe attempts. The default is **5** seconds. |

You then select **Save** to add the health probe.

![configure health probe settings.](https://learn.microsoft.com/en-us/training/wwl-azure/load-balancing-non-https-traffic-azure/media/create-health-probe-2-0a34ee7f.png)
![View list of added health probes in load balancer.](https://learn.microsoft.com/en-us/training/wwl-azure/load-balancing-non-https-traffic-azure/media/create-health-probe-3-b1f594b7.png)
##### Add a load balancer rule

The last task is to create a load balancing rule for the load balancer. A load balancing rule distributes incoming traffic that is sent to a selected IP address and port combination across a group of backend pool instances. Only backend instances that the health probe considers healthy receive new traffic.

On the **Health probes** page of the load balancer, select **Load balancing rules** under **Settings**, and then select **+ Add**.

![Add load balancing rule.](https://learn.microsoft.com/en-us/training/wwl-azure/load-balancing-non-https-traffic-azure/media/create-load-balancing-rule-1-7a88cf13.png)
You need to enter the following information on the **Add load balancing rule** page:

| Setting | Value |
| --- | --- |
| **Name** | Enter a unique name for the load balancing rule. |
| **IP Version** | Select either **IPv4** or **IPv6**. |
| **Frontend IP address** | Select the existing public-facing IP address of the load balancer. |
| **Backend pool** | Select an existing backend pool. The virtual machines in this backend pool are the target for the load balanced traffic of this rule. |
| **Protocol** | Select either the **TCP** or **UDP** protocol. |
| **Port** | Specify the port number for the load balancing rule. The default is port **80**. |
| **Backend port** | You can choose to route traffic to the virtual machine in the backend pool using a different port than the one that clients use by default to communicate with the load balancer (port 80). |
| **Health probe** | Select an existing health probe or create a new one. The load balancing rule uses the health probe to determine which virtual machines in the backend pool are healthy and therefore can receive load balanced traffic. |
| **Session persistence** | You can choose **None**, or **Client IP**, or **Client IP and protocol**. Session persistence specifies that traffic from a client should be handled by the same virtual machine in the backend pool for the duration of a session. **None** specifies that successive requests from the same client may be handled by any virtual machine. **Client IP** specifies that successive requests from the same client IP address will be handled by the same virtual machine. **Client IP and protocol** specifies that successive requests from the same client IP address and protocol combination will be handled by the same virtual machine. |
| **Idle timeout (minutes)** | Specify the time to keep a TCP or HTTP connection open without relying on clients to send *keep-alive* messages. The default idle timeout is **4** minutes, which is also the minimum setting. The maximum setting is 30 minutes. |
| **Enable TCP Reset** | Choose between **Disabled** or **Enabled**. With TCP Reset on Idle set to **Disabled**, Azure doesn't send a TCP reset packet when the idle timeout period is reached. With TCP Reset on Idle set to **Enabled**, Azure sends a TCP reset packet when the idle timeout period is reached. |
| **Enable Floating IP** | Choose between **Disabled** or **Enabled**. With Floating IP set to **Disabled**, Azure exposes a traditional load balancing IP address mapping scheme for ease of use (the VM instances' IP). With Floating IP set to **Enabled**, it changes the IP address mapping to the Frontend IP of the load balancer to allow for more flexibility. |
| **Outbound source network address translation (SNAT)** | Choose between **Disabled** or **Enabled**. With Outbound SNAT set to **Disabled**, Azure doesn't translate the source IP address of outbound flows to public IP addresses. With Outbound SNAT set to **Enabled**, Azure translates the source IP address of outbound flows to public IP addresses. |

![Screenshot of Add load balancing rule - Add.](https://learn.microsoft.com/en-us/training/wwl-azure/load-balancing-non-https-traffic-azure/media/create-load-balancing-rule-2-cd857974.png)
![Screenshot of View list of added load balancing rules.](https://learn.microsoft.com/en-us/training/wwl-azure/load-balancing-non-https-traffic-azure/media/create-load-balancing-rule-3-04f47848.png)
##### Test the load balancer

Having completed the various tasks to create and configure your public load balancer and its components, you should then test your configuration to ensure it works successfully. The simplest way to do this is to copy the **Public IP Address** from the public load balancer resource you created and paste it into a web browser. You should receive a response from one of the VMs in your load balancer. You could then stop whichever VM randomly responds, and once that VM has stopped, refresh the browser page to verify that you receive a response from the other VM in the load balancer instead.

#### Check your knowledge

1.

Which of the following statement about external load balancers is correct?

They have a public IP address.

They don't have a listener IP address.

They have a private, front-facing IP address.

2.

When deploying a new Azure Load Balancer that must support outbound traffic rules. Which SKU should be selected?

Standard

Basic

Either Standard or Basic

You must answer all questions before checking your work.
