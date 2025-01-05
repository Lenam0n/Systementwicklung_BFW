def aufgabe():
    print("Gebe die erste Zahl ein:")
    e1 = input().strip()  
    print("Gebe die zweite Zahl ein:")
    e2 = input().strip()  
    print("Gebe deinen Rechenoperator ein:")
    print("Gültige Zeichen (+ | - | * | /)")
    r = input().strip()  
    
    ergebnis = eval(f"{e1}{r}{e2}")
    print(f"Ergebnis: {ergebnis}")

    '''
    #? mögliches Error Handling
    ausdruck = f"{e1}{r}{e2}"
    try:
        ergebnis = eval(ausdruck)
        print(f"Ergebnis: {ergebnis}")
    except Exception as e:
        print(f"Fehler bei der Berechnung: {e}")

    '''

aufgabe()