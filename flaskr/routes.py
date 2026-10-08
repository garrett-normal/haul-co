from flask import render_template, url_for
from flaskr import app, db
import os

import sqlalchemy as sqla
from sqlalchemy import Boolean
from .forms import LoginForm, RegistrationForm, TicketUploadForm
from flaskr.models import Ticket, User, EmployeeType, Job
from flask import request, redirect
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.security import check_password_hash


@app.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('index.html')