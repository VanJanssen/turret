# -*- coding: utf-8 -*-

"""Interface for performing Nmap scans."""

try:
    from subprocess import run
except ImportError:
    from subprocess import call as run


def scan(arguments):
    run(['nmap'] + list(arguments))
