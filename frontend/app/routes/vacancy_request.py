from ..utils import create_blueprint

from flask import Blueprint, flash, render_template, request, redirect, url_for
from config import Config
import requests

from ..forms import VacancyRequestForm


vacancy_request_bp = Blueprint("vacancy_request", __name__, url_prefix="/vacancy_request")


@vacancy_request_bp.route("/send_request/<int:vacancy_id>", methods=["POST"])
def send_request(vacancy_id):
    form = VacancyRequestForm()

    if form.validate_on_submit():
        data = {
            "vacancy_id": vacancy_id,
            "name": form.name.data,
            "phone_number": form.phone_number.data
        }
        response = requests.post(f"{Config.VACANCY_REQUEST_ENDPOINT}/create", json=data)

        if response.status_code == 200:
            flash("Ви успішно надіслали заявку!", "success")
            return redirect(url_for("vacancy.get_vacancy", vacancy_id=vacancy_id))
        else:
            flash("Трапилася помилка, зверніться в підтримку, якщо вважаєте, що це баг", "danger")

    return render_template("vacancy.html", form=form, vacancy_id=vacancy_id)