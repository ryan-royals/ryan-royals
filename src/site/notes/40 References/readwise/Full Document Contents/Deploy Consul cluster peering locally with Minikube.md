---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/deploy-consul-cluster-peering-locally-with-minikube/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.datocms-assets.com/2885/1620083637-blog-library-product-consul-dark-gradient.jpg)

As you scale Kubernetes, you will often find yourself with multiple clusters running different services. [HashiCorp Consul’s service mesh on Kubernetes](https://developer.hashicorp.com/consul/docs/k8s/connect) helps register and manage requests between services from a single point of control. But how do you manage traffic between services across multiple Consul datacenters on different Kubernetes clusters? [Cluster peering](https://developer.hashicorp.com/consul/docs/connect/cluster-peering) connects Consul datacenters across multiple Kubernetes clusters using [administrative partitions](https://developer.hashicorp.com/consul/docs/enterprise/admin-partitions#default-admin-partition), and offers one point of control to manage traffic across Kubernetes clusters.

This post shows how to use [Minikube](https://minikube.sigs.k8s.io/docs/) to create multiple Kubernetes clusters in your local development environment to test Consul’s cluster peering and configure services across clusters. Testing locally allows you to verify configurations for services and the requests between services in Consul service mesh before applying changes to your production clusters. The post also dives into a [set of Bash scripts](https://github.com/joatmon08/consul-minikubes) to automate the creation and configuration of Kubernetes and Consul clusters that you can adapt for your own local testing environment.

Note that your local development environment must support [Docker](https://www.docker.com/products/docker-desktop/) and offer sufficient resources to run multiple clusters. You can also use a driver that creates clusters in virtual machines. However, not all operating systems support virtual machine drivers. If you create a virtual machine with VirtualBox, you can [attach](https://github.com/joatmon08/consul-minikubes/blob/e57ba618e8ac73af424950aa8f9ed6c87e62c3cb/start.sh) a [host-only network](https://www.virtualbox.org/manual/ch06.html#network_hostonly) to each cluster and configure MetalLB to use that network.

#### Set up a Docker bridge network

By default, Minikube sets up each Kubernetes cluster on its own [Docker bridge network](https://docs.docker.com/network/bridge/). This allows clusters to communicate with each other but does not reflect the scenario of external access to a Kubernetes service through a load balancer. Attach each Minikube virtual machine to a second bridge network. The load balancers run in the second network to simulate mesh gateways communicating over a public network..

Create a network named `metallb` using Docker, with an IP address range of 172.28.0.0/16. Restrict the IP range for Minikube clusters to 172.28.0.0/24 to ensure you do not have overlapping IP addresses for each load balancer:

```
$ SUBNET="172.28.0.0/16"
$ IP_RANGE="172.28.0.0/24"
$ NETWORK_ID=$(docker network create metallb \
--subnet=${SUBNET} --ip-range=${IP_RANGE})
```
Each load balancer in each cluster must have its own IP address range so they can route to each other.

#### Start Minikube with MetalLB

Consul’s cluster peering requires a [mesh gateway](https://developer.hashicorp.com/consul/docs/connect/gateways/mesh-gateway) to facilitate communication between datacenters on different Kubernetes clusters. The mesh gateways require a load balancer to facilitate inbound and outbound requests to services in each Kubernetes cluster. For the load balancer, this example uses [MetalLB](https://metallb.universe.tf/), a Minikube addon, which creates a bare-metal load balancer for your cluster.

Start Minikube with the MetalLB addon and set a profile to indicate a specific Kubernetes cluster, in this example `dc1`:

```
$ minikube start -p dc1 --driver=docker --addons=metallb
```
Connect the cluster to the `metallb`network:

```
$ docker network connect metallb dc1
```
After the Kubernetes cluster starts, configure the `ConfigMap` for MetalLB under `addresses` with an IP address range in the subnet you allocated to the Docker network. For example, you can set the third octet of the network to the number of the cluster:

```
echo "apiVersion: v1
data:
 config: |
   address-pools:
   - name: default
     protocol: layer2
     addresses:
     - 172.28.1.3-172.28.1.254
kind: ConfigMap
metadata:
 name: config
 namespace: metallb-system" | kubectl apply -f -
```
MetalLB will use IP addresses from this range when you request a Kubernetes service with a load balancer. You will need to configure each Kubernetes cluster with its own profile and update MetalLB’s `ConfigMap` with an IP address range from the `metallb` network.

#### Install Consul and mesh gateways

Each Kubernetes cluster has its own Consul cluster and datacenter. Update the Helm values with a Consul datacenter to match the Minikube profile name. Set up TLS and enable mesh gateways for Consul cluster peering. By default, the Helm chart will create a Kubernetes service with a `LoadBalancer` type for the mesh gateway. Install Consul to the `consul` namespace:

```
echo "global:
 name: consul
 datacenter: dc1

 tls:
   enabled: true

 peering:
   enabled: true

 acls:
   manageSystemACLs: true

connectInject:
 enabled: true

meshGateway:
 enabled: true" | helm install consul hashicorp/consul --create-namespace --namespace consul -f -

```
After Consul runs, configure the mesh to peer through mesh gateways:

```
echo "apiVersion: consul.hashicorp.com/v1alpha1
kind: Mesh
metadata:
 name: mesh
spec:
 peering:
   peerThroughMeshGateways: true" | kubectl apply --namespace consul -f -
```
Update Consul’s proxies to access services through their local mesh gateway:

```
echo "apiVersion: consul.hashicorp.com/v1alpha1
kind: ProxyDefaults
metadata:
 name: global
spec:
 meshGateway:
   mode: local" | kubectl apply --namespace consul -f -
```
Repeat these configurations for each Kubernetes cluster you create through Minikube.

#### Set up cluster peering

Peer only the clusters that have services communicating with each other in production to maintain least-privilege. The [script](https://github.com/joatmon08/consul-minikubes/blob/main/consul.sh#L16) included in this post peers all clusters to each other for testing purposes. This example peers `dc1` to `dc2`.

Configure `dc1` as the peering acceptor, which creates a peering token and sets the target peer to `dc2`:

```
echo "apiVersion: consul.hashicorp.com/v1alpha1
kind: PeeringAcceptor
metadata:
 name: dc2
spec:
 peer:
   secret:
     name: peering-token-dc1-to-dc2
     key: data
     backend: kubernetes" | kubectl --context dc1 apply --namespace consul -f -

```
Extract the peering token and copy it to `dc2`:

```
kubectl --context dc1 --namespace consul \
get secret peering-token-dc1-to-dc2 --output yaml | \
kubectl --context dc2 --namespace consul apply -f -
```
Set up `dc2` as the peering dialer, which initiates the peering request to `dc1`:

```
echo "apiVersion: consul.hashicorp.com/v1alpha1
kind: PeeringDialer
metadata:
 name: dc2
spec:
 peer:
   secret:
     name: peering-token-dc1-to-dc2
     key: data
     backend: kubernetes" | kubectl --context dc2 apply --namespace consul -f -
```
Create a unique peering token for each pair of peered clusters.

#### Connecting services

For services to access other services in a peered cluster, export the service from one cluster to another:

```
echo "apiVersion: consul.hashicorp.com/v1alpha1
kind: ExportedServices
metadata:
 name: default
spec:
 services:
   - name: application
     consumers:
     - peer: dc1" | kubectl --context dc2 apply -f -
```
Add an intention to allow a service in the peered cluster (dc1) to access the service in the target cluster (dc2):

```
echo “apiVersion: consul.hashicorp.com/v1alpha1
kind: ServiceIntentions
metadata:
 name: application-deny
spec:
 destination:
   name: application
 sources:
  - name: *
    action: deny
  - name: web
    action: allow
    peer: dc1" | kubectl --context dc2 apply -f -
```
#### Next steps for Consul cluster peering

Once you set up a local testing environment for cluster peering, you can run integration tests for services that need to connect across multiple Consul datacenters and Kubernetes clusters. For a fully automated local testing setup, check out [my repository](https://github.com/joatmon08/consul-minikubes) to configure Minikube and Consul across three clusters. Learn more about deploying in our [cluster peering for Kubernetes r documentation](https://developer.hashicorp.com/consul/docs/k8s/connect/cluster-peering/tech-specs) and deploy an example to Kubernetes clusters on a cloud provider with our tutorial: [Connect services between Consul datacenters with cluster peering](https://developer.hashicorp.com/consul/tutorials/developer-mesh/cluster-peering).
