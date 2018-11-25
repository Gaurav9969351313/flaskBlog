from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from wtforms.file import FileField,FileAllowed

from flask_login import current_user

from companyblog.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('UserName', validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('passConfirm',message='Passwords Must Match')])
    passConfirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register')

    def checkMail(self,field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('Your email has registered already...!!!')

    def checkUsername(self,field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('Your username has registered already...!!!')

class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('UserName', validators=[DataRequired()])
    picture = FileField('Update Profile Pic',validators=[FileAllowed(['jpg','jpeg','png'])])
    submit = SubmitField('Update')
    
    def checkMail(self,field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('Your email has registered already...!!!')

    def checkUsername(self,field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('Your username has registered already...!!!')
