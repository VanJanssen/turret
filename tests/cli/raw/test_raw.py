# -*- coding: utf-8 -*-

from click.testing import CliRunner

from turret import cli


def test_help_output():
    """Test the help output of the raw entry point."""
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
    assert "'turret raw [TOOL] --help'" in result.output
    assert '--help  Show this message and exit.' in result.output
    assert 'nmap  Perform Nmap scans.' in result.output
