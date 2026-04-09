---
{"dg-publish":true,"permalink":"/90-slipbox/keyboards/","tags":["mocs"],"created":"2025-06-11T10:28:48.240+09:30","updated":"2026-03-03T09:55:32.276+10:30","dg-note-properties":{"tags":"mocs","related":["[[Hobbies]]"],"created":"2025-12-08","modified":"2026-03-03"}}
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
