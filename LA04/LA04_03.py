import re 
'''
#? from re import fullmatch 
#!bessere Import variante weil nur fullmatch von re genutzt wird
'''
import os
import random
import string
#from ..Utils.globalUtils import validate #! muss ich mir nochmal anschauen

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#? >>>           Global Util             >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def validate(d: str, type: str) -> bool:
    '''
    Validiert eine Eingabe basierend auf Typ.
    
    Args:
        #* d (str): Daten die zu prüfende Eingabe.
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
        #? -> KeyError ist besser zu beschreiben
    
    valid_input:any = re.fullmatch(regex_patterns[type], str(d)) #! str(d) muss gecasted werden. Keine Ahnung warum. Muss ich nachschauen!

    return bool(valid_input)

def error_Ausgabe(e:any):
    '''
    Generiert eine Ausgabe von Errors nach vorgefertigter Formatierung

    Args:
        #* e (any): Ist der auszugebende Error
    '''
    print(f"{e}") #? Formatierung sollte noch implementiert werden

def ausgabe(t:str):
    print(f"{t}") #? Formatierung sollte noch implementiert werden

def message_err():
    ''' Ausgabe das eine fehlerhafte Eingabe gemacht wurde und erneute Eingabe abgefragt wird'''

    print("Ungültige Eingabe!") 
    print("Versuche es nochmal:")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#? >>>            Aufgaben               >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def listData():
    '''
    
    '''
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>       Utility Functions           >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def list_data_ausgabe(d:any, spacer:str="------------------------"):
        #! anzahl an Spacer Länge über Schleife oder so machen und nur ein Zeichen mitgeben
        print(spacer)
        for key, value in d.items():
            print(f"{key}:")
            for sub_key, sub_value in value.items(): #! Ausgabe sagt nur die Zahl und nicht byte => If bedingung für Size hinzufügen und print ändern
                print(f"  {sub_key}: {sub_value}")
            print(spacer) 
        print() # Zeilenumbruch nach dem Spacern / Ausgabe

    def get_ordner(p_path:str, t_sub_dir:list[str]) -> str:
        '''
        Gibt den vollständigen Pfad zu einem Zielordner zurück, wobei mehrere Unterordner dynamisch kombiniert werden.

        Args:
            #* p_path (str): Der Perent Ordner Pfad, von dem aus navigiert wird.
            #* t_sub_dirs (list[str]): Eine Liste von Unterordnern, die kombiniert werden sollen.

        Returns:
            #? str: Der vollständige Pfad zum Zielordner.
        '''

        return os.path.join(p_path, *t_sub_dir) # Alle Strings aus den Unterordner Array werden von 0 bis N aneinander Konkateniert
        
    
    def get_parent_dir_path(current_path: str) -> str:
        '''
        Gibt den übergeordneten Ordner des aktuellen Pfades zurück.

        Args:
            #* current_path (str): Der aktuelle Pfad.

        Returns:
            #? str: Der übergeordnete Pfad.
        '''
        return os.path.dirname(current_path)

    def get_file_path() -> str: return os.path.dirname(os.path.abspath(__file__))

    def get_target_file_path(p_path:str, path:str) -> str: return os.path.join(p_path, path)

    def get_file_extention(fn:str)-> str:
        match:any = re.search(r'\.([^\s.]+)$', fn)
        if match:
            return f".{match.group(1)}"
        return ""

    def list_items(base_path:str, items:list[str]) -> dict:
        dic:dict[str, dict[str, any]] = {
            item: {
                "Path": get_target_file_path(base_path, item), #! Überflüssig Kompliziert braucht keinen Aufruf der Funktion
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
        path:str = get_ordner(  get_parent_dir_path(  get_file_path()  ),["Utils","Files"]  ) 
        #! Die Liste mit Inputs lösen und dann ggf mit cwd arbeiten statt relationaler Filepath

        if not os.path.exists(path):
            raise LookupError("Error: Angegebender Ordner gibt es nicht!")
        else:
            items:list[str] = os.listdir(path)
            if not items:
                raise LookupError("Error: Ordner ist Leer!")
            result:dict[str, dict[str, any]] = list_items(path, items) #! muss debuggt werden ob type richtig ist
            list_data_ausgabe(result)
            
    except LookupError as e:
        error_Ausgabe(e)

#? ==============================================================================================================


def vocalCounter():
    '''
    
    '''
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>         Counter Logik             >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def VocalCounter(w:str):
        result:str = formated_text(w)
        zeichen:str = "aeiouAEIOU.,!?;:()\\-_[]"

        counter:dict[str,int] = {b: 0 for b in zeichen} #! Checken ob Typisierung richtig ist

        for char in result:
            if char in counter: counter[char] += 1

        for buchstabe, count in counter.items():
            if count > 0: vocal_ausgabe(buchstabe, count) 
                

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>         Util Functions            >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def vocal_ausgabe(c:str,v:int):
        #! Nur eine Benutzung und daher eigentlich obsolete
        print(f"Zeichen [{c}] : {v} mal")

    def formated_text(t:str):
        regex = r"[^aeiouAEIOU.,!?;:()\-_]]"
        result = re.sub(regex, "", t)
        return result
    
    def message():
        #! Nur eine Benutzung und daher eigentlich obsolete
        print("Wilkommen zum Vokale Zähler")
        print("Gebe dafür Text ein um es zählen zu lassen:")
    


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>           Main Logik              >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    message()
    while(True):
        inp = input().strip()  
        if inp == "": message_err() #! Sollte ich noch nen error werfen und catchen
        else: 
            VocalCounter(inp)
            break
            

#? ==============================================================================================================

def rechner():
    '''
    
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

    def massage():
        #! Nur eine Benutzung und daher eigentlich obsolete 
        #! aber alles an einem Ort gebündelt
        print("Was möchtest du berechnen?")
        print("1. Additives rechnen")
        print("2. Substraktives rechnen")
        print("3. Multiplikatives rechnen")
        print("4. Divisionelles rechnen")
        print("Gebe dafür die gültige Nummer ein (1, 2, 3, 4):")

    def Eingabe()-> list[float]:
        try:
            print("Erste Zahl:")
            eingabe_1 = float(input().strip()) 
            print("Zweite Zahl:")
            eingabe_2 = float(input().strip())
            return [eingabe_1, eingabe_2]
        except ValueError: #! WAS IST HIER PASSIERT???
            raise ValueError("Error: Bitte gültige Zahlen eingeben")
                

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>     Rechnenlogik Switch Case      >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def case_plus(a, b): return f"(Addieren) Ergebnis von {a} {options["plus"]['symbol']} {b} = {a + b}"

    def case_minus(a, b): return f"(Subtrahieren) Ergebnis von {a} {options["minus"]['symbol']} {b} = {a - b}"

    def case_mal(a, b): return f"(Multiplizieren) Ergebnis von {a} {options["mal"]['symbol']} {b} = {a * b}"

    def case_geteilt(a, b):
        if b == 0:
            return "Error: Division durch 0 nicht erlaubt" #! Error werfen und Catchen wenn geteilt wird durch 0
        return f"(Dividieren) Ergebnis von {a} {options["geteilt"]['symbol']} {b} = {a / b}"

    switch = {
        "1": case_plus,
        "2": case_minus,
        "3": case_mal,
        "4": case_geteilt
    }

    '''LambdaSwitch
    # Switch-Case mit Lambda-Funktionen
    #! kann ich mir bei Gelegenheit nochmal anschauen
switch = {
    "1": lambda a, b: f"(Addieren) Ergebnis von {a} {options['plus']['symbol']} {b} = {a + b}",
    "2": lambda a, b: f"(Subtrahieren) Ergebnis von {a} {options['minus']['symbol']} {b} = {a - b}",
    "3": lambda a, b: f"(Multiplizieren) Ergebnis von {a} {options['mal']['symbol']} {b} = {a * b}",
    "4": lambda a, b: f"(Dividieren) Ergebnis von {a} {options['geteilt']['symbol']} {b} = {a / b}" if b != 0 else "Error: Division durch 0 nicht erlaubt",
}
    '''


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>           Main Logik              >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    massage() #! Typo
    rechnenart:str = input().strip()
    try:
        if rechnenart not in switch:
            raise ValueError("Error: Ungültige Rechenart. Bitte eine gültige Nummer (1-4) eingeben.")
        while True: 
            try:
                eingabe:list[float] = Eingabe()
                result:str = switch[rechnenart](eingabe[0], eingabe[1])
                ausgabe(result)
                break
            except ValueError as e:
                error_Ausgabe(e)
                continue
    
    except ValueError as e:
        error_Ausgabe(e)
        

#? ==============================================================================================================

def passwortGen():
    '''
    
    '''
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>              Utils                >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def pGen(length:int, charset:list[str]) -> str:
        '''
        Generiert ein zufälliges Passwort aus dem übergebenen Charset.

        Args:
            #* length (int): Die Länge des generierten Passworts.
            #* charset (list[str]): Eine Liste von Zeichen, aus der das Passwort generiert wird.

        Returns:
            #? str: Das generierte Passwort.
        '''
        return ''.join(random.choices(population=charset, weights=None, k=length))


    def generate_charset(letters: bool = True, numbers: bool = True, special: bool = True) -> list[str]:
        '''
        Generiert ein Array von Zeichen basierend auf den übergebenen Parametern.

        Args:
            #* letters (bool): Ob Buchstaben (a-z, A-Z) enthalten sein sollen. Standard: True.
            #* numbers (bool): Ob Zahlen (0-9) enthalten sein sollen. Standard: True.
            #* special (bool): Ob Sonderzeichen enthalten sein sollen. Standard: True.

        Returns:
            #? charset_array (list[str]): Ein Array von Zeichen basierend auf den ausgewählten Kategorien.
        '''

        charset_array = [] #! brauche ich ein arry mit dem extend? => nur ein Element in dem Array

        # Buchstaben hinzufügen
        if letters: charset_array.extend(string.ascii_lowercase + string.ascii_uppercase)

        # Zahlen hinzufügen
        if numbers: charset_array.extend(string.digits)

        # Sonderzeichen hinzufügen
        if special: charset_array.extend("!@#$%^&*()_+-=[]{}|;:,.<>?/`~")

        return charset_array

    def password_ausgabe(d:str):
        '''
        Generiert eine Ausgabe von Text nach vorgefertigter Formatierung
        #! Nur eine Benutzung und daher eigentlich obsolete

        Args:
            #* d (str): Ist der auszugebende Text
        '''
        print(f"Dein generiertes Passwort ist: \"{d}\"")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>           Main Logik              >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    length:str = input("Gebe die Länge deines Passwortes ein: ")

    letters:bool = input("Möchtest du Buchstaben benutzen? (y/n): ") == "y"  #! Nicht optimiert auf andere Eingabe als y oder irgendwas anderes
    numbers:bool = input("Möchtest du Zahlen benutzen? (y/n): ") == "y"  #! Nicht optimiert auf andere Eingabe als y oder irgendwas anderes
    special:bool = input("Möchtest du Sonderzeichen benutzen? (y/n): ") == "y"  #! Nicht optimiert auf andere Eingabe als y oder irgendwas anderes  

    try:
        valid_input:bool = validate(length, "num")
        
        if valid_input:
            pw:str = pGen(length=int(length), charset=generate_charset(letters=letters, numbers=numbers, special=special))
            password_ausgabe(pw)
    except ValueError as e:
        error_Ausgabe(e)
    except Exception as e:
        error_Ausgabe(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

#? ==============================================================================================================

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#? >>>      Functions Switch case        >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

functions = {
    "1" : {
            "name": "ListFiles von Ordner",
            "desc" :"Liste deine Files Aus von einem Ordner mit Zusatz Infos auf.",
            "func": listData
           },
    "2" : {
            "name": "Vokalezähler",
            "desc" :"Zähle die Vokale von einem eingegebenem Wort",
            "func": vocalCounter
           },
    "3" : {
            "name": "Rechner",
            "desc" :"Rechne Plus Minus Mal Geteilt Aufgaben aus",
            "func": rechner
           },
    "4" : {
            "name": "Passwort Generator",
            "desc" :"Erstelle ein Passwort auf Grundlage verschiedener Vorgaben",
            "func": passwortGen
           },
}

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#? >>>             Utils                 >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def error_Ausgabe_Wrapper(func:any,e:any):
    '''
    Wrapped die Error-Ausgaben-Funktion und erweitert das mit weiterer Funktionalität. 
    => Middleware

    Args:
        #* func (any): Error-Ausgaben-Funktion / Möglichkeit für handling mehrerer Error-Ausgaben-Funktionen.
        #* e (any): Der Error, der geworfen wurde, mit dem angehangenen Text.
    '''
    func(e)
    message_err()
    auswahl()

def auswahl():
    anzahl:int = len(functions.keys())
    print("Welche Funktion möchtest du benutzen?")

    for (k,v) in functions.items():
        name = v["name"]
        print(f"{k}. {name}")

    print(f"Gebe dafür eine Zahl zwischen 1 und {anzahl} ein:")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#? >>>           Main Logik              >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def Main():
    while True:
        auswahl()
        inp:str = input().strip()
        try:
            if(validate(inp,"num") ): #! muss eigentlich nicht als int gecasted werden
                functions[inp]["func"]()
                repeat:bool = input("Möchtest du noch eine Function laufen lassen? (y/n): ") == "y"
                if not repeat: break 
            else:
                raise ValueError(f"Ungültige Auswahl: {inp}. Bitte wähle eine gültige Nummer.")
        except ValueError as e:
            error_Ausgabe_Wrapper(error_Ausgabe,e)
        except Exception as e:
            error_Ausgabe_Wrapper(error_Ausgabe,e)



if __name__ == "__main__": Main()