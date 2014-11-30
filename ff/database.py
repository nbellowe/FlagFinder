import os
import sqlite3
from collections import namedtuple

DB_DIRNAME = '.ff'
DB_ENTRY_ITEMS = 3
DB_ENTRY_CATEGORIES = '(file text, line_number integer, comment_line text)'

class ff_db:
	
	def __init__(self, project_rootdir, db_name):

		self.abs_dirpath = os.path.join(project_rootdir, DB_DIRNAME)
		if os.path.isdir(self.abs_dirpath) == False:
			try:
				os.mkdir(self.abs_dirpath)
			except OSError:
				raise

		self.abs_filepath = os.path.join(self.abs_dirpath, db_name)
		self.db_conn = sqlite3.connect(self.abs_filepath)
		self.db_cursor = self.db_conn.cursor()
		db_entry_string = 'CREATE TABLE IF NOT EXISTS flags ' + DB_ENTRY_CATEGORIES
		self.db_cursor.execute(db_entry_string)
		self.db_conn.commit()

	def close(self):
		self.db_cursor.close()
		self.db_conn.close()
	
	def add_entry(self, db_entry):
		db_entry_string = '('
		for i in db_entry:
			db_entry_string += '?,' 
		db_entry_string = db_entry_string[:len(db_entry_string) - 1] + ')'
		db_entry_string = 'INSERT INTO flags VALUES ' + db_entry_string
		self.db_cursor.execute(db_entry_string, db_entry[:DB_ENTRY_ITEMS])
		self.db_conn.commit
		
	def retrieve(self, query_type, *db_search_query):
		query_results = []
		if query_type == 'file':	
			db_search_query = (db_search_query,)
			self.db_cursor.execute('SELECT * FROM flags WHERE file LIKE ?', db_search_query)
			for row in self.db_cursor:
				query_results.append(row)
			print query_results
		

