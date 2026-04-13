---
{"dg-publish":true,"permalink":"/90-slipbox/find/","tags":["notes"],"created":"2026-04-09T15:36:07.367+09:30","updated":"2026-04-09T15:37:32.691+09:30","dg-note-properties":{"tags":"notes","related":["[[Shell]]"],"created":"2026-04-09","modified":"2026-04-09"}}
---


```shell
 find . -type f -printf "%T+ %p\n" | sort | tail -5
```

This command finds the 5 most recently modified files in the current directory tree:

- `find . -type f` - searches for files (not directories) starting from current directory
- `-printf "%T+ %p\n"` - prints modification timestamp + filename for each file
    -  `%T+` = ISO 8601 timestamp format
    - `%p` = file path
    - `\n` = newline
- `sort` - sorts by timestamp (oldest first)
- `tail -5` - shows last 5 entries (most recent)

Output format: `YYYY-MM-DD+HH:MM:SS.milliseconds /path/to/file`
