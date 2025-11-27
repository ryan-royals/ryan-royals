---
{"dg-publish":true,"dg-path":"Slipbox Notes/Git.md","permalink":"/slipbox-notes/git/","tags":["notes"],"created":"2023-06-05","updated":"2025-11-28"}
---


Its Git!

## Handy Tools

[Oh Shit, Git!?! (ohshitgit.com)](https://ohshitgit.com/) - Get out of the shit quick tips!

## Neato Tricks

- Use `.git/info/exclude` as a local `.gitignore` that does not update the gitignore.

## Prune and Remove 'Gone' Using Git

```powershell
git fetch -p
git branch --v | ? { $_ -match "\[gone\]" } | % { -split $_ | select -First 1 } | % { git branch -D $_ }
```

```Bash
git fetch -p && git branch -vv | awk '/: gone]/{print $1}' | xargs git branch -d
```
