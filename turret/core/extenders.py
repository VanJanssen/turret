# -*- coding: utf-8 -*-

"""Utilities to extend Turret functionality."""

import subprocess
from typing import Any, Dict, List, Optional


class CompletedProgram():
    """Returnvalue of Program.run, representing a program that has finished.

    This class is a wrapper around CompletedProcess. It keeps the 'args' and
    'returnvalue' directly accessible, and adds the option for multiple
    outputs types.
    """

    def __init__(self,
                 process: subprocess.CompletedProcess,
                 output: Optional[Dict[str, str]]=None) -> None:
        """Initialize CompletedProgram.

        Args:
            process: A CompletedProcess object returned by a call to
                subprocess.run().
            output: A dictionary of additional output types and formats
                associated with this completed program. By default, it will
                contain the 'stdout' and 'stderr' of the process (these can be
                overwritten by passing a dictionary conaining 'stdout' or
                'stderr' as keys).
        """
        self.process = process
        self.output = {
            'stdout': process.stdout,
            'stderr': process.stderr,
        }
        if output:
            self.output.update(**output)

    @property
    def args(self) -> Any:
        """Arguments of the associated CompletedProcess."""
        return self.process.args

    @property
    def returncode(self) -> int:
        """Returncode of the associated CompletedProcess."""
        return self.process.returncode


class Program():
    """Interface for executing and extending arbitrary programs.

    This class provides a way to execute an arbitrary program and to extend
    its functionality with additonal options and output formats. This base
    class adds options and features which are supported by most programs. More
    complex extentsion can be provided through subclasses.
    """

    def __init__(self,
                 executable: str,
                 arguments: Optional[List[str]] = None,
                 *,
                 show_help: bool = False,
                 help_option: str = '--help',
                 show_version: bool = False,
                 version_option: str = '--version') -> None:
        """Initialize basic Program objects.

        The only required parameter is the executable name. Additional
        arguments can be directly provided, but they can also be added later
        or with the use of options. Some basic options, which are supported by
        most programs, are included in this constructor.

        Args:
            executable: Name of the program to execute. It will be passed
                directly to the subprocess call, so it can be a str, bytes or
                os.PathLike object.
            arguments: List of additonal arguments that will be directly
                passed to the subprocess call.
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
        self.arguments = arguments if arguments is not None else list()
        self.show_help = show_help
        self.help_option = help_option
        self.show_version = show_version
        self.version_option = version_option

    def run(self) -> CompletedProgram:
        """Run the program with the constructed command."""
        return CompletedProgram(subprocess.run(self.command))

    @property
    def command(self) -> List[str]:
        """Construct the command to be executed.

        This read-only property constructs the command based on the executable,
        arguments and additonal options provided. Subclasses that implement
        this, should start with '_command = super().command'. This takes care
        of the basic options.

        Returns:
            A list which can be passed to the subprocess module. The first
            element is the 'executable', followed by the 'arguments'.
            Additional values are appended based on the enabled options.

        """
        _command = [self.executable] + self.arguments

        if self.show_help:
            _command.append(self.help_option)

        if self.show_version:
            _command.append(self.version_option)

        return _command
