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
Now all we need to do to start using the auth app is to include its urls and define some templates. Let's start by adding the urls first. Open up the project `urls.py` file. It should look like this,

```
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

Include the auth urls. We will also add a redirection to the user profile from the root. After the modification your `urls.py` should look like this,

```
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='/accounts/profile/', permanent=True)),
]
```
Now if you run the application with `python manage.py runserver` and try to navigate to `http://localhost:8000/` you will be redirected to `http://localhost:8000/accounts/profile/` and be presented with a beautiful *Page not found (404)* error page.

So the first thing we're going to do is create a profile page for the user, so that Django no longer bugs us with such a *404* page.

### User Profile

We will create a enw Django app for this. Let's call the app `accounts`.

* Go ahead and run `python manage.py startapp accounts`.
* Add this app to the list of your installed apps

```
INSTALLED_APPS = [
    ...
    'accounts',
]
```
* Create a view, we'll use a `TemplateView`

```
from django.views.generic import TemplateView


class UserProfile(TemplateView):
    template_name = 'accounts/profile.html'
```

* Update the projects `urls.py`, add the following to `urlpatterns`,

```
path('accounts/', include('accounts.urls')),
```

* Create `accounts/urls.py` and add the following,

```
from django.urls import path

from accounts.views import UserProfile


urlpatterns = [
    path('profile/', UserProfile.as_view(), name='profile'),
]
```

* Create tempalte folders, `accounts/templates/accounts`. Add the base template as `accounts/templates/base.html` and profile template as `accounts/templates/accounts/profile.html` and we are done. Please refer to the repository for the template codes.
