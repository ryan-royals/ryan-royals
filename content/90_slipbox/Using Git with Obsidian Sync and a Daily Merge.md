---
{"dg-publish":true,"dg-path":"Slipbox Notes/Using Git with Obsidian Sync and a Daily Merge.md","permalink":"/slipbox-notes/using-git-with-obsidian-sync-and-a-daily-merge/","tags":["notes"],"created":"2023-10-17","updated":"2025-11-28"}
---


## What I Learnt

This process broke pretty quickly. By the end of it, the Merge kept failing as the git history did not form a cohesive linear log.  
Stopped using Git unfortunately. Would like to bring a backup back some day.

---

## Using Git with Obsidian Sync and a Daily Merge

Using Git as a backup for Obsidian is a clean way to bulk restore files as changes occur. Obsidian Sync works very well for moving between devices most of the time, but is prone to error and can sometimes duplicate files.  
Git allows us to take constant point in time backups without having to worry about using the Obsidian Sync restore functionality.

### How to Initially Setup

1. Initialise Git at root of vault.
2. Add `.Gitignore`.
3. Push to `main` branch on remote.
4. Checkout new branch for device locally.
5. Install `Obsidian Git` Plugin.
6. Configure Plugin
7. Add pipeline to GitHub

#### Extension

The `Obisdian Git` Plugin found in the community plugins works great. The only configuration required is to set the Vault Backup intervals as required. The extension works by using a Git Repo that is initialised in the Root of the vault, and simply interacts with whatever branch you leave active on the folder.

#### .Gitignore

Since we are using Obsidian Sync, we are best to add a `.gitignore` on each branch that ignores the `.obsidian/` folder. This folder is prone to merge issues, and does not hold a large amount of information that we could not rebuild if required (In comparison to our actual notes.)

#### Branching

My preference is to have a branch for each device, as this allows for a distinct history for each device. I compliment this with a pipeline that automatically merges the branches into main daily.

#### Pipeline

A simple daily merge has been added to main to pull all branches and merge them together. Since we are using Obsidian Sync, we should rarely if at all hit merge issues.

```yaml
name: Daily Merge
on:
  workflow_dispatch:
  schedule:
    - cron: "0 0 * * *"
permissions: write-all

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: Merge all the branches
        run: |
          git --version
          git config user.name "GitHub Actions Bot"
          git config user.email "<>"
          git branch -r

          git for-each-ref --format='%(refname:short)' refs/remotes/origin | while read branch; do echo Merging $branch; sleep 3; git merge $branch; done
          echo Pushing main
          git push
```

### How to Setup a New Device with Git

1. Clone latest Main.
2. Checkout a new branch for device.
3. Open vault in Obsidian.
4. Setup up Obsidian Sync to same vault.

### How to Setup a New Device without Git

1. Open Obsidian like normal, just using the built in Obsidian Sync.
