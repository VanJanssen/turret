# -*- coding: utf-8 -*-

"""Utilities to extend Turret functionality."""

import subprocess


class Program():
    """Interface for executing and extending arbitrary programs.

    This class provides a way to execute an arbitrary program and to extend
    its functionality with additonal options and output formats.
    """

    def __init__(self, executable, arguments=list(), *,
                 show_help=False,
                 help_option='--help',
                 show_version=False,
                 version_option='--version'):
        """Basic boilerplate for Program object creation.

        The only required parameter is the eversionxecutable name. Additional
        arguments can be directly provided, but they can also be added later
        or with the use of options. Some basic options, which are supported by
        most programs, are included in this constructor.

        Args:
            executable: Name of the program to execute. It will be passed
                directly to the subprocess call, so it can be a str, bytes or
                os.PathLike object.
            arguments (list): List of additonal arguments that will be directly
                passed to the subprocess call. No additonal checking will be
                performed, except that it will be converted to a list if it is
                not already one.
            show_help (bool): Boolean to indicate if the program should show
                its help message. This will append the value of 'help_option'
                to the command when executing the program.
            help_option (str): The option to pass to the program in order for
                it to display the help message. Defaults to '--help'.
            show_version (bool): Boolean to indicate if the version should
                show its version information. This will append the value of
                'version_option' to the command when executing the program.
            version_option (str): The option to pass to the program in order
                for it to display the version message. Defaults to '--version'.
        """
        self.executable = executable
        self.arguments = arguments
        self.show_help = show_help
        self.help_option = help_option
        self.show_version = show_version
        self.version_option = version_option

    def run(self):
        return subprocess.run(self.command)

    @property
    def command(self):
        """Constructs the command based on the executable, arguments and
        additonal options provided."""
        _command = [self.executable] + self.arguments

        if self.show_help:
            _command += [self.help_option]

        if self.show_version:
            _command += [self.version_option]

        return _command
