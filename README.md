simple-translate
====
![travis](https://travis-ci.org/zhangoose/simple-translate.svg?branch=master)

WIP

### Local setup

```
git clone https://github.com/zhangoose/simple-translate.git
pip install -r requirements-dev.txt
```

You should have an `.env` file inside `app/` with the following:

```
DEBUG=True
POSTGRES_USERNAME=....
POSTGRES_PASSWORD=....
POSTGRES_HOST=....
POSTGRES_PORT=....
DJANGO_SECRET_KEY=...
API_TOKEN=...
```

You should also replace `app/translation/static/translation/env/env.js`'s `API_TOKEN` value with the `API_TOKEN` above in your `.env`.

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

