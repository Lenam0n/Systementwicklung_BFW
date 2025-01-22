# Lösung 2 #* -> Optimiert aber nicht dem Diagramm mehr exakt entsprechend

def println(nachricht: str) -> None: print(nachricht)
punkte: int = 55

if punkte > 90: println("Bestenote")
if punkte > 75: println("Sehr gut")
if punkte > 50: println("Bestanden")
else: println("durchgefallen")

println("tschüss")