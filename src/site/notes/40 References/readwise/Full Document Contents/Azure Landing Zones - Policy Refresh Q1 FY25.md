---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/azure-landing-zones-policy-refresh-q1-fy-25/","tags":["rw/articles"]}
---

![rw-book-cover](https://techcommunity.microsoft.com/favicon.ico)

As you may be aware, the ALZ team release cadence is now on quarterly basis to help customers and partners manage change in their environments. Additionally, based on feedback from our community, partners and customers that we will only introduce breaking changes every half-year, this release, being 3 months since the last breaking change (FY24 H2), therefore does not contain any breaking changes.

With the generally "quiet" time over the summer (in the northern hemisphere), the ALZ team have taken advantage and worked on enhancing **security**, **quality** and **reliability** of ALZ's Policies.

##### Security

As a core priority for Microsoft, security comes first.

We've updated all our custom minimum TLS version policies to support TLS version 1.2 AND 1.3 as more Azure services roll out supporting TLS 1.3 (we are aware of built-in policies owned by other product teams that require updating and will be working with them in the months ahead).

Most significantly we've introduced the option to audit (for now but over time will increase to deny) the use of **virtual network private subnets,** via the built-in policy ["Subnets should be private"](https://www.azadvertizer.net/azpolicyadvertizer/7bca8353-aa3b-429b-904a-9229c4385837.html). This is a key security feature that ensures resources in a subnet cannot access the internet directly but must either go through a firewall or NAT gateway to egress, reducing exfiltration options for potentially compromised resources. We encourage our partners and customers to review this in their environments, more information can be found here on this topic ["Default outbound access in Azure - MS Learn".](https://learn.microsoft.com/azure/virtual-network/ip-services/default-outbound-access)

We're also addressing other items like disabling local authentication for automation accounts, which is a best practice.

##### Quality

This involved a lot of backend work and scripting to improve testing of contributions to meet the high standards our consumers expect, including enhancements to testing of custom policy contributions but most notably a complete overhaul of deployment testing using the ARM reference implementation (driven through the portal experience). We can now do full deployments depending on the nature of changes from policy only to selected networking topologies, significantly reducing the many hours needed to do end to end testing with every release.

Whilst this doesnt directly benefit our consumers, it does mean we can complete more work as an ALZ team as testing is enhanced and more efficient which in turn means ALZ can add more in each release for our consumers to benefit from.

##### AI Ready

Microsoft is heavily invested in the AI space, and ALZ plays a part in driving it's adoption at scale.

We're working with internal teams preparing to provide prescriptive guidance for customers leveraging Azure AI Services in their tenants. To support these teams and ensuring customers are following best practices securing the Azure AI Services in their tenants, we are releasing significant updates to our recommended policies and initiatives for:

* Azure OpenAI
* Cognitive Services/Search -> AI Services
* Machine Learning
* Bot Service (new) -> AI Bot Services

| **Note:** some services are changing names (as indicated above)

For those using the portal accelerator, the options to configure this are under "Workload Specific Compliance", which has been enhanced to provide a more friendly user experience journey and as before allows you to define the scope to apply:

![thumbnail image 1 of blog post titled 
	
	
	 
	
	
	
				
		
			
				
						
							Azure Landing Zones - Policy Refresh Q1 FY25
							
						
					
			
		
	
			
	
	
	
	
	
](https://techcommunity.microsoft.com/t5/image/serverpage/image-id/627693iF9CFE61663464E19/image-size/large?v=v2&px=999)thumbnail image 1 of blog post titled Azure Landing Zones - Policy Refresh Q1 FY25 
For those just looking to benefit from our awesome policy work in the AI space, head to our [wiki page](https://github.com/Azure/Enterprise-Scale/wiki/ALZ-Policies-Extra) that contains details and links to all of the policies mentioned above.

##### General

We have also made a number of small changes to policies and initiatives to update to the latest and greatest, or added much asked for features like adding the option to select either ALL or AUDIT only diagnostic settings logs to be sent to Log Analytics.

We updated initiatives to use a newer built-in policy versions, added additional configuration options - all driven by feedback from the field (please keep it coming!)

##### Closing

Do note that the ALZ Policy Refresh is released first to the portal experience (as this is where we currently host policy definitions & initiatives as a source of truth), and it takes a short time before these updates are incorporated in the other reference implementations like Terraform, Bicep, etc. Please do check the release notes on those repositories if you are using those implementations.

If you have suggestions for ALZ, please do submit a GitHub Issue over at <https://aka.ms/alz/repo>.

Please do also regularly review our What's New (<https://aka.ms/alz/whatsnew>), as this includes all the details of what has changed, including any updates needed between major releases.

And finally make sure to attend our community call <https://aka.ms/alz/communitycall> which we host every 3 months and discuss releases and also catch-up on the recordings of the previous ones at the same link!
