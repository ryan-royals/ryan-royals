---
{"dg-publish":true,"dg-path":"Azure Verified Modules FAQ.md","permalink":"/azure-verified-modules-faq/","tags":["notes"]}
---


## What Are Azure Verified Modules

**Azure Verified Modules** is a initiative led by Microsoft to have pre constructed, consistently shaped Modules for deploying resources to Azure. These Modules are available publicly and are designed for community collaboration and development, but have dedicated ownership from Microsoft staff to hold accountability for code quality, testing, and maintenance concerns.

## Why Use Azure Verified Modules

**Azure Verified Modules** are designed to accelerate deployment of *resources* and *patterns* to Azure by having standardized inputs and outputs, and having *Well Architected Framework* best practises backed into each resource. This helps alleviate some of the responsibility from customers consuming Azure that would otherwise require a large amount of understanding to know of, and conform to these best practises.

## What Infrastructure as Code Languages Does Azure Verified Modules Use

Both Terraform and Bicep are supported languages for the **AVM**.

## What Types of Modules Are there

**AVM** has 3 types of modules.  
**Resource** modules are used to deliver a specific Azure resource (Like Key vault), with *Well Architected Framework* practises baked in and enabled by default (Such as no public access).  
**Pattern** modules are a collection of **Resource** modules designed to deploy a workload, such as the module *avm-ptn-aks-production*, which deploys AKS, Virtual Network and a Container Registry.  
**Utility** modules do not deploy resources, but are used to add capability to other modules, such as *avm-utl-regions*, which is a module that handles lookup and maintenance of a list of Azure Regions, and their region names, zones available, geography, and other meta data.
