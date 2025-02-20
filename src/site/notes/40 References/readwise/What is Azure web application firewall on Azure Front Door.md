---
{"dg-publish":true,"permalink":"/40-references/readwise/what-is-azure-web-application-firewall-on-azure-front-door/","tags":["rw/articles"]}
---

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_921743/logo-ms-social_OuOwLI6.png)

## Full Document
[[40 References/readwise/Full Document Contents/What is Azure web application firewall on Azure Front Door\|Readwise/Full Document Contents/What is Azure web application firewall on Azure Front Door.md]]

## Highlights
Azure Web Application Firewall (WAF) on Azure Front Door provides centralized protection for your web applications. WAF defends your web services against common exploits and vulnerabilities. It keeps your service highly available for your users and helps you meet compliance requirements. ([View Highlight] (https://read.readwise.io/read/01h3bg4c8aysrqxytje5pq3nq2))


Azure Front Door has [two tiers](https://learn.microsoft.com/en-us/azure/web-application-firewall/afds/afds-overview/../../frontdoor/standard-premium/overview): Front Door Standard and Front Door Premium. WAF is natively integrated with Front Door Premium with full capabilities. For Front Door Standard, only [custom rules](https://learn.microsoft.com/en-us/azure/web-application-firewall/afds/afds-overview#custom-authored-rules) are supported. ([View Highlight] (https://read.readwise.io/read/01h3bg5480j91bg3ebmhhbfken))


• Protect your web applications from web vulnerabilities and attacks without modification to back-end code.
• Protect your web applications from malicious bots with the IP Reputation ruleset.
• Protect your application against DDoS attacks. For more information, see [Application DDoS Protection](https://learn.microsoft.com/en-us/azure/web-application-firewall/afds/afds-overview/../shared/application-ddos-protection). ([View Highlight] (https://read.readwise.io/read/01h3bg4zddr648krn11s44f896))


WAF policy can be configured to run in the following two modes:
• **Detection mode:** When run in detection mode, WAF doesn't take any other actions other than monitors and logs the request and its matched WAF rule to WAF logs. You can turn on logging diagnostics for Front Door. When you use the portal, go to the **Diagnostics** section.
• **Prevention mode:** In prevention mode, WAF takes the specified action if a request matches a rule. If a match is found, no further rules with lower priority are evaluated. Any matched requests are also logged in the WAF logs. ([View Highlight] (https://read.readwise.io/read/01h3bg5n29hwsgqdbd62ahcn3g))


