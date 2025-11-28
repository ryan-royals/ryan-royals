---
{"dg-publish":true,"permalink":"/90-slipbox/tmux-tips/","tags":["notes"]}
---


## Tmux Essential Commands

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
