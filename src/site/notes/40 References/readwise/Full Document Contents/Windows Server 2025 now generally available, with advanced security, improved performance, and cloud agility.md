---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/windows-server-2025-now-generally-available-with-advanced-security-improved-performance-and-cloud-agility/","tags":["rw/articles"]}
---

![rw-book-cover](https://azure.microsoft.com/en-us/blog/wp-content/uploads/2024/06/microsoft_logo-300x300.webp)

Generally available today, [Windows Server 2025](https://www.microsoft.com/windows-server/) builds on our mission to deliver a secure and high-performance Windows Server platform tailored to meet customers’ diverse needs. This release will enable you to deploy apps in any environment, whether on-premises, hybrid environments, or in the cloud.

![Woman at computer monitor](https://azure.microsoft.com/en-us/blog/wp-content/uploads/2024/11/WS-Placeholder-Image.png) 

#### Windows Server 2025

Investing in your success with Windows Server

[Try today](https://www.microsoft.com/en-us/windows-server/) 

#### Advanced multilayered security

In an era where cybersecurity is of utmost importance (see the [Microsoft Digital Defense Report 2024](https://www.microsoft.com/en-us/security/security-insider/intelligence-reports/microsoft-digital-defense-report-2024) and the [Microsoft Threat Intelligence Healthcare Ransomware Report](https://www.microsoft.com/en-us/security/blog/2024/10/22/microsoft-threat-intelligence-healthcare-ransomware-report-highlights-need-for-collective-industry-action/)), Windows Server 2025 stands out with a suite of security features designed to safeguard your data and infrastructure. Here are a few key capabilities: 

* **Active Directory (AD):** The gold standard for identity and authentication only gets better with new security capabilities to help fortify your environment against evolving threats with greater scalability and improvements in protocols, encryption, hardening, and new cryptographic support.
* **File services/server message block (SMB) hardening:** Windows Server 2025 includes SMB over QUIC to enable secure access to file shares over the internet. SMB security also adds hardened firewall defaults, brute force attack prevention, and protections for man in the middle attacks, relay attacks, and spoofing attacks.
* **Delegate Managed Service Accounts (dMSA):** Unlike traditional service accounts, dMSAs don’t require manual password management since AD automatically takes care of it. With dMSAs, specific permissions can be delegated to access resources in the domain, which reduces security risks and provides better visibility and logs of service account activity.

These advanced security features make Windows Server 2025 a robust and secure platform for your IT infrastructure that you should [begin evaluating immediately](https://www.microsoft.com/evalcenter/evaluate-windows-server-2025).

#### Cloud agility anywhere

Windows Server 2025 introduces several advanced hybrid cloud capabilities designed to enhance operational flexibility and connectivity across various environments. Key features include: 

* **Hotpatching enabled by Azure Arc:** Customers operating fully in the cloud have inherent modern security advantages like automatic software updates and back-up and recovery.  Now we’re bringing some of those capabilities to Windows Server 2025 for on-premises customers with a new hotpatching subscription service, enabled by Azure Arc. With hotpatching, customers will experience fewer reboots and minimal disruption to operations. Hotpatching delivers security updates for Azure Arc-enabled Windows Server 2025 Standard or Datacenter running on physical machines, virtual machines, on-premises, or multicloud servers. Hotpatching, currently in preview, will require a monthly subscription. The hotpatching feature remains no additional cost for Windows Server Datacenter Azure Edition virtual machines.
* **Easy Azure Arc onboarding**: Windows Server 2025 brings Azure’s powerful capabilities directly into your datacenter through [Azure Arc](https://azure.microsoft.com/en-us/products/azure-arc). This integration simplifies the onboarding process to Azure’s hybrid features and enhances operational flexibility, allowing you to manage and secure your hybrid and multicloud environments more effectively.
* **Software-defined network (SDN) multisite features**: The software-defined network (SDN) multisite features offer native L2 and L3 connectivity for seamless workload migration across various locations, coupled with unified network policy management.
* **Unified network policy management:** This capability allows for centralized management of network policies, making it easier to maintain consistent security and performance standards across your hybrid cloud environment.

These hybrid cloud capabilities make Windows Server 2025 an ideal choice for organizations looking to optimize their IT infrastructure and leverage the benefits of both on-premises and cloud environments.

#### AI, performance, and scale

Windows Server 2025 is designed to handle the most demanding workloads, including AI and machine learning. Here are some key capabilities: 

* **Hyper-V, AI, and machine learning:** With built-in support for GPU partitioning and the ability to process large data sets across distributed environments, Windows Server 2025 offers a high-performance platform for both traditional applications and advanced AI workloads with live migration and high availability.
* **NVMe storage performance:** Windows Server 2025 delivers up to 60% more storage IOPs performance compared to Windows Server 2022 on identical systems. (Based on 4K randread using Diskpsd 2.2 with Kioxia CM7 SSd)
* **Storage Spaces Direct and storage flexibility:** Windows Server supports a wide range of storage solutions such as local, NAS, and SAN for decades and continues to this day. Windows Server 2025 delivers more storage innovation with Native ReFS deduplication and compression, thinly povisioned Storage Spaces, and Storage Replica Compression now available in all editions of Windows Server 2025.
* **Hyper-V performance and scale:** Windows Server 2025 introduces massive performance and scalability improvements that come from Azure. Windows Server 2025 Hyper-V virtual machine maximums:
	+ Maximum memory per VM: 240 Terabytes\* — (10x previous)
	+ Maximum virtual processors per VM: 2048 VPs\* — (~8.5x previous)

\*Requires Generation 2 VMs

Windows Server 2025 delivers major advancements across the board for Hyper-V, GPU integration, Storage Spaces Direct (software defined storage), software-defined networking, and clustering. These improvements make Windows Server 2025 an excellent option for organizations looking for a virtualization solution and for organizations looking to leverage AI and machine learning while maintaining high performance and scalability.

#### System Center 2025 is available now

By delivering [System Center 2025](https://aka.ms/sc2025) concurrently with [Windows Server 2025](https://www.microsoft.com/en-us/windows-server/), management of Windows Server at scale is available immediately. This allows organizations to make the most of new Windows Server features. Designed to enhance agility, performance, and security, this release is set to enhance how organizations optimize their infrastructure and virtualized software-defined datacenters. We encourage you to visit the [System Center 2025](https://aka.ms/sc2025) post learn more. 

#### Microsoft Ignite 2024

We look forward to meeting you in person and sharing these and other Windows Server 2025 features in our sessions and at our booth at Microsoft [Ignite](https://ignite.microsoft.com/en-US/home) in Chicago, November 19-21. For those of you who can’t make it, many sessions, including our Windows Server breakout titled [Windows Server 2025: New Ways to gain cloud agility and security](https://ignite.microsoft.com/en-US/sessions/BRK238?source=sessions), will be available for online viewing. 

We are also excited to bring new features to customers on existing Windows Server versions like 2016, 2019, 2022, as well as 2025. Windows Server Software Assurance or active subscription customers can access Azure management tools like Azure Update Manager, Azure Policy Guest Configuration, Disaster Recovery, Change Tracking and Inventory, and more, with access to many features coming at no additional cost\*\*. Tune into Microsoft Ignite where we will show more demos and information on how to access these new offerings.

#### Additional Windows Server resources

* [Try Windows Server 2025 today](https://www.microsoft.com/en-us/evalcenter/evaluate-windows-server-2025)
* [Windows Server documentation](https://learn.microsoft.com/en-us/windows-server/)
* Learn more about what’s new in [Windows Server 2025](https://aka.ms/WS2025Highlights)
* [Microsoft Certified](https://learn.microsoft.com/en-us/credentials/certifications/windows-server-hybrid-administrator/): Windows Server Hybrid Administrator Associate
* [Administer Active Directory Domain Services](https://learn.microsoft.com/en-us/credentials/applied-skills/administer-active-directory-domain-services/)

---

#### Notes

\*\* Note: compute and storage may incur additional fees.

The post [Windows Server 2025 now generally available, with advanced security, improved performance, and cloud agility](https://www.microsoft.com/en-us/windows-server/blog/2024/11/04/windows-server-2025-now-generally-available-with-advanced-security-improved-performance-and-cloud-agility/) appeared first on [Microsoft Azure Blog](https://azure.microsoft.com/en-us/blog).
