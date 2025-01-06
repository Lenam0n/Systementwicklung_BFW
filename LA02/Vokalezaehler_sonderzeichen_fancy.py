import re

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>         Counter Logik             >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def VocalCounterExtended(w):
    result = CheckedText(w)
    zeichen = "aeiouAEIOU.,!?;:()\-_[]"

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

    return counter

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>         Util Functions            >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def Ausgabe(c, v, t):
    print(f"Zeichen: {c}, Typ: {t}, Häufigkeit: {v}")

def CheckedText(a):
    regex = r"[^aeiouAEIOU.,!?;:()\-_]]"
    result = re.sub(regex, "", a)
    return result

def ProcessCounter(c):
    results = []
    for buchstabe, info in c.items():
        if info["count"] > 0:
            results.append({
                "zeichen": buchstabe,
                "count": info["count"],
                "type": info["type"]
            })
    return results

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>           Main Logik              >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def Main():
    print("Willkommen zum Vokale Zähler")
    print("Gebe dafür Text ein, um es zählen zu lassen:")
    inp = input().strip()

    counter = VocalCounterExtended(inp)

    results = ProcessCounter(counter)

    for result in results:
        Ausgabe(result["zeichen"], result["count"], result["type"])

Main()