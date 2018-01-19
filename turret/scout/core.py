# -*- coding: utf-8 -*-

"""Utilities to perform reconnaissance on remote targets."""


def recon(targets, mode):
    """Perform reconnaissance on specified targets.

    High level function that will perform reconnaissance on the targets with
    the specified mode. This mode can be 'quick', 'intens', 'slow' or
    'stealth'. Based on the configuration, recon will perform various tasks and
    also call other tools in order to provide as much information as possible
    about the targets.
    """
    raise NotImplementedError('recon: {} {}'.format(targets, mode))
