---
{"dg-publish":true,"dg-path":"Slipbox Notes/Time Provider.md","permalink":"/slipbox-notes/time-provider/","tags":["notes"],"dg-note-properties":{"tags":"notes","related":["[[Terraform]]"],"references":["https://registry.terraform.io/providers/hashicorp/time/latest/docs/resources/sleep"],"created":"2023-12-08","modified":"2026-03-03"}}
---


The Time Provider is mostly used to add Sleep steps between operations, to not cause over run on API calls, and let resources deploy.  
Found that the `Triggers` style of adding sleep does not actually cause the operation to wait when chaining the trigger to the resource failing to wait.
