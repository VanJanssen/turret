# -*- coding: utf-8 -*-

from click.testing import CliRunner

from turret import __version__
from turret.core import cli


def test_help_output():
    """Test the help output of the main entry point."""
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


def test_version_output():
    """Test if version output has the expected format."""
    runner = CliRunner()
    version_result = runner.invoke(cli.main, ['--version'])
    assert 'Turret ' + __version__ in version_result.output
