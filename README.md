# DB Pilot - Django Modular Project

**DB Pilot** is a lightweight, modular **Django** application that demonstrates complete **CRUD (Create, Read, Update, Delete)** operations using an **SQLite** database. It’s designed as a learning project for building modular Django apps with blueprints, SQLAlchemy, and Bootstrap 5.

---

### 🌱 Django Modular Project Structure

```
dstock/
├── manage.py                              # Django management entrypoint
│
├── core/                                  # Project core (settings, URLs, WSGI)
│   ├── __init__.py
│   ├── settings.py                        # Optional for centralized settings (DB, paths, debug, apps)
│   ├── urls.py                            # Root URL router, includes app-level URLs
│   ├── wsgi.py                            # Optional for WSGI entrypoint for Apache/mod_wsgi
│   └── asgi.py                            # Optional for async support (future-proof)
│
├── apps/                                  # Your modular app collection
│   ├── __init__.py
│   │
│   ├── uom/                               # Module 1: Units of Measure
│   │   ├── __init__.py
│   │   ├── admin.py                       # Optional Admin registration
│   │   ├── apps.py                        # Django app config
│   │   ├── models.py                      # Models (tables)
│   │   ├── urls.py                        # App-specific routes
│   │   ├── views.py                       # Views (controllers)
│   │   ├── forms.py                       # Optional (forms for CRUD)
│   │   ├── tests.py                       # Optional tests
│   │   └── templates/
│   │       └── uom/
│   │           └── index.html             # App-level template
│   │
│   ├── categories/                               # Module 2: Categories
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── templates/
│   │       └── categories/
│   │           └── index.html
│   │
│   └── utils/                             # Optional for shared helpers (non-model logic)
│       ├── __init__.py
│       └── helpers.py                     # Optional for Markdown rendering, formatting, etc.
│
├── templates/                             # Global templates shared across all apps
│   ├── base.html                          # Base layout (extends in all app templates)
│   ├── 404.html                           # Optional: custom error page
│   └── includes/                          # Optional for reusable template parts (header/footer)
│       ├── header.html
│       └── footer.html
│
├── static/                                # Shared static files (CSS/JS/Images)
│   ├── css/
│   │   └── style.css
│   └── img/
│       └── favicon.png
│
└── db.sqlite3                             # SQLite database
```

---

### ⚙️ Highlights

| **Django Concept**                  | **Explanation**                                                                                  | **Notes**                                                                              |
| ----------------------------------- | ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| `manage.py`                         | Central command-line utility for running and managing the project.                               | Handles database migrations, running the server, and more.                             |
| `settings.py`                       | Contains all configurations for the project (database, static files, etc.).                      | Configuration for database, apps, middleware, etc.                                     |
| Django Apps                         | Independent modules within the `apps/` directory that handle a specific part of the application. | Similar to Flask's blueprint system, but uses a more integrated approach.              |
| `urls.py`                           | Defines URL patterns for routing requests to views.                                              | Routes are mapped to views here, similar to Flask's `routes.py`.                       |
| `views.py`                          | Contains view functions that handle requests and return responses.                               | Similar to Flask's route handlers.                                                     |
| `apps/utils/`                       | Shared modules or utility functions used across multiple apps.                                   | Like Flask's shared utility modules, but Django doesn't require importing `Blueprint`. |
| `apps/<module>/templates/<module>/` | Templates are placed per app in the `templates` directory.                                       | Django automatically looks in `templates/` for rendering.                              |
| `templates/`                        | Global templates (like `base.html`, `404.html`) are placed here.                                 | Common templates used across the entire project.                                       |
| `static/`                           | Folder where static files like CSS, JS, and images are stored.                                   | Standard static file directory for serving assets.                                     |
| `db.sqlite3`                        | Default database for the project, usually SQLite.                                                | You configure this in `DATABASES['default']` in `settings.py`.                         |

---

### License

This project is intended for learning purposes.
