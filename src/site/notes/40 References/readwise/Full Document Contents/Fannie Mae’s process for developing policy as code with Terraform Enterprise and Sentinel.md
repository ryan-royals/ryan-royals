---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/fannie-mae-s-process-for-developing-policy-as-code-with-terraform-enterprise-and-sentinel/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.datocms-assets.com/2885/1723498229-ilm.png?w=1200&h=630&fit=crop&auto=format)

The Federal National Mortgage Association (FNMA), commonly known as Fannie Mae, is the largest company in the United States and the fifth largest company in the world, by assets. As a government-sponsored enterprise, they are subject to a large number of IT security and compliance regulations. 

Rather than getting bogged down in an ever-evolving regulatory landscape, Fannie Mae is accelerating operations with IT infrastructure lifecycle management products like [Terraform Enterprise](https://www.hashicorp.com/products/terraform). Specifically, they’re automating large-scale cloud infrastructure provisioning while also mitigating security and compliance risks with [policy as code](https://developer.hashicorp.com/sentinel/docs/concepts/policy-as-code), which is supported by Terraform’s [Sentinel framework](https://www.hashicorp.com/sentinel).

This post is based off of the HashiConf session, [Sentinel policy as code in a highly regulated financial industry](https://www.youtube.com/watch?v=PJzosAEmCWk) by Maksim Frenkel, to serve as a guide for your organization to learn from Fannie Mae’s policy as code journey and build your own policy development strategy for risk reduction.

#### Terraform and Sentinel at Fannie Mae

Terraform Enterprise has become an integral part of Fannie Mae's digital transformation journey. Their IT environment includes:

* 700+ active Terraform workspaces
* 80+ AWS services
* 450+ Sentinel policies

At Fannie Mae, Sentinel policies serve as guardrails, ensuring that AWS services are consumed securely in a regulated environment. Fannie Mae derives its cloud security standards from various compliance and data protection frameworks, such as:

* NIST 800-53 and RMF
* CIS benchmarks
* FIPS 140-2 data protection
* Department of Defense [zero trust](https://www.hashicorp.com/solutions/zero-trust-security)

The integration of these standards into Sentinel policies ensures that development environments meet all compliance requirements before infrastructure is provisioned.

So what benefits does Fannie Mae see in using Sentinel for policy as code?

#### Why Sentinel?

Sentinel policy as code offers several advantages in managing infrastructure compliance:

* **Version control:** Use common Git workflows to edit and manage policies in a well-controlled way. Sentinel policies are tied into Terraform and version control through [policy sets](https://developer.hashicorp.com/terraform/cloud-docs/policy-enforcement/manage-policy-sets).
* **Automated testing:** Version controlling Sentinel policy code also makes it easy to run these policies through common automated testing frameworks and build pipelines. Sentinel also has a [built-in test framework](https://developer.hashicorp.com/sentinel/docs/writing/testing).
* **Embedded in the Terraform workflow:** Sentinel policies run in between the plan and apply phases of infrastructure provisioning, acting as a preventative guardrail and ensuring compliance requirements are met before infrastructure is provisioned.

This proactive approach **minimizes the risk of non-compliance** in production environments, allowing development teams to address compliance issues early in the dev environment testing process, before they promote that infrastructure to production. 

It also shifts more responsibility for compliance *left* toward the developer. Instead of manual compliance or security reviews, developers have guardrails embedded in their Terraform workflows that give immediate feedback if there’s a policy violation.

#### What can policy as code be used for?

You can develop Sentinel policy controls for several categories:

|  |  |
| --- | --- |
| **Category** | **Example** |
| Security
  | Ensure DynamoDB server-side encryption and CMK are enabled
  |
| Logging
  | Ensure Amazon ECS task logging to CloudWatch is enabled
  |
| Architecture
  | Ensure Amazon Load Balancer uses approved subnets and security groups
  |
| Resilience
  | Ensure multi-availability-zone for Amazon RDS is enabled in production 
  |
| FinOps
  | Ensure only approved Amazon EC2 instance types are used
  |

Several compliance policies for industry-standard security benchmarks have been built and shared by partners and the community in the [Terraform Registry](https://registry.terraform.io/browse/policies). A good example is the [CIS benchmarks Sentinel policies](https://github.com/hashicorp/terraform-foundational-policies-library?tab=readme-ov-file#center-for-internet-security-cis).

#### Fannie Mae’s process for building policy as code

Fannie Mae uses a comprehensive process for developing Sentinel policies that platform teams at many organizations could implement. The process consists of five stages:

1. Requirements
2. Development
3. Testing
4. Review
5. Release

##### Requirements

For the first step, Fannie Mae recommends designating a cross-sectional group of stakeholders including a representative from platform, security, compliance, app development, and any other relevant department such as FinOps. Once the group of stakeholders is in place, they can start reviewing requirements specifications for any new Sentinel policies. 

When someone wants to propose a policy at Fannie Mae, the first thing they’ll typically do is go to the specific [Terraform provider](https://developer.hashicorp.com/terraform/language/providers) documentation in the [Terraform Registry](https://registry.terraform.io/) for the infrastructure component they want to build a policy for. The screenshot below shows what things you would want to research in the documentation. In this example, the team wants to make a policy for Amazon DynamoDB provisioning.

![Terraform](https://www.datocms-assets.com/2885/1736188612-tf-reg-items.png)Use this documentation to create a granular Sentinel policy specification. Fannie Mae includes five sections in each specification: Resource type, attributes, allowed values, and enforcement level. Your own specifications could add more custom areas but the example specification below uses just Fannie Mae’s five sections (filled in with content for a DynamoDB policy):

###### Resource type

`aws_dynamodb_table`

###### Attributes

`server_side_encryption.enabled`  

`server_side_encryption.kms_key_arn`

(These force server-side encryption to be enabled and used on the KMS key)

###### Allowed values

Enabled with [SSM](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) parameter value.  

`//standard/kms\_key\_arn`  

(This ensures the KMS key is set to an allowed value. In this example, it has to come from an approved SSM parameter that holds the KMS key)

###### Enforcement level

Hard mandatory.  
(See [Sentinel’s three levels of enforcement](https://developer.hashicorp.com/sentinel/docs/concepts/enforcement-levels). Hard mandatory means that provisioning is blocked until all requirements in the policy are met.)

You’ll want the stakeholders and subject matter experts to review and provide feedback on the policy requirements specification before moving on to the next stage.

##### Development

Fannie Mae uses a standard feature branch methodology when building their Sentinel policies: 

1. Start with a feature branch for each policy or any change to a policy set.
2. When finished with the changes, merge the feature branch back into the release branch where Sentinel will get policies from.

This segment of Fannie Mae’s talk takes you through policy syntax in four areas:

* Imports
* Resources
* Functions
* Rules

##### Testing

After building a policy, you need to make sure it actually works. Fannie Mae defines test cases that they want to cover with a given policy. In what situations does it pass? In what situations does it fail? The next embedded segment of Fannie Mae’s talk shows how you generate [Sentinel policy tests](https://developer.hashicorp.com/terraform/tutorials/policy/sentinel-testing) to validate those test cases.

There are two utilities in Sentinel that help with test generation:

* [Sentinel mocks](https://developer.hashicorp.com/terraform/cloud-docs/policy-enforcement/test-sentinel): Exported data from a Terraform plan to mimic real-world conditions
* [Sentinel CLI](https://developer.hashicorp.com/sentinel/docs/commands): A utility to evaluate Sentinel policies against mock data

Having a test suite built for your policies becomes even more important as time goes on because policies become harder to maintain if you don’t have ways of validating that they still result in secure, compliant provisioning even after you modify them.

##### Review

Fannie Mae has two levels of policy code review:

* Peer review
* Information security review

The review phase also puts the tests built in the previous phase into action. This segment of Fannie Mae’s talk takes you through their review and testing pipeline:

A key way that Fannie Mae reduces risk in this phase is by testing each test case for every policy every time. The reason for this is — if a file or function shared by multiple policies was changed, it could affect more policies than the one currently being worked on.

##### Release

The last step is to merge the feature branch for the policy back into the release branch of the policy set. This final segment of Fannie Mae’s talk takes you through their release process and shows you how Sentinel guardrails look to developers using Terraform in their day-to-day work:

#### Lessons learned

After a multi-year journey adopting policy as code in [Terraform Enterprise](https://developer.hashicorp.com/terraform/enterprise), Fannie Mae pointed out several key areas for other adopters to focus on:

##### Fine tune requirements

Requirements gathering is the most important phase. All stakeholders should be clear and precise about what components are going into each policy and how they will reduce compliance and security risks without being a hindrance for developers.

##### Think about performance

As you scale up your policies, you’ll want to start collecting performance and debugging metrics while also using mocks to performance test your policies. Why is this important? If certain validations become too large or inefficient, it can take several minutes for policies to complete instead of a few seconds.

##### Reuse code

Reuse functions throughout your policies to save time and propagate policy coding best practices.

##### Consider backward compatibility

New policies should usually start at the advisory enforcement level and then become hard mandatory when enough infrastructure deployments are passing the policy checks. **Starting with hard mandatory may block all of your developers** because when they re-provision pieces of infrastructure written before the policy was in place, these foundational pieces may not be able to run because of the new policy.

#### Next steps

* To try writing and running some of your own Sentinel policy code, visit our free [Sentinel playground site](https://play.sentinelproject.io/).
* For more information on Sentinel, visit our [documentation](https://developer.hashicorp.com/sentinel/docs).
* Find pre-written and example policies on the [Terraform Registry](https://registry.terraform.io/browse/policies) and [this HashiCorp GitHub repo](https://github.com/hashicorp/terraform-sentinel-policies). HashiCorp and AWS recently worked together on [new pre-written CIS benchmarking policy sets for AWS services](https://registry.terraform.io/search/policies?q=CIS).
* To test Sentinel in your Terraform workflows, sign up for a free trial of [HCP Terraform](https://www.hashicorp.com/products/terraform).
