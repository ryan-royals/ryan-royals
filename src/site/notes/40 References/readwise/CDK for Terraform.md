---
{"dg-publish":true,"permalink":"/40-references/readwise/cdk-for-terraform/","tags":["rw/articles"]}
---

# CDK for Terraform

![rw-book-cover](https://developer.hashicorp.com/og-image/terraform.jpg)
  
URL: https://developer.hashicorp.com/terraform/cdktf
Author: CDK for Terraform | Terraform | HashiCorp Developer

## Summary

Cloud Development Kit for Terraform (CDKTF) lets you use familiar programming languages to define and provision infrastructure.

## Highlights added July 17, 2024 at 10:55 AM
>Cloud Development Kit for Terraform (CDKTF) lets you use familiar programming languages to define and provision infrastructure ([View Highlight] (https://read.readwise.io/read/01h3e7kws5yn9yds704yhj0jmw))


>This gives you access to the entire Terraform ecosystem without learning HashiCorp Configuration Language (HCL) and lets you leverage the power of your existing toolchain for testing, dependency management, etc ([View Highlight] (https://read.readwise.io/read/01h3e7mh1bnte5syg2xss0yqac))


>We support TypeScript, Python, Java, C#, and Go. ([View Highlight] (https://read.readwise.io/read/01h3e7mms5dk5dp16h3dfr9cy6))


>![](https://developer.hashicorp.com/_next/image?url=https%3A%2F%2Fcontent.hashicorp.com%2Fapi%2Fassets%3Fproduct%3Dterraform-cdk%26version%3Drefs%252Fheads%252Fstable-website%26asset%3Dwebsite%252Fdocs%252Fcdktf%252Fterraform-platform.png%26width%3D1776%26height%3D1317&w=3840&q=75) ([View Highlight] (https://read.readwise.io/read/01h3e7mqnanpambnp3dxphx5dx))


>At a high level, you will:
>1. **Create an Application:** Use either a built-in or a custom template to scaffold a project in your chosen language.
>2. **Define Infrastructure:** Use your chosen language to define the infrastructure you want to provision on one or more providers. CDKTF automatically extracts the schema from Terraform providers and modules to generate the necessary classes for your application.
>3. **Deploy**: Use `cdktf` CLI commands to provision infrastructure with Terraform or synthesize your code into a JSON configuration file that others can use with Terraform directly. ([View Highlight] (https://read.readwise.io/read/01h3e7p0d256dhy26hn51hph4q))


>You have a strong preference or need to use a procedural language to define infrastructure. ([View Highlight] (https://read.readwise.io/read/01h3e7ps1vbrcscf7d4yvb1bt8))


>You need to create abstractions to help manage complexity. For example, you want to create constructs to model a reusable infrastructure pattern composed of multiple resources and convenience methods. ([View Highlight] (https://read.readwise.io/read/01h3e7pytrcwrhxdy21g6wky26))


>You are comfortable living on the cutting edge; CDKTF may still have breaking changes before our 1.0 release. ([View Highlight] (https://read.readwise.io/read/01h3e7q1wwk16vq4dm3m1et47b))


>If you plan to create and package your own constructs, we recommend choosing TypeScript. Using TypeScript allows you to use the [cdktf constructs](https://github.com/projen/projen#getting-started) package generator to build and publish your constructs in multiple languages. ([View Highlight] (https://read.readwise.io/read/01h3e7qbx0888720gc22z06ebe))


