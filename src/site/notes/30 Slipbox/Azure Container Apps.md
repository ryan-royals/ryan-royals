---
{"dg-publish":true,"dg-path":"Azure Container Apps.md","permalink":"/azure-container-apps/","tags":["notes"]}
---


## Azure Container Apps

Container Apps are fully managed environment that allows you to run microservices and containers on a serverless platform. Runs on [[Kubernetes\|Kubernetes]] in the backend, but does not expose this.

### Key Features

- Can run multiple container revisions
- HTTPS or TCP ingress
- Split traffic (Blue / Green deployments)
- Internal ingress and service discovery
- Run containers from any registry
- Connects into [[30 Slipbox/Azure Virtual Network\|Azure Virtual Network]]
- Monitor with [[30 Slipbox/Azure Log Analytics Workspace\|Azure Log Analytics Workspace]]
- Can auto scale based on:
  - HTTP traffic
  - Event-driven processing
  - CPU or Memory load
  - KEDA supported scaler

### Example Usage

- API Endpoints
- Background processing applications
- Event-driven processing
- Microservices

### Troubleshooting

- Container Apps does not work when deploying to a Subnet with a NAT Gateway

---

Links: [[30 Slipbox/Azure\|Azure]]  
Tags:  
Reference: [Azure Container Apps overview | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-apps/overview)
