Setup
=====

To install and experiment with the demo app you should create a
virtual environment and activate it. This will make it easy to remove
the app later, since it doesn't do anything useful and you aren't
likely to want to hang onto it after you understand how it works.


  $ pip install virtualenv
  $ virtualenv .venv
  $ . .venv/bin/activate
  (.venv)$ 

Next, install cliff in the same environment.


  (.venv)$ cd scripts
  (.venv)$ python setup.py install

Usage
=====

Both cliff and the demo installed, you can now run the command
``cliffdemo``.

For basic command usage instructions and a list of the commands
available from the plugins, run::

  (.venv)$ cliffdemo -h

or::

  (.venv)$ cliffdemo --help

Run the ``simple`` command by passing its name as argument to ``cliffdemo``.

::

  (.venv)$ cliffdemo simple

The ``simple`` command prints this output to the console:

::

  sending greeting
  hi!


To see help for an individual command, use the ``help`` command::

  (.venv)$ cliffdemo help files

setup.py
--------

The demo application is packaged using distribute_, the modern
implementation of setuptools.

.. literalinclude:: ../../demoapp/setup.py
   :linenos:
The important parts of the packaging instructions are the
``entry_points`` settings. All of the commands are registered in the
``cliff.demo`` namespace. Each main program should define its own
command namespace so that it only loads the command plugins that it
should be managing.

.. _distribute: http://packages.python.org/distribute/
