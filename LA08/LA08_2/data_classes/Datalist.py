from .Data import Data

class Datalist():
    base_path: str | None
    items:list[str] | None
    _datalist: list[Data] | None
    def __init__(self, base_path: str | None = None, items: list[str] | None = None):
            self.base_path: str | None = base_path
            self.items:list[str] | None = items
            self._datalist: list[Data] | None = None
            

    def generate_datalist(self,items:list[str]) -> list[Data]:
        '''Generiert eine Liste von Data-Objekten aus den Items und speichert sie in _datalist.'''
        from os import stat
        from os.path import join

        def get_file_extention(fn:str) -> str:
            '''
            Extrahiert die Dateiendung aus einem Dateinamen.

            Args:
                #* fn (str): Der Filename.

            Returns:
                #? str: Die Dateiendung (z.B. ".txt"), falls vorhanden, sonst ein leerer String.
            '''
            from re import search

            match:any = search(r'\.([^\s.]+)$', fn)

            if match: return f".{match.group(1)}".strip()
            else: return ""

        self._datalist = [
            Data(
                path = join(self.base_path, item),
                size = stat(join(self.base_path, item)).st_size,
                extention = get_file_extention(item)
            )
            for item in items
        ]

    def get_datalist(self) -> list[Data]: return self._datalist
    
    def set_datalist(self, d_liste: list[Data]) -> None: self._datalist = d_liste

    def ausgabe(self,spacer:str= "-"):
        '''
        Gibt die formatierten Datei- und Ordnerinformationen aus.

        Args:
            #* spacer (str, optional): Zeichen zur Trennung der Einträge. Standard: "-" * 25.

        Returns:
            #? None: Gibt die formatierten Daten aus.
        '''
        from os.path import basename

        print(spacer* 25)
        for file in self._datalist:
            print(basename(file.get_path()))
            print(f"  Path: {file.get_path()}")
            print(f"  Size: {file.get_size()} byte")
            print(f"  Extension: {file.get_extention()}")
            print(spacer* 25)

        print() 
