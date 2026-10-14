from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
import sqlalchemy as sqla

from flaskr import db
from flaskr.models import Ticket, Job, EmployeeType, BillableUnit, CargoType
from flaskr.forms import TicketUploadForm

vendor = Blueprint('vendor', __name__)

@vendor.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if not current_user.email_verified:
        return redirect(url_for('accounts.verify'))

    #                                                     [===Admins do not have a driver dashboard===]
    # if current_user.employee_status == EmployeeType.ADMIN:
    #     return redirect(url_for('admin.admin_dashboard'))

    form = TicketUploadForm()
    if form.validate_on_submit():
        ticket = Ticket(
            comments=form.comments.data,
            order_type=form.ticket_type.data,
            billabe_quantity=0,
            billable_unit=BillableUnit.CUBIC_METER,
            owner=current_user, # type: ignore
            owner_id=current_user.id)



    #.all() put data into a list
    user_tickets = db.session.scalars(sqla.select(Ticket).where(Ticket.owner_id == current_user.id)).all() #    .where(Ticket.status != TicketStatus.ACCEPTED)).all()
    active_jobs = db.session.scalars(sqla.select(Job).where(Job.id == current_user.id)).all()

    return render_template('vendor/vendor_dashboard.html', user_tickets=user_tickets, active_jobs=active_jobs, ticketForm=TicketUploadForm())

@vendor.route('/dashboard/tickets-submitted')
@login_required
def tickets_submitted():
    if not current_user.email_verified:
        return redirect(url_for('accounts.verify'))

    return render_template('vendor/tickets_submitted.html')