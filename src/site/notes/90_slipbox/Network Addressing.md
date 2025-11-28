---
{"dg-publish":true,"permalink":"/90-slipbox/network-addressing/","tags":["notes"]}
---


## IPv4

An IPv4 address is 32 **bit** address made up of 4 **Octets**, being the values in-between each `.`  
Each Octet can not have a total value higher than `255`, which is due to each Octet containing 8 **bits**.

### Binary Notation

**110000.10101000.00000001.00101101** = **192.168.1.45**

Run the Binary Number through the **Positional Notation Method**.  
It may be easier to read from right to left, as each Position is doubled.

> 110000

| 8th bit (128) | 7th bit (64) | 6th bit (32) | 5th bit (16) | 4th bit (8) | 3th bit (4) | 2th bit (2) | 1th bit (1) |     |
| ------------- | ------------ | ------------ | ------------ | ----------- | ----------- | ----------- | ----------- | --- |
| 1             | 1            | 0            | 0            | 0           | 0           | 0           | 0           |     |

**110000**: 64 + 128 = 192  
**10101000**: 8 + 32 + 12 = 168  
**00000001**: 1  
**00101101**: 1 + 4 + 8 + 32 = 45

## Subnetting

Subnetting is used to subdivide a Network Address Space, and allocate for use. The typical ways of conveying this information is a Subnet Mask and CIDR Notation.  
The job of a Subnet Mask and CIDR Notation is to simplify the conveying of Binary to being Human Readable.

### What is a Subnet Mask

**255.255.255.0** = **192.168.1**.0  
**11111111.11111111.11111111**.00000000

A Subnet mask is used to Reserve Bits on your Address space.  
The total value for each Octet can not be more than `255`. When declaring a Subnet mask, you are allocating how many Bits you are reserving for the Subnet.

### What is CIDR Notation

192.168.1.0 **/16**  
**1000000.10101000**.00000001.00000000  
Classless Inter-Domain Routing (CIDR) is another notation method for allocating IP Addresses to a Subnet.

/16 means you are reserving 16 Bits to be used in the Subnet. This means you are reserving the first **16** bits of network.

### Converting CIDR Notation to Subnet Mask Using Binary Notation

Subnet Mask = 255.255.224.0  
CIDR Notation = /19  
Binary Notation = 11111111.11111111.11100000.00000000

> 255

| 8th bit (128) | 7th bit (64) | 6th bit (32) | 5th bit (16) | 4th bit (8) | 3th bit (4) | 2th bit (2) | 1th bit (1) |
| ---           | ---          | ---          | ---          | ---         | ---         | ---         | ---         |
| 1             | 1            | 1            | 1            | 1           | 1           | 1           | 1           |  

> 255

| 8th bit (128) | 7th bit (64) | 6th bit (32) | 5th bit (16) | 4th bit (8) | 3th bit (4) | 2th bit (2) | 1th bit (1) |
| ---           | ---          | ---          | ---          | ---         | ---         | ---         | ---         |
| 1             | 1            | 1            | 1            | 1           | 1           | 1           | 1           |

> 224

| 8th bit (128) | 7th bit (64) | 6th bit (32) | 5th bit (16) | 4th bit (8) | 3th bit (4) | 2th bit (2) | 1th bit (1) |
| ---           | ---          | ---          | ---          | ---         | ---         | ---         | ---         |
| 1             | 1            | 0            | 0            | 0           | 0           | 0           | 0           |

> 0  

| 8th bit (128) | 7th bit (64) | 6th bit (32) | 5th bit (16) | 4th bit (8) | 3th bit (4) | 2th bit (2) | 1th bit (1) |
| ---           | ---          | ---          | ---          | ---         | ---         | ---         | ---         |
| 0             | 0            | 0            | 0            | 0           | 0           | 0           | 0           |
