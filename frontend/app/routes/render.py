from flask import render_template, redirect, url_for
from .. import app

# Тестовий маршрут
@app.route("/")
def home():
    return render_template("index.html")