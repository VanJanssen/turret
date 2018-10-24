# -*- coding: utf-8 -*-

"""Command line interface for the Scout component."""

import click


@click.command()
@click.argument('targets', nargs=-1, required=True)
@click.option(
    '--mode',
    default='intens',
    type=click.Choice(['intens', 'quick', 'slow', 'stealth']),
)
def scout(targets, mode):
    """Perform reconnaissance."""
    from turret.scout import recon
    recon(targets, mode=mode)
