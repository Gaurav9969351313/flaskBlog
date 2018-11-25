from flask import Flask
import os

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from companyblog.core.views import core
from companyblog.errorpages.handlers import errorpages
from companyblog.users.views import users

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

loinManager = LoginManager()
loinManager.init_app(app)
loinManager.login_view= 'users.login'

app.register_blueprint(core)
app.register_blueprint(errorpages)
app.register_blueprint(users)