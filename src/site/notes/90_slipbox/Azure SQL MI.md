---
{"dg-publish":true,"permalink":"/90-slipbox/azure-sql-mi/","tags":["notes"],"created":"2026-03-27T09:57:51.498+10:30","updated":"2026-06-11T09:30:38.359+09:30","dg-note-properties":{"created":"2023-04-19","modified":"2026-06-11","references":null,"related":["[[90_slipbox/Azure\|Azure]]"],"tags":"notes"}}
---


Azure SQL MI is a middle ground [[SQL\|SQL]] deployment that is close to a full on prem deployment of SQL, but is not a true SaaS like [[Azure SQL\|Azure SQL]]

> [!warning]  
> Deploy time is *extreme* for this service, taking 4-6 hours

## Troubleshooting

### Cant Connect

- check if NSG has rule allowing port 3442
- Check that route table does not have a 0.0.0.0/0 route

---

Links: [[90_slipbox/Azure\|Azure]]  
Tags:  
Reference:
