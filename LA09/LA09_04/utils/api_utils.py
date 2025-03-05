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


from Types.weather_types import WeatherUnit, LanguageCodes


def build_url(
    url: str,
    api_key: str,
    lat: float = 44.34,
    lon: float = 10.99,
    units: WeatherUnit = "standard",
    lang: LanguageCodes = "de",
) -> str:
    return f"{url}?lat={lat}&lon={lon}&lang={lang}&units={units}&appid={api_key}"


async def fetch_weather_data(
    city: str | None, units: WeatherUnit, base_url: str, api_key: str, lang: str
):
    lat, lon = get_current_location() if not city else get_location_from_name(city=city)
    if not (lat or lon):
        raise SystemError("Wetter konnte nicht gefunden werden!")
    return await fetch_data(
        build_url(
            url=base_url, api_key=api_key, lat=lat, lon=lon, units=units, lang=lang
        )
    )
