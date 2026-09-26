from flask import render_template, url_for
from flaskr import app, db
import os

from datetime import datetime, timezone
import sqlalchemy as sqla
from .forms import LoginForm, RegistrationForm, TicketUploadForm
from flaskr.models import Ticket, User, TicketStatus
from flask import request, redirect
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.security import check_password_hash


@app.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
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



@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User()
        user.email = str(form.username.data)
        user.set_password(str(form.password.data))

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('verify'))

    return render_template('register.html', form=form)

@app.route('/verify')
def verify():
    if not current_user.is_authenticated or current_user.email_verified:
        return redirect(url_for('home'))
    return render_template('email_verification.html')

@app.route('/ticket-submission', methods=['GET', 'POST'])
@login_required
def ticket_submission():
    form = TicketUploadForm()
    msg=None

    if form.validate_on_submit() and current_user:
        ticket = Ticket()
        ticket.owner_id = current_user.id
        ticket.comments = form.comments.data
        db.session.add(ticket)
        db.session.commit()
        form=None
        msg='Your ticket has been submitted for review.'

    return render_template('upload.html', form=form, msg=msg)

@app.route('/dashboard')
@login_required
def dashboard():
    if not current_user.email_verified:
        return redirect(url_for('verify'))
    
    tickets_in_review = db.session.scalars(sqla.select(Ticket)) #    .where(Ticket.status != TicketStatus.ACCEPTED)).all()

    return render_template('vendor_dashboard.html', tickets_in_review=tickets_in_review)

@app.route('/dashboard/tickets-submitted')
@login_required
def tickets_submitted():
    if not current_user.email_verified:
        return redirect(url_for('verify'))

    return render_template('tickets_submitted.html')