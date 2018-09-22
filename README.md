Steps for creating virtual environment:

1. mkdir django_project
2. cd django_project
3. install python3
4. python3 -m venv django_env
5. . django_env/bin/activate .... (to activate envirnoment)
6. pip install django==1.9
7. django-admin startproject ProjectName
8. python manage.py runserver
9. python manage.py startapp APPNAME


....
1. python manage.py showmigrations
2. python manage.py makemigrations
3. python manage.py migrate
