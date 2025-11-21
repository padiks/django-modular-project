# **DB Pilot – Django Modular Project**

**DB Pilot** is a lightweight, modular **Django** application demonstrating complete **CRUD** operations using **SQLite**.
It is designed as a **step-by-step learning project** showing how to build scalable Django apps with a clean, modular architecture.

The repository includes a **sample SQLite database (`db.sqlite3`)** with tables and test data ready to use.
Use **username:** `user` & **password:** `q` to log in.

---

## 🧩 **Project Structure (Modular Django)**

```
project_folder/
├── manage.py
│
├── core/                                  # Core project config
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── apps/
│   ├── uom/                               # Units of Measure (CRUD)
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── forms.py
│   │   └── templates/uom/index.html
│   │
│   ├── items/                             # Items (CRUD + FK examples)
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── forms.py
│   │   └── templates/items/index.html
│   │
│   └── users/                             # Authentication (login/logout)
│       ├── apps.py
│       ├── urls.py
│       ├── views.py
│       └── templates/users/login.html
│
├── templates/
│   ├── base.html
│   └── includes/
│       └── _table_select.html
│
├── static/
│   ├── css/style.css
│   └── img/favicon.png
│
└── db.sqlite3
```

> Only the main modules (*uom*, *items*, *users*) are shown.
> Additional modules exist in earlier guide folders.

---

## 📘 **Included Learning Guides**

The project includes **6 modular guides**, each a self-contained working project:

| Guide                         | Description                          |
| ----------------------------- | ------------------------------------ |
| **01 — Base Template**        | Bootstrap layout, global includes.   |
| **02 — SQLite Database**      | Database config + first tables.      |
| **03 — Full CRUD (ORM)**      | Create, Read, Update, Delete.        |
| **04 — Multi-Table Includes** | Rendering multiple tables modularly. |
| **05 — Foreign Keys**         | Items linked to UOM (relationships). |
| **06 — Authentication**       | Login & logout using Django Auth.    |

Each guide is a **fully working project**, and **each one continues from the previous guide**.
This means **every guide folder already contains all features, files, and improvements from the earlier guides** — so you can download **any guide** and run it instantly.

---

## 🚀 **How to Run**

Minimal requirements (already tested on **Windows** and **Debian**):

```
asgiref==3.10.0
Django==5.2.8
django-debug-toolbar==6.1.0
sqlparse==0.5.3
```

### Start the server

```
pip install -r requirements.txt
python manage.py runserver
```

✔ No migrations required — the included `db.sqlite3` already contains:

* UOM, Categories, Doctype, Items, Users sample data
* Items with foreign keys
* Test user account

### Test Login

* **username:** `user`
* **password:** `q`

---

## 🏗️ **Features**

* Modular Django Architecture (copy → rename → new app)
* Bootstrap UI with reusable includes
* Full CRUD using Django ORM
* Clean foreign key examples (Items → UOM)
* Login/Logout using Django Auth
* Preloaded sample data
* Easy to extend and scale with new modules

---

## 📄 License

This project is for **learning and educational use**.
Feel free to explore, extend, and build upon it.
