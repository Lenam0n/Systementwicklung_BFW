from .errorUtils import error_ausgabe

def user_choice(
    prompt: str,
    choices: list | str,  # Erlaube hier auch einen String als speziellen Marker.
    allow_all: bool = False,
    error_message: str = "Ungültige Eingabe! Bitte wählen Sie eine gültige Option.",
    max_attempts: int = None,
    return_type: type = str
) -> any:
    ''' 
    Fragt den Benutzer nach einer Auswahl und gibt die gewählte Aktion zurück.
    Falls die Eingabe ungültig ist, wird eine Exception geworfen und mit `error_ausgabe()` ausgegeben.

    Besonderheit:
    - Wenn `choices` den speziellen Wert "num" erhält, wird anstelle einer
      Überprüfung gegen eine Liste versucht, die Eingabe direkt in `return_type`
      zu konvertieren. Damit sind alle numerischen Eingaben (die sich konvertieren
      lassen) erlaubt.

    Params:
    #* prompt: str → Die Eingabeaufforderung.
    #* choices: list oder str → Liste der zulässigen Eingaben oder der spezielle
       Marker "num", der alle numerischen Eingaben erlaubt.
    #* error_message: str → Fehlermeldung für ungültige Eingaben.
    #* max_attempts: int → Maximale Anzahl an Eingabeversuchen (None = unendlich).
    #* return_type: type → Der gewünschte Rückgabetyp (z. B. str, int, bool).

    Return:
    #? any → Die vom Benutzer eingegebene Aktion, in `return_type` konvertiert.
    '''
    attempts = 0
    while max_attempts is None or attempts < max_attempts:
        try:
            choice = input(prompt).strip().lower()
            if choices == "num":
                try:
                    return return_type(choice)
                except ValueError:
                    raise ValueError(error_message)
            if allow_all:
                return return_type(choice)
            if choice not in choices:
                raise ValueError(error_message)
            return return_type(choice)
        except ValueError as e:
            error_ausgabe(e)
            attempts += 1

    raise ValueError(f"Maximale Anzahl von {max_attempts} Fehlversuchen erreicht.")
