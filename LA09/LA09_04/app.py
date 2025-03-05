from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from os import environ

load_dotenv()

from routes.weather_route import Weather


app = Flask(__name__)
app.secret_key = environ.get("FLASK_SECRET_KEY")
app.register_blueprint(Weather)


@app.route("/")
def home():
    return render_template(
        "index.html",
        Sections=[
            {
                "title": "Aktuelle Daten",
                "description": "Präzise, aktuelle Wetterdaten, aufbereitet für dich.",
            },
            {
                "title": "Benutzerfreundlich",
                "description": "Eine intuitive Oberfläche für schnelle Informationen.",
            },
            {
                "title": "Zuverlässig",
                "description": "Verlasse dich auf verlässliche Vorhersagen und umfangreiche Daten.",
            },
        ],
    )


if __name__ == "__main__":
    app.run(port=int(environ.get("PORT")), host=environ.get("HOST_ADRESSE"), debug=True)
