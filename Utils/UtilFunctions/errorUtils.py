def error_ausgabe(e: Exception) -> None:
    '''
    Gibt eine Fehlernachricht formatiert aus.

    Params:
    #* e (Exception): Die auszugebende Exception.
    
    Return:
    #? None: Gibt nur eine formatierte Fehlermeldung aus.
    '''
    print(f"Error ({type(e).__name__}): {e}")


def message_err(error_message: str = "Ungültige Eingabe!") -> None:
    '''
    Gibt eine generische oder spezifische Fehlermeldung aus und fordert zur erneuten Eingabe auf.

    Args:
        #* error_message (str, optional): Die spezifische Fehlermeldung. Standard: "Ungültige Eingabe!".

    Returns:
        #? None: Gibt nur eine Fehlermeldung aus.
    '''

    print(f"Error: {error_message}")
    print("Versuche es nochmal:")


def error_ausgabe_wrapper(func:any = None, e:any = None, func_menue:any = None) -> None:
    '''
    Wrapped die Fehlerausgabe und erweitert sie um zusätzliche Funktionalität (z.B. Menü-Neuladen).

    Args:
        #* func (any): Die Fehlerausgabe-Funktion.
        #* e (any): Der Fehler, der weitergegeben wird.
        #* func_menue (any, optional): Falls mitgegeben, wird nach dem Fehler das Menü erneut aufgerufen.

    Returns:
        #? None: Führt die Fehlerausgabe und ggf. die Menü-Funktion aus.
    '''
    
    if not (func == None and e == None): func(e)
    message_err()
    if(func_menue != None): func_menue()

