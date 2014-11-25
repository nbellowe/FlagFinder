import unittest
import random
import subprocess
#import ff
from ff import parse


#def call_ff(option):
 #   return subprocess.Popen("ff "+option, shell=True, stdout=PIPE).stdout.read()
        
        
class Test_Installed(unittest.TestCase): #look into tox and virtualenv, as that will be used for testing!
    '''
    def setUp(self):
        pass
    def test_run(self):
        return_code = subprocess.call("ff --status", shell=True)
        self.assertTrue(return_code > 0)
    
    def test_parsepy(self):
        self.parsed_py = call_ff('--parse test.py')
        self.assertTrue(len(self.parsed_py) > 5)
    def test_parsec(self):
        self.parsed_c = call_ff('--parse test.c')
        self.assertTrue(len(self.parsed_c) > 5)
    def test_parsejava(self):
        self.parsed_j = call_ff('--parse test.java')
        self.assertTrue(len(self.parsed_java) > 5)
    '''
# --Each Function to be tested in parse.py will be its own testing class below.~~ 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# This class will be responsible for testing just the check_comment_line function in parse.py
# The different functions within this class will be responsible for checking different types of comments
class Parse_CheckCommentLine(unittest.TestCase):

	# ** HTML COMMENTS **

    # Test to see if function correctly identfies properly formatted comments
    def test_html_comments_correct(self):
        HTML_test_comments = ["   <!--HAHAHAHA this is a comment", "<!-- as is this", "<!----this is also a comment", "<!-- and this also"]
        for html_comment in HTML_test_comments:
            self.is_html_comment = parse.check_comment_line(html_comment)
            self.assertTrue(self.is_html_comment)
    # Test to see if function correctly ignores wrongly formatted comments
    def test_html_comments_incorrect(self):
        HTML_test_not_comments = ["   <!this is not a comment", "<!nor is this", "!----this is also not a comment", "-- and this also isn't"]
        for html_comment in HTML_test_not_comments:
            self.is_html_comment = parse.check_comment_line(html_comment)
            self.assertFalse(self.is_html_comment)


    # ** PYTHON COMMENTS ** 

             # Test to see if function correctly identfies properly formatted comments
    def test_python_comments_correct(self):
        PYTHON_test_comments = ["   #HAHAHAHA this is a comment", "### as is this", "#this is also a comment", "# <!-- and this also"]
        for python_comment in PYTHON_test_comments:
            self.is_python_comment = parse.check_comment_line(python_comment)
            self.assertTrue(self.is_python_comment)
    # Test to see if function correctly ignores wrongly formatted comments
    def test_python_comments_incorrect(self):
        PYTHON_test_not_comments = ["   <!this is not a comment", "<!nor is this", "!----this is also not a comment", "-- and this also isn't"]
        for python_comment in PYTHON_test_not_comments:
            self.is_python_comment = parse.check_comment_line(python_comment)
            self.assertFalse(self.is_python_comment)

if __name__ == '__main__':
    unittest.main()
