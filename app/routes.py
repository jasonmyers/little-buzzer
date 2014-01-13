from flask import Flask, render_template, flash, redirect
from app import app
from forms import LoginForm

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data +
               '", remember_me=' + str(form.remember_me.data))
        return redirect('/')
    
    return render_template('login.html', title = 'Sign In',
                           form = form,
                           providers = app.config['OPENID_PROVIDERS'])
