#http://beyondgrep.com/ only searches source code, also better. e.g. ack --perl REGEX_PATTERN only searches prl

import subprocess, sys, re

from collections import namedtuple

"""
The DEFAULT_FLAGS array will contain default flags that FF will look for if the
user does not supply his/her own flags.
We can add to this list of course, I just came up with a few that I came up 
with off the top of my head. Feel free to add more
"""

DEFAULT_FLAGS = ['TODO', 'COMPLETED', 'BROKEN', 'IN-PROGRESS', 'NEEDS-APPROVAL','WORKS'] 

"""
The USER_SUPPLIED_FLAGS array will be populated by all the flags that the user
supplies either on the command line when he/she calls FF
or from a config file where the user can keep their flags stored for reuse"""
USER_SUPPLIED_FLAGS = ['']

Flag_Line = namedtuple('Flag_Line', ['fileName', 'comment_line_number', 'comment_line','flag']) #https://docs.python.org/2/library/collections.html

# WORKS!! Checks to see if a line is a comment
def check_comment_line(comment_line):

	
	comment_line = comment_line.strip() #strip() will remove any whitespace from the beginning and end of the string. Allows us to check first meaningful char of each line


	#array that contains all the opening comment syntaxes we need to look for. Will constantly be added to as we expand
	ListOfCommentStarters = ['#',"'''",'"""','//','/*','<!--','%'] # [python-ruby-perl-unixshells single line], [python blockcomments], 
	# [java-c-c++-c#-javascript-objectiveC],[multiline comments],[html], [MATLAB] 

	# Loop through each of the CommentStarters and check if our comment line starts with anyone of them. More efficient way of doing it then what we had before
	# especially from standpoint of scalability when we start adding support for many different kinds of languages and have several different syntaxes for comments
	if comment_line is not []: # if we've passed in just a single line and not an array of lines
		for CommentStarter in ListOfCommentStarters:  #for all the opening comment tags that we are looking for... 
			if comment_line.startswith(CommentStarter) is True: #does our passed in comment_line start with one of the commentStaters?
				return True 	#if it does, return true. If not, continuing iterating through all of the possible commentStarters
		return False 	#if we've gone through all of the commentStarters and we still haven't found a match, then the line is not a comment
	
	else: # if we've passed in an array of lines

	    for CommentStarter in ListOfCommentStarters: # for all the opening comment tags that we are looking for...
	    	for line in comment_line: # for each line that we have passed in 
	    		if line.startswith(CommentStarter) is True: #make the check
	    			return True 		#maybe implement some way of returning which element of the array (which line of code) has the comment and what kind of comment

	        return False

# Method to check if a line of a code is A.) a comment and B.) if it is a comment, whether it contains on of our default flags
# WORKS! 
def check_for_default_flag(comment_line): 
	if check_comment_line(comment_line) is False: #if line isn't a comment then there is no point for looking for flags within it
		return False 
	else:
		if comment_line is not []: # if we haven't passed in an array of lines
			for flag in DEFAULT_FLAGS: # for each flag in our array of default flags...
				if comment_line.find(flag) != -1: #or comment_line.find(flag.lower()) != -1: # if the find method doesn't return -1 (ie: the comment line DOES contain our flag)
					return flag # return that flag so that we know which of the flags is contained inside the line after making the check
			return False    #if we have iterated through all flags and none of them exist in the comment line, then there is no default flag in the comment
		else:
			for flag in DEFAULT_FLAGS:
				for line in comment_line:
					return comment_line.find(flag) != -1 

 # Same as above method except this one will iterate through a user flag array, supplied from the user on the command line or specified 
 # by the user in a config file of sorts
def check_for_user_flag(comment_line): 
	if check_comment_line(comment_line) is False: #if line isn't a comment then there is no point for looking for flags within it
		return False 
	else:
		if comment_line is not []: # if we haven't passed in an array of lines
			for flag in USER_SUPPLIED_FLAGS: # for each flag in our array of default flags...
				if comment_line.find(flag) != -1: # if the find method doesn't return -1 (ie: the comment line DOES contain our flag)
					return flag # return that flag so that we know which of the flags is contained inside the line after making the check
			return False   #if we have iterated through all flags and none of them exist in the comment line, then there is no default flag in the comment
		else:
			for flag in USER_SUPPLIED_FLAGS:
				for line in comment_line:
					return comment_line.find(flag) != -1				

#WORKS
def check_empty(comment_line):
	return comment_line.strip() in ['']

# exception handling function
# avoids finding false positive comment ending syntax in program strings such as  */ that's part of a string 
# will rewrite this soon. I'm thinking that it's purpose is to check if a comment block is ending on a particular line
def check_end_block_comment(comment_line):
	end_block = not((comment_line.find("'''") == -1 and
			comment_line.find('"""') == -1 and
			comment_line.find('*/') == -1 and
			comment_line.find('-->') == -1 and
			comment_line.find('}}') == -1 and
			comment_line.find('-#}') == -1))
	return end_block #dumb way to write it before

# no idea what the hell this does
def check_trailing_comment(comment_line): 
	m = re.search('\S+\s*#\s*TODO.+$', comment_line)
	return m is not None
# no idea what the hell this does
def expand(match):
	all_comment_lines = [match.comment_line] #make sense? heeeel yeah.
	if check_trailing_comment(match.comment_line): #doesn't do trailing comments. Big error.
		pass
	elif check_comment_line(match.comment_line): #if this is a comment, check if the next line is.
		start = match.comment_line_number + 1
		comment_line = comment_linecache.getcomment_line(match.file, start)
		while check_comment_line(comment_line) and not check_todo(comment_line): #select all lines that are still comments, and append those to all.
			all_comment_lines.append(comment_linecache.getcomment_line(match.file, start))
			start += 1
			comment_line = comment_linecache.getcomment_line(match.file, start)
	elif not check_end_block_comment(match.comment_line): #ah damn, the current match is not the end of a block comment
		start = match.comment_line_number + 1 #what about the next one?
		comment_line = comment_linecache.getcomment_line(match.file, start)
		while (not check_empty(comment_line) and not check_todo(comment_line) and not check_end_block_comment(comment_line)):
			all_comment_lines.append(comment_linecache.getcomment_line(match.file, start)) #lets append that bitch. fuck yeah lets do it
			comment_line = comment_linecache.getcomment_line(match.file, start)

	return all_comment_lines
# no idea what the hell this does		
def extract_titles(comment_line):
	contents = re.findall('TODO\((.*?)\)', comment_line)

	if not all([re.match('^[a-zA-Z0-9_\-,/ ]+$', c) for c in contents]):
		return None

	titles = []
	for title in contents:
		titles.extend([x.strip() for x in re.split('[,/]', title)])

	return titles #TODO(nbellowe) sucks, do this yourself Nathan.
# no idea what the hell this does
def get_todo_matches():
	try:
		matches = subprocess.check_output(['ack', '--with-filename', "TODO\\(.*\\)"]) #http://beyondgrep.com/
	except subprocess.CalledProcessError, e: #TODO TEST
		print e.output
		raise e
	matches = [l for l in matches.split('\n') if l.strip() != '']
	matches = [l.split(':', 2) for l in matches]
	matches = [Flag_Line(l[0], int(l[1]), l[2]) for l in matches] #high performance data type. Feel free to get rid of, just think of it as a special communication message. 
	#All this does is takes the list of matches and create a new list of "Flag_Line" type.
	return matches


#this will be essentially the main part of parse.py
# This class will call all the check functions above
# and if the passed in comment_line is a valid comment
# then it will insert all of the information into the tuple
# format that will be easily stored in Jasons DB.

def makeCommentLineTuple(line_of_code,linenumber,filename):

	# Begininning implementation of how the tuple will be formed
	# This WORKS! Been trying it out with the flag_finder_main.py file
	# and the tuple is succesfully created with all the proper attributes
	if check_for_default_flag(line_of_code):
		thisTuple = Flag_Line(file,linenumber,line_of_code,check_for_default_flag(line_of_code))
		return thisTuple

	"""
	# this is simply a logical flow/description of how I see this function working
	# 
	# If comment_line is comment and has flags and it comes from this line number
	# from this file and is identified as this language and is this many lines long
	# then the tuple will be the following:
	# 
	# FlagLine = FlagLine("file", "FLAG", linenumber, "language", lenght_of_comment )
	# 
	# and then this flagline tuple will be passed onto Jasons db.py class to be broken down
	# and inserted into our sql database
	# I'm thinking that the extract titles and expand functions that are above should
	# be removed and instead replaced with something similar in displaytag.py
	# 
	# In displaytag.py we can read in all the attributes of a tag from the DB 
	# and simply display them in the setup that I already have working with 
	# the mock static data
	"""

#if __name__ == '__main__':
 #   return 1