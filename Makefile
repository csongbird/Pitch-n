REQ_DIR = requirements
LINTER = flake8
API = flask_api

FORCE:


tests: FORCE
	cd $(API); make tests

unit: FORCE
	nosetests --exe --verbose --with-coverage --cover-package=.

lint: FORCE
	$(LINTER) $(API)/*.py

prod: tests
	- git commit -a
	git push origin master

dev_env: FORCE
	python3 -m pip install -r $(REQ_DIR)/dev.txt

