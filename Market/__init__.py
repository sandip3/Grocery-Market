# import secrets
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # To suppress a warning
# app.config["SECRET_KEY"] = secrets.token_hex(16)
app.config["SECRET_KEY"] = "b3f00564665f1451456930157dd19504"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page" 
login_manager.login_message_category = "info"


from Market import routes

# from Market import models
