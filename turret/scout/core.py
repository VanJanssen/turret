# -*- coding: utf-8 -*-

"""Utilities to perform reconnaissance on remote targets."""

from subprocess import run
from shlex import split


def recon(arguments):
    run(split('nmap ' + arguments))
