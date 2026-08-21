# CLI Tree

`ChatMath` is currently a root-only CLI. This page must stay synchronized from the real `chatmath --tree` output and must not invent future commands.

```text
chatmath
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## Current Status

| Entry | Status | Notes |
| --- | --- | --- |
| `chatmath --help` | Implemented | Shows root command help. |
| `chatmath --version` | Implemented | Shows the installed package version. |
| `chatmath --tree` | Implemented | Shows the current real CLI tree with parameter signatures. |
| `chatmath --tree-brief` | Implemented | Shows the same command nodes and descriptions without parameter signatures. |
| Mathematics tooling subcommands | Not implemented | Add them only after real mathematics tooling capability exists. |

## Update Rule

When real commands are added, update the Click registration and tests first, then run `chatmath --tree` and `chatmath --tree-brief` to refresh README and this page. ChatStyle's `add_tree_option()` owns both tree flags; do not add a package-local renderer.
