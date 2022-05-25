Create GIT Repository:
1) git init,
2) git remote add origin <link>,
3) git add .,
4) git status,
5) commit,
6) push.

Create Django Project:
1) python -m pip install Django,
2) django-admin startproject name.

Create Django app:
1) python manage.py startapp firstapp.

Run Django Project:
1) python manage.py runserver.

Create Django migrations:
1) python manage.py makemigrations,
2) python manage.py migrate.

Create Super user:
1) python manage.py createsuperuser.

List Template meaning:
1) BACKEND: ключ который указывает что исзпользуется Django templates.
2) DIRS: указывает где хранятся Djabgo templates
3) APP_DIRS: искать только в папке templates?
4) OPTIONS: опции которые изпользуем в django проекте