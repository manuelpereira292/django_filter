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
