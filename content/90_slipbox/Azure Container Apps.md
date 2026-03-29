---
{"dg-publish":true,"dg-path":"Slipbox Notes/Azure Container Apps.md","permalink":"/slipbox-notes/azure-container-apps/","tags":["notes","claude"],"created":"2023-03-31","updated":"2025-11-27"}
---


## Overview

Container Apps are fully managed environment that allows you to run microservices and containers on a serverless platform. Runs on [[90_slipbox/Azure Kubernetes Service\|Azure Kubernetes Service]] in the backend, but does not expose this.

Container Apps abstracts away Kubernetes complexity while retaining container benefits. Perfect for teams wanting modern deployment patterns without operational overhead.

**Trade-off**: Simplicity and cost efficiency vs control and flexibility. Most applications don't need full Kubernetes capabilities and benefit from the managed approach.

### Key Features

- Can run multiple container revisions
- HTTPS or TCP ingress
- Split traffic (Blue / Green deployments)
- Internal ingress and service discovery
- Run containers from any registry
- Connects into [[90_slipbox/Azure Virtual Network\|Azure Virtual Network]]
- Monitor with [[Azure Log Analytics Workspace\|Azure Log Analytics Workspace]]
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

### Architecture Foundation

**Underlying Stack**:
- **Kubernetes**: Container orchestration (hidden from user)
- **KEDA**: Event-driven autoscaling
- **Dapr**: Microservices building blocks  
- **Envoy**: Ingress and service mesh proxy

**Container Apps Environment**: Logical boundary providing shared networking, logging, and configuration

### Key Capabilities

**Serverless Scaling**:
- **Scale-to-zero**: No costs when idle
- **Event-driven**: 50+ scaling triggers (HTTP, queues, databases, schedules)
- **KEDA integration**: Built-in scalers for Azure services
- **Horizontal scaling**: Up to 300 replicas per app

**Networking Model**:
- **Internal ingress**: Service-to-service communication
- **External ingress**: Internet-facing endpoints
- **Automatic HTTPS**: Managed TLS certificates
- **Traffic splitting**: Blue/green and canary deployments
- **Service discovery**: Internal DNS resolution

**Revision Management**:
- **Multiple revisions**: Deploy new versions alongside existing
- **Traffic control**: Route percentage of traffic to different versions
- **Rollback capability**: Instant revert to previous revision

### Resource Management

**Compute Allocation**:
- **Preset combinations**: Limited CPU/memory pairings
  - 0.25 vCPU + 0.5Gi RAM
  - 0.5 vCPU + 1Gi RAM  
  - 1 vCPU + 2Gi RAM
  - 2 vCPU + 4Gi RAM
  - 4 vCPU + 8Gi RAM

**Limitations**: Cannot specify arbitrary resource combinations

### Scaling Triggers

**HTTP-based**: Concurrent requests, request rate  
**Azure Service Bus**: Queue depth, topic subscription  
**Azure Storage**: Blob count, queue messages  
**Database**: SQL query results, Cosmos DB change feed  
**Custom metrics**: Via Azure Monitor or external systems  
**Cron schedules**: Time-based scaling

### Configuration & Secrets

**Environment Variables**: Standard container configuration  
**Azure Key Vault**: Secure secret injection via references  
**Dapr Components**: External service connections (databases, message queues)  
**Config Maps**: Shared configuration across containers

### Monitoring & Observability

**Built-in Features**:
- **Application Insights**: Automatic telemetry collection
- **Log Analytics**: Structured logging and queries
- **Azure Monitor**: Metrics and alerting
- **Distributed tracing**: Via Dapr integration

**Log Queries**:

```kusto
ContainerAppConsoleLogs_CL
| where ContainerName_s == "api-service"
| where Log_s contains "ERROR"
| summarize count() by bin(TimeGenerated, 5m)
```

### Storage Options

**Limitations**:
- **Ephemeral storage**: Container filesystem (lost on restart)
- **Azure Files**: Shared file system mounting
- **No persistent volumes**: No StatefulSet equivalent

**External Dependencies**: Designed to use Azure PaaS services (SQL Database, Cosmos DB, Storage Account)

### Security Model

**Environment Isolation**: Apps within same environment can communicate freely  
**Managed Identity**: Authenticate to Azure services without secrets  
**HTTPS-only**: Built-in TLS termination  
**Network restrictions**: IP allowlists and VNET integration

**Limitations**:
- No pod-level security contexts
- No network policies between services
- Limited RBAC granularity

### Integration Patterns

**Event-Driven Architecture**:

```yaml
scale:
  rules:
  - name: servicebus-trigger
    custom:
      type: azure-servicebus
      metadata:
        queueName: orders
        messageCount: 5
```

**Dapr Service Invocation**: HTTP/gRPC communication between services  
**State Management**: External state stores via Dapr components

### Deployment Models

**Container Registry Sources**:
- Azure Container Registry
- Docker Hub  
- GitHub Container Registry
- Any OCI-compliant registry

**CI/CD Integration**:
- **GitHub Actions**: Built-in deployment actions
- **Azure DevOps**: Container Apps tasks
- **Infrastructure as Code**: Bicep, ARM, Terraform

### Cost Model

**Pay-per-use Pricing**:
- **vCPU consumption**: $0.000024 per vCPU-second
- **Memory consumption**: $0.000024 per 4GB-second  
- **Request charges**: $0.0000004 per request

**Example Cost Calculation**:

```
Normal operations: 2 vCPU × 8 hours × $0.000024 = $0.38/day
Flash traffic: 20 vCPU × 2 hours × $0.000024 = $0.96/event
Annual: ~$140 + event costs
```

### Performance Characteristics

**Cold Start**: 2-4 seconds (Azure Container Instances boot time)  
**Scaling Speed**: 30-60 seconds to reach target replicas  
**Network Latency**: +1-2ms overhead per Envoy proxy hop  
**Throughput Limits**: 300 concurrent instances per app

### Use Cases & Patterns

**API Backends**: REST APIs with variable load  
**Event Processing**: Queue-based message processing  
**Scheduled Jobs**: Cron-triggered batch operations  
**Microservices**: Service-oriented architectures  
**Webhooks**: Event receivers with scale-to-zero

### Limitations Vs AKS

**Cannot do**:
- Custom operators or controllers
- StatefulSets for databases
- Advanced networking (service mesh configuration)
- Custom security policies
- Multi-cluster deployments
- Persistent volume management

### When Container Apps Wins

**Ideal scenarios**:
- **Event-driven workloads** with unpredictable traffic
- **Microservices** with simple HTTP/messaging communication
- **Cost optimization** for intermittent usage patterns
- **Rapid development** without infrastructure management
- **Small to medium teams** without dedicated platform engineering

### Migration Considerations

**From VMs/App Service**: Containerize applications first  
**To AKS**: Straightforward - container images transfer directly  
**From Kubernetes**: May require architecture changes for stateful components

## Troubleshooting

### Container Apps Environment Deployment Timeout

When encountering issues, Container Apps can deploy for 30+ minutes and ultimately fail without much error tracking.  
Confirm that DNS is resolvable, as if calling to a failed DNS server, the deployment will not succeed.
