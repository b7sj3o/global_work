from flask import Flask, request, send_from_directory
from .routes import base_bp, admin_bp, vacancy_bp, uploads_bp

app = Flask(__name__, template_folder="templates", static_folder="static")

app.register_blueprint(base_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(vacancy_bp)
app.register_blueprint(uploads_bp)

app.config.from_object("config.Config")
    

