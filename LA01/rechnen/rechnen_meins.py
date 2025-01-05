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
            print("Möchtest du noch etwas berechnen? (y / n)") 
            eingabe = input().strip().lower()

            if eingabe not in ["y", "n"]:
                raise ValueError("Error: Gebe eine gültige Eingabe ein")
            
            print("\n\n\n\n\n\n\n") if eingabe == "y" else print("Okay Bye ^^")
            return True if eingabe == "y" else False
        except ValueError as e:
            errorMessage(e)
            continue


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>             Utils                 >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def errorMessage(e):
    print(f"\n\n{e}\n\n")

def Eingabe():
    try:
        print("Erste Zahl:")
        eingabe_1 = float(input().strip()) 
        print("Zweite Zahl:")
        eingabe_2 = float(input().strip())
        return [eingabe_1, eingabe_2]
    except ValueError:
        raise ValueError("Error: Bitte gültige Zahlen eingeben")
            

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>     Rechnenlogik Switch Case      >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def case_plus(a, b):
    state = "plus"
    return f" (Addieren) Ergebnis von {a} {options[state]['symbol']} {b} = {a + b}"

def case_minus(a, b):
    state = "minus"
    return f"(Subtrahieren) Ergebnis von {a} {options[state]['symbol']} {b} = {a - b}"

def case_mal(a, b):
    state = "mal"
    return f"(Multiplizieren) Ergebnis von {a} {options[state]['symbol']} {b} = {a * b}"

def case_geteilt(a, b):
    state = "geteilt"
    if b == 0:
        return "Error: Division durch 0 nicht erlaubt"
    return f"(Dividieren) Ergebnis von {a} {options[state]['symbol']} {b} = {a / b}"

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
            while True: 
                try:
                    eingabe = Eingabe()
                    result = switch[rechnenart](eingabe[0], eingabe[1])
                    print(result)
                    break
                except ValueError as e:
                    errorMessage(e)
                    continue
            result2 = massage2()
            if result2 == False:
                break
        
        except ValueError as e:
            errorMessage(e)
            continue

Main()