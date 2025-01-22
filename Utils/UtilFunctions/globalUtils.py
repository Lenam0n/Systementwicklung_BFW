import re

def validate(d: any, type: str) -> bool:
    '''
    Validiert eine Eingabe basierend auf Typ.
    
    Args:
        #* d (any): Daten die zu prüfende Eingabe.
        #* type (str): Der Typ der Validierung (z.B. "num", "text").
        
    Returns:
        #? bool: True, wenn die Eingabe gültig ist, sonst False.
    '''

    regex_patterns = {
        "num": r"\d+",           # Nur Zahlen
        "text": r"[a-zA-Z]+"     # Nur Buchstaben
    }

    if type not in regex_patterns:
        raise ValueError(f"Ungültiger Typ: '{type}' wird nicht unterstützt.")

    valid_input = re.fullmatch(regex_patterns[type], str(d))

    return bool(valid_input)
