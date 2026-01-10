# flask-secure-todo-manager

A robust, full-stack Flask application for task management featuring User Authentication (Login/Signup), CRUD operations, and a responsive UI.


# Flask TaskMaster: Secure Todo Application

A full-stack Python web application built with Flask that allows users to manage their daily tasks within a secure, authenticated environment.


## 🌟 Key Features

* **User Accounts:** Secure user registration and login functionality.
* **Password Hashing:** Uses industry-standard encryption for user security.
* **Personalized Dashboard:** Each user can only view and manage their own tasks.
* **Full CRUD Operations:**
    - Create: Add new tasks with descriptions.
    - Read: View a clean list of pending tasks.
    - Update: Mark tasks as complete or edit details.
    - Delete: Remove tasks once finished.
* **Responsive UI:** Built with Bootstrap to ensure the app looks great on mobile and desktop.

## 🛠️ Tech Stack

* **Backend:** Python 3.x, Flask
* **Database:** SQLite (SQLAlchemy ORM)
* **Auth:** Flask-Login, Werkzeug Security
* **Frontend:** Jinja2 Templates, Bootstrap 5, Custom CSS

## ⚙️ Installation & Setup

1. **Clone the Project:**
   git clone https://github.com/jatingulati1264/flask-secure-todo-manager/
   cd flask-todo-app

2. **Setup Virtual Environment:**
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate

3. **Install Requirements:**
   pip install flask flask-sqlalchemy flask-login

4. **Initialize Database:**
   In your terminal, run:
   python -c "from app import db; db.create_all()"

5. **Run the App:**
   python app.py

The application will be accessible at: http://127.0.0.1:5000/

## 📂 Project Directory Structure

flask-todo-app/
│
├── static/              # CSS styles and JavaScript
├── templates/           # HTML templates (Login, Signup, Index)
├── app.py               # Main application and routes
├── models.py            # User and Task database models
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation
