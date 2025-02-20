---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/what-is-bgp-border-gateway-protocol-an-introduction/","tags":["rw/articles"]}
---

![rw-book-cover](https://i.ytimg.com/vi/A1KXPpqlNZ4/maxresdefault.jpg)

Jen English: Border Gateway Protocol is the routing protocol that connects the entire internet. While that description makes BGP sound simple, it's a bit more complicated. Routing in a flat local area network is easy. Every device is connected to the same computer network and they use local network addresses to communicate with other devices and resources. If node A wants to connect to node B on the same LAN, it can do so directly. Once an organization has more than one LAN, it needs to connect all of the LANs. So if 

node A wants to connect to node C on a different LAN, the request must go through a router, which forwards the request the network on which node C is connected. This type of routing is relatively simple and can use various internal routing protocols, including internal BGP. Large organizations and most ISPs manage internet connectivity for multiple network sites and locations. This is called an autonomous system, or AS. While networks inside an AS handle 

routing for their own local traffic, a BGP router directs all inbound traffic into the autonomous system, and all outbound traffic going to the internet from inside the AS. The public internet comprises thousands of these autonomous systems, and BGP directs how packets should be forwarded between them. When a BGP router connects to a router in a neighboring AS, it's called external BGP. Each BGP router contains routing tables it can use to find available pass on 

the global internet. When a BGP router receives a request, it uses this information to determine the best path to the destination. For BGP to work, AS operators need to trust each other. As such, they configure peering agreements that enable them to establish direct connections with each other, and permit BGP traffic to travel throughout their autonomous systems.
