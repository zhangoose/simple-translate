simple-translate
====
![travis](https://travis-ci.org/zhangoose/simple-translate.svg?branch=master)

WIP

### Local setup

```
git clone https://github.com/zhangoose/simple-translate.git
pip install -r requirements.txt
```

You should have an `.env` file inside `app/` with the following:

```
DEBUG=True
POSTGRES_USERNAME=....
POSTGRES_PASSWORD=....
POSTGRES_HOST=....
DJANGO_SECRET_KEY=...
```

### Running locally

```
python manage.py migrate
python manage.py runserver
```

### Tests

Tests powered by py.test

```
pytest tests/
```

