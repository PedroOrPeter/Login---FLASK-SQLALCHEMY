from flask import render_template, url_for, flash, redirect
from crud import app, database, bcrypt
from crud.forms import FormLogin, FormCreateAccount
from crud.models import Usuario
from flask_login import login_user


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.password, form_login.password.data):
            login_user(usuario, remember=form_login.remember_button.data)
            flash(f'Welcome Back: {form_login.email.data}', 'alert-success')
            return redirect(url_for('home'))
        else:
            flash('Login Failed: ', 'alert-danger')
    return render_template('login.html', form_login=form_login)


@app.route('/signIn', methods=['GET', 'POST'])
def signIn():
    form_createAccount = FormCreateAccount()
    if form_createAccount.validate_on_submit():
        cript_password = bcrypt.generate_password_hash(form_createAccount.password.data)
        usuario = Usuario(username=form_createAccount.username.data, email=form_createAccount.email.data, password=cript_password)
        database.session.add(usuario)
        database.session.commit()
        flash(f'Welcome, {form_createAccount.username.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template('signIn.html', form_createAccount=form_createAccount)
