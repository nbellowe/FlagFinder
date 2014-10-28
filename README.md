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
		Label each line with a flag --> 1 char or int per line. 
			Comment
			Flag detected
			Starts new method
			Ends method
			New flag
	args:
		-h help
		-p parser
		-s --settings 
		-l --list 
	
	
http://cliff.readthedocs.org/en/latest/demoapp.html
   
