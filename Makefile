help:
	@echo "install - install from source"
	@echo "docs    - generate HTML documentation"
	@echo "clean   - remove build artifacts"

release: docs
	cd scripts && sudo rm -rf dist build
	cd scripts && sudo python setup.py sdist upload

sdist: docs
	cd scripts && sudo python setup.py sdist
	ls -l dist

install: 
	cd scripts && sudo python setup.py install

clean:
	cd scripts && sudo rm -rf dist build *.egg-info
	(cd docs && sudo make clean)

.PHONY: docs
docs:
	(cd docs && sudo make clean html)
