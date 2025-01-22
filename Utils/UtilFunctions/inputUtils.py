from .errorUtils import error_ausgabe

def user_choice(
    prompt: str,
    choices: dict[str, any],
    error_message: str = "Ungültige Eingabe! Bitte wählen Sie eine gültige Option.",
    max_attempts: int = None,
    return_type: type = str
) -> any:
    ''' 
    Fragt den Benutzer nach einer Auswahl und gibt die gewählte Aktion zurück.
    Falls die Eingabe ungültig ist, wird eine Exception geworfen und mit `error_ausgabe()` ausgegeben.

    Params:
    #* prompt: str → Die Eingabeaufforderung.
    #* choices: dict → Mapping von Eingaben zu Aktionen (z. B. {"j": True, "n": False}).
    #* error_message: str → Fehlermeldung für ungültige Eingaben.
    #* max_attempts: int → Maximale Anzahl an Eingabeversuchen (None = unendlich).
    #* return_type: Type → Gibt den Rückgabewert in einem bestimmten Typ zurück (str, int, bool etc.).

    Return:
    #? any → Die gewählte Aktion (in `return_type` konvertiert).
    '''

    attempts = 0
    while max_attempts is None or attempts < max_attempts:
        try:
            choice = input(prompt).strip().lower()
            if choice not in choices:
                raise ValueError(error_message)
            return return_type(choices[choice]) 
        except ValueError as e:
            error_ausgabe(e)
            attempts += 1

    raise ValueError(f"Maximale Anzahl von {max_attempts} Fehlversuchen erreicht.")