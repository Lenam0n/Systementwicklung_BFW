import string
import re
import os
import random
from datetime import datetime
#from ..Utils.globalUtils import validate #! muss ich mir nochmal anschauen

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#? >>>           Global Util             >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

'''
#! Custom input Funktion mit eingebauter Validierungsverweisung
def c_input() -> str | int | float:
    #Kommentar
    return
'''

def validate(d: str, type: str) -> bool:
    '''
    Validiert eine Eingabe basierend auf einem bestimmten Typ.

    Args:
        #* d (str): Die zu prüfende Eingabe.
        #* type (str): Der Typ der Validierung (z.B. "num" für Zahlen, "text" für Buchstaben).

    Returns:
        #? bool: True, wenn die Eingabe gültig ist, sonst False.

    Errors:
        #! ValueError: Falls ein ungültiger Typ angegeben wurde.
    '''
    
    regex_patterns = {
        "num": r"\d+",           # Nur Zahlen
        "text": r"[a-zA-Z]+"     # Nur Buchstaben
    }

    if type not in regex_patterns:
        raise ValueError(f"Ungültiger Typ: '{type}' wird nicht unterstützt.") 
    
    valid_input:any = re.fullmatch(regex_patterns[type], str(d)) 

    return bool(valid_input)

def error_ausgabe(e: Exception) -> None:
    '''
    Gibt eine Fehlernachricht formatiert aus.

    Args:
        #* e (Exception): Die auszugebende Exception.

    Returns:
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

def error_ausgabe_wrapper(func:any, e:any, func_menue:any = None) -> None:
    #! Muss ich nochmal schauen ob ich alle funktionen in ein While wrappe und hier immer die Message mitgebe
    '''
    Wrapped die Fehlerausgabe und erweitert sie um zusätzliche Funktionalität (z.B. Menü-Neuladen).

    Args:
        #* func (any): Die Fehlerausgabe-Funktion.
        #* e (any): Der Fehler, der weitergegeben wird.
        #* func_menue (any, optional): Falls mitgegeben, wird nach dem Fehler das Menü erneut aufgerufen.

    Returns:
        #? None: Führt die Fehlerausgabe und ggf. die Menü-Funktion aus.
    '''
    
    func(e) #! muss ich noch auf exsistenz validieren mit None aus dem Parameter
    message_err()
    if(func_menue != None): func_menue()

def validate_y_n_input(prompt: str) -> bool:
    '''
    Validiert eine Ja/Nein-Eingabe (y/n).

    Args:
        #* prompt (str): Die Eingabeaufforderung für den Benutzer.

    Returns:
        #? bool: True, wenn "y" eingegeben wurde, sonst False.

    Errors:
        #! ValueError: Falls eine ungültige Eingabe gemacht wurde.
    '''

    while True:
        response = input(prompt).strip().lower()
        if response in ["y", "n"]:
            return response == "y"
        error_ausgabe(ValueError("Ungültige Eingabe! Bitte nur 'y' oder 'n' verwenden."))



def format_text(text: str, pattern: str) -> str:
    #! schauen wo man es noch nutzen kann
    '''
    Entfernt alle Zeichen aus einem Text, die nicht mit dem angegebenen Regex-Pattern übereinstimmen.

    Args:
        #* text (str): Der zu filternde Text.
        #* pattern (str): Ein Regex-Muster, das die erlaubten Zeichen definiert.

    Returns:
        #? str: Der bereinigte Text, der nur die Zeichen enthält, die mit dem Regex übereinstimmen.
    '''

    return re.sub(pattern, "", text)

def get_time_of_output() -> str:
    '''
    Gibt die aktuelle Uhrzeit und das Datum im Format "YYYY-MM-DD HH:MM:SS" zurück.

    Returns:
        #? str: Der aktuelle Zeitstempel im lesbaren Format.
    '''

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#*  return datetime.now().timestamp() 
#*      => so wäre es für den Unix Zeitstempel


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#? >>>            Aufgaben               >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def list_data() -> None:
    '''
    Listet Dateien und Ordner eines bestimmten Verzeichnisses mit zusätzlichen Informationen auf.

    Returns:
        #? None: Gibt die Dateien mit Details aus.

    Errors:
        #! LookupError: Falls das Verzeichnis nicht existiert oder leer ist.
    '''
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>       Utility Functions           >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def list_data_ausgabe(d:any, spacer:str= "-" * 25) -> None:
        '''
        Gibt die formatierten Datei- und Ordnerinformationen aus.

        Args:
            #* d (any): Dictionary mit den Dateiinformationen.
            #* spacer (str, optional): Zeichen zur Trennung der Einträge. Standard: "-" * 25.

        Returns:
            #? None: Gibt die formatierten Daten aus.
        '''

        print(spacer)
        for key, value in d.items():
            print(f"{key}:")
            for sub_key, sub_value in value.items():
                if sub_key == "Size": print(f"  {sub_key}: {sub_value} byte")
                else: print(f"  {sub_key}: {sub_value}")
            print(spacer) 
        print() # Zeilenumbruch nach dem Spacern / Ausgabe

    def get_ordner(p_path:str, t_sub_dir:list[str]) -> str:
        '''
        Erstellt einen vollständigen Pfad aus einem Basisverzeichnis und einer Liste von Unterordnern.

        Args:
            #* p_path (str): Basisverzeichnis.
            #* t_sub_dir (list[str]): Liste von Unterordnern.

        Returns:
            #? str: Der kombinierte Verzeichnispfad.
        '''

        return os.path.join(p_path, *t_sub_dir) # Alle Strings aus den Unterordner Array werden von 0 bis n aneinander Konkateniert
        
    
    def get_parent_dir_path(current_path: str) -> str:
        '''
        Gibt das übergeordnete Verzeichnis eines gegebenen Pfads zurück.

        Args:
            #* current_path (str): Der aktuelle Pfad.

        Returns:
            #? str: Der übergeordnete Verzeichnispfad.
        '''

        return os.path.dirname(current_path)

    def get_file_path() -> str: 
        '''
        Gibt den absoluten Pfad des aktuellen Skripts zurück.

        Returns:
            #? str: Der vollständige Dateipfad des aktuellen Skripts.
        '''
        
        return os.path.dirname(os.path.abspath(__file__))

    def get_target_file_path(p_path:str, path:str) -> str: 
        '''
        Erstellt einen vollständigen Dateipfad basierend auf einem Basisverzeichnis und einem relativen Pfad.

        Args:
            #* p_path (str): Das Basisverzeichnis.
            #* path (str): Der relative Pfad zur Datei.

        Returns:
            #? str: Der kombinierte absolute Dateipfad.
        '''

        return os.path.join(p_path, path)

    def get_file_extention(fn:str) -> str:
        '''
        Extrahiert die Dateiendung aus einem Dateinamen.

        Args:
            #* fn (str): Der Dateiname.

        Returns:
            #? str: Die Dateiendung (z.B. ".txt"), falls vorhanden, sonst ein leerer String.
        '''

        match:any = re.search(r'\.([^\s.]+)$', fn)
        if match:
            return f".{match.group(1)}"
        return ""

    def list_items(base_path:str, items:list[str]) -> dict:
        '''
        Erstellt ein Dictionary mit Informationen über Dateien und Ordner in einem Verzeichnis.

        Args:
            #* base_path (str): Der Basisverzeichnispfad.
            #* items (list[str]): Liste der Dateinamen.

        Returns:
            #? dict: Ein Dictionary mit Pfad, Größe und Erweiterung jeder Datei.
        '''

        dic:dict[str, dict[str, any]] = {
            item: {
                "Path": get_target_file_path(base_path, item),
                "Size": os.stat(get_target_file_path(base_path, item)).st_size,
                "Extention" : get_file_extention(item).strip()
            }
            for item in items
        }
        return dic


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>           Main Logik              >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    try:
        path:str = get_ordner(  get_parent_dir_path(  get_file_path()  ),["Utils","Mokdata"]  ) 
        #! Die Liste mit Inputs lösen und dann ggf mit cwd arbeiten statt relationaler Filepath
        #? Erweiterbar mit von CWD alle Subordner auflisten die man dann mit einem index auswählen kann 
            #? => dann automatisch übergeben werden im array

        if not os.path.exists(path):
            raise LookupError("Angegebender Ordner gibt es nicht!")
        else:
            items:list[str] = os.listdir(path)
            if not items:
                raise LookupError("Ordner ist Leer!")
            result:dict[str, dict[str, any]] = list_items(path, items)
            list_data_ausgabe(result)
            
    except LookupError as e:
        error_ausgabe(e)

#? ==============================================================================================================


def vocal_counter() -> None:
    '''
    Zählt bestimmte Zeichen (Vokale und Sonderzeichen) in einem eingegebenen Text.

    Returns:
        #? None: Gibt die Zeichenanzahl formatiert aus.

    Errors:
        #! ValueError: Falls eine ungültige oder leere Eingabe gemacht wurde.
    '''
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>         Counter Logik             >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def count_characters(w: str) -> dict[str, int]:
        '''
        Zählt die Häufigkeit bestimmter Zeichen im eingegebenen Text.

        Args:
            #* w (str): Der zu analysierende Text.  

        Returns:
            #? dict[str, int]: Ein Dictionary mit Zeichen als Schlüssel und deren Häufigkeit als Wert.
        '''
        
        #* r bei rf"" ist raw text
        zeichen: str = r"aeiouAEIOU.,!?;:()\-_[]"
        result: str = format_text(w, rf"[^{zeichen}]")

        counter: dict[str, int] = {b: 0 for b in zeichen}

        for char in result:
            if char in counter:
                counter[char] += 1

        return counter 


    def print_character_counts(counter: dict[str, int]) -> None: #! Name ändern
        '''
        Gibt die Häufigkeit der gezählten Zeichen aus.

        Args:
            #* counter (dict[str, int]): Dictionary mit Zeichen und deren Häufigkeit.

        Returns:
            #? None: Gibt die Häufigkeiten formatiert in der Konsole aus.
        '''

        for buchstabe, count in counter.items():
            if count > 0:
                print(f"Zeichen [{buchstabe}] : {count} mal")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>           Main Logik              >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    while True:
        try:
            inp:str = input("Gebe dafür Text ein, um es zählen zu lassen: ").strip()
            if not inp:
                raise ValueError("Eingabe darf nicht leer sein!")
            counter_result: dict[str,int] = count_characters(inp)
            print_character_counts(counter_result)
            break
        except ValueError as e:
            error_ausgabe(str(e)) #! Warum String cast
            

#? ==============================================================================================================

def rechner() -> None:
    '''
    Führt Grundrechenarten (Addition, Subtraktion, Multiplikation, Division) basierend auf Benutzereingaben aus.

    Returns:
        #? None: Gibt das berechnete Ergebnis aus.

    Errors:
        #! ValueError: Falls eine ungültige Rechenart oder eine ungültige Zahl eingegeben wurde.
        #! ZeroDivisionError: Falls eine Division durch 0 erfolgt.
    '''
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>           Varriabeln              >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    #! Eigentlich überflüssig aber fürs Verständis so umgesetzt
    options = {
        "plus": {"symbol": "+"},
        "minus": {"symbol": "-"},
        "mal": {"symbol": "*"},
        "geteilt": {"symbol": "/"}
    }

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>             Utils                 >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def rechner_message() -> None:
        '''
        Gibt eine Übersicht über die verfügbaren Rechenoperationen aus.

        Returns:
            #? None: Gibt die Informationen in der Konsole aus.

        Info:
            -> Nur eine Benutzung und daher eigentlich obsolete 
            -> Aber alles an einem Ort gebündelt an Ausgaben
        '''

        print("Was möchtest du berechnen?")
        print("1. Additives rechnen")
        print("2. Substraktives rechnen")
        print("3. Multiplikatives rechnen")
        print("4. Divisionelles rechnen")
        print("Gebe dafür die gültige Nummer ein (1, 2, 3, 4):")

    def rechner_number_eingabe()-> list[float]:
        '''
        Fragt den Benutzer nach zwei Zahlen für eine Berechnung.

        Returns:
            #? list[float]: Eine Liste mit zwei Zahlen.

        Errors:
            #! ValueError: Falls eine ungültige Zahl eingegeben wurde.
        '''

        try:
            print("Erste Zahl:")
            eingabe_1 = float(input().strip()) 
            print("Zweite Zahl:")
            eingabe_2 = float(input().strip())
            return [eingabe_1, eingabe_2]
        except ValueError:
            raise ValueError("Bitte gültige Zahlen eingeben") #? Eigene Fehlernachicht werfen und nicht die generische des ValueErrors
                

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>     Rechnenlogik Switch Case      >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#! ------------------------------------------------------------------------------------
#? Version ohne Lambda

    def case_plus(a, b) -> str: return f"(Addieren) Ergebnis von {a} {options["plus"]['symbol']} {b} = {a + b}"

    def case_minus(a, b) -> str: return f"(Subtrahieren) Ergebnis von {a} {options["minus"]['symbol']} {b} = {a - b}"

    def case_mal(a, b) -> str: return f"(Multiplizieren) Ergebnis von {a} {options["mal"]['symbol']} {b} = {a * b}"

    def case_geteilt(a, b) -> str:
        if b == 0:
            raise ZeroDivisionError("Division durch 0 nicht erlaubt")
        return f"(Dividieren) Ergebnis von {a} {options['geteilt']['symbol']} {b} = {a / b}"

    switch = {
        "1": case_plus,
        "2": case_minus,
        "3": case_mal,
        "4": case_geteilt
    }

#! ------------------------------------------------------------------------------------
#? Version mit Lambda
    '''# LambdaSwitch
switch = {
    "1": lambda a, b: f"(Addieren) Ergebnis von {a} {options['plus']['symbol']} {b} = {a + b}",
    "2": lambda a, b: f"(Subtrahieren) Ergebnis von {a} {options['minus']['symbol']} {b} = {a - b}",
    "3": lambda a, b: f"(Multiplizieren) Ergebnis von {a} {options['mal']['symbol']} {b} = {a * b}",
    "4": lambda a, b: f"(Dividieren) Ergebnis von {a} {options['geteilt']['symbol']} {b} = {a / b}" if b != 0 else "Error: Division durch 0 nicht erlaubt",
}
    '''
#! ------------------------------------------------------------------------------------

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>           Main Logik              >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    rechner_message()
    rechnenart:str = input().strip()
    try:
        if rechnenart not in switch:
            raise ValueError("Error: Ungültige Rechenart. Bitte eine gültige Nummer (1-4) eingeben.")
        while True: 
            try:
                eingabe: list[float] = rechner_number_eingabe()
                result: str = switch[rechnenart](eingabe[0], eingabe[1])
                print(result)
                break
            except ValueError as e:
                error_ausgabe(e)
                continue
            except ZeroDivisionError as e:
                error_ausgabe(e)
                continue
    except ValueError as e:
        error_ausgabe(e)
        

#? ==============================================================================================================

def passwort_gen() -> None:
    '''
    Generiert ein zufälliges Passwort basierend auf Benutzerpräferenzen.

    Returns:
        #? None: Gibt das generierte Passwort und die Erstellungszeit aus.

    Errors:
        #! ValueError: Falls eine ungültige Passwortlänge eingegeben wurde.
    '''
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>              Utils                >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def p_gen(length:int, charset:list[str]) -> str:
        '''
        Erstellt ein zufälliges Passwort aus einer Zeichenliste.

        Args:
            #* length (int): Die gewünschte Passwortlänge.
            #* charset (list[str]): Die Zeichenliste, aus der das Passwort generiert wird.

        Returns:
            #? str: Das generierte Passwort.
        '''

        return ''.join(random.choices(population=charset, weights=None, k=length))
        #* r.choises gibt eine liste zurück -> mit join auf ein leeren string wird alles aus dem Array konkateniert


    def generate_charset(letters: bool = True, numbers: bool = True, special: bool = True) -> list[str]:
        '''
        Erstellt eine Zeichenliste für die Passwortgenerierung basierend auf Benutzerpräferenzen.

        Args:
            #* letters (bool): Ob Buchstaben enthalten sein sollen.
            #* numbers (bool): Ob Zahlen enthalten sein sollen.
            #* special (bool): Ob Sonderzeichen enthalten sein sollen.

        Returns:
            #? list[str]: Eine Liste mit Zeichen basierend auf den aktivierten Kategorien.
        '''

        charset_array = []

        #* Buchstaben hinzufügen
        if letters: charset_array.extend(string.ascii_letters) # Letters hat lower und upper mit drinne

        #* Zahlen hinzufügen
        if numbers: charset_array.extend(string.digits)

        #* Sonderzeichen hinzufügen
        if special: charset_array.extend("!@#$%^&*()_+-=[]{}|;:,.<>?/`~")

        return charset_array
    
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>           Main Logik              >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def get_valid_input(prompt: str, validation_type: str) -> str:
        '''
        Fragt den Benutzer nach einer Eingabe und validiert diese mit der `validate()`-Funktion.

        Args:
            #* prompt (str): Die Eingabeaufforderung für den Benutzer.
            #* validation_type (str): Der Validierungstyp ("num" für Zahlen, "text" für Buchstaben).

        Returns:
            #? str: Die validierte Eingabe.
        '''

        while True:
            user_input = input(prompt).strip()
            if validate(user_input, validation_type):
                return user_input
            error_ausgabe(ValueError(f"Ungültige Eingabe! Bitte eine gültige {validation_type}-Eingabe machen."))

    prompts = {
        "length": "Gebe die Länge deines Passwortes ein: ",
        "letters": "Möchtest du Buchstaben benutzen? (y/n): ",
        "numbers": "Möchtest du Zahlen benutzen? (y/n): ",
        "special": "Möchtest du Sonderzeichen benutzen? (y/n): "
    }

    selections = {
        key: (int(get_valid_input(prompt, "num")) if key == "length" else validate_y_n_input(prompt))
        for key, prompt in prompts.items()
    }
    # => {'length':int,'letters': bool, 'numbers': bool, 'special': bool}

    length: int = selections["length"]
    letters: bool = selections["letters"]
    numbers: bool = selections["numbers"]
    special: bool = selections["special"]

    try:
        valid_input:bool = validate(length, "num")
        
        if valid_input:
            pw: str = p_gen(length=length, charset=generate_charset(letters=letters, numbers=numbers, special=special))
            print(f"Dein generiertes Passwort ist: \"{pw}\"")
            print(f"Zeit des Erstellens von dem Passwort: {get_time_of_output()}")
    except ValueError as e:
        error_ausgabe(e)
    except Exception as e:
        error_ausgabe(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

#? ==============================================================================================================

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#? >>>      Functions Switch case        >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

functions = {
    "1" : {
            "name": "ListFiles von Ordner",
            "desc" :"Liste deine Files Aus von einem Ordner mit Zusatz Infos auf.",
            "func": list_data
           },
    "2" : {
            "name": "Vokalezähler",
            "desc" :"Zähle die Vokale von einem eingegebenem Wort",
            "func": vocal_counter
           },
    "3" : {
            "name": "Rechner",
            "desc" :"Rechne Plus Minus Mal Geteilt Aufgaben aus",
            "func": rechner
           },
    "4" : {
            "name": "Passwort Generator",
            "desc" :"Erstelle ein Passwort auf Grundlage verschiedener Vorgaben",
            "func": passwort_gen
           },
    "5": {
            "name": "Code Beenden", 
            "func": lambda: (print("Okay Bye"), exit()) #! zu nicht Lambda ändern
        }
}

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#? >>>             Utils                 >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def auswahl() -> None:
    '''
    Zeigt das Hauptmenü an und listet alle verfügbaren Funktionen zur Auswahl.

    Returns:
        #? None: Gibt das Menü in der Konsole aus.
    '''

    anzahl:int = len(functions.keys())
    print("Welche Funktion möchtest du benutzen?")

    for (k,v) in functions.items(): print(f"{k}. {v["name"]}")

    print(f"Gebe dafür eine Zahl zwischen 1 und {anzahl} ein:")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#? >>>           Main Logik              >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def Main() -> None:
    '''
    Hauptmenü der Anwendung. Bietet verschiedene Funktionen zur Auswahl.

    Returns:
        #? None: Führt die gewählte Funktion aus.

    Errors:
        #! ValueError: Falls eine ungültige Auswahl getroffen wurde.
    '''

    while True:
        auswahl()
        inp: str = input().strip()
        try:
            if validate(inp, "num"):
                functions[inp]["func"]()
                while True:
                    try:
                        repeat: bool = validate_y_n_input("Möchtest du noch eine Funktion laufen lassen? (y/n): ")
                        break 
                    except ValueError as e:
                        error_ausgabe(e)
                if not repeat:
                    return
            else:
                raise ValueError(f"Ungültige Auswahl: {inp}. Bitte wähle eine gültige Nummer.")
        except ValueError as e:
            error_ausgabe_wrapper(error_ausgabe, e, auswahl)
        except Exception as e:
            error_ausgabe_wrapper(error_ausgabe, e, auswahl)


#? ==============================================================================================================

if __name__ == "__main__": Main()