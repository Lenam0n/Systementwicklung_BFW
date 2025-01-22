import os

def load_ignore_list(file_path):
    """Lädt ignorierte Ordner und Dateien aus einer strukturierten Ignore-Datei."""
    ignored_folders = set()
    ignored_files = set()

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            section = None
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):  # Kommentare ignorieren
                    continue
                
                if line == "[folders]":
                    section = "folders"
                elif line == "[files]":
                    section = "files"
                elif section == "folders":
                    ignored_folders.add(line)
                elif section == "files":
                    ignored_files.add(line)

    return ignored_folders, ignored_files

def build_directory_tree(root_dir, ignored_folders):
    """Erstellt eine rekursive Dictionary-Struktur der Verzeichnisse ab root_dir."""
    tree = {}

    for root, dirs, _ in os.walk(root_dir, topdown=True):
        # Entferne ignorierte Ordner (inkl. Unterverzeichnisse)
        dirs[:] = [d for d in dirs if os.path.join(root, d) not in [os.path.join(root_dir, f) for f in ignored_folders]]

        # Relativen Pfad **ab dem CWD** berechnen
        rel_path = os.path.relpath(root, root_dir)
        if rel_path == ".":
            continue  # CWD selbst nicht in das Tree-Dict aufnehmen

        # Aktuelle Position im Dictionary finden
        node = tree
        path_parts = rel_path.split(os.sep)
        for part in path_parts:
            node = node.setdefault(part, {})

        # Füge leere Dicts für Subdirectories hinzu
        for subdir in dirs:
            node[subdir] = {}

    return tree

def print_directory_tree(tree, first=True):
    """Gibt die Verzeichnisstruktur rekursiv in der gewünschten Form aus."""
    keys = list(tree.keys())

    if first:
        print("\n📂 Verzeichnisstruktur:")

    for index, parent in enumerate(keys):
        if not first:
            print("-" * 40)  # Trennlinie **oberhalb** des Hauptordners

        print(f"📁 {parent}")

        if tree[parent]:  # Falls es Subordner gibt, rekursiv aufrufen
            print_subdirectory_tree(tree[parent], indent=4)

        first = False  # Danach keine "Verzeichnisstruktur" mehr ausgeben

def print_subdirectory_tree(subtree, indent=4):
    """Rekursive Hilfsfunktion für die Ausgabe von Unterordnern."""
    for sub, subdirs in subtree.items():
        print(" " * indent + f"📁 {sub}")
        if subdirs:
            print_subdirectory_tree(subdirs, indent + 4)
        else:
            print(" " * (indent + 4) + "📂 Keine weiteren Subordner")

def get_dir_structure():
    cwd = os.getcwd()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ignore_file = os.path.join(script_dir, ".ignore_dirs")

    ignored_folders, ignored_files = load_ignore_list(ignore_file)
    dir_tree = build_directory_tree(cwd, ignored_folders)

    # **Nur die Hauptstruktur ab CWD ausgeben**
    print_directory_tree(dir_tree, first=True)

if __name__ == "__main__": get_dir_structure()