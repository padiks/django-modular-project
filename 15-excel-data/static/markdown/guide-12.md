# Django - Guide 12 Part 1: Compute Module

Note:
This guide is part of your ongoing Django project. Unlike previous modules such as Stock, Items, and Movements, this chapter focuses on simple Django operations like formulas and static content. The goal is to learn Django concepts by applying them in small, practical examples before returning to the main project.

---

## Objectives

By the end of this guide, you will:

* Set up the Compute module with two routes: Summation and Summary
* Handle summation of two user input values
* Display a static summary page
* Set up URL routing for the Compute module
* Create a simple navigation menu

---

## Project Structure (Relevant Files)

```
project_folder/
├── core/
│   └── urls.py                 (Core URLs)
├── apps/
│   ├── compute/
│   │   ├── views.py            (Views for summation and summary)
│   │   ├── urls.py             (URLs for the compute module)
│   │   └── templates/compute/
│   │       ├── summation.html
│   │       └── summary.html
└── db.sqlite3
```

---

## 1. `core/urls.py` - Routing

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
    path('', include('apps.movements.urls')),
    path('compute/', include('apps.compute.urls')),
]
```

> The `compute` module is included in the core URLs and accessible via `/compute/`.

---

## 2. `apps/compute/urls.py`

```python
from django.urls import path
from . import views

app_name = 'compute' # Set the namespace for the compute app

urlpatterns = [
    path('summation/', views.summation, name='summation'),  # Summation route
    path('summary/', views.summary, name='summary'),        # Summary route
]
```

> Two routes are defined:
>
> * `/compute/summation/` for the summation page
> * `/compute/summary/` for the static summary page

---

## 3. `apps/compute/views.py`

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

> **Summation**: Handles POST requests to calculate the sum of two numbers provided by the user.
> **Summary**: A static page for providing additional details or context.

---

## 4. Templates

### summation.html

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

### summary.html

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

## 5. Navigation Menu

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

## Final Result

| Feature                       | Admin | User |
| ----------------------------- | ----- | ---- |
| View summation page           | Yes   | Yes  |
| View summary page             | Yes   | Yes  |
| Perform summation calculation | Yes   | Yes  |
| Static summary page           | Yes   | Yes  |

---

## Summary

This guide shows how to build a simple **Compute** module in Django with routes for summation and summary. The module allows users to input two numbers and calculate their sum, and also provides a static summary page.

The **Compute** module is integrated into the larger Django project, with a centralized navigation menu for users to access both features easily. This modular approach makes it easy to extend functionality in the future.

---

# Django - Guide 12 Part 2: Rendering Static Markdown

>**Note:**
>This section of the guide focuses on rendering **static markdown files** in a Django project. You will learn how to serve markdown files from the `static` directory and render them as HTML using a dedicated view.

The **Markdown Renderer** module allows users to view markdown content on your website by converting `.md` files into HTML and displaying them dynamically.

---

## Objectives

By the end of this guide, you will:

* Set up routes to render markdown files
* Convert markdown content to HTML using the `markdown` Python library
* Display static markdown content in a custom template
* Handle custom markdown files with dynamic URLs

---

## Project Structure (Relevant Files)

```
project_folder/
├── core/
│   ├── urls.py               (Core URLs for routing, including markdown paths)
│   └── views.py              (Views for rendering markdown)
├── static/
│   └── markdown/
│       └── guide-12.md       (Sample markdown file)
└── templates/
    └── markdown_renderer.html (Template to render markdown content)
```

---

## 1. core/urls.py - Routing for Markdown

In your `core/urls.py`, add routes to handle markdown rendering requests. These routes are responsible for serving the markdown files and rendering them using the appropriate view.

```python
from django.contrib import admin
from django.urls import path, include
from . import views  # Import views for markdown rendering

urlpatterns = [
    path('admin/', admin.site.urls),
    path('compute/', include('apps.compute.urls')),
    path('markdown/', views.render_markdown_view, name='render_markdown'),
    path('markdown/<str:filename>/', views.render_markdown_file, name='render_markdown_file'),
    path('', include('apps.movements.urls')),
    path('uom/', include('apps.uom.urls')),
]
```

---

## 2. core/views.py - Markdown Rendering Logic

You can define two views in your `views.py` file. One is for rendering static content, and the other dynamically handles markdown files.

### Static Markdown Content

```python
from django.shortcuts import render

def render_markdown_view(request):
    # Static content, you can replace this with dynamic content as needed
    content = "Your markdown content goes here"
    return render(request, 'markdown_renderer.html', {'content': content})
```

This simple view renders predefined static markdown content into HTML.

### Dynamic Markdown File Handling

```python
from django.http import HttpResponse, Http404
from pathlib import Path
from django.conf import settings
import markdown

def render_markdown_file(request, filename):
    # Construct the path to the markdown file in static/markdown folder
    markdown_file_path = Path(settings.BASE_DIR) / 'static' / 'markdown' / f'{filename}.md'
    
    # Check if the file exists
    if markdown_file_path.exists():
        # Read the content of the markdown file
        with open(markdown_file_path, 'r') as file:
            content = file.read()
        
        # Convert markdown content to HTML using the markdown library
        html_content = markdown.markdown(content, extensions=['fenced_code', 'codehilite', 'tables'])
        
        # Return the rendered HTML content to the template
        return render(request, 'markdown_renderer.html', {'content': html_content})
    else:
        raise Http404(f"File '{filename}.md' not found.")
```

---

## 3. Template: markdown_renderer.html

The `markdown_renderer.html` template is used to render the HTML content generated from the markdown file.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    
    <!-- Display the rendered markdown content -->
    <div>{{ content|safe }}</div>
</body>
</html>
```

This template is simple and outputs the converted markdown content inside a `div`. The `|safe` filter ensures that HTML from the markdown is rendered correctly.

---

## 4. Accessing Markdown Pages

After setting up the views and templates, you can navigate to:

* **Static markdown content**: `/markdown/`
* **Dynamic markdown files**: `/markdown/guide-12/`

---

## Final Result

| Feature                     | Admin | User |
| --------------------------- | ----- | ---- |
| View static markdown page   | Yes   | Yes  |
| View dynamic markdown files | Yes   | Yes  |

---

## Summary

This guide shows how to set up a simple **Markdown Renderer** in Django to display static markdown files as HTML. By using Django views and the `markdown` library, you can easily render `.md` files as part of your web application.
