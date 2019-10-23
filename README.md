# Lemur CMS 

## Installation


Be sure you have installed **npm and node**.

Clone this repository:

```shell script
git clone https://github.com/lemur-cms/lemur-cms
cd lemur-cms
```
### Installation - using make

Run installtion:
```shell script
make install
```

Then run backend server:

```shell script
make run_backend:
```

And React frontend server:

```shell script
make run_frontend:
```

Visit REST API on ``http://localhost:8000/api/``.  
Open ``http://localhost:3000/`` and enjoy React!

### Installation - step by step

Setup a virtualenv:

```shell script
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

There is a sqlite database called lemur_db by default.

Run migrations and create a superuser:

```shell script
python manage.py migrate
python manage.py createsuperuser
```

Import the fixtures:

```shell script
python manage.py loaddata fixtures/pages.json
```

Start backend server:

```shell script
python manage.py runserver
```

Install **React** frontend:

```shell script
cd frontend
npm install
```

Start frontend server:

```shell script
npm start
```
