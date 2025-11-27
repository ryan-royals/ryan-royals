---
{"dg-publish":true,"dg-path":"Slipbox Notes/Azure Kubernetes Service.md","permalink":"/slipbox-notes/azure-kubernetes-service/","tags":["notes","claude"],"created":"2024-07-12","updated":"2025-11-27"}
---


## Azure Kubernetes Service (AKS)

**Core concept**: Microsoft-managed Kubernetes control plane that handles cluster operations while you manage worker nodes and applications.

**Start simple**: Begin with basic networking and storage, add complexity as needed  
**Embrace GitOps**: Treat cluster configuration as code  
**Monitor resource usage**: Right-size based on actual workload demands  
**Plan IP addressing**: CNI choice is hard to change later  
**Automate upgrades**: Don't let clusters fall behind on versions

### Managed Vs Self-Managed

**What Microsoft manages**:
- Kubernetes API server, etcd, controller manager, scheduler
- Control plane patching and upgrades
- SLA: 99.95% uptime for control plane
- Master node scaling and availability

**What you manage**:
- Worker nodes (VMs running your workloads)  
- Node OS updates and security patches
- Application deployments and configurations
- Cluster networking and storage

### AKS-Specific Features

**Node Pools**:
- Multiple VM types in single cluster
- System pools (cluster services) vs user pools (workloads)
- Spot instances for cost optimization
- Windows and Linux node support

**Automatic Scaling**:
- **Cluster Autoscaler**: Adds/removes nodes based on demand
- **Pod Autoscaler**: HPA + VPA support
- **Virtual Nodes**: Serverless pods via Azure Container Instances

**Azure Integrations**:
- **Azure CNI**: Native VNET integration with pod IP assignment
- **Azure Policy**: Governance via OPA Gatekeeper policies  
- **Azure Monitor**: Logs, metrics, and Container Insights
- **Azure Key Vault**: Secret injection via CSI driver
- **Azure AD**: Integrated authentication and RBAC

### Networking Options

**Kubenet (Basic)**:
- Nodes get VNET IPs, pods use private range
- NAT for pod egress traffic
- Simpler setup, fewer IP addresses required

**Azure CNI (Advanced)**:
- Pods get VNET IP addresses directly
- Better integration with Azure services
- Requires larger IP address space planning

**Calico Network Policies**: Micro-segmentation between pods

### Storage Integration

**Azure Disk**: High-performance SSD/HDD for single pod access  
**Azure Files**: Shared storage across multiple pods  
**Azure NetApp Files**: Enterprise NFS for high-performance workloads  
**Dynamic Provisioning**: Automatic volume creation via storage classes

### Security Features

**Azure AD Integration**:
- Users authenticate with Azure AD credentials
- Kubernetes RBAC maps to Azure AD groups
- Conditional access policies supported

**Pod Security**:
- Azure Policy for Pod Security Standards
- Image scanning via Microsoft Defender
- Network security groups integration

**Private Clusters**:
- API server accessible only via private endpoint
- No public internet access to control plane
- VPN or ExpressRoute required for management

### Monitoring & Observability

**Container Insights**:
- Pre-built dashboards for cluster health
- Node and pod performance metrics
- Live log streaming from containers

**Integration Options**:
- Azure Monitor Logs for centralized logging
- Prometheus + Grafana via marketplace
- Application Insights for application telemetry

### Development & CI/CD

**Azure DevOps Integration**:
- Built-in service connections
- YAML pipelines for deployments
- Helm chart support

**GitHub Actions**:
- Azure/k8s-deploy actions
- OIDC authentication without secrets
- GitOps workflows with Flux extension

**Draft**: Generates Kubernetes manifests from source code

### Cost Optimization

**Pricing Model**:
- **Control plane**: ~$73/month (managed for you)
- **Worker nodes**: Pay for VMs you provision
- **Bandwidth**: Standard Azure networking charges

**Cost-saving strategies**:
- Spot instance node pools (up to 90% savings)
- Reserved instances for predictable workloads
- Cluster autoscaler for right-sizing
- Azure Advisor recommendations

### Upgrade Management

**Control Plane Upgrades**:
- Microsoft handles automatically (with notification)
- Choose maintenance windows
- Non-disruptive to running workloads

**Node Upgrades**:
- You control timing and process
- Rolling updates with drain/cordon
- Automatic security patches available

### High Availability Options

**Availability Zones**:
- Control plane spans multiple zones automatically
- Node pools can be zone-redundant
- 99.95% SLA with zone support

**Multi-Region**:
- Deploy multiple clusters across regions
- Traffic Manager for DNS failover
- Shared Azure Container Registry

### Backup & Disaster Recovery

**Velero**: Cluster-level backup solution  
**Azure Backup**: Integration with Azure Backup service  
**GitOps**: Infrastructure as code for cluster recreation

### Extensions & Add-ons

**Microsoft-Managed Extensions**:
- **Azure Policy**: Governance and compliance
- **Dapr**: Microservices building blocks  
- **Istio**: Service mesh (preview)
- **Open Service Mesh**: Lightweight service mesh
- **GitOps (Flux)**: Automated deployments from Git

**Partner Extensions**:
- **Datadog**: Monitoring and observability
- **New Relic**: Application performance monitoring
- **Falco**: Runtime security monitoring

### When to Choose AKS

**Ideal scenarios**:
- Complex microservices requiring Kubernetes features
- Teams with Kubernetes expertise
- Need for custom operators or CNCF ecosystem
- Advanced networking or security requirements
- Multi-cloud portability strategy

**vs Container Apps**:
- More operational complexity but greater control
- Higher base costs but better resource optimization
- Learning curve vs rapid deployment
- Full Kubernetes ecosystem vs curated experience

### Common Pitfalls

**Overprovisioning**: Starting with too many/large nodes  
**Networking complexity**: CNI choice impacts future flexibility  
**Upgrade anxiety**: Delaying upgrades increases technical debt  
**Monitoring gaps**: Not implementing comprehensive observability  
**Security defaults**: Relying only on default security settings

### Integration with Azure Services

**Seamless integrations**:
- **Azure Container Registry**: Private image storage with vulnerability scanning
- **Azure Load Balancer**: Automatic service exposure
- **Azure Application Gateway**: Advanced ingress with WAF
- **Azure Firewall**: Network security for egress traffic
- **Log Analytics**: Centralized logging and querying

AKS bridges the gap between Kubernetes complexity and Azure cloud-native services, providing enterprise-grade container orchestration with reduced operational overhead compared to self-managed Kubernetes.
