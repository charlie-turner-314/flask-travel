from datetime import date, datetime
from travel import create_app
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo



#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    
    #linking two fields - password should be equal to data entered in confirm
    password = PasswordField('Password', validators=[InputRequired(),
                         EqualTo('confirm',
                         message="Passwords must match")])
    confirm = PasswordField("Confirm Password")
    #submit button
    submit = SubmitField("Register")

class DestinationForm(FlaskForm):
    name = StringField('Country', validators=[InputRequired()])
    # adding two validators, one to ensure input is entered and other to check if the 
    #description meets the length requirements
    description = TextAreaField('Description', 
                validators=[InputRequired()])
    image = StringField('Cover Image', validators=[InputRequired()])
    currency = StringField('Currency', validators=[InputRequired()])
    submit = SubmitField("Create")

    #this should already be there in the forms.py
  
class CommentForm(FlaskForm):
    text = TextAreaField('Comment', [InputRequired()])
    created_at = datetime.now()
    submit = SubmitField('Post Comment')