from KlassendiagrammÜbung.Kunde import Kunde
from KlassendiagrammÜbung.Fahrzeug import Fahrzeug

class Rechnung:
    kunde: Kunde
    interval: int
    kosten: float
    fahrzeug: Fahrzeug
    status: str

    def __init__(
        self,
        kunde: Kunde,
        interval: int,
        kosten: float,
        fahrzeug: Fahrzeug,
        status: str,
    ):
        self.kunde = kunde
        self.interval = interval
        self.kosten = kosten
        self.fahrzeug = fahrzeug
        self.status = status
