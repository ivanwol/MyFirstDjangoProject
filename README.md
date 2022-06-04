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

Tag now:
1) Y - year(4 symbols)
2) F - month(full)
3) j - day
4) N - month(cut version)
5) P - time
6) y - year(2 symbols)

HTML дает возможность работать с блоком if с помощью тегов:
    {% if n > 0 %}
        <p>Число положительное</p>
    {% elif n < 0 %}
        <p>Число отрицательное</p>
    {% else %}
        <p>Что-то пошло не так</p>
    {% endif %}

В HTML есть цикл for:
    <ul>
        {% for i in country %}
        <li>{{ i }}</li>
        {% endfor %}
    </ul>