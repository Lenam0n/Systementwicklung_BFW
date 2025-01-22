import random

# Initialisierung
anz = 1
zahl = random.randint(1, 6)  # Erstes Würfeln

# Schleife: Würfeln, bis eine 6 fällt
while zahl != 6:
    anz += 1
    zahl = random.randint(1, 6)  # Würfeln erneut

# Ausgabe der Anzahl der Würfe
print("Anzahl der Würfe:", anz)
