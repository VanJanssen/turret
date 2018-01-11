# -*- coding: utf-8 -*-

"""
Entry point for the command line interface of Turret.

The command line interface is split across multiple files, to increase
modulairity and maintainability. Every component of Turret has its own
subcommand, the CLI for this is in the `cli.py` file of this component. This
file imports the subcommands for those components and adds them to the main
group.
"""


import click

from turret.raw.cli import raw
from turret.scout.cli import scout


@click.group()
@click.version_option(message='Turret %(version)s')
def main():
    """Main entry point for the Turret CLI."""
    pass


main.add_command(scout)
main.add_command(raw)
