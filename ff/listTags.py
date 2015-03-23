import logging
import os
import database

from cliff.lister import Lister


class Files(Lister):
    """Show identifed flags for a given file.
    """

    log = logging.getLogger(__name__)



    def get_parser(self,prog_name):
        '''
        I used this from one of the cliffdemo classes, it simply is used
        to take in additional command line arguments on top of the main command
        In our case, list is the main command, and then we want to collect the
        name of the file name which will be the second argument
        '''

        parser = super(Files, self).get_parser(prog_name)
        parser.add_argument('filename', nargs='?', default='**no_file**')
        return parser

    def take_action(self, parsed_args):
        userProjectDirectoryPath = os.environ['PWD']
        db_File = database.ff_db(userProjectDirectoryPath)
        file_name = parsed_args.filename
        TupleList = db_File.retrieve('file',file_name)
        os.system("figlet -c 'Flags!' ")
        print "+------------+"
        print "| File Name: |", file_name
        print "+------------+"
        
        return (('Tag #', 'Comment Flag','Comment Line Number','Comment Content'),
                ((n[0], n[4], n[2], n[3]) for n in TupleList)
                )
