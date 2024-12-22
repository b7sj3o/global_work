from flask import Blueprint, abort, flash, render_template, request, redirect, session, url_for, current_app
from flask_babel import _
import requests
from wtforms import FileField, StringField, TextAreaField

from ..utils import save_file


vacancy_bp = Blueprint("vacancy", __name__, url_prefix="/vacancy")

@vacancy_bp.route("/<int:vacancy_id>", methods=["GET", "POST"])
def get_vacancy(vacancy_id):
    if request.method == "POST":
        name = request.form.get("name")
        phone_number = request.form.get("phone_number")
        
        data = {
            "vacancy_id": vacancy_id,
            "name": name,
            "phone_number": phone_number
        }

        # Send data to the backend
        try:
            response = requests.post(f"{current_app.config['VACANCY_REQUEST_ENDPOINT']}/create", json=data)
            if response.status_code == 200:
                flash(_("Ви успішно надіслали заявку!"), "success")
                return redirect(url_for("vacancy.get_vacancy", vacancy_id=vacancy_id))
            elif response.status_code == 400:
                flash(_("Ваша заявка вже подана для цієї вакансії"), "warning")
            else:
                flash(_("Сталася помилка, зверніться в підтримку, якщо вважаєте, що це баг"), "danger")
        except requests.RequestException as e:
            flash(_("Помилка при відправці заявки: ") + str(e), "danger")

    lang = request.cookies.get("language", "uk")

    vacancy = requests.get(f"{current_app.config['VACANCY_ENDPOINT']}/{vacancy_id}").json()

    authorized = session.get("authorized", False)

    return render_template("vacancy.html", vacancy=vacancy, lang=lang, authorized=authorized)



@vacancy_bp.route("/create", methods=["GET", "POST"])
def create_vacancy():
    if not session.get("authorized"):
        abort(403)
        
    if request.method == "POST":
        r = request.form
        data = {
            "title": r.get("title"),
            "title_ru": r.get("title_ru"),
            "description": r.get("description"),
            "description_ru": r.get("description_ru"),
            "salary": r.get("salary"),
            "salary_ru": r.get("salary_ru"),
            "schedule": r.get("schedule"),
            "schedule_ru": r.get("schedule_ru"),
            "accommodation": r.get("accommodation"),
            "accommodation_ru": r.get("accommodation_ru"),
            "work_location": r.get("work_location"),
            "work_location_ru": r.get("work_location_ru"),
            "main_image_path": "",
            "images_path": [],
            "video_path": ""
        }


        # Save main image
        main_image = request.files.get("main_image_path")
        if main_image:
            data["main_image_path"] = save_file(main_image, current_app.config['IMAGES_SAVE'])

        # Save other images
        additional_images = request.files.getlist("images_path")
        filenames = []
        for img in additional_images:
            if img:
                filenames.append(save_file(img, current_app.config['IMAGES_SAVE']))
        data["images_path"] = filenames

        # Save video
        video = request.files.get("video_path")
        if video and video.filename:
            data["video_path"] = save_file(video, current_app.config['VIDEOS_SAVE'])

        # Send data to the backend
        try:
            response = requests.post(f"{current_app.config['VACANCY_ENDPOINT']}/create", json=data)
            response.raise_for_status()
            flash(_("Вакансію створено успішно!"), "success")
            return redirect(url_for("base.home"))
        except requests.RequestException as e:
            flash(_("Помилка при створенні вакансії"), "danger")

    return render_template("vacancy-form.html")


@vacancy_bp.route("/update/<int:vacancy_id>", methods=["GET", "POST"])
def update_vacancy(vacancy_id):
    if not session.get("authorized"):
        abort(403)

    vacacncy = requests.get(f"{current_app.config['VACANCY_ENDPOINT']}/{vacancy_id}").json()

    if request.method == "POST":
        r = request.form
        data = {
            "title": r.get("title"),
            "title_ru": r.get("title_ru"),
            "description": r.get("description"),
            "description_ru": r.get("description_ru"),
            "salary": r.get("salary"),
            "salary_ru": r.get("salary_ru"),
            "schedule": r.get("schedule"),
            "schedule_ru": r.get("schedule_ru"),
            "accommodation": r.get("accommodation"),
            "accommodation_ru": r.get("accommodation_ru"),
            "work_location": r.get("work_location"),
            "work_location_ru": r.get("work_location_ru"),
            "main_image_path": "",
            "images_path": [],
            "video_path": ""
        }


        # Save main image
        main_image = request.files.get("main_image_path")
        if main_image:
            data["main_image_path"] = save_file(main_image, current_app.config['IMAGES_SAVE'])
        else:
            data["main_image_path"] = vacacncy["main_image_path"]

        # Save other images
        additional_images = request.files.getlist("images_path")
        filenames = []
        for img in additional_images:
            if img:
                filenames.append(save_file(img, current_app.config['IMAGES_SAVE']))
        
        data["images_path"] = filenames or vacacncy["images_path"]

        # Save video
        video = request.files.get("video_path")
        if video and video.filename:
            data["video_path"] = save_file(video, current_app.config['VIDEOS_SAVE'])
        else:
            data["video_path"] = vacacncy["video_path"]

        # Send data to the backend
        try:
            response = requests.put(f"{current_app.config['VACANCY_ENDPOINT']}/update/{vacancy_id}", json=data)
            response.raise_for_status()
            flash(_("Вакансію успішно оновлено!"), "success")
            return redirect(url_for("base.home"))
        except requests.RequestException as e:
            print(e)
            flash(_("Помилка при оновленні вакансії"), "danger")

    return render_template("vacancy-form.html", vacancy=vacacncy)


@vacancy_bp.route("/delete/<int:vacancy_id>", methods=["POST"])
def delete_vacancy(vacancy_id):
    if not session.get("authorized"):
        abort(403)

    response = requests.delete(f"{current_app.config['VACANCY_ENDPOINT']}/delete/{vacancy_id}")
    if response.status_code == 204:
        flash(_("Вакансію успішно видалено!"), "success")
    else:
        flash(_("Не вдалося видалити вакансію."), "danger")

    return redirect(url_for("base.home"))


@vacancy_bp.route("/delete-request/<int:request_id>", methods=["POST"])
def delete_request(request_id):
    if not session.get("authorized"):
        abort(403)

    response = requests.delete(f"{current_app.config['VACANCY_REQUEST_ENDPOINT']}/delete/{request_id}")
    if response.status_code == 204:
        flash(_("Заявку успішно видалено!"), "success")
    else:
        flash(_("Не вдалося видалити заявку."), "danger")

    return redirect(url_for("admin.admin"))


# Actually it's not only archieve, but also unarchieve
@vacancy_bp.route("/archieve-request/<int:request_id>", methods=["POST"])
def archieve_request(request_id):
    if not session.get("authorized"):
        abort(403)

    response = requests.patch(f"{current_app.config['VACANCY_REQUEST_ENDPOINT']}/archieve/{request_id}")
    if response.status_code == 200:
        flash(_("Заявку успішно (роз)архівовано!"), "success")
    else:
        flash(_("Не вдалося архівовувати заявку."), "danger")

    return redirect(url_for("admin.admin"))