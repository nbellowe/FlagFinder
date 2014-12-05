import logging
import os
from collections import namedtuple
import database



from cliff.lister import Lister


class Files(Lister):
    """Show a list of files in the current directory.

    The file name and size are printed by default.
    """

    

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):

    	userProjectDirectoryPath = os.environ['PWD']
    	db_File = database.ff_db(userProjectDirectoryPath)

    	TupleList = db_File.retrieve('file','parse.py')
    	
    	Flag_Line = namedtuple('Flag_Line', ['fileName', 'commentLineNumber', 'commentContent','Flag'])
    	TupleOne = Flag_Line("sample.py",34,"#this is the TODO comment","TODO")
    	TupleTwo = Flag_Line("hello.py",17,"#this is the COMPLETED comment","COMPLETED")
    	TupleThree = Flag_Line("goodbye.py",27,"#this is the BROKEN comment","BROKEN")
    	TupleFour = Flag_Line("pooper.py",156,"#this is yet another stupid TODO comment","TODO")
    	TupleFive = Flag_Line("nathan.py",32,"#NEEDS-APPROVAL from the big boss","NEEDS-APPROVAL")
    	TupleSix = Flag_Line("hahaha.py",2,"#this is the BROKEN comment which goes on on on on and for no reason","BROKEN")
    	TupleSeven = Flag_Line("fff.py",156,"#this is yet another stupid comment that fortunately WORKS","WORKS")

    	listOfTuples = [TupleOne,TupleTwo,TupleThree,TupleFour, TupleFive,TupleSix,TupleSeven]
        
    	print "+------------+"
    	print "| File Name: |"
    	print "+------------+"
        print TupleList
        return (('Comment Line Number', 'Flag', 'Comment Content'),
                ((n[1],n[3],n[2][:30]) for n in listOfTuples)
                )
