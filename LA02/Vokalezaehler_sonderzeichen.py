import re

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>         Counter Logik             >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def VocalCounterExtended(w):
    result = CheckedText(w)
    zeichen = "aeiouAEIOU.,!?;:()\-_[]"

    '''
    counter = {
    b: {
        "count": 0,
        "type": "Buchstabe" if b.lower() in "aeiou" else "Sonderzeichen"
    }
    for b in zeichen
}

for char in result:
    if char in counter:
        counter[char]["count"] += 1

# Ausgabe der Ergebnisse
for buchstabe, info in counter.items():
    if info["count"] > 0:
        Ausgabe(buchstabe, info['count'], info['type']) 
    '''

    counter = {b: 0 for b in zeichen}

    for char in result:
        if char in counter:
            counter[char] += 1

    for buchstabe, count in counter.items():
        if count > 0:
            Ausgabe(buchstabe, count) 
            

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>         Util Functions            >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def Ausgabe(c,v):
    print(f"Zeichen [{c}] : {v} mal")
    #f"Zeichen: {c}, Typ: {info['t']}, Häufigkeit: {info['v']}"

def CheckedText(a):
    regex = r"[^aeiouAEIOU.,!?;:()\-_]]"
    result = re.sub(regex, "", a)
    return result


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>           Main Logik              >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def Main():
    print("Wilkommen zum Vokale Zähler")
    print("Gebe dafür Text ein um es zählen zu lassen:")
    inp = input().strip()
    result = VocalCounterExtended(inp)

Main()