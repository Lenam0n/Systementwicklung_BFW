import psutil
import json
from Task import Task


class Taskmanager:
    _processList: list[Task]

    def __init__(self):
        self._processList = []
        self._initiate()

    def _initiate(self) -> None:

        self._processList = [
            Task(
                pid=process.info["pid"],
                name=process.info["name"],
                status=process.info["status"],
                memory_usage=process.info["memory_percent"],
            )
            for process in psutil.process_iter(
                ["pid", "name", "status", "memory_percent"]
            )
        ]

    def export(self, type: str) -> None:
        from os import getcwd
        from os.path import join

        data = self._prepare_export_tasklist()
        sucsess: bool | None = None
        match (type.lower()):
            case "json":
                sucsess = self._export_to_json(
                    data=data,
                    filename="test",
                    extention="json",
                    path=join(getcwd(), "LA08", "LA08_5"),
                    dir="out",
                    mode="x",
                )
            case _:
                print("Invalid type")  #! ändern zu error

        if sucsess:
            print(f"Export der {type} File war erfolgreich!")
        else:
            print(f"Export der {type} File hat fehlgeschlagen!")

    def _prepare_export_tasklist(self) -> dict[str, dict[str | int | float]]:
        export_dict = {}
        for p in self._processList:
            export_dict[p.get_name()] = {
                "name": p.get_name(),
                "pid": p.get_pid(),
                "status": p.get_status(),
                "memory_usage": p.get_memory_usage(),
            }
        return export_dict

    def _export_to_json(
        self,
        data: dict,
        filename: str,
        extention: str,
        path: str,
        dir: str,
        mode: str | None = None,
    ) -> bool:
        """Speichert ein Dictionary als JSON-Datei."""
        from os.path import join, exists
        from os import makedirs
        from Utils.UtilFunctions.errorUtils import error_ausgabe

        dir_path = join(path, dir)
        if not exists(dir_path):
            makedirs(name=dir_path, exist_ok=False)
        filepath = filepath = join(path, dir, f"{filename}.{extention}")
        try:
            if not mode:
                raise AttributeError("Fileverarbeitungsmodus wurde nicht mitgegeben!")

            else:
                with open(file=filepath, mode=mode.lower(), encoding="utf-8") as file:
                    json.dump(data, file, indent=4, ensure_ascii=True)
                return True

        except Exception as e:
            error_ausgabe(e)
            return False

    def ausgabe(self) -> None:
        for index, p in enumerate(self._processList):
            print("~" * 40)
            print(f"Name: {p.get_name()}")
            print("~" * 40)
            print(" " * 3, f"Process ID: {p.get_pid()}")
            print(" " * 3, f"Status: {p.get_status()}")
            print(" " * 3, f"Memory Usage: {p.get_memory_usage()}")
            if index == len(self._processList) - 1:
                print()
