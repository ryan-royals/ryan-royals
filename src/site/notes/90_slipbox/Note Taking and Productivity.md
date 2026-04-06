---
{"dg-publish":true,"dg-path":"Slipbox Notes/Note Taking and Productivity.md","permalink":"/slipbox-notes/note-taking-and-productivity/","tags":["mocs"],"created":"2023-03-22","updated":"2026-03-03","dg-note-properties":{"created":"2023-03-22","modified":"2026-03-03","tags":"mocs","related":["[[Hobbies]]"]}}
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

