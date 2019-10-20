
help:
	@echo "Lemur CMS"
	@echo ""
	@echo "help              Show this help"
	@echo "install           Install Lemur CMS"
	@echo "run               Start backend server"

install:
	virtualenv -p python3 venv
	. venv/bin/activate && \
	pip install -r requirements.txt && \
	python manage.py migrate && \
	python manage.py createsuperuser && \
	python manage.py loaddata fixtures/pages.json fixtures/articles.json && \
	cd frontend && npm install

load_fixtures:
	. venv/bin/activate && \
	python manage.py loaddata fixtures/pages.json fixtures/articles.json

run_backend:
	. venv/bin/activate && \
	python manage.py runserver

run_frontend:
	cd frontend && npm start
