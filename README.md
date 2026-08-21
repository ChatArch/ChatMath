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

[英文版](README.en.md) | [简体中文](README.md)
</div>

# ChatMath

ChatMath 是 ChatArch 的 mathematics tooling 包入口。当前包保持 root-only CLI 和 ChatEnv 配置发现入口；真实数学工具子命令尚未暴露。

## 快速开始

```bash
pip install ChatMath
chatmath --help
chatmath --version
chatmath --tree
chatmath --tree-brief
```

## 当前 CLI 树

```text
chatmath
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## CLI 规范

ChatMath 当前保留 root-only CLI 和 ChatEnv 配置发现入口。`--tree` 与 `--tree-brief` 由 ChatStyle 的 `add_tree_option()` 从真实 Click 注册面生成；前者保留参数签名，后者省略参数签名。新增交互式命令时，应继续使用 ChatStyle 的 `CommandSchema` / `CommandField`、`add_interactive_option()` 与 `resolve_command_inputs()`；没有真实交互命令前，不暴露 scaffold/demo 子命令。

## 目录结构

- `src/`：包源码
- `tests/code-tests/`：代码测试和历史测试迁移
- `tests/cli-tests/`：真实 CLI 测试，doc-first
- `tests/mock-cli-tests/`：mock/fake CLI 测试，doc-first
- `docs/`：长期维护文档，由 MkDocs 构建

## 开发说明

扩展脚手架前，先阅读 `DEVELOP.md` 和 `AGENTS.md`。
