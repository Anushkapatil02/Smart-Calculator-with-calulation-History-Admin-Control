# Smart-Calculator-with-calulation-History-Admin-Control
A responsive and interactive web-based calculator built using Django with real-time calculation history, filtering options, and secure admin-controlled history management.

# Smart Calculator with History & Admin Controls

A responsive and interactive web-based calculator built using **Django** with real-time calculation history, filtering options, and secure admin-controlled history management.

---

## 🚀 Features

- Perform basic arithmetic operations: **Addition (+), Subtraction (-), Multiplication (×), Division (/)**
- Auto-save every calculation to the database with timestamp.
- Display calculation history in an interactive table.
- Filter history based on:
  - Today
  - Last 10 Days
  - Weekly
  - Monthly
- **Admin-only secure history deletion:**
  - Two-step confirmation with password protection.
- Fully responsive and modern UI using **HTML, CSS, Font Awesome**.

---

## 🛠 Technology Stack

- **Backend:** Django 5.x (Python)
- **Frontend:** HTML5, CSS3, Font Awesome
- **Database:** SQLite (default Django database)

---

## 📂 Project Structure

calculator_project/
├── calculator/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   └── calculator/
│   │       └── index.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── calculator_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

---

## ⚙️ Installation Guide

1. **Clone the repository:**

https://github.com/your-username/smart-calculator-django.git

2. **Create and activate virtual environment:**

python -m venv venv
venv\Scripts\activate  # On Windows

3. **Install dependencies:**

pip install django

4. **Run migrations:**

python manage.py migrate

5. **Start the server:**

python manage.py runserver

6. **Access the app:**

http://127.0.0.1:8000/

---

## 🔑 Admin Password

- Default admin password for clearing history: `admin123`
- You can change this in `views.py`:

ADMIN_PASSWORD = 'your_secure_password_here'

---


## 💡 Future Enhancements

- User authentication for multi-user support.
- Graphical representation of calculation trends.
- Export history to PDF or Excel.

---

## 📧 Contact

For queries or collaborations:

Name: Anushka Patil
LinkedIn Profile: https://linkedin.com/in/anushka-patil-79345022b


---


