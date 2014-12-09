import logging
import os
import database
from cliff.lister import Lister


class UserFlag(Lister):
    """
    Allows user to add custom flags to be searched for
    """

    log = logging.getLogger(__name__)



    def get_parser(self,prog_name):
        '''
        I used this from one of the cliffdemo classes, it simply is used
        to take in additional command line arguments on top of the main command
        In our case, list is the main command, and then we want to collect the
        list of flags into a list which will be the second argument
        '''

        parser = super(UserFlag, self).get_parser(prog_name)
        parser.add_argument('flags', nargs='+',type=str)
        return parser

    def take_action(self, parsed_args):
        user_config = open(".ffconfig", 'a')
        for flag in parsed_args.flags:
            user_config.write(flag+"\n")




