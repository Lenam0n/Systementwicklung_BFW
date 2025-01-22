# Lösung 3
#* Noch weiter entfehrnt vom Diagramm
def println(nachricht: str) -> None: print(nachricht)

punkte: int = 55

if punkte > 90:
    println("Bestenote")
    println("Sehr gut")
    println("Bestanden")
elif punkte > 75:
    println("Sehr gut")
    println("Bestanden")
elif punkte > 50:
    println("Bestanden")
else:
    println("durchgefallen")

println("tschüss")