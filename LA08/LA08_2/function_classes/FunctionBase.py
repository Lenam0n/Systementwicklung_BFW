from abc import ABC, abstractmethod

class FunctionBase(ABC):
    @abstractmethod
    def _message(self) -> None:
        """
        Gibt eine initiale Nachricht oder Information aus.
        """
        pass

    @abstractmethod
    def _initiate(self) -> None:
        """
        Startet oder initialisiert den jeweiligen Prozess.
        """
        pass

    @abstractmethod
    def ausgabe(self) -> None:
        """
        Kümmert sich um die Ausgabe des Ergebnisses oder der Daten.
        """
        pass