# -*- coding: utf-8 -*-

from pytest import raises

from turret.scout.core import recon


def test_not_implemented():
    with raises(NotImplementedError):
        recon('targets', 'mode')
