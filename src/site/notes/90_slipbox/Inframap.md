---
{"dg-publish":true,"dg-path":"Slipbox Notes/Inframap.md","permalink":"/slipbox-notes/inframap/","tags":["notes"],"created":"2023-05-25","updated":"2025-11-28"}
---


Inframap is a tool used to generate a diagram of Terraform configuration based on a state file.  
It is like Terraforms own Graph command. But Inframap filters to make it human readable.

## Findings

I found that this is only looking for a VNET and grabbing he resources that depend on that. This is handy, but lacks information that we would like, as in the Managed Virtual Network for ADF.  
The graphs are also based on GraphViz, and not visually appealing.  
Alternate tooling would be suggested if presenting to a client.

Reference: [cycloidioinframap Read your tfstate or HCL to generate a graph specific for each provider, showing only the resources that are most importantrelevant.](https://github.com/cycloidio/inframap)
