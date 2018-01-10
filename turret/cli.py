# -*- coding: utf-8 -*-

"""Console script for turret."""

from sys import exit

import click


def not_installed_message(applications):
    """
    Return a string message saying the applications are not installed. Takes
    a list of strings as input.
    """
    message = 'Error: Failed to perform this action, because the following ' \
              'applications are not installed, or not available in the PATH:\n'
    for application in applications:
        message += '  - {}\n'.format(application)
    return message


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
    try:
        scan(arguments)
    except OSError as e:
        click.echo(not_installed_message(['nmap']), err=True)
        exit(1)
