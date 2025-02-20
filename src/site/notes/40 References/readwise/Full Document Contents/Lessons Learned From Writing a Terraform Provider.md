---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/lessons-learned-from-writing-a-terraform-provider/","tags":["rw/articles"]}
---

![rw-book-cover](https://miro.medium.com/v2/resize:fit:1200/0*yus1i9iJmzmgapWM)

![](https://miro.medium.com/v2/resize:fit:700/0*yus1i9iJmzmgapWM)Photo by [Dan Cristian Pădureț](https://unsplash.com/@dancristianpaduret?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)
I wanted to build my own Terraform provider for a long time but never had a real chance because of the strong community that built providers for every major service.

However, finally, after a couple of years of waiting, I got a chance to build a provider from scratch. It was a challenging but extremely rewarding experience. In this article, we will explore the lessons learned during the process, sharing insights, tips, and best practices for creating a robust Terraform provider.

But first, let’s start with a problem. We have a small team managing multiple projects. Each person in the team can manage multiple projects and each project has at least one domain. When we receive an email from a customer, we need to be sure that it is going to be forwarded to the right person and this should be managed in a convenient and automated way.

![](https://miro.medium.com/v2/resize:fit:700/1*64ZzQySyonJ6sz2qm_K_SQ.png)
This concept is called email forwarding and we stopped on the service which is called [Forward Email](https://forwardemail.net). Here you can manage a set of domain names and aliases that will define email forward rules. It has a well-documented API and no Terraform provider or even SDK.

This is where my adventure begins.

#### Start with learning from others

There is a lot of documentation and tutorials over the internet on how to start a Terraform provider, however, I believe that it’s impossible to learn everything that you need in a single resource.

As a first step of your learning, I recommend watching a speech called [“Creating a Terraform Provider for just about anything”](https://www.youtube.com/watch?v=noxwUVet5RE) by Eddie Zaneski. It is pretty insightful and entertaining to give you a high-level overview of concepts you need to understand to start digging deeper.

Then, to understand the key concepts, provider lifecycle, and best practices, you can start reading [HashiCorp's official documentation](https://developer.hashicorp.com/terraform/plugin). When you feel ready to get your hands dirty, don’t start from a blank page, it’s better to use the official [Terraform provider template](https://github.com/hashicorp/terraform-provider-scaffolding-framework). Clone it and start designing your provider on top.

With basic knowledge of theory, it is now the best moment to check out open-source Terraform provider projects on GitHub to see how they are used in real-world scenarios. For me, some of the best examples were:

* [ForwardEmail Terraform provider](https://github.com/abagayev/terraform-provider-forwardemail), my small provider covers everything you need to start.
* [Namecheap Terraform Provider](https://github.com/namecheap/terraform-provider-namecheap), which is relatively small and focused on resources related to domain management.
* [DigitalOcean Terraform Provider](https://github.com/digitalocean/terraform-provider-digitalocean) can be a source of best practices since developed by a bigger team and used by many.

#### Think on multiple levels of abstraction

While developing a Terraform provider, you will experience three levels of abstraction that will define the way you develop.

![](https://miro.medium.com/v2/resize:fit:700/1*YIL5oQWS2wsD9uvuAd2B_g.png)
First of all, you need to keep in mind how users will use your provider in their modules. How do we configure a provider? Which resources do we need? Do we need data sources and resource import? Which attributes should be sensitive, have a default value, or be optional?

That business logic should be represented in the Terraform provider code. To deliver the best experience to the users we need to take care of testing, documentation, logging, and error handling.

The last part that should be extracted is the Go client that works with the API of the service you’re integrating with your provider. You may use or contribute to the existing client, or create one from scratch if it never existed before.

#### Adopt acceptance testing

Terraform providers are typically tested using acceptance tests. Unit tests can be used as well, however, unit testing is mostly applied for testing small and isolated pieces like helper methods that support the provider.

Acceptance tests interact with the Terraform that runs pieces of HCL code which is provided as test cases. This interaction includes the full cycle from initializing terraform, to applying and destroying infrastructure for each test case.

![](https://miro.medium.com/v2/resize:fit:700/1*d8g8XCslil1R8_WqeGJDaQ.png)
It also means that during the test resources managed by the provider are going to be created and destroyed in the real world. For each step in this cycle, you can write code that will check if the resources were created, updated, or deleted properly by accessing the API of a service behind the provider you’re developing and testing.

In some cases, HCL code can become a bit complicated because you want to test resource updates or can’t test resources in isolation, so you need to create extra resources. The test case can look like this:

```
 resource "forwardemail_domain" "test" {  
  name = "stark.com"  
 }  
  
 resource "forwardemail_alias" "test" {  
   name   = "tony"  
   domain = forwardemail_domain.test.name  
   
   recipients = ["james@rhodes.com"]  
}
```

In the example, I set up an email redirect from `tony@stark.com` to his best friend `james@rhodes.com`, however, two resources are needed to be created because the alias depends on the domain. So even if you want to test only alias resources, you need to provide all dependencies to run the test.

#### Invest in automation

The combination of Terraform and Go gives you a lot of great automation tools that you can use generously.

Make your CI more robust. Include [Go linters](https://golangci-lint.run/) to help maintain code quality, enforce coding standards, and catch potential issues early in the development process, promoting clean, consistent, and error-free Go code. Run tests on different versions of Terraform, but remember that it will increase computing and resource usage.

Use tools that are free for open-source projects. Use GitHub workflows and enable [code security](https://docs.github.com/code-security) to keep vulnerabilities out of your codebase with CodeQL, Dependabot, and secret scanning. Gain insights into your code’s test coverage with [Codecov](https://codecov.io/), identify untested or under-tested areas, and ensure comprehensive testing.

If you want to publish your provider to Terraform Registry, you probably should provide good documentation, so the community can use your work. If you want to save some time you can use [tfplugindocs](https://github.com/hashicorp/terraform-plugin-docs) to generate and validate plugin documentation.

### Things to remember

* Developing a Terraform provider can be complex, so be patient, persistent, and open to learning from your experiences.
* The approach of running acceptance tests against the real system can be a challenge but will guarantee a code that works.
* Feel stuck? Scroll up and learn from others by exploring the code or talking to the engineers.
* Keep an eye on changes in Terraform and Go best practices by regularly reviewing the official documentation and participating in discussions.

Happy terraforming!
