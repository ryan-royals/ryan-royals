---
{"dg-publish":true,"permalink":"/90-slipbox/alz-accelerator/","tags":["notes"],"created":"2025-06-11T10:28:47.584+09:30","updated":"2026-04-06T18:11:04.349+09:30","dg-note-properties":{"tags":"notes","orgs":["[[Microsoft]]"],"related":["[[Terraform]]"],"created":"2023-10-27","modified":"2026-04-06"}}
---


Azure Landing Zones Accelerator is a Powershell Module used to provision the Platform of the [[90_slipbox/Azure Landing Zones\|Azure Landing Zones]] , as well as a Github repo & pipeline, and Managed Identities.  
It is a simple form that takes the basic inputs for the platform (name, network ranges, location) and also asks meta questions (Terraform or Bicep, Github; ADO or Terraform Cloud, Hub networking module or classic.)

Module Source code : <https://github.com/Azure/ALZ-PowerShell-Module>  
Repo that gets used as a template: <https://github.com/Azure/alz-terraform-accelerator>
