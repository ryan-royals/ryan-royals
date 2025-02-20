---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/best-practices-for-avoiding-cloud-security-and-compliance-costs/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.datocms-assets.com/2885/1599960918-blog-library-abstract-00038.jpg?w=1200&h=630&fit=crop&auto=format)

Compliance costs –– the total costs an organization incurs to comply with industry regulations and standards –– are on the rise, and so are the costs of failing to do so. 

* In highly regulated industries such as financial services, Deloitte estimates that compliance-related operating costs at retail and corporate banks [increased 60%](https://www2.deloitte.com/us/en/pages/regulatory/articles/cost-of-compliance-regulatory-productivity.html) over the past decade.
* [Recent SEC regulations](https://www.sec.gov/newsroom/press-releases/2023-139) on cybersecurity risk and incident disclosures have put an increased focus on proactive risk mitigation and efficient incident response procedures
* On a broader scale, the Cato Institute found that the average US firm spends between [1.3% and 3.3%](https://www.cato.org/research-briefs-economic-policy/cost-regulatory-compliance-united-states) of its total wage bill on regulatory compliance.
* Specific to data protection regulations, The Ponemon Institute calculates that the average cost for organizations that experience non-compliance problems is [$14.82 million](https://static.fortra.com/globalscape/pdfs/guides/gs-true-cost-of-compliance-data-protection-regulations-gd.pdf), a 45% increase from 2011.

In this blog, we’ll focus on three key areas IT operations, security, and compliance need to focus on in order to not just mitigate risk, but avoid some risks altogether.

#### Shifting from risk mitigation to risk avoidance

Building out strategies that mitigate infrastructure management risks can help reduce the occurrences of breach and compliance costs, but a strategy that works to avoid as many risks as possible altogether will eliminate costs even further. According to [Gartner](https://www.gartner.com/en/newsroom/press-releases/2024-02-22-gartner-identifies-top-cybersecurity-trends-for-2024), this risk avoidance will come in the form of improved developer experience:

“Security leaders recognize that shifting focus from increasing awareness to fostering behavioral change will help reduce cybersecurity risks. By 2027, 50% of large enterprise CISOs will have adopted ***human-centric security design practices*** to minimize cybersecurity-induced friction and maximize control adoption.” [Emphasis added.]

Human-centric security design means that your security strategies are designed around human psychology and typical behaviors among the users working in your organization’s IT environment.

So avoiding common human pitfalls such as bad manual password management practices or relying on user memory to choose the right settings when provisioning infrastructure, eliminating any of those risky processes constitutes an instance where we’re avoiding risk rather than mitigating it. 

#### Best-practice capabilities for risk avoidance in cloud infrastructure

Focus on developing predefined workflows that are secure and compliant by default. Bake security best practices and compliance requirements into developer workflows. Security teams can help define these workflows so they can rest assured that developers are following protocol.

Then developers can also rest assured that they’re following best practices and can develop freely within company-standard workflows. Unlocking developer autonomy through these standard workflows results in a faster time-to-market for product features, which benefits everyone at the business. Enforcing the proliferation of standardized workflows is the responsibility of platform and cybersecurity teams\*. \*To build security and compliance directly into developer workflows, platform and security teams should focus on a few key capabilities and components: 

##### Golden images, modules, and workflows

Platform teams should leverage infrastructure as code to develop “golden” machine images, infrastructure modules, and deployment workflows. What do we mean by “golden”? It means that the experts on your platform, security, and compliance teams have developed a ‘gold’ standard template for infrastructure and its deployment that developers can choose from an internal registry and start building safely. These company-standard images and modules contain the most up-to-date… 

* System packages
* Logging and monitoring tools
* Security patches
* Configuration hardening

And anything else your operations teams deem necessary. 

Another key practice in risk avoidance is having golden workflows. The first part of golden workflows is [policy as code](https://developer.hashicorp.com/sentinel/docs/concepts/policy-as-code). Like infrastructure as code, these policies are codified, versioned, and auditable. They allow teams to create soft or hard gates around certain actions during deployment. 

For example, if a developer is deploying new modules, or working outside the golden image library, a policy written to detect compliance violations in their infrastructure deployment would automatically scan and catch that issue before it becomes a breach. This allows for deeper checks and an extra layer of security that fills in any gaps in the golden image/module process. 

Once policies and golden templates are established, platform teams can build a management layer on top of these to give developers deployment templates that don’t require them to know anything about the configuration or policy systems that need to be triggered. This last abstraction layer is the final step in building an [internal developer platform (IDP)](https://www.youtube.com/watch?v=2Nrlkn-km5A).

By building out these standardized reusable components and workflows to create a golden path, you no longer have to choose between speed or security risks. This guardrailed software delivery approach reduces risk *and* accelerates developer productivity by removing the manual cloud deployment tasks that so often lead to breaches in security and compliance.

##### Lifecycle management

As organizations mature in their centralized IDP adoption, they need to take a lifecycle-management approach to the golden components that the development teams use. That means having efficient and effective processes for the creation, testing, deployment, updating, and removal of standardized modules, policies, and images.

Your platform will need to have UIs and dashboards that provide centralized visibility and controls for all of these things. Teams will want a fast way to generate tests to see if new modules, policies, and images will work the way they’re intended. They’ll need live lists of image and module versions so developers can know if they’re using an older standard image or a newer one. And security and compliance teams will want controls to instantly deprecate unused or vulnerable cloud modules that might pose a security risk or higher cost.

With full-lifecycle management controls and visibility, security risks are quickly detected and removed while costs are kept low.

##### Integrated secrets management

Maintaining the compliance and security posture of cloud resources depends on IT organizations’ ability to secure credentials, keys, and other secrets. Stolen credentials are the number one way threat actors breach organizations, according to the [Verizon Data Breach Investigations Report (DBIR)](https://www.verizon.com/business/resources/reports/dbir/). Integrated secrets management capabilities deliver [identity-based security](https://www.hashicorp.com/resources/why-should-we-use-identity-based-security-as-we-ado) to automatically authenticate and authorize access to secrets and other sensitive data. This allows IT organizations to:

* Automatically scan across cloud resources and developer repositories to identify exposed secrets and prioritize the remediation of exposed secrets and unmanaged secrets.
* Block unauthorized users by authenticating access based on trusted identities. Short-lived, just-in-time credentials that expire automatically help to reduce [secret sprawl](https://www.hashicorp.com/resources/what-is-secret-sprawl-why-is-it-harmful) across the organization.
* Shift to automatic secrets rotation or [dynamic secrets](https://www.hashicorp.com/blog/why-we-need-dynamic-secrets) to eliminate slow and risky manual secrets rotation with end-to-end secrets management.

For more tips on secrets management, read about our [5 best practices for secrets management](https://www.hashicorp.com/resources/5-best-practices-for-secrets-management).

#### The benefits of risk avoidance

Because they are constantly changing and growing, enterprise cloud environments are breeding grounds for all manner of technology and business risks. By establishing best practices for compliance and cybersecurity policies from the beginning and throughout the infrastructure lifecycle, IT organizations can provide application development environments that are secure by default. With compliance and cybersecurity guardrails in place, developers can focus on speeding up their delivery of innovative applications to market. 

To learn more about how best practices in security and infrastructure lifecycle management can help avoid compliance and cybersecurity risks, [watch our webinar series on risk management](https://www.hashicorp.com/campaign/slm-webinar-series) and follow HashiCorp on [LinkedIn](https://www.linkedin.com/company/hashicorp/).
