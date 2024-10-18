---
{"dg-publish":true,"permalink":"/40-references/readwise/configure-azure-application-gateway-training/","tags":["rw/articles"]}
---

![40 References/attachments/be6ec1dc11499f9537329d089643e21f_MD5.jpg](/img/user/40%20References/attachments/be6ec1dc11499f9537329d089643e21f_MD5.jpg)
  
URL: https://learn.microsoft.com/en-us/training/modules/load-balancing-https-traffic-azure/3-configure-azure-application-gateway
Author: wwlpublish

## Summary

The Azure Application Gateway routes requests to web servers and monitors their health. It uses health probes to check if servers are functioning, automatically stopping requests to unhealthy servers. Listeners and request routing rules help manage incoming traffic and direct it to the appropriate backend servers.

## Highlights added September 26, 2024 at 9:39 AM
>**Probe property** **Value** **Description** Probe URL `<protocol>://127.0.0.1:<port>/` The protocol and port are inherited from the backend HTTP settings to which the probe is associated Interval 30 The amount of time in seconds to wait before the next health probe is sent. Time-out 30 The amount of time in seconds the application gateway waits for a probe response before marking the probe as unhealthy. If a probe returns as healthy, the corresponding backend is immediately marked as healthy. Unhealthy threshold 3 Governs how many probes to send in case there's a failure of the regular health probe. In v1 SKU, these additional health probes are sent in quick succession to determine the health of the backend quickly and don't wait for the probe interval. In the case of v2 SKU, the health probes wait the interval. The back-end server is marked down after the consecutive probe failure count reaches the unhealthy threshold. ([View Highlight] (https://read.readwise.io/read/01j8nthp20x4zmej5gx81tjzp6))


## Highlights added September 26, 2024 at 9:55 AM
>Custom probes give you more granular control over the health monitoring. When using custom probes, you can configure a custom hostname, URL path, probe interval, and how many failed responses to accept before marking the back-end pool instance as unhealthy, etc.
>**Custom health probe settings**
>The following table provides definitions for the properties of a custom health probe.
>Expand table
>**Probe property**
>**Description**
>Name
>Name of the probe. This name is used to identify and refer to the probe in back-end HTTP settings.
>Protocol
>Protocol used to send the probe. This property must match with the protocol defined in the back-end HTTP settings it is associated to
>Host
>Host name to send the probe with. In v1 SKU, this value is used only for the host header of the probe request. In v2 SKU, it's used both as host header and SNI
>Path
>Relative path of the probe. A valid path starts with '/'
>Port
>If defined, this property is used as the destination port. Otherwise, it uses the same port as the HTTP settings that it is associated to. This property is only available in the v2 SKU
>Interval
>Probe interval in seconds. This value is the time interval between two consecutive probes
>Time-out
>Probe time-out in seconds. If a valid response isn't received within this time-out period, the probe is marked as failed
>Unhealthy threshold
>Probe retry count. The back-end server is marked down after the consecutive probe failure count reaches the unhealthy threshold ([View Highlight] (https://read.readwise.io/read/01j8ntqwtkre6zw3fjfdqkhmvh))


