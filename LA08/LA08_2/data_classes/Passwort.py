class Passwort():
    _passwort:str | None
    _length:int | None

    def __init__(self): 
        self._passwort = None  
        self._length = None  

    def get_passwort(self) -> str: return self._passwort
    def get_length(self) -> str: return self._length

    def set_passwort(self, pw:str) -> None: self._passwort = pw
    def set_length(self, len:str) -> None: self._length = len

    def ausgabe(self) -> None: print(f"Dein generiertes Passwort ist: \"{self._passwort}\"")