from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField, TelField
from wtforms.validators import DataRequired, Length, Regexp


class VacancyForm(FlaskForm):
    title = StringField(
        "Назва вакансії",
        validators=[DataRequired(), Length(max=255)],
        render_kw={"placeholder": "Напишіть назву вакансії"},
    )
    main_image_path = FileField(
        "Головне зображення",
        validators=[DataRequired()],
        render_kw={"placeholder": "Завантажити зображення"},
    )
    images_path = FileField("Додаткові фото", render_kw={"multiple": True})
    video_path = FileField("Відео", render_kw={"placeholder": "Завантажити відео"})
    short_description = TextAreaField(
        "Короткий опис",
        validators=[DataRequired()],
        render_kw={"placeholder": "Введіть короткий опис вакансії"},
    )
    description = TextAreaField(
        "Детальний опис",
        validators=[DataRequired()],
        render_kw={"placeholder": "Введіть детальний опис вакансії"},
    )

    submit = SubmitField("Створити вакансію")


class VacancyRequestForm(FlaskForm):
    name = StringField(
        "Ваше ім'я",
        validators=[DataRequired(), Length(max=255)],
        render_kw={"placeholder": "Ім'я"},
    )
    phone_number = TelField(
        "Ваш телефон",
        validators=[
            DataRequired(),
            Regexp(r"^\+380\d{9}$", message="Телефон має бути у форматі +380XXXXXXXXX"),
        ],
        render_kw={"placeholder": "+380 (XX) XXX-XX-XX"},
    )

    submit = SubmitField("Відправити")
