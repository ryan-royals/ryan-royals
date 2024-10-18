---
{"dg-publish":true,"permalink":"/40-references/readwise/terraform-1-8-provider-functions-for-aws-google-cloud-and-kubernetes/","tags":["rw/articles"]}
---

![40 References/attachments/b8b4cd65207667b50c9858f2b9618976_MD5.jpg](/img/user/40%20References/attachments/b8b4cd65207667b50c9858f2b9618976_MD5.jpg)
  
URL: https://www.hashicorp.com/blog/terraform-1-8-adds-provider-functions-for-aws-google-cloud-and-kubernetes
Author: Aurora Chun

## Summary

Provider-defined functions are now available in AWS, Google Cloud, and Kubernetes providers with Terraform 1.8. These custom functions enhance Terraform's capabilities and simplify complex tasks like ARN manipulation and Kubernetes manifest decoding. Users can now easily extend Terraform configurations using these new functions for diverse tasks.

## Highlights added August 30, 2024 at 2:23 PM
>To access a provider-defined function, reference the `provider::` namespace with the local name of the Terraform Provider. For example, you can use the `direxists` function by including `provider::local::direxists()` in your Terraform configuration. ([View Highlight] (https://read.readwise.io/read/01hv544brw8rew2wjg508bwz0j))


>The Google Cloud provider also includes a new `region_from_zone` provider-defined function that helps obtain region names from a given zone (e.g. “us-west1” from “us-west1-a”). This simple string processing could be achieved in multiple ways using Terraform’s built-in functions previously, but the new function simplifies the process:
>locals {
>zone = “us-central1-a”
># ways to derive the region “us-central1” using built-in functions
>region_1 = join("-", slice(split("-", local.zone), 0, 2))
>region_2 = substr(local.zone, 0, length(local.zone)-2)
># our new region_from_zone function makes this easier!
>region_3 = provider::google::region_from_zone(local.zone)
>} ([View Highlight] (https://read.readwise.io/read/01hv544p54nqn66x34b9wsq8hx))


