from pathlib import Path
import hashlib
from Utils.UtilFunctions import error_ausgabe

def ausgabe(d: str) -> None: 
    print(f"{d}")

def validate_file(file: Path) -> bool:
    """Überprüft, ob eine Datei existiert und nicht leer ist."""
    if not file.exists():
        print(f"Warnung: Die Datei {file} existiert nicht.")
        return False
    if file.stat().st_size == 0:
        print(f"Warnung: Die Datei {file} ist leer.")
        return False
    return True

def get_hash_from_file(file: Path = None) -> str:
    """Berechnet den SHA256-Hash einer Datei."""
    if not file: raise LookupError("File*s gibt es nicht!")
    if not validate_file(file): return None 

    return hashlib.sha256(open(file, "rb").read()).hexdigest()

def get_hashes_from_files(files: list[Path]) -> dict[str, str]:
    """Berechnet die Hashes für alle Dateien in der Liste."""
    hash_dict = {}
    for file in files:
        hash_val = get_hash_from_file(file)
        if hash_val: hash_dict[file.name] = hash_val
    return hash_dict

def get_all_files_from_folder(p: Path) -> list[Path]:
    """Gibt alle Dateien aus einem Ordner zurück."""
    files: list[Path] = list(p.glob("*"))
    if not files: raise LookupError("Keine Files in dem Ordner!")
    return files

def check_for_duplicate_hashes(hash_dict: dict[str, str]) -> None:
    hash_groups = {}

    for filename, hash_val in hash_dict.items():
        if hash_val not in hash_groups: hash_groups[hash_val] = []  
        hash_groups[hash_val].append(filename)

    any_matches = False
    for hash_val, filenames in hash_groups.items():
        if len(filenames) > 1: 
            any_matches = True
            ausgabe(f"Die folgenden Dateien haben denselben Hash ({hash_val}): {', '.join(filenames)}")

    if not any_matches:
        ausgabe("Es wurden keine gleichen Hashes gefunden.")

def Main() -> None:
    file_path: Path = Path.cwd() / "LA06" / "out"
    files: list[Path] = get_all_files_from_folder(file_path)
    
    try:
        file_paths = [file_path / file for file in files]
        hash_dict = get_hashes_from_files(file_paths)
        check_for_duplicate_hashes(hash_dict)
    except Exception as e:
        error_ausgabe(e=e)

if __name__ == "__main__": 
    Main()
