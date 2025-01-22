from abc import ABC, abstractmethod

class Haus(ABC):
    def __init__(self, adresse, preis, farbe):
        self.adresse = adresse
        self._preis = preis
        self.__farbe = farbe

    @abstractmethod
    def anzeigen(self):
        """Abstrakte Methode, die in den Unterklassen implementiert werden muss."""
        pass

    def set_farbe(self, farbe):
        self.__farbe = farbe

    def get_farbe(self):
        return self.__farbe

#! ------------------------------------------------------------------------------------

class Blockhaus(Haus):
    def __init__(self, adresse, preis, farbe, holzart):
        super().__init__(adresse, preis, farbe)
        self.holzart = holzart

    def anzeigen(self):
        print(f"Blockhaus - Adresse: {self.adresse}, Preis: {self._preis}€, Holzart: {self.holzart}")

#! ------------------------------------------------------------------------------------

class Villa(Haus):
    def __init__(self, adresse, preis, farbe, pool):
        super().__init__(adresse, preis, farbe)
        self.pool = pool

    def anzeigen(self):
        print(f"Villa - Adresse: {self.adresse}, Preis: {self._preis}€, Pool: {'Ja' if self.pool else 'Nein'}")

#! ------------------------------------------------------------------------------------

# Häuser erstellen
blockhaus = Blockhaus("Waldstraße 10", 250000, "Braun", "Eiche")
villa = Villa("Sonnenweg 5", 750000, "Weiß", True)

# Ausgabe
blockhaus.anzeigen()
print(f"Farbe des Blockhauses: {blockhaus.get_farbe()}")

villa.anzeigen()
print(f"Farbe der Villa: {villa.get_farbe()}")
