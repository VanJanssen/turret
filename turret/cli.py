# -*- coding: utf-8 -*-

"""Console script for turret."""

import click


@click.group()
@click.version_option(message='Turret %(version)s')
def main():
    """Main console script for turret."""
    pass


@main.command()
@click.argument('arguments', nargs=-1, required=True)
def scout(arguments):
    """Perform reconnaissance."""
    from turret import scout
    scout.recon(arguments)


@main.group()
def raw():
    """
    Directly call supported tools.

    Invoke supported tools with your specified arguments and options. Turret
    extends the functionality of each supported tool by adding additional
    options. Check the help page for each supported tool to find out which
    options are added, by running 'turret raw [TOOL] --help'.
    """
    pass


@raw.command(context_settings=dict(
    ignore_unknown_options=True,
))
@click.argument('arguments', nargs=-1, type=click.UNPROCESSED)
def nmap(arguments):
    """Perform Nmap scans."""
    from turret.scout.nmap import scan
    scan(arguments)
