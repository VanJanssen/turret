# -*- coding: utf-8 -*-

"""Unit tests for the `scout.core` module."""

from pytest import raises

from turret.scout.core import recon


def test_not_implemented():
    """For now this function is not yet implemented."""
    with raises(NotImplementedError):
        recon('targets', 'mode')
