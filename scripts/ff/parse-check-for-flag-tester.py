import parse


test_comments = ["# - TODo this is not a good example", "<!-- as is TODO this", "/*NEEDS-APPROVAL is also a comment", "/*NEEDS-APPROVAL TODO"]




def testTODO():
    print ("Testing check_for_flag for flag comments")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for comment in test_comments:
        print(comment)
        print (parse.check_for_flag(comment))
        print ("")







print (" * * * * * * *")
testTODO()
