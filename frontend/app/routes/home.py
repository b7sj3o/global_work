import requests
from flask import render_template
from ..utils import create_blueprint
from config import Config
import json

base_bp = create_blueprint(name="base", url_prefix="/")

@base_bp.route("/")
def home():
    response = requests.get(f"{Config.VACANCY_ENDPOINT}/list")
    data = json.loads(response.text)

    return render_template("index.html", vacancies=data)


@base_bp.route("/about_us")
def about_us():
    return render_template("about-us.html")