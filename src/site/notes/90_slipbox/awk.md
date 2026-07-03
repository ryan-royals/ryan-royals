---
{"dg-publish":true,"permalink":"/90-slipbox/awk/","tags":["notes"],"created":"2026-04-09T15:31:51.116+09:30","updated":"2026-06-11T09:30:38.147+09:30","dg-note-properties":{"created":"2026-04-09","modified":"2026-06-11","related":["[[Shell]]"],"tags":"notes"}}
---


For quick, table-based outputs like CSVs, `ps`, or any structured text where you want the header and matching results, `awk` is often your best friend. It’s concise, powerful, and easy to type once you’ve practiced:

```bash
awk 'NR==1 || /search_term/'
```

- `NR==1` catches the header.
- `/search_term/` finds your match.
- Works on standard input from a file or pipe.

## Example

```bash
ps aux | awk 'NR==1 || /malicious\.sh/'
cat file.csv | awk 'NR==1 || /error/'
```

## Alias

```bash
alias search_with_header="awk 'NR==1 || /$1/'"
```
