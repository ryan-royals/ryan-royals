---
{"dg-publish":true,"permalink":"/90-slipbox/du/","tags":["notes"],"created":"2026-04-09T15:37:04.709+09:30","updated":"2026-04-13T09:29:23.858+09:30","dg-note-properties":{"tags":"notes","related":["[[Shell]]"],"aliases":"Dish Usage","created":"2026-04-09","modified":"2026-04-13"}}
---


```shell
du -sh */ | sort -h | tail -10
```

- `du -sh */` - calculates disk usage for each directory:
    - `-s` = summarize (don't show subdirectories)
    - `-h` = human-readable format (KB, MB, GB)
    - `*/` = only directories in current path
- `sort -h` - sorts by human-readable sizes (understands K, M, G suffixes)
- `tail -10` - shows last 10 entries (largest directories)

Output format: `1.2G dirname/`
