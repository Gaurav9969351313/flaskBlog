from flask import Flask, render_template
from companyblog.core.views import core

app = Flask(__name__)

app.register_blueprint(core)
