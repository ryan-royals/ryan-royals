---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/administrative-distance/","tags":["rw/articles"]}
---

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article0.00998d930354.png)

**Administrative distance** (**AD**) or **route preference**1(https://en.wikipedia.org/wiki/Administrative_distance#cite_note-1) is a number of [arbitrary unit](https://en.wikipedia.org/wiki/Arbitrary_unit) assigned to [dynamic routes](https://en.wikipedia.org/wiki/Dynamic_route), [static routes](https://en.wikipedia.org/wiki/Static_route) and directly-connected routes. The value is used in [routers](https://en.wikipedia.org/wiki/Router_(computing)) to rank [routes](https://en.wikipedia.org/wiki/Routing) from most preferred (low AD value) to least preferred (high AD value).2(https://en.wikipedia.org/wiki/Administrative_distance#cite_note-Understanding_Route_Redistribution-2)3(https://en.wikipedia.org/wiki/Administrative_distance#cite_note-cisco-3) When multiple paths to the same destination are available in its [routing table](https://en.wikipedia.org/wiki/Routing_table), the router uses the route with the lowest administrative distance.

Router vendors typically design their routers to assign a default administrative distance to each kind of route. For example, on Cisco routers, routes issued by the [Open Shortest Path First](https://en.wikipedia.org/wiki/OSPF) routing protocol have a lower default administrative distance than routes issued by the [Routing Information Protocol](https://en.wikipedia.org/wiki/Routing_Information_Protocol). This is because, by default on Cisco routers, OSPF has a default administrative distance of 110 and RIP has a default administrative distance of 120. Administrative distance values can, however, usually be adjusted manually by a [network administrator](https://en.wikipedia.org/wiki/Network_administrator).2(https://en.wikipedia.org/wiki/Administrative_distance#cite_note-Understanding_Route_Redistribution-2)

#### Overview

The administrative distance (AD) value is assigned by the [router](https://en.wikipedia.org/wiki/Router_(computing)) on a per-protocol basis. Routers, by design, should not install multiple routes into the routing table as this has the potential to cause routing loops.2(https://en.wikipedia.org/wiki/Administrative_distance#cite_note-Understanding_Route_Redistribution-2) While a router may run multiple [routing protocols](https://en.wikipedia.org/wiki/Routing_protocol) on the same device, it is necessary for the router to implement a process to ensure that multiple routes, pointing to the same destination do not simultaneously exist in the routing table. Each process running on a router advertises its administrative distance value to the local router. The router uses this value to determine which route should be used. Once a route has been selected, the routing information database is updated. If two routes have the same administrative distance, the router uses its vendor-specific algorithm to determine which route should be installed.2(https://en.wikipedia.org/wiki/Administrative_distance#cite_note-Understanding_Route_Redistribution-2) [Cisco](https://en.wikipedia.org/wiki/Cisco) routers simply ignore the values and fall back to the default values, which are never the same.4(https://en.wikipedia.org/wiki/Administrative_distance#cite_note-ReferenceA-4)

The router will usually compare administrative distances to determine which protocol has the lowest value. The router prefers protocols that have a lower assigned administrative distance. For example, OSPF has a default distance of 110, so it is preferred by the router process, over RIP, which has a default distance of 120. The administrator can arbitrarily reconfigure the administrative distances, which affects the ranking of the preferred routes by the routing process. On Cisco routers, [static routes](https://en.wikipedia.org/wiki/Static_routing) have an administrative distance of 1, making them preferred over routes issued by a [dynamic routing protocol](https://en.wikipedia.org/wiki/Dynamic_routing). The administrative distance is a value that is always only referenced by the local router itself. The administrative distance is not advertised on the network.2(https://en.wikipedia.org/wiki/Administrative_distance#cite_note-Understanding_Route_Redistribution-2)

#### Default administrative distances

##### Cisco

The following table lists the default administrative distances for various routing protocols used on [Cisco](https://en.wikipedia.org/wiki/Cisco_Systems) routers.3(https://en.wikipedia.org/wiki/Administrative_distance#cite_note-cisco-3)

| Routing protocol | Administrative distance  |
| --- | --- |
| Directly connected interface | 0a(https://en.wikipedia.org/wiki/Administrative_distance#cite_note-5)5(https://en.wikipedia.org/wiki/Administrative_distance#cite_note-Cisco_AD-6) |
| Static route | 1  |
| Dynamic Mobile Network Routing (DMNR) | 3  |
| [EIGRP](https://en.wikipedia.org/wiki/EIGRP) summary route | 5  |
| External [BGP](https://en.wikipedia.org/wiki/BGP) | 20  |
| [EIGRP](https://en.wikipedia.org/wiki/EIGRP) internal route | 90  |
| [IGRP](https://en.wikipedia.org/wiki/IGRP) | 100  |
| [Open Shortest Path First](https://en.wikipedia.org/wiki/OSPF) (OSPF) | 110  |
| [Intermediate System to Intermediate System](https://en.wikipedia.org/wiki/IS-IS) (IS-IS) | 115  |
| [Routing Information Protocol](https://en.wikipedia.org/wiki/Routing_Information_Protocol) (RIP) | 120  |
| [Exterior Gateway Protocol](https://en.wikipedia.org/wiki/Exterior_Gateway_Protocol) (EGP) | 140  |
| [ODR](https://en.wikipedia.org/wiki/On_Demand_Routing) | 160  |
| [EIGRP](https://en.wikipedia.org/wiki/EIGRP) external route | 170  |
| Internal [BGP](https://en.wikipedia.org/wiki/BGP) | 200  |
| [Next Hop Resolution Protocol](https://en.wikipedia.org/wiki/Next_Hop_Resolution_Protocol) (NHRP) | 2506(https://en.wikipedia.org/wiki/Administrative_distance#cite_note-Cisco_NHRP-7) |
| Default static route learned via DHCP | 254  |
| Unknown and unused | 255b(https://en.wikipedia.org/wiki/Administrative_distance#cite_note-8) |

1. **[^](https://en.wikipedia.org/wiki/Administrative_distance#cite_ref-5)** Only the interface itself has an administrative distance of 0, since a route cannot have a distance of less than 1.
2. **[^](https://en.wikipedia.org/wiki/Administrative_distance#cite_ref-8)** An administrative distance of 255 will cause the router to remove the route from the routing table and not use it.

##### Juniper

The following table lists the default administrative distances for various routing protocols used on Juniper routers.7(https://en.wikipedia.org/wiki/Administrative_distance#cite_note-Juniper_AD-9)

| Routing protocol | Administrative distance  |
| --- | --- |
| Directly connected interface | 0  |
| Static routes | 5  |
| OSPF internal routes | 10  |
| IS-IS Level 1 Internal | 15  |
| IS-IS Level 2 Internal | 18  |
| [RIP](https://en.wikipedia.org/wiki/Routing_Information_Protocol) | 100  |
| Aggregate (route summary) | 130  |
| OSPF external routes | 150  |
| IS-IS Level 1 External | 160  |
| IS-IS Level 2 External | 165  |
| BGP | 170  |

##### Extreme Networks

The following table lists the default administrative distances used on ExtremeXOS / Switch-Engine.

| Routing protocol  | Administrative distance  |
| --- | --- |
| Directly connected  | 10  |
| MPLS  | 20  |
| Blackhole  | 50  |
| Static  | 1100  |
| HostMobility  | 1150  |
| ICMP-Redirect  | 1200  |
| Fabric  | 1699  |
| eBGP  | 1700  |
| iBGP  | 1900  |
| OSPFintra  | 2200  |
| OSPFinter  | 2300  |
| IS-IS  | 2350  |
| IS-IS L1  | 2360  |
| IS-IS L2  | 2370  |
| RIP  | 2400  |
| OSPF AS Ext  | 3100  |
| OSPF Ext1  | 3200  |
| OSPF Ext2  | 3300  |
| IS-IS L1 Ext  | 3400  |
| IS-IS L2 Ext  | 3500  |
| Bootp  | 5000  |

The following table lists the default administrative distances used on Extreme VOSS / Fabric-Engine.

| Routing Protocol  | Administrative distance  |
| --- | --- |
| Local  | 0  |
| Static  | 5  |
| SPBm L1  | 7  |
| OSPFintra  | 20  |
| OSPFinter  | 25  |
| eBGP  | 45  |
| RIP  | 100  |
| OSPF Ext1  | 120  |
| OSPF Ext2  | 125  |
| iBGP  | 175  |

#### Configuration

##### Cisco IOS

The [network administrator](https://en.wikipedia.org/wiki/Network_administrator) may modify the administrative distance to change the desired ranking of router protocols. This may be necessary in cases where [routing redistribution](https://en.wikipedia.org/w/index.php?title=Routing_redistribution&action=edit&redlink=1) has to be used, otherwise, routing loops could occur.3(https://en.wikipedia.org/wiki/Administrative_distance#cite_note-cisco-3) The Cisco Internetwork Operating System enables network administrators to modify the distance by changing the distance value in sub-router configuration mode. In the example below, RIP's administrative distance is changed to 89 so that it used in preference to OSPF.3(https://en.wikipedia.org/wiki/Administrative_distance#cite_note-cisco-3)

```
R1#enable

R1#configure terminal

R1(config)#router rip

R1(config-router)#distance 89

```

Manually configuring the administrative distance is also required when configuring a floating static route. Floating static routes are used to provide an alternate path when a primary link fails. In order for static routes to be configured as a backup, the static route's administrative distance would need to be adjusted. Otherwise, it will take precedence over all routing protocols and routes issued from a routing protocol will not be inserted into the routing table.3(https://en.wikipedia.org/wiki/Administrative_distance#cite_note-cisco-3) The example below shows how to configure the administrative distance to 254 to specify that it should only be used as a last resort.

`R1(config)# **ip route 10.0.0.0 255.0.0.0 backupLink 1 254**`

In the event that two routing protocols are configured with the same administrative distance, the [Cisco](https://en.wikipedia.org/wiki/Cisco_Systems) router will ignore the configured values and instead use the default values.4(https://en.wikipedia.org/wiki/Administrative_distance#cite_note-ReferenceA-4)

Verifying the configuration of the administrative distance is done on Cisco equipment using the *show ip route* command in [privileged exec mode](https://en.wikipedia.org/w/index.php?title=Privileged_exec_mode&action=edit&redlink=1) on the console of the [Cisco](https://en.wikipedia.org/wiki/Cisco_Systems) router.8(https://en.wikipedia.org/wiki/Administrative_distance#cite_note-10)9(https://en.wikipedia.org/wiki/Administrative_distance#cite_note-11) In the example shown below, the administrative distance is 1. The letter "S" indicates that the route is a [static route](https://en.wikipedia.org/wiki/Static_route) that has, for all intents and purposes, been added manually to the router process by the administrator and installed into the routing table.

```
Router#enable

Router#configure terminal

Router(config)#ip route 1.1.1.0 255.255.255.0 fastEthernet 0/0

Router(config)#do show ip route

```

The *do show ip route* command will display the following, confirming that a [static route](https://en.wikipedia.org/wiki/Static_routing) has an administrative distance of 1.

`***S 1.1.1.0/0 [1/0] via 172.31.0.1***`

#### See also

* [Metrics (networking)](https://en.wikipedia.org/wiki/Metrics_(networking)), used for choosing a route when administrative distance is the same10(https://en.wikipedia.org/wiki/Administrative_distance#cite_note-12)11(https://en.wikipedia.org/wiki/Administrative_distance#cite_note-13)12(https://en.wikipedia.org/wiki/Administrative_distance#cite_note-14)

#### References

1. **[^](https://en.wikipedia.org/wiki/Administrative_distance#cite_ref-1)** ["Route Preferences"](https://www.juniper.net/documentation/software/cable/junosg30/swconfig30-interfaces/html/protocols-overview4.html). Juniper Networks. Retrieved 2018-06-18.
2. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/Administrative_distance#cite_ref-Understanding_Route_Redistribution_2-0) [***b***](https://en.wikipedia.org/wiki/Administrative_distance#cite_ref-Understanding_Route_Redistribution_2-1) [***c***](https://en.wikipedia.org/wiki/Administrative_distance#cite_ref-Understanding_Route_Redistribution_2-2) [***d***](https://en.wikipedia.org/wiki/Administrative_distance#cite_ref-Understanding_Route_Redistribution_2-3) [***e***](https://en.wikipedia.org/wiki/Administrative_distance#cite_ref-Understanding_Route_Redistribution_2-4) Franck Le; Geoffrey G. Xie; Hui Zhang, [*Understanding Route Redistribution*](https://www.cs.cmu.edu/~4D/papers/rr-icnp07.pdf) (PDF)
3. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/Administrative_distance#cite_ref-cisco_3-0) [***b***](https://en.wikipedia.org/wiki/Administrative_distance#cite_ref-cisco_3-1) [***c***](https://en.wikipedia.org/wiki/Administrative_distance#cite_ref-cisco_3-2) [***d***](https://en.wikipedia.org/wiki/Administrative_distance#cite_ref-cisco_3-3) [***e***](https://en.wikipedia.org/wiki/Administrative_distance#cite_ref-cisco_3-4) Cisco Systems (2013), [What is Administrative Distance?](http://www.cisco.com/en/US/tech/tk365/technologies_tech_note09186a0080094195.shtml), retrieved 14 September 2013
4. ^ [Jump up to: ***a***](https://en.wikipedia.org/wiki/Administrative_distance#cite_ref-ReferenceA_4-0) [***b***](https://en.wikipedia.org/wiki/Administrative_distance#cite_ref-ReferenceA_4-1) Cisco Systems(n.d.), Information About Routing, Cisco Systems Inc, retrieved 16 September 2013
5. **[^](https://en.wikipedia.org/wiki/Administrative_distance#cite_ref-Cisco_AD_6-0)** Cisco, [*Default AD*](http://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/15986-admin-distance.html#topic2)
6. **[^](https://en.wikipedia.org/wiki/Administrative_distance#cite_ref-Cisco_NHRP_7-0)** Cisco, [*NHRP*](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_nhrp/command/reference/irn_book/nhrp-commands--a-through-z.html#wp8534493760)
7. **[^](https://en.wikipedia.org/wiki/Administrative_distance#cite_ref-Juniper_AD_9-0)** Juniper, [*Default AD*](https://www.juniper.net/documentation/en_US/junos/topics/reference/general/routing-protocols-default-route-preference-values.html)
8. **[^](https://en.wikipedia.org/wiki/Administrative_distance#cite_ref-10)** Cisco Systems (n.d), [Configuring Static Routing](http://www.cisco.com/en/US/docs/switches/datacenter/sw/5_x/nx-os/unicast/configuration/guide/l3_route.html), Cisco Systems Inc., retrieved 14 September 2013
9. **[^](https://en.wikipedia.org/wiki/Administrative_distance#cite_ref-11)** Cisco Systems (n.d), [Show Commands](http://www.cisco.com/en/US/docs/switches/datacenter/sw/6_x/nx-os/unicast/command/reference/l3_cmds_show.html#wp1688356), Cisco Systems Inc., retrieved 14 September 2013
10. **[^](https://en.wikipedia.org/wiki/Administrative_distance#cite_ref-12)** ["Administrative Distance and Metric"](https://etutorials.org/Networking/Integrated+cisco+and+unix+network+architectures/Chapter+8.+Static+Routing+Concepts/Administrative+Distance+and+Metric/). Retrieved 2021-12-23.
11. **[^](https://en.wikipedia.org/wiki/Administrative_distance#cite_ref-13)** ["Understand the significance of administrative distance and metrics when working with routers"](https://www.techrepublic.com/article/understand-the-significance-of-administrative-distance-and-metrics-when-working-with-routers/). Retrieved 2021-12-23.
12. **[^](https://en.wikipedia.org/wiki/Administrative_distance#cite_ref-14)** ["Administrative distance & metric"](https://study-ccna.com/administrative-distance-metric/). Retrieved 2021-12-23.
