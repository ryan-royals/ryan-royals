---
{"dg-publish":true,"permalink":"/90-slipbox/azure-dns-does-not-support-cname-flattening-on-apex/","tags":["today-i-learns"],"created":"2026-04-09T15:14:12.913+09:30","updated":"2026-04-09T15:18:08.751+09:30","dg-note-properties":{"tags":"today-i-learns","related":["[[Azure Public DNS Zone]]","[[DNS]]"],"created":"2026-04-09","modified":"2026-04-09"}}
---


In Azure DNS, you can not configure `CNAME` on the apex (`ryanroyals.cloud`), it can only be a `A` record.  
With the use of [[90_slipbox/Azure Traffic Manager\|Azure Traffic Manager]], you can make this work but as a paid service.  
[[Cloudflare\|Cloudflare]] does support this out of the box.
