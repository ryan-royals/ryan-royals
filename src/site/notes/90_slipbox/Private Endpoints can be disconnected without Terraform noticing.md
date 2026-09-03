---
{"dg-publish":true,"permalink":"/90-slipbox/private-endpoints-can-be-disconnected-without-terraform-noticing/","tags":["today-i-learns"],"created":"2026-07-01T12:32:22.476+09:30","updated":"2026-07-06T14:28:41.180+09:30","dg-note-properties":{"created":"2026-07-01","modified":"2026-07-06","related":["[[Azure Private Endpoint]]","[[Terraform]]"],"tags":"today-i-learns"}}
---


If services like Function Apps are mysteriously headless where it can not reach its backend storage, it may be related to Private Endpoints being deployed, but stuck in a disconnected / deleting state. This is not revealed to Terraform, so the only way to clarify is to look in the Azure Portal.
