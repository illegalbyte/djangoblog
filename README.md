# djangoblog 👨‍💻

![Test Workflow](https://github.com/illegalbyte/djangoblog/actions/workflows/django.yml/badge.svg)

<p float="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-original.svg" width="100" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-plain.svg" width="100" /> 
</p>

A blogging platform built on Django and Python – deployable with PythonAnywhere.com.

![Snake Gif](https://i0.wp.com/europeisnotdead.com/wp-content/uploads/2020/05/Czechia-European-Animal-Related-Idioms-Dráždit-hada-bosou-nohou.gif?fit=300%2C300&ssl=1)

## Functionality

A list of existing and planned functionality for my DjangoBlog project.

- [X] Build models for article content and link with Django admin console
- [X] Ability to publish posts via the admin console
- [X] Publish new posts via a webform
- [X] Edit existing posts
- [X] Hide the edit functionality for non-authenticated users
- [X] Add tests for requesting index page
- [X] Add tests for requesting an individual post's page
- [X] Add tests for submitting an edit
- [ ] Add tests for posting via webform
- [X] CI/CD using GitHub Actions
- [ ] Function to create draft posts
- [ ] Additional security via Django decorators and login url
- [ ] Add comment function

## Django Basics

### Running the server

The Django server is started via the runserver command.

```Shell
python3 manage.py runserver
```

### Initialising the Admin Panel with a user

```Shell
python3 manage.py createsuperuser
```

### PythonAnywhere

Updating static files (e.g. CSS) must be done manually via the PythonAnywhere bash console using the following command:

```Shell
python3 manage.py collectstatic
```

Once you have a user setup, you can access Django's awesome Admin panel at ```/admin/```. For added security this url can be changed to something more obscure via ```/mysite/urls.py```

### Adding models to the database

When creating a new Django project, you must create a models.py file. This file contains the database models. Any additions to the models.py file will only be reflected in the database if you run the following commands:

```Shell
python3 manage.py makemigrations blog
```

```Shell
python3 manage.py migrate blog
```

[Thanks to DjangoGirls for the amazing learning materials](https://tutorial.djangogirls.org)
