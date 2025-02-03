from Utils.UtilFunctions.inputUtils import user_choice
from .FunctionBase import FunctionBase

class Rechner(FunctionBase):
    _num_1: int | float 
    _num_2: int | float
    _rechenart: str
    _result: int | float 

    def __init__(self):
        self._choises = {
                            "1": lambda a, b: f"(Addieren) Ergebnis von {a} + {b} = {a + b}",
                            "2": lambda a, b: f"(Subtrahieren) Ergebnis von {a} - {b} = {a - b}",
                            "3": lambda a, b: f"(Multiplizieren) Ergebnis von {a} * {b} = {a * b}",
                            "4": lambda a, b: f"(Dividieren) Ergebnis von {a} / {b} = {a / b}" if b != 0 else None
                        }
        self._initiate()

    def _message(self) -> None:
        print("Was möchtest du berechnen?")
        print("1. Additives Rechnen")
        print("2. Subtraktives Rechnen")
        print("3. Multiplikatives Rechnen")
        print("4. Divisionelles Rechnen")
    
    def _initiate(self) -> None:
        self._rechenart = self._create_rechenart()
        self._num_1, self._num_2 = self._create_numbers()
        self._result = self._calculate()

    def _create_rechenart(self) -> str:
        self._message()
        return user_choice(
            prompt="Gebe dafür die gültige Nummer ein (1, 2, 3, 4): ",
            choices=list(self._choises.keys()),
            error_message="Ungültige Rechenart. Bitte eine gültige Nummer eingeben"
        )
    
    def _create_numbers(self) -> tuple[int | float]:
        def convert(value: str) -> int | float:
            if ',' in value: return float(value.replace(',', '.'))
            else: return int(value)

        return tuple(
            convert(
                user_choice(
                    prompt=f"{zahl} Zahl: ",
                    choices="num",
                    error_message="Bitte gültige Zahlen eingeben",
                    return_type=str
                )
            )
            for zahl in ("Erste", "Zweite")
        )

    def _calculate(self) -> int | float:
        result = self._choises[self._rechenart](self._num_1, self._num_2)
        if result is None: raise ValueError("Division durch 0 nicht erlaubt")

        if isinstance(result, float) and result.is_integer(): return int(result)
        else: return result
        
    def get_result(self) -> int | float:
        return self._result

    def ausgabe(self) -> None:
        print(self._result)
