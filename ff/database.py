import os
import sqlite3
from collections import namedtuple



FLAGTABLE_ENTRY_ELEMENTS = 5
FLAGTABLE_ENTRY_CATEGORIES ='(tag_id INTEGER,file_name TEXT,line_number INTEGER,comment_content TEXT,flag TEXT)'


class ff_db:

	
	def __init__(self, project_rootdir):
		
		self.FILE = 'file'
		self.FLAG = 'flag'
		self.FILE_AND_FLAG = 'file+flag'

		db_name = '.' + os.path.split(project_rootdir)[1] + '-ff.db'
		self.abs_filepath = os.path.join(project_rootdir, db_name)

		self.db_conn = sqlite3.connect(self.abs_filepath)
		self.db_conn.text_factory = str #this is so what I get back from the DB isn't in Unicode strings but ASCII text, more easily passable to parse.py.

		self.db_cursor = self.db_conn.cursor()
		self.db_cursor.execute('CREATE TABLE IF NOT EXISTS flags_table ' + FLAGTABLE_ENTRY_CATEGORIES)
		self.db_conn.commit()

	def close(self):

		self.db_cursor.close()
		self.db_conn.close()

	def add_entries(self, db_entry_list):
		
		def sanatize_input(db_entry, tag_id): #this prepends tag_id's onto entries and sanatizes entry elements that are strings to allow us to insert comments, flags, and filenames that have single and double quotes within them (SQLite whines unless they're properly formatted).
			tag_tuple = namedtuple('tag_tuple', 'tag')
			l = ['','','']
			l[0] = db_entry[0]
			l[1] = db_entry[2]
			l[2] = db_entry[3]
			for entry in l:
				entry = entry.replace("'", "''").replace("\"", "\"\"")
			prepend_tag = namedtuple('tagged', tag_tuple._fields + db_entry._fields)
			tagged_db_entry = prepend_tag(tag_id, l[0], db_entry[1], l[1], l[2])
			return tagged_db_entry


		tag_id = 1
		drop_file_entries = (db_entry_list[0][0],)
		self.db_cursor.execute('DELETE FROM flags_table WHERE file_name=?', drop_file_entries)
		for db_entry in db_entry_list:

			tagged_db_entry = sanatize_input(db_entry, tag_id)

			self.db_cursor.execute('INSERT INTO flags_table VALUES (?,?,?,?,?)', tagged_db_entry[:FLAGTABLE_ENTRY_ELEMENTS])

			tag_id += 1
		self.db_conn.commit()
	
	def retrieve(self, query_type, db_search_query):

		if query_type == self.FILE:	#return flags in file <filename> with db.retrieve(db.FILE,'<filename>')
			db_search_query = (db_search_query,)
			self.db_cursor.execute('SELECT * FROM flags_table WHERE file_name LIKE ?', db_search_query)

		elif query_type == self.FLAG:	#return flags in all files corresponding to flag type <flag> with db.retrieve(db.FLAG,'<flag>')
			db_search_query = (db_search_query,)
			self.db_cursor.execute('SELECT * FROM flags_table WHERE flag LIKE ?', db_search_query)

		elif query_type == self.FILE_AND_FLAG:	#return flags in file <filename> corresponding to flag type <flag> with db.retrieve(db.FILE_AND_FLAG,['<filename>','<flag>']) <---note the list this time.
			db_search_query = (db_search_query[0],db_search_query[1])
			self.db_cursor.execute('SELECT * FROM flags_table WHERE file_name LIKE ? AND flag LIKE ?', db_search_query)

		else:
			print 'Invalid search query type: ' + query_type
			return []
			
		return self.db_cursor.fetchall()

