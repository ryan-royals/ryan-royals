---
{"dg-publish":true,"permalink":"/90-slipbox/rip-grep/","tags":["notes"],"created":"2026-03-27T09:57:51.536+10:30","updated":"2026-04-09T15:32:43.055+09:30","dg-note-properties":{"tags":"notes","related":null,"created":"2026-02-24","modified":"2026-04-09"}}
---


Grep, but faster.  
This does not sound like it matters, but it has mattered for me plenty of times in stupid dense directories.

## Options

### -i

Makes the result just the file name. *inline*

### -0

Null terminate the file path, so it can work with xargs when there are spaces in the file name.
