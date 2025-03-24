---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/public-preview-private-subnet/","tags":["rw/articles"]}
---

![rw-book-cover](https://azurecomcdn.azureedge.net/cvt-7c05f9e517923fd679a6e186eecacb1ba4b2a7170271d8a0142c0a3e471be91c/images/shared/social/azure-icon-250x250.png)

Announcing the public preview for the ability to create private subnets.

Currently, when virtual machines are created in a virtual network without any explicit outbound connectivity, they are assigned a default outbound public IP address. These implicit IPs are subject to change, not associated with a subscription, difficult to troubleshoot, and do not follow Azure's model of "secure by default" which ensures customers have strong security without additional steps needed. (The depreciation for this type of implicit connectivity was [recently announced](https://azure.microsoft.com/en-us/updates/default-outbound-access-for-vms-in-azure-will-be-retired-transition-to-a-new-method-of-internet-access/) and is scheduled for September 2025.)

The private subnet feature will let you prevent this insecure implicit connectivity for any newly created subnets by setting the "default outbound access" parameter to false. You can then pick your preferred method for explicit outbound connectivity to the internet.

For more information on private subnets and default outbound access, see our [documentation](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/default-outbound-access).
