# 🧭 Django Minimal Modular Setup (Using Existing SQLite Database)

```bash
# Go to your working folder
$ cd /home/user/Public/web

# Create a new project folder <django_folder>
$ mkdir dstock
$ cd dstock

# Create and activate virtual environment
$ python3 -m venv venv
$ source venv/bin/activate

# Upgrade pip
(venv) $ pip install --upgrade pip

# Install Django
(venv) $ pip install Django

# Create the main Django project (named core)
(venv) $ django-admin startproject core .

# Create apps folder for modular structure
(venv) $ mkdir apps

# Create sample modules (uom and categories)
(venv) $ python manage.py startapp apps.uom
(venv) $ python manage.py startapp apps.categories

# Create folders for shared templates, static, and data
(venv) $ mkdir templates static data

# Copy your existing SQLite database into root
(venv) $ cp /path/to/your/db.sqlite3 ./db.sqlite3

# (No migrations needed — we are using existing database)
```

---

### 🗂️ Verify Structure

```bash
$ tree -L 2

dstock/
├── manage.py
├── core/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   ├── __init__.py
│   └── uom/
├── templates/
│   ├── base.html
│   ├── 404.html 
│   └── uom/
│       └── index.html
├── static/
└── venv/
```

---

### ⚙️ Update `settings.py`

Open `core/settings.py` and edit a few lines:

```python
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add your apps folder to Python path
import sys
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Database (use existing SQLite in /db.sqlite3)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Add your modular apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.uom',
    'apps.categories',
]

# Templates and static files
TEMPLATES[0]['DIRS'] = [os.path.join(BASE_DIR, 'templates')]
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

---

### 🧩 Example Quick Test View

Create `apps/uom/views.py`:

```python
from django.shortcuts import render
from django.db import connection

def index(request):
    # Example: query existing database table directly
    with connection.cursor() as cursor:
        cursor.execute("SELECT name FROM your_table LIMIT 5")
        rows = cursor.fetchall()

    return render(request, 'uom/index.html', {'rows': rows})
```

Create `apps/uom/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='uom_index'),
]
```

Include it in `core/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.uom.urls')),
]
```

Create `templates/uom/index.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Django UOM</title>
</head>
<body>
    <h1>Database rows</h1>
    <ul>
        {% for row in rows %}
            <li>{{ row.0 }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

---

### 🚀 Run It

```bash
(venv) $ python manage.py runserver 4444
```

Then open in browser:
👉 [http://127.0.0.1:4444/](http://127.0.0.1:4444/)

You should see the first few rows from your database table displayed.

---

### License

This project is intended for learning purposes.
