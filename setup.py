#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
spoof your MAC address with spoofee in OS X, Windows & Linux.
"""
from setuptools import setup, find_packages


def get_version():
    """
    Load and return the current package version.
    """
    local_results = {}
    exec(compile(open('spoofee/version.py').read(), 'spoofee/version.py', 'exec'), {}, local_results)
    return local_results['__version__']


if __name__ == '__main__':
    setup(
        name='Spoofee',
        version=get_version(),
        description=__doc__,
        long_description=__doc__,
        author='r0otz-ee',
        author_email='illu5iv3@yahoo.com',
        url='',
        packages=find_packages(),
        include_package_data=True,
        install_requires=[
            'docopt'
        ],
        scripts=[
            'scripts/spoofee.py',
	    'scripts/spoofee'
        ],
        license='lit'
    )
