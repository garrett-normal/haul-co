# login, logout, register, email verification, etc
import os
from flaskr import db
from flaskr.forms import LoginForm, RegistrationForm
from models import User

from werkzeug.security import check_password_hash
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user
import sqlalchemy as sqla

accounts = Blueprint('accounts', __name__)

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
            return redirect(url_for('login'))

        #log user in and redirect
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('dashboard'))

    return render_template('login.html', form=form)