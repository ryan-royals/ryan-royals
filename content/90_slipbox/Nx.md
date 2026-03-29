---
{"dg-publish":true,"dg-path":"Slipbox Notes/Nx.md","permalink":"/slipbox-notes/nx/","tags":["notes"],"created":"2025-10-15","updated":"2025-11-28"}
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

# Show all targets for a specific project 
nx show project <project-name> 
# See the project graph visually (opens in browser) 
nx graph 
# List all projects that have a specific target 
nx show projects --with-target build 
nx show projects --with-target test
nx show projects --with-target apply
```
