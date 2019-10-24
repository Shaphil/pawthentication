# Pawthentication (Default)

This app explores the default authentication views provided by Django as is. The only modification is the addition of two views for handling User registration and profile.

## Running the application

Typical way of running.

* Inside the project folder with an activated virtualenv, `pip install -r requirements.txt`
* Run the migrations, `python manage.py migrate`
* Creating a superuser is not necessary, but you can create one, `python manage.py createsuperuser`, follow the instructions afterwards.
* Run the application, `python manage.py runserver`

---

## Building the application

First let's create our Pawthentication Django project. Inside an activated virtual environment do the following.

1. Install Django, `pip install django`
2. Create the pawthentication project, `django-admin startproject pawthentication`

We are going to explore the default views provided by django. The authentication app is in `django.contrib.auth`. To use the app you need to make sure that you have it included in your `INSTALLED_APPS` settings. It is included by default when you create the project, so usually it looks like this by default,

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
