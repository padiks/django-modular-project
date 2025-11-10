# Stock - Django Modular CRUD

**Despatch** is a lightweight, modular **Django** application that demonstrates complete **CRUD (Create, Read, Update, Delete)** operations using an **SQLite** database. It’s designed as a learning project for building modular Django apps with blueprints, SQLAlchemy, and Bootstrap 5.

---

### 🌱 Django Modular Project Structure

```
dstock/
├── manage.py                              # Django management entrypoint
│
├── core/                                  # Project core (settings, URLs, WSGI)
│   ├── __init__.py
│   ├── settings.py                        # Centralized settings (DB, paths, debug, apps)
│   ├── urls.py                            # Root URL router, includes app-level URLs
│   ├── wsgi.py                            # WSGI entrypoint for Apache/mod_wsgi
│   └── asgi.py                            # Optional for async support (future-proof)
│
├── apps/                                  # Your modular app collection
│   ├── __init__.py
│   │
│   ├── categories/                        # Module 1: Categories
│   │   ├── __init__.py
│   │   ├── admin.py                       # Admin registration
│   │   ├── apps.py                        # Django app config
│   │   ├── models.py                      # Models (tables)
│   │   ├── urls.py                        # App-specific routes
│   │   ├── views.py                       # Views (controllers)
│   │   ├── forms.py                       # Optional (forms for CRUD)
│   │   ├── tests.py                       # Optional tests
│   │   └── templates/
│   │       └── categories/
│   │           └── index.html             # App-level template
│   │
│   ├── uom/                               # Module 2: Units of Measure
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── templates/
│   │       └── uom/
│   │           └── index.html
│   │
│   └── utils/                             # Shared helpers (non-model logic)
│       ├── __init__.py
│       └── helpers.py                     # Markdown rendering, formatting, etc.
│
├── templates/                             # Global templates shared across all apps
│   ├── base.html                          # Base layout (extends in all app templates)
│   ├── 404.html                           # Optional: custom error page
│   └── includes/                          # For reusable template parts (header/footer)
│       ├── header.html
│       └── footer.html
│
├── static/                                # Shared static files (CSS/JS/Images)
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── mode.js
│   └── img/
│       └── book_207114.png
│
└── db.sqlite3                             # SQLite database
```

---

### ⚙️ Highlights

| Flask Concept         | Django Equivalent                     | Notes                                                                 |
| --------------------- | ------------------------------------- | --------------------------------------------------------------------- |
| `app.py`              | `manage.py` + `core/settings.py` | Django uses `manage.py` and project settings for initialization.      |
| `config.py`           | `settings.py`                         | All environment, DB, and path configs go here.                        |
| Blueprints in `apps/` | Django “apps” in `apps/`              | Same modularity pattern — each app has its own models, views, URLs.   |
| `routes.py`           | `urls.py` + `views.py`                | Django separates routing and view logic.                              |
| Shared utilities      | `apps/utils/`                         | Works exactly like Flask’s shared modules.                            |
| Templates per module  | `apps/<module>/templates/<module>/`   | Django finds them automatically if configured in `TEMPLATES['DIRS']`. |
| Global templates      | `templates/`                          | Works the same — your `base.html`, `404.html`, etc.                   |
| Static files          | `static/`                             | Standard Django static collection folder.                             |
| Database              | `data/db.sqlite3`                     | You can point `DATABASES['default']['NAME']` to this path.            |

---

### 🧩 Example Django Root `urls.py`

```python
# core/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', include('apps.categories.urls')),
    path('uom/', include('apps.uom.urls')),
]
```

---

### 🪶 Example App URL + View (like Flask’s routes.py)

**apps/uom/urls.py**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='uom_index'),
]
```

**apps/uom/views.py**

```python
from django.shortcuts import render

def index(request):
    return render(request, 'uom/index.html')
```

---

### 🧭 Django Minimal Modular Setup (Using Existing SQLite Database)

```bash
# Go to your working folder
$ cd /home/user/Public/web

# Create a new project folder
$ mkdir django_folder
$ cd django_folder

# Create and activate virtual environment
$ python3 -m venv venv
$ source venv/bin/activate

# Upgrade pip
(venv) $ pip install --upgrade pip

# Install Django
(venv) $ pip install Django

# Create the main Django project (named dstock)
(venv) $ django-admin startproject dstock .

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

### 🧭 Django Minimal Setup (Bootstrap + Hello World)

```bash
# Go to your working folder
$ cd /home/user/Public/web

# Create project folder
$ mkdir django_folder
$ cd django_folder

# Create and activate virtual environment
$ python3 -m venv venv
$ source venv/bin/activate

# Upgrade pip
(venv) $ pip install --upgrade pip

# Install Django
(venv) $ pip install Django

# Create Django project (dstock)
(venv) $ django-admin startproject dstock .

# Create apps folder
(venv) $ mkdir apps

# Create sample module uom
(venv) $ python manage.py startapp apps.uom

# Create templates and static folders
(venv) $ mkdir templates static
```

---

### 🗂️ Verify Structure

```
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
│   └── uom/
│       └── index.html
├── static/
└── venv/
```

---

### ⚙️ Update `settings.py`

Open `core/settings.py` and edit:

```python
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add apps folder to Python path
import sys
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Minimal installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.uom',
]

# Templates and static files
TEMPLATES[0]['DIRS'] = [os.path.join(BASE_DIR, 'templates')]
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

---

### 🧩 Minimal Home Page View

Create `apps/uom/views.py`:

```python
from django.shortcuts import render

def index(request):
    return render(request, 'uom/index.html')
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

---

### 🏗️ Templates

**`templates/base.html`** (Bootstrap via CDN):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Django App{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-4">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

**`templates/uom/index.html`**:

```html
{% extends 'base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
<h1 class="text-center">Hello World</h1>
{% endblock %}
```

---

### 🚀 Run It

```bash
(venv) $ python manage.py runserver 4444
```

Open in browser:
👉 [http://127.0.0.1:4444/](http://127.0.0.1:4444/)

You should see **Hello World** centered on the page with Bootstrap styling.

---

### License

This project is intended for learning purposes.
