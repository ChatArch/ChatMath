from pathlib import Path

from click.testing import CliRunner

from chatmath import __version__
from chatmath.cli import main


ROOT = Path(__file__).resolve().parents[1]
TREE_OUTPUT = (
    "chatmath\n"
    "├── --help  # Show this message and exit.\n"
    "├── --version  # Show the version and exit.\n"
    "├── --tree  # Print the registered CLI tree and exit.\n"
    "└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.\n"
)


def test_help_lists_shared_tree_options():
    result = CliRunner().invoke(main, ["--help"])

    assert result.exit_code == 0
    assert "--tree" in result.output
    assert "--tree-brief" in result.output


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert f"chatmath, version {__version__}" in result.output


def test_tree_reports_registered_root_only_surface():
    result = CliRunner().invoke(main, ["--tree"])

    assert result.exit_code == 0
    assert result.output == TREE_OUTPUT


def test_tree_brief_reports_same_root_only_surface():
    result = CliRunner().invoke(main, ["--tree-brief"])

    assert result.exit_code == 0
    assert result.output == TREE_OUTPUT


def test_documented_tree_matches_registered_surface():
    fenced_tree = f"```text\n{TREE_OUTPUT}```"

    for relative_path in (
        "README.md",
        "README.en.md",
        "docs/cli-tree.md",
        "docs/cli-tree.en.md",
    ):
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        assert fenced_tree in text, relative_path
