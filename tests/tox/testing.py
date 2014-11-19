import unittest
import random
import subprocess
import ff

def call_ff(option):
    return subprocess.Popen("ff "+option, shell=True, stdout=PIPE).stdout.read()


class Test_Example(unittest.TestCase):
    def setUp(self):
      self.HTML_test_comments = ["   <!--HAHAHAHA this is a comment", "<!-- as is this", "<!----this is also a comment", "TODO"]
      self.comments = ["# - TODo this is not a good example", "<!-- as is TODO this", "//COMPLETED is also a comment", "/*NEEDS-APPROVAL TODO"]
    def test_HTML(self):
        print ()
        for html_comment in self.comments:
          self.assertEquals(html_comment, ff.parse.check_comment_line(html_comment)) # look into parameter for message on failure: "Testing check_comment_line for HTML comment tags"

class Test_Installed(unittest.TestCase): #look into tox and virtualenv, as that will be used for testing!
    def setUp(self):
        pass
    def test_run(self):
        return_code = subprocess.call("ff --status", shell=True)
        self.assertTrue(return_code > 0) #may not work.
    def test_parsepy(self):
        self.parsed_py = call_ff('--parse test.py')
        self.assertTrue(len(self.parsed_py) > 5)
    def test_parsec(self):
        self.parsed_c = call_ff('--parse test.c')
        self.assertTrue(len(self.parsed_c) > 5)
    def test_parsejava(self):
        self.parsed_j = call_ff('--parse test.java')
        self.assertTrue(len(self.parsed_java) > 5)
    #Guys please write more tests.

        
if __name__ == '__main__':
    unittest.main()
