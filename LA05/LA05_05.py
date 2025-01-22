# Lösung 1 #* -> Am nähsten dran

def println(nachricht: str) -> None: print(nachricht)

punkte: int = 55

if punkte > 90: println("Bestenote")
else:
    if punkte > 75: println("Sehr gut")
    else:
        if punkte > 50: println("Bestanden")
        else: println("durchgefallen")

println("tschüss")