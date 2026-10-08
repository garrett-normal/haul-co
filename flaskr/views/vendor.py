from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
import sqlalchemy as sqla

from flaskr import db
from flaskr.models import Ticket, Job
from flaskr.forms import TicketUploadForm

vendor = Blueprint('vendor', __name__)

@vendor.route('/ticket-submission', methods=['GET', 'POST'])
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

    return render_template('vendor/upload.html', form=form, msg=msg)

@vendor.route('/dashboard')
@login_required
def dashboard():
    if not current_user.email_verified:
        return redirect(url_for('accounts.verify'))

    #                                                     [===Admins do not have a driver dashboard===]
    # if current_user.employee_status == EmployeeType.ADMIN:
    #     return redirect(url_for('admin.admin_dashboard'))

    #.all() put data into a list
    tickets_in_review = db.session.scalars(sqla.select(Ticket).where(Ticket.owner_id == current_user.id)).all() #    .where(Ticket.status != TicketStatus.ACCEPTED)).all()
    active_jobs = db.session.scalars(sqla.select(Job).where(Job.id == current_user.id)).all()

    print('JOBS ',active_jobs)
    print('TICKETS ',tickets_in_review)

    return render_template('vendor/vendor_dashboard.html', tickets_in_review=tickets_in_review, active_jobs=active_jobs)

@vendor.route('/dashboard/tickets-submitted')
@login_required
def tickets_submitted():
    if not current_user.email_verified:
        return redirect(url_for('accounts.verify'))

    return render_template('vendor/tickets_submitted.html')