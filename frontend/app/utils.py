from flask import Blueprint, Config, current_app
from werkzeug.datastructures import FileStorage
import os
# from config import Config


def create_blueprint(name: str, url_prefix: str) -> Blueprint:
    return Blueprint(
        name,
        __name__,
        url_prefix=url_prefix,
        template_folder="templates",
        static_folder="static",
    )


def save_file(file: FileStorage, folder: str) -> str:
    # Generate absolute path for image
    uploads_folder = os.path.join(current_app.config["UPLOADS_FOLDER_ABSOLUTE"], folder)
    if not os.path.exists(uploads_folder):
        os.makedirs(uploads_folder)

    filename = file.filename
    file_path = os.path.join(uploads_folder, filename)

    file.save(file_path)

    return os.path.join("/uploads", folder, filename).replace("\\", "/")