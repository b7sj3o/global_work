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
from ..utils import create_blueprint
from ..forms import LoginForm

# from config import Config
import json

base_bp = create_blueprint(name="base", url_prefix="/")


@base_bp.route("/")
def home():
    response = requests.get(f"{current_app.config['VACANCY_ENDPOINT']}/list")
    data = json.loads(response.text)

    return render_template("index.html", vacancies=data)


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
    if "authorized" in session:
        flash("Ви вже зареєстровані", "success")
        return redirect(url_for("base.home"))

    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            data = {"username": form.username.data, "password": form.password.data}

            response = requests.get(
                f"{current_app.config['ADMIN_ENDPOINT']}/login", json=data
            )
            response_data = response.json()

            if response.status_code == 200:
                # setting cookies
                session["authorized"] = True

                flash(response_data["message"], "success")
                return redirect(url_for("admin.admin"))
            else:
                flash(response_data.get("detail", "Помилка"), "danger")

        else:
            flash("Форма містить помилки. Перевірте введені дані.", "danger")

    return render_template("login.html", form=form)
