def validate(d: any, type: str) -> bool:
    '''
    Validiert eine Eingabe basierend auf Typ.
    
    Args:
        #* d (any): Daten die zu prüfende Eingabe.
        #* type (str): Der Typ der Validierung (z.B. "num", "text").
        
    Returns:
        #? bool: True, wenn die Eingabe gültig ist, sonst False.
    '''
    from re import fullmatch

    regex_patterns = {
        "num": r"\d+",           # Nur Zahlen
        "text": r"[a-zA-Z]+"     # Nur Buchstaben
    }

    if type not in regex_patterns: raise ValueError(f"Ungültiger Typ: '{type}' wird nicht unterstützt.")

    valid_input = fullmatch(regex_patterns[type], str(d))

    if not valid_input: raise ValueError("Ungültige Eingabe")

    return bool(valid_input)

def format_text(text: str, pattern: str) -> str:
    '''
    Entfernt alle Zeichen aus einem Text, die nicht mit dem angegebenen Regex-Pattern übereinstimmen.

    Args:
        #* text (str): Der zu filternde Text.
        #* pattern (str): Ein Regex-Muster, das die erlaubten Zeichen definiert.

    Returns:
        #? str: Der bereinigte Text, der nur die Zeichen enthält, die mit dem Regex übereinstimmen.
    '''
    from re import sub

    return sub(pattern, "", text)

def get_time_of_output(format:str = "normal") -> str:
    '''
    Gibt die aktuelle Uhrzeit und das Datum im Format "YYYY-MM-DD HH:MM:SS" zurück.

    Returns:
        #? str: Der aktuelle Zeitstempel im lesbaren Format.
    '''
    from datetime import datetime
    match format:
        case "normal": return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        case "unix": return datetime.now().timestamp() 
        case _: raise TypeError("Unbekanntes Zeitformat!")