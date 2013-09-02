#USING WTF
from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField, BooleanField
from models import db, User, Entries

class SignupForm(Form):
    firstname = TextField("First name:",  [validators.DataRequired("Please enter your first name.")])
    lastname = TextField("Last name:",  [validators.DataRequired("Please enter your last name.")])
    email = TextField("Email:",  [validators.DataRequired("Please enter your email address."), validators.Email("Please enter your email address.")])
    password = PasswordField('Password:', [validators.Required("Please enter a password.")])
    submit = SubmitField("Send")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email = self.email.data.lower()).first()
        if user:
            self.email.errors.append("That email is already taken")
            return False
        else:
            return True

class LoginForm(Form):
    email = TextField("Email:",  [validators.DataRequired("Please enter your email address."), validators.Email("Please enter your email address.")])
    password = PasswordField('Password:', [validators.DataRequired("Please enter a password.")])
    submit = SubmitField("Sign In")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email = self.email.data.lower()).first()

        if user and user.check_password(self.password.data):
            return True
        else:
            self.email.errors.append("Invalid e-mail or password")
            return False

class PublishForm(Form):
    topic = TextField("Title:", [validators.DataRequired("Please enter your title"),validators.length(min=5, max=100, message="Please enter characters between 5 and 100")])
    article = TextAreaField("Article:", [validators.DataRequired("field cannot be blank"),validators.length(min = 50, max=700, message="Please enter characters between 50 and 700")])
    submit = SubmitField("Send")


    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
