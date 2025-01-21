def println(nachricht: str) -> None:
    print(nachricht)

punkte: int = 55

if punkte > 90:
    println("Bestenote")

if punkte > 75:
    println("Sehr gut")

if punkte > 50:
    println("Bestanden")
else:
    println("durchgefallen")

println("tschüss")


'''
#? so wäre das Diagramm aber ist das nicht extrem Redundant?

def println(nachricht: str) -> None: print(nachricht)

punkte: int = 55

if punkte > 90:
    println("Bestenote")
    println("Sehr gut")
    println("Bestanden")
else:
    if punkte > 75:
        println("Sehr gut")
        println("Bestanden")
    else:
        if punkte > 50:
            println("Bestanden")
        else:
            println("durchgefallen")

println("tschüss")

#! -------------------------------------------------------------------------


def println(nachricht: str) -> None:
    print(nachricht)

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

'''