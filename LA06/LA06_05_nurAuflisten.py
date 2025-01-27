from pathlib import Path
import hashlib
from Utils.UtilFunctions import error_ausgabe

def ausgabe(d: str) -> None: print(f"{d}")

def get_hash_from_file(file: Path = None) -> str:
    if not file: raise LookupError("File*s gibt es nicht!")
    
    return hashlib.sha256(open(file, "rb").read()).hexdigest()

def get_hashes_from_files(files: list[Path]) -> dict[str, str]:
    return {file.name: get_hash_from_file(file) for file in files}
    #? Path.name gibt nur den Namen der File zurück 
    #? => z.b "test.txt" aus "../Systementwicklung_BFW/LA06/out/test.txt"

def get_all_files_from_folder(p:Path) -> list[Path]:
    files:list[Path] = list(p.glob("*"))
    if not files: raise LookupError("Keine Files in dem Ordner!")
    else: return files

#! -----------------------------------------------------------------------

def Main() -> None:
    file_path: str = Path.cwd() / "LA06" / "out"
    files: list[str] = get_all_files_from_folder(file_path)
    try:
        file_paths = [file_path / file for file in files]
        hash_dict = get_hashes_from_files(file_paths)
        for filename, hash_val in hash_dict.items():
            ausgabe(f"{filename}: {hash_val}")
    except Exception as e:
        error_ausgabe(e=e)

if __name__ == "__main__": Main()