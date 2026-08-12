# CLI Tree

`ChatMath` is currently a root-only CLI. This page must stay synchronized from the real `chatmath --tree` output and must not invent future commands.

```text
chatmath  # ChatArch mathematics tooling entrypoint
├── --help  # show command help
├── --version  # show the installed package version
└── --tree  # show this CLI tree
```

## Current Status

| Entry | Status | Notes |
| --- | --- | --- |
| `chatmath --help` | Implemented | Shows root command help. |
| `chatmath --version` | Implemented | Shows the installed package version. |
| `chatmath --tree` | Implemented | Shows the current real CLI tree. |
| Mathematics tooling subcommands | Not implemented | Add them only after real mathematics tooling capability exists. |

## Update Rule

When real commands are added, update the Click registration and tests first, then run `chatmath --tree` to refresh README and this page.
