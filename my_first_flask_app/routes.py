
from flask import render_template, url_for, flash, redirect
from my_first_flask_app import app, db, bcrypt
from my_first_flask_app.models import User, Post
from my_first_flask_app.forms import RegistrationForm, LoginForm

posts = [
    {
        'section': 'Mastitis checkup',
        'title': 'Mastitis information',
        'content': 'Here you can see an information about mastitis', 
        'date_posted': 'Jan 01, 2020'
    },
    {
        'section': 'Feeding status',
        'title': 'Information about feeding quality',
        'content': 'Here you can see an information about feeding process',
        'date_posted': 'Jan 01, 2020'
    },
    {
        'section': 'Ketosis checkup',
        'title': 'Ketosis information',
        'content': 'Here you can see an information about ketosis',
        'date_posted': 'Jan 01, 2020'
    },
    {
        'section': 'Heard overview',
        'title': 'Heard information',
        'content': 'Here you can see an information about your heard',
        'date_posted': 'Jan 01, 2020'
    }
]

@app.route("/") # home page 
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about") # home page 
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET', 'POST']) # registration page 
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #encrypting user password
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        #creating user with hashed password
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        #adding user with hashed password to the database
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST']) # home page 
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'asp@foss.dk' and form.password.data == '12345':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccesssful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)