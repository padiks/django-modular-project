# **DB Pilot – Django Modular Project**

**DB Pilot** is a lightweight, modular **Django** application demonstrating complete **CRUD** operations using **SQLite**.
It is designed as a **step-by-step learning project**, showing how to build scalable Django apps with a clean, modular architecture.

The repository includes a **sample SQLite database (`db.sqlite3`)** with preloaded tables and test data.

Available login credentials:

* **User account:** `user` / `demo`
* **Admin account:** `admin` / `root`

---

If you want, I can also make a slightly more polished version suitable for a README with better formatting. Do you want me to do that?


---

If you want, I can also make a slightly more polished version suitable for a README with better formatting. Do you want me to do that?

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
│   │   ├── templates/uom/form.html
│   │   └── templates/uom/index.html
│   │
│   ├── items/                             # Items (CRUD + FK examples)
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── forms.py
│   │   ├── templates/items/form.html
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

Each guide is a **fully working project** and **continues from the previous guide**.
This means **every guide folder already includes all features, files, and improvements from the earlier guides**, so you can download **any guide** and run it instantly.

---

## 🚀 **How to Run**

Minimal requirements (already tested on **Windows** and **Debian**):

```
asgiref==3.10.0
Django==5.2.8
django-debug-toolbar==6.1.0
sqlparse==0.5.3
```

---

### Start the Server

Install dependencies and run the project:

```bash
pip install -r requirements.txt
python manage.py runserver
```

✔ **No migrations required** — the included `db.sqlite3` already contains:

* UOM, Categories, Doctype, Items, Users sample data
* Items with foreign keys
* Test user account

---

### Running the Project from GitHub

You can also download the project directly from GitHub and run it easily:

```bash
# Clone the repository
git clone https://github.com/padiks/django-modular-project.git

# Go into the project folder
cd django-modular-project
cd 06-auth-login-logout

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate       # Linux / macOS
# For Windows PowerShell use: venv\Scripts\Activate.ps1
# For Windows CMD use: venv\Scripts\activate.bat

# Upgrade pip and install required packages
pip install --upgrade pip
pip install Django django-debug-toolbar

# Run the development server
python manage.py runserver
```

You should see output similar to:

```
System check identified no issues (0 silenced).
Django version 5.2.8, using settings 'core.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

---

### Test Login

* **username:** `user`
* **password:** `demo`

* **username:** `admin`
* **password:** `root`

---

## 🏗️ **Features**

* Modular Django Architecture (copy → rename → new app)
* Bootstrap UI with reusable includes
* Full CRUD using Django ORM
* Clean foreign key examples (Items → UOM)
* Login/Logout using Django Auth
* Preloaded sample data
* Debug toolbar **already integrated** (can be easily removed if needed)
* Easy to extend and scale with new modules

---

## 📄 License

This project is for **learning and educational use**.
Feel free to explore, extend, and build upon it.
