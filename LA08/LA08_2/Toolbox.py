from data_classes.Charset import Charset
from function_classes.Rechner import Rechner
from function_classes.VocalCounter import VocalCounter
from function_classes.PasswortGenerator import PasswortGenerator
from function_classes.ListData import ListData
import function_classes
from Utils.UtilFunctions.inputUtils import user_choice


class Toolbox:
    functions:list[any]
    function_instances:list[any]
    def __init__(self):
        self.functions = (
            [getattr(function_classes, cls) for cls in dir(function_classes)
            if isinstance(getattr(function_classes, cls), type)]
            + [
                (lambda f: (setattr(f, "__name__", "Programm beenden"), f)[1])
                (lambda: (print("okay bye") or exit()))
            ]
        )

        self.function_instances = []

    def _runDatalist(self, function_class: ListData) -> ListData:
        '''
        
        '''
        """       
            base_path:str = user_choice(
            prompt = f"Gebe dafür eine Zahl zwischen 1 und {anzahl} ein: ",
            choices = list(range(1, anzahl + 1)))
        #! auswahl von cwd oder ein genauer pfad -> wie validiere ich den random path?    
        """
        from os import getcwd
        base_path: str = getcwd()
        subdir: str | list[str] | None = ["Utils","Mokdata"], #! Usereingabe noch einbauen!
        return function_class(base_path = base_path, subdir = subdir)
    
    def _runVocalCounter(self, function_class:VocalCounter):
        '''
        
        '''
        from data_classes.Charset import Charset

        charset = Charset()
        charset.initiate_charset(vocal=True)
        return function_class(charset)
    
    def _runRechner(self, function_class:Rechner) -> Rechner:
        '''
        
        '''
        return function_class()

    def _runPasswordGenerator(self, function_class:PasswortGenerator) -> PasswortGenerator:
        '''
        
        '''

        charset = Charset()
        charset.initiate_charset(vocal=False)
        passwort_length = user_choice(prompt="Gebe die Länge deines Passwortes ein: ", choices="num", return_type=int)
        return function_class(charset=charset , length=passwort_length)

    def _auswahl(self) -> int:
        '''
        Zeigt das Hauptmenü an und listet alle verfügbaren Funktionen zur Auswahl und nimmt die Auswahl, validiert entgegen.

        Returns:
            #? Input (str): Gibt die Menüauswahl zurück.
        '''
        from Utils.UtilFunctions.inputUtils import user_choice

        anzahl:int = len(self.functions)
        print("Welche Funktion möchtest du benutzen?")
        for index, function_class in enumerate(self.functions): print(f"{(index +1)}. {function_class.__name__}")
        return user_choice(
            prompt = f"Gebe dafür eine Zahl zwischen 1 und {anzahl} ein: ",
            choices = list(map(str, range(1, anzahl + 1))),
            error_message = "Ungültiger Index!",
            return_type=int)

    def initiate(self) -> None:
        '''Hauptfunktion von der Toolbox'''
        from Utils.UtilFunctions.inputUtils import user_choice
        while True:
            inp:int = self._auswahl()
            try:
                function_class = self.functions[(inp - 1)]
                function_instance = None
                match function_class.__name__:
                    case "ListData": function_instance = self._runDatalist(function_class=function_class)
                    case "VocalCounter": function_instance = self._runVocalCounter(function_class=function_class)
                    case "Rechner": function_instance = self._runRechner(function_class=function_class)
                    case "PasswortGenerator": function_instance = self._runPasswordGenerator(function_class=function_class)
                    case "Programm beenden": function_class()
                    case _: raise RuntimeError(f"Keine spezielle Funktion für {function_class.__name__}")

                if function_instance != None: 
                    self.function_instances.append(function_instance) 
                    function_instance.ausgabe()
                else: raise RuntimeError("Es wurde keine Funktionsklasse erstellt!")

            except Exception as e:
                from Utils.UtilFunctions.errorUtils import error_ausgabe
                error_ausgabe(e)

            repeat: bool = user_choice(
                    prompt="Möchtest du noch eine Funktion laufen lassen? (y/n): ",
                    choices=["y","n"]) == "y"
                
            if not repeat: break