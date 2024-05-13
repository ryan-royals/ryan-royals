---
{"dg-publish":true,"dg-path":"Exam AZ-700 Designing and Implementing Microsoft Azure Networking Solutions.md","permalink":"/exam-az-700-designing-and-implementing-microsoft-azure-networking-solutions/","tags":["projects"]}
---


## Exam AZ-700: Designing and Implementing Microsoft Azure Networking Solutions

[Exam AZ-700: Designing and Implementing Microsoft Azure Networking Solutions - Certifications | Microsoft Learn](https://learn.microsoft.com/en-us/certifications/exams/az-700/)

### Modules in Learning Path

[[30 Slipbox/Introduction to Azure Virtual Networks\|Introduction to Azure Virtual Networks]]  
[[99 Inbox/Design and Implement hybrid networking\|Design and Implement hybrid networking]]  
[[Design and implement Azure ExpressRoute\|Design and implement Azure ExpressRoute]]  
[[Load balance non-HTTP(S) traffic in Azure\|Load balance non-HTTP(S) traffic in Azure]]  
[[Load balance HTTP(S) traffic in Azure\|Load balance HTTP(S) traffic in Azure]]  
[[Design and implement network security\|Design and implement network security]]  
[[Design and implement private access to Azure Services\|Design and implement private access to Azure Services]]  
[[Design and implement network monitoring\|Design and implement network monitoring]]

## Things to Learn

- What is SSL offloading

## Revision Factoids

- Basic Route Based VPN Gateway support 10 S2S VPNs.
	- VpnGw1 supports 30, VPNGw5Az supports 100
- VpnGw4 supports 5000 P2S connections with 5Gbps
	- VpnGw5 supports 10000 P2S connections and 10Gbps
- Windows Admin Center is used to configure Azure Extended Network
- Express Route Microsoft Peering by default advertises no rules to the ExpressRoute. A Route Filter must be used to select what services to advertise (Exchange Online as a Example.)
- Express Route FastPath allows you to bypass the virtual network gateway
- Bidirectional Forwarding Detection is enabled on your router to see if a link goes offline, and provides near instant failover
- ExpressRoute scale units are 2Gbps each
- network policies are tenant or sub level policies that contain routes and security group rules
- Service endpoints can be used to restrict access to particular services, like storage accounts
- Enabling Direct Server Return (DSR), known in Azure as Floating IP, involves creating a loopback adapter on the virtual machine and assigning the loopback adapter the IP address of the frontend listener. This way, the virtual machines knows where to send the traffic back to for session affinity.  
[[30 Slipbox/Az700 trial exam\|Az700 trial exam]]
