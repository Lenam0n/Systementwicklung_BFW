from pathlib import Path

from Utils.UtilFunctions import error_ausgabe
from Utils.UtilFunctions import user_choice

def validate_path(path: Path, should_exist: bool = True) -> bool:
    '''
    Validiert, ob eine Datei existiert oder nicht.

    Params:
    #* path: Path → Der zu überprüfende Dateipfad.
    #* should_exist: bool → Erwartet, dass die Datei existiert (True) oder nicht existiert (False).
    
    Errors:
    #! LookupError: Wenn der Pfad nicht die gewünschten Bedingungen erfüllt.
    '''

    if should_exist and not path.exists(): raise LookupError(f"Datei existiert nicht: {path}")
    if not should_exist and path.exists(): raise LookupError(f"Datei existiert bereits: {path}")
    if not path.is_file(): raise LookupError(f"Pfad ist keine Datei: {path}")
    return True

def createFile(name: str = "name.txt", content: str = "", p: str = "") -> bool:
    '''
    Erstellt eine Datei mit optionalem Inhalt. Falls die Datei existiert, kann der Nutzer:
    - Überschreiben
    - Anhängen
    - Ignorieren
    '''
    file_path = Path(p) / name

    try: validate_path(file_path.parent, should_exist=True)  #* Prüft, ob das Verzeichnis existiert.
    except LookupError as e:
        error_ausgabe(e)
        return False

    if file_path.exists():
        try: validate_path(file_path, should_exist=True)  #* Prüft, ob es eine Datei ist.
        except LookupError as e:
            error_ausgabe(e)
            return False
        #! Hier sollte eine abfrage kommen oder direkt schon die file erstellt werden

        choices = {"ü": "overwrite", "u": "overwrite", "a": "append", "i": "ignore"}
        action = user_choice(prompt=f"Die Datei '{file_path.name}' existiert bereits. [Ü]berschreiben, [A]nhängen, [I]gnorieren: ", choices=choices)

        match action:
            case "overwrite":
                file_path.write_text(data=content, encoding="utf-8")
                print(f"Datei überschrieben: {file_path}")
                return True
            case "append":
                file_path.write_text(data=(file_path.read_text(encoding="utf-8") + "\n" + content), encoding="utf-8")
                print(f"Inhalt angehängt: {file_path}")
                return True
            case _:
                print(f"Datei bleibt unverändert: {file_path}")
                return False
    # Datei erstellen, wenn sie nicht existiert
    try:
        validate_path(path=file_path, should_exist=False)  # Prüft, dass die Datei nicht existiert.
    except LookupError as e:
        error_ausgabe(e)
        return False

    file_path.write_text(data=content, encoding="utf-8")
    print(f"Datei erstellt: {file_path}")
    return True

def Main() -> None:
    filename = "test"
    createFile(content="Hallo, Welt!", p=Path.cwd()/"LA06"/"out"/filename)

if __name__ == "__main__": Main()
