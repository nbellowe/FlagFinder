#!/usr/bin/env python

PROJECT = 'Flag_Finder'

# Change docs/sphinx/conf.py too!
VERSION = '0.01'

from setuptools import setup, find_packages

try:
    long_description = open('README.rst', 'rt').read()
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
        'cliff.demo': [
            'simple = cliffdemo.simple:Simple',

       ],
    },

    zip_safe=False,
)
