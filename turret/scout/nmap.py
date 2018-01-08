# -*- coding: utf-8 -*-

"""Interface for performing Nmap scans."""

from subprocess import run


def scan(arguments):
    run(['nmap'] + list(arguments))
