## 🧱 Step-by-Step Guide to Create Your Modular Django Project - Sum Calculator App

### **1. Create the Root Project Folder (`my_project`)**

First, create your **root project folder**:

```bash
mkdir my_project
cd my_project
```

This folder will hold the entire Django project, including the `core/` and `apps/` folders.

---

### **2. Create the Django Project (`core`)**

Now, inside `my_project/`, create the **Django project** (`core`):

```bash
django-admin startproject core
cd core
```

This will create the following structure:

```
my_project/                    # Root folder
├── manage.py                  # Django management entrypoint
└── core/                       # Project core folder
    ├── __init__.py
    ├── settings.py             # Centralized settings (DB, paths, debug, apps)
    ├── urls.py                 # Root URL router, includes app-level URLs
    ├── wsgi.py                 # WSGI entrypoint for Apache/mod_wsgi
    └── asgi.py                 # Optional for async support (future-proof)
```

---

### **3. Create the `apps/` Folder**

Now, create the **`apps/`** folder, which will hold all your modular apps:

```bash
mkdir ../apps
```

Your folder structure should now look like this:

```
my_project/  
├── manage.py  
├── core/  
│   ├── __init__.py  
│   ├── settings.py  
│   ├── urls.py  
│   ├── wsgi.py  
│   └── asgi.py  
└── apps/                       # Modular apps go here
```

---

### **4. Create the `sum` App**

Inside the `apps/` folder, create a new app called **`sum`**:

```bash
python manage.py startapp sum ../apps/sum
```

Now you’ll have this structure for the `sum` app:

```
apps/  
└── sum/  
    ├── __init__.py  
    ├── admin.py  
    ├── apps.py  
    ├── models.py  
    ├── tests.py  
    ├── views.py  
    ├── urls.py           # We will create this next
    └── templates/  
        └── sum/  
            └── index.html  # We will create this later
```

---

### **5. Add the `sum` App to `INSTALLED_APPS`**

Now go back to `core/settings.py` and add `'sum'` to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sum',  # Add the new 'sum' app here
]
```

---

### **6. Set Up the `sum/urls.py` File**

Create the `urls.py` file inside the `apps/sum` directory to define the URL patterns for the `sum` app.

```python
# apps/sum/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='sum_index'),
]
```

Then, in `core/urls.py`, include the `sum` app's URLs:

```python
# core/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sum/', include('sum.urls')),  # Include sum app URLs
]
```

---

### **7. Run the Server**

Now you can run your Django server:

```bash
python manage.py runserver
```

Navigate to [http://127.0.0.1:8000/sum/](http://127.0.0.1:8000/sum/) to test everything.

---

Now, you have a clean, modular setup with **`my_project/`** as the root folder, **`core/`** for your main project configuration, and **`apps/`** for modular apps like `sum`.

---

## **Step 8: Create the New App (`sum`)**

Inside your project root (where `manage.py` is), create a new app called `sum` under the `apps/` directory:

```bash
python manage.py startapp sum apps/sum
```

Now you’ll have this folder structure inside `apps/`:

```
apps/
 └── sum/
      ├── __init__.py
      ├── admin.py
      ├── apps.py
      ├── models.py
      ├── tests.py
      ├── views.py
      ├── urls.py        # We’ll create this next
      └── templates/
          └── sum/
              └── index.html  # We’ll create this later
```

---

## **Step 9: Add the App to `INSTALLED_APPS`**

Open `core/settings.py` and add `'sum'` to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sum',  # Add 'sum' app here
]
```

---

## **Step 10: Create the View for the App**

Edit the `apps/sum/views.py` file to handle the logic for adding two numbers. The `index` view will render a form and calculate the sum of the two numbers:

```python
from django.shortcuts import render

def index(request):
    result = None

    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1', 0))
            num2 = float(request.POST.get('num2', 0))
            result = num1 + num2
        except ValueError:
            result = "Invalid input"

    return render(request, 'sum/index.html', {'result': result})
```

---

## **Step 11: Create the `urls.py` File for the App**

Inside the `apps/sum` directory, create a `urls.py` file that defines the URL pattern for the `sum` app:

```python
# apps/sum/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='sum_index'),
]
```

Then, in the `core/urls.py` file, include the `sum` app's URLs:

```python
# core/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sum/', include('sum.urls')),  # Include sum app's URLs
]
```

---

## **Step 12: Create the Template for the App**

Inside `apps/sum/templates/sum/`, create the `index.html` template for the "Sum Calculator" page.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sum Calculator</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container py-5">
        <div class="row justify-content-center">
            <div class="col-md-6">
                <div class="card shadow-sm">
                    <div class="card-body">
                        <h3 class="card-title text-center mb-4">Add Two Numbers</h3>

                        <form method="POST" class="mb-3">
                            {% csrf_token %}
                            <div class="mb-3">
                                <label for="num1" class="form-label">Number 1</label>
                                <input type="number" step="any" name="num1" id="num1" class="form-control" required>
                            </div>

                            <div class="mb-3">
                                <label for="num2" class="form-label">Number 2</label>
                                <input type="number" step="any" name="num2" id="num2" class="form-control" required>
                            </div>

                            <button type="submit" class="btn btn-primary w-100">Calculate</button>
                        </form>

                        {% if result is not None %}
                            <div class="alert alert-info text-center">
                                <strong>Result: </strong>{{ result }}
                            </div>
                        {% endif %}
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```

This HTML page uses **Bootstrap** to create a clean and responsive form


for inputting two numbers and displaying the result.

---

## **Step 13: Run the Project**

Finally, run your Django development server:

```bash
python manage.py runserver
```

Now you can test the app by visiting [http://127.0.0.1:8000/sum/](http://127.0.0.1:8000/sum/) in your browser. You should see a page where you can input two numbers, click "Calculate", and view their sum.

---

### ✅ **Result:**

* The **Sum Calculator** form should allow users to enter two numbers, click **Calculate**, and display the sum on the same page.

---

#### Tags

Django, Python, Modular App, Bootstrap
