FlagFinder
==========

Alex Tzinov
Nathan Bellowe
Jason Kinnard

Software that will allow programmers to organize their code within their code, without having to worry about creating a clean, organized set of tasks in the future.
#How it works
	Parses file comments into database.
	Searches this database to find comments
	Displays it in friendly format
	
##To release
	`cd scripts && rm -rf dist build
	cd scripts && python setup.py sdist upload`
##To create distributable
	`cd scripts && python setup.py sdist
	ls -l dist`

##To install from source
	`cd scripts && python setup.py install`

##To Clean:
	`cd scripts && rm -rf dist build *.egg-info
	(cd docs && make clean)`
##Validation testing:
	`cram -v ./tests/cram`

##Verification Testing:
	`tox ./tests/tox`

##Build docs
	`(cd docs && make clean html)`
	
#Development Dependencies:
`pip install Sphinx`
`pip install docutils`
`pip install tox`
