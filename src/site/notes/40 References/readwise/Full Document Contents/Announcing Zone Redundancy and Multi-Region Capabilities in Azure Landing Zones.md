---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/announcing-zone-redundancy-and-multi-region-capabilities-in-azure-landing-zones/","tags":["rw/articles"]}
---

![rw-book-cover](https://techcommunity.microsoft.com/t5/image/serverpage/image-id/592909i02E26D7975DE458B/image-size/original?v=v2&px=-1)

In today's dynamic business environment, the resilience of cloud infrastructure is not just a preference but a necessity. We are thrilled to announce the latest enhancements in Azure Landing Zones with the rollout of the first phase of zone redundancy and multi-region support, designed to meet the high demands for availability and resilience in your cloud deployments.

We also are announcing our plans and subsequent roadmap to make our ALZ Bicep and ALZ Terraform implementation options zone-redundant by the end of the calendar year (2024).

#### Zone Redundancy: A New Layer of Resilience

The addition of zone redundancy to Azure Landing Zones brings a significant improvement to the robustness of your cloud architecture. By enabling deployment across multiple [availability zones](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview) within Azure regions, your workloads can achieve higher levels of availability and fault tolerance. This ensures that even if one zone experiences an outage, your applications can continue to operate seamlessly, minimizing downtime and service interruptions, whilst also improving your SLA.

##### Benefits of Zone Redundancy:

* Enhanced High Availability: Applications can be deployed across different zones, safeguarding against single points of failure.
* Improved Fault Tolerance: Independent power, cooling, and networking in each zone means that an incident in one zone won’t affect the others.
* SLA Assurance: Azure provides robust service level agreements that support zone redundancy, reinforcing your uptime commitments.

#### Multi-Region Support: Global Expansion with Local Resilience

With multi-region support, Azure Landing Zones now enable your infrastructure to span across multiple Azure regions. This is particularly beneficial for businesses that require a global presence and need to ensure that regional outages do not affect their worldwide operations.

#### Advantages of Multi-Region Support:

* Span locations: Serve your customers from multiple regions, optimizing for performance and user experience.
* Disaster Recovery: In the event of a regional disruption, traffic can be redirected to alternate regions with minimal impact.
* Operational Flexibility: Diversify your deployment across regions to meet regulatory compliance and data sovereignty requirements.

#### What are we announcing today? (Phase 1a)

We are announcing [ALZ Portal](https://aka.ms/alz/portal) now fully supports zone redundancy with Availability Zones as well as the ability to deploy Azure Landing Zones to multiple Azure regions. Alongside this we have also introduced zone redundancy to our [Bicep](https://aka.ms/alz/bicep/accelerator) and [Terraform](https://aka.ms/alz/tf/accelerator) Accelerators.

![thumbnail image 1 of blog post titled 
	
	
	 
	
	
	
				
		
			
				
						
							Announcing Zone Redundancy and Multi-Region Capabilities in Azure Landing Zones
							
						
					
			
		
	
			
	
	
	
	
	
](https://techcommunity.microsoft.com/t5/image/serverpage/image-id/592909i02E26D7975DE458B/image-size/large?v=v2&px=999)
We have undertaken an extensive exercise to enhance our CAF documentation with the following guidance being updated:

To reflect our multi-region enhancements, we've also made an update to the Azure Landing Zones conceptual architecture diagram that you can also download [here](https://aka.ms/alz/visio).

![thumbnail image 2 of blog post titled 
	
	
	 
	
	
	
				
		
			
				
						
							Announcing Zone Redundancy and Multi-Region Capabilities in Azure Landing Zones
							
						
					
			
		
	
			
	
	
	
	
	
](https://techcommunity.microsoft.com/t5/image/serverpage/image-id/592917iBCB1756972FBFD2B/image-size/large?v=v2&px=999)
#### Next steps and Important information for existing ALZ Bicep and Terraform customers

Building on the great updates we've announced today, we need to adopt these changes into our Bicep and Terraform Infrastructure-as-Code offerings, as deployment defaults.

* Phase 1b by September 2024 - Bicep and Terraform Accelerators to include multi-region support
* Phase 2 by end of calendar year 2024 - ALZ Bicep and Terraform Modules will be zone redundant by default by default by end of calendar year 2024.

#### Conclusion

The integration of zone redundancy and multi-region support into Azure Landing Zones empowers organizations to elevate their cloud strategy. These enhancements align with our commitment to provide resilient infrastructure by default, ensuring that our customers can operate confidently in the cloud.

As you embark on or continue your cloud journey, consider these new features to fortify your deployments against the unexpected, keeping your services reliable, secure, and available—no matter what challenges arise.

We encourage you to leverage these latest offerings in your Azure deployment strategy to provide robust, resilient services to your customers. Stay tuned for more updates as we continue to innovate and enhance Azure Landing Zones.
