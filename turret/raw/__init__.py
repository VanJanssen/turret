# -*- coding: utf-8 -*-

"""Raw components of Turret.

To perform its tasks, Turret uses various external tools. For example,
instead of implementing its own network scanner, Turret leverages the power
of the highly advanced Nmap. Turret invokes this tool with various preset
arguments, parses its output and acts upon that. This module contains the
wrappers around these tools, as used internally by Turret. However, these
wrapper can also be used by other users, as Turret exposes this as part of its
API, and a dedicated CLI command is available for every tool.
"""
