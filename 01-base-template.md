# 🧭 Django Minimal Setup (Bootstrap + Hello World)

```bash
# Go to your working folder
$ cd /home/user/Public/web

# Create project folder <django_folder>
$ mkdir dstock
$ cd dstock

# Create and activate virtual environment
$ python3 -m venv venv
$ source venv/bin/activate

# Upgrade pip
(venv) $ pip install --upgrade pip

# Install Django
(venv) $ pip install Django

# Create Django project (named core)
(venv) $ django-admin startproject core .

# Create apps folder
(venv) $ mkdir apps

# Create a normal app (Django doesn't support dot paths here)
(venv) $ python manage.py startapp uom

# Move it into the apps folder
(venv) $ mv uom apps/

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
│   ├── base.html
│   ├── 404.html                          
│   └── uom/
│       └── index.html
├── static/
└── venv/
```

---

### ⚙️ Update `settings.py`

Open `core/settings.py` and edit:

```python
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent

# Add apps folder to Python path
sys.path.insert(0, str(BASE_DIR / 'apps'))

# Local development
DEBUG = True
ALLOWED_HOSTS = []

# If you want DEBUG = False (like production)
# DEBUG = False
# ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

SECRET_KEY = 'The quick brown fox jumps over the fence.'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'uom',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
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
