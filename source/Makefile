LINTER = flake8
SRC_DIR = source

FORCE:

docs: FORCE
	pydoc3 $(SRC_DIR).endpoints
	pydoc3 $(SRC_DIR).db
	
%.html: %.py
	pydoc3 -w ./$<
	git add $@
	
tests: lint unit

unit: FORCE
	nosetests --exe --verbose --with-coverage --cover-package=$(SRC_DIR)

lint: FORCE
	$(LINTER) *.py

