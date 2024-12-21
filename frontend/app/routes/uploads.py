from flask import Blueprint, send_from_directory, current_app
# from config import Config


uploads_bp = Blueprint("uploads", __name__, url_prefix="/uploads")

@uploads_bp.route("/<folder>/<filename>")
def uploaded_file(folder, filename):
    allowed_folders = ['images', 'videos']
    if folder not in allowed_folders:
        return "Invalid folder", 404
    
    folder_path = f"{current_app.config['UPLOADS_FOLDER_RELATIVE']}/{folder}"
    
    return send_from_directory(folder_path, filename)
