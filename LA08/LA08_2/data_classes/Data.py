class Data ():
    _path:str
    _size:any
    _extention:str
    def __init__(
                    self,
                    path:str | None, 
                    size:any, 
                    extention:str | None
                ):
        self._path = path
        self._size = size
        self._extention = extention

    def get_path(self) -> str: return self._path
    def get_size(self) -> str: return self._size
    def get_extention(self) -> str: return self._extention
    
    def set_path(self,p:str) -> None: self._path = p
    def set_size(self,s:bytes) -> None: self._size = s
    def set_extention(self,ex:str) -> None: self._extention = ex
    