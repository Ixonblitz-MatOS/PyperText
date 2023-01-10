# pylint: disable=locally-disabled, super-init-not-called, broad-except, unspecified-encoding,attribute-defined-outside-init,import-error

import os
import cv2#type:ignore
from validators import url as urls#type:ignore
from .htmlWidget import htmlObject
def exists(file:str)->bool:return os.path.exists(file)
def isFile(file:str)->bool:return os.path.isfile(file)
def isUrl(url:str)->bool:return urls(url)
def getHeight(image:str)->int:return int(cv2.imread(image).shape[0])
def getWidth(image:str)->int:return int(cv2.imread(image).shape[1])
def stripLast(string:str)->str:return string.rstrip(string[-1])
class SuspendedString(htmlObject):
    '''
    Class to hold suspended string to be properly handled if printed or if returned in str
    '''
    def __init__(self,header:str,val:str,footer:str) -> None:
        self.header: str=header
        self.footer: str=footer
        self.value: str=val
    def form(self) -> str:
        '''
        Passes Suspended Value        
        '''
        return self.header+self.value+self.footer
    def __str__(self) -> str:return self.value
    def __repr__(self)->str:return self.value
    