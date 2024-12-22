from datetime import timedelta
import requests
from flask import (
    flash,
    redirect,
    render_template,
    request,
    url_for,
    make_response,
    current_app,
    session,
)
from flask_babel import _
from ..utils import create_blueprint
import json

base_bp = create_blueprint(name="base", url_prefix="/")


@base_bp.route("/")
def home():
    vacancies = requests.get(f"{current_app.config['VACANCY_ENDPOINT']}/list").json()

    lang = request.cookies.get("language", "uk")

    return render_template("index.html", vacancies=vacancies, lang=lang)


@base_bp.route("/about_us")
def about_us():
    return render_template("about-us.html")


@base_bp.route("/reviews")
def reviews():
    return render_template("reviews.html")

@base_bp.route("/contacts")
def contacts():
    return render_template("contacts.html")

@base_bp.route("/login", methods=["GET", "POST"])
def login():
    if session.get("authorized"):
        flash(_("Ви вже зареєстровані"), "success")
        return redirect(url_for("base.home"))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        remember_me = "remember_me" in request.form

        data = {"username": username, "password": password}
        
        response = requests.get(
            f"{current_app.config['ADMIN_ENDPOINT']}/login", json=data
        )

        if response.status_code == 200:
            session["authorized"] = True
            flash(_("Ви успішно ввійшли в акаунт!"), "success")
            
            # Set session lifetime
            if remember_me:
                session.permanent = True
                current_app.permanent_session_lifetime = timedelta(days=32) 
            else:
                session.permanent = False # expire if you close the browser
                current_app.permanent_session_lifetime = timedelta(days=1) 

            return redirect(url_for("admin.admin"))
        else:
            flash(_("Трапилася помилка!"), "danger")

    return render_template("login.html")
