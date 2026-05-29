---
{"dg-publish":true,"permalink":"/90-slipbox/conditional-forwarding-in-ad-dns-can-not-be-privatelink-subdomain/","tags":["today-i-learns"],"created":"2026-05-29T14:27:28.769+09:30","updated":"2026-05-29T14:29:06.654+09:30","dg-note-properties":{"tags":"today-i-learns","related":["[[Active Directory]]","[[Azure Private Link]]"],"created":"2026-05-29","modified":"2026-05-29"}}
---


When you are forwarding the `privatelink` subdomain, and not the actual fqdn of the resource, this fails the check in azure and you will get the public address.  
This is something to do with how Azure as a platform computes the DNS in the backend, its not just a simple CNAME where you are skipping a step.
