---
{"dg-publish":true,"permalink":"/90-slipbox/search-and-replace-content-in-files/","tags":["how-tos"],"created":"2026-02-24T20:23:48.304+10:30","updated":"2026-04-09T10:46:20.894+09:30","dg-note-properties":{"tags":"how-tos","related":["[[RipGrep]]","[[sed]]","[[Shell|Bash]]","[[xargs]]"],"created":"2026-02-24","modified":"2026-04-09"}}
---


## Problem

Need to edit the contents across X amount of files, down directories

## Solutions

### Easy Shell search and Replace

`rg {target} -l -0 | xargs -0 sed -i 's/{target}/{replace}/'`
