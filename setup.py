#!/usr/bin/env python

PROJECT = 'FlagFinder'
VERSION = '0.02'

from setuptools import setup, find_packages

try:
    long_description = open('README.md', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='FlagFinder',
    long_description=long_description,

    author='Nathan Bellowe',
    author_email='nbellowe@gmail.com',

    url='https://github.com/nbellowe/FlagFinder',


    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=['cliff'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'ff = ff.main:main'
        ],
        'ff': [
        'd = ff.display_tag:DispTag',
        'parse = ff.flag_finder_main:Main',
        'setup = ff.flag_finder_main:Setup',
        ],
    },

    zip_safe=False,
)
