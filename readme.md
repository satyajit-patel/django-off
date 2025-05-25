#### some usefull commands
```
python -m venv .venv
.venv\Scripts\activate
py -m pip install Django
django-admin startproject projectName
cd projectName
    python manage.py runserver
    python manage.py startapp appName
    python manage.py migrate // removes unapplied migration errors
deactivate
```

#### flow
user -> req -> urls.py -> views.js -> res -> user