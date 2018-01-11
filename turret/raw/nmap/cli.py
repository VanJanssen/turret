# -*- coding: utf-8 -*-

"""Command line interface for the Raw Nmap command."""

import sys

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


@click.command(context_settings=dict(
    ignore_unknown_options=True,
))
@click.argument('arguments', nargs=-1, type=click.UNPROCESSED)
def nmap(arguments):
    """Perform Nmap scans."""
    from turret.raw.nmap.nmap import scan
    try:
        scan(arguments)
    except OSError:
        click.echo(not_installed_message(['nmap']), err=True)
        sys.exit(1)
