import psutil
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
                # ? Es gibt die Memory Usage aus in richtiger Ausgabe aber es ist Prozent und dem entsprechend nicht so viel.
                # ? Aktuell Stand Test wäre es 59,49% die benutzt werden.
            )
            for process in psutil.process_iter(
                ["pid", "name", "status", "memory_percent"]
            )
        ]

    def ausgabe(self) -> None:
        for index, p in enumerate(self._processList):
            print("~" * 40)
            print(f"Name: {p.get_name()}")
            print("~" * 40)
            print(" " * 3, f"Process ID: {p.get_pid()}")
            print(" " * 3, f"Status: {p.get_status()}")
            print(" " * 3, f"Memory Usage: {p.get_formated_memory_usage()}")
            if index == len(self._processList) - 1:
                print()

    def test(self):
        sum: int = 0
        for p in self._processList:
            sum += p.get_memory_usage()
        return sum
