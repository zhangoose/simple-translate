simple-translate
====
![travis](https://travis-ci.org/zhangoose/simple-translate.svg?branch=master)

An application that takes inputted text, detect its language, and translate it into English. Also able to display historical translations.

Translations done using [Transltr.org](http://transltr.org/)'s API (thank you!!!).

![preview](https://d17oy1vhnax1f7.cloudfront.net/items/063y1b0b1J1j2k3h0W3g/Screen%20Recording%202016-12-29%20at%2005.27%20PM.gif?v=9e8e58fe)

For now hosted on [Amazon EC2](http://ec2-35-166-234-91.us-west-2.compute.amazonaws.com/).

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

