from flask import Flask, request, send_from_directory
from .routes import base_bp, admin_bp, vacancy_bp, uploads_bp, vacancy_request_bp
from config import Config


app = Flask(__name__, template_folder="templates", static_folder="static")

app.config["SECRET_KEY"] = "your_secret_key"


app.register_blueprint(base_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(vacancy_bp)
app.register_blueprint(vacancy_request_bp)
app.register_blueprint(uploads_bp)

@app.route('/uploads/<folder>/<filename>')
def uploads(folder, filename):
    allowed_folders = ['images', 'videos']
    if folder not in allowed_folders:
        return "Invalid folder", 404
    
    folder_path = f"{Config.UPLOADS_FOLDER_RELATIVE}/{folder}"
    
    return send_from_directory(folder_path, filename)

app.config.from_object("config.default")
    

