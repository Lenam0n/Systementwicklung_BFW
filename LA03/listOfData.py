import os

def ausgabe(d):
    for e in d:
        print(f"{e}")

def get_ordner(name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, name)

def Main():
    path = get_ordner("test_ordner")
    if os.path.exists(path):
        ausgabe(os.listdir(path))

Main()