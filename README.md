# **DB Pilot – Django Modular Project**

**DB Pilot** is a lightweight, modular **Django** application demonstrating complete **CRUD** operations using **SQLite**.
It is designed as a **step-by-step learning project**, showing how to build scalable Django apps with a clean, modular architecture.

The repository includes a **sample SQLite database (`db.sqlite3`)** with preloaded tables and test data.

Available login credentials:

* **User account:** `user` / `demo`
* **Admin account:** `admin` / `root`

---

You can **check the running project online** at: [https://padiks.pythonanywhere.com](https://padiks.pythonanywhere.com) ✅

This live demo lets you **explore all modules**, test CRUD operations, and see role-based access in action without needing to set up anything locally.

---

## 🧩 **Project Structure (Modular Django)**

```
project_folder/
├── manage.py
│
├── core/                                  # Core Django settings & URL configuration
│   ├── settings.py
│   └── urls.py
│
├── apps/                                  # Modular Django apps
│   ├── items/                             # Items app (CRUD + ForeignKey examples)
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── forms.py
│   │   └── templates/items/
│   │        ├── index.html
│   │        └── form.html
│   │
│   ├── <other-modules>/                   # Placeholder for additional apps/modules
│   │
│   └── users/                             # Authentication & role-based access
│       ├── apps.py
│       ├── urls.py
│       ├── views.py
│       ├── templatetags/group_filters.py  # Custom template filters for user groups
│       └── templates/users/login.html
│
├── templates/                             # Project-wide templates
│   ├── base.html                          # Main layout for all pages
│   ├── admin/base_site.html               # Custom Django admin layout
│   └── includes/                          # Reusable partial templates
│       ├── _table_select.html
│       └── footer.html
│
├── static/                                # Static files (CSS, images)
│   ├── css/style.css
│   └── img/favicon.png
│
└── db.sqlite3                             # SQLite database
```

> Some modules (*items*, *users*) are shown.
> Additional modules exist in earlier guide folders.

---

## 📘 **Included Learning Guides**

The project includes **16 modular guides**, each a self-contained working project:

| Guide                                          | Description                                                                                                  |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **01 — Base Template**                         | Bootstrap layout, global includes.                                                                           |
| **02 — SQLite Database**                       | Database config + first tables.                                                                              |
| **03 — Full CRUD (ORM)**                       | Create, Read, Update, Delete.                                                                                |
| **04 — Multi-Table Includes**                  | Rendering multiple tables modularly.                                                                         |
| **05 — Foreign Keys**                          | Items linked to UOM (relationships).                                                                         |
| **06 — Authentication**                        | Login & logout using Django Auth.                                                                            |
| **07 — User Management Admin Customization**   | Manage users and superusers, use Groups for roles, customize admin panel, control table visibility per role. |
| **08 — Role-Based Admin**                      | Admin panel with advanced role-based access.                                                                 |
| **09 — Role-Based CRUD Module**                | CRUD operations restricted by user roles.                                                                    |
| **10 — DataTables Integration**                | Dynamic tables with search, sort, and pagination.                                                            |
| **11 — Stock Movements Module**                | Manages and tracks stock transactions, including the movement of items and supporting stock-related entries. |
| **12 — Compute Module & Markdown Renderer**    | Handles basic calculations (e.g., summation) and renders static markdown content into HTML.                  |
| **13 — Django Rest Framework (DRF)**           | Setting up a based API to manage data such as books.                                                         |
| **14 — Rest API Consumer**                     | Fetch and display data from an external REST API in Django.                                                  |
| **15 — Display Excel Data**                    | Read and display Excel data in a table format.                                                               |
| **16 — PDF Viewer**                            | Load a PDF from the media folder, and render it page-by-page using PDF.js                                    |

Each guide is a **fully working project** and **continues from the previous guide**.
This means **every guide folder already includes all features, files, and improvements from the earlier guides**, so you can download **any guide** and run it instantly.

---

## 🚀 **How to Run**

Minimal requirements (already tested on **Windows** and **Debian**):

```
asgiref==3.10.0
certifi==2025.11.12
charset-normalizer==3.4.4
Django==5.2.8
django-cors-headers==4.9.0
django-debug-toolbar==6.1.0
djangorestframework==3.16.1
djangorestframework_simplejwt==5.5.1
et_xmlfile==2.0.0
idna==3.11
Markdown==3.10
numpy==2.3.5
openpyxl==3.1.5
pandas==2.3.3
PyJWT==2.10.1
python-dateutil==2.9.0.post0
pytz==2025.2
PyYAML==6.0.3
requests==2.32.5
six==1.17.0
sqlparse==0.5.3
tzdata==2025.2
urllib3==2.5.0
```

---

### Start the Server

Install dependencies and run the project:

```bash
pip install -r requirements.txt
python manage.py runserver
```

✔ **No migrations required** — the included `db.sqlite3` already contains the necessary data and schema.

✔ **Migrations might be required in the future** — If you modify models or the schema, run the following commands to apply changes:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### Running the Project from GitHub

You can also download the project directly from GitHub and run it easily:

```bash
# Clone the repository
git clone https://github.com/padiks/django-modular-project.git

# Go into the project folder
cd django-modular-project
cd 14-rest-api-consumer

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate       # Linux / macOS
# For Windows PowerShell use: venv\Scripts\Activate.ps1
# For Windows CMD use: venv\Scripts\activate.bat

# Upgrade pip and install required packages
pip install --upgrade pip
pip install Django django-debug-toolbar markdown openpyxl djangorestframework djangorestframework-simplejwt

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




