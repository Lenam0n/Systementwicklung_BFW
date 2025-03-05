from Bahnreise import Bahnreise


def Main() -> None:
    Reise1 = Bahnreise(Reisenr="1000", Zielort="Rom", Reisepreis=750.0)
    print(Reise1.hole_zielort())


if __name__ == "__main__":
    Main()
