---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/what-is-ip-address-168-63-129-16/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png)

#### In this article

1. [Scope of IP address 168.63.129.16](https://learn.microsoft.com/en-us/azure/virtual-network/what-is-ip-address-168-63-129-16#scope-of-ip-address-1686312916)
2. [Troubleshoot connectivity](https://learn.microsoft.com/en-us/azure/virtual-network/what-is-ip-address-168-63-129-16#troubleshoot-connectivity)
3. [Next steps](https://learn.microsoft.com/en-us/azure/virtual-network/what-is-ip-address-168-63-129-16#next-steps)

IP address 168.63.129.16 is a virtual public IP address that is used to facilitate a communication channel to Azure platform resources. Customers can define any address space for their private virtual network in Azure. Therefore, the Azure platform resources must be presented as a unique public IP address. This virtual public IP address facilitates the following operations:

* Enables the VM Agent to communicate with the Azure platform to signal that it is in a "Ready" state.
* Enables communication with the DNS virtual server to provide filtered name resolution to the resources (such as VM) that don't have a custom DNS server. This filtering makes sure that customers can resolve only the hostnames of their resources.
* Enables [health probes from Azure Load Balancer](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-custom-probe-overview) to determine the health state of VMs.
* Enables the VM to obtain a dynamic IP address from the DHCP service in Azure.
* Enables Guest Agent heartbeat messages for the PaaS role.

Note

In a non-virtual network scenario (Classic), a private IP address is used instead of 168.63.129.16. This private IP address is dynamically discovered through DHCP. Firewall rules specific to 168.63.129.16 need to be adjusted as appropriate.

#### Scope of IP address 168.63.129.16

The public IP address 168.63.129.16 is used in all regions and all national clouds. Microsoft owns this special public IP address and it doesn't change. We recommend that you allow this IP address in any local (in the VM) firewall policies (outbound direction). The communication between this special IP address and the resources is safe because only the internal Azure platform can source a message from this IP address. If this address is blocked, unexpected behavior can occur in various scenarios. 168.63.129.16 is a [virtual IP of the host node](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview#azure-platform-considerations) and as such it isn't subject to user defined routes.

* The VM Agent requires outbound communication over ports 80/tcp and 32526/tcp with WireServer (168.63.129.16). These ports should be open in the local firewall on the VM. The communication on these ports with 168.63.129.16 isn't subject to the configured network security groups.
* 168.63.129.16 can provide DNS services to the VM. If DNS services provided by 168.63.129.16 isn't desired, outbound traffic to 168.63.129.16 ports 53/udp and 53/tcp can be blocked in the local firewall on the VM.

 By default DNS communication isn't subject to the configured network security groups unless targeted using the [AzurePlatformDNS](https://learn.microsoft.com/en-us/azure/virtual-network/service-tags-overview#available-service-tags) service tag. To block DNS traffic to Azure DNS through NSG, create an outbound rule to deny traffic to [AzurePlatformDNS](https://learn.microsoft.com/en-us/azure/virtual-network/service-tags-overview#available-service-tags). Specify **"Any"** as **"Source"**, **"\*"** as **"Destination port ranges"**, **"Any"** as protocol and **"Deny"** as action.
* When the VM is part of a load balancer backend pool, [health probe](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-custom-probe-overview) communication should be allowed to originate from 168.63.129.16. The default network security group configuration has a rule that allows this communication. This rule uses the [AzureLoadBalancer](https://learn.microsoft.com/en-us/azure/virtual-network/service-tags-overview#available-service-tags) service tag. If desired, this traffic can be blocked by configuring the network security group. The configuration of the block result in probes that fail.

#### Troubleshoot connectivity

Note

When running the following tests, the action must be run as Administrator (Windows) and Root (Linux) to ensure accurate results.

##### Windows OS

You can test communication to 168.63.129.16 by using the following tests with PowerShell.

PowerShell 

```
Test-NetConnection -ComputerName 168.63.129.16 -Port 80
Test-NetConnection -ComputerName 168.63.129.16 -Port 32526
Invoke-RestMethod -Headers @{"Metadata"="true"} -Method GET -Uri http://168.63.129.16/?comp=versions

```

Results should return as follows.

PowerShell 

```
Test-NetConnection -ComputerName 168.63.129.16 -Port 80
ComputerName     : 168.63.129.16
RemoteAddress    : 168.63.129.16
RemotePort       : 80
InterfaceAlias   : Ethernet
SourceAddress    : 10.0.0.4
TcpTestSucceeded : True

```

PowerShell 

```
Test-NetConnection -ComputerName 168.63.129.16 -Port 32526
ComputerName     : 168.63.129.16
RemoteAddress    : 168.63.129.16
RemotePort       : 32526
InterfaceAlias   : Ethernet
SourceAddress    : 10.0.0.4
TcpTestSucceeded : True

```

PowerShell 

```
Invoke-RestMethod -Headers @{"Metadata"="true"} -Method GET -Uri http://168.63.129.16/?comp=versions
xml                            Versions
---                            --------
version="1.0" encoding="utf-8" Versions

```

You can also test communication to 168.63.129.16 by using `telnet` or `psping`.

If successful, telnet should connect and the file that is created is empty.

PowerShell 

```
telnet 168.63.129.16 80 >> C:\<<EDIT-DIRECTORY>>\168-63-129-16_test-port80.txt
telnet 168.63.129.16 32526 >> C:\<<EDIT-DIRECTORY>>\168-63-129-16_test--port32526.txt

```

PowerShell 

```
Psping 168.63.129.16:80 >> C:\<<EDIT-DIRECTORY>>\168-63-129-16_test--port80.txt
Psping 168.63.129.16:32526 >> C:\<<EDIT-DIRECTORY>>\168-63-129-16_test-port32526.txt

```

##### Linux OS

On Linux, you can test communication to 168.63.129.16 by using the following tests.

Bash 

```
echo "Testing 80 168.63.129.16 Port 80" > 168-63-129-16_test.txt
traceroute -T -p 80 168.63.129.16 >> 168-63-129-16_test.txt
echo "Testing 80 168.63.129.16 Port 32526" >> 168-63-129-16_test.txt
traceroute -T -p 32526 168.63.129.16 >> 168-63-129-16_test.txt
echo "Test 168.63.129.16 Versions"  >> 168-63-129-16_test.txt
curl http://168.63.129.16/?comp=versions >> 168-63-129-16_test.txt

```

Results inside 168-63-129-16\_test.txt should return as follows.

Bash 

```
traceroute -T -p 80 168.63.129.16
traceroute to 168.63.129.16 (168.63.129.16), 30 hops max, 60 byte packets
1  168.63.129.16 (168.63.129.16)  0.974 ms  1.085 ms  1.078 ms

traceroute -T -p 32526 168.63.129.16
traceroute to 168.63.129.16 (168.63.129.16), 30 hops max, 60 byte packets
1  168.63.129.16 (168.63.129.16)  0.883 ms  1.004 ms  1.010 ms

curl http://168.63.129.16/?comp=versions
<?xml version="1.0" encoding="utf-8"?>
<Versions>
<Preferred>
<Version>2015-04-05</Version>
</Preferred>
<Supported>
<Version>2015-04-05</Version>
<Version>2012-11-30</Version>
<Version>2012-09-15</Version>
<Version>2012-05-15</Version>
<Version>2011-12-31</Version>
<Version>2011-10-15</Version>
<Version>2011-08-31</Version>
<Version>2011-04-07</Version>
<Version>2010-12-15</Version>
<Version>2010-28-10</Version>
</Supported>

```

#### Next steps

* [Security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)
* [Create, change, or delete a network security group](https://learn.microsoft.com/en-us/azure/virtual-network/manage-network-security-group)
