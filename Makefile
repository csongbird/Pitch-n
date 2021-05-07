LINTER = flake8
API = source
set FLASK_APP=source
FORCE:

tests: FORCE
	cd $(API); make tests

prod: tests
	- git commit -a
	git push origin main

dev_env: FORCE
	python3 -m pip install -r dev.txt

heroku:
	# install heroku
	curl https://cli-assets.heroku.com/install.sh | sh
	heroku apps:create sd-pitch-n
	heroku login
	# set up heroku app as remote for this repo
	heroku git:remote -a sd-pitch-n
	heroku config:set PYTHONPATH="/app"
	heroku config:set GAME_HOME="/app"
	echo "web: gunicorn source.endpoints:app" > Procfile

docs: FORCE
	cd $(API); make docs

site:
	FLASK_APP=$(API)
	flask run
