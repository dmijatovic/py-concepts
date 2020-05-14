from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user

from app.models import User

class RegistrationForm(FlaskForm):
  username=StringField("Username",
    validators=[DataRequired(),Length(min=4,max=100)])
  email=StringField("Email",
    validators=[DataRequired(), Email()])
  password=PasswordField("Password",
    validators=[DataRequired(),Length(min=6,max=100)])
  confirm_password=PasswordField("Confirm password",
    validators=[DataRequired(), EqualTo('password')])

  submit=SubmitField("Sign up")

  # custom validation function
  def validate_username(self,username):
    user = User.query.filter_by(username=username.data).first()
    if user:
      raise ValidationError(f'Username {username.data} already used')

  # custom validation email
  def validate_email(self,email):
    user = User.query.filter_by(email=email.data).first()
    if user:
      raise ValidationError(f'Email {email.data} already used')


class LoginForm(FlaskForm):
  email=StringField("Email",
    validators=[DataRequired(),Length(min=4,max=100)])
  password=PasswordField("Password",
    validators=[DataRequired(),Length(min=6,max=100)])
  remember=BooleanField("Remember me")

  submit=SubmitField("Log in")


class UpdateAccountForm(FlaskForm):
  username=StringField("Username",
    validators=[DataRequired(),Length(min=4,max=100)])
  email=StringField("Email",
    validators=[DataRequired(), Email()])

  picture = FileField("Update profile picture",
    validators=[FileAllowed(['jpg','png','svg'])])

  submit=SubmitField("Update")

  # custom validation function
  def validate_username(self,username):
    if username.data != current_user.username:
      user = User.query.filter_by(username=username.data).first()
      if user:
        raise ValidationError(f'Username {username.data} already used')

  # custom validation email
  def validate_email(self,email):
    if email.data != current_user.email:
      user = User.query.filter_by(email=email.data).first()
      if user:
        raise ValidationError(f'Email {email.data} already used')

class PostNewForm(FlaskForm):
  title=StringField("Title",[DataRequired()])
  content=TextAreaField("Content",[DataRequired()])
  submit=SubmitField("Post")

