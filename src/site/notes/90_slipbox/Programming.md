---
{"dg-publish":true,"permalink":"/90-slipbox/programming/","tags":["mocs"],"created":"2025-12-08","updated":"2026-03-03","dg-note-properties":{"created":"2025-12-08","references":null,"tags":"mocs","related":null,"modified":"2026-03-03"}}
---


## All Linked


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
