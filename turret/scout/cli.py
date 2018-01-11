# -*- coding: utf-8 -*-

"""Command line interface for the Scout component."""

import click


@click.command()
@click.argument('arguments', nargs=-1, required=True)
def scout(arguments):
    """Perform reconnaissance."""
    from turret import scout
    scout.recon(arguments)
