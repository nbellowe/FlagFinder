FlagFinder
==========

Alex Tzinov
Nathan Bellowe
Jason Kinnard

Software that will allow programmers to organize their code within their code, without having to worry about creating a clean, organized set of tasks in the future.
#Organization:

Our repository was organized into 3 main subfolders for documentation, data, and source code files. Additionally, the top folder held simple development scripts and configuration files. 
`
scripts
ff
data
`
#How it works
	Parses file comments into database.
	Searches this database to find comments
	Displays it in friendly format

##Necessary Libaries
	
	python-dev
	libsqlite3-dev

##Installing
	cd FlagFinder
	python setup.py install

##How To Use
	ff start
	* follow instructions *

##To Run Test Cases
	cd ff
	tox

##To release
	`cd ff && rm -rf dist build`
	cd ff && python setup.py sdist upload`
##To create distributable
	`cd ff && python setup.py sdist
	ls -l dist`

##To Clean:
	`cd ff && rm -rf dist build *.egg-info
	(cd docs && make clean)`

##Build docs
	`(cd docs && make clean html)`
