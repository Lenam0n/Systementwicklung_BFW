from data_classes.Charset import Charset
from .FunctionBase import FunctionBase

#"aeiouAEIOU.,!?;:()\-_[]"
class VocalCounter(FunctionBase):
    _charset: Charset
    _counter_result: dict[str,int]
    def __init__(self,
                 charset:Charset):
        self._charset = charset.get_charset()
        self._counter_result = self._create() 
        self._initiate()

    def _message(self):
        return super()._message()
        
    def _create(self) -> dict[str,int]: return {b: 0 for b in self._charset}
    
    def _initiate(self) -> None:
        from Utils.UtilFunctions.globalUtils import format_text

        inp:str = input("Gebe dafür Text ein, um es zählen zu lassen: ")
        result: str = format_text(inp, rf"[^r{self._charset}]")
        for char in result:
            if char in self._counter_result:
                self._counter_result[char] += 1

    def ausgabe(self) -> None:
        '''
        Gibt die Häufigkeit der gezählten Zeichen aus.

        Args:
            #* counter (dict[str, int]): Dictionary mit Zeichen und deren Häufigkeit.

        Returns:
            #? None: Gibt die Häufigkeiten formatiert in der Konsole aus.
        '''

        for buchstabe, count in self._counter_result.items():
            if count > 0:
                print(f"Zeichen [{buchstabe}] : {count} mal")
     