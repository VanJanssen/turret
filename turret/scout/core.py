# -*- coding: utf-8 -*-

"""Utilities to perform reconnaissance on remote targets."""


def recon(arguments):
    from turret.raw.nmap.nmap import scan
    scan(arguments)
