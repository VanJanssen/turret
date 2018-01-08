# -*- coding: utf-8 -*-

"""Tests for the command line interface of Turret."""

from shutil import which

from click.testing import CliRunner

from turret import __version__
from turret import cli


def test_main():
    """Test the main entry point."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    help_result = runner.invoke(cli.main, ['--help'])

    # Test exit codes
    assert result.exit_code == 0
    assert help_result.exit_code == 0

    # Verify that the '--help' option yields the same output
    assert result.output == help_result.output

    # Test output of help message for expected values
    assert '--version  Show the version and exit.' in result.output
    assert '--help     Show this message and exit.' in result.output
    assert 'raw    Directly call supported tools.' in result.output
    assert 'scout  Perform reconnaissance.' in result.output

    # Test `--version` option
    version_result = runner.invoke(cli.main, ['--version'])
    assert 'Turret ' + __version__ in version_result.output


def test_raw():
    """Test the raw command group."""
    runner = CliRunner()
    result = runner.invoke(cli.raw)
    help_result = runner.invoke(cli.raw, ['--help'])

    # Test exit code
    assert result.exit_code == 0
    assert help_result.exit_code == 0

    # Verify that the '--help' option yields the same output
    assert result.output == help_result.output

    # Test output of help message for expected values
    assert 'Directly call supported tools.' in result.output
    assert '--help  Show this message and exit.' in result.output
    assert "'turret raw [TOOL] --help'" in result.output
    assert '--help  Show this message and exit.' in result.output
    assert 'nmap  Perform Nmap scans.' in result.output


def test_raw_nmap():
    """Test the raw nmap command."""
    runner = CliRunner()
    result = runner.invoke(cli.nmap)

    # Test is dependent on whether nmap is installed
    if which('nmap'):
        pass
    else:
        assert result.exit_code == 1
        assert 'Error: Failed' in result.output
        assert '- nmap' in result.output
