from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
  username=StringField("Username",
    validators=[DataRequired(),Length(min=4,max=20)])
  email=StringField("Email",
    validators=[DataRequired(),Length(min=4,max=20), Email()])
  password=PasswordField("Password",
    validators=[DataRequired(),Length(min=4,max=100)])
  confirm_password=PasswordField("Password",
    validators=[DataRequired(),Length(min=4,max=100), EqualTo(password)])

  submit=SubmitField("Sign up")


class LoginForm(FlaskForm):
  username=StringField("Email",
    validators=[DataRequired(),Length(min=4,max=20)])  
  password=PasswordField("Password",
    validators=[DataRequired(),Length(min=4,max=100)])
  remember=BooleanField("Remember me")

  submit=SubmitField("Log in")

