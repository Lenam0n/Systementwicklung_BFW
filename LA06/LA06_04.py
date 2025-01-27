from pathlib import Path
import hashlib
from Utils.UtilFunctions import error_ausgabe

def ausgabe(d:str) -> None: print(f"{d}")

def get_hash_from_file(file:Path = None) -> str:
    if not file:
        raise LookupError("File*s gibt es nicht!")

    return hashlib.sha256(open(file, "rb").read()).hexdigest()
    #? @Param open(mode: "r") => read 
    #? @Param open(mode: "b") => binarymode sprich rückgabe als bytes und nicht als string
    #* -----------------------------------------------------------------------------------
    #? @Param open(mode: "rb") => kombination von beidem


def Main() -> None:
    file_path:str= Path.cwd()/"LA06"/"out"
    file:str = "test.txt"
    try:
        hash_val:hash = get_hash_from_file(file=file_path/file)
        ausgabe(hash_val)
    except Exception as e:
        error_ausgabe(e=e)

if __name__ == "__main__": Main()