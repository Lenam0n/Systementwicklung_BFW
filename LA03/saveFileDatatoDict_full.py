import os
from datetime import datetime
import re

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

def get_file_extention(fn):
    match = re.search(r'\.([^\s.]+)$', fn)
    if match:
        return f".{match.group(1)}"
    return ""

def list_items(base_path, items):
    dic = {
        item: {
            "Path": get_filepath(base_path, item),
            "Rechte": os.stat(get_filepath(base_path, item)).st_mode,
            "Size": os.stat(get_filepath(base_path, item)).st_size,
            "Access Time": datetime.fromtimestamp(os.stat(get_filepath(base_path, item)).st_atime),
            "Modification Time": datetime.fromtimestamp(os.stat(get_filepath(base_path, item)).st_mtime),
            "Change Time": datetime.fromtimestamp(os.stat(get_filepath(base_path, item)).st_ctime),
            "User ID": os.stat(get_filepath(base_path, item)).st_uid,
            "Gruppen ID": os.stat(get_filepath(base_path, item)).st_gid,
            "Verknüpfungen": os.stat(get_filepath(base_path, item)).st_nlink,
            "INode": os.stat(get_filepath(base_path, item)).st_ino,
            "Geräte ID": os.stat(get_filepath(base_path, item)).st_dev,
            "Extention" : get_file_extention(item).strip()
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

Main()
