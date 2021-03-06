#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
from setuptools import find_packages
from setuptools import setup

test_requirements = [
    'pytest',
]

setup(
    # metadata see setup.cfg
    packages=find_packages('plonecli'),
    entry_points={
        'console_scripts': [
            'plonecli=plonecli.cli:cli'
        ]
    },
    include_package_data=True,
    install_requires=[
        'Click>=6.8a99',
        'bobtemplates.plone>=3.0.0a3',
        'mr.bob',
        'setuptools',
        'zest.releaser',
    ],
    extras_require={
        'test': test_requirements,
        'dev': [
            'tox',
            'zest.releaser[recommended]',
        ],
    },
    zip_safe=False,
    keywords='plonecli',
    scripts=['plonecli_autocomplete.sh'],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=['pytest-runner'],
)
