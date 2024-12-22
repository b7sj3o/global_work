from flask import Flask, request, send_from_directory
from flask_babel import Babel
from .routes import base_bp, admin_bp, vacancy_bp, uploads_bp


app = Flask(__name__, template_folder="templates", static_folder="static")
app.config.from_object("config.Config")

babel = Babel()

def get_locale():
    return request.cookies.get('language', app.config['BABEL_DEFAULT_LOCALE'])

babel.init_app(app, locale_selector=get_locale)

app.register_blueprint(base_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(vacancy_bp)
app.register_blueprint(uploads_bp)


    

