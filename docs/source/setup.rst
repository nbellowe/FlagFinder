Setup
=====

To develop


  $ pip install virtualenv
  $ virtualenv .venv
  $ . .venv/bin/activate
  (.venv)$ cd ff
  (.venv)$ python setup.py install

Usage
=====

parse: ff parse [filename]
setup: ff setup
interactive: ff

setup.py
--------

The demo application is packaged using distribute_, the modern
implementation of setuptools.

.. literalinclude:: ../../ff/setup.py
   :linenos:

.. _distribute: http://packages.python.org/distribute/
