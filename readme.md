#### some usefull commands
```
python -m venv .venv
.venv\Scripts\activate
py -m pip install Django
django-admin startproject projectName
cd projectName
    python manage.py runserver
    python manage.py startapp appName // make sure to tell the project that we have a new app now
deactivate
```

- flow
user -> req -> urls.py -> views.js -> res -> user