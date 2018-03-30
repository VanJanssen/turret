#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'psutil>=4.4.0',
    'xmltodict',
]

setup_requirements = [
    'pytest-runner',
]

test_requirements = [
    'pytest',
    'pytest-cov',
]

setup(
    name='turret',
    version='0.1.0',
    description="Discover, analyse, manage, attack and defend computer networks.",
    long_description=readme + '\n\n' + history,
    author="Erwin Janssen",
    author_email='erwinjanssen@outlook.com',
    url='https://github.com/VanJanssen/turret',
    packages=find_packages(include=['turret']),
    entry_points={
        'console_scripts': [
            'turret=turret.core.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='turret',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
