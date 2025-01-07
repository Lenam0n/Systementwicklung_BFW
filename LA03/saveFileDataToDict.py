import os


def ausgabe(d):
    for key, value in d.items():
        print(f"{key}:")
        for sub_key, sub_value in value.items():
            print(f"  {sub_key}: {sub_value}")
        print()

def get_ordner(name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, name)

def get_filepath(p_path, path):
    return os.path.join(p_path, path)



def list_items(base_path, items):
    dic = {
        item: {
            "Path": get_filepath(base_path, item),
            "Size": os.stat(get_filepath(base_path, item)).st_size
        }
        for item in items
    }
    return dic

def Main():
    path = get_ordner("test_ordner")
    if os.path.exists(path):
        items = os.listdir(path)
        result = list_items(path, items)
        ausgabe(result)
    else:
        print("Pfad gibt es nicht!")

Main()
