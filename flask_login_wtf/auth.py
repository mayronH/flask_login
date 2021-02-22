from flask import Blueprint, render_template, redirect
from flask.globals import request
from flask.helpers import url_for, flash
from flask_login import login_user, current_user
from datetime import datetime
from .forms import SignupForm, LoginForm
from .models import User
from . import db, login_manager

auth_blueprint = Blueprint('auth_blueprint', __name__, template_folder='templates', static_folder='static')

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main_blueprint.app'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(password=form.password.data):
            login_user(user)
            next_page = request.args.get('next')

            return redirect(next_page or url_for('main_blueprint.app'))

        flash('Email/senha inválidos')
        return redirect(url_for('auth_blueprint.login'))
    
    return render_template(
        'login.html',
        form = form
    )

@auth_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()

        if existing_user is None:
            user = User(
                name=form.name.data,
                email=form.email.data,
                created_date=datetime.now()
            )
            user.set_password(form.password.data)

            db.session.add(user)
            db.session.commit()
            login_user(user)

            return redirect(url_for('main_blueprint.app'))

        flash('Já existe um registro com esse email')

    return render_template(
        'signup.html',
        form = form
    )

@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    flash("Você precisa estar logado para continuar nesta página")
    return redirect(url_for('auth_blueprint.login'))

