# -*- coding: utf-8 -*-

"""Command line interface for the Raw component."""

import click


from turret.raw.nmap.cli import nmap


@click.group()
def raw():
    """
    Directly call supported tools.

    Invoke supported tools with your specified arguments and options. Turret
    extends the functionality of each supported tool by adding additional
    options. Check the help page for each supported tool to find out which
    options are added, by running 'turret raw [TOOL] --help'.
    """
    pass


raw.add_command(nmap)
