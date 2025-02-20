---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/azure-synapse-private-link-hub-implementation-guidance/","tags":["rw/articles"]}
---

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article4.6bc1851654a0.png)

Microsoft Teams 

![](cid:logo)

![](cid:b11f9000-7100-493b-afe3-ce000dfd231d)

Leigh Shayler
 
7 minutes ago 

Azure Synapse - Private Link Hub - Implementation Guidance 

Hi All,

We recently did a bit of a deep dive on Azure Synapse Private Link Hub for private connectivity to Azure Synapse. Particularly with regard to customers with multiple workspaces. The key take aways are:

* Azure Synapse Private Link Hub is not at all tied to a Workspace
* When you create a private link from the hub, it gives you a private IP address and private DNS record for
**web.azuresynapse.net** portal.
* Because you can only have a single DNS record for web.azuresynapse.net you can't create two hubs in a connected environment and have them be resolvable to all virtual networks.
* In a customer like HSS. If you put the Synapse Private Link Hub in a customer's spoke virtual network. Firewall restrictions will prevent other customers from accessing the Synapse Portal because they can't access things in other customers networks.

Therefore, you should

* Only deploy one private link hub in a shared / hub virtual network.
* This virtual network should be accessible (firewall rules) to all users / customers that require access to Synapse.
* You only need to create a single private link connection within the hub and link it to the shared / hub virtual network
* You should use DNS zones managed within the hub virtual network so that all users can resolve the name of
**web.azuresynapse.net**

There are plenty of docs on it, none of which are overly clear:

* [azure-docs/articles/synapse-analytics/security/how-to-connect-to-workspace-from-restricted-network.md
 at main · MicrosoftDocs/azure-docs (github.com)](https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/synapse-analytics/security/how-to-connect-to-workspace-from-restricted-network.md "https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/synapse-analytics/security/how-to-connect-to-workspace-from-restricted-network.md")
* [Azure
 Synapse Private Link hub. What is a Synapse Private Link Hub? | by Vijay K J | Medium](https://medium.com/@viju.coorg/azure-synapse-private-link-hub-4eb758df9e40 "https://medium.com/@viju.coorg/azure-synapse-private-link-hub-4eb758df9e40")
* [Synapse
 Connectivity Series Part #2 – Inbound Synapse Private Endpoints – Azure Aggregator (wordpress.com)](https://azureaggregator.wordpress.com/2023/01/27/synapse-connectivity-series-part-2-inbound-synapse-private-endpoints-2/ "https://azureaggregator.wordpress.com/2023/01/27/synapse-connectivity-series-part-2-inbound-synapse-private-endpoints-2/")

**Ryan** **Royals**,

Lee Borlace

![](cid:39210b1a-d0cd-4810-90f9-e698016b1654)

Ryan Royals
 
3 minutes ago 

Awesome, thanks!

So Private Link Hub in its actual implementation is actually just a Managed VNET that you can connect multiple Synapse workspaces to?

![](cid:39210b1a-d0cd-4810-90f9-e698016b1654)

Ryan Royals
 
2 minutes ago 

'Managed' holds a lot of weight in that name.

a Managed Virtual Network is not a Virtual Network

same as a Managed Private Endpoint is not a Private Endpoint

![](cid:39210b1a-d0cd-4810-90f9-e698016b1654)

Ryan Royals
 
just now 

Also, to be that guy.

Should this go into the Ark knowledge base? [Arkahna - Knowledge Base - Confluence (atlassian.net)](https://arkahna.atlassian.net/wiki/spaces/KB/overview "https://arkahna.atlassian.net/wiki/spaces/kb/overview")

[Go
 to Teams >](https://teams.microsoft.com/l/message/19:8f1ace7e639f43c8aceef0bea5c68d18@thread.tacv2/1698727767778?tenantId=0fee3d31-b963-4a1c-8f4a-ca367205aa65&lm=deeplink&lmsrc=email&emltid=45899741-d72a-45ba-9339-6141465345af&emltype=ShareToOutlook&linktype=openSkypeTeams&cmpid=ShareToOutlook) 

<div>
<div> </div>
<table align="center" border="0" cellpadding="0" cellspacing="0">
<tbody>
<tr>
<td style="max-width:800px; min-width:650px; border:solid; border-width:1px; border-color:#e6e6e6; border-radius:2px; box-shadow:0 0 10px rgba(0,0 ,0 ,0.08)">
<table align="center" border="0" cellpadding="0" cellspacing="0" style="object-fit: contain; min-width: 650px; max-width: 800px; border-color: rgb(230, 230, 230); word-break: break-word; background-color: rgb(255, 255, 255);" width="100%">
<tbody>
<tr>
<td style="background: rgb(99, 101, 162);">
<table style="width:100%">
<tbody>
<tr>
<td style='padding-left: 10px; font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; font-size: 20px; font-stretch: normal; line-height: 1.79; letter-spacing: normal; font-weight: normal; color: white;'>
Microsoft Teams </td>
<td style="padding-right:10px; width:30px">
<img data-outlook-trace="F:1|T:1" height="30" src="cid:logo" style="width:30px; height:30px" width="30"/>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td style="padding: 24px 10px 20px 12px; background-color: rgb(243, 242, 241);">
<table border="0" cellpadding="0" cellspacing="0" style="width:100%">
<tbody>
<tr>
<td style="width:40px; vertical-align:top; padding-top:10px">
<img data-outlook-trace="F:1|T:1" height="40" src="cid:b11f9000-7100-493b-afe3-ce000dfd231d" style="display:block; height:40px; width:40px; border-radius:50%" width="40"/>
</td>
<td style="padding-left:10px; vertical-align:top">
<table border="0" cellpadding="10" cellspacing="0" style="background: white; object-fit: contain; width: 100%; word-break: break-word;">
<tbody>
<tr>
<td style="border-left:3px solid #e97548">
<span style='font-size: 12px; font-weight: bold; font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; padding-left: 5px; color: rgb(50, 49, 48);'>Leigh Shayler
</span>   <span style='font-size: 12px; font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; color: gray;'>
7 minutes ago </span>
<div style='font-size: 18px; font-weight: 600; font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; padding-left: 5px; color: rgb(50, 49, 48);'>
Azure Synapse - Private Link Hub - Implementation Guidance </div>
<div style='font-size: 14px; font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; padding-left: 5px; color: rgb(50, 49, 48);'>
<p>Hi All,</p>
<p> </p>
<p>We recently did a bit of a deep dive on Azure Synapse Private Link Hub for private connectivity to Azure Synapse. Particularly with regard to customers with multiple workspaces. The key take aways are:</p>
<p> </p>
<ul>
<li>Azure Synapse Private Link Hub is not at all tied to a Workspace</li>
<li>When you create a private link from the hub, it gives you a private IP address and private DNS record for
<strong>web.azuresynapse.net </strong>portal.</li>
<li>Because you can only have a single DNS record for web.azuresynapse.net you can't create two hubs in a connected environment and have them be resolvable to all virtual networks.</li>
<li>In a customer like HSS. If you put the Synapse Private Link Hub in a customer's spoke virtual network. Firewall restrictions will prevent other customers from accessing the Synapse Portal because they can't access things in other customers networks.</li>
</ul>
<p>Therefore, you should</p>
<ul>
<li>Only deploy one private link hub in a shared / hub virtual network.</li>
<li>This virtual network should be accessible (firewall rules) to all users / customers that require access to Synapse.</li>
<li>You only need to create a single private link connection within the hub and link it to the shared / hub virtual network</li>
<li>You should use DNS zones managed within the hub virtual network so that all users can resolve the name of
<strong>web.azuresynapse.net</strong>
</li>
</ul>
<p> </p>
<p>There are plenty of docs on it, none of which are overly clear:</p>
<ul>
<li><a data-auth="NotApplicable" href="https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/synapse-analytics/security/how-to-connect-to-workspace-from-restricted-network.md" id="OWAd33650b1-e187-45f2-4fb3-8451a5a4c117" title="https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/synapse-analytics/security/how-to-connect-to-workspace-from-restricted-network.md">azure-docs/articles/synapse-analytics/security/how-to-connect-to-workspace-from-restricted-network.md
 at main · MicrosoftDocs/azure-docs (github.com)</a></li>
<li><a data-auth="NotApplicable" href="https://medium.com/@viju.coorg/azure-synapse-private-link-hub-4eb758df9e40" id="OWAb4344b77-2904-c5e1-905d-af0af455fdc0" title="https://medium.com/@viju.coorg/azure-synapse-private-link-hub-4eb758df9e40">Azure
 Synapse Private Link hub. What is a Synapse Private Link Hub? | by Vijay K J | Medium</a></li>
<li><a data-auth="NotApplicable" href="https://azureaggregator.wordpress.com/2023/01/27/synapse-connectivity-series-part-2-inbound-synapse-private-endpoints-2/" id="OWAc509d6a7-8552-ed49-e1f8-2ea4a7b114c6" title="https://azureaggregator.wordpress.com/2023/01/27/synapse-connectivity-series-part-2-inbound-synapse-private-endpoints-2/">Synapse
 Connectivity Series Part #2 – Inbound Synapse Private Endpoints – Azure Aggregator (wordpress.com)</a></li>
</ul>
<p><span itemid="0" itemscope="" itemtype="http://schema.skype.com/Mention" style="color: rgb(204, 74, 49);"><strong>Ryan</strong></span> <span itemid="1" itemscope="" itemtype="http://schema.skype.com/Mention" style="color: rgb(204, 74, 49);"><strong>Royals</strong></span>,
<span itemid="2" itemscope="" itemtype="http://schema.skype.com/Mention" style="color: rgb(98, 100, 167);">
Lee</span> <span itemid="3" itemscope="" itemtype="http://schema.skype.com/Mention" style="color: rgb(98, 100, 167);">Borlace</span></p>
</div>
</td>
</tr>
<tr>
<td style="background: rgb(253, 252, 251); border-top: 2px solid rgb(243, 242, 241); border-left: 3px solid rgb(98, 100, 167);">
<table border="0" cellpadding="0" cellspacing="0" style="width:100%; word-break:break-all; word-break:break-word">
<tbody>
<tr>
<td height="40" style="width:40px; vertical-align:top; padding-top:5px" width="42">
<img data-outlook-trace="F:1|T:1" height="40" src="cid:39210b1a-d0cd-4810-90f9-e698016b1654" style="display:block; height:40px; width:40px; border-radius:50%" width="40"/>
</td>
<td style="padding-left:10px; vertical-align:top">
<span style='font-size: 12px; font-weight: bold; font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; color: rgb(50, 49, 48);'>Ryan Royals
</span>   <span style='font-size: 12px; font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; color: gray;'>
3 minutes ago </span>
<div style='font-size: 14px; font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; color: rgb(50, 49, 48);'>
<div>
<div>Awesome, thanks!</div>
<div> </div>
<div>So Private Link Hub in its actual implementation is actually just a Managed VNET that you can connect multiple Synapse workspaces to?</div>
</div>
</div>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td style="background: rgb(253, 252, 251); border-left: 3px solid rgb(98, 100, 167);">
<table border="0" cellpadding="0" cellspacing="0" style="width:100%; word-break:break-all; word-break:break-word">
<tbody>
<tr>
<td height="40" style="width:40px; vertical-align:top; padding-top:5px" width="42">
<img data-outlook-trace="F:1|T:1" height="40" src="cid:39210b1a-d0cd-4810-90f9-e698016b1654" style="display:block; height:40px; width:40px; border-radius:50%" width="40"/>
</td>
<td style="padding-left:10px; vertical-align:top">
<span style='font-size: 12px; font-weight: bold; font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; color: rgb(50, 49, 48);'>Ryan Royals
</span>   <span style='font-size: 12px; font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; color: gray;'>
2 minutes ago </span>
<div style='font-size: 14px; font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; color: rgb(50, 49, 48);'>
<div>
<div>'Managed' holds a lot of weight in that name.</div>
<div>a Managed Virtual Network is not a Virtual Network</div>
<div>same as a Managed Private Endpoint is not a Private Endpoint</div>
</div>
</div>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td style="background: rgb(253, 252, 251); border-left: 3px solid rgb(98, 100, 167);">
<table border="0" cellpadding="0" cellspacing="0" style="width:100%; word-break:break-all; word-break:break-word">
<tbody>
<tr>
<td height="40" style="width:40px; vertical-align:top; padding-top:5px" width="42">
<img data-outlook-trace="F:1|T:1" height="40" src="cid:39210b1a-d0cd-4810-90f9-e698016b1654" style="display:block; height:40px; width:40px; border-radius:50%" width="40"/>
</td>
<td style="padding-left:10px; vertical-align:top">
<span style='font-size: 12px; font-weight: bold; font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; color: rgb(50, 49, 48);'>Ryan Royals
</span>   <span style='font-size: 12px; font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; color: gray;'>
just now </span>
<div style='font-size: 14px; font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; color: rgb(50, 49, 48);'>
<div>
<div>Also, to be that guy.</div>
<div itemprop="copy-paste-block">Should this go into the Ark knowledge base? <a data-auth="NotApplicable" href="https://arkahna.atlassian.net/wiki/spaces/KB/overview" id="OWAc0fa610a-d566-de55-635c-8fdd584548ae" title="https://arkahna.atlassian.net/wiki/spaces/kb/overview">
Arkahna - Knowledge Base - Confluence (atlassian.net)</a>
</div>
</div>
</div>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr align="right">
<td style="padding-right: 15px; padding-bottom: 20px; background-color: rgb(243, 242, 241);">
<a data-auth="NotApplicable" href="https://teams.microsoft.com/l/message/19:8f1ace7e639f43c8aceef0bea5c68d18@thread.tacv2/1698727767778?tenantId=0fee3d31-b963-4a1c-8f4a-ca367205aa65&amp;lm=deeplink&amp;lmsrc=email&amp;emltid=45899741-d72a-45ba-9339-6141465345af&amp;emltype=ShareToOutlook&amp;linktype=openSkypeTeams&amp;cmpid=ShareToOutlook" id="deeplink" style='font-size: 16px; font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; text-decoration: none; color: rgb(99, 101, 162);'><span style="text-decoration: none; color: rgb(99, 101, 162);">Go
 to Teams &gt; </span></a>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
</div>
