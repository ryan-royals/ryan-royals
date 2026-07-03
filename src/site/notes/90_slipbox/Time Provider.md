---
{"dg-publish":true,"permalink":"/90-slipbox/time-provider/","tags":["notes"],"created":"2026-03-27T09:57:51.497+10:30","updated":"2026-06-11T09:30:38.167+09:30","dg-note-properties":{"created":"2023-12-08","modified":"2026-06-11","references":["https://registry.terraform.io/providers/hashicorp/time/latest/docs/resources/sleep"],"related":["[[Terraform]]"],"tags":"notes"}}
---


The Time Provider is mostly used to add Sleep steps between operations, to not cause over run on API calls, and let resources deploy.  
Found that the `Triggers` style of adding sleep does not actually cause the operation to wait when chaining the trigger to the resource failing to wait.
