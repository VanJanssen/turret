# -*- coding: utf-8 -*-

"""Command line interface for the Raw Nmap command."""

import ipaddress
import sys

import click
import netifaces


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
def nmap(subnet, arguments):
    """Perform Nmap scans."""
    subnets = set()
    for interface in subnet:
        try:
            # TODO: deal with multiple addresses
            # TODO: move this to utilities
            address = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]
        except ValueError:
            raise click.BadParameter("'{}' is not a valid interface.".format(
                                     interface))
        except KeyError:
            raise click.BadParameter("'{}' has no IPv4 address.".format(
                                     interface))
        netmask = bin(int(ipaddress.ip_address(address['netmask']))).count('1')
        network = ipaddress.ip_network('{}/{}'.format(address['addr'], netmask), strict=False)  # noqa: E501
        subnets.add(str(network))
    from turret.raw.nmap.nmap import scan
    # TODO: Clean way to add multple arguments after they have been validated
    arguments += tuple(subnets)
    try:
        scan(arguments)
    except OSError:
        click.echo(not_installed_message(['nmap']), err=True)
        sys.exit(1)
