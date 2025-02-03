from Utils.UtilFunctions.errorUtils import error_ausgabe
from Utils.UtilFunctions.inputUtils import user_choice
import string

class Charset():
    _num: str | None
    _letters: str | None
    _special: str | None

    def __init__(self):
        self._num = None
        self._letters = None
        self._special = None

    def initiate_charset(self, vocal: bool = False):
        prompt_1: str = "Möchtest du "
        prompt_2: str = " benutzen? (y/n): "

        try:
            charset_dict = {}
            if vocal:
                charset_dict["letters"] = "aeiouAEIOU"
                charset_dict["special"] = r".,!?;:()\-_[]"
            else:
                #* Buchstaben hinzufügen
                if self._create_letters_charset(prompt_1, prompt_2):
                    charset_dict["letters"] = string.ascii_letters

                #* Zahlen hinzufügen
                if self._create_num_charset(prompt_1, prompt_2):
                    charset_dict["num"] = string.digits

                #* Sonderzeichen hinzufügen
                if self._create_special_charset(prompt_1, prompt_2):
                    charset_dict["special"] = "!@#$%^&*()_+-=[]{}|;:,.<>?/`~"

            if not charset_dict:
                raise AttributeError("Charset darf nicht leer sein!")
            
            self._letters = charset_dict.get("letters", None)
            self._num = charset_dict.get("num", None)
            self._special = charset_dict.get("special", None)

        except Exception as e:
            error_ausgabe(e)

    def _create_num_charset(self, prompt_1: str, prompt_2: str) -> bool:
        return user_choice(
            prompt=f"{prompt_1} Zahlen {prompt_2}",
            choices=["y", "n"]
        ) == "y"

    def _create_letters_charset(self, prompt_1: str, prompt_2: str) -> bool:
        return user_choice(
            prompt=f"{prompt_1} Buchstaben {prompt_2}",
            choices=["y", "n"]
        ) == "y"

    def _create_special_charset(self, prompt_1: str, prompt_2: str) -> bool:
        return user_choice(
            prompt=f"{prompt_1} Sonderzeichen {prompt_2}",
            choices=["y", "n"]
        ) == "y"

    def get_charset(self):
        charset = "".join(part for part in (self._letters, self._num, self._special) if part)
        return charset if charset else None
