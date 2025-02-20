---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/7-ways-to-optimize-cloud-spend-with-terraform/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.datocms-assets.com/2885/1714778525-terraform-cost-optimization.png?w=1200&h=630&fit=crop&auto=format)

The statistics are clear: Nearly every IT organization is overspending on cloud. For example, 94% of respondents to the [2023 HashiCorp State of Cloud Strategy Survey](https://www.hashicorp.com/state-of-the-cloud#:%7E:text=94%25%20are%20still%20wasting%20money%20in%20the%20cloud) experienced some form of avoidable cloud costs (aka “cloud waste”). [S&P Global](https://www.spglobal.com/marketintelligence/en/documents/enterprises-are-missing-out-on-24b-by-not-optimizing-cloud-spending-not-going-multicloud.pdf) estimates there is $24 billion in untapped cloud savings annually across the enterprises they surveyed. And the [Cloud Native Computing Foundation’s latest survey on cloud native FinOps and cloud financial management](https://www.infoq.com/news/2024/03/cncf-finops-kubernetes-overspend/) found that 70% of respondents are losing money from overprovisioning while 43% are failing to deactivate idle resources after they’ve been used.

There’s no mystery around why this is happening. Operators know that the most common sources of cloud waste are:

* Overprovisioned resources
* Idle or underused resources

Yet companies still struggle to address these sources with the right skills, tools, and processes.

This post looks at why cloud waste is so tough to control and explores seven [HashiCorp Terraform](https://www.hashicorp.com/products/terraform) capabilities that can help mitigate them.

*For a comprehensive look at cloud and operational cost savings strategies at each level of cloud adoption maturity, read our white paper:*

#### Cloud waste: Where does it come from?

Why are so many companies spending more on cloud resources than they need to? It often comes down to inexperience, reliability concerns, a lack of tracking, and insufficient processes and guardrails.

##### Inexperience and reliability concerns

Early in a cloud migration, developers are often given a lot of leeway to buy the cloud infrastructure they think they need. When infrastructure first moves to the cloud, there’s no longer an ops team or sysadmin to stop developers from clicking a few buttons, entering a company credit card, and provisioning 50 cloud compute instances. Developers can easily make errors when manually entering infrastructure parameters for every deployment — provisioning 21 instances instead of 12, for example. 

While overprovisioning is often unintentional, some developers prefer to overprovision infrastructure so that they don’t unexpectedly run out of compute and cause application outages. Similarly, teams may buy cloud services with more features and capabilities than they really need. These types of overprovisioning may be due to fear and a lack of clarity around cost vs. reliability tradeoffs, but simple inexperience also plays a part.

According to the HashiCorp State of Cloud Strategy Survey, [90% of organizations face gaps in their cloud-related skill sets](https://www.hashicorp.com/blog/unpacking-the-2023-hashicorp-state-of-cloud-strategy-survey-video), and that was a primary cause of cloud waste for 43% of respondents. While senior developers and experienced operations/platform engineers may know how to right-size cloud resources, they may not have an automated way to propagate their knowledge and best practices to junior developers and others across the organization.

##### Lack of tracking and process

With many teams working on different projects, it’s not uncommon for organizations to simply lose track of non-production infrastructure that’s still incurring costs. Developers and sales engineers often create demo or sandbox environments but forget to decommission them when they are no longer needed. 

Without tracking or tools to clean up non-production resources automatically, the organization may not even know what it’s spending money on. Team members may have to expend effort just to track down and gather context on all of these resources when managers finally start to notice the waste. 

#### How Terraform helps

If your entire organization hasn’t yet adopted infrastructure as code through Terraform, doing so is a high-ROI first step that will organically reduce cloud-management costs. [Migrating to Terraform](https://www.youtube.com/watch?v=gjeyz5kIO1U&t=41s) brings a level of standardization and core stability to cloud infrastructure usage that:

* Increases productivity by eliminating inefficient manual processes
* Reduces security risks and the risk of human error
* Increases infrastructure visibility and architectural clarity

South African banking group Nedbank, for example, was able to complete projects at [25% lower resource costs](https://www.hashicorp.com/case-studies/nedbank), deploying more than 1,000 virtual machines a month using the HCP Terraform pipeline.

![HCP](https://www.datocms-assets.com/2885/1714778624-hcp-terraform-workflow.png)Terraform provides features to help teams manage costs, enforce policies, and increase productivity throughout the cloud adoption process. Here are some key features Terraform offers for optimizing cloud spend:

##### 1. Modules

Terraform modules allow you to templatize and reuse common, org-approved Terraform configurations to reduce code duplication and standardize organizational requirements and best practices. HCP Terraform and Terraform Enterprise include a built-in [private registry](https://developer.hashicorp.com/terraform/registry/private), allowing platform teams to test and publish modules for easy discovery and self-service consumption by downstream teams. 

Using Terraform’s private registry as a central, org-wide internal infrastructure repository lets engineering teams from across the organization pool their best infrastructure practices into one platform as code, eliminating large swaths of unnecessary work by separate teams trying to write configurations that have already been created elsewhere in the organization. And by encouraging developers to use “golden” modules approved by the security, operations, governance, and platform teams, with security and operational best practices baked in, organizations not only limit errors and security risks, they also reduce costs because cost-efficient infrastructure choices are also baked in.

These golden modules help less experienced developers use the cost-efficient infrastructure resources that senior engineers and architects have selected for their most common use cases.

##### 2. No-code provisioning

HCP Terraform and Terraform Enterprise further simplify the golden module workflow with a feature called [no-code provisioning](https://developer.hashicorp.com/terraform/tutorials/cloud/no-code-provisioning).

No-code provisioning gives platform teams a process for building fully push-button, self-service provisioning workflows that application developers and even non-technical stakeholders can use. No knowledge of Terraform, HashiCorp Configuration Language ([HCL](https://github.com/hashicorp/hcl)), or the command line is required. Users of no-code workspaces and modules don’t need to manage Terraform configurations or directly use version control systems. They simply select no-code modules from a menu and with a few clicks, they have secure, cost-optimized infrastructure crafted by the experts on their organization’s platform team.

These simplified no-code workflows empower more people within an organization to cost-efficiently self-serve their deployments, which also saves time for platform teams since they can delegate provisioning tasks to more users without having to step in and help.

##### 3. Automated policy guardrails

Even with golden modules, code reviews are needed in the provisioning process because errors can still creep in and security holes can open up. Organizations may also want to enforce cost-control policies and reliability best practices that can’t be contained in modules.

Manual policy checks become productivity bottlenecks, demanding an approver’s time and energy. That’s why automating as much of the approval criteria as possible is imperative for controlling time costs and optimizing cloud costs.

HCP Terraform and Terraform Enterprise let platform teams compose and manage automation for those policy checks with [HashiCorp Sentinel](https://www.hashicorp.com/sentinel) and Open Policy Agent (OPA). Sentinel and OPA are [policy as code](https://developer.hashicorp.com/sentinel/docs/concepts/policy-as-code) frameworks that enable platform teams to write policy rule automations as customizable and auditable code. And just as infrastructure as code allows configuration sharing among industry experts, high-quality policy as code libraries are also free and discoverable in the [public Terraform Registry](https://registry.terraform.io/browse/policies). 

Sentinel policies can put guardrails around security and compliance, but they can also be used to control cloud costs by limiting the types and size of compute and storage resources, or by limiting the cloud services and regions that can be provisioned. 

For illustration, imagine a golden module with an input variable for the number of instances to provision. Even though the module will build the resources according to the platform team’s security and cost specifications, the user-entered data won’t always be controllable. If a user accidentally enters 200 instances for provisioning instead of 20, the module might not stop that action, but an automatic policy check can. It’s not hard to see how policy checks can make a big difference in optimizing cloud costs.

##### 4. Run tasks

HCP Terraform and Terraform Enterprise also contain deep policy automation integrations with many popular testing and scanning tools. These integrations are called *[run tasks](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/settings/run-tasks)* and they are built in collaboration with partner tool vendors. 

Using run tasks in addition to Sentinel or OPA policies, organizations can harness third-party cloud cost optimization products in their provisioning pipelines, such as Infracost, Kion, and Bridgecrew. For a full list of Terraform run task integrations, visit the [Terraform Registry](https://registry.terraform.io/browse/run-tasks).

Together, modules, policies, and run tasks help organizations bake security and budget compliance into their provisioning pipelines by default, with little to no human intervention required. But what about Day 2?

##### 5. Drift detection

Even with a secure, compliant initial provisioning process, changes may occur outside of the normal workflow. These might include changes made directly through the cloud console, emergency actions taken during an outage, or even changes in Terraform provider defaults. These out-of-band changes can cause [configuration drift](https://www.hashicorp.com/resources/how-can-i-prevent-configuration-drift), which leads to unexpected behavior and performance issues that can undercut cost management efforts.

Drift detection is a feature of the [health assessments](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/health) system in HCP Terraform and Terraform Enterprise. Terraform drift detection regularly scans for infrastructure drift by comparing the actual state of resources to the last saved state. Proactive notifications help teams catch and track unexpected changes while also identifying potential policy or process issues that need to be addressed. Terraform’s health dashboard also lets users quickly roll back infrastructure that has drifted away from its desired state, preventing unexpected budget overages due to drift.

##### 6. Continuous validation

Approved modules and policy checks are excellent ways to ensure compliance before provisioning, but they can't prevent every issue. Checks are also necessary in production where live infrastructure is running. Terraform’s ongoing health assessments monitor infrastructure immediately after provisioning; Day 2, and beyond.

[Continuous validation](https://www.youtube.com/watch?v=qMNyy-7jW7w) in HCP Terraform and Enterprise provides these ongoing checks to make sure infrastructure is working as expected. Just like approved modules and policy checks, continuous validation can be used to [control budgets and close security gaps](https://www.hashicorp.com/blog/8-terraform-continuous-validation-use-cases-for-aws-google-cloud-and-azure). For example, it could be used to continuously check if a set of infrastructure complies with [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) parameters set by the finance and platform teams. It can also detect certificate expiration and check simple information such as whether a virtual machine (VM) is up and running.

Continuous validation uses custom assertions created by platform teams to trigger notifications that alert infrastructure owners as soon as a check fails. This helps avoid: 

* Budget non-compliance
* Downtime due to expiring certificates
* Security issues from outdated images
* and many more scenarios

##### 7. Ephemeral workspaces

According to the HashiCorp State of Cloud Strategy Survey, half of all respondents [struggle with idle or underused resources](https://www.hashicorp.com/state-of-the-cloud). Lack of expiration dates on temporary cloud resources impacted the bottom line of [39% of organizations](https://www.hashicorp.com/state-of-the-cloud#:%7E:text=LACK%20OF%20EXPIRATION%20DATE%20ON%20TEMPORARY%20CLOUD%20RESOURCES). 

Idle or underutilized resources are big contributors to avoidable cloud spend. Most organizations have few, if any, processes to clean up temporary infrastructure deployments, and many don’t take advantage of the ability to deprovision non-production infrastructure outside of work hours. 

Terraform’s [ephemeral workspaces](https://www.hashicorp.com/blog/terraform-ephemeral-workspaces-public-beta-now-available) let customers automate the destruction of temporary resources at a set time or based on inactivity. Administrators can require ephemeral workspace usage in certain cases to reduce management toil and infrastructure costs by eliminating the need for manual clean-up and simplifying workspace management. 

#### A systematic approach to cloud cost optimization

Reducing cloud waste requires systematic management from Day 0 to Day N. [HCP Terraform](https://www.hashicorp.com/products/terraform) has a comprehensive array of features to stop cloud waste and it's free to try as your organization scales its infrastructure provisioning practices.

For a deeper dive into the topic of cloud and operations cost savings, visit our [cloud cost optimization page](https://www.hashicorp.com/solutions/cloud-cost-optimization) and download the [3 phases of optimizing cloud and operator spend with Terraform](https://www.hashicorp.com/on-demand/3-phases-of-optimizing-cloud-and-operator-spend-with-terraform?utm_source=direct&utm_medium=organic&utm_campaign=blogtest&utm_content=&utm_offer=whitepaper) white paper. 

We’d love to learn about your team’s challenges and discuss how HashiCorp can help your organization optimize cloud spending. [Have a chat](https://www.hashicorp.com/contact) with our sales and solutions engineers.
