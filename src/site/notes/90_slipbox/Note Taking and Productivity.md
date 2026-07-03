---
{"dg-publish":true,"permalink":"/90-slipbox/note-taking-and-productivity/","tags":["mocs"],"created":"2026-03-27T09:57:51.512+10:30","updated":"2026-06-11T09:30:38.229+09:30","dg-note-properties":{"created":"2023-03-22","modified":"2026-06-11","related":["[[Hobbies]]"],"tags":"mocs"}}
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
      - tags
      - date
      - file.name
      - related
    sort:
      - property: date
        direction: ASC
      - property: related
        direction: ASC
      - property: file.name
        direction: DESC
      - property: tags
        direction: DESC
    columnSize:
      note.tags: 88
      note.date: 105
      file.name: 234
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

