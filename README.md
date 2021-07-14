# django_filter

Django Dynamic Filter Form

Create github repositorie

Clone repositorie on VScode

Create virtual environment
py -m venv venv

Enter virtual environment
.\venv\scripts\activate

Install django
pip install django

Create file requirements.txt
Necessary apps for project
pip freeze > requirements.txt

Create project Django (the project is created in base folder with dot in the final)
django-admin startproject <project_name> .

Initialize server manage.py
py .\manage.py runserver

Open link
http://127.0.0.1:8000/

Create database apps - migrate
py manage.py migrate

Edit <project_name>/settins.py
```python
LANGUAGE_CODE = 'pt'
TIME_ZONE = 'Europe/Lisbon'
```

Create app users
py manage.py startapp users

Edit <project_name>/settins.py
```python
INSTALLED_APPS = [
    # Users apps
    'users.apps.UsersConfig',
]

# User Model

AUTH_USER_MODEL = 'users.User'
```

Copy users/admin.py
Copy users/apps.py
Copy users/forms.py
Copy users/models.py

Delete db.sqlite3

Create model - makemigrations
py manage.py makemigrations

Create database apps - migrate
py manage.py migrate

Create super user
py manage.py createsuperuser

