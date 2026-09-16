from flaskr import db
from flaskr.models import User
import sqlalchemy as sqla
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, ValidationError, Email, Length, EqualTo
import wtforms

class LoginForm(FlaskForm):
    username = StringField("Email", validators=[DataRequired(message="An email is required"), Email()])
    password = PasswordField("Password", validators=[DataRequired(message="A password is required"), Length(min=8)])
    remember_me = BooleanField("Remember Me")
    # recaptcha = RecaptchaField()
    submit = SubmitField("Sign In")

class RegistrationForm(FlaskForm):
    username = StringField("Email", validators=[DataRequired(message="A valid email is required"), Email()])
    password = PasswordField("Password", validators=[DataRequired(message="A password is required"), Length(min=8)])
    rep_password = PasswordField("Confirm password", validators=[DataRequired(message="You must confirm your password"), EqualTo('password')])
    # recaptcha = RecaptchaField()
    submit = SubmitField("Register")


    def validate_email(self, username):
        user = db.session.scalar(sqla.select(User).where(User.email == username.data))
        if user is not None:
            raise ValidationError("This email is already taken")

class TicketUploadForm(FlaskForm):
    # img = FileField("Ticket image", validators=[wtforms.validators.regexp(r"^.+\.(jpg|png)$")]) # type: ignore
    comments = TextAreaField("Comments or instructions", validators=[Length(max=300)])
    submit = SubmitField("Submit for Review")