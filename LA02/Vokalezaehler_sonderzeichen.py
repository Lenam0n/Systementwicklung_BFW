import re

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>         Counter Logik             >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def VocalCounterExtended(w):
    result = CheckedText(w)
    zeichen = "aeiouAEIOU.,!?;:()\-_[]"

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
    VocalCounterExtended(inp)

Main()
