# Grocery Market [Flask] 🛒

## Overview 📋
**Grocery Market** is a web-based application designed to simplify the management of grocery items for small to medium-sized businesses. 
- Built with Flask, this application allows users to securely log in, manage their inventory, and track grocery items with ease.

## Features ✨
- **User Authentication**: Secure user login and registration system powered by Flask-Login and Flask-Bcrypt.
- **Product Management**: Add, update, delete, and view grocery items through a user-friendly interface.
- **Database Integration**: Efficient data storage and retrieval using Flask-SQLAlchemy.
- **Form Validation**: Robust form handling and validation using Flask-WTF and WTForms.
- **Responsive Design**: Accessible across various devices with a clean and intuitive layout.
- **Automation Tools**: Includes support for automation with `pyautogui` and `pyperclip` for enhanced user interactions.

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
pip install Flask
pip install Flask-SQLAlchemy
pip install Flask-WTF
pip install WTForms
pip install email-validator
pip install Flask-Bcrypt
pip install Flask-Login
pip install pyautogui pyperclip
```
or 

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python run.py
```
- Access the application by navigating to `http://127.0.0.1:5000` in your web browser.

## Usage 🚀

### User Authentication
- **Username**: sandip
- **Password**: sandip

### Managing Grocery Items
- **Add New Item**: Easily add new grocery items with details such as name, price, and quantity.
- **Update Item**: Modify existing grocery item details as needed.
- **Delete Item**: Remove items that are no longer needed.
- **View All Items**: Quickly view a list of all items in the inventory.

### Automation Tools
- **PyAutoGUI & Pyperclip**: Automate repetitive tasks like copying and pasting text, navigating through the app, and more.

## Dependencies 📦
- `Flask` - Web framework
- `Flask-SQLAlchemy` - Database ORM
- `Flask-WTF` - Form handling and validation
- `WTForms` - Form handling and validation
- `email-validator` - Email validation for forms
- `Flask-Bcrypt` - Password hashing
- `Flask-Login` - User session management
- `pyautogui` - Automation tool for GUI tasks
- `pyperclip` - Cross-platform clipboard module

## Folder Structure 📂
```plaintext
Grocery-Market/
├── instance
│   └── market.db
├── Market/
│   ├── static
│   │   └── img
│   │       └── Logo.png
│   ├── templates/
│   │   ├── includes
│   │   │   ├── item.html
│   │   │   └── owned_item_model.html
│   │   ├── base.html
│   │   ├── HomePage.html
│   │   ├── login.html
│   │   ├── market.html
│   │   └── register.html
│   ├── static/
│   │   ├── main.css
│   │   └── images/
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   └── routes.py
│
├── .venv
├── Procfile
├── Readme.md
├── requirements.txt
└── run.py
```

## Licensing 📜
This project is open-source and licensed under the MIT License. Contributions are welcome!

## Acknowledgments 🙏
- **Flask**: For providing a powerful and flexible web framework.
- **SQLAlchemy**: For seamless database integration.
- **Open-Source Community**: For various tools and libraries that made this project possible.

---


"pip install gunicorn" = For seveing mutithreding yout app in heruku it use 'Procfile'
'Procfile' = used by heruku for deploying app
