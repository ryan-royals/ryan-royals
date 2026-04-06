---
{"dg-publish":true,"dg-path":"Slipbox Notes/Tmux Tips.md","permalink":"/slipbox-notes/tmux-tips/","tags":["notes"],"created":"2025-08-13","updated":"2026-03-03","dg-note-properties":{"tags":"notes","created":"2025-08-13","related":["[[Shell|Shell]]"],"references":null,"aliases":"tmux","modified":"2026-03-03"}}
---


## Tmux Essential Commands

- `Ctrl+B, ?`- Show all the key commands

### Sessions

- `tmux new-session -s name` - Create named session
- `tmux attach -t name` - Attach to session
- `tmux list-sessions` - Show all sessions
- `tmux kill-session -t name` - Kill session

### Key Bindings (Default: Ctrl+B)

- `Ctrl+B, d` - Detach from session
- `Ctrl+B, c` - Create new window
- `Ctrl+B, %` - Split vertically
- `Ctrl+B, "` - Split horizontally
- `Ctrl+B, Arrow` - Switch panes
- `Ctrl+B, 0-9` - Switch to window number
- `Ctrl+B, x` - Kill current pane
- `Ctrl+B, &` - Kill current window
- `Ctrl+B, s` - Session Manager

### Remote Usage

- `ssh -t host 'tmux attach -t session'` - Direct attach via SSH
- `Ctrl+B, Ctrl+B` - Send prefix to nested tmux session

### Quick Start

```bash
tmux new-session -s work    # Start session
# Do work...
# Ctrl+B, d                # Detach
tmux attach -t work         # Reattach later
```
