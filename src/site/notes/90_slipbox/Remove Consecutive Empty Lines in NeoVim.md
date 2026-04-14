---
{"dg-publish":true,"permalink":"/90-slipbox/remove-consecutive-empty-lines-in-neo-vim/","tags":["how-tos"],"created":"2026-04-10T16:48:17.337+09:30","updated":"2026-04-10T16:48:50.364+09:30","dg-note-properties":{"tags":"how-tos","related":["[[NeoVim]]","[[Search and Replace in NeoVim]]"],"created":"2026-04-10","modified":"2026-04-10"}}
---


## Problem

Condense multiple consecutive empty lines into single empty lines:

## Solutions

### Solution 1

```vim
:%s/\n\n\zs\n\+//g
```

**Breakdown:**
- `\n\n` - Match two newlines (one empty line)
- `\zs` - Zero-width start match (only delete what follows)
- `\n\+` - Match additional newlines
- Result: Keeps one empty line, removes extras
