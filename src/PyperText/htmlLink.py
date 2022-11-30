from PyperText.htmlWidget import htmlWidget
from PyperText.tools import isUrl,SuspendedString
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
            self.options.append(f"href=\"{link}\"")
            self.link=link
            self.CustomHeader=True
        else:
            if force:
                self.link=link
                self.options.append(f"href=\"{link}\"")
                self.CustomHeader:bool=True
                return None
            print("Url is not valid, to use anyway set force equal to True")
    def setText(self,text:str|SuspendedString)->None:
        '''
        Add text to show for the Link
        '''
        if type(text) is str:self.text:str=text
        else:self.text=text.form()#type:ignore
    def setTextColor(self,color:str)->None:
        '''
        Sets color of the link text
        '''
        self.style.append(f"color:{color};")
        self.CustomHeader=True
    def setBackgroundColor(self,color:str)->None:
        '''
        Set the background color
        '''
        self.style.append(f"background-color:{color};")
        self.CustomHeader=True
    def addTarget(self,target:str)->None:
        '''
        Sets where the link is loaded:
        _blank = new tab or window
        _self = in same frame it was clicked
        _parent = in parent frame
        _top = opens in full body of the window
        {name of iframe}**Not Implemented
        '''
        t: list[str]=["_blank","_self","_parent","_top"]
        if target not in t:
            print("Target is either incorrect or not implemented(if you used an iframe name)")
            return None
        self.options.append(f"target=\"{target}\"")