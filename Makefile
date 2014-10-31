help:
	@echo "install - install from source"
	@echo "docs    - generate HTML documentation"
	@echo "clean   - remove build artifacts"

release: docs
	cd scripts && rm -rf dist build
	cd scripts && python setup.py sdist upload

sdist: docs
	cd scripts && python setup.py sdist
	ls -l dist

install: 
	cd scripts && python setup.py install

clean:
	cd scripts && rm -rf dist build *.egg-info
	(cd docs && make clean)

.PHONY: docs
docs:
	(cd docs && make clean html)
