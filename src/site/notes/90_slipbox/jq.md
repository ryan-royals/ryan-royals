---
{"dg-publish":true,"permalink":"/90-slipbox/jq/","tags":["notes"],"created":"2026-04-09T10:04:59.919+09:30","updated":"2026-06-11T09:30:38.145+09:30","dg-note-properties":{"aliases":"jq tips","created":"2026-04-09","modified":"2026-06-11","related":["[[Shell]]"],"tags":"notes"}}
---


## Quick Filters

```bash
az storage account list | jq '.[]' # Show all in the top []
az storage account list | jq '.[].name' # Show all `name` in each object under the top []
az storage account list | jq '.[] | select (.name == "staccountname")' # Select the matching object with matching name
az storage account list | jq '.[] | select (.name == "staccountname") | .name, .tags, .resourceGroup, .id ' # Select the matching object with matching name, and select matching keys
```
