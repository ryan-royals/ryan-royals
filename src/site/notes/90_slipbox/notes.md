---
{"dg-publish":true,"permalink":"/90-slipbox/notes/","tags":["inbox/new"],"created":"2026-05-29T14:33:37.598+09:30","updated":"2026-05-29T14:38:27.761+09:30","dg-note-properties":{"tags":"inbox/new","related":null,"created":"2026-05-29","modified":"2026-05-29"}}
---



```base
filters:
  and:
    - file.tags.contains("notes")
views:
  - type: table
    name: Table
    order:
      - file.name
      - related
      - created
      - modified
      - dg-publish
    sort: []

```

