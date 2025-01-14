import random
import re
from typing import Any
import string

def pGen(length:int, charset:list[str]):
    '''
    Generiert ein zufälliges Passwort aus dem übergebenen Charset.

    Args:
        #* length (int): Die Länge des generierten Passworts.
        #* charset (list[str]): Eine Liste von Zeichen, aus der das Passwort generiert wird.

    Returns:
        #? str: Das generierte Passwort.
    '''
    password = ''.join(random.choices(population=charset, weights=None, k=length))

    return password



def generate_charset(letters: bool = True, numbers: bool = True, special: bool = True) -> list:
    '''
    Generiert ein Array von Zeichen basierend auf den übergebenen Parametern.

    Args:
        #* letters (bool): Ob Buchstaben (a-z, A-Z) enthalten sein sollen. Standard: True.
        #* numbers (bool): Ob Zahlen (0-9) enthalten sein sollen. Standard: True.
        #* special (bool): Ob Sonderzeichen enthalten sein sollen. Standard: True.

    Returns:
        #? list: Ein Array von Zeichen basierend auf den ausgewählten Kategorien.
    '''

    charset_array = []

    # Buchstaben hinzufügen
    if letters:
        charset_array.extend(string.ascii_lowercase + string.ascii_uppercase)

    # Zahlen hinzufügen
    if numbers:
        charset_array.extend(string.digits)

    # Sonderzeichen hinzufügen
    if special:
        charset_array.extend("!@#$%^&*()_+-=[]{}|;:,.<>?/`~")

    return charset_array

def ausgabe(d:str):
    '''
    Generiert eine Ausgabe von Text nach vorgefertigter Formatierung

    Args:
        #* d (str): Ist der auszugebende Text
    '''
    print(f"Dein generiertes Passwort ist: \"{d}\"")

def errorAusgabe(e:any):
    '''
    Generiert eine Ausgabe von Errors nach vorgefertigter Formatierung

    Args:
        #* e (any): Ist der auszugebende Error
    '''
    print(f"{e}")


def validate(d: Any, type: str) -> bool:
    '''
    Validiert eine Eingabe basierend auf Typ.
    
    Args:
        #* d (Any): Daten die zu prüfende Eingabe.
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


def Main():
    length:str = input("Gebe die Länge deines Passwortes ein:")

    letters:bool = input("Möchtest du Buchstaben benutzen? (y/n): ") == "y"  #! Nicht optimiert
    numbers:bool = input("Möchtest du Zahlen benutzen? (y/n): ") == "y"  #! Nicht optimiert
    special:bool = input("Möchtest du Sonderzeichen benutzen? (y/n): ") == "y"  #! Nicht optimiert  



    try:
        valid_input:bool = validate(str(length), "num")

        if valid_input:
            pw:str = pGen(length=int(length), charset=generate_charset(letters=letters, numbers=numbers, special=special))
            ausgabe(pw)
    except ValueError as e:
        errorAusgabe(e)
    except Exception as e:
        errorAusgabe(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

#! =======================================================

Main()