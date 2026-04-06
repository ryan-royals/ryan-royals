---
{"dg-publish":true,"permalink":"/90-slipbox/terraform-parallelism-investigation/","tags":["notes"],"created":"2026-03-27T09:57:51.498+10:30","updated":"2026-03-27T09:57:51.498+10:30","dg-note-properties":{"created":"2023-12-12","tags":"notes","related":["[[Terraform]]"],"references":["https://arkahna.atlassian.net/jira/software/c/projects/AALZP/issues/AALZP-258?jql=project%20%3D%20%22AALZP%22%20AND%20text%20~%20%22concurrent%22%20ORDER%20BY%20created%20DESC","https://developer.hashicorp.com/terraform/cli/commands/apply#parallelism-n","https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/request-limits-and-throttling"],"modified":"2026-03-03"}}
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
