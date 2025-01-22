class Haus:
    def __init__(self, adresse, preis, farbe):
        self.adresse = adresse  # public: für alle sichtbar
        self._preis = preis  # protected: sollte nur in Unterklassen direkt genutzt werden
        self.__farbe = farbe  # private: kann nur innerhalb der Klasse direkt genutzt werden

    def anzeigen(self):
        """Public Methode: Gibt grundlegende Informationen aus."""
        print(f"Adresse: {self.adresse}, Preis: {self._preis}€")

    def set_farbe(self, farbe):
        """Public Methode: Ändert die Farbe des Hauses."""
        self.__farbe = farbe

    def get_farbe(self):
        """Public Methode: Holt die aktuelle Farbe des Hauses."""
        return self.__farbe

#! ------------------------------------------------------------------------------------

class Blockhaus(Haus):
    def __init__(self, adresse, preis, farbe, holzart):
        super().__init__(adresse, preis, farbe)
        self.holzart = holzart  # public Attribut

    def anzeigen(self):
        """Überschreibt die Methode für die spezifischen Daten des Blockhauses."""
        super().anzeigen()
        print(f"Holzart: {self.holzart}")

#! ------------------------------------------------------------------------------------

class Villa(Haus):
    def __init__(self, adresse, preis, farbe, pool):
        super().__init__(adresse, preis, farbe)
        self.pool = pool  # public Attribut

    def anzeigen(self):
        """Überschreibt die Methode für die spezifischen Daten der Villa."""
        super().anzeigen()
        print(f"Hat einen Pool: {'Ja' if self.pool else 'Nein'}")

#! ------------------------------------------------------------------------------------


# Häuser erstellen
blockhaus = Blockhaus("Waldstraße 10", 250000, "Braun", "Eiche")
villa = Villa("Sonnenweg 5", 750000, "Weiß", True)

# Ausgabe
blockhaus.anzeigen()
print(f"Farbe des Blockhauses: {blockhaus.get_farbe()}")

villa.anzeigen()
print(f"Farbe der Villa: {villa.get_farbe()}")
