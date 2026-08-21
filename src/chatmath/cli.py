"""CLI entrypoint for chatmath."""

from __future__ import annotations

import click
from chatstyle import add_tree_option

from chatmath import __version__


@click.group(name="chatmath", invoke_without_command=True)
@click.version_option(__version__, prog_name="chatmath")
@add_tree_option(renderer_options={"root_name": "chatmath"})
@click.pass_context
def main(ctx: click.Context) -> None:
    """chatmath command line interface."""
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


if __name__ == "__main__":
    main()
