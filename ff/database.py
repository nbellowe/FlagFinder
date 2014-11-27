import os
import sqlite3
import namedtuple

#project_rootdir = os.environ['PWD']

def db_exists(dirname, filename):

    abs_filepath = os.path.join(dirname, filename)	

    if os.path.isdir(dirname):
        if os.path.isfile(abs_filepath + '-ff.db'): 
            return True
    return False

def db_add_entry(project_rootdir, db_entry):

	#db_entry = Some amorphous blob, to grow and shrink as per the whims of parse.py. Accepted into this function as a namedtuple.

	#project_rootdir = This is the root directory of the project. Orignally hardcoded in as os.environ['PWD'], which gives current working directory. Nathan wisely talked me into making it relative.

    def make_db_entry_string(db_entry):
        entry_string = ''
        if db_entry == ():
            print 'Error: empty entry supplied as argument'
        for i in range(0, len(db_entry):
            entry_string += '?,'
        return entry_string[:(len(entry_string)-3)]  #quick and dirty way of shaving off an entry so the 'file' entry can be hardcoded in somewhere outside this string. The file entry is extra important -- it's how we organize our db.

    def setup_db_input_args(db_entry):
        input_arg_string = ''
        for i in range(0, len(db_entry):
            input_arg_string = input_arg_string + db_entry[i]
        return input_arg_string[:len(input_arg_string)-2]

    db_dirname = os.path.join(project_rootdir, '.ff')
    db_filename = os.path.split(project_rootdir)[1] + '-ff.db'

    if db_exists(db_dirname, db_filename) == False:
        try:
            os.mkdir(db_dirname)
        except OSError:
            return 1
        finally:
            db_conn = sqlite3.connect(os.path.join(db_dirname, db_filename))
            db_cursor = db_conn.cursor()
            db_cursor.execute('create table PARENT_FILE_TABLE')
    db_entry_string = make_db_entry_string(db_entry)
    #does table exist? else:
    db_cursor.execute('create table ? (' + db_entry_string + ')', setup_db_args(db_entry))
    db_entry[0], #file
    db_entry[1], #comment_line_number
    db_entry[2]) #comment_line make this related to parent file table somehow.
    #does entry exist?
