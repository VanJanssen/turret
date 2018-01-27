# -*- coding: utf-8 -*-

"""Core functionality related to Nmap."""

from turret.core.extenders import Program


class Nmap(Program):
    """Interface for performing Nmap scans."""

    def __init__(self, *,
                 executable='nmap',
                 **kwargs):
        super().__init__(executable, **kwargs)
