import logging
import os, glob, re

from cliff.command import Command

class CompareParse(Command):
    "this is the parse to test Alex's/real one and generate comparative test scripts for an awesome unit testing framework"
    # current working directory
    path = os.getcwd()
    glob_pattern = re.compile("(todo:.*$)",re.IGNORECASE)
    
    def find_todos(string=""):
        """ prints strings matching compiled pattern"""
        if glob_pattern.search(string):
            string.strip()
            print(string) #note no line number.
    
    
    def read(file_read):
        for line in open(file_read):
            find_todos(line) 
    
    def find_files_in_directory(working_directory=path):
        ls = os.listdir(working_directory)
        for curfile in ls:
            # Do not read hidden files
            if curfile[0] == '.':
                continue
            else:
                self.log.debug("file is: " + curfile)
                read(curfile)
    if not path:
        self.log.debug('before release, remove default path argument')
    find_files_in_directory(path='~/FlagFinder/to-commit')
    
    
    
class Example(Command):
    "A simple command that prints a message."
    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.log.debug('simple.Example')


class Error(Command):
    "Always raises an error"
    log = logging.getLogger(__name__)
    
    def take_action(self, parsed_args):
        self.log.debug('simple.Error, error will immediately be thrown: ')
        raise RuntimeError('I will kill your family if you forget to delete me. ')
