from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    FileField,
    SubmitField,
    TelField,
    BooleanField,
)
from wtforms.validators import DataRequired, Length, Regexp


class VacancyForm(FlaskForm):
    title = StringField(
        "Назва вакансії (UA)",
        validators=[DataRequired(), Length(max=255)],
        render_kw={"placeholder": "Напишіть назву вакансії українською"},
    )
    title_ru = StringField(
        "Назва вакансії (RU)",
        validators=[DataRequired(), Length(max=255)],
        render_kw={"placeholder": "Напишіть назву вакансії російською"},
    )
    main_image_path = FileField(
        "Головне зображення",
        validators=[DataRequired()],
        render_kw={"placeholder": "Завантажити зображення"},
    )
    images_path = FileField("Додаткові фото", render_kw={"multiple": True})
    video_path = FileField("Відео", render_kw={"placeholder": "Завантажити відео"})

    salary = StringField(
        "Зарплата (UA)",
        validators=[DataRequired()],
        render_kw={"placeholder": "Введіть зарплату українською"},
    )
    salary_ru = StringField(
        "Зарплата (RU)",
        validators=[DataRequired()],
        render_kw={"placeholder": "Введіть зарплату російською"},
    )
    schedule = StringField(
        "Графік (UA)",
        validators=[DataRequired()],
        render_kw={"placeholder": "Введіть графік роботи українською"},
    )
    schedule_ru = StringField(
        "Графік (RU)",
        validators=[DataRequired()],
        render_kw={"placeholder": "Введіть графік роботи російською"},
    )
    accommodation = StringField(
        "Проживання (UA)",
        validators=[DataRequired()],
        render_kw={"placeholder": "Умови проживання українською"},
    )
    accommodation_ru = StringField(
        "Проживання (RU)",
        validators=[DataRequired()],
        render_kw={"placeholder": "Умови проживання російською"},
    )
    work_location = StringField(
        "Місце роботи (UA)",
        validators=[DataRequired()],
        render_kw={"placeholder": "Вкажіть місце роботи українською"},
    )
    work_location_ru = StringField(
        "Місце роботи (RU)",
        validators=[DataRequired()],
        render_kw={"placeholder": "Вкажіть місце роботи російською"},
    )

    description = TextAreaField(
        "Детальний опис (UA)",
        validators=[DataRequired()],
        render_kw={"placeholder": "Введіть детальний опис вакансії українською"},
    )
    description_ru = TextAreaField(
        "Детальний опис (RU)",
        validators=[DataRequired()],
        render_kw={"placeholder": "Введіть детальний опис вакансії російською"},
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
        validators=[DataRequired()],
        render_kw={"placeholder": "+380 (XX) XXX-XX-XX"},
    )

    submit = SubmitField("Відправити")


class LoginForm(FlaskForm):
    username = StringField(
        "Ваш нікнейм",
        validators=[DataRequired(), Length(max=255)],
        render_kw={"placeholder": "Нікнейм"},
    )
    password = TelField(
        "Ваш пароль",
        validators=[DataRequired()],
        render_kw={"placeholder": "Пароль"},
    )
    remember_me = BooleanField("Запам'ятати мене")

    submit = SubmitField("Відправити")
