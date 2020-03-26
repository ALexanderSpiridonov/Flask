from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app=Flask(__name__)
app.config['SECRET_KEY'] = '60d198c06f34330635165c34358eedc4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

################################################################## __ DATABASE STRUCTURE __ #######################################################################
#creating database as classes 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    # чтобы достать все посты юзера. это не колонка это дополнительный запрос ко всем публикациям пользователя one to many relationships
    # Один пользователь может иметь несколько постов, но один пост может иметь только одного юзера. 
    # мы создаем связь к Post (входит как строка). backref - вроде колонки к Post (или идентификатора), чтобы найти автора в таблице постов.
    posts = db.relationship('Post', backref='author', lazy=True) 

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"   # как печатать объект

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    # НУЖНО что бы обозначить юзера в посте. чтобы обеспечить связь таблиц через ForeignKey with lowercase. 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

###########################################################################################################################################################################

posts = [
    {
        'section': 'Mastitis checkup',
        'title': 'Mastitis information',
        'content': 'Here you can see an information about mastitis', 
        'date_posted': 'Jan 01, 2020'
    },
    {
        'section': 'Ketosis checkup',
        'title': 'Ketosis information',
        'content': 'Here you can see an information about ketosis',
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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
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

if __name__ == '__main__':
    app.run(debug=True)