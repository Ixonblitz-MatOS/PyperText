from htmlWidget import htmlWidget
class Textbox(htmlWidget):
    '''
    HTML Textbox Class derived from htmlWidget
    '''
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
                if i.__includes__("style"):self.style=i.split("style=")[1].split(";")  # type: ignore
                else:continue
        del self.options[self.options.index("style")]
        for i in final:final+=i+" "
        return final
    def _buildStyle(self)->str:
        final=""
        for i in final:final+=i
        return final
    def finalize(self)->None:
        '''
        Finalizes code to self.code
        '''
        if self.CustomHeader:
            print("Finalizing with Custom Header")
            self.code=self.header[-1]+self._buildOptions()+f" style=\"{self._buildStyle()}\">"+self.text+self.footer
        else:
            print("Finalizing with Default Header")
            self.code=self.header+self.text+self.footer