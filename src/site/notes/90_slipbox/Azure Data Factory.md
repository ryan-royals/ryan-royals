---
{"dg-publish":true,"permalink":"/90-slipbox/azure-data-factory/","tags":["notes"],"created":"2025-06-11T10:28:47.694+09:30","updated":"2026-03-03T09:55:32.435+10:30","dg-note-properties":{"created":"2023-05-02","modified":"2026-03-03","tags":"notes","related":["[[Azure]]"],"references":null}}
---


Azure Data Factory is a cloud based Extract-Transform-Load and Extract-Load-Transform tool used to manage data within Azure

It consists of the following key components:

- Pipelines
- Activities
- Datasets
- Linked Services
- Data Flows
- Integration Runtimes

## Technical Notes

### Networking

| Configuration | Inputs |
| ------------- | ------ |
| Ports         | 443    |  

<https://learn.microsoft.com/en-us/azure/data-factory/data-movement-security-considerations#firewall-requirements-for-on-premisesprivate-network>
