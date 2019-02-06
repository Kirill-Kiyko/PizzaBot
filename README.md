# PizzaBot

PizzaBot is a testing bot, created using FSM and Django REST framework

## Installation

Pizzabot use:
- python3.5.2
- Django==2.1.3
- djangorestframework==3.8.2
- transitions==0.6.9

Install Django and Django REST:

```
$ pip3 install django

$ pip3 install djangorestframework

$ pip3 install markdown

$ pip3 install django-filter
```

Install transitions:

```
$ pip3 install transitions
```

## Usage

Bot use predefined token for TelegramAPI. You can replace it with own:

```python
TELEGRAM_URL = 'https://api.telegram.org/bot{TOKEN}/'
```

After cloning repository, use this commands:

```
$ cd PizzaBot

$ python3 manage.py makemigrations

$ python3 manage.py migrate
```

Run bot using this command:

```
$ python3 manage.py runserver
```

It will start local server on 127.0.0.1:8000
