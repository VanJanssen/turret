# -*- coding: utf-8 -*-

from pytest import raises

from turret.core.extenders import Program

test_name = 'ls'


def test_defaults():
    program = Program(test_name)
    assert program.arguments == list()
    assert program.show_help is False
    assert program.help_option == '--help'
    assert program.show_version is False
    assert program.version_option == '--version'
    assert program.command == [test_name]


def test_command_read_only():
    program = Program('some_name')
    with raises(AttributeError):
        program.command = 'This assignment must fail'


def test_help_options():
    program = Program(test_name, show_help=True, help_option='-h')
    assert program.command == [test_name, '-h']
    program.help_option = '--show-help'
    assert program.command == [test_name, '--show-help']


def test_version_options():
    program = Program(test_name, show_version=True, version_option='-V')
    assert program.command == [test_name, '-V']
    program.version_option = '--show-version'
    assert program.command == [test_name, '--show-version']


def test_arguments():
    program = Program(test_name, ['some', 'arguments'])
    assert program.arguments == ['some', 'arguments']
    assert program.command == [test_name, 'some', 'arguments']

    # Vales that evaulate to False, should reset program.arguments to an
    # empty list.
    for value in (list(), dict(), '', None, False):
        program.arguments = value
        assert program.arguments == list()

    # Strings are split into a list, but quotes should be respected.
    program.arguments = 'value \'single quotes\' "double quotes"'
    assert program.arguments == ['value', 'single quotes', 'double quotes']

    # Tuple becomes list
    program.arguments = ('some', 'arguments')
    assert program.arguments == ['some', 'arguments']


def test_run():
    program = Program(test_name)
    assert program.run() is 0
    program = Program(test_name, show_help=True)
    assert program.run() is 0
    program = Program(test_name, show_version=True)
    assert program.run() is 0
