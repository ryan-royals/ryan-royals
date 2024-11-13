---
{"dg-publish":true,"permalink":"/40-references/readwise/what-is-an-azure-dns-private-zone/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png)

## Summary

Overview of a private DNS zone

## Highlights

Azure Private DNS provides a reliable, secure DNS service to manage and resolve domain names in a virtual network without the need to add a custom DNS solution ([View Highlight] (https://read.readwise.io/read/01h0efv199revzvccvem4h4ppn))


The records contained in a private DNS zone aren't resolvable from the Internet. DNS resolution against a private DNS zone works only from virtual networks that are linked to it. ([View Highlight] (https://read.readwise.io/read/01h0efv6n0hfsg57554makswv9))


Single-label private DNS zones aren't supported. Your private DNS zone must have two or more labels. For example, contoso.com has two labels separated by a dot. A private DNS zone can have a maximum of 34 labels. ([View Highlight] (https://read.readwise.io/read/01h0efvev1hsy12zkq1prgmq9h))


You can't create zone delegations (NS records) in a private DNS zone. If you intend to use a child domain, you can directly create the domain as a private DNS zone. Then you can link it to the virtual network without setting up a nameserver delegation from the parent zone. ([View Highlight] (https://read.readwise.io/read/01h0efvnr7xe7ffc1wpjhrbjvk))


Private DNS zones linked to a VNet are queried first when using the default DNS settings of a VNet. Azure provided DNS servers are queried next. However, if a [custom DNS server](https://learn.microsoft.com/en-us/azure/dns/private-dns-privatednszone/../virtual-network/manage-virtual-network#change-dns-servers) is defined in a VNet, then private DNS zones linked to that VNet are not automatically queried, because the custom settings override the name resolution order. ([View Highlight] (https://read.readwise.io/read/01hww196vvxp47qwzebzd7nde0))


