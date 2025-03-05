from KlassendiagrammÜbung.Zahlungserinnerung import Zahlungserinnerung
from KlassendiagrammÜbung.Fahrzeug import Fahrzeug
from KlassendiagrammÜbung.Rechnung import Rechnung
from KlassendiagrammÜbung.Mietvertrag import Mietvertrag


class Kunde:
    name: str
    nachname: str
    inMiete: list[Fahrzeug] | None
    rechnung: list[Rechnung] | None
    zahlungserinnerung: list[Zahlungserinnerung] | None
    mietvertrag: Mietvertrag | None

    def __init__(
        self,
        name: str,
        nachname: str,
        inMiete: list[Fahrzeug] | None = None,
        rechnung: list[Rechnung] | None = None,
        zahlungserinnerung: list[Zahlungserinnerung] | None = None,
        mietvertrag: Mietvertrag | None = None,
    ):
        self.name = name
        self.nachname = nachname
        self.inMiete = inMiete
        self.rechnung = rechnung
        self.zahlungserinnerung = zahlungserinnerung
        self.mietvertrag = mietvertrag

    def bezahlen(self) -> bool:
        return True

    def mieten(self, fahrzeug: Fahrzeug | None) -> Fahrzeug | None:
        return Fahrzeug

    def einsehen(
        self,
        rechnung: list[Rechnung] | None = None,
        zahhlungserinnerung: list[Zahlungserinnerung] | None = None,
        mietvertrag: list[Mietvertrag] | None = None,
    ) -> None | list[Zahlungserinnerung] | list[Mietvertrag] | list[Rechnung]:
        if rechnung and zahhlungserinnerung and mietvertrag == None:
            return None
        if rechnung:
            return self.rechnung
        if zahhlungserinnerung:
            return self.zahlungserinnerung
        if mietvertrag:
            return self.mietvertrag
        raise ValueError("Falsche mitgaben")
