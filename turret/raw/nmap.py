# -*- coding: utf-8 -*-

"""Raw module for Nmap.

This module provides direct access to Nmap, but also to the wrapper and
utility functions added by Turret. All functions can be access through the
API and there is a dedicated nmap CLI subcommand.
"""

import sys
from typing import List

import click

from turret.core.extenders import Program
from turret.core.util import interface_subnets


def not_installed_message(applications: List[str]) -> str:
    """Return an error message with required applications.

    Return a string message saying the applications are not installed. Takes
    a list of strings as input.
    """
    message = 'Error: Failed to perform this action, because the following ' \
              'applications are not installed, or not available in the PATH:\n'
    for application in applications:
        message += '  - {}\n'.format(application)
    return message


class Nmap(Program):
    """Interface for performing Nmap scans."""

    def __init__(self, *,
                 executable: str = 'nmap',
                 **kwargs) -> None:
        """Initialize Nmap scanner object."""
        super().__init__(executable, **kwargs)


@click.command('nmap', context_settings=dict(
    ignore_unknown_options=True,
))
@click.option(
    '--subnet',
    metavar='<interface>',
    multiple=True,
    # TODO: Also make this work for IPv6, multiple ways to do this:
    #           * If IPv6 is available: do both or prefer IPv6.
    #           * Multiple options:
    #               * --subnet-ipv4, --subnet--ipv4
    #               * --subnetv4, --subnetv6
    #           * A way to specify the IP version of this option, with a
    #             default value, something like --subnet eth0,v4
    # TODO: Is it possible that there are multiple IP address with differen
    #       subnets associated with a single interface?
    help="Appends the IPv4 subnet associated with the interface as target. "
         "Suppose the interface 'eth0' has IP address '192.168.1.60' "
         "and netmask '255.255.255.0'. The option '--iface-subnet eth0' will "
         "append the nmap command with the target '192.168.1.0/24'.")
@click.argument('arguments', nargs=-1, type=click.UNPROCESSED)
def cli(subnet, arguments):
    """Perform Nmap scans."""
    subnets = set()
    for interface in subnet:
        try:
            subnets = subnets.union(str(s) for s in interface_subnets(interface))  # noqa: 501
        except ValueError:
            raise click.BadParameter("'{}' is not a valid interface.".format(
                                     interface))
        except KeyError:
            raise click.BadParameter("'{}' has no IPv4 address.".format(
                                     interface))
    # TODO: Clean way to add multple arguments after they have been validated
    arguments += tuple(subnets)
    try:
        nmap = Nmap(arguments=list(arguments))
        nmap.run()
    except OSError:
        click.echo(not_installed_message(['nmap']), err=True)
        sys.exit(1)
