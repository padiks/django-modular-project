# Stock - Django Modular Project

**Despatch** is a lightweight, modular **Django** application that demonstrates complete **CRUD (Create, Read, Update, Delete)** operations using an **SQLite** database. It’s designed as a learning project for building modular Django apps with blueprints, SQLAlchemy, and Bootstrap 5.

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
│   ├── categories/                        # Module 1: Units of Measure
│   │   ├── __init__.py
│   │   ├── admin.py                       # Optional Admin registration
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

| Flask Concept         | Django Equivalent                     | Notes                                                                 |
| --------------------- | ------------------------------------- | --------------------------------------------------------------------- |
| `app.py`              | `manage.py` + `core/settings.py`      | Django uses `manage.py` and project settings for initialization.      |
| `config.py`           | `settings.py`                         | All environment, DB, and path configs go here.                        |
| Blueprints in `apps/` | Django “apps” in `apps/`              | Same modularity pattern — each app has its own models, views, URLs.   |
| `routes.py`           | `urls.py` + `views.py`                | Django separates routing and view logic.                              |
| Shared utilities      | `apps/utils/`                         | Works exactly like Flask’s shared modules.                            |
| Templates per module  | `apps/<module>/templates/<module>/`   | Django finds them automatically if configured in `TEMPLATES['DIRS']`. |
| Global templates      | `templates/`                          | Works the same — your `base.html`, `404.html`, etc.                   |
| Static files          | `static/`                             | Standard Django static collection folder.                             |
| Database              | `db.sqlite3     `                     | You can point `DATABASES['default']['NAME']` to this path.            |

---

### License

This project is intended for learning purposes.
