import os
import sqlite3
from collections import namedtuple



FLAGTABLE_ENTRY_ELEMENTS = 5
FLAGTABLE_ENTRY_CATEGORIES ='(tag_id INTEGER,file_name TEXT,line_number INTEGER,comment_content TEXT,flag TEXT)'


class ff_db:
	
	def __init__(self, project_rootdir):

		db_name = '.' + os.path.split(project_rootdir)[1] + '-ff.db'
		self.abs_filepath = os.path.join(project_rootdir, db_name)

		self.db_conn = sqlite3.connect(self.abs_filepath)
		self.db_conn.text_factory = str #this is so what I get back from the DB isn't in Unicode stringsbut ASCII text, more easily passable to parse.py.

		self.db_cursor = self.db_conn.cursor()
		#might want to drop all tables here so when parse.py is run the db is regenerated each time. Depends how far I get with this :P
		self.db_cursor.execute('CREATE TABLE IF NOT EXISTS flags_table ' + FLAGTABLE_ENTRY_CATEGORIES)
		self.db_conn.commit()

	def close(self):
		self.db_cursor.close()
		self.db_conn.close()

	def add_entries(self, db_entry_list):
		tag_id = 1
		for db_entry in db_entry_list:
			tag_tuple = namedtuple('tag_tuple', 'tag')

			prepend_tag = namedtuple('tagged', tag_tuple._fields + db_entry._fields)
			tagged_db_entry = prepend_tag(tag_id, db_entry[0], db_entry[1], db_entry[2], db_entry[3]) #THIS IS AWFULLY BAD PRACTICE BUT KEEPING FOR NOW

			self.db_cursor.execute('INSERT INTO flags_table VALUES (?,?,?,?,?)', tagged_db_entry[:FLAGTABLE_ENTRY_ELEMENTS]) #TODO: Make sure you're not adding duplicate entries!

			reversed_entry = tuple(reversed(tagged_db_entry)) 

			self.db_cursor.execute('UPDATE flags_table SET flag=?, comment_content=?, line_number=? WHERE file_name=? AND tag_id=?', reversed_entry)
			tag_id += 1
			self.db_conn.commit()
	
	def retrieve(self, query_type, db_search_query):
		query_results = []
		if query_type == 'file':	
			db_search_query = (db_search_query,)
			self.db_cursor.execute('SELECT * FROM flags_table WHERE file_name LIKE ?', db_search_query)
			for row in self.db_cursor:
				query_results.append(row)
			return query_results

		

