# -*- coding: utf-8 -*-

"""Utilities for use in Turret."""

import ipaddress

import netifaces


def interface_subnet(interface):
    """Given a network interface, retrieve the associated IPv4 subnet.

    Args:
        interface: Name of the interface, for example 'eth0' or wlp3s0'.
    """
    # TODO: deal with multiple addresses
    # TODO: add IPv6 support
    address = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]
    netmask = bin(int(ipaddress.ip_address(address['netmask']))).count('1')
    subnet = ipaddress.ip_network('{}/{}'.format(address['addr'], netmask), strict=False)  # noqa: E501
    return subnet
