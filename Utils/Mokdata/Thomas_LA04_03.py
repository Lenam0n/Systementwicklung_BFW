import os
import random
import string
import datetime

def count_vowels(text):
    anzahl_vokale = 0
    for buchstabe in text:
        if buchstabe.lower() in "aeiou":
            anzahl_vokale += 1
    return anzahl_vokale

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)

        # Nur Dateien rausfiltern
        files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
        return files
    except FileNotFoundError:
        print(f"Ordner '{folder_path}' existiert nicht oder ist ungültig.")
        return []

def get_files_with_sizes(folder_path):
    files = list_files_in_folder(folder_path)
    file_sizes = {}
    for file in files:
        full_path = os.path.join(folder_path, file)
        file_sizes[file] = os.path.getsize(full_path)
    return file_sizes

def filter_files_by_extension(file_dict, extension):
    filtered = {}
    for filename, size in file_dict.items():
        if filename.lower().endswith(extension.lower()):
            filtered[filename] = size
    return filtered

def password_generator(length, use_special_chars=True):
    """
    Generate a random password with uppercase, lowercase, numbers, and optional special characters.
    
    :param length: Length of the password to be generated
    :param use_special_chars: Boolean indicating whether to include special characters
    :return: Generated password as a string
    """
    if length < 12 or length > 30:
        return "Password length must be between 12 and 30 characters."

    # Character sets for the password
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation if use_special_chars else ""

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits)
    ]

    if use_special_chars:
        password.append(random.choice(special_characters))

    # Combine all allowed character sets
    all_characters = uppercase + lowercase + digits + special_characters

    # Fill the rest of the password length with random choices from allowed character sets
    while len(password) < length:
        password.append(random.choice(all_characters))

    # Shuffle the password to make it random
    random.shuffle(password)

    return ''.join(password)

def main():
    while True:
        print("\nWählen Sie eine Funktion:")
        print("1. Vokalzähler")
        print("2. Dateien in einem Ordner auflisten")
        print("3. Dateigrößen anzeigen")
        print("4. Dateien nach Endung filtern")
        print("5. Passwortgenerator")
        print("6. Beenden")

        choice = input("Ihre Wahl: ")

        if choice == "1":
            text = input("Gib einen Text ein: ")
            vokale = count_vowels(text)
            print(f"Anzahl der Vokale in deinem Text: {vokale}")

        elif choice == "2":
            folder = input("Gib einen Ordnerpfad ein: ")
            files = list_files_in_folder(folder)
            if files:
                print("Dateien in Ordner:", files)
            else:
                print("Keine Dateien gefunden oder Ordner nicht vorhanden.")

        elif choice == "3":
            folder = input("Gib einen Ordnerpfad ein: ")
            file_sizes = get_files_with_sizes(folder)
            if file_sizes:
                print("Dateigrößen:", file_sizes)
            else:
                print("Keine Dateien gefunden oder Ordner nicht vorhanden.")

        elif choice == "4":
            folder = input("Gib einen Ordnerpfad ein: ")
            file_sizes = get_files_with_sizes(folder)
            if file_sizes:
                extension = input("Welche Endung möchtest du filtern (z. B. .txt)? ")
                filtered = filter_files_by_extension(file_sizes, extension)
                print(f"Gefilterte Dateien ({extension}):", filtered)
            else:
                print("Keine Dateien gefunden oder Ordner nicht vorhanden.")

        elif choice == "5":
            length = 0
            while length < 12 or length > 30:
                try:
                    length = int(input("Enter the desired password length (minimum 12, maximum 30): "))
                    if length < 12 or length > 30:
                        print("Password length must be between 12 and 30 characters.")
                except ValueError:
                    print("Bitte geben Sie eine gültige Zahl ein.")

            use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"
            
            # Get the current timestamp
            timestamp = datetime.datetime.now()
            print(f"Password generated on: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
            print("Generated password:", password_generator(length, use_special_chars))

        elif choice == "6":
            print("Programm beendet.")
            break

        else:
            print("Ungültige Auswahl. Bitte versuchen Sie es erneut.")

if __name__ == "__main__":
    main()
