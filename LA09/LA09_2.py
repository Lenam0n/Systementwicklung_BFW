async def fetch_data(url: str) -> any:  #! anpassen auf richtigen datentyp
    import aiohttp

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


def get_current_location() -> list[float]:
    import geocoder

    location = geocoder.ip("me")
    return location.lat, location.lng


def get_location_from_name(city: str = "Düsseldorf") -> list[float]:
    from geopy.geocoders import Nominatim

    location = Nominatim(user_agent="dein_user_agent").geocode(
        city, exactly_one=True, timeout=10
    )
    return location.latitude, location.longitude


from weather_types import WeatherUnit, LanguageCodes


def build_url(
    url: str,
    api_key: str,
    lat: float = 44.34,
    lon: float = 10.99,
    units: WeatherUnit = "standard",
    lang: LanguageCodes = "de",
) -> str:
    return f"{url}?lat={lat}&lon={lon}&lang={lang}&units={units}&appid={api_key}"


def use_data(data: any) -> dict[str, any] | None:
    if not data:
        return None
    return {
        "temp": data["main"]["temp"],
        "weather": [{"description": item["description"]} for item in data["weather"]],
        "wind": {"speed": data["wind"]["speed"], "direction": data["wind"]["deg"]},
    }


def ausgabe(data: dict[str, any] | None) -> None:
    if not data:
        print("Keine Daten zum ausgeben!")
        return
    print(f"Temperatur wird {data["temp"]}°")
    print(
        f"Das Wetter wird {' & '.join(w['description'] for w in data['weather'] if len(data['weather']) > 1)}"
    )

    print(
        f"Die Windgeschwindigkeit wird mit {data["wind"]["speed"]}km/h aus der Richtung {data['wind']["direction"]}° kommen."
    )


async def main():
    from dotenv import load_dotenv
    import os
    from Utils.UtilFunctions.inputUtils import user_choice

    load_dotenv()
    api_key: str = os.environ.get("WEATHER_API_KEY")
    base_url: str = os.environ.get("WEATHER_URL")
    inp: str = user_choice(
        prompt="Möchtest du einen Ort angeben oder von deinem aktuellen Ort das Wetter wissen?\n1 Einen bestimmter Ort\n2 Aktueller Ort\n3 Abbrechen\n",
        choices=["1", "2", "3"],
        return_type=int,
    )
    if inp == 3:
        return
    if inp == 2:
        print("\n\n\nLoading...")
    lat, lon = (
        get_current_location()
        if inp == 2
        else get_location_from_name(
            user_choice(
                prompt="Gebe den Namen einer Stadt ein: ",
                allow_all=True,
                choices="",
            ),
        )
    )
    if not (lat or lon):
        print("Wetter konnte nicht gefunden werden!")
        return
    data = await fetch_data(
        build_url(url=base_url, api_key=api_key, lat=lat, lon=lon, units="metric")
    )
    ausgabe(use_data(data))


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
