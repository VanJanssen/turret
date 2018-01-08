# -*- coding: utf-8 -*-

"""Utilities to perform reconnaissance on remote targets."""


def recon(arguments):
    from turret.scout.nmap import scan
    scan(arguments)
