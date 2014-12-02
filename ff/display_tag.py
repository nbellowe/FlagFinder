import logging
import os

from cliff.show import ShowOne





class Tag:

    # All of these attributes will be extracted from the comment line after it has gone through parse.py
    # We'll have to find a way to store this information for each line of code that is a comment (each comment_line). 
    # Maybe Nathans highperfomance tuple thing will work well
    # I am hardcoding these values for demonstration purposes only, these will be filled in dynamically as we parse each
    # line of code of the file and then store them somewhere so they can be retrieved when the user calls ff -d [someTag]
    # I hardcoded these values just so I can see how Cliff(ShowOne) would display them. If you run ff d you can test it!    

    tagContent = " # This is a sample tag with the flag TODO in it"
    tagLineNumber = 37 # not sure how we would go about extracting this but I think it would be cool to have this info associated with every tag
    tagFileName = "testMain.py" # name of the file from which the tag was found, shouldn't be too hard to extract
    tagLanguage = "Python" # name of language used, or at least range of possible languages based off of the type of comment syntax
    tagFlag = "TODO" # if any kind of flag is identified, it'll be added as part of the tags information
    tagNumberOfLines = 1 #how many lines the comment is (could be a multiline comment )

    # Again I want to restate that THIS IS NOT A FINAL SOLUTION/IMPLEMENTATION. This is just kind of how I had envisioned us 
    # extracting/storing information about each tag and then using Cliffs ShowOne class/library thingamajig to display it nicely. 
    # Formatting the information is easy (obviously, Cliff does that for us), and setting it up for ShowOne to display is also easy
    # (simply enter the columns and then the data as its setup below), it'll be extracting this information and then somehow storing it 
    # somewhere (hidden data file?? seems much simpler than setting up entire DB) that will be the more difficult part



class DispTag(ShowOne):
    "Show details about a tag"
   
    log = logging.getLogger(__name__)
    
    def take_action(self, parsed_args):
    
     
        sampleTag = Tag()
        self.app.stdout.write(sampleTag.tagContent)
        self.app.stdout.write("\n")    
        columns = ('Beginning Of Tag',
                   'Line-Number',
                   'File-Name',
                   'Language',
                   'Flag',
                   'Number of Lines',
                   )
        data = (sampleTag.tagContent.strip()[:10], # Ideally, we would show the first several characters AFTER the comment syntax, avoid repitition 
                sampleTag.tagLineNumber, 
                sampleTag.tagFileName,
                sampleTag.tagLanguage,
                sampleTag.tagFlag,
                sampleTag.tagNumberOfLines,
                )
        return (columns, data)
