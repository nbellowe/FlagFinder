import parse


HTML_test_comments = ["   <!--HAHAHAHA this is a comment", "<!-- as is this", "<!----this is also a comment", "TODO"]

comments = ["# - TODo this is not a good example", "<!-- as is TODO this", "//COMPLETED is also a comment", "/*NEEDS-APPROVAL TODO"]




def testHTML():
    print ("Testing check_comment_line for HTML comment tags")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for html_comment in comments:
        print(html_comment)
        print (parse.check_comment_line(html_comment))
        print ("")







print (" * * * * * * *")
testHTML()
