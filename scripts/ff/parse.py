#http://beyondgrep.com/ only searches source code, also better. e.g. ack --perl REGEX_PATTERN only searches prl

import subprocess, sys, comment_linecache, re

from collections import namedtuple
#Alex, challenge for you in particular. For your first project, make any of these be able to be passed either a comment_line array,
#(multicomment_line comments), or a single comment_line. Also, you'll be sad to know, I already commented this and deleted them! 
#Figure a couple out, and text me if you need help.
# note none of this will likely be used, as in the end we will likely have performance issues.
TODO_FLAGS = 'TODO' #note, parse yaml, make someone else do the rest of this shit, because to much design work. Make array-capable

Flag_Line = namedtuple('Flag_Line', ['file', 'comment_line_number', 'comment_line']) #https://docs.python.org/2/library/collections.html

def check_comment_line(comment_line):
	comment_line = comment_line.strip()
	return comment_line.startswith('#') or comment_line.startswith('//') #remember must parse

def check_todo(comment_line):
	return comment_line.find('TODO') != -1 #TODO here in this case will be a user supplied variable at some point

def check_empty(comment_line):
	return comment_line.strip() in ['', '*']

# exception handling function
# avoids finding false positive comment ending syntax in program strings such as  */ that's part of a string 
def check_end_block_comment(comment_line):
	end_block = not((comment_line.find("'''") == -1 and
			comment_line.find('"""') == -1 and
			comment_line.find('*/') == -1 and
			comment_line.find('-->') == -1 and
			comment_line.find('}}') == -1 and
			comment_line.find('-#}') == -1))
	return end_block #dumb way to write it before

def check_trailing_comment(comment_line): 
	m = re.search('\S+\s*#\s*TODO.+$', comment_line)
	return m is not None

def expand(match):
	all_comment_lines = [match.comment_line] #make sense?
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
		
def extract_titles(comment_line):
	contents = re.findall('TODO\((.*?)\)', comment_line)

	if not all([re.match('^[a-zA-Z0-9_\-,/ ]+$', c) for c in contents]):
		return None

	titles = []
	for title in contents:
		titles.extend([x.strip() for x in re.split('[,/]', title)])

	return titles #TODO(nbellowe) sucks, do this yourself Nathan.

def get_todo_matches():
	try:
		matches = subprocess.check_output(['ack', '--with-filename', "TODO\\(.*\\)"]) #http://beyondgrep.com/
	except subprocess.CalledProcessError, e: #TODO TEST
		print e.output
		raise e
	matches = [l for l in matches.split('\n') if l.strip() != '']
	matches = [l.split(':', 2) for l in matches]
	matches = [Flag_Line(l[0], int(l[1]), l[2]) for l in matches] #high performance data type. Feel free to get rid of, just think of it as a special communication message. All this does is takes the list of matches and create a new list of "Flag_Line" type.
	return matches


if __name__ == '__main__':
    return 1
