---
{"dg-publish":true,"permalink":"/90-slipbox/importing-cloudflare-dns-to-terraform/","tags":["how-tos"],"created":"2026-02-24T09:36:06.170+10:30","updated":"2026-03-03T09:55:32.292+10:30","dg-note-properties":{"tags":"how-tos","related":["[[Cloudflare]]","[[Terraform]]"],"created":"2026-02-24","modified":"2026-03-03"}}
---


## Problem

To import CloudFlare DNS entries into Terraform, you need access to each DNS Entries dns_record_id, which is not presented in the web portal.

```bash
$ terraform import cloudflare_dns_record.example '<zone_id>/<dns_record_id>'
```

## Solutions

### Cf-terraforming

Cloudflare offer a tool called **cf-terraforming**[^1] which can be used to generate the import blocks based on the current state, and get their IDs.

### API

You can get the `dns_record_id` using a curl against the api.[^2]

[^1]: <https://developers.cloudflare.com/terraform/advanced-topics/import-cloudflare-resources/>

[^2]: <https://developers.cloudflare.com/api/resources/dns/subresources/records/methods/list/>
