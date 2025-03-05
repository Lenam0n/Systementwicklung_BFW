from KlassendiagrammÜbung.Kunde import Kunde


class Fahrzeug:
    marke: str
    mieter: Kunde | None
    zustand: str

    def __init__(self, marke: str, zustand: str, mieter: Kunde | None = None):
        self.marke = marke
        self.mieter = mieter
        self.zustand = zustand
