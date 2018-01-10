# -*- coding: utf-8 -*-

try:
    from shutil import which
except ImportError:
    from distutils.spawn import find_executable as which

from click.testing import CliRunner

from turret import cli


def test_nmap_installed():
    """
    Test if nmap installation is correctly handled.

    The behaviour of this test is dependent on whether Nmap is installed or
    not. If it is installed, assert that Nmap is executed and the output is
    piped to the stdout of Turret. If it is not installed, assert that this
    exception is handled by printing an error message and terminating the
    program, instead of printing a Python stack trace.
    """
    runner = CliRunner()
    result = runner.invoke(cli.nmap, ['--version'])

    # If nmap is not installed, exit with the appropriate error message.
    if which('nmap'):
        assert result.exit_code == 0
    else:
        assert result.exit_code == 1
        assert 'Error: Failed' in result.output
        assert '- nmap' in result.output
