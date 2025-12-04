---
{"dg-publish":true,"dg-path":"Slipbox Notes/Terraform Cloud Development Kit.md","permalink":"/slipbox-notes/terraform-cloud-development-kit/","tags":["notes"],"created":"2023-06-26","updated":"2025-11-28"}
---


Terraform Cloud Development Kit is a tool used to abstract from Terraform, and allow the writing of TF using TypeScript, Python, Java, C# and Go. TypeScript is the language of choice at this time.  
 ![f36932751a5f5d5146af0d5cb97173c7_MD5.jpg](/img/user/10_attachments/f36932751a5f5d5146af0d5cb97173c7_MD5.jpg)  
This allows for the Application code to manage the complexity of Terraform, where Terraform sometimes struggles with loops and abstractions.

At a high level, the workflow is:

1. **Create an Application:** Use either a built-in or a custom template to scaffold a project in your chosen language.
2. **Define Infrastructure:** Use your chosen language to define the infrastructure you want to provision on one or more providers. CDKTF automatically extracts the schema from Terraform providers and modules to generate the necessary classes for your application.
3. **Deploy**: Use `cdktf` CLI commands to provision infrastructure with Terraform or synthesize your code into a JSON configuration file that others can use with Terraform directly.

## Current Impressions

Current impressions are that this tool, although very cool, is not too useful for us right now. Terraform holds strength in being 'Infrastructure as Text', with both programmers and non-programmers able to learn the language with minimal issue. This layer of abstraction offers more power, but also could complicate what could otherwise be simple.
