---
{"dg-publish":true,"permalink":"/90-slipbox/azure/","tags":["mocs"],"created":"2026-03-27T09:57:51.512+10:30","updated":"2026-03-27T09:57:51.512+10:30","dg-note-properties":{"created":"2023-03-22","modified":"2026-03-03","tags":"mocs","orgs":["[[Microsoft]]"]}}
---



```base
filters:
  and:
    - file.hasLink(this)
views:
  - type: table
    name: All
    groupBy:
      property: file.tags
      direction: DESC
    order:
      - file.name
      - tags
      - related
    sort:
      - property: tags
        direction: ASC
  - type: table
    name: Meetings
    filters:
      and:
        - file.tags.contains("meetings")
    groupBy:
      property: file.tags
      direction: DESC
    order:
      - file.name
      - people
      - orgs
      - related
    columnSize:
      note.tags: 126
  - type: table
    name: Workbooks
    filters:
      and:
        - file.tags.contains("workbooks")
    order:
      - file.name
      - archived

```


## Additional Links

- [AzAdvertizer](https://www.azadvertizer.net/index.html)
