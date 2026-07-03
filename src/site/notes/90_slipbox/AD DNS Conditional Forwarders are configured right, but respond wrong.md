---
{"dg-publish":true,"permalink":"/90-slipbox/ad-dns-conditional-forwarders-are-configured-right-but-respond-wrong/","tags":["today-i-learns"],"created":"2026-05-29T14:13:45.148+09:30","updated":"2026-06-11T09:30:38.401+09:30","dg-note-properties":{"created":"2026-05-29","modified":"2026-06-11","related":["[[Active Directory]]"],"tags":"today-i-learns"}}
---


Try resolving the dns from another machine. Its counter intuitive, but I have found that when you lookup the dns on itself, it does not respect the forwarder and will instead give you the public address.
