from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from crud.models import Usuario

class FormCreateAccount(FlaskForm):
    username = StringField(' Username ', validators=[DataRequired()])
    email = StringField(' E-mail ', validators=[DataRequired(), Email()])
    password = PasswordField(' Password ', validators=[DataRequired(), Length(8, 16)])
    confirm_password = PasswordField(' Confirm Password ', validators=[DataRequired(), EqualTo('password')])
    button_submit_createAccount = SubmitField(' Confirm ')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail already exist')


class FormLogin(FlaskForm):
    email = StringField(' E-mail ', validators=[DataRequired(), Email()])
    password = PasswordField(' Password ', validators=[DataRequired(), Length(8, 16)])
    button_submit_confirmAccount = SubmitField(' Confirm ')
    remember_button = BooleanField(' Remember me ')