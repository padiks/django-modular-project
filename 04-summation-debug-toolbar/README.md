# **Summation and Debug Toolbar Integration**

### **Short Description:**

A Django web application that allows users to input five numbers and compute their sum. Additionally, the project integrates the Django Debug Toolbar for enhanced development debugging, providing insights into requests, and more.

---

## **Project Structure**

```
dfemsum/
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
│   └── summation/
│       ├── __init__.py
│       ├── urls.py                        # App-specific routes
│       ├── views.py                       # Views (controllers)
│       └── templates/
│           └── summation/
│               └── index.html             # App-level template
│
├── templates/                             # Global templates shared across all apps
│   └── base.html                          # Base layout (extends in all app templates)
│
└── static/                                # Shared static files (CSS/JS/Images)
```

---

## **Guide 1: Setting up Django project environment (Debian)**

### **Step 1: Install Python and pip**

Check if Python 3 is installed:

```bash
python3 --version
```

Install Python 3 and pip if needed:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```

---

### **Step 2: Create the project folder**

Make sure you are in `/home/user/Public/web`:

```bash
mkdir dfemsum
cd dfemsum
```

This is your **project root folder**, as we discussed.

---

### **Step 3: Create a virtual environment**

It’s best practice to use a virtual environment per project:

```bash
cd /home/user/Public/web
python3 -m venv venv
```

This will create a folder `venv/` that contains all project dependencies isolated from the system Python.

Activate it:

```bash
source venv/bin/activate
```

Your terminal should now show `(venv)` at the beginning.

---

### **Step 4: Install Django**

With the virtual environment activated:

```bash
pip install django
```

Check version:

```bash
django-admin --version
```

---

### **Step 5: Create the Django project**

Inside `dfemsum/`:

```bash
django-admin startproject core .
```

Notice the dot `.` at the end – it tells Django to create the project in the current folder without nesting extra folders.

Your structure now:

```
dfemsum/
├── manage.py
└── core/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    └── asgi.py
```

---

### **Step 6: Test the project**

Run the server:

```bash
python manage.py runserver
```

Open your browser at `http://127.0.0.1:8000/` – you should see the **default Django welcome page**.

✅ This confirms Django is installed and the project is running.

---

## **Guide 2: Create modular app and test a simple view**

### **Step 1: Create the apps folder**

Inside your project root (`/home/user/Public/web/dfemsum`):

```bash
mkdir apps
touch apps/__init__.py
```

This will hold all your modular apps, like `summation`.

---

### **Step 2: Create the `summation` app**

Inside `apps/`:

```bash
cd apps
django-admin startapp summation
```

Make sure `apps/summation/` has these files:

```
__init__.py
admin.py
apps.py
models.py
tests.py
views.py
migrations/
```

---

### **Step 3: Register the app in `settings.py`**

Open `core/settings.py` and add `'apps.summation',` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.summation',  # <-- add this
]
```

---

### **Step 4: Fix `apps/summation/apps.py`**

Edit `apps/summation/apps.py` so the `name` matches the full Python path to your app:

```python
from django.apps import AppConfig

class SummationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.summation'  # <-- full path is required
```

This ensures Django can import your app correctly.

---

### **Step 5: Create a simple view**

Edit `apps/summation/views.py`:

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, this is the Summation app!")
```

---

### **Step 6: Create app-specific URLs**

Create `apps/summation/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='summation_index'),
]
```

---

### **Step 7: Hook app URLs to project**

Edit `core/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # <-- temporary root redirects to /summation/ for Guide 2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summation/', include('apps.summation.urls')),
    path('', lambda request: redirect('summation/')),  # <-- temporary root redirects to /summation/
]
```

The root URL `/` now redirects to `/summation/` for testing purposes.

---

### **Step 8: Test the app**

Run the server (make sure your virtual environment `venv` is activated):

```bash
python manage.py runserver
```

Open in your browser:

```
http://127.0.0.1:8000/summation/
```

You should see:

```
Hello, this is the Summation app!
```

✅ Success! Your modular `summation` app is running and ready for further development.

---

## **Guide 3: Static Files + Base Template Setup**

---

### **Step 1 — Create the `static` folder**

Inside your project root:

```
/dfemsum
    /core
    /apps
    /static   <-- create this
```

Create it:

```bash
mkdir static
```

---

### **Step 2 — Create CSS folder and stylesheet**

```bash
mkdir static/css
touch static/css/style.css
```

Put your **exact CSS** inside `static/css/style.css`:

```css
@import url('https://fonts.googleapis.com/css2?family=Neucha&display=swap');

body {
  font-family: "Neucha", Arial, Helvetica, sans-serif !important;
  line-height: 1.7;
  color: #222;
  background-color: #fff;
}

p {
  font-family: "Neucha", Arial, Helvetica, sans-serif;
  font-size: 1.15rem;
  line-height: 1.8;
  font-weight: 400;
  color: #333;                  
  margin-bottom: 1.2rem;
  text-align: justify;
}
```

---

### **Step 3 — Add static settings (core/settings.py)**

These must exist:

```python
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
```

---

### **Step 4 — Create global templates folder**

Create:

```bash
mkdir templates
```

Update `TEMPLATES` in `core/settings.py`:

```python
'DIRS': [BASE_DIR / "templates"],
```

---

### **Step 5 — Create `base.html`**

Create file:

```
templates/base.html
```

Paste your **exact** template:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  {% load static %}
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{% block title %}Django App{% endblock %}</title>
  
  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="{% static 'css/style.css' %}" rel="stylesheet">
</head>
<body class="bg-light d-flex justify-content-center" style="padding-top: 50px;">

  <div class="card shadow-lg p-4" style="width: 800px;">
    {% block content %}{% endblock %}
  </div>

  <!-- JavaScript -->
  <script>
    // JavaScript code here...
  </script>

  <!-- Bootstrap JS Bundle -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

---

### **Step 6 — Create summation template**

Create:

```

apps/summation/templates/summation/index.html

````

Paste your **exact** summation template:

```html
{% extends 'base.html' %}

{% block title %}Summation{% endblock %}

{% block content %}
<h4 class="mb-4 text-center">Summation</h4>

<div class="row g-2 mb-3">
  <div class="col"><input id="v1" type="number" class="form-control" placeholder="0.000"></div>
  <div class="col"><input id="v2" type="number" class="form-control" placeholder="0.000"></div>
  <div class="col"><input id="v3" type="number" class="form-control" placeholder="0.000"></div>
  <div class="col"><input id="v4" type="number" class="form-control" placeholder="0.000"></div>
  <div class="col"><input id="v5" type="number" class="form-control" placeholder="0.000"></div>
  <div class="col"><input id="result" type="text" class="form-control bg-light" placeholder="0.000" readonly></div>
</div>

<div class="d-flex justify-content-end gap-2">
  <button id="computeBtn" class="btn btn-primary" style="width:120px;">Compute</button>
  <button id="clearBtn" class="btn btn-secondary" style="width:120px;">Clear</button>
</div>
{% endblock %}
````

---

### **Step 7 — Render template from view**

In `apps/summation/views.py`:

```python
from django.shortcuts import render

def index(request):
    return render(request, 'summation/index.html')
```

---

### **Step 8 — Test**

Run server:

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/summation/
```

---

## **Guide 4: Setting Up Django Debug Toolbar**

---

### **Step 1 — Install Django Debug Toolbar**

First, you need to install the **Django Debug Toolbar** package. Run the following command in your terminal:

```bash
pip install django-debug-toolbar
```

---

### **Step 2 — Add `debug_toolbar` to `INSTALLED_APPS`**

In `core/settings.py`, add `'debug_toolbar'` to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.summation',
    'debug_toolbar',   # <-- Add the Debug Toolbar app
]
```

---

### **Step 3 — Add Debug Toolbar Middleware**

In `core/settings.py`, add the **Debug Toolbar middleware** to the `MIDDLEWARE` setting:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
```

---

### **Step 4 — Allow Local IPs for Debug Toolbar**

Add the following to `core/settings.py`:

```python
INTERNAL_IPS = [
    "127.0.0.1",  # Localhost
    "localhost",  # Also allow localhost by name
]
```

---

### **Step 5 — Configure Debug Toolbar (Optional)**

Optional configuration:

```python
# Guide 4 debug toolbar
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': lambda request: True,
}
```

---

### **Step 6 — Update `core/urls.py` to Include Debug Toolbar URLs**

In `core/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summation/', include('apps.summation.urls')),
    path('', lambda request: redirect('summation/')),

    if settings.DEBUG:
        import debug_toolbar
        urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns,
]
```

---

### **Step 7 — Run Your Server**

```bash
python manage.py runserver
```

---

### **Step 8 — Access the Debug Toolbar**

Navigate to:

```
http://127.0.0.1:8000/summation/
```

You should now see the **Django Debug Toolbar**.

---

## License

This project is for **learning purposes only**.

