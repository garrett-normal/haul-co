from flask import Flask, redirect, url_for
from config import Config
# from .filters import datetime_format
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_talisman import Talisman
import flask_talisman

#main app & config
app = Flask(__name__)
app.config.from_object(Config)

#register filters
@app.template_filter('datetime_format')
def datetime_format(value, format="%H:%M %d-%m-%y"):
    return value.strftime(format)
app.jinja_env.filters['datetime_format'] = datetime_format

#talisman security
Talisman(app, 
         content_security_policy= {
             'default-src': '\'self\'',
             'style-src': ['\'self\'', 'fonts.googleapis.com', 'https://googleapis.com', 'cdn.jsdelivr.net', '\'unsafe-inline\'', '\'unsafe-hashes\''],
             'font-src': ['\'self\'', 'fonts.googleapis.com', 'https://fonts.gstatic.com', 'cdn.jsdelivr.net'],
             'script-src': ['\'self\'', 'cdn.jsdelivr.net']
         }, 
         content_security_policy_nonce_in=['\'style-src\''])

#database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#csrf protection
csrf = CSRFProtect(app)

#user management
login_manager = LoginManager(app)
# login_manager.login_view = "login" # type: ignore
@login_manager.unauthorized_handler
def unauthorized():
    return "You must be logged in to view this page."

# from app import routes
from flaskr import forms, routes, models
