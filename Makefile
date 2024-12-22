.PHONY: run-backend run-frontend run install t_extract t_update t_extract_update t_compile
run-backend:
	python backend/app.py

run-frontend:
	python frontend/app.py

run:
	python run.py

install:
	pip install -r requirements.txt


t_extract:
	pybabel extract -F babel.cfg -o messages.pot .

t_update:
	pybabel update -i messages.pot -d translations

t_extract_update:
	t_extract; t_update

t_compile:
	pybabel compile -d translations
