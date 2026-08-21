<div align="center">
    <a href="https://pypi.python.org/pypi/ChatMath">
        <img src="https://img.shields.io/pypi/v/ChatMath.svg" alt="PyPI version" />
    </a>
    <a href="https://github.com/ChatArch/ChatMath/actions/workflows/ci.yml">
        <img src="https://github.com/ChatArch/ChatMath/actions/workflows/ci.yml/badge.svg" alt="Tests" />
    </a>
    <a href="https://arch.gh.wzhecnu.cn/ChatMath/">
        <img src="https://img.shields.io/badge/docs-mkdocs-blue.svg" alt="Documentation" />
    </a>
</div>

<div align="center">

[English](README.en.md) | [简体中文](README.md)
</div>

# ChatMath

ChatMath is the ChatArch mathematics tooling package entrypoint. The package currently keeps a root-only CLI plus a ChatEnv configuration discovery entry point; real mathematics tooling subcommands are not exposed yet.

## Quick Start

```bash
pip install ChatMath
chatmath --help
chatmath --version
chatmath --tree
chatmath --tree-brief
```

## Current CLI Tree

```text
chatmath
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## CLI Contract

ChatMath currently keeps a root-only CLI plus a ChatEnv configuration discovery entry point. ChatStyle's `add_tree_option()` generates `--tree` and `--tree-brief` from the real Click registry; the full tree keeps parameter signatures and the brief tree omits them. When real interactive commands are added, continue using ChatStyle's `CommandSchema` / `CommandField`, `add_interactive_option()`, and `resolve_command_inputs()`; until then, do not expose scaffold/demo subcommands.

## Layout

- `src/`: package source code
- `tests/code-tests/`: code tests and migrated historical tests
- `tests/cli-tests/`: real CLI tests, doc-first
- `tests/mock-cli-tests/`: mock/fake CLI tests, doc-first
- `docs/`: long-lived project docs built by MkDocs

## Development Notes

See `DEVELOP.md` and `AGENTS.md` before expanding the scaffold.
