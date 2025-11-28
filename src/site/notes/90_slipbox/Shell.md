---
{"dg-publish":true,"permalink":"/90-slipbox/shell/","tags":["notes"]}
---


## Table and Filtered Content

For quick, table-based outputs like CSVs, `ps`, or any structured text where you want the header and matching results, `awk` is often your best friend. It’s concise, powerful, and easy to type once you’ve practiced:

```bash
awk 'NR==1 || /search_term/'
```

- `NR==1` catches the header.
- `/search_term/` finds your match.
- Works on standard input from a file or pipe.

### Example

```bash
ps aux | awk 'NR==1 || /malicious\.sh/'
cat file.csv | awk 'NR==1 || /error/'
```

### Alias

```bash
alias search_with_header="awk 'NR==1 || /$1/'"
```

## Find and Sort by Access Date

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

## Disk Usage with Sort

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
