# -*- coding: utf-8 -*-

"""Unit tests for the `interface_subnets` function."""

import ipaddress
import socket
from collections import namedtuple
from unittest.mock import MagicMock

import psutil
import pytest

from turret.core.util import interface_subnets

snic = namedtuple('snic', 'family address netmask')
test_net_if_addrs = {
    'enp4s0': [
        snic(
            family=socket.AF_PACKET,
            address='11:22:33:44:55:66',
            netmask=None,
        )
    ],
    'lo': [
        snic(
            family=socket.AF_INET,
            address='127.0.0.1',
            netmask='255.0.0.0',
        ),
        snic(
            family=socket.AF_INET6,
            address='::1',
            netmask='ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff',
        ),
        snic(
            family=socket.AF_PACKET,
            address='00:00:00:00:00:00',
            netmask=None,
        )
    ],
    'wlp3s0': [
        snic(
            family=socket.AF_INET,
            address='192.168.2.80',
            netmask='255.255.255.0',
        ),
        snic(
            family=socket.AF_INET6,
            address='fe80::a8bb:ccff:fedd:eeff%wlp3s0',
            netmask='ffff:ffff:ffff:ffff::',
        ),
        snic(
            family=socket.AF_PACKET,
            address='aa:11:bb:22:cc:33',
            netmask=None,
        )
    ]
}


def test_invalid_interface():
    """An invalid interface should raise a 'ValueError'."""
    psutil.net_if_addrs = MagicMock(return_value=test_net_if_addrs)
    with pytest.raises(ValueError):
        interface_subnets('invalid')


def test_valid_interface():
    """A valid interface should return the subnets of this range."""
    psutil.net_if_addrs = MagicMock(return_value=test_net_if_addrs)
    subnets = interface_subnets('wlp3s0')
    assert subnets == {ipaddress.ip_network('192.168.2.0/24'), }
