from datetime import datetime
from data_classes.Passwort import Passwort
from data_classes.Charset import Charset
from .FunctionBase import FunctionBase

class PasswortGenerator(FunctionBase):
    _passwort:Passwort | None
    _time_of_creation:datetime | None
    _charset:Charset | None
    _passwort_length:int | None

    def __init__(self,charset:Charset,length:int):
        self._charset = charset
        self._passwort_length = length
        self._time_of_creation = None
        self._initiate()

    def _message(self):
        return super()._message()

    def _initiate(self) -> None:
        from random import choices
        from Utils.UtilFunctions.globalUtils import get_time_of_output

        
        self._time_of_creation = get_time_of_output()

        pw = Passwort()
        pw.set_passwort(''.join(choices(population=self._charset.get_charset(), weights=None, k=self._passwort_length)))
        pw.set_length(self._passwort_length)

        self._passwort = pw


    def ausgabe(self) -> None: 
        self._passwort.ausgabe()
        print(f"Zeit des Erstellens von dem Passwort: {self._time_of_creation}")

