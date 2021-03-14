REQ_DIR = .
LINTER = flake8

FORCE:


tests: lint unit

unit: FORCE
	nosetests --exe --verbose --with-coverage --cover-package=.

lint: FORCE
	$(LINTER) *.py

prod: tests
	- git commit -a
	git push origin master

dev_env: FORCE
	python3 -m pip install --user -r $(REQ_DIR)/dev.txt

