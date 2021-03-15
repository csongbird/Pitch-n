REQ_DIR = requirements
LINTER = flake8
API = source

FORCE:


tests: FORCE
	cd $(API); make tests

prod: tests
	- git commit -a
	git push origin master

dev_env: FORCE
	python3 -m pip install -r $(REQ_DIR)/dev.txt

