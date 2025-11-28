---
{"dg-publish":true,"permalink":"/90-slipbox/terraform-parallelism-investigation/","tags":["notes"]}
---


Terraform by standard works on 10 operations at a time, being represented by the 10 defaults for the parallelism switch on the command line.  
Azure ARM does not have any documented limitation on concurrent operations but does limit to the number of operations per hour.  
There is a lack of documentation as to why 10 is the default, and any risks associated to upping the parallelism.

## Testing

Testing was conducted to see if scaling the Parallelism will produce a faster deployment. On paper, it makes sense that 100 parallelisms should be 10x faster than the default.  
Test was conducted deploying 16 Virtual Machines, Nics, Managed Disks and Virtual Network.

|   |   |
|---|---|
|**Parallelism Number**|**Total operation time**|
|10|11m3s|
|50|10m3s|
|100|7m47s|

## Findings

The results indicate that increasing the parallelism does decrease total operation time, but not in linear way.  
The current recommendation based on the findings is to not increase the default. This is to:

- Keep default settings so pipelines are easier to maintain.
- Minimize risk of overlapping resource deployments failing.
- Reduce risk of other unknown issues occurring from Terraform or ARM or any other Providers otherwise untested.
