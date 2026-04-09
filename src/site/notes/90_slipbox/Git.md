---
{"dg-publish":true,"permalink":"/90-slipbox/git/","tags":["notes"],"created":"2025-06-11T10:28:48.103+09:30","updated":"2026-04-09T15:38:39.556+09:30","dg-note-properties":{"created":"2023-06-05","modified":"2026-04-09","tags":"notes","related":["[[Programming]]"],"aliases":"Git Tips"}}
---


## Handy Tools

[Oh Shit, Git!?! (ohshitgit.com)](https://ohshitgit.com/) - Get out of the shit quick tips!


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

