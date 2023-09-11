install: 
	# install Commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format: 
	# format Commands
	black *.py &&\
		black */*.py
lint: 
	# pylint Commands
test:
	# test Commands
deploy:
	# deploy Commands
all: 
	install format lint test deploy