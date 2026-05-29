---
{"dg-publish":true,"permalink":"/90-slipbox/troubleshooting-conditional-forwarding-for-private-links/","tags":["notes"],"created":"2026-05-29T14:13:45.148+09:30","updated":"2026-05-29T14:20:25.252+09:30","dg-note-properties":{"tags":["notes"],"related":["[[Azure Private Link]]","[[Active Directory]]"],"created":"2026-05-29","modified":"2026-05-29"}}
---

## Can not be the `privatelink.*` address
When you are forwarding the `privatelink` subdomain, and not the actual fqdn of the resource, this fails the check in azure and you will get the public address.
This is something to do with how Azure as a platform computes the DNS in the backend, its not just a simple CNAME where you are skipping a step.

## AD DNS is configured right, but responding wrong

Try resolving the dns from another machine. Its counter intuitive, but I have found that when you lookup the dns on itself, it does not respect the forwarder and will instead give you the public address.
