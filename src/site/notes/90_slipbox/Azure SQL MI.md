---
{"dg-publish":true,"permalink":"/90-slipbox/azure-sql-mi/","tags":["notes"]}
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
