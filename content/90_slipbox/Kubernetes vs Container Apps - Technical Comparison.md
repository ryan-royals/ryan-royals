---
{"dg-publish":true,"dg-path":"Slipbox Notes/Kubernetes vs Container Apps - Technical Comparison.md","permalink":"/slipbox-notes/kubernetes-vs-container-apps-technical-comparison/","tags":["notes","claude"],"created":"2025-01-09","updated":"2025-11-28"}
---


**Core difference**: Kubernetes exposes orchestration primitives directly; Container Apps abstracts them into a serverless model.

## Architecture & Control

**Container Apps**
- Curated Kubernetes distribution with Microsoft's opinionated choices
- Hidden control plane (etcd, API server, controllers)
- Built on Kubernetes + KEDA + Dapr + Envoy
- Single declarative resource model

**Kubernetes**
- Full control plane access and configuration
- Direct manipulation of pods, services, deployments, configmaps
- Choose your own networking (CNI), service mesh, operators
- Multiple resource types requiring coordination

## Networking & Traffic Management

**Container Apps**
- Automatic service discovery via internal domains
- Built-in Envoy proxy (not configurable)
- Automatic HTTPS with managed certificates
- Limited to basic traffic splitting
- No custom ingress controllers or network policies

**Kubernetes**
- Custom ingress controllers (nginx, traefik, istio-gateway)
- Service mesh configuration (Istio, Linkerd)
- Network policies for micro-segmentation
- Advanced traffic patterns (circuit breakers, retries, fault injection)
- Multi-cluster networking capabilities

## Scaling & Resource Management

**Container Apps**
- KEDA-powered scaling with 50+ built-in triggers
- Scale-to-zero by default
- Preset CPU/memory combinations only
- Event-driven scaling (queues, HTTP, custom metrics)
- No control over scaling velocity or policies

**Kubernetes**
- Horizontal Pod Autoscaler (HPA) + Vertical Pod Autoscaler (VPA)
- Custom metrics via Prometheus + KEDA
- Granular resource requests/limits (any combination)
- Pod disruption budgets and scaling policies
- Cluster autoscaling for node provisioning

## Security Model

**Container Apps**
- Environment-level security boundary
- Basic security controls
- Managed identities for Azure services
- No pod-level security contexts or network policies
- Limited compliance framework support

**Kubernetes**
- Pod Security Standards and custom security contexts
- RBAC for fine-grained access control
- Network policies for traffic segmentation
- OPA Gatekeeper for policy enforcement
- Runtime security with tools like Falco
- Multi-layer defense in depth

## Data & Storage

**Container Apps**
- Ephemeral storage + Azure Files mounting
- No persistent volumes or storage classes
- Forces external services (Azure SQL, Redis, Storage)
- No StatefulSets for ordered deployments

**Kubernetes**
- Full persistent volume ecosystem
- Multiple storage classes (SSD, HDD, local)
- StatefulSets for databases and queues
- Volume snapshots and backup strategies
- Custom storage operators

## Cost Model

**Container Apps**
- Pay-per-use: vCPU-seconds + memory-GB-seconds + requests
- True scale-to-zero (no idle costs)
- No cluster management overhead
- Example: ~$300/year for typical microservices with intermittent load

**Kubernetes**
- Always-on infrastructure costs (nodes, load balancer, storage)
- Reserved instance pricing available (up to 72% savings)
- Operational overhead (platform engineering)
- Example: ~$6,800/year base + scaling costs

## Operational Complexity

**Container Apps**
- ~14 hours/month operational overhead
- Microsoft manages: OS patching, cluster upgrades, certificates
- You manage: application deployment, configuration, troubleshooting

**Kubernetes**
- ~50 hours/month operational overhead
- You manage: cluster upgrades, node patching, monitoring setup, security policies
- Plus application management complexity

## Migration Complexity

**Container Apps → Kubernetes**: Moderate (2-6 weeks)
- Container images transfer directly
- Need to rewrite YAML manifests (deployment, service, ingress)
- Add monitoring, logging, security configurations

**Kubernetes → Container Apps**: Variable (1-4 weeks to months)
- **Blockers**: StatefulSets, custom operators, advanced networking
- **Architecture changes**: External services replace in-cluster dependencies
- **Limitations**: Preset resource combinations, reduced control

## Performance Characteristics

**Container Apps**
- Cold start: 2-4 seconds (Azure Container Instances)
- Scaling time: 30-60 seconds to reach full scale
- Network latency: +1-2ms per Envoy hop
- Throughput limit: 300 instances per app

**Kubernetes**
- No cold starts (min replicas configurable)
- Scaling time: 10-20 seconds for pods, 2-3 minutes for nodes
- Custom network optimization (eBPF with Cilium)
- Virtually unlimited throughput scaling

## When Container Apps Wins

- **Event-driven architectures** with unpredictable traffic
- **Cost optimization** for intermittent workloads
- **Small teams** without dedicated platform engineering
- **Rapid development** and time-to-market priorities
- **Simple microservices** with standard communication patterns

## When Kubernetes Becomes Essential

- **Complex stateful workloads** requiring in-cluster data stores
- **Advanced networking** requirements (service mesh, multi-cluster)
- **Strict compliance** needing custom security policies
- **High-performance** applications requiring resource optimization
- **Multi-cloud portability** strategies
- **Custom operators** and CNCF ecosystem tooling

## Expert Decision Framework

**Technical sophistication spectrum**:

```
Simple ←→ Complex
Container Apps ←→ Kubernetes

Serverless ←→ Infrastructure-focused
Container Apps ←→ Kubernetes

Fast Time-to-Market ←→ Full Control
Container Apps ←→ Kubernetes
```

**Bottom line**: Most teams overestimate their need for Kubernetes complexity. Container Apps solves 90% of containerized application requirements with 10% of the operational burden. Start with Container Apps; migrate to Kubernetes when you hit specific limitations that justify the complexity investment.
