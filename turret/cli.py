# -*- coding: utf-8 -*-

"""Console script for turret."""

import click


@click.group()
@click.version_option(message='%(prog)s %(version)s')
def main():
    """Main console script for turret."""
    pass


@main.command()
@click.argument('arguments', nargs=-1, required=True)
def scout(arguments):
    """Perform reconnaissance."""
    from turret import scout
    scout.recon(arguments)
