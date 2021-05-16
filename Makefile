export PYTHONPATH=${CURDIR}
LINTER = flake8
API = source

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
	heroku config:set FLASK_APP=$(API)
	heroku config:set FLASK_ENV=development
	echo "web: gunicorn source.app:app" > Procfile

docs: FORCE
	cd $(API); make docs
