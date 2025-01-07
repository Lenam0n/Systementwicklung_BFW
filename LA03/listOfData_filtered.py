import os
import re

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>            Ausgaben               >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def ausgabe(d):
    for key, value in d.items():
        print(f"{key}:")
        for sub_key, sub_value in value.items():
            print(f"  {sub_key}: {sub_value}")
        print()

def error_ausgabe(e):
    print(f"{e}")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>       Utility Functions           >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def get_ordner(name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, name)

def get_filepath(p_path, path):
    return os.path.join(p_path, path)

def get_file_extention(fn):
    match = re.search(r'\.([^\s.]+)$', fn)
    if match:
        return f".{match.group(1)}"
    return ""

def get_vaild_file(type,data):
    return {k:v for k, v in data.items() if v.get("Extention") == type}


def list_items(base_path, items):
    dic = {
        item: {
            "Path": get_filepath(base_path, item),
            "Size": os.stat(get_filepath(base_path, item)).st_size,
            "Extention" : get_file_extention(item).strip()
        }
        for item in items
    }
    return dic


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#* >>>           Main Logik              >>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def Main():
    try:
        path = get_ordner("test_ordner")
        extention = ".txt"
        #? Text eingabe für den Nutzer einfügen statt extention fest festlegen
        if not os.path.exists(path):
            raise LookupError("Angegebender Ordner gibt es nicht!")
        else:
            items = os.listdir(path)
            result = list_items(path, items)
            ausgabe(get_vaild_file(extention,result))
            
    except LookupError as e:
        error_ausgabe(e)

#! >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Main()
