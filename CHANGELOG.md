# Changelog

## 2026-08-22 - 0.1.2

### Added

- Added `chatmath --tree-brief` and installed-console-script CI coverage across Python 3.10-3.12.

### Changed

- Replaced the package-local tree renderer with ChatStyle's registered Click tree runtime.
- Aligned runtime bounds to `chatstyle>=0.2.0,<0.3.0` and `chatenv>=0.2.10,<0.3.0`.
- Synchronized bilingual CLI tree documentation and tightened the MkDocs Material compatibility bound.

## 2026-08-12 - 0.1.1

### Added

- Added real root-only `chatmath --tree` generated from the Click command surface.
- Added bilingual CLI tree docs and workflow/docs contract tests.

### Changed

- Removed unused direct ChatStyle runtime dependency while preserving the ChatEnv provider entry point.
- Switched docs URLs to the ChatArch custom docs domain and enabled MkDocs Material emoji rendering.
- Hardened tag-only OIDC publish and PR preview-doc workflows.

## 2026-07-01 - 0.1.0

### Added

- Initial ChatMath package scaffold with `chatmath` CLI.
- ChatEnv provider entry point for `chatmath` configuration discovery.
- CI and tag-driven Trusted Publisher workflow scaffold.
