import os
import re
import random
import string

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>        Utility Functions          >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def validate(d: str, vtype: str) -> bool:
    '''
    Validiert eine Eingabe basierend auf einem vordefinierten Typ (z.B. Zahlen, Text).

    Args:
        d (str): Die zu prüfende Eingabe.
        vtype (str): Der Typ der Validierung ("num" oder "text").

    Returns:
        bool: True, wenn die Eingabe gültig ist, sonst False.
    '''
    try:
        patterns: dict[str, str] = {
            "num": r"\d+",
            "text": r"[a-zA-Z]+"
        }
        if vtype not in patterns:
            raise ValueError(f"Ungültiger Typ: '{vtype}' wird nicht unterstützt.")
        return bool(re.fullmatch(patterns[vtype], str(d)))
    except Exception as e:
        print(f"Fehler bei der Validierung: {e}")
        return False

def error_output(e: Exception) -> None:
    '''
    Gibt einen Fehler formatiert aus.

    Args:
        e (Exception): Der auszugebende Fehler.
    '''
    print(f"Error: {e}")

def list_data_output(data: dict[str, dict[str, any]], spacer: str = "-" * 25) -> None:
    '''
    Gibt die Inhalte eines Verzeichnisses formatiert aus.

    Args:
        data (dict): Die Verzeichnisdaten mit Details zu Dateien.
        spacer (str): Der Trenner zwischen den Einträgen (Standard: "-------------------------").
    '''
    try:
        print(spacer)
        for key, value in data.items():
            print(f"{key}:")
            for sub_key, sub_value in value.items():
                print(f"  {sub_key}: {sub_value}")
            print(spacer)
    except Exception as e:
        error_output(f"Fehler bei der Ausgabe der Daten: {e}")

def generate_password(length: int, charset: list[str]) -> str:
    '''
    Generiert ein zufälliges Passwort basierend auf der angegebenen Länge und Zeichensatz.

    Args:
        length (int): Die Länge des Passworts.
        charset (list[str]): Der Zeichensatz für das Passwort.

    Returns:
        str: Das generierte Passwort.
    '''
    try:
        if length <= 0:
            raise ValueError("Die Passwortlänge muss größer als 0 sein.")
        if not charset:
            raise ValueError("Der Zeichensatz darf nicht leer sein.")
        return ''.join(random.choices(population=charset, k=length))
    except Exception as e:
        error_output(f"Fehler bei der Passwortgenerierung: {e}")
        return ""

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>         Hauptfunktionen           >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def list_data() -> None:
    '''
    Listet die Dateien in einem bestimmten Ordner auf und zeigt Details wie Pfad, Größe und Erweiterung.
    '''
    def get_path(base: str, *sub_dirs: str) -> str:
        '''
        Kombiniert den Basispfad mit Unterordnern.

        Args:
            base (str): Der Basispfad.
            sub_dirs (str): Unterordner.

        Returns:
            str: Der vollständige Pfad.
        '''
        return os.path.join(base, *sub_dirs)

    def get_file_details(path: str, files: list[str]) -> dict[str, dict[str, any]]:
        '''
        Erstellt eine Übersicht der Dateien mit deren Pfad, Größe und Erweiterung.

        Args:
            path (str): Der Ordnerpfad.
            files (list[str]): Liste der Dateien.

        Returns:
            dict[str, dict[str, any]]: Ein Dictionary mit Datei-Details.
        '''
        try:
            return {
                file: {
                    "Path": get_path(path, file),
                    "Size": os.stat(get_path(path, file)).st_size,
                    "Extension": os.path.splitext(file)[1]
                } for file in files
            }
        except FileNotFoundError:
            raise FileNotFoundError("Eine oder mehrere Dateien wurden nicht gefunden.")
        except Exception as e:
            raise RuntimeError(f"Fehler beim Abrufen von Dateidetails: {e}")
    try:
        path: str = os.path.join(os.path.abspath(os.path.join(__file__, "../../")), "Utils", "Files")
        if not os.path.exists(path):
            raise FileNotFoundError("Der angegebene Ordner existiert nicht.")

        items: list[str] = os.listdir(path)
        if not items:
            raise FileNotFoundError("Der Ordner ist leer.")

        result: dict[str, dict[str, any]] = get_file_details(path, items)
        list_data_output(result)

    except FileNotFoundError as e:
        error_output(e)
    except PermissionError:
        error_output("Keine Berechtigung, um auf den Ordner zuzugreifen.")
    except Exception as e:
        error_output(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

def vocal_counter() -> None:
    '''
    Zählt die Vokale in einem eingegebenen Text und gibt die Anzahl pro Zeichen aus.
    '''
    def count_vocals(text: str) -> dict[str, int]:
        '''
        Zählt die Vorkommen aller Vokale im Text.

        Args:
            text (str): Der zu analysierende Text.

        Returns:
            dict[str, int]: Ein Dictionary mit Vokalen und deren Anzahl.
        '''
        try:
            filtered: str = re.sub(r"[^aeiouAEIOU]", "", text)
            return {char: filtered.count(char) for char in set(filtered)}
        except Exception as e:
            raise ValueError(f"Fehler beim Zählen der Vokale: {e}")

    try:
        text: str = input("Gebe einen Text ein: ").strip()
        if not text:
            raise ValueError("Eingabe darf nicht leer sein.")

        results: dict[str, int] = count_vocals(text)
        for char, count in results.items():
            print(f"Zeichen [{char}]: {count} mal")
    except ValueError as e:
        error_output(e)
    except Exception as e:
        error_output(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

def calculator() -> None:
    '''
    Führt einfache mathematische Operationen (Addition, Subtraktion, Multiplikation, Division) basierend auf Benutzereingaben aus.
    '''
    operations: dict[str, tuple[str, any]] = {
        "1": ("+", lambda a, b: a + b),
        "2": ("-", lambda a, b: a - b),
        "3": ("*", lambda a, b: a * b),
        "4": ("/", lambda a, b: a / b if b != 0 else (_ for _ in ()).throw(ZeroDivisionError("Division durch 0 ist nicht erlaubt")))
    }

    try:
        print("Wähle eine Rechenoperation:")
        print("1. Addition")
        print("2. Subtraktion")
        print("3. Multiplikation")
        print("4. Division")

        operation: str = input("Eingabe: ").strip()
        if operation not in operations:
            raise ValueError("Ungültige Auswahl.")

        def parse_number(prompt: str) -> int | float:
            '''
            Versucht die Eingabe als int oder float zu parsen.

            Args:
                prompt (str): Der Eingabeaufforderungstext.

            Returns:
                int | float: Die geparste Zahl als int oder float.

            Raises:
                ValueError: Wenn die Eingabe keine gültige Zahl ist.
            '''
            user_input: str = input(prompt).strip()
            try:
                if '.' in user_input:
                    return float(user_input)
                else:
                    return int(user_input)
            except ValueError:
                raise ValueError(f"Ungültige Zahl: '{user_input}'. Bitte eine gültige Zahl eingeben.")

        a: int | float = parse_number("Erste Zahl: ")
        b: int | float = parse_number("Zweite Zahl: ")

        symbol: str
        func: any
        symbol, func = operations[operation]
        result: any = func(a, b)
        print(f"Ergebnis: {a} {symbol} {b} = {result}")

    except ZeroDivisionError:
        error_output("Division durch 0 ist nicht erlaubt.")
    except ValueError as e:
        error_output(e)
    except KeyboardInterrupt:
        error_output("Eingabe abgebrochen.")
    except Exception as e:
        error_output(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

def password_generator() -> None:
    '''
    Generiert ein sicheres Passwort basierend auf Benutzereinstellungen (Länge, Zeichensatz).
    '''
    def build_charset() -> list[str]:
        '''
        Baut den Zeichensatz basierend auf Benutzerauswahl auf.

        Returns:
            list[str]: Der erstellte Zeichensatz.
        '''
        charset: list[str] = []
        try:
            def get_yes_no_input(prompt: str) -> bool:
                response: str = input(prompt).strip().lower()
                if response not in ["y", "n"]:
                    raise ValueError("Ungültige Eingabe! Bitte nur 'y' oder 'n' verwenden.")
                return response == "y"

            if get_yes_no_input("Buchstaben verwenden? (y/n): "):
                charset.extend(string.ascii_letters)
            if get_yes_no_input("Zahlen verwenden? (y/n): "):
                charset.extend(string.digits)
            if get_yes_no_input("Sonderzeichen verwenden? (y/n): "):
                charset.extend("!@#$%^&*()_+-=[]{}|;:,.<>?/")
        except ValueError as e:
            error_output(f"Fehler beim Erstellen des Zeichensatzes: {e}")
        return charset

    try:
        length: int = int(input("Passwortlänge: ").strip())
        if length <= 0:
            raise ValueError("Die Passwortlänge muss größer als 0 sein.")

        charset: list[str] = build_charset()
        if not charset:
            raise ValueError("Kein Zeichensatz ausgewählt.")

        password: str = generate_password(length, charset)
        if password:
            print(f"Generiertes Passwort: {password}")
    except ValueError as e:
        error_output(e)
    except Exception as e:
        error_output(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>          Hauptprogramm           >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def main() -> None:
    '''
    Hauptprogramm zur Auswahl und Ausführung verschiedener Funktionen.
    '''
    functions: dict[str, tuple[str, any]] = {
        "1": ("List Dateien", list_data),
        "2": ("Vokalezähler", vocal_counter),
        "3": ("Rechner", calculator),
        "4": ("Passwort Generator", password_generator),
        "5": ("Code Beenden", lambda: (print("Okay Bye"), exit()))
    }

    try:
        while True:
            print("Wähle eine Funktion:")
            for key, (name, _) in functions.items():
                print(f"{key}. {name}")

            choice: str = input("Eingabe: ").strip()
            if choice in functions:
                _, func = functions[choice]
                func()
                if input("Noch eine Funktion ausführen? (y/n): ").strip().lower() != "y":
                    break
            else:
                print("Ungültige Auswahl.")
    except KeyboardInterrupt:
        print("Programm wurde vom Benutzer abgebrochen.")
    except Exception as e:
        error_output(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    main()
