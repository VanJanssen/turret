# -*- coding: utf-8 -*-
# pylint: disable=unidiomatic-typecheck

"""Unit tests for the `clean_xml_dict` function."""

from collections import OrderedDict

import pytest

from turret.core.util import clean_xml_dict


def test_empty_ordered_dict():
    """Expects an empty normal dict."""
    raw = OrderedDict()
    clean = clean_xml_dict(raw)

    assert type(clean) is dict
    assert not clean


def test_simple_ordered_dict():
    """Expects a normal dict where the keys are cleaned."""
    raw = OrderedDict([
        ('element', '@value should not be cleaned'),
        ('@attribute', 'some value'),
    ])
    clean = clean_xml_dict(raw)

    assert type(clean) is dict
    assert clean == {
        'element': '@value should not be cleaned',
        'attribute': 'some value',
    }


def test_nested_ordered_dict():
    """Expects the nested dict to be cleaned."""
    raw = OrderedDict([
        ('nested', OrderedDict([
            ('key', 'value'),
            ('@attr', 'attr value'),
        ])),
        ('key', 'another value'),
    ])
    clean = clean_xml_dict(raw)

    assert type(clean) is dict
    assert type(clean['nested']) is dict
    assert clean == {
        'nested': {
            'key': 'value',
            'attr': 'attr value',
        },
        'key': 'another value',
    }


@pytest.mark.parametrize('raw,expected', [
    ('9876', 9876),
    ('0543', 543),
])
def test_int_string(raw, expected):
    """Expects an integer, not a float."""
    clean = clean_xml_dict(raw)
    assert type(clean) is int
    assert clean == expected


@pytest.mark.parametrize('raw,expected', [
    ('9876.543', 9876.543),
    ('0543.210', 543.21),
])
def test_float_string(raw, expected):
    """Expects a float, not an integer."""
    clean = clean_xml_dict(raw)
    assert type(clean) is float
    assert clean == expected


@pytest.mark.parametrize('raw,expected', [
    ('False', False),
    ('false', False),
    ('FALSE', False),
    ('True', True),
    ('true', True),
    ('TRUE', True),
])
def test_bool_string(raw, expected):
    """Expects a boolean."""
    clean = clean_xml_dict(raw)
    assert clean is expected


def test_normal_string():
    """Expects no cleaning takes place on non-special strings."""
    raw = '@ some string ++ that should not be cleaned 214'
    clean = clean_xml_dict(raw)
    assert raw is clean

    raw = 'False is the start of this string.'
    clean = clean_xml_dict(raw)
    assert raw is clean


def test_empty_list():
    """Expects a *new* empty list."""
    raw = []
    clean = clean_xml_dict(raw)

    assert type(clean) is list
    assert raw is not clean


def test_simple_list():
    """Expects a new list containing the cleaned elements."""
    raw = [
        OrderedDict([
            ('key', 'value'),
            ('@attr', 'attribute'),
        ]),
        'other element',
        '5',
    ]
    clean = clean_xml_dict(raw)

    assert type(clean) is list
    assert raw is not clean
    assert clean == [
        {
            'key': 'value',
            'attr': 'attribute',
        },
        'other element',
        5,
    ]


def test_nested():
    """Expects all nested elements to be cleaned."""
    raw = [
        [
            '5',
            '6',
            OrderedDict([
                ('int', 2),
            ]),
        ],
        OrderedDict([
            ('list', [
                'true',
                'false',
            ]),
            ('float', '3.7'),
        ])
    ]
    clean = clean_xml_dict(raw)

    assert clean == [
        [
            5,
            6,
            {'int': 2},
        ],
        {
            'list': [
                True,
                False,
            ],
            'float': 3.7,
        }
    ]
