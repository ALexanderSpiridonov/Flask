from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SECRET_KEY'] = '60d198c06f34330635165c34358eedc4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from my_first_flask_app import routes