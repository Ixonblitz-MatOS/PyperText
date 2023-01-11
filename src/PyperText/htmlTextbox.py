"""
Textbox Widget
"""
# pylint: disable=locally-disabled, invalid-name, line-too-long, super-init-not-called, broad-except, unspecified-encoding,attribute-defined-outside-init
from ultraimport.ultraimport import ultraimport
htmlWidget=ultraimport('__dir__/htmlWidget.py','htmlWidget')
class Textbox(htmlWidget):
    '''
    HTML Textbox Class derived from htmlWidget
    '''
    code=""
    type="Textbox"
    def __init__(self) -> None:
        self.options:list[str]=list[str]()
        self.style:list[str]=list[str]()
        self.text:str=""
        self.CustomHeader:bool=False
        self.header:str="<textarea>"
        self.footer:str="</textarea>"
    def addCustomOption(self,option:str)->None:
        '''
        Add option not implemented yet
        Requires no editing before script
        '''
        self.options.append(option)
        self.CustomHeader=True
    def setText(self,text:str)->None:
        '''
        Set the Textbox text
        '''
        self.text=text
    def setSize(self,cols:str|int,rows:str|int)->None:
        '''
        Set the size of textbox
        '''
        self.options.append(f"cols=\"{str(cols)}\" rows=\"{str(rows)}\"")
        self.CustomHeader=True
    def changeTextColor(self,color:str)->None:
        '''
        Set the color of the text
        '''
        self.style.append(f"color:{color};")
        self.CustomHeader=True
    def changeBackgroundColor(self,color:str)->None:
        '''
        Set the background of the textbox
        '''
        self.style.append(f"background-color:{color};")
        self.CustomHeader=True
    def setID(self,ids:str)->None:
        '''
        Set the textbox ID
        '''
        self.options.append(f"id=\"{ids}\"")
        self.CustomHeader=True
    def _buildOptions(self)->str:
        final=""
        if "style" in self.options:
            for i in self.options:
                if i.__includes__("style"):
                    self.style=i.split("style=")[1].split(";")[0]#type:ignore
                else:continue
            del self.options[self.options.index("style")]
        for i in self.options:
            final+=i+" "
        return final
    def _buildStyle(self)->str:
        final=""
        for i in final:
            final+=i
        return final
    def finalize(self)->None:
        '''
        Finalizes code to self.code
        '''
        if self.CustomHeader:
            print("Textbox: Creating Textbox with Custom Header")
            if self._buildStyle()=='' or self._buildStyle()==' ':
                self.code=self.header.rstrip(self.header[-1])+f" {self._buildOptions()}>"+self.text+self.footer
            else:
                self.code=self.header.rstrip(self.header[-1])+" "+self._buildOptions()+f" style=\"{self._buildStyle()}\">"+self.text+self.footer
        else:
            print("Textbox: Creating Textbox with Default Header")
            self.code=self.header+self.text+self.footer

if __name__=="__main__":
    pass
