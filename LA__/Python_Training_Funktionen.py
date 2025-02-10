# Diese Funktion begrüßt den Nutzer mit "Hallo <Nutzername>", basierend auf dem übergebenen Namen.
def begruessung_nutzer(name) -> None:
    print(f"Hallo {name} ^^")


# Diese Funktion addiert zwei Zahlen und gibt das Ergebnis zurück.
def zwei_zahlen_addieren(a, b) -> int:
    return a + b


# Diese Funktion kehrt die Reihenfolge der Elemente in einer Liste um und gibt sie zurück.
def liste_umkehren(liste: list[any]) -> list[any]:
    return liste.reverse()


# Diese Funktion findet das längste Wort in einer Liste von Wörtern.
def laengstes_wort_finden(wörter):
    wort = ""
    for e in wörter:
        if len(e) > len(wort):
            wort = e
    return wort


# Diese Funktion generiert eine zufällige Zahl im angegebenen Bereich.
def zufaellige_zahl_generieren(min, max) -> int:
    return range(min, max)


# Diese Funktion gibt die aktuelle Uhrzeit im Format "HH:MM:SS" aus.
def aktuelle_uhrzeit_ausgeben() -> None:
    from datetime import datetime

    print(datetime.now())


# Diese Funktion generiert ein zufälliges Passwort mit der angegebenen Länge.
def passwort_generieren(länge):
    from random import choices
    import string

    return "".join(choices(population=(string.ascii_letters + string.digits), k=länge))


# Diese Funktion berechnet die Anzahl der Tage bis zu einem bestimmten zukünftigen Datum.
def tage_bis_zukuenftiges_datum(datum):
    from datetime import datetime

    return datum - datetime.today()


# Diese Funktion findet die gemeinsamen Elemente zwischen zwei Listen und gibt diese zurück.
def gemeinsame_elemente_finden(liste1, liste2) -> list[any, any]:
    for e1 in liste1:
        for e2 in liste2:
            if e1 == e2:
                return e1, e2


# Diese Funktion prüft, ob ein Wort ein Palindrom ist (d.h., vorwärts und rückwärts gleich).
def palindrom_pruefen(wort):
    if str(wort) == str(wort)[::-1]:
        print(f'"{wort}" ist ein Palindrome')
        return wort
    else:
        print(f'"{wort}" ist kein Palindrome')
