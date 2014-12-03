# Welcome to the main meat of Flag Finder!!
# 
# This will be the class that parses the command line arguments,
# validates whether the passed in file actually exists through a quick
# excepction handler, and then if the file is valid and exists, each line
# of it is read. Each of these lines is relayed on to parse.py
# where the makeCommentLineTuple function is responsible for making all the checks
# for comments and then forming the tuple with all of the comment lines attributes

import os
import parse
from collections import namedtuple
import re
from cliff.command import Command

class Main(Command):


	# I used this from one of the cliffdemo classes, it simply is used
	# to take in additional command line arguments on top of the main command
	# In our case, parse is the main command, and then we want to collect the
	# name of the file name which will be the second argument
    def get_parser(self,prog_name):
        parser = super(Main,self).get_parser(prog_name)
        parser.add_argument('filename',nargs='?', default='null')
        return parser


    # Again more of cliffs conventions, take_action contains all the stuff
    # that will actually be going on
    def take_action(self, parsed_args):   

    	# Small helper function to determine the language being used by the file
    	# It'll good to have this language identified for attribute purposes
    	# I will add more languages later on
    	def checkLanguageOfFile(filename):
	    	if filename[-3:] == '.py':
	    		return "Python"
	    	elif filename[-2:] == '.c': 
	    		return "C"
	    	elif filename[-4:] == '.cpp': 
	    		return "C++"

	   	# try opening file and reading all the lines and parsing and etc.
    	try: 
        	with open(parsed_args.filename) as usersFile:
        		# this can be outside the loop of reading every line, the file
        		# will stay the same once it is read in above
			    print "Your file name is: ", usersFile.name
			    #the language will also be consistent for a single file so this 
			    #can also be printed at the top outside of the loop
			    print "The language is: ", checkLanguageOfFile(usersFile.name)
			    print "-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\n"

			    # for each line of the file...
			    # we add in the num counter to keep track of what line number each
			    # comment is on
			    for num, line in enumerate(usersFile, 1):
			    	# if the line is a comment and has a flag...
			    	if parse.check_for_default_flag(line):

			    		# calls the function in parse which forms the tuple
			        	comment_line = (parse.makeCommentLineTuple(line.rstrip('\n'),num,usersFile.name))
			 
			        	# in the final implementation, the following print lines
			        	# probably won't exist. Instead, the comment_line tuple that 
			        	# is formed above will be fed into Jasons DB as the namedtuple
			        	# and then the displaytag.py function will read in from the DB
			        	# and display to the user on command. In other words, calling
			        	# parse from CL will only parse the users file and feed its
			        	# parsed, "tupled" contents into the db, that's it.
			        	# Calling disp from CL is what will actually display all the tags.
			        	# I added the print statements for now so that we can call parse from
			        	# CL and see it work. it works, try it:) 
			        	
			        	print "Your comment is: ",comment_line.comment_line
			        	print "This comment is on line number: ",comment_line.comment_line_number
			        	print "The flag is: ", comment_line.flag
	
		        		print "\n"
	# The open file function can encounter an IOError if the user supplies a 
	# file that doesn't exist, or if they supply nothing after the parse command
	# This will catch that, telling the user the the file they tried parsing doesn't
	# exist and also reminding them how to call the parse function
	      
	except IOError:
		print "Input/Output Error: file", parsed_args.filename,"not found"
		print "Usage of parse command: ff parse [FILENAME]"