from flask import Blueprint, render_template, redirect, url_for
from flaskr import db
from flaskr.models import User,EmployeeType

from flask_login import login_required, current_user

admin = Blueprint(name='admin', import_name=__name__, url_prefix='/manage')

#admin dashboard
@admin.route('/dashboard')
@login_required
def admin_dashboard():
    if not current_user.email_verified:
        return redirect(url_for('verify'))
    #hard to explain this
    #double clause
    employee_list = db.session.scalars(db.select(User).where(User.id != current_user.id).where(User.employee_status == EmployeeType.ADMIN)).all()
    mems = db.session.scalars(db.select(User).where(User.id != current_user.id).where(User.employee_status != EmployeeType.ADMIN)).all()
    return render_template('admin/admin_dashboard.html', employee_list=employee_list, mems=mems)


#have a clickable graph on the dashboard that links to the jobs page
@admin.route('/jobs')
@login_required
def job_view_admin():
    return render_template('admin/admin_jobs_view.html')