'''
 Welcome to the main part of Flag Finder!! 
 This will be the class that parses the command line arguments,
 validates whether the passed in file actually exists through a quick
 excepction handler, and then if the file is valid and exists, each line
 of it is read. Each of these lines is relayed on to parse.py
 where the makeCommentLineTuple function is responsible for making all the checks
 for comments and then forming the tuple with all of the comment lines attributes.
 This tuple is then returned to the main function (this one) where it is added to 
 the DB
'''
import os
import parse
from collections import namedtuple
import re
from cliff.command import Command
import database

class Main(Command):
	'''
	Main class. Inherits the Command class from cliff so that the contents of this 
	class can be called from the Command Line as a command
	'''


	def get_parser(self,prog_name):
		'''
		I used this from one of the cliffdemo classes, it simply is used
		to take in additional command line arguments on top of the main command
		In our case, parse is the main command, and then we want to collect the
	 	name of the file name which will be the second argument
	 	'''

		parser = super(Main, self).get_parser(prog_name)
		parser.add_argument('filename', nargs='?', default='')
		return parser
		


	def take_action(self, parsed_args):   
		
		
		#This will be ran quickly with every iteration of parse to check if user
		#has added any custom flags that they want looked for
		try:
			user_config = open(".ffconfig", 'r')
			for line in user_config:
				parse.DEFAULT_FLAGS.append(line.rstrip('\n'))
		except IOError:
			print ("You are not in the same directory as where you ran ff start!")
			return 0
		

	   	# try opening file and reading all the lines and parsing and etc.
		user_project_directory_path = os.environ['PWD']
		db_file = database.ff_db(user_project_directory_path)
		try: 
			with open(parsed_args.filename) as users_file:
				comments = []
				for num, line in enumerate(users_file, 1):
				# if the line is a comment and has a flag...
					if parse.check_for_default_flag(line):

						# calls the function in parse which forms the tuple
						comment_line = (parse.make_comment_line_tuple(line.rstrip('\n'), num, users_file.name))
						# add this tuple to the running list of tuples that we have so far
						comments.append(comment_line)

					    #add the entire list of tuples at once to the db
				if comments == []:
					print users_file.name," had no flags in it."
					return 0
				db_file.add_entries(comments)
				print ("")
				print ("File succesfully parsed! Call ff list <filename> to see results!\n")  
		except IOError:
			print "Input/Output Error: file", parsed_args.filename, "not found"
        	#print "Usage of parse command: ff parse [FILENAME]"


			    # for each line of the file...
			    # we add in the num counter to keep track of what line number each
			    # comment is on
			    # 
		  
			    
						
	# The open file function can encounter an IOError if the user supplies a 
	# file that doesn't exist, or if they supply nothing after the parse command
	# This will catch that, telling the user the the file they tried parsing doesn't
	# exist and also reminding them how to call the parse function   
		
class Setup(Command):
	'''
	Allows the user to call setup from the command line which sets up his FF enviroment
	Sets up the database, the configuration file, and prints basic usage tips
	'''

	

	def take_action(self, parsed_args):
		user_project_directory_name = os.path.split(os.getcwd())[1]
		user_project_directory_path = os.environ['PWD']
		user_db_name = user_project_directory_name

		#os.system("figlet -c -f mini 'Welcome To' ")
		#os.system("figlet -c 'Flag Finder' ")
		print "+-----------------------------+"
		print "|Welcome To Flag Finder!"
		print "+-----------------------------+"
		print "______________________________________________________________________________________"
		print "* Your configuration file is called .ffconfig"
		print "* Edit .ffconfig for your custom flags"
		print "* Your database file is called", user_db_name
		print "* Your current project directory path is", user_project_directory_path
		print"_______________________________________________________________________________________"

		#os.system("figlet -c 'Usage:' ")
		print "+-------+"
		print "|Usage:"
		print "+-------+"

		print "** STEP 1: Run ff start in the root of your project to setup database and config file (you just did this!)\n"
		print "** STEP 2(optional):  Run ff add <flag1> <flag2> ... to add custom flags that you want searched. Otherwise, default flags will be found"
		print "  ----------------->  To insure proper usage, enter flags in ALL CAPS seperated by a space"
		print "  ----------------->  Warning: Ignore 'NoneType' error when running ff add, error means nothing\n"
		print "** STEP 3: Run ff parse <filename> to parse the comment flags of a file\n"
		print "** STEP 4: Run ff list <filename> to see your flags from that file!\n"


		print "+-----------------------------+"
		print "|Default Flags to Be Searched:| TODO | COMPLETED | BROKEN | IN-PROGRESS | NEEDS-APPROVAL"
		print "+-----------------------------+"
		# set up config file
		user_config = open(".ffconfig", 'a')

		
		
		#set up database
		db_file = database.ff_db(user_project_directory_path)
