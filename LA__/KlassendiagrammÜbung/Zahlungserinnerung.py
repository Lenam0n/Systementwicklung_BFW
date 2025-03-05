from KlassendiagrammÜbung.Kunde import Kunde
from KlassendiagrammÜbung.Fahrzeug import Fahrzeug
from KlassendiagrammÜbung.Rechnung import Rechnung


class Zahlungserinnerung:
    kunde: Kunde
    erste: bool
    offeneKosten: float
    bezogeneRechnung: Rechnung

    def __init__(
        self, kunde: Kunde, erste: bool, offeneKosten: float, bezogeneRechnung: Rechnung
    ):
        self.kunde = kunde
        self.erste = erste
        self.offeneKosten = offeneKosten
        self.bezogeneRechnung = bezogeneRechnung
