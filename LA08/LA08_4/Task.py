class Task:
    _pid: int
    _name: str
    _status: str  #! custom type für running | sleep
    _memory_usage: float

    def __init__(self, pid: int, name: str, status: str, memory_usage: float):
        self._pid = pid
        self._name = name
        self._status = status
        self._memory_usage = memory_usage

    def get_pid(self) -> int:
        return self._pid

    def get_name(self) -> str:
        return self._name

    def get_status(self) -> str:
        return self._status

    def get_memory_usage(self) -> float:
        return self._memory_usage
    
