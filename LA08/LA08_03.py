"""
# 3) System-Prozesse abrufen

## Entwickeln Sie eine Funktion, welche die aktuell laufenden Prozesse des Systems und zugehörige Daten enthält.

> Finden Sie hierfür ein entsprechend sinnvolles Python-Modul.
"""

import psutil


def Main() -> None:
    for process in psutil.process_iter(
        ["pid", "name", "status", "memory_info", "memory_percent"]
    ):
        print(process.info)


if __name__ == "__main__":
    Main()
