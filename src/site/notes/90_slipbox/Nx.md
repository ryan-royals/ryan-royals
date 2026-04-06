---
{"dg-publish":true,"permalink":"/90-slipbox/nx/","tags":["notes"],"created":"2026-03-27T09:57:51.533+10:30","updated":"2026-03-27T09:57:51.533+10:30","dg-note-properties":{"tags":"notes","related":["[[Programming]]"],"created":"2025-10-15","modified":"2026-03-03","aliases":"NX Tips"}}
---


## Quick Tips

### Initialise a New Repo

Running `npx create-nx-workspace *name*` creates a new directory with `*name*`, with npm and everything set up in there.

### Refresh / Reset NX

```bash
nx reset
```

### List Projects

```bash
# List all projects in your workspace
nx show projects

# Show project details (including targets/executors)
nx show project <project-name>

# List projects with a specific tag
nx show projects --with-target <target-name>
```

### List Generators

``` bash
# List all available generators
nx list

# Show generators for a specific plugin
nx list @arkahna-accelerate
nx list @nx/node

# Show details about a specific generator
nx g @nx/react:component --help

```

### List Executors / Targets

``` bash
# Show all Projects
nx show projects

# Show Project Tasks and Graph (Opens in browser)
nx show project <project-name> 
# See the project graph visually (opens in browser) 
nx graph 
# List all projects that have a specific target 
nx show projects --with-target build 
nx show projects --with-target test
nx show projects --with-target apply
```

### Show Affected

```shell
nx show projects --affected
```
