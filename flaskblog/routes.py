from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author':'Rodrigo Moura',
        'title':'Post 1',
        'content':' conteudo ahahaha',
        'date_posted':'April 11, 2019'
    },
    {
        'author':'Carlos Santana',
        'title':'Post 2',
        'content':' conteudo asodjaspdk',
        'date_posted':'April 11, 2019'
    },
    {
        'author':'Carlos Santana',
        'title':'Post 3',
        'content':' conteudo asodjaspdk',
        'date_posted':'April 13, 2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == '123':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsucessful. Please check username and passowrd', 'danger')

    return render_template('login.html', title='Login', form=form)