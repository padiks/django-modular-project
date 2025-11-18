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

| **Django Concept**                  | **Notes**                                                                                                                                                                 |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `manage.py`                         | Django uses `manage.py` for project initialization and running commands.                                                                                                  |
| `settings.py`                       | Contains all configurations for the environment, database, paths, etc.                                                                                                    |
| `apps/`                             | Modular structure where each app (e.g., `uom`, `products`) has its own models, views, and routes.                                                                         |
| `urls.py`                           | Defines routes (URLs) and maps them to specific views.                                                                                                                    |
| `views.py`                          | Contains the view functions that handle requests and return responses.                                                                                                    |
| `apps/utils/`                       | Shared utility functions, just like reusable modules.                                                                                                                     |
| `apps/<module>/templates/<module>/` | Templates specific to each app are stored in the `templates` folder inside the app directory.                                                                             |
| `templates/`                        | Global templates like `base.html`, `404.html`, etc., that are shared across the project.                                                                                  |
| `static/`                           | Contains static files (CSS, JavaScript, images) accessible by the browser.                                                                                                |
| `db.sqlite3`                        | The project includes a sample SQLite database file (`db.sqlite3`) with pre-populated tables and data. Point to this file in `DATABASES['default']['NAME']` configuration. |

---

### License

This project is intended for learning purposes.
