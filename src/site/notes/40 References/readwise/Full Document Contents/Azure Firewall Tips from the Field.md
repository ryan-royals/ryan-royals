---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/azure-firewall-tips-from-the-field/","tags":["rw/articles"]}
---

![rw-book-cover](https://techcommunity.microsoft.com/t5/image/serverpage/image-id/511933i1331CB5B611FB750/image-size/original?v=v2&px=-1)

#### Introduction

Hi folks! My name is Felipe Binotto, Cloud Solution Architect, based in Australia. 

In this post, I will provide some tips and clarifications about Azure Firewall based on my experience from the field. 

 

#### Topics

The following are the topics we are going to discuss. 

* Azure Firewall Policy Inheritance
* Azure Firewall Rule Processing Logic
* Azure Firewall Rule Collection Group, Rule Collection and Rule naming
* Azure Firewall DNS
* Azure Firewall FQDN and URL
* Azure Firewall Logging
* IP Groups
* Inbound and Outbound connections
* SNAT
* Infrastructure-as-Code

 

#### Rule Processing Logic

This is an important topic to understand before we can talk about anything else. The first thing to understand is that Azure Firewall denies all traffic by default. Therefore, you need to allow traffic based on your requirements. The second concept to understand is that rules are terminating which means if there is a match, the processing stops, and other rules are not evaluated. The third concept to understand is the logic of how firewall rules are processed: 

 

1. If you have Threat Intelligence enabled, these are the highest priority rules and are always processed first.
2. If there is a parent firewall policy, all DNAT rules are processed based on: 
	1. The highest Rule Collection Group
	2. The highest Rule Collection
3. Then for the child policy or only policy if no parent present, all DNAT rules are processed based on: 
	1. The highest Rule Collection Group
	2. The highest Rule Collection
4. Once all DNAT rules are processed, if there is a parent firewall policy, all Network rules are processed based on: 
	1. The highest Rule Collection Group
	2. The highest Rule Collection
5. Then for the child policy or only policy if no parent present, once all DNAT rules are processed, all Network rules are processed based on: 
	1. The highest Rule Collection Group
	2. The highest Rule Collection
6. Finally, once all DNAT and Network rules are processed, if there is a parent firewall policy, all Application rules are processed based on: 
	1. The highest Rule Collection Group
	2. The highest Rule Collection
7. Then for the child policy or only policy if no parent present, once all DNAT and Network rules are processed, all Application rules are processed based on: 
	1. The highest Rule Collection Group
	2. The highest Rule Collection

So, let’s take as an example the tables below:

 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rule Name**  | **Rule Type**  | **Priority**  | **Policy Type**  |
| Platform-RCG01  | Rule Collection Group  | 500  | Parent  |
| P-NAT-RC01  | DNAT Rule Collection  | 2000  | Parent  |
| P-APP-RC01  | Application Rule Collection  | 1000  | Parent  |
| P-NET-RC01  | Network Rule Collection  | 1100  | Parent  |
| P-NET-RC02  | Network Rule Collection  | 1500  | Parent  |

 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rule Name**  | **Rule Type**  | **Priority**  | **Policy Type**  |
| C-WorkloadA-RCG01  | Rule Collection Group  | 200  | Child  |
| C-NAT-RC01  | DNAT Rule Collection  | 5000  | Child  |
| C-APP-RC01  | Application Rule Collection  | 1200  | Child  |
| C-NET-RC01  | Network Rule Collection  | 1300  | Child  |

 

Based on the rule processing logic, rules should be processed in the following order: 

 

1. P-NAT-RC01
2. C-NAT-RC01
3. P-NET-RC01
4. P-NET-RC02
5. C-NET-RC01
6. P-APP-RC01
7. C-APP-RC01

 

#### Policy Inheritance

We briefly touched on policy inheritance on the previous section, but let’s talk about it in a broader sense. Firewall policies can have a parent firewall policy. The rules of the parent policy are processed before the rules of the child policy (not exactly as explained before). 

 

If you have only 1 firewall, it doesn’t necessarily make sense to have a parent policy; however, if you have multiple firewalls (perhaps across different regions) and those firewalls have rules in common, you can leverage a parent policy to define those rules. 

 

Here are some scenarios in which you might consider using an Azure Firewall parent policy: 

 

1. **Consistent Base Rules**: If you have certain firewall rules that should be enforced consistently across multiple environments or subscriptions (e.g., allowing traffic to a specific set of management servers or blocking traffic to known malicious IPs), you can set those rules in a parent policy. Child policies can then inherit these base rules.

 

1. **Tiered Access Control**: If your organization follows a tiered access model, you can create parent policies for each tier. Specific applications or environments can then inherit the right policy tier through child policies, and further refine rules as needed.

 

1. **Shared Environments**: For large organizations with shared Azure environments, a parent policy can ensure there's a consistent set of rules for shared resources. Individual teams or projects can then use child policies to add or adjust rules for their specific needs without affecting the base set of rules.

1. **Easier Management and Auditing**: By using a parent policy, you can simplify management and auditing. Any changes to the parent policy will automatically propagate to all child policies, ensuring consistency. This can be especially useful if you have regulatory or compliance requirements to meet.

 

#### Tips for a good naming convention

I always recommend your Rule Collection Groups, Rule Collections and Rules are clearly named to indicate their purpose. 

 

In my experience, there are 2 best ways to write our rules which I will provide examples below. 

In this first example, if I was going to create rules that are related to the Platform in a parent policy, I would create a new Rule Collection Group, named **P-PLATFORM-RCG01.**

 

Then let’s say I have to create a rule to allow RDP from a specific subnet on-prem to a specific subnet in my VNet and another rule for communication between AD Connect and On-prem Domain Controllers. I would create a Rule Collection named **P-NET-RC01** where I would add the 2 rules. The first I would name **RDP-10.0.2.0/24-to-10.100.5.0/24** and the second would be **AD-10.100.0.0/24-to-10.0.0.0/24.** 

 

As you can see in the figure below, the purpose of the rules and where they fit are very clear. 

 

 

![fbinotto_3-1695867405730.png](https://techcommunity.microsoft.com/t5/image/serverpage/image-id/511933i1331CB5B611FB750/image-size/large?v=v2&px=999 "fbinotto_3-1695867405730.png")

 

In my second example, I will use the same information from the previous example, but instead of creating a single Rule Collection, I’m going to create 2, one for each rule. So, we still have a Rule Collection Group named **P-PLATFORM-RCG01** and under it, we will have 2 Rule Collections named **P-RDP-RC01** and **P-ADCONNECT-RC01**. This makes their purpose very clear and easily identifiable as depicted in the figure below. 

 

![fbinotto_4-1695867449114.png](https://techcommunity.microsoft.com/t5/image/serverpage/image-id/511934iB0776C14DFB547CD/image-size/large?v=v2&px=999 "fbinotto_4-1695867449114.png")

 

To summarize, in both examples, we know those rules are Platform related and are in a parent policy (or single policy if no parent/child relationship). However, they differ in how we group the rules and describe their purpose. In the first example, we group the rules based on type (Network) and describe their purpose on the name of the Rule (RDP from 10.0.2.0/24 to 10.100.5.0/24). All rules of the same type would go in the same Rule Collection. In the second example, we group the rules based on their purpose (RDP) and provide traffic information as the Rule name (10.0.2.0/24 to 10.100.5.0/24). 

 

**Note:** Be aware of the maximum number of Rule Collection Groups which is 50 for policies created before July 2022 and 60 for policies created after July 2022. 

 

#### Azure Firewall DNS

I will not extend this section too much because there is plenty of documentation about it. However, there are two topics I want to talk about. 

 

**Resolution of internal DNS names** 

It’s important to understand that for the Azure Firewall to be able to resolve internal FQDNs or URLs you specify in your Network or Application rules, it needs to have DNS settings enabled and Custom DNS servers configured. Otherwise, when you try to resolve an internal DNS name, it will forward the query to 168.63.129.16 and it will not be able to resolve it. The firewall will **NOT** inherit the DNS settings from the VNet it is connected to. 

 

![fbinotto_5-1695867501480.png](https://techcommunity.microsoft.com/t5/image/serverpage/image-id/511935i59E251991D7D2421/image-size/large?v=v2&px=999 "fbinotto_5-1695867501480.png")

 

 

**Resolution of FQDN in Network rules** 

If you are using FQDN in your Network rules, make sure you have DNS Proxy enabled. Azure Firewall translates the FQDN to an IP address(es) based on the selected DNS server. This translation happens for both application and network rule processing. 

 

When a new DNS resolution takes place, new IP addresses are added to firewall rules. Old IP addresses that are no longer returned by the DNS server expire in 15 minutes. Azure Firewall rules are updated every 15 seconds from DNS resolution of the FQDNs in network rules. 

If a client computer is configured to use a DNS server that isn't the firewall DNS proxy, the results can be unpredictable. 

 

For example, assume a client workload is in US East, and uses a primary DNS server hosted in US East. Azure Firewall DNS server settings are configured for a secondary DNS server hosted in US West. The firewall’s DNS server hosted in US West results in a response different than that of the client in US East. 

 

This is a common scenario, and why clients should use the firewall’s DNS proxy functionality. Clients should use the firewall as their resolver if you use FQDNs in Network rules. You can ensure IP address resolution consistency by clients and the firewall itself. 

 

![fbinotto_6-1695867538143.png](https://techcommunity.microsoft.com/t5/image/serverpage/image-id/511936iEDC78A67127E2DF8/image-size/large?v=v2&px=999 "fbinotto_6-1695867538143.png")

 

#### Azure Firewall FQDN and URL

The only thing to understand in this section is that if you want to use URL paths for encrypted traffic (HTTPS), you must enable TLS inspection. For example, if you don’t enable TLS inspection, consider the following rules: 

 

 

#### Azure Firewall Logging

Configuring Firewall logs to be forwarded to Log Analytics is essential to be able to understand your traffic patterns and troubleshoot unexpected behavior. 

 

The figure below configures the Firewall to send all (non-legacy) logs to a Log Analytics workspace. I recommend you select the destination table as ‘Resource specific’ so that each log type has its own table. The advantages are: 

 

* It makes it much easier to work with the data in the log queries.
* It makes it easier to discover schemas and their structure.
* Improves performance across both ingestion latency and query times.
* Allows you to grant Azure RBAC rights on a specific table.

 

![fbinotto_7-1695867586839.png](https://techcommunity.microsoft.com/t5/image/serverpage/image-id/511937i0F1ADA60A918BC83/image-size/large?v=v2&px=999 "fbinotto_7-1695867586839.png")

 

 

For example, if a customer complains they can access any website but not google.com and you don’t know why because you didn’t create all the firewall rules, you could go to your Log Analytics workspace and easily identify the root cause. The figure below shows that google.com is getting blocked by a Rule named DenyGoogle part of the DenyWebsites Rule Collection. All the other websites can be accessed because there is another Rule named Allow All HTTPS part of the AllowHTTP Rule Collection. 

 

![fbinotto_8-1695867630310.png](https://techcommunity.microsoft.com/t5/image/serverpage/image-id/511938i0E390AA8BC7DF256/image-size/large?v=v2&px=999 "fbinotto_8-1695867630310.png")

 

 

The following KQL query will look up Application Rules for all denied outbound traffic which contains “google.com” as part of the FQDN. 

 

 

```
AZFWApplicationRule 
| where Action contains "Deny" 
| where Fqdn contains "google.com" 

```

 

 

If you want to check the traffic which you are allowing via Application Rules you can simply run the following KQL query.

 

 

```
AZFWApplicationRule 
| where Action contains "Allow"
```

 

 

One more example, look up all Network Rules for traffic on port TCP 3389 that was denied. 

 

 

```
AZFWNetworkRule 
| where Action contains “Deny” 
| where DestinationPort == “3389” 
| where Protocol contains “TCP” 
```

 

 

#### IP Groups

IP Groups allow you to group IP addresses to be used in Firewall rules. They can be used as follows: 

 

* As a source address in DNAT rules
* As a source or destination address in network rules
* As a source address in application rules

 

Let’s say you want to allow all traffic between 5 VNets across your Azure spokes. You would create an IP Group with the address space of those 5 VNets as per the figure below. 

 

![fbinotto_9-1695867664811.png](https://techcommunity.microsoft.com/t5/image/serverpage/image-id/511939iD57C59B5C6244DAC/image-size/large?v=v2&px=999 "fbinotto_9-1695867664811.png")

 

 

Now you can create an any-to-any rule between those 5 VNets by simply creating a network rule and set the IP Group as source and destination as displayed below. 

 

![fbinotto_10-1695867696980.png](https://techcommunity.microsoft.com/t5/image/serverpage/image-id/511940iDA7708DADD00B223/image-size/large?v=v2&px=999 "fbinotto_10-1695867696980.png")

 

#### Inbound and Outbound Connections

A couple things to understand about Inbound and Outbound connections. 

 

* Inbound traffic coming from the Internet directly to the Firewall can only be evaluated by DNAT rules. E.g., you cannot configure a network rule to allow traffic from public IPs to your private IPs.
* Network rules are used for inbound and outbound east/west traffic and outbound north/south traffic.
* Application rules are used for outbound traffic only. For inbound Layer 7 traffic, use Application Gateway with WAF instead.

 

#### SNAT

These are the things you need to understand about SNAT with Azure Firewall: 

 

* Outbound traffic to public IP addresses is always SNATed by default.
* Outbound traffic using private IPs will not be SNATed.
* Application rules are always SNATed.
* When SNAT in the Firewall happens, the destination will see the public IP address of the Firewall if the destination was a Public IP or one IP part of the AzureFirewallSubnet if the target was a private IP.

 

#### Infrastructure-as-Code

I really recommend you deploy your firewall and rules as code for the following reasons: 

 

* The code is your documentation.
* It is easy to read the rules in the code.
* It serves as a backup. If there is any issue you can always redeploy.
* It is easy to roll back a bad change.
* You can apply multiple rules together.

 

Refer to the following links for more information: 

 

[Deploy Firewall with Bicep](https://learn.microsoft.com/en-us/azure/firewall-manager/quick-firewall-policy-bicep) 

[Deploy Firewall with Terraform](https://learn.microsoft.com/en-us/azure/firewall-manager/quick-firewall-policy-terraform) 

[Deploy Firewall with ARM template](https://learn.microsoft.com/en-us/azure/firewall-manager/quick-secure-virtual-hub) 

 

#### Conclusion

Azure Firewall offers a comprehensive suite of functionalities designed to enhance security, manage traffic, and maintain optimal connectivity within Azure networks. Key highlights we discussed include: 

 

**Rule Processing Logic**: It's crucial to remember that Azure Firewall denies all traffic by default. The precedence of rule evaluation is paramount, from Threat Intelligence to child policies' Application rules. 

 

**Policy Inheritance**: This enables efficient management, particularly for multi-regional deployments, promoting a layered rule application approach. 

 

**Naming Convention**: Properly naming your rules ensures easy identification, troubleshooting, and organization, and can greatly affect how efficiently you manage and understand your firewall rules. 

 

**Azure Firewall DNS**: Addressing the significance of DNS settings, and the value of DNS Proxy to guarantee IP address resolution consistency. 

 

**Azure Firewall FQDN and URL**: Enabling TLS inspection is crucial when needing to filter based on URL paths in encrypted traffic. 

 

**Logging**: This is essential for comprehensive monitoring and troubleshooting. Directing logs to a specialized space can expedite issue detection and resolution. 

 

**IP Groups**: By facilitating the bundling of IP addresses, they simplify the process of rule creation, particularly for complex traffic patterns. 

 

**Inbound and Outbound Connections**: Understanding traffic direction and its relevance to the type of rule to be applied is fundamental. 

 

**SNAT**: It's important to understand how source NATting affects outbound traffic visibility, especially for security and compliance reasons. 

 

**Infrastructure-as-Code**: Adopting this approach not only simplifies deployment but also ensures consistency, transparency, and flexibility in firewall rule management. 

 

As digital landscapes continue to evolve, securing and managing your network's traffic flow remains of utmost importance. Azure Firewall, when appropriately configured, stands as a robust line of defense, safeguarding resources and ensuring smooth communication. Embracing best practices and understanding intricate functionalities, as highlighted in this guide, ensures you derive maximum benefits from your Azure Firewall deployment.  

 

I hope this was informative to you and thanks for reading! 

 

 

**Disclaimer** 

The sample scripts are not supported under any Microsoft standard support program or service. The sample scripts are provided AS IS without warranty of any kind. Microsoft further disclaims all implied warranties including, without limitation, any implied warranties of merchantability or of fitness for a particular purpose. The entire risk arising out of the use or performance of the sample scripts and documentation remains with you. In no event shall Microsoft, its authors, or anyone else involved in the creation, production, or delivery of the scripts be liable for any damages whatsoever (including, without limitation, damages for loss of business profits, business interruption, loss of business information, or other pecuniary loss) arising out of the use of or inability to use the sample scripts or documentation, even if Microsoft has been advised of the possibility of such damages.
