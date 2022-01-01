# djangoblog 

A blogging platform built on Django and Python – deployed with PythonAnywhere.com.

![Snake Gif](https://i0.wp.com/europeisnotdead.com/wp-content/uploads/2020/05/Czechia-European-Animal-Related-Idioms-Dráždit-hada-bosou-nohou.gif?fit=300%2C300&ssl=1)

## Django Basics

### Running the server

The Django server is started via the runserver command.

```bash
python3 manage.py runserver
```

### Initialising the Admin Panel with a user

```bash
python3 manage.py createsuperuser
```

Once you have a user setup, you can access Django's awesome Admin panel at /admin/. For added security this url can be changed to something more obscure via ```/mysite/urls.py```

[Thanks to DjangoGirls for the great learning materials](https://tutorial.djangogirls.org)
