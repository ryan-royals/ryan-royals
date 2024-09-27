---
{"dg-publish":true,"permalink":"/40-references/readwise/design-and-implement-azure-vpn-gateway-training/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png)
  
URL: https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/2-design-implement-vpn-gateway
Author: wwlpublish

## Summary

Azure VPN Gateways provide secure encrypted connections between Azure virtual networks and on-premises locations over the public Internet. When planning a VPN gateway deployment, consider factors like throughput, VPN type, and gateway SKU. Different VPN types, such as RouteBased and PolicyBased, have specific configuration requirements and limitations for establishing connections.

## Highlights added August 30, 2024 at 2:23 PM
>The local network gateway typically refers to the on-premises location. You give the site a name by which Azure can refer to it, then specify the IP address or FQDN of the on-premises VPN device for the connection. You also specify the IP address prefixes that will be routed through the VPN gateway to the VPN device. The address prefixes you specify are the prefixes located in the on-premises network. ([View Highlight] (https://read.readwise.io/read/01hx5m9cdpkf5denb32tabpf8z))


>There is a validated list of standard VPN devices that work well with the VPN gateway. This list was created in partnership with device manufacturers like Cisco, Juniper, Ubiquiti, and Barracuda Networks. ([View Highlight] (https://read.readwise.io/read/01hx5mmyf0734zj9bj2d5vndqm))


>To provide better availability for your VPN connections, there are a few options available:
>• VPN Gateway redundancy (Active-standby)
>• Multiple on-premises VPN devices
>• Active-active Azure VPN gateway
>• Combination of both ([View Highlight] (https://read.readwise.io/read/01hx5mqkf42j09s1bshy97rysv))


>Here you create and set up the Azure VPN gateway in an active-active configuration and create two local network gateways and two connections for your two on-premises VPN devices as described above. The result is a full mesh connectivity of 4 IPsec tunnels between your Azure virtual network and your on-premises network. ([View Highlight] (https://read.readwise.io/read/01hx5nrz9xt6xw6hjzbqf8p840))


>Troubleshoot Azure VPN Gateway using diagnostic logs
>Using diagnostic logs, you can troubleshoot multiple VPN gateway related events including configuration activity, VPN Tunnel connectivity, IPsec logging, BGP route exchanges, Point to Site advanced logging.
>There are several diagnostic logs you can use to help troubleshoot a problem with your VPN Gateway.
>• **GatewayDiagnosticLog** - Contains diagnostic logs for gateway configuration events, primary changes, and maintenance events.
>• **TunnelDiagnosticLog** - Contains tunnel state change events. Tunnel connect/disconnect events have a summarized reason for the state change if applicable.
>• **RouteDiagnosticLog** - Logs changes to static routes and BGP events that occur on the gateway.
>• **IKEDiagnosticLog** - Logs IKE control messages and events on the gateway.
>• **P2SDiagnosticLog** - Logs point-to-site control messages and events on the gateway.
>Use Azure Monitor to analyze the data collected in the diagnostic logs. ([View Highlight] (https://read.readwise.io/read/01hx5nxgtjkyn5vqvxtxnctbzj))


