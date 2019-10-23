
help:
	@echo "Lemur CMS"
	@echo ""
	@echo "help              Show this help"
	@echo "install           Install Lemur CMS"
	@echo "load_fixtures     Load examples fixtures"
	@echo "run_backend       Start backend server"
	@echo "run_frontend      Start frontend server"

install:
	virtualenv -p python3 venv
	. venv/bin/activate && \
	pip install -r requirements.txt && \
	python manage.py migrate && \
	python manage.py createsuperuser && \
	$(MAKE) load_fixtures
	cd frontend && npm install

load_fixtures:
	. venv/bin/activate && \
	python manage.py loaddata fixtures/pages.json

run_backend:
	. venv/bin/activate && \
	python manage.py runserver

run_frontend:
	cd frontend && npm start
