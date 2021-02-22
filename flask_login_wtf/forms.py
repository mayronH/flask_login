from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class SignupForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[
                                    DataRequired(), 
                                    Email(message="Informe um email válido"), 
                                    Length(min=6, message="Email precisa ter pelo menos 6 caracteres")
                                ]
    )
    password = PasswordField('Senha', validators=[DataRequired()])
    confirm = PasswordField('Confirme sua senha', validators=[
                                                    DataRequired(), 
                                                    EqualTo('password', message="Senhas não batem")
                                                ]
    )
    submit = SubmitField('Registrar')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
                                    DataRequired(), 
                                    Email(message="Informe um email válido"), 
                                    Length(min=6, message="Email precisa ter pelo menos 6 caracteres")
                                ]
    )
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Login')