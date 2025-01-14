import os
from datetime import datetime 
import re

class File():
    def __init__(self,p_path,dir):
        self.__p_path = p_path
        self.__dir = dir
        self.path = self.createPath()
        self.size = self.createSize()
        self.accessTime = self.createAccessTime()
        self.modificationTime = self.createModificationTime()
        self.changeTime = self.createChangeTime()
        self.UID = self.createUID()
        self.GID = self.createGID()
        self.link = self.createLink()
        self.INode = self.createINode()
        self.deviceID = self.createDeviceID()
        self.extention = self.createExtention()
        pass

    def createPath(self):
        return os.path.join(self.p_path, self.dir)
    def createRechte(self):
        return
    def createSize(self):
        return
    def createAccessTime(self):
        return
    def createChangeTime(self):
        return
    def createModificationTime(self):
        return
    def createUID(self):
        return
    def createGID(self):
        return
    def createLink(self):
        return
    def createINode(self):
        return
    def createDeviceID(self):
        return
    def createExtention(self):
        match = re.search(r'\.([^\s.]+)$', fn)
        if match:
            return f".{match.group(1)}"
        return ""
    
    def display_info(self):
        '''Zeigt die Datei-Informationen an.'''
        print(f"File: {self.file_name}")
        print(f"  Path: {self.path}")
        print(f"  Extension: {self.extension}")
        print(f"  Size: {self.size} bytes")
        print(f"  Access Time: {self.access_time}")
        print(f"  Modification Time: {self.modification_time}")
        print(f"  Change Time: {self.change_time}")
        print()