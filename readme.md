# Pawthentication

This app explores the default authentication views provided by Django as is. The only modification is the addition of two views for handling User registration and profile.

## Running the application

Typical way of running.

- Inside the project folder with an activated virtualenv, `pip install -r requirements.txt`
- Run the migrations, `python manage.py migrate`
- Creating a superuser is not necessary, but you can create one, `python manage.py createsuperuser`, follow the instructions afterwards.
- Run the application, `python manage.py runserver`

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

Now if you run the application with `python manage.py runserver` and try to navigate to `http://localhost:8000/` you will be redirected to `http://localhost:8000/accounts/profile/` and be presented with a beautiful _Page not found (404)_ error page.

So the first thing we're going to do is create a profile page for the user, so that Django no longer bugs us with such a _404_ page.

### User Profile

We will create a enw Django app for this. Let's call the app `accounts`.

- Go ahead and run `python manage.py startapp accounts`.
- Add this app to the list of your installed apps

```
INSTALLED_APPS = [
    ...
    'accounts',
]
```

- Create a view, we'll use a `TemplateView`

```
from django.views.generic import TemplateView


class UserProfile(TemplateView):
    template_name = 'accounts/profile.html'
```

- Update the projects `urls.py`, add the following to `urlpatterns`,

```
path('accounts/', include('accounts.urls')),
```

- Create `accounts/urls.py` and add the following,

```
from django.urls import path

from accounts.views import UserProfile


urlpatterns = [
    path('profile/', UserProfile.as_view(), name='profile'),
]
```

- Create tempalte folders, `accounts/templates/accounts`. Add the base template as `accounts/templates/base.html` and profile template as `accounts/templates/accounts/profile.html` and we are done. Please refer to the repository for the template codes.

### User Registration

Django doesn't provide a `RegistrationView` out of the box, so we will create our own. For the view we'll use a `generic.CreateView` and `UserCreationForm`. The code for the view looks like this,

```
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class RegistrationView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
```

Few things to notice here,

1. The `success_url` attribute. From the doc, it is _The URL to redirect to when the form is successfully processed._ We can see that it redirects to `login`, but we haven't defined a template yet. If the registration form submits successfully we'll be redirected to the `login` endpoint and be presented with a `TemplateDoesNotExist` error. So, we need to create a template for that. If you wondered why we are using `reverse_lazy()` instead of `reverse()`, please have a look at this answer from SO - [https://stackoverflow.com/a/48671384](https://stackoverflow.com/a/48671384)
2. We will put the template for this endpoint at the project templates folder, outside of the app's templates folder. That is where Django expects all the authentication templates to exist. We will keep it there because it made sense to me to keep the registration template with all the other authentication templates like login for example, so that it looks well organized. You can keep it anywhere you want.
3. Django forms are not very beautiful by default. We are using Bootstrap to make our site look nice, but that doesn't affect the form elements. You see, the form is handled by Django as an object and not your traditional html form elements that you can decorate to make it look nicer. When Django encounters a `{{ form }}` variable, _All the form’s fields and their attributes will be unpacked into HTML markup from that `{{ form }}` by Django’s template language._ (from Django doc). Thus you have less control over the looks of the elements. You can obviously do forms the old way using all html controls and handling everything by yourself. But the problem with that is that **YOU HAVE TO DO EVERYTHING BY YOURSELF.** To make our forms nice and shiny, we'll add an extension called the Crispy Forms.

Let's start by adding crispy forms to the project,

- `pip install --upgrade django-crispy-forms`.
- Add Crispy Forms to `INSTALLED_APPS`,

```
INSTALLED_APPS = [
    ...
    'crispy_forms',
]
```

- Select a _Template packs_ and add corresponding setting. We're going to choose `bootstrap4` so our setting looks like this, `CRISPY_TEMPLATE_PACK = 'bootstrap4'`.

Now we are all set to use Crispy Forms in our application. Let's create our registration template and start using it.

**N.B** These templates are going to reside directly under our project directory, outside of any app folder.

- From project root create folders `templates/registration`.
- Update `TEMPLATES['DIRS']` setting as follows

```
TEMPLATES = [
    {
        ...
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        ...
]
```

- Add the registration template to `templates/registration/register.html`. Please refer to the repository for the template code.

  - Inside the template load crispy form with this tag `{% load crispy_forms_tags %}`
  - Use the `crispy` filter to _render the form or formset using django-crispy-forms elegantly div based fields_, `{{ form | crispy }}`.

- Update `accounts.urls`,

```
from accounts.views import RegistrationView

urlpatterns = [
    ...
    path('register/', RegistrationView.as_view(), name='register'),
]
```

Navigate to [http://localhost:8000/accounts/register/](http://localhost:8000/accounts/register/) and you should see a nice registration form.
