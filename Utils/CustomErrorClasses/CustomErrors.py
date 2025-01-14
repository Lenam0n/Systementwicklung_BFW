class CustomError(Exception):
    """Ein benutzerdefinierter Fehler für spezielle Fälle."""
    def __init__(self, message):
        # Die Basisklasse Exception initialisieren
        super().__init__(message)
