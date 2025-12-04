---
{"dg-publish":true,"dg-path":"Slipbox Notes/Rsync.md","permalink":"/slipbox-notes/rsync/","tags":["notes"],"created":"2025-08-12","updated":"2025-11-28"}
---


## Basic Command

```bash
rsync -avzP --partial --inplace user@source-ip:/source/path/ /dest/path/
```

- Incremental by default (only transfers changes)
- Resumable transfers
- Network efficient with compression
- Perfect for repeated migrations

## Setup Notes

- Configure SSH keys for passwordless access
- Use `--dry-run` to test first
- Add `--bwlimit=10000` to limit bandwidth if needed

## Key Flags

- `-a` archive (preserves permissions/timestamps)
- `-v` verbose
- `-z` compress during transfer
- `-P` progress + keep partial files

### --partial

Keeps partially transferred files when interrupted. Without this flag, rsync deletes incomplete temp files and restarts from 0%. With --partial, interrupted transfers resume from where they left off.

### --inplace

Updates destination files directly instead of using temp files. Saves disk space (no 2x storage needed) and enables better resume capability, but files can be corrupted if transfer is interrupted. Trade-off: efficiency vs safety.
