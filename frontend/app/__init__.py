from flask import Flask

app = Flask(__name__, template_folder="templates", static_folder="static/CSS")

from .routes import home

app.config.from_object('config.default')



