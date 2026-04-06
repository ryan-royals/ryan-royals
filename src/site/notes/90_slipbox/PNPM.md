---
{"dg-publish":true,"permalink":"/90-slipbox/pnpm/","tags":["notes"],"created":"2026-01-06","updated":"2026-03-03","dg-note-properties":{"created":"2026-01-06","modified":"2026-03-03","aliases":"PNPM Tips","tags":"notes","related":["[[Programming]]"],"pageId":"1669169153","spaceId":"331808774","confluenceUrl":"https://arkahna.atlassian.net/wiki/spaces/~6332438e748d1bfcb85930b7/pages/1669169153/PNPM"}}
---


## Package Discovery

### Using the `workspace:*` Constraint

*packages.json*

```json
  "devDependencies": {
    "@arkahna-elements/ark-nx-terraform": "workspace:*",
    "@arkahna-elements/ark-nx-workspace": "workspace:*",

```

Using the `workspace` constraint in combination with the `pnpm-workspace.yaml` file, you can use local packages rather than a remote source. This includes packages directories above, and ignoring sub directories.

 *pnpm-workspace.yaml*

```yaml
packages:
  - 'libs/*'
  - 'terraform/apps/*'
  - 'terraform/modules/*'
  - '../../../node_packages/*'
  - '../../modules/**'
  - '!../../**/node_modules/**
```

### Using the `npm:` Redirect

*packages.json*

```json
  "dependencies": {
    "@arkahna-elements/ark-core-gov-base": "npm:@customer/ark-core-gov-base@latest"
  }
```

Using the `npm:` tag in the version constraint allows you to remap one package to another. This includes pointing to your own forks of packages on private registries.

### Using Overrides

*pnpm-workspace.yaml*

```yaml
overrides:
  "foo": "^1.0.0"
  "quux": "npm:@myorg/quux@^1.0.0"
  "bar@^2.1.0": "3.0.0"
  "qar@1>zoo": "2"
```

Using overrides, you can override package versions for the whole repo when working in a mono-repo. This also works with dependencies of your packages.  
Be careful, as if you do not define a version in the override, it will just use the `latest` dist-tag, regardless of what any `package.json` defines.
