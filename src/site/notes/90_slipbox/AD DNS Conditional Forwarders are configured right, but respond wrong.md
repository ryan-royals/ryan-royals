---
{"dg-publish":true,"permalink":"/90-slipbox/ad-dns-conditional-forwarders-are-configured-right-but-respond-wrong/","tags":["today-i-learns"],"created":"2026-05-29T14:13:45.148+09:30","updated":"2026-05-29T14:28:55.765+09:30","dg-note-properties":{"tags":"today-i-learns","related":["[[Active Directory]]"],"created":"2026-05-29","modified":"2026-05-29"}}
---


Try resolving the dns from another machine. Its counter intuitive, but I have found that when you lookup the dns on itself, it does not respect the forwarder and will instead give you the public address.
