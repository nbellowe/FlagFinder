import logging
import os

from cliff.show import ShowOne





class Tag:

    # All of these attributes will be extracted from the comment line after it has gone through parse.py
    # We'll have to find a way to store this information for each line of code that is a comment (each comment_line). 
    # Maybe Nathans highperfomance tuple thing will work well
    # I am hardcoding these values for demonstration purposes only, these will be filled in dynamically as we parse each
    # line of code of the file and then store them somewhere so they can be retrieved when the user calls ff -d [someTag]

    tagContent = " # This is a sample tag with the flag TODO in it"
    tagLineNumber = 37
    tagFileName = "testMain.py"
    tagLanguage = "Python"
    tagFlag = "TODO"
    tagNumberOfLines = 1



class DispTag(ShowOne):

    log = logging.getLogger(__name__)
 
    print("This is your comment: \n")

    
    def take_action(self, parsed_args):
        
        sampleTag = Tag()
        print(sampleTag.tagContent)    
        columns = ('Beginning Of Tag',
                   'Line-Number',
                   'File-Name',
                   'Language',
                   'Flag',
                   'Number of Lines',
                   )
        data = (sampleTag.tagContent.strip()[:10], # display only the first several characters of the tag 
                sampleTag.tagLineNumber,
                sampleTag.tagFileName,
                sampleTag.tagLanguage,
                sampleTag.tagFlag,
                sampleTag.tagNumberOfLines,
                )
        return (columns, data)
