# universal functions (in pkg)

import subprocess, sys, comment_linecache, re

from collections import namedtuple, Counter
#Alex, challenge for you in particular. For your first project, make any of these be able to be passed either a comment_line array, (multicomment_line comments), or a single comment_line.


TODO_FLAGS = 'TODO' #note, parse yaml, make someone else do the rest of this shit, because to much design work. Make array-capable

Match = namedtuple('Match', ['file', 'comment_line_number', 'comment_line'])

def check_comment_line(comment_line):
	comment_line = comment_line.strip()
	return comment_line.startswith('#') or comment_line.startswith('//') #remember must parse

def check_todo(comment_line):
	return comment_line.find('TODO') != -1

def check_empty(comment_line):
	return comment_line.strip() in ['', '*']

def check_end_block_comment(comment_line):
	return (comment_line.find("'''") != -1 or
			comment_line.find('"""') != -1 or
			comment_line.find('*/') != -1 or
			comment_line.find('-->') != -1 or
			comment_line.find('}}') != -1 or
			comment_line.find('-#}') != -1)

def check_trailing_comment(comment_line):
	m = re.search('\S+\s*#\s*TODO.+$', comment_line)
	return m is not None

def expand(match):
	all_comment_lines = [match.comment_line]
	if check_trailing_comment(match.comment_line):
		pass
	elif check_comment_line(match.comment_line):
		start = match.comment_line_number + 1
		comment_line = comment_linecache.getcomment_line(match.file, start)
		while check_comment_line(comment_line) and not check_todo(comment_line):
			all_comment_lines.append(comment_linecache.getcomment_line(match.file, start))
			start += 1
			comment_line = comment_linecache.getcomment_line(match.file, start)
	elif not check_end_block_comment(match.comment_line):
		start = match.comment_line_number + 1
		comment_line = comment_linecache.getcomment_line(match.file, start)
		while (not check_empty(comment_line) and
			   not check_todo(comment_line) and
			   not check_end_block_comment(comment_line)):
			all_comment_lines.append(comment_linecache.getcomment_line(match.file, start))
			start += 1
			comment_line = comment_linecache.getcomment_line(match.file, start)

	return all_comment_lines
		
def extract_names(comment_line):
	contents = re.findall('TODO\((.*?)\)', comment_line)

	# names must be alphanumeric or _-. Commas and slash OK as seperators.
	if not all([re.match('^[a-zA-Z0-9_\-,/ ]+$', c) for c in contents]):
		return None

	names = []
	for name in contents:
		names.extend([x.strip() for x in re.split('[,/]', name)])

	return names

def get_todo_matches():
	try:
		matches = subprocess.check_output(['ack', '--with-filename', "TODO\\(.*\\)"])
	except subprocess.CalledProcessError, e:
		print e.output
		raise e
	matches = [l for l in matches.split('\n') if l.strip() != '']
	matches = [l.split(':', 2) for l in matches]
	matches = [Match(l[0], int(l[1]), l[2]) for l in matches]

	return matches

def interactive(match_names=None, show_count=False):
	matches = get_todo_matches()

	count = 0
	count_by_name = Counter()

	for match in matches:
		result_comment_lines = expand(match)
		names = extract_names(match.comment_line)

		if names == None:
			continue

		if match_names != []:
			if not any([n in names for n in match_names]):
				continue

		count += 1
		for n in names:
			count_by_name[n] += 1

		if not show_count:
			print '%s:%d' % (match.file, match.comment_line_number), ', '.join(names)
			for l in result_comment_lines:
				print l.strip()
			print
	if show_count and match_names != []:
		print '%d TODOs' % count
	elif show_count and match_names == []:
		for name, count in count_by_name.most_common():
			print name, count
