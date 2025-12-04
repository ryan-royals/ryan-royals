---
{"dg-publish":true,"dg-path":"Slipbox Notes/Azure DevOps Pipeline issue interacting with Azure Storage.md","permalink":"/slipbox-notes/azure-dev-ops-pipeline-issue-interacting-with-azure-storage/","tags":["notes"],"created":"2024-01-18","updated":"2025-11-28"}
---

There is a known issue with Azure DevOps, that when interacting with Azure Services deployed in the same region as the ADO instance, it uses a private ip to interact, and will not be allowed through Azure Storage Account whitelist.  
This is problematic with Terraform, as we can not start the pipeline to interact with the state file.  
As you can not add a private IP to the Azure Storage Firewall, the only reasonable solution that has been found so far is to trigger the pipeline to instead Allow all connections to the firewall.

Tried a few solutions, including changing the routing from Microsoft to Internet routing, but no change.
