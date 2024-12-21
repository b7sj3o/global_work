from flask import Blueprint, flash, render_template, request, redirect, url_for, current_app
# from config import Config
import requests
from wtforms import FileField, StringField, TextAreaField

from ..utils import save_file
from ..forms import VacancyForm, VacancyRequestForm


vacancy_bp = Blueprint("vacancy", __name__, url_prefix="/vacancy")

@vacancy_bp.route("/<int:vacancy_id>", methods=["GET", "POST"])
def get_vacancy(vacancy_id):
    
    form = VacancyRequestForm()

    if request.method == "POST":
        if form.validate_on_submit():
            data = {
                "vacancy_id": vacancy_id,
                "name": form.name.data,
                "phone_number": form.phone_number.data
            }
            response = requests.post(f"{current_app.config['VACANCY_REQUEST_ENDPOINT']}/create", json=data)

            print(response.status_code)
            if response.status_code == 200:
                flash("Ви успішно надіслали заявку!", "success")
                return redirect(url_for("vacancy.get_vacancy", vacancy_id=vacancy_id))
            elif response.status_code == 400:
                flash("Ваша заявка вже подана для цієї вакансії", "warning")
            else:
                flash("Сталася помилка, зверніться в підтримку, якщо вважаєте, що це баг", "danger")
        else:
            flash("Форма містить помилки. Перевірте введені дані.", "danger")

    response = requests.get(f"{current_app.config['VACANCY_ENDPOINT']}/{vacancy_id}")

    if response.status_code == 200:
        vacancy = response.json()
    else:
        flash("Вакансію не знайдено", "danger")

    return render_template("vacancy.html", vacancy=vacancy, form=form)


@vacancy_bp.route("/create", methods=["GET", "POST"])
def create_vacancy():
    form = VacancyForm()

    if request.method == "POST" and form.validate_on_submit():
        data = {
            "title": form.title.data,
            "title_ru": form.title_ru.data,
            "description": form.description.data,
            "description_ru": form.description_ru.data,
            "salary": form.salary.data,
            "salary_ru": form.salary_ru.data,
            "schedule": form.schedule.data,
            "schedule_ru": form.schedule_ru.data,
            "accommodation": form.accommodation.data,
            "accommodation_ru": form.accommodation_ru.data,
            "work_location": form.work_location.data,
            "work_location_ru": form.work_location_ru.data,
            "main_image_path": "",
            "images_path": [],
            "video_path": ""
        }

        main_image = form.main_image_path.data
        if main_image:
            data["main_image_path"] = save_file(main_image, current_app.config['IMAGES_SAVE'])

        additional_images = request.files.getlist(form.images_path.name)
        filenames = []
        for img in additional_images:
            if img:
                filenames.append(save_file(img, current_app.config['IMAGES_SAVE']))
        data["images_path"] = filenames

        video = form.video_path.data
        if video and video.filename:
            data["video_path"] = save_file(video, current_app.config['VIDEOS_SAVE'])

        try:
            response = requests.post(f"{current_app.config['VACANCY_ENDPOINT']}/create", json=data)
            response.raise_for_status()
            flash("Вакансію створено успішно!", "success")
            return redirect(url_for("base.home"))
        except requests.RequestException as e:
            flash(f"Помилка при створенні вакансії: {str(e)}", "danger")
    elif request.method == "POST":
        flash("Форма не валідна, повідомте розробника, якщо вважаєте, що це баг", "danger")
    
    return render_template("vacancy-form.html", form=form)


@vacancy_bp.route("/update/<int:vacancy_id>", methods=["POST"])
def update_vacancy(vacancy_id):
    # Логіка для оновлення вакансії
    return f"Оновлено вакансію {vacancy_id}"


@vacancy_bp.route("/delete/<int:vacancy_id>", methods=["POST"])
def delete_vacancy(vacancy_id):
    response = requests.delete(f"{current_app.config['VACANCY_ENDPOINT']}/delete/{vacancy_id}")
    if response.status_code == 204:
        flash("Вакансію успішно видалено!", "success")
    else:
        flash("Не вдалося видалити вакансію.", "danger")

    return redirect(url_for("base.home"))


@vacancy_bp.route("/delete-request/<int:request_id>", methods=["POST"])
def delete_request(request_id):
    response = requests.delete(f"{current_app.config['VACANCY_REQUEST_ENDPOINT']}/delete/{request_id}")
    if response.status_code == 204:
        flash("Заявку успішно видалено!", "success")
    else:
        flash("Не вдалося видалити заявку.", "danger")

    return redirect(url_for("admin.admin"))


@vacancy_bp.route("/archieve-request/<int:request_id>", methods=["POST"])
def archieve_request(request_id):
    response = requests.patch(f"{current_app.config['VACANCY_REQUEST_ENDPOINT']}/archieve/{request_id}")
    if response.status_code == 200:
        flash("Заявку успішно архівовано!", "success")
    else:
        flash("Не вдалося архівовувати заявку.", "danger")

    return redirect(url_for("admin.admin"))