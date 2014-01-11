from flask import Flask, render_template, flash, redirect
from app import app
from forms import LoginForm

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Sign In',
                           form = form)

if __name__ == '__main__':
    app.run(debug=True)
