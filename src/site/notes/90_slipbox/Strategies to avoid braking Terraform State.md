---
{"dg-publish":true,"permalink":"/90-slipbox/strategies-to-avoid-braking-terraform-state/","tags":["notes"]}
---


Terraform State files are similar to a JSON structure, that  simply tracks deployed resources. They less break and more can be configured incorrectly. The times they are referred to as broken is either when a bad configuration has been applied to the state file, or if there has been configuration drift in the cloud platform that has not been represented in the Terraform project files. For a true break to happen on the state file, you would have to edit the file by hand, which you never need to do. Terraform offers tooling to modify the state file (Untrack resources, import others, etc). These tools are robust and work well.

If a bad configuration has been applied that does not work in the Terraform code (Something like a SKU on a resource that does not exist). This is usually resolved by fixing the issues and then applying the fix. Worse case we use Azure Storage Accounts with snapshots enabled on the Blobs so we can roll back to a time just before the bad configuration was applied.

If there has been configuration drift, this is resolved by updating the Terraform files, or importing the new resources to be managed in the state file to the state file. This is typically a symptom of the DevOps workflow being skipped and someone directly using the Azure Portal or other tooling to update the platform.

Otherwise the real 1 sentence:  
Terraform state only breaks dramatically if you edit it by hand. We use snapshots on the state store as point in time backups and never edit it by hand, as there is never a need to.
