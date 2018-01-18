# -*- coding: utf-8 -*-

from click.testing import CliRunner

from turret.core import cli


def test_help_output():
    """Test the help output of the scout command."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ['scout', '--help'])

    # Test exit code
    assert result.exit_code == 0

    # Test output of help message for expected values
    assert '--mode' in result.output
    assert '--help' in result.output


def test_not_implemented():
    """Recon is not implented yet."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ['scout', 'target', '--mode', 'stealth'])

    assert result.exit_code != 0
    assert 'NotImplementedError' in repr(result)
