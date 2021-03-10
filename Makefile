# Makefile

FORCE:

tests: FORCE
	flake8 *.py
	nosetests --with-coverage --cover-package=.

prod: tests
	git commit -a
	git push origin main

dev_env: FORCE
	pip install --user -r requirements/dev.txt

