from KlassendiagrammÜbung.Kunde import Kunde
from KlassendiagrammÜbung.Fahrzeug import Fahrzeug


class Mietvertrag:
    kunde: Kunde
    laufzeit: int
    kosten: float
    fahrzeug: Fahrzeug

    def __init__(self, kunde: Kunde, laufzeit: int, kosten: float, fahrzeug: Fahrzeug):
        self.kunde = kunde
        self.laufzeit = laufzeit
        self.kosten = kosten
        self.fahrzeug = fahrzeug
