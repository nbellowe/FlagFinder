FlagFinder
==========

Alex Tzinov
Nathan Bellowe
Jason Kinnard

Software that will allow programmers to organize their code within their code, without having to worry about creating a clean, organized set of tasks in the future.
#How it works
	Searches up all directories until it finds a .flagfinder.yaml file (or something similar)
	Possible settings for .flagfinder.yaml
		Possible flags
		File masks
		.flagfinder/
			history/
		Use git .ignore
	
	In each file:
		Parse each file into lines 
		#Label each line with a flag --> 1 char or int per line. (Haven't implemented, maybe `Jason` would like to?
			in process
		#Return a mashup of that info. `Jason`
	Write specs
	Write random general crap to make us look good (this project is >2 hours from completion if someone wanted to, but could extend into 20-1000 hrs of work, you know?)
		

	args:
	Someone should implement these, that isn't named Nathan.
    I, Alexander the Great, will start working on implementing these at some point. Also, Do you guys think we should make a man page? 
    Because I can throw one together the next couple of days if you guys think we need one
		-h help  
		-p parser (main meat of program)
		-s --settings (user can reach/edit config file through here I'm assuming) 
		-l --list  (list of all tags found?)
        -d [TAG] --display (Display information about tag. ie: what file, what line number, language of comment, what flag, etc)
	
	
http://cliff.readthedocs.org/en/latest/demoapp.html
   
