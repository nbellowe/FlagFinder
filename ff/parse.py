'''
File that is responsible for parsing lines of code, deciding if the line is a comment,
deciding if the line is a comment with a flag, and then populating the namedtuple data 
type that will be inserted into the database
'''

from collections import namedtuple

"""
The DEFAULT_FLAGS array will contain default flags that FF will look for if the
user does not supply his/her own flags.
"""
DEFAULT_FLAGS = ['TODO', 'COMPLETED', 'BROKEN', 'IN-PROGRESS', 'NEEDS-APPROVAL'] 


"""
The USER_SUPPLIED_FLAGS array will be populated by all the flags that the user
supplies either on the command line when he/she calls FF
or from a config file where the user can keep their flags stored for reuse
"""
USER_SUPPLIED_FLAGS = ['']

FlagLine = namedtuple('FlagLine', ['fileName', 'commentLineNumber', 'commentContent', 'Flag']) 
#https://docs.python.org/2/library/collections.html


def check_comment_line(code_line):
	'''
	Checks to see if a passed in line of code is a comment by looking at the beginning syntax of the line
	:param code_line: a line of code from the users file
	:type code_line: str
	:returns: bool
	'''
	#WORKS
	#strip() will remove any whitespace from the beginning and end of the string. Allows us to check first meaningful char of each line
	code_line = code_line.strip() 

	#array that contains all the opening comment syntaxes we need to look for. 
	comment_starters = ['#', "'''", '"""', '//', '/*', '<!--', '%'] 
	# [python-ruby-perl-unixshells single line], [python blockcomments], 
	# [java-c-c++-c#-javascript-objectiveC],[multiline comments],[html], [MATLAB] 

	# Loop through each of the comment_starters and check if our comment line starts with anyone of them.
	 
	if code_line is not []: # if we've passed in just a single line and not an array of lines...
		for comment_starter in comment_starters:  #for all the opening comment tags that we are looking for... 
			if code_line.startswith(comment_starter) is True: #does our passed in code_line start with one of the commentStaters?
				return True 	#if it does, return true. If not, continuing iterating through all of the possible commentStarters
		return False 	#if we've gone through all of the commentStarters and we still haven't found a match, then the line is not a comment
	
	else: # if we've passed in an array of lines

	    for comment_starter in comment_starters: # for all the opening comment tags that we are looking for...
	    	for line in code_line: # for each line that we have passed in 
	    		if line.startswith(comment_starter) is True: #make the check
	    			return True 		

	        return False

def check_for_default_flag(code_line): 
	'''
	Checks to see if a passed in line of code is a comment AND if it contains a flag defined by us
	:param code_line: a line of code from the users file
	:type code_line: str
	'''
	
	if check_comment_line(code_line) is False: #if line isn't a comment then there is no point for looking for flags within it
		return False 
	else:
		if code_line is not []: # if we haven't passed in an array of lines
			for flag in DEFAULT_FLAGS: # for each flag in our array of default flags...
				if code_line .find(flag) != -1:# if the find method doesn't return -1 (ie: the comment line DOES contain our flag)
					return flag # return that flag so that we know which of the flags is contained inside the line after making the check
			return False    #if we have iterated through all flags and none of them exist in the comment line, then there is no default flag in the comment
		else:
			for flag in DEFAULT_FLAGS:
				for line in code_line:
					return code_line .find(flag) != -1 			

def check_empty(code_line):
	'''
	Checks to see if a given line is empty
	:param code_line: a line of code from the users file
	:type code_line : str
	:returns: bool
	'''
	return code_line .strip() in ['']

def check_end_block_comment(comment_line):
	'''
	Checks to see if a certain line of code contains syntax that signifies the end of a commment block
	'''
	end_block = not((comment_line.find("'''") == -1 and
			comment_line.find('"""') == -1 and
			comment_line.find('*/') == -1 and
			comment_line.find('-->') == -1 and
			comment_line.find('}}') == -1 and
			comment_line.find('-#}') == -1))
	return end_block #dumb way to write it before


def make_comment_line_tuple(line_of_code, linenumber, filename):
	"""
	This function will be responsible for taking in information about a line
	from the main method, passing it into the check_comment_line and check_for_default_flag
	functions, and if the line is a correctly formatted comment containing a flag, we create 
	the named tuple that will be passed into the DB for storage

	: param line_of_code: an integer that represents what line number that code of line is

	"""

	
	if check_for_default_flag(line_of_code):
		this_tuple = FlagLine(filename, linenumber, line_of_code, check_for_default_flag(line_of_code))
		#print thisTuple
		return this_tuple 
	

#if __name__ == '__main__':
 #   return 1
