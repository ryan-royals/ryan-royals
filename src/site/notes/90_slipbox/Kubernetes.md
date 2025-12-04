---
{"dg-publish":true,"dg-path":"Slipbox Notes/Kubernetes.md","permalink":"/slipbox-notes/kubernetes/","tags":["notes","claude"],"created":"2024-09-06","updated":"2025-11-27"}
---


**Core concept**: Distributed systems operating system that manages containerized applications across clusters through declarative configuration.

## Architecture Overview

**Control Plane** (cluster brain):
- **API Server**: Single entry point for all cluster operations
- **etcd**: Distributed key-value store for cluster state
- **Controller Manager**: Runs control loops ensuring desired state
- **Scheduler**: Assigns pods to nodes based on resource requirements

**Worker Nodes** (compute muscle):
- **kubelet**: Node agent managing container lifecycle
- **Container Runtime**: Docker/containerd executing containers  
- **kube-proxy**: Network proxy handling service load balancing

## Core Abstraction Model

**Pods**: Smallest deployable unit (usually one container + shared storage/network)  
**Deployments**: Manage pod replicas, rolling updates, rollbacks  
**Services**: Stable network endpoints with load balancing  
**ConfigMaps**: Non-sensitive configuration data  
**Secrets**: Sensitive data (passwords, certificates)  
**Namespaces**: Virtual cluster isolation

## The Control Loop Pattern

**How Kubernetes works**:
1. **Desired State**: Declared via YAML manifests
2. **Current State**: Observed through continuous monitoring
3. **Control Loop**: Controllers reconcile differences automatically

Example: Deployment with 3 replicas → Pod crashes → Controller detects → Starts replacement → Returns to 3 replicas

## Key Capabilities

**Auto-healing**: Restarts failed containers, reschedules pods, replaces nodes  
**Horizontal Scaling**: Add/remove pod replicas based on CPU, memory, custom metrics  
**Rolling Updates**: Zero-downtime deployments with gradual replacement  
**Service Discovery**: Built-in DNS, automatic endpoint updates  
**Load Balancing**: Traffic distribution across healthy pods  
**Storage Orchestration**: Persistent volumes, dynamic provisioning  
**Secret Management**: Encrypted storage, secure pod injection

## Resource Management

**Requests vs Limits**:
- **Requests**: Guaranteed resources (used for scheduling)
- **Limits**: Maximum allowed usage (prevents resource starvation)

**Quality of Service Classes**:
- **Guaranteed**: Requests = Limits (highest priority)
- **Burstable**: Requests < Limits (medium priority)  
- **BestEffort**: No requests/limits (lowest priority, killed first)

## Networking Model

**Cluster Networking Requirements**:
- Every pod gets unique IP address
- Pods communicate without NAT
- Nodes communicate with pods without NAT
- Pod sees its own IP (no NAT confusion)

**Service Types**:
- **ClusterIP**: Internal cluster access only
- **NodePort**: Exposes service on each node's IP
- **LoadBalancer**: Cloud provider load balancer
- **ExternalName**: DNS CNAME mapping

## ConfigMap Deep Dive

**Storage**: Lives in etcd (Kubernetes' key-value store)  
**Scope**: Namespaced resource with cluster-wide persistence  
**Size limit**: 1MB maximum per ConfigMap  
**Data type**: Plain text key-value pairs only

**Consumption Methods**:
- Environment variables
- Command-line arguments  
- Volume mounts (files in filesystem)

**Persistence Model**: ConfigMap exists independently of pod lifecycle → survives pod/node failures

## Scaling Patterns

**Horizontal Pod Autoscaler (HPA)**:
- Scales pod replicas based on CPU, memory, custom metrics
- Works with Deployments, StatefulSets, ReplicaSets

**Vertical Pod Autoscaler (VPA)**:
- Adjusts resource requests/limits automatically
- Right-sizes containers based on actual usage

**Cluster Autoscaler**:
- Adds/removes nodes based on pending pods
- Integrates with cloud provider APIs

## Security Architecture

**RBAC (Role-Based Access Control)**:
- Users → Roles → Resources permissions
- ServiceAccounts for pod-level access control

**Pod Security Standards**:
- **Privileged**: Unrestricted access (avoid)
- **Baseline**: Minimally restrictive
- **Restricted**: Heavily restricted (recommended)

**Network Policies**: Firewall rules controlling pod-to-pod traffic

## Storage Ecosystem

**Persistent Volumes (PV)**: Cluster storage resources  
**Persistent Volume Claims (PVC)**: Pod storage requests  
**Storage Classes**: Dynamic provisioning templates  
**StatefulSets**: Ordered deployment for stateful apps

## Ecosystem & Operators

**Service Mesh**: Istio, Linkerd (traffic management, security, observability)  
**GitOps**: ArgoCD, Flux (automated deployments from Git)  
**Monitoring**: Prometheus, Grafana (metrics and dashboards)  
**Package Management**: Helm (application templates)  
**Policy Engines**: OPA Gatekeeper (admission control)

## When Kubernetes Makes Sense

**Sweet spot scenarios**:
- Microservices architectures (5+ services)
- High availability requirements
- Complex deployment strategies
- Multi-environment consistency  
- Compliance/security requirements
- Team has platform engineering expertise

## Common Anti-patterns

**Kubernetes overkill**:
- Single monolithic application
- Small team without ops expertise
- Simple applications with predictable load
- Startups focused on product-market fit

## Operational Reality

**Day 2 Operations**:
- Cluster upgrades every 3-4 months
- Security patching and certificate management
- Monitoring/logging infrastructure maintenance
- Backup and disaster recovery procedures
- Capacity planning and cost optimization

**Complexity Tax**: ~50 hours/month operational overhead for production clusters

## Expert Insight

Kubernetes solves real distributed systems problems but introduces significant operational complexity. The platform is incredibly powerful when you need its capabilities, but many teams adopt it prematurely.

**Key decision factor**: Do your distributed systems requirements justify the operational investment? If not, consider managed alternatives first.
