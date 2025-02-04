"""
# 5) Daten exportieren

## Ergänzen Sie die Klasse Task Manager um eine Methode, die die Liste aller Prozesse in eine JSON-Datei exportiert.
"""

from Taskmanager import Taskmanager

Tm = Taskmanager()
# Tm.ausgabe()
Tm.export("json")
