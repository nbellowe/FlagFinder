import unittest
import subprocess
import ff
from ff import parse




# This class will be used to check the installing and calling of our tool
# from the command line
class CheckInstallStuff(unittest.TestCase):

    def testHelpCommand(self):
        return_code = subprocess.check_call(["ff","--help"])
        self.assertTrue(return_code ==0)



# --Each Function to be tested in parse.py will be its own testing class below.~~ 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# This class will be responsible for testing just the check_comment_line function in parse.py
# The different mini-functions within this class will be responsible for checking different types of comments ie: different languages
class Parse_CheckCommentLine(unittest.TestCase):

	# ** HTML COMMENTS **
    
    # Testing if Parse correctly identfies properly formatted HTML comments
    def test_correct_html_comments(self):
        HTML_test_comments = ["   <!--HAHAHAHA this is a comment", "<!-- as is this", "<!----this is also a comment", "<!-- and this also"]
        for html_comment in HTML_test_comments:
            self.is_html_comment = parse.check_comment_line(html_comment)
            self.assertTrue(self.is_html_comment)
    #Testing if Parse correctly ignores incorrectly formatted HTML comments
    def test_incorrect_html_comments(self):
        HTML_test_not_comments = ["   <!this is not a comment", "<!nor is this", "!----this is also not a comment", "-- and this also isn't"]
        for html_comment in HTML_test_not_comments:
            self.is_html_comment = parse.check_comment_line(html_comment)
            self.assertFalse(self.is_html_comment)


    # ** PYTHON/RUBY/UNIX BASH/PERL SINGLE LINE COMMENTS ** 

    #Testing if Parse correctly identfies properly formated Python/Ruby/Bash/Perl single line comments
    def test_correct_python_singleline_comments(self):
        PYTHON_test_comments = ["   #HAHAHAHA this is a comment", "### as is this", "#this is also a comment", "# <!-- and this also"]
        for python_comment in PYTHON_test_comments:
            self.is_python_comment = parse.check_comment_line(python_comment)
            self.assertTrue(self.is_python_comment)
    #Testing if Parse correctly ignores incorrectly formatted Python/Ruby/Bash/Perl single line comments
    def test_incorrect_python_singleline_comments(self):
        PYTHON_test_not_comments = ["   <# this is not a comment", "'##nor is this", "!---###this is also not a comment", "-##- and this also isn't"]
        for python_comment in PYTHON_test_not_comments:
            self.is_python_comment = parse.check_comment_line(python_comment)
            self.assertFalse(self.is_python_comment)


     # ** PYTHON BLOCK COMMENTS ** 

    # Test to see if function correctly identfies properly formatted python block comments
    def test_correct_python_block_comments(self):
        PYTHON_BLOCK_test_comments = ["   '''HAHAHAHA this is a comment", '""" as is this', " '''this is also a comment", '""" <!-- and this also']
        for python_block_comment in PYTHON_BLOCK_test_comments:
            self.is_python_block_comment = parse.check_comment_line(python_block_comment)
            self.assertTrue(self.is_python_block_comment)
    # Test to see if function correctly ignores wrongly formatted python block comments
    def test_incorrect_python_block_comments(self):
        PYTHON_BLOCK_test_not_comments = [" ''  <# this is not a comment", "''##nor is this", ' ""!---###this is also not a comment', "''-##- and this also isn't"]
        for python_comment in PYTHON_BLOCK_test_not_comments:
            self.is_python_comment = parse.check_comment_line(python_comment)
            self.assertFalse(self.is_python_comment)

    # ** Java/C/C++/C#/Javascript/ObjectiveC ** 

    # Test to see if function correctly identfies properly formatted comments
    def test_correct_java_comments(self):
       	JAVA_test_comments = ["   //HAHAHAHA this is a comment", '////as is this', " //d//this is also a comment", '// <!-- and this also']
        for java_comment in JAVA_test_comments:
            self.is_java_comment = parse.check_comment_line(java_comment)
            self.assertTrue(self.is_java_comment)
    # Test to see if function correctly ignores wrongly formatted comments
    def test_incorrect_java_comments(self):
        JAVA_test_not_comments = [" / this is not a comment", "<--/#nor is this", ' /!---###this is also not a comment', "/#-##- and this also isn't"]
        for java_comment in JAVA_test_not_comments:
            self.is_java_comment = parse.check_comment_line(java_comment)
            self.assertFalse(self.is_java_comment)


     # ** MultiLine Comments ** 

    # Test to see if function correctly identfies properly formatted comments
    def test_correct_multiline_comments(self):
        MULTILINE_test_comments = ["   /* HAHAHAHA this is a comment", '/*//as is this', " /**this is also a comment", '/*** <!-- and this also']
        for multiline_comment in MULTILINE_test_comments:
            self.is_multiline_comment = parse.check_comment_line(multiline_comment)
            self.assertTrue(self.is_multiline_comment)
    # Test to see if function correctly ignores wrongly formatted comments
    def test_incorrect_multiline_comments(self):
        MULTILINE_test_not_comments = [" */ this is not a comment", "<--/*nor is this", ' /!*--###this is also not a comment', "/#*##- and this also isn't"]
        for multiline_comment in MULTILINE_test_not_comments:
            self.is_multiline_comment = parse.check_comment_line(multiline_comment)
            self.assertFalse(self.is_multiline_comment)


     # ** MatLab Comments ** 

    # Test to see if function correctly identfies properly formatted comments
    def test_correct_matlab_comments(self):
        MATLAB_test_comments = ["%HAHAHAHA this is a comment", "%as is this", " %this is also a comment", '%and this also']
        for matlab_comment in MATLAB_test_comments:
            self.is_matlab_comment = parse.check_comment_line(matlab_comment)
            self.assertTrue(self.is_matlab_comment)
    # Test to see if function correctly ignores wrongly formatted comments
    def test_incorrect_matlab_comments(self):
        MATLAB_test_not_comments = [" */ this is not a comment", "<--/*nor is this", ' /!*--###this is also not a comment', "/#*##- and this also isn't"]
        for matlab_comment in MATLAB_test_not_comments:
            self.is_matlab_comment = parse.check_comment_line(matlab_comment)
            self.assertFalse(self.is_matlab_comment)

# This class will be responsible for testing just the check_for_default_flag function in parse.pu
# The different mini-functions within will check different kinds of flags
class Parse_CheckDefaultFlag(unittest.TestCase):

    #Checks to make sure that even lines with flags are NOT identified as comment flags if they are not a comment
    def test_for_flag_without_comment(self):
        non_comments_with_flags = ["This is a non-comment with a TODO flag", "**This is another noncomment with BROKEN", "''Another COMPLETED flag no comment"]

        for non_comment_with_flag in non_comments_with_flags:
            self.no_comment_flag = parse.check_for_default_flag(non_comment_with_flag)
            self.assertFalse(self.no_comment_flag)
    # checks to see if a TODO flag is correctly identified
    def test_for_TODO_flag(self):
        comments_with_TODO_flags = ["# This is a comment with a TODO flag", "// This is another comment with TODO", "'''Another TODO flag"]

        for comment_with_todo in comments_with_TODO_flags:
            self.todo_flag = parse.check_for_default_flag(comment_with_todo)
            self.assertEqual(self.todo_flag,"TODO")

    # checks to see if a COMPLETED flag is correctly identified
    def test_for_COMPLETED_flag(self):
        comments_with_COMPLETED_flags = ["# This is a comment with a COMPLETED flag", "// This is another comment with COMPLETED", "'''Another COMPLETED flag"]

        for comment_with_completed in comments_with_COMPLETED_flags:
            self.completed_flag = parse.check_for_default_flag(comment_with_completed)
            self.assertEqual(self.completed_flag,"COMPLETED")
    # checks to see if a BROKEN flag is correctly identified
    def test_for_BROKEN_flag(self):
        comments_with_BROKEN_flags = ["# This is a comment with a BROKEN flag", "// This is another comment with BROKEN", "'''Another BROKEN flag"]

        for comment_with_broken in comments_with_BROKEN_flags:
            self.broken_flag = parse.check_for_default_flag(comment_with_broken)
            self.assertEqual(self.broken_flag,"BROKEN")

    #I got lazy and didn't write the taste cases for the rest of the default flags because I don't think 
    # we need all those tests. They're repetitive and the ones above I think are sufficient enough
    # to test the function. I will, however, add tests cases to test user supplied flags eventually

# This class will be responsible for testing the check_empty function in parse.py
class Parse_CheckEmpty(unittest.TestCase):
    
    # Tests to see if a given line is correctly identified as being empty
    def testEmpty(self):

        empty_line = "    "

        self.isLineEmpty = parse.check_empty(empty_line)
        self.assertTrue(self.isLineEmpty)
    # Tests to see if a given line is correctly identifed as being NOT empty
    def testNotEmpty(self):

        second_line = "     sdfsdf "
        self.isSecondLineEmpty = parse.check_empty(second_line)
        self.assertFalse(self.isSecondLineEmpty)

        

if __name__ == '__main__':
    unittest.main()
