#### Some usefull commands
```
python -m venv .venv
.venv\Scripts\activate
py -m pip install Django
django-admin startproject projectName
cd projectName
    python manage.py runserver
    python manage.py startapp appName
    python manage.py createsuperuser
    pip install pillow
    python manage.py makemigrations appName
    python manage.py migrate
deactivate
```

#### Flow
user -> req -> urls.py -> views.js -> res -> user