# -*- coding: utf-8 -*-

"""Console script for turret."""

import click


@click.command()
@click.version_option(message='%(prog)s %(version)s')
def main(args=None):
    """Console script for turret."""
    click.echo("Replace this message by putting your code into "
               "turret.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
