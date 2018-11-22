from flask import Flask, render_template
from companyblog.core.views import core
from companyblog.errorpages.handlers import errorpages

app = Flask(__name__)

app.register_blueprint(core)
app.register_blueprint(errorpages)
