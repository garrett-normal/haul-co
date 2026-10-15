from flask import Blueprint, render_template, redirect, url_for
from flaskr import db
from flaskr.models import User,EmployeeType, Job
from flaskr.forms import JobCreationForm

from flask_login import login_required, current_user
import sqlalchemy as sqla

admin = Blueprint(name='admin', import_name=__name__, url_prefix='/manage')

#admin dashboard
@admin.route('/dashboard', methods=['GET', 'POST'])
@login_required
def admin_dashboard():
    if not current_user.email_verified:
        return redirect(url_for('verify'))

    create_job = JobCreationForm()
    if create_job.validate_on_submit():
        driver = db.session.get(User, create_job.driver.data)
        if driver:
            job = Job(title=str(create_job.title.data),
                                desc=create_job.description.data,
                                driver=driver,
                                author=current_user)
            db.session.add(job)
            db.session.commit()

    
    #hard to explain this
    #double clause
    employee_list = db.session.scalars(db.select(User).where(User.id != current_user.id).where(User.employee_status == EmployeeType.ADMIN)).all()
    mems = db.session.scalars(db.select(User).where(User.id != current_user.id).where(User.employee_status != EmployeeType.ADMIN)).all()
    return render_template('admin/admin_dashboard.html', employee_list=employee_list, mems=mems, ticket_review_count=1, new_job_form=create_job)


#have a clickable graph on the dashboard that links to the jobs page
@admin.route('/jobs')
@login_required
def jobs():
    return render_template('admin/active_jobs.html')