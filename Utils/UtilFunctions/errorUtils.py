def error_ausgabe(e: Exception) -> None:
    '''
    Gibt eine Fehlernachricht formatiert aus.

    Params:
    #* e (Exception): Die auszugebende Exception.
    
    Return:
    #? None: Gibt nur eine formatierte Fehlermeldung aus.
    '''
    print(f"Error ({type(e).__name__}): {e}")