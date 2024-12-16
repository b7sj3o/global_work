.PHONY: run-backend
run-backend:
	python backend/app.py

.PHONY: run-frontend
run-frontend:
	python frontend/app.py

.PHONY: run
run:
	python run.py

.PHONY: install
install:
	pip install -r requirements.txt


