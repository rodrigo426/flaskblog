
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'a938378b3ed72d986a532be7120cd635'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskblog.db'
db = SQLAlchemy(app)

from flaskblog import routes