class Bahnreise:
    _reisenummer: str
    _zielort: str
    _reisepreis: float

    def __init__(self, Reisenr: str = "", Zielort: str = "", Reisepreis: float = 0.0):
        self._reisenummer = Reisenr
        self._zielort = Zielort
        self._reisepreis = Reisepreis

    def hole_zielort(self) -> str:
        return self._zielort

    def setze_zielort(self, Zielort: str) -> None:
        self._zielort = Zielort

    def hole_reisenummer(self) -> str:
        return self._reisenummer

    def setze_reisenummer(self, Reisenr: str) -> None:
        self._reisenummer = Reisenr

    def hole_reisepreis(self) -> str:
        return self._reisepreis

    def setze_reisepreis(self, Reisepreis: float) -> None:
        self._reisepreis = Reisepreis