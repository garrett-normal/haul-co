from flask_wtf.form import _Auto

from flaskr import db
from flaskr.models import User, CargoType, Job, EmployeeType
from flask_login import current_user
import sqlalchemy as sqla
from flask_wtf import FlaskForm#, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FileField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, Length, EqualTo
import wtforms

class LoginForm(FlaskForm):
    username = StringField("Email", validators=[DataRequired(message="An email is required"), Email(message='A valid email is required')])
    password = PasswordField("Password", validators=[DataRequired(message="A password is required"), Length(min=8)])
    remember_me = BooleanField("Remember Me")
    # recaptcha = RecaptchaField()
    submit = SubmitField("Sign In")

class RegistrationForm(FlaskForm):
    username = StringField("Email", validators=[DataRequired(message="A valid email is required"), Email(message='A valid email is required')])
    password = PasswordField("Password", validators=[DataRequired(message="A password is required"), Length(min=8)])
    rep_password = PasswordField("Confirm password", validators=[DataRequired(message="You must confirm your password"), EqualTo('password')])
    # recaptcha = RecaptchaField()
    submit = SubmitField("Register")


    def validate_email(self, username):
        user = db.session.scalar(sqla.select(User).where(User.email == username.data))
        if user is not None:
            raise ValidationError("This email is already taken")

class TicketUploadForm(FlaskForm):
    img = FileField("Ticket image", validators=[wtforms.validators.regexp(r"^.+\.(jpg|png)$")]) # type: ignore
    job_select = SelectField("Job Selection", choices=[], coerce=int)
    ticket_type = SelectField("Ticket Type", choices=[(t.name, t.value) for t in CargoType]) 
    comments = TextAreaField("Comments or instructions", validators=[Length(max=300)])
    submit = SubmitField("Submit for review")

    def __init__(self, formdata=_Auto, **kwargs):
        super().__init__(formdata, **kwargs)
        if current_user.is_authenticated:
            jobs = db.session.scalars(sqla.select(Job).where(current_user.id == Job.driver_id)).all()
            self.job_select.choices = [(j.id, j.title) for j in jobs]

class JobCreationForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(message="A brief title is required"), Length(min=10, max=80, message="Title must be 10-80 characters.")])
    description = TextAreaField("Description", validators=[Length(max=400, message="No more than 400 characters should be used.")])
    driver = SelectField("Driver", choices=[], coerce=int,validators=[DataRequired(message="A driver must be selected.")])
    submit = SubmitField("Create Job")

    print("running form")
    def __init__(self, formdata=_Auto, **kwargs):
        print("running init")
        super().__init__(formdata, **kwargs)
        drivers = db.session.scalars(sqla.select(User).where(User.employee_status != EmployeeType.ADMIN)).all()
        if drivers.__len__() > 0:
            self.driver.choices = [(d.id, d.full_name + " - " + d.employee_status.value) for d in drivers]