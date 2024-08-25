# Grocery Market [Flask] 🛒

## Overview 📋
**Grocery Market** is a web-based application developed using the Flask framework. It is designed to simplify the management of grocery items for small to medium-sized businesses. The application offers secure user authentication, efficient product management, and robust database integration, making it an ideal solution for inventory management.

## Technical Stack 🛠️
- **Frontend**: HTML, CSS, Flask-WTF for form handling.
- **Backend**: Python, Flask, Flask-SQLAlchemy for ORM, Flask-Login for user session management.
- **Database**: SQLite (with Flask-SQLAlchemy).
- **Automation Tools**: PyAutoGUI, Pyperclip.
- **Deployment**: Render, Gunicorn for server.

## Features ✨
- **User Authentication**: Secure login and registration system with Flask-Login and Flask-Bcrypt.
- **Product Management**: Ability to add, update, delete, and view grocery items through an intuitive interface.
- **Database Integration**: Manage data storage and retrieval with Flask-SQLAlchemy.
- **Form Validation**: Robust form handling and validation using Flask-WTF and WTForms.
- **Automation Support**: Incorporates PyAutoGUI and Pyperclip for enhanced user interactions.
- **Responsive Design**: Accessible on various devices with a clean, user-friendly layout.

## Installation 🛠️

### Step 1: Clone the Repository
```bash
git clone https://github.com/sandip3/Grocery-Market.git
cd Grocery-Market
```

### Step 2: Create a Virtual Environment (Optional but Recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows/Ubuntu use `venv\Scripts\activate`
```

### Step 3: Install Flask and Required Dependencies
```bash
pip install Flask Flask-SQLAlchemy Flask-WTF WTForms email-validator Flask-Bcrypt Flask-Login pyautogui pyperclip
```
or 
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```
- Access the application by navigating to `http://127.0.0.1:5000` in your web browser.

## Usage 🚀

### User Authentication
- **Username**: sandip
- **Password**: sandip

- **Username**: user1
- **Password**: password1

You can also create a new account to log in and explore the features, including buying and selling grocery items.

### Managing Grocery Items
- **Add New Item**: Easily add new grocery items with details such as name, price, and quantity.
- **Update Item**: Modify existing grocery item details as needed.
- **Delete Item**: Remove items that are no longer needed.
- **View All Items**: Quickly view a list of all items in the inventory.

### Automation Tools
- **PyAutoGUI & Pyperclip**: Automate repetitive tasks like copying and pasting text, navigating through the app, and more.

## Deployment 🌐

- **Live Demo**: [Grocery Market on Render](https://grocery-market.onrender.com/)
- **GitHub Repository**: [Grocery Market on GitHub](https://github.com/sandip3/Grocery-Market)

## Dependencies 📦

- `Flask==3.0.3` - Web framework
- `Flask-SQLAlchemy==3.1.1` - Database ORM
- `Flask-WTF==1.2.1` - Form handling and validation
- `WTForms==3.1.2` - Form handling and validation
- `email-validator==2.2.0` - Email validation for forms
- `Flask-Bcrypt==1.0.1` - Password hashing
- `Flask-Login==0.6.3` - User session management
- `pyautogui==0.9.54` - Automation tool for GUI tasks
- `pyperclip==1.9.0` - Cross-platform clipboard module
- `gunicorn==23.0.0` - For serving the app with multithreading on platforms like Render

## Folder Structure 📂
```plaintext
Grocery-Market/
├── instance/
│   └── market.db
├── Market/
│   ├── static/
│   │   └── img/
│   │       └── Logo.png
│   ├── templates/
│   │   ├── includes/
│   │   │   ├── item.html
│   │   │   └── owned_item_model.html
│   │   ├── base.html
│   │   ├── HomePage.html
│   │   ├── login.html
│   │   ├── market.html
│   │   └── register.html
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   └── routes.py
│
├── .venv/
├── Procfile
├── Readme.md
├── requirements.txt
└── app.py
```

## Licensing 📜
This project is open-source and licensed under the MIT License. Contributions are welcome!

## Acknowledgments 🙏
- **Flask**: For providing a powerful and flexible web framework.
- **SQLAlchemy**: For seamless database integration.
- **Open-Source Community**: For various tools and libraries that made this project possible.

---
