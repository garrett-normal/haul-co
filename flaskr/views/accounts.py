# login, logout, register, email verification, etc
import os
from flaskr import db
from flaskr.forms import LoginForm, RegistrationForm
from flaskr.models import User, EmployeeType

from werkzeug.security import check_password_hash
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sqla

accounts = Blueprint('accounts', __name__)

#fix for prod, in debug mode
@accounts.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = RegistrationForm()
    if form.validate_on_submit():
        print("RUNNING")
        user = User()
        user.email = str(form.username.data)
        user.full_name = 'John Smith'
        user.set_password('password')
        user.employee_status = EmployeeType.ADMIN

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('accounts.verify'))

    return render_template('accounts/register.html', form=form)

@accounts.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = LoginForm()
    
    if form.validate_on_submit():
        hash = os.environ.get('FAKE_HASH')

        if not hash or not form.password.data:
            raise RuntimeError('Hash hasn\'t been set or password data is None')

        #Check password & user account - extra hash adds time to request so users cannot tell if account exists or not (hash doesnt run if user doesnt exist)
        user = db.session.scalar(sqla.select(User).where(User.email == form.username.data))
        password_ok = user.check_password(form.password.data) if user else check_password_hash(hash, form.password.data)

        if user is None or not password_ok:
            return redirect(url_for('accounts.login'))

        #log user in and redirect
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('dashboard'))

    return render_template('accounts/login.html', form=form)

@accounts.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('accounts.login'))

@accounts.route('/verify')
def verify():
    if not current_user.is_authenticated or current_user.email_verified:
        return redirect(url_for('home'))
    return render_template('accounts/email_verification.html')

@accounts.route('/account-settings')
@login_required
def settings():
    return render_template('accounts/settings.html')