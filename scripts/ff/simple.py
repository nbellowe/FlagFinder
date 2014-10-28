import logging

from cliff.command import Command


class Example(Command):
    "A simple command that prints a message."

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.log.info('Gdebugreet')
        self.log.debug('debugging')
        self.app.stdout.write('Writing\n')


class Error(Command):
    "Always raises an error"

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.log.info('causing error')
        raise RuntimeError('this is an exception')
