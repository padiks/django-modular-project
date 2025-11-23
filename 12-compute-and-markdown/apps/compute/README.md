# 📘 Django – Guide 12: Compute Module

> **📌 Note:**
> This guide is standalone and covers the setup and implementation of the **Compute** module, which includes two primary features: summation calculation and a static summary page.

The repository includes a **sample SQLite database (`db.sqlite3`)** for testing.

Available login credentials:

* **User account:** `user` / `demo`
* **Admin account:** `admin` / `root`

---

## 🎯 Objectives

By the end of this guide, you will:

* ✅ Set up the **Compute** module with two routes: **Summation** and **Summary**
* ✅ Handle summation of two user-provided numbers with a simple form
* ✅ Display a **static summary** page
* ✅ Organize **URL routing** for the Compute module
* ✅ Create a **centralized menu** for navigation between pages

---

## 📁 Project Structure (Relevant Files)

```
project_folder/
├── core/
│   └── urls.py               ← Core URLs for routing
├── apps/
│   ├── compute/
│   │   ├── views.py          ← Views for summation and summary
│   │   ├── urls.py           ← URLs for the compute module
│   │   └── templates/compute/
│   │       ├── summation.html ← Summation page template
│   │       └── summary.html   ← Static summary page template
└── db.sqlite3                ← Sample database (optional for testing)
```

---

## 1️⃣ `core/urls.py` — Routing

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('uom/', include('apps.uom.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('categories/', include('apps.categories.urls')),
    path('doctype/', include('apps.doctype.urls')),
    path('items/', include('apps.items.urls')),
    path('', include('apps.movements.urls')),  # Home page
    path('compute/', include('apps.compute.urls')),  # Includes the compute URLs
]
```

> ✅ The `compute` module is included in the core URLs and accessible via `/compute/`.

---

## 2️⃣ `apps/compute/urls.py` — Compute Routes

```python
from django.urls import path
from . import views

app_name = 'compute'  # Set the namespace for the compute app

urlpatterns = [
    path('summation/', views.summation, name='summation'),  # Summation route
    path('summary/', views.summary, name='summary'),        # Summary route
]
```

> ✅ Two routes are defined:
>
> * `/compute/summation/` for the summation page
> * `/compute/summary/` for the static summary page

---

## 3️⃣ `apps/compute/views.py` — Views

```python
from django.shortcuts import render

# Summation View
def summation(request):
    input1 = ''  # Default to an empty string
    input2 = ''  # Default to an empty string
    sum_values = None

    if request.method == 'POST':
        input1 = request.POST.get('input1', '')
        input2 = request.POST.get('input2', '')

        try:
            input1 = float(input1)
            input2 = float(input2)
            sum_values = input1 + input2
        except ValueError:
            sum_values = 'Invalid input. Please enter numeric values.'

    return render(request, 'compute/summation.html', {
        'title': 'Summation',
        'input1': input1,
        'input2': input2,
        'sum_values': sum_values,
    })

# Summary View (Static page)
def summary(request):
    return render(request, 'compute/summary.html', {
        'title': 'Summary',
    })
```

> ✅ **Summation**: Handles POST requests to calculate the sum of two numbers provided by the user.
> ✅ **Summary**: A static page for providing additional details or context.

---

## 4️⃣ Templates

### `summation.html`

This template allows the user to input two numbers and calculate their sum.

```html
{% extends 'base.html' %}

{% block title %}{{ title }}{% endblock %}

{% block content %}
<div class="card shadow-lg p-4 mb-3">
    <h4 class="mb-4 text-center">{{ title }}</h4>

    <form method="POST">
        {% csrf_token %}
        <div class="mb-3">
            <label for="input1" class="form-label">Input 1</label>
            <input type="text" class="form-control" id="input1" name="input1" value="{{ input1 }}">
        </div>
        
        <div class="mb-3">
            <label for="input2" class="form-label">Input 2</label>
            <input type="text" class="form-control" id="input2" name="input2" value="{{ input2 }}">
        </div>

        <button type="submit" class="btn btn-primary">Compute</button>
    </form>

    {% if sum_values is not None %}
    <div class="mt-3">
        <h5>Result:</h5>
        <p><strong>Sum:</strong> {{ sum_values }}</p>
    </div>
    {% endif %}
</div>
{% endblock %}
```

### `summary.html`

This template displays a static summary page.

```html
{% extends 'base.html' %}

{% block title %}{{ title }}{% endblock %}

{% block content %}
<div class="card shadow-lg p-4 mb-3">
    <h4 class="mb-4 text-center">{{ title }}</h4>
    <p>This is a static summary page.</p>
</div>
{% endblock %}
```

---

## 5️⃣ Navigation Menu

To enable users to switch between the **Summation** and **Summary** pages, we include a simple navigation menu:

```html
<div class="mb-3">
    <ul class="nav justify-content-center">
        <li class="nav-item">
            <a class="nav-link border" href="{% url 'compute:summation' %}">Summation</a>
        </li>
        <li class="nav-item">
            <a class="nav-link border" href="{% url 'compute:summary' %}">Summary</a>
        </li>
    </ul>
</div>
```

> ✅ This menu is placed in the `base.html` template or any other layout template you are using.

---

## 🎉 Final Result

| Feature                       | Admin | User  |
| ----------------------------- | ----- | ----- |
| View summation page           | ✅ Yes | ✅ Yes |
| View summary page             | ✅ Yes | ✅ Yes |
| Perform summation calculation | ✅ Yes | ✅ Yes |
| Static summary page           | ✅ Yes | ✅ Yes |

> Admin and users can both access the **Summation** and **Summary** pages, but only users with the correct permissions (in future versions) will be able to add or modify data. In this version, both can view and use the summation form.

---

## 🎯 Summary

This guide shows how to build a simple **Compute** module in Django with routes for summation and summary. The module allows users to input two numbers and calculate their sum, and also provides a static summary page.

The **Compute** module is integrated into the larger Django project, with a centralized navigation menu for users to access both features easily. This modular approach makes it easy to extend functionality in the future.
