from htmlWidget import htmlWidget
from tools import isUrl
class Link(htmlWidget):
    def __init__(self) -> None:
        self.link=""
        self.text=""
        self.header="<a>"
        self.footer="</a>"
        self.CustomHeader=False
        self.options:list[str]=list[str]()
        self.style:list[str]=list[str]()
    def addUrl(self,link:str,force:bool=False)->None:
        '''
        Add the url for the link
        '''
        if isUrl(link):
            self.options.append(f"src=\"{link}\"")
            self.link=link
            self.CustomHeader=True
        else:
            if force:
                self.link=link
                self.options.append(f"src=\"{link}\"")
                self.CustomHeader=True
                return None
            print("Url is not valid, to use anyway set force equal to True")