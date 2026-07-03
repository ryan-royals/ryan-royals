---
{"dg-publish":true,"permalink":"/90-slipbox/git/","tags":["notes"],"created":"2026-03-27T09:57:51.532+10:30","updated":"2026-06-11T09:30:38.297+09:30","dg-note-properties":{"aliases":"Git Tips","created":"2023-06-05","modified":"2026-06-11","related":["[[Programming]]"],"tags":"notes"}}
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

