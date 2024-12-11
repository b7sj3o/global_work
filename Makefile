.PHONY: run-backend
run-backend:
	uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload

.PHONY: run-frontend
run-frontend:
	python frontend/app.py

.PHONY: run
run:
	python run.py

.PHONY: install
install:
	pip install -r requirements.txt


