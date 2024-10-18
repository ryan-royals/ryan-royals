---
{"dg-publish":true,"permalink":"/40-references/readwise/what-is-azure-dns-private-resolver/","tags":["rw/articles"]}
---

![40 References/attachments/aed272417ab44a26e6bdcceab03aeb5f_MD5.jpg](/img/user/40%20References/attachments/aed272417ab44a26e6bdcceab03aeb5f_MD5.jpg)
  
URL: https://learn.microsoft.com/en-us/azure/dns/dns-private-resolver-overview
Author: greg-lindsay

## Summary

In this article, get started with an overview of the Azure DNS Private Resolver service.

## Highlights added August 30, 2024 at 2:23 PM
>Azure DNS Private Resolver is a new service that enables you to query Azure DNS private zones from an on-premises environment and vice versa without deploying VM based DNS servers. ([View Highlight] (https://read.readwise.io/read/01gz4y000d6b1q4q7q0ma5esyn))


>ully managed: Built-in high availability, zone redundancy ([View Highlight] (https://read.readwise.io/read/01gz4y0wcn515dqtcfn5nnew62))


>Cost reduction: Reduce operating costs and run at a fraction of the price of traditional IaaS solutions. ([View Highlight] (https://read.readwise.io/read/01gz4y13yw982vegxpwasqpwwk))


>Private access to your Private DNS zones: Conditionally forward to and from on-premises. ([View Highlight] (https://read.readwise.io/read/01gz4y1jsv5m2zzm4b5rhpfxwx))


>Scalability: High performance per endpoint. ([View Highlight] (https://read.readwise.io/read/01gz4y1p07ds13kx7q38wxjrt6))


>DevOps Friendly: Build your pipelines with Terraform, ARM, or Bicep. ([View Highlight] (https://read.readwise.io/read/01gz4y1vvxef1fw4ypk8zmncdv))


>The inbound endpoint requires a subnet in the VNet where it’s provisioned. The subnet can only be delegated to **Microsoft.Network/dnsResolvers** ([View Highlight] (https://read.readwise.io/read/01gz4y2d6vwxgyq58ms518nmg3))


>A DNS forwarding rule includes one or more target DNS servers that are used for conditional forwarding, and is represented by:
>• A domain name
>• A target IP address
>• A target Port and Protocol (UDP or TCP) ([View Highlight] (https://read.readwise.io/read/01gz4y7c0g0vp4vswyabzvcjxf))


>A DNS resolver can only reference a virtual network in the same region as the DNS resolver. ([View Highlight] (https://read.readwise.io/read/01gz4y7n83rvqp5enyzs7wgwy5))


>virtual network can't be shared between multiple DNS resolvers. A single virtual network can only be referenced by a single DNS resolver. ([View Highlight] (https://read.readwise.io/read/01gz4y32x9h47j47wbvn4zt9my))


>The following IP address space is reserved and can't be used for the DNS resolver service: 10.0.1.0 - 10.0.16.255. ([View Highlight] (https://read.readwise.io/read/01gz4y4bneeb0m3y5jt3zex4vj))


>A subnet must be a minimum of /28 address space or a maximum of /24 address space. ([View Highlight] (https://read.readwise.io/read/01gz4y4hvb5xxdn9xn3r33wjy0))


>A subnet can't be shared between multiple DNS resolver endpoints. A single subnet can only be used by a single DNS resolver endpoint ([View Highlight] (https://read.readwise.io/read/01gz4y4s77t8b0xnbgs08szknm))


>All IP configurations for a DNS resolver inbound endpoint must reference the same subnet. Spanning multiple subnets in the IP configuration for a single DNS resolver inbound endpoint isn't allowed. ([View Highlight] (https://read.readwise.io/read/01gz4y5f2bpjka5aj6k9smwz10))


>The subnet used for a DNS resolver inbound endpoint must be within the virtual network referenced by the parent DNS resolver ([View Highlight] (https://read.readwise.io/read/01gz4y6x3t2wrcnfg15kgevx7d))


>An outbound endpoint can't be deleted unless the DNS forwarding ruleset and the virtual network links under it are deleted. ([View Highlight] (https://read.readwise.io/read/01gz4y5yvxgvdzar3wdawkg5pp))


>Rulesets can have up to 1000 rules. ([View Highlight] (https://read.readwise.io/read/01gz4y63k7s0wcyc0e9gpjagjy))


>IPv6 enabled subnets aren't supported. ([View Highlight] (https://read.readwise.io/read/01gz4y6d7ek1dxngfewmdh5a9y))


>DNS private resolver does not support Azure ExpressRoute FastPath ([View Highlight] (https://read.readwise.io/read/01gz4y6q16dnzfenhme8tfh1ms))


