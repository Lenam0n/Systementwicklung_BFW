from flask import Blueprint, redirect, render_template, request, url_for, session

Weather = Blueprint(
    "weather", __name__, url_prefix="/weather"  # ,template_folder="weather"
)


@Weather.route("/", methods=["GET"])
def weather_form():
    languageCodes = {
        "sq": "Albanian",
        "af": "Afrikaans",
        "ar": "Arabic",
        "az": "Azerbaijani",
        "eu": "Basque",
        "be": "Belarusian",
        "bg": "Bulgarian",
        "ca": "Catalan",
        "zh_cn": "Chinese Simplified",
        "zh_tw": "Chinese Traditional",
        "hr": "Croatian",
        "cz": "Czech",
        "da": "Danish",
        "nl": "Dutch",
        "en": "English",
        "fi": "Finnish",
        "fr": "French",
        "gl": "Galician",
        "el": "Greek",
        "he": "Hebrew",
        "hi": "Hindi",
        "hu": "Hungarian",
        "is": "Icelandic",
        "id": "Indonesian",
        "it": "Italian",
        "ja": "Japanese",
        "kr": "Korean",
        "ku": "Kurmanji (Kurdish)",
        "la": "Latvian",
        "lt": "Lithuanian",
        "mk": "Macedonian",
        "no": "Norwegian",
        "fa": "Persian (Farsi)",
        "pl": "Polish",
        "pt": "Portuguese",
        "pt_br": "Português Brasil",
        "ro": "Romanian",
        "ru": "Russian",
        "sr": "Serbian",
        "sk": "Slovak",
        "sl": "Slovenian",
        "sp": "Spanish (Alternative Abkürzung)",
        "es": "Spanish",
        "sv": "Swedish (Alternative Abkürzung)",
        "se": "Swedish",
        "th": "Thai",
        "tr": "Turkish",
        "ua": "Ukrainian (Alternative Abkürzung)",
        "uk": "Ukrainian",
        "vi": "Vietnamese",
        "zu": "Zulu",
    }

    return render_template("weather_form.html", language=languageCodes)


@Weather.route("/", methods=["POST"])
def submit_weather():
    weather_city = request.form.get("cityname")
    session["units"] = request.form.get("units") or None
    session["lang"] = request.form.get("language") or None
    return redirect(url_for("weather.weather", city=weather_city.lower()))


@Weather.route("/<city>")
def weather(city):
    from utils.api_utils import fetch_weather_data
    from os import environ
    from asyncio import run as runAsync

    units = session.get("units") or "metic"
    lang = session.get("lang") or "de"

    weather_info = runAsync(
        fetch_weather_data(
            city=str(city).capitalize(),
            api_key=environ.get("WEATHER_API_KEY"),
            base_url=environ.get("WEATHER_URL"),
            units=units,
            lang=lang,
        )
    )
    weather_info["units"] = units
    return render_template("weather.html", weather_info=weather_info)
