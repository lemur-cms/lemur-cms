# Lemur CMS 

## Installation

Be sure you have installed **npm and node**.

Clone this repository:

```bash
git clone https://github.com/lemur-cms/lemur-cms
cd lemur-cms
```

Setup a virtualenv:

```bash
python -p python3 venv
. venv/bin/activate
pip install -r requirements.txt
```

There is a sqlite database called lemur_db by default.

Run migrations and create a superuser:

```bash
./manage.py migrate
./manage.py createsuperuser
```

Import the fixtures:

```bash
./manage.py loaddata fixtures/pages.json
```

Start backend server:

```bash
./manage.py runserver
```

Install **React** frontend:

```bash
cd frontend
npm install
```

Start frontend server:

```bash
npm start
```

Visit REST API on ``http://localhost:8000/api/``.  
Open ``http://localhost:3000/`` and enjoy React!
