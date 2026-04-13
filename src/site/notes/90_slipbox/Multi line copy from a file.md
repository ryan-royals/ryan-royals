---
{"dg-publish":true,"permalink":"/90-slipbox/multi-line-copy-from-a-file/","tags":["how-tos"],"created":"2026-03-27T09:57:51.396+10:30","updated":"2026-04-09T15:32:52.984+09:30","dg-note-properties":{"tags":"how-tos","related":["[[RipGrep]]","[[Shell|Bash]]"],"created":"2026-03-11","modified":"2026-04-09"}}
---


## Problem

I want to copy all matching lines out of a file, without having to move them about first

## Solutions

### RipGrep and Pipe to Wl-copy

```sh
rg -oP 'regex.*' file.txt | wl-copy
```

**-o**  
Print only the matching part  
**-P**  
Perl compatible regex, for things like `\S`
