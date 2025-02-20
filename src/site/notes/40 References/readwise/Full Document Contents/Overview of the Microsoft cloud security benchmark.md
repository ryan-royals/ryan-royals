---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/overview-of-the-microsoft-cloud-security-benchmark/","tags":["rw/articles"]}
---

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_921743/open-graph-image_Z0zqIG2.png)

#### In this article

1. [What's new in Microsoft cloud security benchmark v1](https://learn.microsoft.com/en-us/security/benchmark/azure/overview#whats-new-in-microsoft-cloud-security-benchmark-v1)
2. [Controls](https://learn.microsoft.com/en-us/security/benchmark/azure/overview#controls)
3. [Recommendations in Microsoft cloud security benchmark](https://learn.microsoft.com/en-us/security/benchmark/azure/overview#recommendations-in-microsoft-cloud-security-benchmark)
4. [Download](https://learn.microsoft.com/en-us/security/benchmark/azure/overview#download)
5. [Next steps](https://learn.microsoft.com/en-us/security/benchmark/azure/overview#next-steps)

The Microsoft cloud security benchmark (MCSB) provides prescriptive best practices and recommendations to help improve the security of workloads, data, and services on Azure and your multi-cloud environment. This benchmark focuses on cloud-centric control areas with input from a set of holistic Microsoft and industry security guidance that includes:

* **Cloud Adoption Framework**: Guidance on security, including [strategy, roles and responsibilities](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/organize/cloud-security), [Azure Top 10 Security Best Practices](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/get-started/security#step-1-establish-essential-security-practices), and [reference implementation.](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/enterprise-scale)
* **Azure Well-Architected Framework**: Guidance on [securing your workloads on Azure](https://learn.microsoft.com/en-us/assessments/?mode=pre-assessment&session=local).
* **The Chief Information Security Officer (CISO) Workshop**: [Program guidance and reference strategies to accelerate security modernization using Zero Trust principles](https://learn.microsoft.com/en-us/security/ciso-workshop/the-ciso-workshop).
* **Other industry and cloud service providers security best practice standards and framework**: Examples include the Amazon Web Services (AWS) Well-Architected Framework, Center for Internet Security (CIS) Controls, National Institute of Standards and Technology (NIST), and Payment Card Industry Data Security Standard (PCI-DSS).

#### What's new in Microsoft cloud security benchmark v1

Note

Microsoft cloud security benchmark is the successor of Azure Security Benchmark (ASB), which was rebranded in October 2022.

Google Cloud Platform support in MCSB is now available as a preview feature both in MCSB benchmark guidance and Microsoft Defender for Cloud.

Here's what's new in the Microsoft cloud security benchmark v1:

1. **Comprehensive multi-cloud security framework**: Organizations often have to build an internal security standard to reconcile security controls across multiple cloud platforms to meet security and compliance requirements on each of them. This often requires security teams to repeat the same implementation, monitoring and assessment across the different cloud environments (often for different compliance standards). This creates unnecessary overhead, cost, and effort. To address this concern, we enhanced the ASB to MCSB to help you quickly work with different clouds by:

	* Providing a single control framework to easily meet the security controls across clouds
	* Providing consistent user experience for monitoring and enforcing the multi-cloud security benchmark in Defender for Cloud
	* Staying aligned with Industry Standards (e.g., CIS, NIST, PCI) ![Mapping between ASB and CIS Benchmark](https://learn.microsoft.com/en-us/security/benchmark/media/mcsb-vs-other-frameworks.png)
2. **Automated control monitoring for AWS in Microsoft Defender for Cloud**: You can use Microsoft Defender for Cloud [Regulatory Compliance Dashboard](https://learn.microsoft.com/en-us/azure/defender-for-cloud/update-regulatory-compliance-packages) to monitor your AWS environment against MCSB just like how you monitor your Azure environment. We developed approximately 180 AWS checks for the new AWS security guidance in MCSB, allowing you to monitor your AWS environment and resources in Microsoft Defender for Cloud.

  ![Screenshot of MSCB integration into Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/security/benchmark/media/mcsb-defender-for-cloud.png)
3. **A refresh of the existing Azure guidance and security principles**: We also refreshed some of the existing Azure security guidance and security principles during this update so you can stay current with the latest Azure features and capabilities.

#### Controls

| Control Domains | Description |
| --- | --- |
| [Network security (NS)](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-network-security) | Network Security covers controls to secure and protect networks, including securing virtual networks, establishing private connections, preventing, and mitigating external attacks, and securing DNS. |
| [Identity Management (IM)](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-identity-management) | Identity Management covers controls to establish a secure identity and access controls using identity and access management systems, including the use of single sign-on, strong authentications, managed identities (and service principals) for applications, conditional access, and account anomalies monitoring. |
| [Privileged Access (PA)](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-privileged-access) | Privileged Access covers controls to protect privileged access to your tenant and resources, including a range of controls to protect your administrative model, administrative accounts, and privileged access workstations against deliberate and inadvertent risk. |
| [Data Protection (DP)](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-data-protection) | Data Protection covers control of data protection at rest, in transit, and via authorized access mechanisms, including discover, classify, protect, and monitor sensitive data assets using access control, encryption, key management and certificate management. |
| [Asset Management (AM)](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-asset-management) | Asset Management covers controls to ensure security visibility and governance over your resources, including recommendations on permissions for security personnel, security access to asset inventory, and managing approvals for services and resources (inventory, track, and correct). |
| [Logging and Threat Detection (LT)](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-logging-threat-detection) | Logging and Threat Detection covers controls for detecting threats on cloud, and enabling, collecting, and storing audit logs for cloud services, including enabling detection, investigation, and remediation processes with controls to generate high-quality alerts with native threat detection in cloud services; it also includes collecting logs with a cloud monitoring service, centralizing security analysis with a SIEM, time synchronization, and log retention. |
| [Incident Response (IR)](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-incident-response) | Incident Response covers controls in incident response life cycle - preparation, detection and analysis, containment, and post-incident activities, including using Azure services (such as Microsoft Defender for Cloud and Sentinel) and/or other cloud services to automate the incident response process. |
| [Posture and Vulnerability Management (PV)](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-posture-vulnerability-management) | Posture and Vulnerability Management focuses on controls for assessing and improving cloud security posture, including vulnerability scanning, penetration testing and remediation, as well as security configuration tracking, reporting, and correction in cloud resources. |
| [Endpoint Security (ES)](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-endpoint-security) | Endpoint Security covers controls in endpoint detection and response, including use of endpoint detection and response (EDR) and anti-malware service for endpoints in cloud environments. |
| [Backup and Recovery (BR)](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-backup-recovery) | Backup and Recovery covers controls to ensure that data and configuration backups at the different service tiers are performed, validated, and protected. |
| [DevOps Security (DS)](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-devops-security) | DevOps Security covers the controls related to the security engineering and operations in the DevOps processes, including deployment of critical security checks (such as static application security testing, vulnerability management) prior to the deployment phase to ensure the security throughout the DevOps process; it also includes common topics such as threat modeling and software supply security. |
| [Governance and Strategy (GS)](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-governance-strategy) | Governance and Strategy provides guidance for ensuring a coherent security strategy and documented governance approach to guide and sustain security assurance, including establishing roles and responsibilities for the different cloud security functions, unified technical strategy, and supporting policies and standards. |

#### Recommendations in Microsoft cloud security benchmark

Each recommendation includes the following information:

* **ID**: The Benchmark ID that corresponds to the recommendation.
* **CIS Controls v8 ID(s)**: The CIS Controls v8 control(s) that correspond to the recommendation.
* **CIS Controls v7.1 ID(s)**: The CIS Controls v7.1 control(s) that correspond to the recommendation (not available in the web due to the formatting reason).
* **PCI-DSS v3.2.1 ID(s)**: The PCI-DSS v3.2.1 control(s) that correspond to the recommendation.
* **NIST SP 800-53 r4 ID(s)**: The NIST SP 800-53 r4 (Moderate and High) control(s) correspond to this recommendation.
* **Security Principle**: The recommendation focused on the "what", explaining the control at the technology-agnostic level.
* **Azure Guidance**: The recommendation focused on the "how", explaining the Azure technical features and implementation basics.
* **AWS Guidance**: The recommendation focused on the "how", explaining the AWS technical features and implementation basics.
* **Implementation and additional context**: The implementation details and other relevant context which links to the Azure and AWS service offering documentation articles.
* **Customer Security Stakeholders**: The [security functions](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/organize/cloud-security#security-functions) at the customer organization who may be accountable, responsible, or consulted for the respective control. It may be different from organization to organization depending on your company’s security organization structure, and the roles and responsibilities you set up related to Azure security.

The control mappings between MCSB and industry benchmarks (such as CIS, NIST, and PCI) only indicate that a specific Azure feature(s) can be used to fully or partially address a control requirement defined in these industry benchmarks. You should be aware that such implementation does not necessarily translate to the full compliance of the corresponding control(s) in these industry benchmarks.

We welcome your detailed feedback and active participation in the Microsoft cloud security benchmark effort. If you would like to provide direct input, please email us at [benchmarkfeedback@microsoft.com](mailto:benchmarkfeedback@microsoft.com).

#### Download

You can download the Benchmark and baseline offline copy in [spreadsheet format](https://github.com/MicrosoftDocs/SecurityBenchmarks).

#### Next steps

* See the first security control: [Network security](https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-network-security)
* Read the [Microsoft cloud security benchmark introduction](https://learn.microsoft.com/en-us/security/benchmark/azure/introduction)
* Learn the [Azure Security Fundamentals](https://learn.microsoft.com/en-us/azure/security/fundamentals)
