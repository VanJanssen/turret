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

    program.arguments = ['something', 'else']
    assert program.arguments == ['something', 'else']
    assert program.command == [test_name, 'something', 'else']


def test_run():
    program = Program(test_name)
    assert program.run().returncode is 0
    program = Program(test_name, show_help=True)
    assert program.run().returncode is 0
    program = Program(test_name, show_version=True)
    assert program.run().returncode is 0


def test_completed_program():
    program = Program(test_name, ['-al'])
    completed = program.run()
    assert completed.args == ['ls', '-al']
    assert completed.returncode == 0
    assert isinstance(completed.output['stdout'], bytes)
    assert completed.output['stderr'] == b''
