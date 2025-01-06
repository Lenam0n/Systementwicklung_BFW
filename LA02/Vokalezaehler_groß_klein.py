import re

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>         Counter Logik             >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def VocalCounter(a):
    result = CheckedText(a)
    counter:int = len(result)
    return counter

def VocalCounterExtended(w):
    result = CheckedText(w)
    counter_a:int = 0
    counter_e:int = 0
    counter_i:int = 0
    counter_o:int = 0
    counter_u:int = 0
    counter_A:int = 0
    counter_E:int = 0
    counter_I:int = 0
    counter_O:int = 0
    counter_U:int = 0

    for i in result:
        if(i == "a"):
            counter_a = counter_a +1
            continue
        elif(i == "e"):
            counter_e = counter_e +1
            continue
        elif(i == "i"):
            counter_i = counter_i +1
            continue
        elif(i == "o"):
            counter_o = counter_o +1
            continue
        elif(i == "u"):
            counter_u = counter_u +1
            continue
        elif(i == "A"):
            counter_A = counter_A +1
            continue
        elif(i == "E"):
            counter_E = counter_E +1
            continue
        elif(i == "I"):
            counter_I = counter_I +1
            continue
        elif(i == "O"):
            counter_O = counter_O +1
            continue
        elif(i == "U"):
            counter_U = counter_U +1
            continue

    if counter_a != 0: Ausgabe("a",counter_a)
    if counter_e != 0: Ausgabe("e",counter_e)
    if counter_i != 0: Ausgabe("i",counter_i)
    if counter_o != 0: Ausgabe("o",counter_o)
    if counter_u != 0: Ausgabe("u",counter_u)
    if counter_A != 0: Ausgabe("A",counter_A)
    if counter_E != 0: Ausgabe("E",counter_E)
    if counter_I != 0: Ausgabe("I",counter_I)
    if counter_O != 0: Ausgabe("O",counter_O)
    if counter_U != 0: Ausgabe("U",counter_U)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>         Util Functions            >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def Ausgabe(v,c):
    print(f"{c} : {v}")

def CheckedText(a):
    regex = r"[^aeiouAEIOU]"
    result = re.sub(regex, "", a)
    return result


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>           Main Logik              >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def Main():
    print("Wilkommen zum Vokale Zähler")
    print("Gebe dafür Text ein um es zählen zu lassen:")
    inp = input().strip()
    #result = VocalCounter(inp)
    #print(result)
    result = VocalCounterExtended(inp)

Main()