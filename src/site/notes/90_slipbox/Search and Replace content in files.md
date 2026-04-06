---
{"dg-publish":true,"permalink":"/90-slipbox/search-and-replace-content-in-files/","tags":["how-tos"],"created":"2026-03-27T09:57:51.534+10:30","updated":"2026-03-27T09:57:51.534+10:30","dg-note-properties":{"tags":"how-tos","related":["[[RipGrep]]","[[sed]]","[[Shell|Bash]]","[[xargs]]"],"created":"2026-02-24","modified":"2026-03-03"}}
---


## Problem

Need to edit the contents across X amount of files, down directories

## Solutions

### Easy Shell search and Replace

`rg {target} -l -0 | xargs -0 sed -i 's/{target}/{replace}/'`
