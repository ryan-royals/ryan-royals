---
{"dg-publish":true,"permalink":"/90-slipbox/shell/","tags":["notes"],"created":"2025-07-30T16:53:57.248+09:30","updated":"2026-04-09T15:38:26.432+09:30","dg-note-properties":{"tags":"notes","related":["[[Programming]]"],"aliases":["Bash","Bash Tips","Shell","Shell Tips","Zsh","Zsh Tips"],"created":"2025-07-30","modified":"2026-04-09"}}
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

