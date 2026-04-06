---
{"dg-publish":true,"dg-path":"Slipbox Notes/ALZ Accelerator.md","permalink":"/slipbox-notes/alz-accelerator/","tags":["notes"],"dg-note-properties":{"tags":"notes","orgs":["[[Microsoft]]"],"related":["[[90_slipbox/Azure Landing Zones\|Azure Landing Zones]]","[[Terraform]]"],"created":"2023-10-27","modified":"2026-03-03"}}
---


Azure Landing Zones Accelerator is a Powershell Module used to provision the Platform of the [[Azure Landing Zones]], as well as a Github repo & pipeline, and Managed Identities.  
It is a simple form that takes the basic inputs for the platform (name, network ranges, location) and also asks meta questions (Terraform or Bicep, Github; ADO or Terraform Cloud, Hub networking module or classic.)

Module Source code : <https://github.com/Azure/ALZ-PowerShell-Module>  
Repo that gets used as a template: <https://github.com/Azure/alz-terraform-accelerator>
