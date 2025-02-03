from os import listdir, getcwd
from os.path import exists, join, isfile
from Utils.UtilFunctions.errorUtils import error_ausgabe
from .FunctionBase import FunctionBase
from data_classes.Datalist import Datalist

class ListData(FunctionBase):
    base_path:str
    subdir:str | list[str]
    path:str
    datalist:Datalist
    def __init__(
                self, 
                base_path:str = getcwd(), 
                subdir: str | list[str] | None = None,
            ):
        self.base_path = base_path
        self.subdir = subdir # ["Utils","Mokdata"]
        self.path = self._get_ordner() #! Error wird noch nicht gecatched
        self.datalist = Datalist(base_path = self.path)

        self._initiate()

        '''
        #? Erweiterbar mit von CWD alle Subordner auflisten die man dann mit einem index auswählen kann 
            #? => dann automatisch übergeben werden im array
        '''

    def _message(self):
        return super()._message()

    #? Absoluter Pfad zu Target Ordner
    def _get_ordner(self) -> str:
        '''
        Erstellt einen vollständigen Pfad aus einem Basisverzeichnis und einer Liste von Unterordnern.

        Args:
            #* p_path (str): Basisverzeichnis.
            #* t_sub_dir (list[str]): Liste von Unterordnern.

        Returns:
            #? str: Der kombinierte Verzeichnispfad.
        '''

        path = self.base_path + "\\" + "\\".join(*self.subdir)
        if not exists(path): raise LookupError(f"Angegebender Ordner: \"{path}\" gibt es nicht!")
        else: return path

    #? füge Files aus Path Datalist hinzu
    def _initiate(self) -> None:
        try:
            items:list[str] = list(
            filter(lambda item: 
                   isfile( join((self.base_path + "\\" + "\\".join(*self.subdir)), item) ), 
                   listdir(self.base_path+ "\\" + "\\".join(*self.subdir)) ) )
            
            if not items: raise LookupError("Ordner ist Leer!")
        
            self.datalist.generate_datalist(items=items)
                
        except LookupError as e:
            error_ausgabe(e)  

    #? Ausgabenweiterleitung an Datalist
    def ausgabe(self) -> None:
        self.datalist.ausgabe(spacer="-")