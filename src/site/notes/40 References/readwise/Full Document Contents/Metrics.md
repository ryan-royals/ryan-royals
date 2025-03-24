---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/metrics/","tags":["rw/articles"]}
---

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article1.be68295a7e40.png)

For other uses, see [Metric (disambiguation)](https://en.wikipedia.org/wiki/Metric_(disambiguation)).

**Router metrics** are configuration values used by a [router](https://en.wikipedia.org/wiki/Router_(computing)) to make routing decisions. A *metric* is typically one of many fields in a [routing table](https://en.wikipedia.org/wiki/Routing_table). Router metrics help the router choose the best route among multiple feasible routes to a destination. The route will go in the direction of the gateway with the lowest metric.

A router metric is typically based on information such as [path length](https://en.wikipedia.org/wiki/Hop_(networking)), [bandwidth](https://en.wikipedia.org/wiki/Bandwidth_(computing)), [load](https://en.wikipedia.org/wiki/Load_(computing)), [hop count](https://en.wikipedia.org/wiki/Hop_count), path cost, [delay](https://en.wikipedia.org/wiki/Network_delay), [maximum transmission unit](https://en.wikipedia.org/wiki/Maximum_transmission_unit) (MTU), [reliability](https://en.wikipedia.org/wiki/Reliability_(computer_networking)) and communications cost.

#### Examples

A metric can include:

* measuring link utilization (using SNMP)
* number of hops ([hop count](https://en.wikipedia.org/wiki/Hop_count))
* speed of the path
* packet loss (router congestion/conditions)
* [Network delay](https://en.wikipedia.org/wiki/Network_delay)
* path reliability
* path [bandwidth](https://en.wikipedia.org/wiki/Bandwidth_(computing))
* throughput [SNMP - query routers]
* [load](https://en.wikipedia.org/wiki/Load_(computing))
* [Maximum transmission unit](https://en.wikipedia.org/wiki/Maximum_transmission_unit) (MTU)
* administrator configured value

In [EIGRP](https://en.wikipedia.org/wiki/EIGRP), metrics is represented by an integer from 0 to 4,294,967,295 (The size of a 32-bit integer). In [Microsoft Windows XP](https://en.wikipedia.org/wiki/Microsoft_Windows_XP) routing it ranges from 1 to 9999.

A metric can be considered as:1(https://en.wikipedia.org/wiki/Metrics_(networking)#cite_note-1)

* additive - the total cost of a path is the sum of the costs of individual links along the path,
* concave - the total cost of a path is the minimum of the costs of individual links along the path,
* multiplicative - the total cost of a path is the product of the costs of individual links along the path.

#### Service level metrics

Router metrics are metrics used by a router to make routing decisions. It is typically one of many fields in a routing table.

Router metrics can contain any number of values that help the router determine the best route among multiple routes to a destination. A router metric typically based on information like path length, bandwidth, load, hop count, path cost, delay, MTU, reliability and communications cost.

#### See also

* [Administrative distance](https://en.wikipedia.org/wiki/Administrative_distance), indicates the source of routing table entry and is used in preference to metrics for routing decisions2(https://en.wikipedia.org/wiki/Metrics_(networking)#cite_note-2)3(https://en.wikipedia.org/wiki/Metrics_(networking)#cite_note-3)4(https://en.wikipedia.org/wiki/Metrics_(networking)#cite_note-4)

#### References

1. **[^](https://en.wikipedia.org/wiki/Metrics_(networking)#cite_ref-1)** Rao, S. Dharma; Murthy, C. Siva Ram (2005). "Distributed dynamic QoS-aware routing in WDM optical networks". *Computer Networks*. **48** (4): 585–604. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1016/j.comnet.2004.11.003](https://doi.org/10.1016%2Fj.comnet.2004.11.003).
2. **[^](https://en.wikipedia.org/wiki/Metrics_(networking)#cite_ref-2)** ["Administrative Distance and Metric"](https://etutorials.org/Networking/Integrated+cisco+and+unix+network+architectures/Chapter+8.+Static+Routing+Concepts/Administrative+Distance+and+Metric/). [Archived](https://web.archive.org/web/20211122173400/http://etutorials.org/Networking/Integrated+cisco+and+unix+network+architectures/Chapter+8.+Static+Routing+Concepts/Administrative+Distance+and+Metric/) from the original on 2021-11-22. Retrieved 2021-12-23.
3. **[^](https://en.wikipedia.org/wiki/Metrics_(networking)#cite_ref-3)** ["Understand the significance of administrative distance and metrics when working with routers"](https://www.techrepublic.com/article/understand-the-significance-of-administrative-distance-and-metrics-when-working-with-routers/). [Archived](https://web.archive.org/web/20211223222331/https://www.techrepublic.com/article/understand-the-significance-of-administrative-distance-and-metrics-when-working-with-routers/) from the original on 2021-12-23. Retrieved 2021-12-23.
4. **[^](https://en.wikipedia.org/wiki/Metrics_(networking)#cite_ref-4)** ["Administrative distance & metric"](https://study-ccna.com/administrative-distance-metric/). [Archived](https://web.archive.org/web/20211223222332/https://study-ccna.com/administrative-distance-metric/) from the original on 2021-12-23. Retrieved 2021-12-23.

#### External links

* [Survey of routing metrics](http://rainer.baumann.info/public/tik262.pdf)
