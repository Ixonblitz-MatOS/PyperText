import os
import cv2
from validators import url as urls
def exists(file:str)->bool:return os.path.exists(file)
def isFile(file:str)->bool:return os.path.isfile(file)
def isUrl(url:str)->bool:return urls(url)
def getHeight(image:str)->int:return int(cv2.imread(image).shape[0])
def getWidth(image:str)->int:return int(cv2.imread(image).shape[1])