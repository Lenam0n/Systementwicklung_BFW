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

    for i in result:
        if(i == "a"):
            counter_a = counter_a +1
        elif(i == "e"):
            counter_e = counter_e +1
        elif(i == "i"):
            counter_i = counter_i +1
        elif(i == "o"):
            counter_o = counter_o +1
        elif(i == "u"):
            counter_u = counter_u +1


    if counter_a != 0: Ausgabe("a",counter_a)
    if counter_e != 0: Ausgabe("e",counter_e)
    if counter_i != 0: Ausgabe("i",counter_i)
    if counter_o != 0: Ausgabe("o",counter_o)
    if counter_u != 0: Ausgabe("u",counter_u)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>         Util Functions            >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def Ausgabe(c,v):
    print(f"Buchstabe [{c}] : {v} Mal")

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
    inp = input().strip().lower()
   #result = VocalCounter(inp)
    result = VocalCounterExtended(inp)
    #print(result)

Main()