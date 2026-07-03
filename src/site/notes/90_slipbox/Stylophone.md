---
{"dg-publish":true,"permalink":"/90-slipbox/stylophone/","tags":["notes"],"created":"2026-06-15T09:34:52.618+09:30","updated":"2026-06-25T16:01:00.717+09:30","dg-note-properties":{"created":"2026-06-12","modified":"2026-06-25","related":null,"tags":"notes"}}
---


[![Comment Image](https://preview.redd.it/i-need-tabs-for-stylophone-gen-x-2-v0-u6bbeifwhq7g1.png?width=1080&format=png&auto=webp&s=309fa0f3d72bafcf362cf23b0cb85fa7833cc65d)](https://preview.redd.it/i-need-tabs-for-stylophone-gen-x-2-v0-u6bbeifwhq7g1.png?width=1080&format=png&auto=webp&s=309fa0f3d72bafcf362cf23b0cb85fa7833cc65d)

If you want to convert S-1 tabs to Gen X-2, you can use the numbering in the picture and convert by this rule: Check if there is any number lower than 3 (1 or 2)? If YES: Add 5 to all numbers. If NO (all numbers are 3 or higher): Subtract 2 from all numbers. Also it is a monophonic synthesizer, so you can't play chords.


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

