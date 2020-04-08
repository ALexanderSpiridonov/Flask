from datetime import datetime
from my_first_flask_app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

################################################################## __ DATABASE STRUCTURE __ #######################################################################
#creating database as classes

class User(db.Model, UserMixin):
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