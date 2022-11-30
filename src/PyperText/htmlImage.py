from htmlWidget import htmlWidget
from tools import exists
class Image(htmlWidget):
    def __init__(self,path:str)->None:
        if exists(path):self.file=path
        else:
            try:open(path,'x')
            except:
                print("Cannot create the file and file does not exist")
                quit(1)
        self.text=""
        self.options:list[str]=list[str]()
        self.style:list[str]=list[str]()
        self.header="<img>"
        self.footer="</img>"
        self.CustomHeader=False
    def setAlternativeText(self,text:str)->None:
        '''
        Set text for if image fails to load.
        '''
        self.text=text