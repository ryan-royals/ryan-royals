---
{"dg-publish":true,"permalink":"/40-references/readwise/tutorial-create-a-microsoft-entra-domain-services-managed-domain-microsoft-entra-id/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)

## Full Document
[[40 References/readwise/Full Document Contents/Tutorial - Create a Microsoft Entra Domain Services Managed Domain - Microsoft Entra ID\|Readwise/Full Document Contents/Tutorial - Create a Microsoft Entra Domain Services Managed Domain - Microsoft Entra ID.md]]

## Highlights
Microsoft Entra Domain Services provides managed domain services such as domain join, group policy, LDAP, Kerberos/NTLM authentication that is fully compatible with Windows Server Active Directory. You consume these domain services without deploying, managing, and patching domain controllers yourself. Domain Services integrates with your existing Microsoft Entra tenant. This integration lets users sign in using their corporate credentials, and you can use existing groups and user accounts to secure access to resources. ([View Highlight] (https://read.readwise.io/read/01j2ae493msz5tc9ng1c71jhxc))


Important
You can't move the managed domain to a different subscription, resource group, or region after you create it. Take care to select the most appropriate subscription, resource group, and region when you deploy the managed domain. ([View Highlight] (https://read.readwise.io/read/01j2ae3ycf3ezzgce0rtk5mn65))


When you create a managed domain, you specify a DNS name. There are some considerations when you choose this DNS name:
• **Built-in domain name:** By default, the built-in domain name of the directory is used (a *.onmicrosoft.com* suffix). If you wish to enable secure LDAP access to the managed domain over the internet, you can't create a digital certificate to secure the connection with this default domain. Microsoft owns the *.onmicrosoft.com* domain, so a Certificate Authority (CA) won't issue a certificate.
• **Custom domain names:** The most common approach is to specify a custom domain name, typically one that you already own and is routable. When you use a routable, custom domain, traffic can correctly flow as needed to support your applications.
• **Non-routable domain suffixes:** We generally recommend that you avoid a non-routable domain name suffix, such as *contoso.local*. The *.local* suffix isn't routable and can cause issues with DNS resolution. ([View Highlight] (https://read.readwise.io/read/01j2ae57b4aavcnaqza2p6sv6t))


