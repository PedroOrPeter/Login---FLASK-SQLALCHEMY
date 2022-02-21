from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)


app.config['SECRET_KEY'] = 'e944ba60802ad434a1c0c9961d6c3ff2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from crud import routes