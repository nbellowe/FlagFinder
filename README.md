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
		-h help 
		-p parser
		-s --settings 
		-l --list 
	
	
http://cliff.readthedocs.org/en/latest/demoapp.html
   
