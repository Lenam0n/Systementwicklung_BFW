# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>        Globale Varriabeln         >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#* Rechnen Options Dictionary
options = {
    "plus": {"symbol": "+"},
    "minus": {"symbol": "-"},
    "mal": {"symbol": "*"},
    "geteilt": {"symbol": "/"}
}

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>          Messages Logik           >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def massage():
    print("Was möchtest du berechnen?")
    print("1. Additives rechnen")
    print("2. Substraktives rechnen")
    print("3. Multiplikatives rechnen")
    print("4. Divisionelles rechnen")
    print("Gebe dafür die gültige Nummer ein (1, 2, 3, 4):")

def massage2():
    while True:
        try:
            eingabe = input("Möchtest du noch etwas berechnen? (y / n) ").strip().lower()
            if eingabe not in ["y", "n"]:
                raise ValueError("Error: Gebe eine gültige Eingabe ein")
            print("\n\n\n\n\n\n\n") if eingabe == "y" else print("Okay Bye ^^")
            return eingabe == "y"
        except ValueError as e:
            errorMessage(e)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>             Utils                 >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def errorMessage(e):
    print(f"\n\n{e}\n\n")

def Eingabe():
    while True:
        try:
            eingabe_1 = float(input("Erste Zahl: ").strip())
            eingabe_2 = float(input("Zweite Zahl: ").strip())
            return [eingabe_1, eingabe_2]
        except ValueError:
            errorMessage("Error: Bitte gültige Zahlen eingeben")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>     Rechnenlogik Switch Case      >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def rechner_logik(state, a, b, op):
    return f"({state}) Ergebnis von {a} {op} {b} = {op(a, b)}"

def case_plus(a, b):
    return rechner_logik("Addieren", a, b, lambda a, b: a + b)

def case_minus(a, b):
    return rechner_logik("Subtrahieren", a, b, lambda a, b: a - b)

def case_mal(a, b):
    return rechner_logik("Multiplizieren", a, b, lambda a, b: a * b)

def case_geteilt(a, b):
    if b == 0:
        return "Error: Division durch 0 nicht erlaubt"
    return rechner_logik("Dividieren", a, b, lambda a, b: a / b)

def default_case():
    raise ValueError("Error: Ungültige Eingabe für die Rechenart")

#* Switch Case Dictionary
switch = {
    "1": case_plus,
    "2": case_minus,
    "3": case_mal,
    "4": case_geteilt
}

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>           Main Logik              >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def Main():
    while True:
        massage()
        rechnenart = input().strip()
        try:
            if rechnenart not in switch:
                raise ValueError("Error: Ungültige Rechenart. Bitte eine gültige Nummer (1-4) eingeben.")
            eingabe = Eingabe()
            print(switch[rechnenart](*eingabe))
            if not massage2():
                break
        except ValueError as e:
            errorMessage(e)

Main()