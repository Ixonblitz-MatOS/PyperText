"""
Link object
"""
# pylint: disable=locally-disabled, line-too-long,invalid-name, super-init-not-called, broad-except, unspecified-encoding,attribute-defined-outside-init
from typing import Any,Type,Callable
from ultraimport.ultraimport import ultraimport

Class=Any|Type[type]
htmlWidget=ultraimport('__dir__/htmlWidget.py','htmlWidget')
SuspendedString,isUrl=ultraimport('__dir__/tools.py',{'SuspendedString':Class,"isUrl":Callable})

class Link(htmlWidget):
    """
    Link object for PyperText
    """
    code=""
    type="Link"
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
            print("Link: Url is not valid, to use anyway set force equal to True")
    def setText(self,text:str|SuspendedString)->None:
        '''
        Add text to show for the Link
        '''
        if isinstance(text,str):
            self.text:str=text
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
            print("Link: Target is either incorrect or not implemented(if you used an iframe name)")
            return None
        self.options.append(f"target=\"{target}\"")
    def _buildStyle(self)->str:
        final=""
        if "style" in self.options:
            for i in self.options:
                if i.__includes__("style"):
                    self.style=i.split("style=")[1].split(";")  # type: ignore
                    for i in self.style:
                        i+=";"
                else:continue
            del self.options[self.options.index("style")]
        for i in final:
            if i.endswith(";"):
                final+=i
            else:final+=i+";"
        return final
    def _buildOptions(self)->None:
        '''
        build text to alt
        '''
        self.options.append(f"alt=\"{self.text}\"")
    def finalize(self)->None:
        '''
        Finalize the Image to self.code
        '''
        if self.CustomHeader:
            print("Link: Creating Link with Custom Header")
            if self._buildStyle() =="" or self._buildStyle()==" ":
                self.code=self.header.rstrip(self.header[-1])+f" {self._buildOptions()}>"
            else:
                self.code=self.header.rstrip(self.header[-1])+ f"style=\"{self._buildOptions()}\" {self._buildOptions()}>"
        else:
            print("Link: Creating Link with Default Header")
            self.code=self.header+self.text+self.footer

if __name__=="__main__":
    pass
