# 🎨 ArtPractice - Art Tutorial Platform

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Django](https://img.shields.io/badge/Django-5.2-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

A Django-based web application for sharing and discovering art tutorials.  
Users can browse tutorials by category, create new tutorials, and manage art techniques.

---

## 🚀 Features

- ✅ **Full CRUD Functionality** – Create, read, update, and delete tutorials  
- 📂 **Category Organization** – Custom category ordering  
- 🏷️ **Technique Tagging** – Attach techniques to tutorials  
- 🔎 **Search & Filtering** – Search by title or content  
- 🎯 **Difficulty Levels** – Beginner, Intermediate, Advanced  
- 👁️ **Publish Control** – Draft & published states  
- 📱 **Responsive Design** – Clean custom CSS layout  

---

## 🛠️ Tech Stack

- **Backend:** Django 5.2  
- **Database:** PostgreSQL  
- **Frontend:** HTML5 / CSS3  
- **Language:** Python 3.8+  

---

## 📦 Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/JonDoe841/ArtPractice
cd ArtPractice
```

---

### 2️⃣ Create Virtual Environment

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install django psycopg2-binary
```

---

### 4️⃣ Setup PostgreSQL Database

```sql
CREATE DATABASE art_practice;

CREATE USER postgres_user WITH PASSWORD 'password';

ALTER ROLE postgres_user SET client_encoding TO 'utf8';
ALTER ROLE postgres_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE postgres_user SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE art_practice TO postgres_user;
```

---

### 5️⃣ Configure Database in `settings.py`

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "art_practice",
        "USER": "postgres_user",
        "PASSWORD": "password",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
```

---

### 6️⃣ Apply Migrations

```bash
python manage.py migrate
```

---

### 7️⃣ (Optional) Create Initial Categories

```bash
python manage.py shell
```

```python
from categories.models import Category

Category.objects.create(name="Drawing", description="Pencil and charcoal techniques", order=1)
Category.objects.create(name="Painting", description="Watercolor, acrylic and oil", order=2)
Category.objects.create(name="Digital Art", description="Procreate, Photoshop tools", order=3)

exit()
```

---

### 8️⃣ Run Development Server

```bash
python manage.py runserver
```

Open your browser at:

```
http://127.0.0.1:8000
```

---

## 📁 Project Structure

```
ArtPractice/
├── manage.py
├── README.md
├── ArtPractice/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── categories/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── core/
│   ├── views.py
│   ├── context_processors.py
│   └── urls.py
├── tutorials/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templatetags/
│       └── custom_filters.py
└── templates/
    ├── base.html
    ├── 404.html
    ├── core/
    │   └── home_page.html
    ├── categories/
    │   ├── add_category.html
    │   ├── category_list.html
    │   ├── category_detail.html
    │   ├── edit_category.html
    │   └── delete_category.html
    └── tutorials/
        ├── tutorial_list.html
        ├── tutorial_details.html
        ├── tutorial_create.html
        ├── tutorial_edit.html
        └── tutorial_delete.html
```

---

## 🎯 Usage

### Browsing Tutorials
- View all published tutorials
- Filter by category
- Search by keyword

### Creating Tutorials
- Fill tutorial details
- Choose category & techniques
- Tutorials are unpublished by default

### Managing Categories
- Add, edit, delete categories
- Control display order

---

## 🎨 Custom Template Filter

`minutes_to_hours`  
Converts minutes to readable format:

```
90 → 1h 30min
```

---

## ⚙️ Configuration Notes

- Authentication is not implemented (project requirement)
- Tutorials default to unpublished
- Categories appear globally in footer

---

## 📚 Educational Purpose

This project was created for the **Django Basics Regular Exam – SoftUni**.

---

## 📄 License

Educational use only.