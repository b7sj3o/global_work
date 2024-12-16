from flask import Blueprint, send_from_directory, current_app
import os

uploads_bp = Blueprint("uploads", __name__, url_prefix="/uploads")

@uploads_bp.route("/<path:filename>")
def uploaded_file(filename):
    uploads_folder = os.path.join(current_app.root_path, "uploads")
    return send_from_directory(uploads_folder, filename)
