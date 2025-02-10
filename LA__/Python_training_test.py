def test_begruessung_nutzer():
    from Python_Training_Funktionen import begruessung_nutzer

    print("Teste: begruessung_nutzer")
    begruessung_nutzer(input("Gebe einen Namen ein: "))
    print()


def test_zwei_zahlen_addieren():
    from Python_Training_Funktionen import zwei_zahlen_addieren

    print("Teste: zwei_zahlen_addieren")
    print(zwei_zahlen_addieren(5, 7))
    print()


def test_liste_umkehren():
    from Python_Training_Funktionen import liste_umkehren

    print("Teste: liste_umkehren")
    test_liste = [1, 2, 3, 4]
    liste_umkehren(test_liste)
    print(test_liste)
    print()


def test_laengstes_wort_finden():
    from Python_Training_Funktionen import laengstes_wort_finden

    print("Teste: laengstes_wort_finden")
    print(laengstes_wort_finden(["Katze", "Elefant", "Hund"]))
    print()


def test_zufaellige_zahl_generieren():
    from Python_Training_Funktionen import zufaellige_zahl_generieren

    print("Teste: zufaellige_zahl_generieren")
    print(zufaellige_zahl_generieren(1, 10))
    print()


def test_aktuelle_uhrzeit_ausgeben():
    from Python_Training_Funktionen import aktuelle_uhrzeit_ausgeben

    print("Teste: aktuelle_uhrzeit_ausgeben")
    aktuelle_uhrzeit_ausgeben()
    print()


def test_passwort_generieren():
    from Python_Training_Funktionen import passwort_generieren

    print("Teste: passwort_generieren")
    print(passwort_generieren(10))
    print()


def test_tage_bis_zukuenftiges_datum():
    from Python_Training_Funktionen import tage_bis_zukuenftiges_datum
    from datetime import datetime

    print("Teste: tage_bis_zukuenftiges_datum")
    zieldatum = datetime(2025, 12, 31)
    print(tage_bis_zukuenftiges_datum(zieldatum))
    print()


def test_gemeinsame_elemente_finden():
    from Python_Training_Funktionen import gemeinsame_elemente_finden

    print("Teste: gemeinsame_elemente_finden")
    print(gemeinsame_elemente_finden([1, 2, 3], [2, 3, 4]))
    print()


def test_palindrom_pruefen():
    from Python_Training_Funktionen import palindrom_pruefen

    print("Teste: palindrom_pruefen")
    palindrom_pruefen("radar")
    palindrom_pruefen("python")
    print()


if __name__ == "__main__":
    test_begruessung_nutzer()
    test_zwei_zahlen_addieren()
    test_liste_umkehren()
    test_laengstes_wort_finden()
    test_zufaellige_zahl_generieren()
    test_aktuelle_uhrzeit_ausgeben()
    test_passwort_generieren()
    test_tage_bis_zukuenftiges_datum()
    test_gemeinsame_elemente_finden()
    test_palindrom_pruefen()
