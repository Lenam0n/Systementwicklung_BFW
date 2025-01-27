from pathlib import Path

def get_file_data(p=None) -> str:
    if(not p):
        raise LookupError("File exsistiert nicht!")
    else:
        data:str = open(p,"r").read()
        if not data:
            raise LookupError("File ist leer!")
        else:
            return data
    
def get_file_path(p:Path):
    #! Kann ich noch file Validation machen
    pass

def Main() -> None:
    print(get_file_data(p=Path.cwd()/"LA06"/"out"/"test.txt"))

if __name__ == "__main__" : Main()
